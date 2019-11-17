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
		"_Template.svg"
	],
	"Directory": [
		".git", ".github", ".vscode"
	]
}

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
InvalidSVGFileList = []
for File in SVGFileList:
	ThatFile = open(os.path.join(PathData["Repository"], File), "rt")
	ThatFileContent = ThatFile.read()
	ThatFile.close()
	if (ThatFileContent.find(ValidPattern) != 0):
		InvalidSVGFileList.append(File)
	elif (ThatFileContent.find("<g>") != -1):
		InvalidSVGFileList.append(File)
if (len(InvalidSVGFileList) > 0):
	print("Invalid SVG File:", InvalidSVGFileList)
else:
	print("All SVG file are valid!")
sys.exit(0)
