---
aid: specflow
url: https://raw.githubusercontent.com/api-evangelist/specflow/refs/heads/main/apis.yml
name: SpecFlow
description: SpecFlow was an open-source BDD (Behavior-Driven Development) testing framework for .NET that allowed teams to write executable specifications in natural language using the Gherkin syntax. Originally developed by TechTalk, it was acquired by Tricentis in 2020 and reached end-of-life on December 31, 2024. The community continuation is Reqnroll, a fork maintaining full backward compatibility.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
tags:
  - .NET
  - BDD
  - Cucumber
  - Gherkin
  - Testing
created: '2024-01-01'
modified: '2026-05-02'
position: Consumer
segments:
  - Testing
  - .NET
apis:
  - aid: specflow:specflow
    name: SpecFlow
    tags:
      - .NET
      - BDD
      - Cucumber
      - Gherkin
      - Testing
    humanURL: https://github.com/SpecFlowOSS/SpecFlow
    properties:
      - url: https://github.com/SpecFlowOSS/SpecFlow
        type: GitHubRepo
      - url: https://docs.specflow.org
        type: Documentation
      - url: https://www.nuget.org/packages/SpecFlow/
        type: NuGet
      - url: https://reqnroll.net/
        type: Successor
    description: SpecFlow is a BDD framework for .NET that bridges the communication gap between domain experts and developers by enabling natural language specifications (Gherkin) to be executed as automated tests. It supports NUnit, xUnit, and MSTest as underlying test runners. Reached end-of-life December 31, 2024; succeeded by the community-driven Reqnroll project.
  - aid: specflow:reqnroll
    name: Reqnroll
    tags:
      - .NET
      - BDD
      - Cucumber
      - Gherkin
      - Open Source
      - Testing
    humanURL: https://reqnroll.net/
    properties:
      - url: https://reqnroll.net/
        type: Website
      - url: https://reqnroll.net/documentation/
        type: Documentation
      - url: https://github.com/reqnroll/Reqnroll
        type: GitHubRepo
      - url: https://www.nuget.org/packages/Reqnroll/
        type: NuGet
    description: Reqnroll is the open-source community continuation and fork of SpecFlow, maintaining full backward compatibility while supporting .NET 8.0 and .NET 9.0. Created in 2024 after Tricentis announced SpecFlow end-of-life, Reqnroll has over 5,000 active projects and a growing contributor base.
common:
  - url: https://github.com/SpecFlowOSS/SpecFlow
    name: SpecFlow GitHub Repository
    type: GitHubRepo
    description: 'null'
  - url: https://docs.specflow.org
    name: SpecFlow Documentation
    type: Documentation
    description: 'null'
  - url: https://www.nuget.org/packages/SpecFlow/
    name: SpecFlow on NuGet
    type: NuGet
    description: 'null'
  - url: https://reqnroll.net/
    name: Reqnroll - SpecFlow Successor
    type: Successor
    description: 'null'
  - url: https://reqnroll.net/news/2025/01/specflow-end-of-life-has-been-announced/
    name: SpecFlow End-of-Life Announcement
    type: Blog
    description: 'null'
  - name: Features
    type: Features
    data:
      - name: Gherkin Syntax
      - name: BDD Scenarios
      - name: .NET Integration
      - name: NUnit Support
      - name: xUnit Support
      - name: MSTest Support
      - name: Visual Studio Integration
      - name: Step Definitions
      - name: Scenario Outlines
      - name: Data Tables
      - name: Hooks
      - name: Context Injection
      - name: Parallel Execution
      - name: Living Documentation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
