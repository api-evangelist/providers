---
aid: microsoft-nuget
name: Microsoft NuGet
description: NuGet is the package manager for .NET, hosted by Microsoft. It provides APIs for searching, downloading, publishing, and managing .NET packages through the NuGet Gallery and private feeds.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - .NET
  - Microsoft
  - NuGet
  - Package Management
url: https://raw.githubusercontent.com/api-evangelist/microsoft-nuget/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-nuget:server-api
    name: NuGet Server API
    tags:
      - .NET
      - NuGet
      - Package Management
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.nuget.org/v3/
    humanURL: https://learn.microsoft.com/en-us/nuget/api/overview
    properties:
      - url: https://learn.microsoft.com/en-us/nuget/api/overview
        type: Documentation
      - url: https://learn.microsoft.com/en-us/nuget/api/search-query-service-resource
        type: Reference
    description: The NuGet Server API (v3) provides RESTful access to the NuGet package registry. Developers can search packages, download package content, retrieve package metadata and versions, push new packages, and manage package listings. The API uses a service index pattern for resource discovery and supports both nuget.org and private feeds.
common:
  - type: Portal
    url: https://www.nuget.org/
  - type: Website
    url: https://www.nuget.org/
  - type: GitHub Organization
    url: https://github.com/NuGet
  - type: Documentation
    url: https://learn.microsoft.com/en-us/nuget/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/nuget/quickstart/install-and-use-a-package-in-visual-studio
  - type: Terms of Service
    url: https://www.nuget.org/policies/Terms
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Status
    url: https://status.nuget.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
