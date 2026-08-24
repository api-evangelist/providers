---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Microsoft Net Agentic Access
  operation_count: 7
  slug: microsoft-net-agentic-access
  summary_line: 7 operations
api_count: 9
apis:
- description: Comprehensive reference for .NET APIs across all packages, namespaces, and types in the .NET ecosystem including .NET 9, .NET Standard, and .NET Framework.
  name: Microsoft .NET API Browser
  slug: dotnet-api
- description: RESTful API for interacting with nuget.org and private NuGet feeds, supporting package search, download, push, delete, and metadata queries for .NET package management.
  name: NuGet Server API
  slug: nuget-api
- description: Cross-platform command-line interface for developing, building, running, and publishing .NET applications. Provides commands for project creation, package management, testing, and deployment.
  name: .NET CLI
  slug: dotnet-cli
- description: Framework for building HTTP-based RESTful APIs and web services with ASP.NET Core, including controllers, minimal APIs, routing, model binding, authentication, and OpenAPI integration.
  name: ASP.NET Core Web API
  slug: aspnet-core-api
- description: Cloud-ready stack for building observable, production-ready distributed applications in .NET with built-in service discovery, health checks, telemetry, and configuration management.
  name: .NET Aspire
  slug: dotnet-aspire
- description: The PackageContent API from Microsoft .NET — 3 operation(s) for packagecontent.
  name: Microsoft .NET PackageContent API
  slug: microsoft-net-packagecontent-api
- description: The Registration API from Microsoft .NET — 2 operation(s) for registration.
  name: Microsoft .NET Registration API
  slug: microsoft-net-registration-api
- description: The Search API from Microsoft .NET — 1 operation(s) for search.
  name: Microsoft .NET Search API
  slug: microsoft-net-search-api
- description: The ServiceIndex API from Microsoft .NET — 1 operation(s) for serviceindex.
  name: Microsoft .NET ServiceIndex API
  slug: microsoft-net-serviceindex-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NuGet Server API (V3) PackageContent API
  slug: open-microsoft-net-packagecontent-api
- collection_type: open
  name: NuGet Server API (V3) PackageContent Registration API
  slug: open-microsoft-net-registration-api
- collection_type: open
  name: NuGet Server API (V3) PackageContent Search API
  slug: open-microsoft-net-search-api
- collection_type: open
  name: NuGet Server API (V3) PackageContent ServiceIndex API
  slug: open-microsoft-net-serviceindex-api
- collection_type: open
  name: NuGet Server API (V3)
  slug: open-microsoft-net
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-net-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-net-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-net-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-net-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://dotnet.microsoft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/dotnet/
- group: start
  title: ''
  type: GettingStarted
  url: https://dotnet.microsoft.com/learn
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/dotnet/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotnet
- group: operate
  title: ''
  type: Support
  url: https://dotnet.microsoft.com/platform/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/dotnet
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/.net
- group: other
  title: ''
  type: X
  url: https://twitter.com/dotnet
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/dotnet/core/blob/main/release-notes/README.md
- group: build
  title: ''
  type: SDKs
  url: https://dotnet.microsoft.com/download
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/dotnet/
created: '2024-01-01'
description: Microsoft .NET is a free, cross-platform, open source developer platform for building many different types of applications. The .NET APIs and developer tools provide programmatic access to .NET runtime services, NuGet package management, project templates, and build tooling across web, mobile, desktop, games, IoT, cloud, and microservices workloads.
features:
- description: Build and run .NET applications on Windows, macOS, and Linux with full platform support.
  name: Cross-Platform Development
- description: .NET runtime with JIT compilation, garbage collection, and ahead-of-time compilation for optimal performance.
  name: High Performance Runtime
- description: Access over 350,000 packages through the NuGet package manager for rapid development.
  name: NuGet Package Ecosystem
- description: Build lightweight HTTP APIs with minimal code using the minimal API pattern in ASP.NET Core.
  name: Minimal APIs
- description: Built-in support for containers, Kubernetes, microservices, and cloud deployment through .NET Aspire.
  name: Cloud Native Support
- description: Apply code changes to running applications without restarting for faster development cycles.
  name: Hot Reload
finops:
- name: Microsoft Net Finops
  service_category: API
  slug: microsoft-net-finops
image: /assets/icons/microsoft-net.png
integrations:
- description: Deep integration with Microsoft Azure cloud services including App Service, Functions, and Container Apps.
  name: Azure
- description: Full IDE support with IntelliSense, debugging, profiling, and project templates in Visual Studio.
  name: Visual Studio
- description: Lightweight development with the C# Dev Kit extension for Visual Studio Code.
  name: VS Code
- description: CI/CD pipeline integration with GitHub Actions for .NET build, test, and deploy workflows.
  name: GitHub Actions
- description: Container support with official .NET Docker images and multi-stage build templates.
  name: Docker
- description: Object-relational mapping for database access with support for SQL Server, PostgreSQL, SQLite, and more.
  name: Entity Framework Core
layout: provider
modified: '2026-04-18'
name: Microsoft .NET
nav: Providers
network: true
overview: 'Microsoft .NET publishes 4 APIs on the [APIs.io](https://apis.io/) network, including PackageContent API, Registration API, Search API, and 1 more. Tagged areas include .NET, C#, Cloud, Cross-Platform, and Developer Tools.


  Microsoft .NET''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, YouTube channel, and 11 more developer resources.'
plans:
- name: Microsoft Net Plans Pricing
  plan_count: 3
  slug: microsoft-net-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Microsoft Net Rate Limits
  slug: microsoft-net-rate-limits
score:
  band: developing
  composite: 42.2
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 57.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 42.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-net/refs/heads/main/screenshots/microsoft-net-2026-06-20T185509.png
security:
- kind: authentication
  name: Microsoft Net Authentication
  slug: microsoft-net-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Net Domain Security
  slug: microsoft-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Net Vulnerability Disclosure
  slug: microsoft-net-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-net
tags:
- .NET
- C#
- Cloud
- Cross-Platform
- Developer Tools
- Microsoft
- Open-Source
use_cases:
- description: Build scalable enterprise web applications using ASP.NET Core with authentication, authorization, and data access.
  name: Enterprise Web Applications
- description: Design and deploy microservices using .NET with gRPC, message queues, and service discovery.
  name: Microservices Architecture
- description: Develop cloud-native applications with .NET Aspire, containers, and Azure integration.
  name: Cloud-Native Applications
- description: Create production-ready REST APIs with OpenAPI documentation, versioning, and rate limiting.
  name: RESTful API Development
- description: Build Windows desktop applications using WPF, WinForms, or .NET MAUI for cross-platform desktop.
  name: Desktop Applications
website: https://dotnet.microsoft.com/
---
