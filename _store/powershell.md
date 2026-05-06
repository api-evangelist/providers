---
aid: powershell
name: PowerShell
description: PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. The PowerShell ecosystem exposes APIs through the PowerShell Gallery (an OData-based package repository), the Runspace .NET hosting APIs, and PowerShell Remoting protocols (WS-Management and SSH).
type: Index
image: https://raw.githubusercontent.com/PowerShell/PowerShell/master/assets/ps_black_64.svg
tags:
  - Automation
  - Command-Line
  - Cross-Platform
  - Scripting
  - Shell
  - Windows
  - DevOps
url: https://raw.githubusercontent.com/api-evangelist/powershell/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: powershell:powershell-gallery-api
    name: PowerShell Gallery API
    description: The PowerShell Gallery is the central repository for PowerShell modules, scripts, and DSC resources. It exposes a public OData v2 API for searching, retrieving, and downloading packages programmatically.
    image: https://www.powershellgallery.com/Content/Images/Branding/psgallerylogo.svg
    humanURL: https://www.powershellgallery.com/
    baseURL: https://www.powershellgallery.com/api/v2
    tags:
      - Modules
      - NuGet
      - Packages
      - Repository
      - OData
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/powershell/gallery/overview
      - type: Metadata
        url: https://www.powershellgallery.com/api/v2/$metadata
    contact:
      - FN: PowerShell Gallery Support
        url: https://github.com/PowerShell/PowerShellGallery/issues
  - aid: powershell:powershell-runspace-api
    name: PowerShell Runspace API
    description: .NET APIs for creating, configuring, and managing PowerShell runspaces from host applications. Enables embedding PowerShell execution inside .NET programs.
    humanURL: https://docs.microsoft.com/en-us/dotnet/api/system.management.automation.runspaces
    tags:
      - Automation
      - .NET
      - Runspace
      - SDK
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/powershell/scripting/developer/hosting/creating-runspaces
      - type: SDK
        url: https://www.nuget.org/packages/System.Management.Automation/
      - type: Examples
        url: https://github.com/PowerShell/PowerShell/tree/master/test/hosting
  - aid: powershell:powershell-remoting-api
    name: PowerShell Remoting API
    description: APIs and protocols for remote PowerShell execution over WS-Management (WinRM) and SSH. Enables one-to-one and one-to-many remote command and session management.
    humanURL: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/running-remote-commands
    tags:
      - Remoting
      - SSH
      - WinRM
      - WS-Management
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/powershell/scripting/learn/remoting/powershell-remoting-faq
      - type: ProtocolSpecification
        url: https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-psrp/
common:
  - type: Website
    url: https://microsoft.com/powershell
  - type: GitHub
    url: https://github.com/PowerShell/PowerShell
  - type: Documentation
    url: https://docs.microsoft.com/en-us/powershell/
  - type: Blog
    url: https://devblogs.microsoft.com/powershell/
  - type: Community
    url: https://github.com/PowerShell/PowerShell/blob/master/docs/community/README.md
  - type: GettingStarted
    url: https://docs.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started
  - type: License
    url: https://github.com/PowerShell/PowerShell/blob/master/LICENSE.txt
  - type: Releases
    url: https://github.com/PowerShell/PowerShell/releases
  - type: Roadmap
    url: https://github.com/PowerShell/PowerShell/projects
  - type: Security
    url: https://github.com/PowerShell/PowerShell/security/policy
  - type: Contributing
    url: https://github.com/PowerShell/PowerShell/blob/master/.github/CONTRIBUTING.md
maintainers:
  - FN: Microsoft
    email: powershell@microsoft.com
    url: https://github.com/PowerShell
---
