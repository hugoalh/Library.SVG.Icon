# ==============================================================================
# SVG Icon Library - Quick View - Generator
#   Author:
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
PathData["Document"] = os.path.join(PathData["Repository"], ".github\\QuickView.md")
PathData["Document_List"] = os.path.join(PathData["Repository"], ".github\\QuickView_List.md")
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
print("Path - Document - List:", PathData["Document_List"])
print("Ignore - SVG File:", IgnoreList["SVGFile"])
print("Ignore - Directory:", IgnoreList["Directory"])
def DetectIsIgnore(InputFileName):
	for Element in IgnoreList["Directory"]:
		if (InputFileName.find(Element) == 0):
			return True
	for Element in IgnoreList["SVGFile"]:
		if (InputFileName.find(Element) != -1):
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

# ::::::::::::::::::::::::::::::::::::::
# Program - Generate Document Content
# ::::::::::::::::::::::::::::::::::::::
DocumentContent = {}
DocumentContent_List = {}
def DocumentContentManualGenerator(InternalCatalog, HeaderString, FindQuery, FindResult):
	SVGFileList_Proceeded = []
	DocumentContent[InternalCatalog] = ""
	DocumentContent_List[InternalCatalog] = ""
	for Element in SVGFileList:
		ElementPath = Element.replace("\\", "/")
		ElementName = ElementPath.replace(".svg", "")
		if (Element.find(FindQuery) == FindResult):
			DocumentContent[InternalCatalog] = DocumentContent[InternalCatalog] + "<img src=\"../" + ElementPath + "\" />"
			DocumentContent_List[InternalCatalog] = DocumentContent_List[InternalCatalog] + "\n\t<tr><td><img src=\"../" + ElementPath + "\" /></td>" + "<td>" + ElementName + "</td></tr>"
			SVGFileList_Proceeded.append(Element)
	DocumentContent[InternalCatalog] = HeaderString + "\n\n" + DocumentContent[InternalCatalog]
	DocumentContent_List[InternalCatalog] = HeaderString + "\n\n<table>" + DocumentContent_List[InternalCatalog] + "\n</table>"
	for Element in SVGFileList_Proceeded:
		SVGFileList.remove(Element)
DocumentContentManualGenerator("General", "## General", "\\", -1)
DocumentContentManualGenerator("Align", "## Align", "Align\\", 0)
DocumentContentManualGenerator("Arrow", "## Arrow", "Arrow\\", 0)
DocumentContentManualGenerator("Chess", "## Chess", "Chess\\", 0)
DocumentContentManualGenerator("Clock", "## Clock", "Clock\\", 0)
DocumentContentManualGenerator("Dice", "## Dice", "Dice\\", 0)
DocumentContentManualGenerator("Input_Chinese", "### Chinese", "Input\\Chinese\\", 0)
DocumentContentManualGenerator("Input_SimplifiedChinese", "### Simplified Chinese", "Input\\SimplifiedChinese\\", 0)
DocumentContentManualGenerator("Input", "## Input", "Input\\", 0)
DocumentContentManualGenerator("Minecraft", "## Minecraft", "Minecraft\\", 0)
DocumentContentManualGenerator("Navigate", "## Navigate", "Navigate\\", 0)
DocumentContentManualGenerator("Poker", "## Poker", "Poker\\", 0)
DocumentContentManualGenerator("Triangle", "## Triangle", "Triangle\\", 0)
if (len(SVGFileList) > 0):
	raise ValueError("SVG Files are not fully handled by generator, please check the pattern!")

# ::::::::::::::::::::::::::::::::::::::
# Program - Write Document
# ::::::::::::::::::::::::::::::::::::::
Document = open(PathData["Document"], "wt", 1, "utf_8", "replace")
Document.write(
	"# <div align=\"center\">SVG Icon Library - Quick View</div>\n\n" + 
	"<img src=\"../Eye.svg\" width=\"16\" height=\"16\" />View | <a href=\"./QuickView.md\"><img src=\"../Grid.svg\" width=\"16\" height=\"16\" />Grid</a>　<a href=\"./QuickView_List.md\"><img src=\"../ListBullet.svg\" width=\"16\" height=\"16\" />List</a>\n\n" + 
	"<div align=\"right\"><strong>Last Update: </strong>" + CurrentUTCTime + " UTC</div>\n\n" + 
	"<strong>Note:</strong> This may take a while to load completely!\n\n" + 
	DocumentContent["General"] + "\n\n" + 
	DocumentContent["Align"] + "\n\n" + 
	DocumentContent["Arrow"] + "\n\n" + 
	DocumentContent["Chess"] + "\n\n" + 
	DocumentContent["Clock"] + "\n\n" + 
	DocumentContent["Dice"] + "\n\n" + 
	DocumentContent["Input"] + "\n\n" + 
	DocumentContent["Input_Chinese"] + "\n\n" + 
	DocumentContent["Input_SimplifiedChinese"] + "\n\n" + 
	DocumentContent["Minecraft"] + "\n\n" + 
	DocumentContent["Navigate"] + "\n\n" + 
	DocumentContent["Poker"] + "\n\n" + 
	DocumentContent["Triangle"] + "\n"
)
Document.close()
Document_List = open(PathData["Document_List"], "wt", 1, "utf_8", "replace")
Document_List.write(
	"# <div align=\"center\">SVG Icon Library - Quick View - List</div>\n\n" + 
	"<img src=\"../Eye.svg\" width=\"16\" height=\"16\" />View | <a href=\"./QuickView.md\"><img src=\"../Grid.svg\" width=\"16\" height=\"16\" />Grid</a>　<a href=\"./QuickView_List.md\"><img src=\"../ListBullet.svg\" width=\"16\" height=\"16\" />List</a>\n\n" + 
	"<div align=\"right\"><strong>Last Update: </strong>" + CurrentUTCTime + " UTC</div>\n\n" + 
	"<strong>Note:</strong> This may take a while to load completely!\n\n" + 
	DocumentContent_List["General"] + "\n\n" + 
	DocumentContent_List["Align"] + "\n\n" + 
	DocumentContent_List["Arrow"] + "\n\n" + 
	DocumentContent_List["Chess"] + "\n\n" + 
	DocumentContent_List["Clock"] + "\n\n" + 
	DocumentContent_List["Dice"] + "\n\n" + 
	DocumentContent_List["Input"] + "\n\n" + 
	DocumentContent_List["Input_Chinese"] + "\n\n" + 
	DocumentContent_List["Input_SimplifiedChinese"] + "\n\n" + 
	DocumentContent_List["Minecraft"] + "\n\n" + 
	DocumentContent_List["Navigate"] + "\n\n" + 
	DocumentContent_List["Poker"] + "\n\n" + 
	DocumentContent_List["Triangle"] + "\n"
)
Document_List.close()
print("Quick View Generator runs successful!")
sys.exit(0)
