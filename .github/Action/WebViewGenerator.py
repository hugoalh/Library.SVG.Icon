# ==============================================================================
# SVG Icon Library - Action - Web View Generator
#   Author & Contributor:
#     hugoalh
#   Language:
#     Python 3.8
# ==============================================================================
import os, pathlib, sys, time

# ::::::::::::::::::::::::::::::::::::::
# Data
# ::::::::::::::::::::::::::::::::::::::
CurrentUTCTime = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
PathData = {
	"Repository": str(pathlib.Path(os.path.abspath(__file__)).parent.parent.parent)
}
PathData["Document"] = os.path.join(PathData["Repository"], "index.html")
IgnoreList = {
	"SVGFile": [
		"_Template.svg", "_Template_Disable.svg"
	],
	"Directory": [
		".git", ".github", ".vscode"
	]
}

# ::::::::::::::::::::::::::::::::::::::
# Program - List Data & Get Data
# ::::::::::::::::::::::::::::::::::::::
print("Current UTC Time:", CurrentUTCTime)
print("Path - Repository:", PathData["Repository"])
print("Path - Document:", PathData["Document"])
print("Ignore - SVG File:", IgnoreList["SVGFile"])
print("Ignore - Directory:", IgnoreList["Directory"])
def DetectIsIgnore(InputFileName):
	for Element in IgnoreList["Directory"]:
		if (InputFileName.find(Element) == 0):
			return True
	for Element in IgnoreList["SVGFile"]:
		if (InputFileName.find(Element) == 0):
			return True
	if (InputFileName.find(".svg", len(InputFileName) - len(".svg")) == -1):
		return True
	return False
SVGFileList = []
for Root, Directories, FilesName in os.walk(PathData["Repository"]):
	for FileName in FilesName:
		FileFullPath = os.path.join(Root, FileName).replace(PathData["Repository"] + "\\", "")
		if (DetectIsIgnore(FileFullPath) == False):
			SVGFileList.append(FileFullPath)
print("SVG File:", SVGFileList)
SVGFileCount = str(len(SVGFileList))

# ::::::::::::::::::::::::::::::::::::::
# Program - Generate Document Content
# ::::::::::::::::::::::::::::::::::::::
DocumentContent = {}
def DocumentContentManualGenerator(InternalCatalog, HeaderString, FindQuery, FindResult):
	SVGFileList_Proceeded = []
	DocumentContent[InternalCatalog] = ""
	for Element in SVGFileList:
		ElementPath = Element.replace("\\", "/")
		ElementName = ElementPath.replace(".svg", "")
		if (Element.find(FindQuery) == FindResult):
			DocumentContent[InternalCatalog] = DocumentContent[InternalCatalog] + "<span><span><a href=\"./" + ElementPath + "\"><img src=\"./" + ElementPath + "\" /></a><br />" + ElementName + "</span></span>\n"
			SVGFileList_Proceeded.append(Element)
	DocumentContent[InternalCatalog] = HeaderString + "\n<div class=\"flex\">\n" + DocumentContent[InternalCatalog] + "</div>"
	for Element in SVGFileList_Proceeded:
		SVGFileList.remove(Element)
DocumentContentManualGenerator("General", "<h2>General</h2>", "\\", -1)
DocumentContentManualGenerator("Align", "<h2>Align</h2>", "Align\\", 0)
DocumentContentManualGenerator("Arrow", "<h2>Arrow</h2>", "Arrow\\", 0)
DocumentContentManualGenerator("Chess", "<h2>Chess</h2>", "Chess\\", 0)
DocumentContentManualGenerator("Clock", "<h2>Clock</h2>", "Clock\\", 0)
DocumentContentManualGenerator("Dice", "<h2>Dice</h2>", "Dice\\", 0)
DocumentContentManualGenerator("Input_Chinese", "<h3>Chinese</h3>", "Input\\Chinese\\", 0)
DocumentContentManualGenerator("Input_SimplifiedChinese", "<h3>Simplified Chinese</h3>", "Input\\SimplifiedChinese\\", 0)
DocumentContentManualGenerator("Input", "<h2>Input</h2>", "Input\\", 0)
DocumentContentManualGenerator("Minecraft", "<h2>Minecraft</h2>", "Minecraft\\", 0)
DocumentContentManualGenerator("Navigate", "<h2>Navigate</h2>", "Navigate\\", 0)
DocumentContentManualGenerator("Poker", "<h2>Poker</h2>", "Poker\\", 0)
DocumentContentManualGenerator("Roblox", "<h2>Roblox</h2>", "Roblox\\", 0)
DocumentContentManualGenerator("Triangle", "<h2>Triangle</h2>", "Triangle\\", 0)
if (len(SVGFileList) > 0):
	raise ValueError("SVG Files are not fully handled by generator, please check the pattern!")

# ::::::::::::::::::::::::::::::::::::::
# Program - Write Document
# ::::::::::::::::::::::::::::::::::::::
DocumentContentPrepareWrite = (
"""<!DOCTYPE html>
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
		<div id="heroheader" class="framework">
			<div>
				<span class="logo"><img src="./SVG_Alt.svg" /></span>
				<div>
					<span class="title">SVG Icon Library</span>
					<span class="description"><a href="https://github.com/hugoalh">hugoalh</a>/<a href="https://github.com/hugoalh/Library.SVG.Icon">Library.SVG.Icon</a></span>
				</div>
			</div>
		</div>
		<div id="page" class="framework">
			<div class="information">
				<p><strong>Last Update: </strong>""" + CurrentUTCTime + """ UTC</p>
				<p><strong>Total: </strong>""" + SVGFileCount + """</p>
				<p><strong>License: </strong><a href="./LICENSE.md">CC0 1.0</a></p>
				<p>
					<strong>Note:</strong><br />
					<ul>
						<li>This may take a while to load completely!</li>
						<li>Use "Find In Page" function to search icons!</li>
					</ul>
				</p>
			</div>
			<div class="content">
""" + DocumentContent["General"] + "\n" + 
	DocumentContent["Align"] + "\n" + 
	DocumentContent["Arrow"] + "\n" + 
	DocumentContent["Chess"] + "\n" + 
	DocumentContent["Clock"] + "\n" + 
	DocumentContent["Dice"] + "\n" + 
	DocumentContent["Input"] + "\n" + 
	DocumentContent["Input_Chinese"] + "\n" + 
	DocumentContent["Input_SimplifiedChinese"] + "\n" + 
	DocumentContent["Minecraft"] + "\n" + 
	DocumentContent["Navigate"] + "\n" + 
	DocumentContent["Poker"] + "\n" + 
	DocumentContent["Roblox"] + "\n" + 
	DocumentContent["Triangle"] + """
			</div>
		</div>
	</body>
</html>
"""
)
Document = open(PathData["Document"], "wt", 1, "utf_8", "replace")
Document.write(DocumentContentPrepareWrite)
Document.close()
print("Web View Generator runs successful!")
sys.exit(0)
