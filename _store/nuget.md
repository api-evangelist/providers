---
aid: nuget
name: NuGet
description: NuGet is the package manager for .NET, providing a centralized repository for developers to discover, share, and consume reusable code libraries. The NuGet developer platform exposes a set of HTTP APIs that enable programmatic access to package search, metadata retrieval, content download, catalog browsing, and package publishing against the nuget.org feed.
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Package Management
  - .NET
  - Packages
  - Dependencies
  - Software Distribution
  - Registry
url: https://raw.githubusercontent.com/api-evangelist/nuget/refs/heads/main/apis.yml
created: '2025-03-05'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nuget:nuget-server-api
    name: NuGet Server API
    description: The NuGet Server API is a set of HTTP endpoints used to download packages, fetch metadata, publish new packages, and perform other operations against a NuGet package source. The V3 API uses JSON as its underlying media type and is accessed through a service index located at https://api.nuget.org/v3/index.json, which enumerates all available resources and capabilities.
    humanURL: https://learn.microsoft.com/en-us/nuget/api/overview
    tags:
      - Package Management
      - .NET
      - Packages
      - Registry
      - Dependencies
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/api/overview
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/api/service-index
      - type: GitHubRepository
        url: https://github.com/NuGet/NuGetGallery
      - type: OpenAPI
        url: openapi/nuget-server-api-openapi.yml
  - aid: nuget:nuget-catalog-api
    name: NuGet Catalog API
    description: The NuGet Catalog API is an append-only resource that records the full history of all package events on nuget.org, including packages being added, modified, listed, unlisted, and deleted. It provides a chronologically ordered log of every change to the package source, enabling consumers to build and maintain their own local copy of the entire set of packages available on nuget.org.
    humanURL: https://learn.microsoft.com/en-us/nuget/api/catalog-resource
    tags:
      - Package Management
      - .NET
      - Catalog
      - Event Log
      - Packages
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/api/catalog-resource
      - type: OpenAPI
        url: openapi/nuget-catalog-api-openapi.yml
  - aid: nuget:nuget-search-api
    name: NuGet Search API
    description: The NuGet Search API allows clients to query for packages available on a NuGet package source using the SearchQueryService resource found in the service index. It supports filtering by keyword, target framework, prerelease status, and package type, and returns paginated results with package metadata including versions, descriptions, download counts, and dependency information.
    humanURL: https://learn.microsoft.com/en-us/nuget/api/search-query-service-resource
    tags:
      - Package Management
      - .NET
      - Search
      - Discovery
      - Packages
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/api/search-query-service-resource
      - type: OpenAPI
        url: openapi/nuget-search-api-openapi.yml
  - aid: nuget:nuget-package-metadata-api
    name: NuGet Package Metadata API
    description: The NuGet Package Metadata API, accessed through the RegistrationsBaseUrl resource, provides detailed metadata about packages available on a NuGet package source. It returns registration information including all available versions of a package, their dependencies, download URLs, descriptions, authors, license information, and deprecation status.
    humanURL: https://learn.microsoft.com/en-us/nuget/api/registration-base-url-resource
    tags:
      - Package Management
      - .NET
      - Metadata
      - Package Registry
      - Versions
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/api/registration-base-url-resource
      - type: OpenAPI
        url: openapi/nuget-package-metadata-api-openapi.yml
  - aid: nuget:nuget-package-content-api
    name: NuGet Package Content API
    description: The NuGet Package Content API, accessed through the PackageBaseAddress resource, allows clients to download package content files (.nupkg) and package manifests (.nuspec) from a NuGet feed. It uses a flat container structure where packages are organized by lowercase package ID and version, providing direct access to the binary package files.
    humanURL: https://learn.microsoft.com/en-us/nuget/api/package-base-address-resource
    tags:
      - Package Management
      - .NET
      - Package Download
      - Content
      - NuPkg
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/api/package-base-address-resource
      - type: OpenAPI
        url: openapi/nuget-package-content-api-openapi.yml
common:
  - type: Portal
    url: https://learn.microsoft.com/en-us/nuget/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/nuget/api/overview
  - type: Website
    url: https://www.nuget.org/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: TermsOfService
    url: https://www.nuget.org/policies/Terms
  - type: Blog
    url: https://devblogs.microsoft.com/nuget/
  - type: Login
    url: https://www.nuget.org/users/account/LogOn
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
