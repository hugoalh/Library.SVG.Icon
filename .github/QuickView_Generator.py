# ==============================================================================
# SVG Icon Library - Quick View - Generator
#   Author:
#     hugoalh
#   Language:
#     Python 3.8
# ==============================================================================
import os, pathlib, time

# Data
CurrentUTCTime = time.strftime("%Y-%m-%d %H:%M", time.gmtime())
PathData = {
	"Repository": str(pathlib.Path(os.path.abspath(__file__)).parent.parent)
}
PathData["Document"] = os.path.join(PathData["Repository"], ".github\\QuickView.md")
IgnoreList = {
	"SVGFile": [
		"_Template.svg"
	],
	"Directory": [
		".git", ".github", ".vscode"
	]
}

# Program
print("Current UTC Time:", CurrentUTCTime)
print("Repository Path:", PathData["Repository"])
print("Document Path:", PathData["Document"])
print("Ignore SVG File:", IgnoreList["SVGFile"])
print("Ignore Directory:", IgnoreList["Directory"])
def DetectIsIgnore(InputFileName):
	for Element in IgnoreList["Directory"]:
		if (InputFileName.find(Element) == 0):
			return True
	for Element in IgnoreList["SVGFile"]:
		if (InputFileName.find(Element) != -1):
			return True
	if (InputFileName.find(".svg", len(InputFileName) - 5) == -1):
		return True
	return False
SVGFileList = []
for Root, Directories, FilesName in os.walk(PathData["Repository"]):
	for FileName in FilesName:
		FullPath = os.path.join(Root, FileName).replace(PathData["Repository"] + "\\", "")
		if (DetectIsIgnore(FullPath) == False):
			SVGFileList.append(FullPath)
print("SVG File:", SVGFileList)
DocumentContent = {
	"General": ""
}
SVGFileList_Proceeded = []
DocumentContent["General"] = DocumentContent["General"] + "<table>"
for Element in SVGFileList:
	if (Element.find("\\") == -1):
		DocumentContent["General"] = DocumentContent["General"] + "\n\t<tr><td><img src=\"../" + Element + "\" /></td>" + "<td>" + Element.replace(".svg", "") + "</td></tr>"
		SVGFileList_Proceeded.append(Element)
DocumentContent["General"] = DocumentContent["General"] + "\n</table>"
print("Document Content - General" + DocumentContent["General"])
# Document = open(PathData["Document"], "wt")
# Document.close()