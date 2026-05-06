---
aid: microsoft-package
name: Microsoft Package
description: A collection of Microsoft package management APIs covering NuGet, Windows Package Manager (WinGet), Microsoft Store, and Azure Artifacts for managing and distributing software packages across Microsoft platforms.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure Artifacts
  - Microsoft
  - NuGet
  - Package Management
  - WinGet
url: https://raw.githubusercontent.com/api-evangelist/microsoft-package/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-package:nuget-package-api
    name: NuGet Package API
    description: API for managing .NET packages through NuGet Gallery.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.nuget.org/
    baseURL: https://api.nuget.org/v3/index.json
    tags:
      - .NET
      - Libraries
      - NuGet
      - Packages
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/api/overview
      - type: Authentication
        url: https://learn.microsoft.com/en-us/nuget/api/authentication
  - aid: microsoft-package:winget-api
    name: Windows Package Manager (WinGet) API
    description: API for the Windows Package Manager client for discovering and installing applications.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/windows/package-manager/
    baseURL: https://winget.azureedge.net/cache
    tags:
      - Applications
      - Package Manager
      - Windows
      - WinGet
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/package-manager/
      - type: GitHub Organization
        url: https://github.com/microsoft/winget-cli
  - aid: microsoft-package:microsoft-store-api
    name: Microsoft Store API
    description: API for managing app submissions and accessing Microsoft Store catalog.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/windows/uwp/monetize/create-and-manage-submissions-using-windows-store-services
    baseURL: https://manage.devcenter.microsoft.com/v1.0/my/
    tags:
      - Apps
      - Commercial
      - Microsoft Store
      - Submissions
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/windows/uwp/monetize/create-and-manage-submissions-using-windows-store-services
      - type: Authentication
        url: https://learn.microsoft.com/en-us/windows/uwp/monetize/create-and-manage-submissions-using-windows-store-services
  - aid: microsoft-package:azure-artifacts-api
    name: Azure Artifacts Package API
    description: API for managing packages in Azure Artifacts including NuGet, npm, Maven, and Python packages.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://azure.microsoft.com/en-us/services/devops/artifacts/
    baseURL: https://pkgs.dev.azure.com/{organization}/
    tags:
      - Artifacts
      - Azure
      - DevOps
      - Packages
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/azure/devops/artifacts/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/devops/integrate/get-started/authentication/authentication-guidance
common:
  - type: Portal
    url: https://developer.microsoft.com/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
