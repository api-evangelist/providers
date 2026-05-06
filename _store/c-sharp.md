---
aid: c-sharp
url: https://raw.githubusercontent.com/api-evangelist/c-sharp/refs/heads/main/apis.yml
name: C#
tags:
  - .NET
  - C#
  - Microsoft
  - Programming Language
  - Topic
  - Roslyn
  - NuGet
  - Dotnet
  - Language
type: Index
x-type: topic
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-01'
modified: '2026-04-23'
position: Consumer
description: C# is a modern, object-oriented programming language developed by Microsoft as part of the .NET platform. It is used for building Windows applications, web services, games (via Unity), and enterprise software, offering strong typing, garbage collection, and rich framework support. The C# language is defined by a standardized specification and implemented by the Roslyn compiler, with packages distributed via NuGet and running on the .NET runtime.
apis:
  - aid: c-sharp:c-sharp-language
    name: C# Language
    tags:
      - C#
      - Programming Language
      - Microsoft
    humanURL: https://learn.microsoft.com/en-us/dotnet/csharp/
    properties:
      - type: Website
        url: https://learn.microsoft.com/en-us/dotnet/csharp/
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/
      - type: Language Reference
        url: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/
      - type: Language Specification
        url: https://learn.microsoft.com/en-us/dotnet/csharp/specification/
    description: 'The C# language itself: syntax, semantics, type system, and standard library conventions. Maintained by Microsoft with a formal ECMA-334 specification and modern features such as records, pattern matching, async/await, and nullable reference types.'
  - aid: c-sharp:roslyn-compiler
    name: Roslyn (.NET Compiler Platform)
    tags:
      - Compiler
      - Roslyn
      - Open Source
    humanURL: https://github.com/dotnet/roslyn
    properties:
      - type: GitHub
        url: https://github.com/dotnet/roslyn
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/
    description: Roslyn is the open-source .NET compiler platform that provides C# and Visual Basic compilers with rich code analysis APIs, enabling custom analyzers, refactorings, and tooling.
  - aid: c-sharp:dotnet-runtime
    name: .NET Runtime
    tags:
      - Runtime
      - Dotnet
      - Open Source
    humanURL: https://github.com/dotnet/runtime
    properties:
      - type: GitHub
        url: https://github.com/dotnet/runtime
      - type: Download
        url: https://dotnet.microsoft.com/download
      - type: Documentation
        url: https://learn.microsoft.com/en-us/dotnet/core/
    description: The .NET runtime hosts and executes C# programs, providing the CLR, base class libraries, garbage collection, and cross-platform support for Windows, Linux, and macOS.
  - aid: c-sharp:nuget
    name: NuGet Package Manager
    tags:
      - Package Manager
      - NuGet
      - Registry
    humanURL: https://www.nuget.org
    properties:
      - type: Website
        url: https://www.nuget.org
      - type: Documentation
        url: https://learn.microsoft.com/en-us/nuget/
      - type: API
        url: https://learn.microsoft.com/en-us/nuget/api/overview
      - type: GitHub
        url: https://github.com/NuGet
    description: NuGet is the package manager for .NET, providing a central registry of open-source and commercial libraries distributed as packages for use in C# and other .NET projects. NuGet exposes a documented HTTP API for package discovery and publishing.
  - aid: c-sharp:aspnet-core
    name: ASP.NET Core
    tags:
      - Web Framework
      - ASP.NET
    humanURL: https://learn.microsoft.com/en-us/aspnet/core
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/aspnet/core
      - type: GitHub
        url: https://github.com/dotnet/aspnetcore
    description: ASP.NET Core is the cross-platform web framework for C#, used to build web applications, APIs, and real-time services on the .NET runtime.
common:
  - type: Website
    url: https://learn.microsoft.com/en-us/dotnet/csharp/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/
  - type: Language Reference
    url: https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/
  - type: Specification
    url: https://learn.microsoft.com/en-us/dotnet/csharp/specification/
  - type: GitHub Org
    url: https://github.com/dotnet
  - type: Roslyn Compiler
    url: https://github.com/dotnet/roslyn
  - type: .NET Runtime
    url: https://github.com/dotnet/runtime
  - type: .NET Docs
    url: https://github.com/dotnet/docs
  - type: NuGet
    url: https://www.nuget.org
  - type: Download .NET
    url: https://dotnet.microsoft.com/download
  - type: Blog
    url: https://devblogs.microsoft.com/dotnet/
  - type: Community
    url: https://dotnet.microsoft.com/platform/community
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
