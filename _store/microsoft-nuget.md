---
aid: microsoft-nuget
url: https://raw.githubusercontent.com/api-evangelist/microsoft-nuget/refs/heads/main/apis.yml
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
name: Microsoft NuGet
tags:
- .NET
- Microsoft
- NuGet
- Package Management
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: NuGet is the package manager for .NET, hosted by Microsoft. It provides APIs for searching, downloading, publishing, and managing .NET packages through the NuGet Gallery and private feeds.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

