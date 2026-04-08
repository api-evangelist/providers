---
aid: powershell
url: https://raw.githubusercontent.com/api-evangelist/powershell/refs/heads/main/apis.yml
apis:
- name: PowerShell Gallery API
  description: The PowerShell Gallery is the central repository for PowerShell modules, scripts, and DSC resources.
  image: https://www.powershellgallery.com/Content/Images/Branding/psgallerylogo.svg
  humanURL: https://www.powershellgallery.com/
  baseURL: https://www.powershellgallery.com/api/v2
  tags:
  - Modules
  - Nuget
  - Packages
  - Repository
  properties:
  - type: documentation
    url: https://docs.microsoft.com/en-us/powershell/gallery/overview
  - type: openapi
    url: https://www.powershellgallery.com/api/v2/$metadata
  - type: swagger
    url: https://www.powershellgallery.com/api/v2/swagger.json
  contact:
  - type: support
    url: https://github.com/PowerShell/PowerShellGallery/issues
- name: PowerShell Runspace API
  description: APIs for creating and managing PowerShell runspaces programmatically from .NET applications.
  humanURL: https://docs.microsoft.com/en-us/dotnet/api/system.management.automation.runspaces
  tags:
  - Automation
  - Dotnet
  - Runspace
  - Sdk
  properties:
  - type: documentation
    url: https://docs.microsoft.com/en-us/powershell/scripting/developer/hosting/creating-runspaces
  - type: sdk
    url: https://www.nuget.org/packages/System.Management.Automation/
  - type: examples
    url: https://github.com/PowerShell/PowerShell/tree/master/test/hosting
- name: PowerShell Remoting API
  description: APIs for remote PowerShell execution using WS-Management and SSH protocols.
  humanURL: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands
  tags:
  - Remoting
  - Ssh
  - Winrm
  - Ws-Management
  properties:
  - type: documentation
    url: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/powershell-remoting-faq
  - type: protocol-specification
    url: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-psrp/
name: PowerShell
tags:
- Automation
- Command-Line
- Cross-Platform
- Scripting
- Shell
- Windows
type: Contract
image: https://raw.githubusercontent.com/PowerShell/PowerShell/master/assets/ps_black_64.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

