# ==============================================================================
# SVG Icon Library - Action - Check Valid
#   Author & Contributor:
#     hugoalh
#   Language:
#     Python 3.8
# ==============================================================================
import os, pathlib, sys

# ::::::::::::::::::::::::::::::::::::::
# Data
# ::::::::::::::::::::::::::::::::::::::
PathData = {
	"Repository": str(pathlib.Path(os.path.abspath(__file__)).parent.parent.parent)
}
PathData["Template"] = os.path.join(PathData["Repository"], "_Template.svg")
IgnoreList = {
	"SVGFile": [
		"_Template.svg", "_Template_Disable.svg"
	],
	"Directory": [
		".git", ".github", ".vscode"
	]
}
AdobeIllustratorXML = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!-- Generator: Adobe Illustrator 16.0.0, SVG Export Plug-In . SVG Version: 6.00 Build 0)  -->\n<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\" \"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n"

# ::::::::::::::::::::::::::::::::::::::
# Program - List Data & Get Data
# ::::::::::::::::::::::::::::::::::::::
print("Path - Repository:", PathData["Repository"])
print("Path - Template:", PathData["Template"])
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

# ::::::::::::::::::::::::::::::::::::::
# Program - Find Invalid SVG
# ::::::::::::::::::::::::::::::::::::::
ValidFile = open(PathData["Template"], "rt")
ValidPattern = ValidFile.read().replace("\n</svg>\n", "")
ValidFile.close()
InvalidSVGFileList = {}
for File in SVGFileList:
	ThatFile = open(os.path.join(PathData["Repository"], File), "rt")
	ThatFileContent = ThatFile.read()
	ThatFile.close()
	InvalidSVGFileList[File] = []
	if (ThatFileContent.find(AdobeIllustratorXML) == 0):
		ThatFileContent = ThatFileContent.replace(AdobeIllustratorXML, "")
		ReopenThatFile = open(os.path.join(PathData["Repository"], File), "wt", 1, "utf_8", "replace")
		ReopenThatFile.write(ThatFileContent)
		ReopenThatFile.close()
	if (ThatFileContent.find(ValidPattern) != 0):
		InvalidSVGFileList[File].append("Invalid Pattern!")
	if (ThatFileContent.find("<g>") != -1):
		InvalidSVGFileList[File].append("Contain Group!")
	if (ThatFileContent.find("fill=\"#040000\"") != -1):
		InvalidSVGFileList[File].append("Adobe Illustrator CMYK!")
	if (len(InvalidSVGFileList[File]) == 0):
		del InvalidSVGFileList[File]
if (len(InvalidSVGFileList) > 0):
	print("Invalid SVG File:", InvalidSVGFileList)
else:
	print("All SVG file are valid!")
sys.exit(0)
