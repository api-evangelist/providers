---
aid: nunit
name: NUnit
description: NUnit is a unit-testing framework for all .NET languages. Initially ported from JUnit, the current production release has been completely rewritten with many new features and support for a wide range of .NET platforms. NUnit is a software testing framework, not a remote HTTP API service.
type: Index
position: Producer
access: 1st-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - .NET
  - C#
  - Framework
  - Open Source
  - TDD
  - Testing
  - Unit Testing
url: https://raw.githubusercontent.com/api-evangelist/nunit/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nunit:nunit-framework-api
    name: NUnit Framework API
    description: The core NUnit testing framework programming API for writing and executing unit tests in .NET applications. Provides assertions, attributes, and lifecycle hooks consumed via the NUnit NuGet package.
    humanURL: https://docs.nunit.org/
    tags:
      - Assertions
      - Attributes
      - Testing
    properties:
      - type: Documentation
        url: https://docs.nunit.org/articles/nunit/intro.html
      - type: Getting Started
        url: https://docs.nunit.org/articles/nunit/getting-started.html
      - type: Reference
        url: https://docs.nunit.org/api/
      - type: NuGet Package
        url: https://www.nuget.org/packages/NUnit
      - type: Source Code
        url: https://github.com/nunit/nunit
  - aid: nunit:nunit-console-runner
    name: NUnit Console Runner
    description: Console runner for executing NUnit tests from the command line, enabling automation in build pipelines and CI/CD systems.
    humanURL: https://docs.nunit.org/articles/nunit/running-tests/Console-Runner.html
    tags:
      - Console
      - Test Runner
      - CLI
    properties:
      - type: Documentation
        url: https://docs.nunit.org/articles/nunit/running-tests/Console-Runner.html
      - type: Command Line Reference
        url: https://docs.nunit.org/articles/nunit/running-tests/Console-Command-Line.html
      - type: NuGet Package
        url: https://www.nuget.org/packages/NUnit.ConsoleRunner
  - aid: nunit:nunit3-test-adapter
    name: NUnit3 Test Adapter
    description: Test adapter for running NUnit tests in Visual Studio, dotnet test, and other VSTest-compatible test runners.
    humanURL: https://docs.nunit.org/articles/vs-test-adapter/Index.html
    tags:
      - Visual Studio
      - Test Adapter
      - VSTest
    properties:
      - type: Documentation
        url: https://docs.nunit.org/articles/vs-test-adapter/Index.html
      - type: NuGet Package
        url: https://www.nuget.org/packages/NUnit3TestAdapter
      - type: Source Code
        url: https://github.com/nunit/nunit3-vs-adapter
  - aid: nunit:nunit-analyzers
    name: NUnit Analyzers
    description: Roslyn-based analyzers for NUnit that detect common test authoring mistakes and suggest fixes at compile time.
    humanURL: https://docs.nunit.org/articles/nunit-analyzers/NUnit-Analyzers.html
    tags:
      - Analyzers
      - Roslyn
      - Code Quality
    properties:
      - type: Documentation
        url: https://docs.nunit.org/articles/nunit-analyzers/NUnit-Analyzers.html
      - type: NuGet Package
        url: https://www.nuget.org/packages/NUnit.Analyzers
      - type: Source Code
        url: https://github.com/nunit/nunit.analyzers
common:
  - type: Website
    url: https://nunit.org
  - type: Documentation
    url: https://docs.nunit.org
  - type: GitHub Organization
    url: https://github.com/nunit
  - type: Blog
    url: https://nunit.org/news/
  - type: Community
    url: https://nunit.org/community/
  - type: Change Log
    url: https://docs.nunit.org/articles/nunit/release-notes/
  - type: License
    url: https://docs.nunit.org/articles/nunit/license.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
