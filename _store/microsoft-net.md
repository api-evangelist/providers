---
aid: microsoft-net
name: Microsoft .NET
description: Microsoft .NET is a free, cross-platform, open source developer platform for building many different types of applications. The .NET APIs and developer tools provide programmatic access to .NET runtime services, NuGet package management, project templates, and build tooling across web, mobile, desktop, games, IoT, cloud, and microservices workloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/microsoft-net/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - .NET
  - C#
  - Cloud
  - Cross-Platform
  - Developer Tools
  - Microsoft
  - Open Source
apis:
  - aid: microsoft-net:dotnet-api
    name: Microsoft .NET API Browser
    description: Comprehensive reference for .NET APIs across all packages, namespaces, and types in the .NET ecosystem including .NET 9, .NET Standard, and .NET Framework.
    humanURL: https://learn.microsoft.com/en-us/dotnet/api/
    baseURL: https://learn.microsoft.com/en-us/dotnet/api/
    tags:
      - API Browser
      - Class Library
      - Reference
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dotnet/api/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/dotnet/api/
  - aid: microsoft-net:nuget-api
    name: NuGet Server API
    description: RESTful API for interacting with nuget.org and private NuGet feeds, supporting package search, download, push, delete, and metadata queries for .NET package management.
    humanURL: https://learn.microsoft.com/en-us/nuget/api/overview
    baseURL: https://api.nuget.org/v3/
    tags:
      - NuGet
      - Package Management
      - Package Registry
      - REST
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/api/overview
      - type: APIReference
        url: https://learn.microsoft.com/en-us/nuget/api/overview
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/nuget/quickstart/install-and-use-a-package-in-visual-studio
  - aid: microsoft-net:dotnet-cli
    name: .NET CLI
    description: Cross-platform command-line interface for developing, building, running, and publishing .NET applications. Provides commands for project creation, package management, testing, and deployment.
    humanURL: https://learn.microsoft.com/en-us/dotnet/core/tools/
    baseURL: https://learn.microsoft.com/en-us/dotnet/core/tools/
    tags:
      - Build
      - CLI
      - Developer Tools
      - Tooling
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dotnet/core/tools/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet
  - aid: microsoft-net:aspnet-core-api
    name: ASP.NET Core Web API
    description: Framework for building HTTP-based RESTful APIs and web services with ASP.NET Core, including controllers, minimal APIs, routing, model binding, authentication, and OpenAPI integration.
    humanURL: https://learn.microsoft.com/en-us/aspnet/core/web-api/
    baseURL: https://learn.microsoft.com/en-us/aspnet/core/
    tags:
      - ASP.NET Core
      - REST
      - Web API
      - Web Framework
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/aspnet/core/web-api/
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/aspnet/core/tutorials/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/aspnet/core/getting-started
  - aid: microsoft-net:dotnet-aspire
    name: .NET Aspire
    description: Cloud-ready stack for building observable, production-ready distributed applications in .NET with built-in service discovery, health checks, telemetry, and configuration management.
    humanURL: https://learn.microsoft.com/en-us/dotnet/aspire/
    baseURL: https://learn.microsoft.com/en-us/dotnet/aspire/
    tags:
      - Cloud Native
      - Distributed Systems
      - Microservices
      - Observability
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dotnet/aspire/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/dotnet/aspire/get-started/build-your-first-aspire-app
common:
  - type: Portal
    url: https://dotnet.microsoft.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dotnet/
  - type: GettingStarted
    url: https://dotnet.microsoft.com/learn
  - type: Blog
    url: https://devblogs.microsoft.com/dotnet/
  - type: GitHubOrganization
    url: https://github.com/dotnet
  - type: Support
    url: https://dotnet.microsoft.com/platform/support
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/servicesagreement/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: YouTube
    url: https://www.youtube.com/dotnet
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/.net
  - type: X
    url: https://twitter.com/dotnet
  - type: ChangeLog
    url: https://github.com/dotnet/core/blob/main/release-notes/README.md
  - type: SDK
    url: https://dotnet.microsoft.com/download
  - type: Training
    url: https://learn.microsoft.com/en-us/training/dotnet/
  - type: Features
    data:
      - name: Cross-Platform Development
        description: Build and run .NET applications on Windows, macOS, and Linux with full platform support.
      - name: High Performance Runtime
        description: .NET runtime with JIT compilation, garbage collection, and ahead-of-time compilation for optimal performance.
      - name: NuGet Package Ecosystem
        description: Access over 350,000 packages through the NuGet package manager for rapid development.
      - name: Minimal APIs
        description: Build lightweight HTTP APIs with minimal code using the minimal API pattern in ASP.NET Core.
      - name: Cloud Native Support
        description: Built-in support for containers, Kubernetes, microservices, and cloud deployment through .NET Aspire.
      - name: Hot Reload
        description: Apply code changes to running applications without restarting for faster development cycles.
  - type: UseCases
    data:
      - name: Enterprise Web Applications
        description: Build scalable enterprise web applications using ASP.NET Core with authentication, authorization, and data access.
      - name: Microservices Architecture
        description: Design and deploy microservices using .NET with gRPC, message queues, and service discovery.
      - name: Cloud-Native Applications
        description: Develop cloud-native applications with .NET Aspire, containers, and Azure integration.
      - name: RESTful API Development
        description: Create production-ready REST APIs with OpenAPI documentation, versioning, and rate limiting.
      - name: Desktop Applications
        description: Build Windows desktop applications using WPF, WinForms, or .NET MAUI for cross-platform desktop.
  - type: Integrations
    data:
      - name: Azure
        description: Deep integration with Microsoft Azure cloud services including App Service, Functions, and Container Apps.
      - name: Visual Studio
        description: Full IDE support with IntelliSense, debugging, profiling, and project templates in Visual Studio.
      - name: VS Code
        description: Lightweight development with the C# Dev Kit extension for Visual Studio Code.
      - name: GitHub Actions
        description: CI/CD pipeline integration with GitHub Actions for .NET build, test, and deploy workflows.
      - name: Docker
        description: Container support with official .NET Docker images and multi-stage build templates.
      - name: Entity Framework Core
        description: Object-relational mapping for database access with support for SQL Server, PostgreSQL, SQLite, and more.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
