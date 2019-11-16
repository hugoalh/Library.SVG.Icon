# ==============================================================================
# SVG Icon Library - Index Generator
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
	"Repository": str(pathlib.Path(os.path.abspath(__file__)).parent.parent)
}
PathData["Document"] = os.path.join(PathData["Repository"], "index.html")
IgnoreList = {
	"SVGFile": [
		"_Template.svg"
	],
	"Directory": [
		".git", ".github", ".vscode"
	]
}

# ::::::::::::::::::::::::::::::::::::::
# Program - Listing Data & File
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
			DocumentContent[InternalCatalog] = DocumentContent[InternalCatalog] + "<span><span><img src=\"./" + ElementPath + "\" /><br />" + ElementName + "</span></span>\n"
			SVGFileList_Proceeded.append(Element)
	DocumentContent[InternalCatalog] = HeaderString + "\n<div class=\"flex\">\n" + DocumentContent[InternalCatalog] + "\n</div>"
	for Element in SVGFileList_Proceeded:
		SVGFileList.remove(Element)
DocumentContentManualGenerator("General", "<h1>General</h1>", "\\", -1)
DocumentContentManualGenerator("Align", "<h1>Align</h1>", "Align\\", 0)
DocumentContentManualGenerator("Arrow", "<h1>Arrow</h1>", "Arrow\\", 0)
DocumentContentManualGenerator("Chess", "<h1>Chess</h1>", "Chess\\", 0)
DocumentContentManualGenerator("Clock", "<h1>Clock</h1>", "Clock\\", 0)
DocumentContentManualGenerator("Dice", "<h1>Dice</h1>", "Dice\\", 0)
DocumentContentManualGenerator("Input_Chinese", "<h2>Chinese</h2>", "Input\\Chinese\\", 0)
DocumentContentManualGenerator("Input_SimplifiedChinese", "<h2>Simplified Chinese</h2>", "Input\\SimplifiedChinese\\", 0)
DocumentContentManualGenerator("Input", "<h1>Input</h1>", "Input\\", 0)
DocumentContentManualGenerator("Minecraft", "<h1>Minecraft</h1>", "Minecraft\\", 0)
DocumentContentManualGenerator("Navigate", "<h1>Navigate</h1>", "Navigate\\", 0)
DocumentContentManualGenerator("Poker", "<h1>Poker</h1>", "Poker\\", 0)
DocumentContentManualGenerator("Triangle", "<h1>Triangle</h1>", "Triangle\\", 0)
if (len(SVGFileList) > 0):
	raise ValueError("SVG Files are not fully handled by generator, please check the pattern!")

# ::::::::::::::::::::::::::::::::::::::
# Program - Write Document
# ::::::::::::::::::::::::::::::::::::::
DocumentContentPrepareWrite = ("<!DOCTYPE html>\n" + 
	"<html>\n" + 
	"<head>\n" + 
	"<!-- Character Encode --->\n" + 
	"<meta charset=\"UTF-8\" />\n" + 
	"<!-- Security --->\n" + 
	"<meta name=\"referrer\" content=\"origin-when-cross-origin\" />\n" + 
	"<meta name=\"robots\" content=\"index, follow\" />\n" + 
	"<!-- Information --->\n" + 
	"<meta name=\"application-name\" content=\"SVG Icon Library\" />\n" + 
	"<meta name=\"apple-mobile-web-app-title\" content=\"SVG Icon Library\" />\n" + 
	"<meta name=\"title\" content=\"SVG Icon Library\" />\n" + 
	"<meta name=\"author\" content=\"hugoalh\" />\n" + 
	"<meta name=\"description\" content=\"A SVG icon library.\" />\n" + 
	"<meta name=\"keywords\" content=\"library svg svg-icon svg-icons\" />\n" + 
	"<!-- Render --->\n" + 
	"<meta dir=\"auto\" />\n" + 
	"<meta autocapitalize=\"off\" />\n" + 
	"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\" />\n" + 
	"<meta name=\"mobile-web-app-capable\" content=\"yes\" />\n" + 
	"<meta name=\"apple-mobile-web-app-capable\" content=\"yes\" />\n" + 
	"<!-- Style --->\n" + 
	"<link rel=\"stylesheet\" href=\"./index.css\" />\n" + 
	"<title>SVG Icon Library</title>\n" + 
	"</head>\n" + 
	"<body>\n" + 
	"<div id=\"heroheader\" class=\"framework\">\n" + 
	"<span class=\"title\">SVG Icon Library</span>\n" + 
	"<span class=\"description\"><a href=\"https://github.com/hugoalh\">hugoalh</a>/<a href=\"https://github.com/hugoalh/Library.SVG.Icon\">Library.SVG.Icon</a> - A SVG icon library.</span>\n" + 
	"</div>\n" + 
	"<div id=\"page\" class=\"framework\">\n" + 
	"<div class=\"information\">\n" + 
	"<strong>Last Update: </strong>" + CurrentUTCTime + " UTC<br />\n" + 
	"<strong>Total: </strong>" + SVGFileCount + "<br />\n" + 
	"<strong>Note:</strong> This may take a while to load completely!\n" + 
	"</div>\n" + 
	"<div class=\"content\">\n" + 
	DocumentContent["General"] + "\n" + 
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
	DocumentContent["Triangle"] + "\n" + 
	"</div>\n" + 
	"</div>\n" + 
	"</body>\n" + 
	"</html>\n"
)
Document = open(PathData["Document"], "wt", 1, "utf_8", "replace")
Document.write(DocumentContentPrepareWrite)
Document.close()
print("Index Generator runs successful!")
sys.exit(0)
