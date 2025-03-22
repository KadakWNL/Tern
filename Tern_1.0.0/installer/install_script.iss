[Setup]
AppName=Tern
AppVersion=1.0.0
DefaultDirName={autopf}\Tern
DefaultGroupName=Tern
OutputDir=.
OutputBaseFilename=Tern_Installer
Compression=lzma
SolidCompression=yes
SetupIconFile=Logo\final.ico

[Files]
Source: "Tern.exe"; DestDir: "{app}"
Source: "frontend_dist\*"; DestDir: "{app}\frontend"
Source: "frontend_dist\assets\*"; DestDir: "{app}\frontend\assets"
Source: "Logo\*"; DestDir: "{app}\Logo"

[Icons]
Name: "{group}\Tern"; Filename: "{app}\Tern.exe"

[Run]
Filename: "{app}\Tern.exe"; Description: "Launch Tern"; Flags: nowait postinstall
