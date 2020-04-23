/*==================
SVG Icon Library - Toolbox
	Author & Contributor:
		hugoalh
	Language:
		NodeJS 12
==================*/
const NodeJS = {
	Console: require("console"),
	FileSystem: require("fs"),
	OperatingSystem: require("os"),
	Path: require("path"),
};
function ReadFile(Address, Encode = "utf8", WhenError = function () {
	process.exit(0);
}) {
	let FileContent;
	try {
		FileContent = NodeJS.FileSystem.readFileSync(
			Address,
			{
				encoding: Encode,
				flag: "r"
			}
		);
	} catch (error) {
		NodeJS.Console.error(error);
		WhenError();
	};
	return FileContent;
};
function WriteFile(Address, Content, Encode = "utf8", WhenError = function () {
	process.exit(0);
}) {
	try {
		NodeJS.FileSystem.writeFileSync(
			Address,
			Content,
			{
				encoding: Encode,
				flag: "w"
			}
		);
	} catch (error) {
		NodeJS.Console.error(error);
		WhenError();
	};
};
const Configuration = JSON.parse(
	ReadFile(
		NodeJS.Path.join(__dirname, "Toolbox_Configuration.json")
	)
);
Configuration["Root"] = NodeJS.Path.join(__dirname, Configuration["Root"]);
Configuration["Minify"].forEach((value, index) => {
	Configuration["Minify"][index] = Configuration["Minify"][index].replace(new RegExp("\r\n", "gu"), "\n").replace(new RegExp("\n", "gu"), "\r\n"), "gu";
	Configuration["Minify"][index] = new RegExp(Configuration["Minify"][index].replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&"));
});
function DetermineIsIgnoreDirectory(Path) {
	for (let index = 0; index < Configuration["Ignore"]["Directory"].length; index++) {
		if (Path.search(Configuration["Ignore"]["Directory"][index]) == 0) {
			return true;
		};
	};
	return false;
};
function DetermineIsIgnoreFile(Path) {
	if (Path.length <= ".svg".length) {
		return true;
	};
	if (Path.search(".svg") != (Path.length - ".svg".length)) {
		return true;
	};
	if (Path.search("_") == 0) {
		return true;
	};
	for (let index = 0; index < Configuration["Ignore"]["File"].length; index++) {
		if (Path.search(Configuration["Ignore"]["File"][index]) == 0) {
			return true;
		};
	};
	return false;
};
function DetermineIsDirectory(Path) {
	const Stat = NodeJS.FileSystem.lstatSync(
		NodeJS.Path.join(Configuration["Root"], Path)
	);
	return Stat.isDirectory();
};
function ReadDirectory(Path) {
	const List = NodeJS.FileSystem.readdirSync(
		NodeJS.Path.join(Configuration["Root"], Path),
		{
			encoding: "utf8",
			withFileTypes: false
		}
	);
	const Result = {
		"Directories": [],
		"Files": []
	};
	List.forEach((value, index) => {
		const RDPath = NodeJS.Path.join(Path, value);
		if (DetermineIsDirectory(RDPath) == true && DetermineIsIgnoreDirectory(RDPath) == false) {
			Result["Directories"].push(RDPath);
		} else if (DetermineIsIgnoreFile(RDPath) == false) {
			Result["Files"].push(RDPath);
		};
	});
	return Result;
};
function FullReadDirectory() {
	let WaitingDirectories = [""];
	let Files = [];
	while (WaitingDirectories.length > 0) {
		let CurrentDirectory = WaitingDirectories.shift();
		let Result = ReadDirectory(CurrentDirectory);
		Files.push(...Result["Files"]);
		WaitingDirectories.push(...Result["Directories"]);
	};
	return Files;
};
Configuration["FileList"] = FullReadDirectory();

/*::::::::
Check Valid
::::::::*/
try {
	Configuration["ValidFileContent"] = ReadFile(
		NodeJS.Path.join(Configuration["Root"], Configuration["Template"])
	);
	Configuration["ValidFilePattern"] = Configuration["ValidFileContent"].replace("\r\n</svg>\r\n", "");
} catch (error) {
	NodeJS.Console.error(error);
};
const InvalidSVGFileList = {};
Promise.allSettled(
	Configuration["FileList"].map((value, index) => {
		new Promise((resolve, reject) => {
			const FileFullPath = NodeJS.Path.join(Configuration["Root"], value);
			let FileContent = ReadFile(
				NodeJS.Path.join(Configuration["Root"], value)
			);
			InvalidSVGFileList[value] = [];
			for (let index = 0; index < Configuration["Minify"].length; index++) {
				if (FileContent.search(Configuration["Minify"][index]) != -1) {
					FileContent = FileContent.replace(Configuration["Minify"][index], "");
					WriteFile(FileFullPath, FileContent);
				};
			};
			if (FileContent == Configuration["ValidFileContent"]) {
				InvalidSVGFileList[value].push("Null!");
			};
			if (FileContent.search(Configuration["ValidFilePattern"]) != 0) {
				InvalidSVGFileList[value].push("Invalid Pattern!");
			};
			if (FileContent.search("<g>") != -1) {
				InvalidSVGFileList[value].push("Contain Group!");
			};
			if (FileContent.search("<def>") != -1) {
				InvalidSVGFileList[value].push("Contain Function!");
			};
			if (FileContent.search("fill=\"#040000\"") != -1) {
				InvalidSVGFileList[value].push("CMYK!");
			};
			if (InvalidSVGFileList[value].length == 0) {
				delete InvalidSVGFileList[value];
			};
		}).catch((error) => {
		});
	})
);
if (Object.keys(InvalidSVGFileList).length > 0) {
	NodeJS.Console.warn(`Invalid SVG File:
${JSON.stringify(InvalidSVGFileList)}`);
} else {
	NodeJS.Console.log("All SVG file are valid!");
};

/*::::::::
Web View Generate
::::::::*/
function Time_Internal() {
	let Pattern = "%Y%-%MO%-%D% %HH%:%MI%",
		CurrentTime = new Date(),
		InternalData = {};
	Promise.allSettled([
		new Promise((resolve, reject) => {
			InternalData["Y"] = CurrentTime.getUTCFullYear().toString();
		}).catch((error) => {
		}),
		new Promise((resolve, reject) => {
			InternalData["mo"] = CurrentTime.getUTCMonth() + 1;
		}).catch((error) => {
		}),
		new Promise((resolve, reject) => {
			InternalData["d"] = CurrentTime.getUTCDate();
		}).catch((error) => {
		}),
		new Promise((resolve, reject) => {
			InternalData["hh"] = CurrentTime.getUTCHours();
		}).catch((error) => {
		}),
		new Promise((resolve, reject) => {
			InternalData["mi"] = CurrentTime.getUTCMinutes();
		}).catch((error) => {
		})
	]);
	Promise.allSettled([
		new Promise((resolve, reject) => {
			if (InternalData["mo"] >= 1 && InternalData["mo"] <= 9) {
				InternalData["MO"] = `0${InternalData["mo"].toString()}`;
			} else {
				InternalData["MO"] = InternalData["mo"].toString();
			};
		}).catch((error) => {
		}),
		new Promise((resolve, reject) => {
			if (InternalData["d"] >= 1 && InternalData["d"] <= 9) {
				InternalData["D"] = `0${InternalData["d"].toString()}`;
			} else {
				InternalData["D"] = InternalData["d"].toString();
			};
		}).catch((error) => {
		}),
		new Promise((resolve, reject) => {
			if (InternalData["hh"] >= 0 && InternalData["hh"] <= 9) {
				InternalData["HH"] = `0${InternalData["hh"].toString()}`;
			} else {
				InternalData["HH"] = InternalData["hh"].toString();
			};
		}).catch((error) => {
		}),
		new Promise((resolve, reject) => {
			if (InternalData["mi"] >= 0 && InternalData["mi"] <= 9) {
				InternalData["MI"] = `0${InternalData["mi"].toString()}`;
			} else {
				InternalData["MI"] = InternalData["mi"].toString();
			};
		}).catch((error) => {
		})
	]);
	[
		"Y",
		"MO",
		"D",
		"HH",
		"MI",
	].forEach((Directive, index) => {
		Pattern = Pattern.replace(new RegExp(`%${Directive}%`, "gu"), InternalData[Directive]);
	});
	return Pattern;
};
const CurrentUTCTime = Time_Internal();
const DocumentContent = {};
let AwaitingFiles = Configuration["FileList"];
const TotalFileCount = AwaitingFiles.length;
function DocumentContentManualGenerator(InternalCatalog, HeaderString, FindQuery, FindResult) {
	let Content = "",
		ProceededFiles = [];
	AwaitingFiles.forEach((value, index) => {
		if (value.search(FindQuery) == FindResult) {
			const ElementPath = value.replace(new RegExp("\\\\", "gu"), "/");
			const ElementName = ElementPath.replace(".svg", "");
			Content += `<span><span><a href="./${ElementPath}"><img src="./${ElementPath}" /></a><br />${ElementName}</span></span>
`;
			ProceededFiles.push(value);
		}
	});
	DocumentContent[InternalCatalog] = `${HeaderString}
<div class="flex">
${Content}</div>`;
	ProceededFiles.forEach((value, index) => {
		AwaitingFiles.splice(AwaitingFiles.indexOf(value), 1);
	});
};
[
	["General", "<h2>General</h2>", "\\\\", -1],
	["Adobe", "<h2>Adobe</h2>", "Adobe\\\\", 0],
	["Align", "<h2>Align</h2>", "Align\\\\", 0],
	["Arrow", "<h2>Arrow</h2>", "Arrow\\\\", 0],
	["Chess", "<h2>Chess</h2>", "Chess\\\\", 0],
	["Clock", "<h2>Clock</h2>", "Clock\\\\", 0],
	["Dice", "<h2>Dice</h2>", "Dice\\\\", 0],
	["Git", "<h2>Git</h2>", "Git\\\\", 0],
	["Google", "<h2>Google</h2>", "Google\\\\", 0],
	["Input_Chinese", "<h3>Chinese</h3>", "Input\\\\Chinese\\\\", 0],
	["Input_SimplifiedChinese", "<h3>Simplified Chinese</h3>", "Input\\\\SimplifiedChinese\\\\", 0],
	["Input", "<h2>Input</h2>", "Input\\\\", 0],
	["Microsoft", "<h2>Microsoft</h2>", "Microsoft\\\\", 0],
	["Minecraft", "<h2>Minecraft</h2>", "Minecraft\\\\", 0],
	["Navigate", "<h2>Navigate</h2>", "Navigate\\\\", 0],
	["Poker", "<h2>Poker</h2>", "Poker\\\\", 0],
	["Roblox", "<h2>Roblox</h2>", "Roblox\\\\", 0],
	["StepfordCountyRailway", "<h2>Stepford County Railway</h2>", "StepfordCountyRailway\\\\", 0],
	["Triangle", "<h2>Triangle</h2>", "Triangle\\\\", 0]
].forEach((value, index) => {
	const [InternalCatalog, HeaderString, FindQuery, FindResult] = value;
	DocumentContentManualGenerator(InternalCatalog, HeaderString, FindQuery, FindResult);
});
if (AwaitingFiles.length > 0) {
	NodeJS.Console.error("SVG Files are not fully handled by generator, please check the pattern!");
	process.exit(0);
};
let FullDocumentContent = `<!DOCTYPE html>
<html>
	<head>
		<!-- Character Encode --->
		<meta charset="UTF-8" />
		<!-- Security --->
		<meta name="referrer" content="origin-when-cross-origin" />
		<meta name="robots" content="index, follow" />
		<!-- Information --->
		<meta name="application-name" content="SVG Icon Library" />
		<meta name="apple-mobile-web-app-title" content="SVG Icon Library" />
		<meta name="title" content="SVG Icon Library" />
		<meta name="author" content="hugoalh" />
		<meta name="description" content="A SVG icon library." />
		<meta name="keywords" content="library svg svg-icon svg-icons" />
		<!-- Render --->
		<meta dir="auto" />
		<meta autocapitalize="off" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no" />
		<meta name="mobile-web-app-capable" content="yes" />
		<meta name="apple-mobile-web-app-capable" content="yes" />
			<!-- Style --->
			<link rel="stylesheet" href="./index.css" />
		<title>SVG Icon Library</title>
	</head>
	<body>
		<nav id="heroheader" class="framework">
			<div>
				<span class="logo"><img src="./SVG_Alt.svg" /></span>
				<div>
					<span class="title">SVG Icon Library</span>
					<span class="description"><a href="https://github.com/hugoalh">hugoalh</a>/<a href="https://github.com/hugoalh/Library.SVG.Icon">Library.SVG.Icon</a></span>
				</div>
			</div>
		</nav>
		<div id="page" class="framework">
			<div class="information">
				<p><b>Last Updated: </b>${CurrentUTCTime} UTC</p>
				<p><b>Total: </b>${TotalFileCount}</p>
				<p><b>License: </b><a href="https://github.com/hugoalh/Library.SVG.Icon/blob/master/LICENSE.md">CC0 1.0</a></p>
				<p>
					<b>Note:</b><br />
					<ul>
						<li>This may take a while to load completely!</li>
						<li>Use "Find In Page" function to search icons!</li>
					</ul>
				</p>
			</div>
			<div class="content">
${DocumentContent["General"]}
${DocumentContent["Adobe"]}
${DocumentContent["Align"]}
${DocumentContent["Arrow"]}
${DocumentContent["Chess"]}
${DocumentContent["Clock"]}
${DocumentContent["Dice"]}
${DocumentContent["Git"]}
${DocumentContent["Google"]}
${DocumentContent["Input"]}
${DocumentContent["Input_Chinese"]}
${DocumentContent["Input_SimplifiedChinese"]}
${DocumentContent["Microsoft"]}
${DocumentContent["Minecraft"]}
${DocumentContent["Navigate"]}
${DocumentContent["Poker"]}
${DocumentContent["Roblox"]}
${DocumentContent["StepfordCountyRailway"]}
${DocumentContent["Triangle"]}
			</div>
		</div>
	</body>
</html>
`;
FullDocumentContent = FullDocumentContent.replace(new RegExp("\r\n", "gu"), "\n").replace(new RegExp("\n", "gu"), "\r\n");
WriteFile(
	NodeJS.Path.join(Configuration["Root"], Configuration["Export"]["WebView"]),
	FullDocumentContent
);
process.exit(0);
