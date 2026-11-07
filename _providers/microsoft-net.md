---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Microsoft Net Agentic Access
  operation_count: 7
  slug: microsoft-net-agentic-access
  summary_line: 7 operations
api_count: 10
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
- baseURL: https://api.nuget.org/v3
  baseurl_source: declared
  description: The PackageContent API from Microsoft .NET — 3 operation(s) for packagecontent.
  name: Microsoft .NET PackageContent API
  slug: microsoft-net-packagecontent-api
- baseURL: https://api.nuget.org/v3
  baseurl_source: declared
  description: The Registration API from Microsoft .NET — 2 operation(s) for registration.
  name: Microsoft .NET Registration API
  slug: microsoft-net-registration-api
- baseURL: https://api.nuget.org/v3
  baseurl_source: declared
  description: The Search API from Microsoft .NET — 1 operation(s) for search.
  name: Microsoft .NET Search API
  slug: microsoft-net-search-api
- description: Comprehensive reference documentation for all .NET APIs including the .NET Runtime, base class libraries, ASP.NET Core, Entity Framework, and Azure SDK libraries. Browse types, members, namespaces, an
  name: .NET API Browser
  slug: net-api-browser
- baseURL: https://api.nuget.org/v3
  baseurl_source: declared
  description: The Service Index API from Microsoft .NET — 1 operation(s) for service index.
  name: Microsoft .NET Service Index API
  slug: microsoft-net-service-index-api
artifact_total: 48
collections:
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
- group: other
  href: https://artifacts.apis.io/microsoft-net/capabilities/microsoft-net-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-net-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/microsoft-net/rules/microsoft-net-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-net-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-net/json-ld/microsoft-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-net/vocabulary/microsoft-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-net-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/microsoft-net/hosts/microsoft-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-net/vendors/microsoft-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-net-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://dotnet.microsoft.com/
- group: build
  href: https://artifacts.apis.io/microsoft-net/packages/microsoft-net-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-net-packages.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-net/well-known/microsoft-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-net-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-net/well-known/microsoft-net-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-net-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/en-us/msrc/cvd
- group: auth
  href: https://artifacts.apis.io/microsoft-net/security/microsoft-net-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-net-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: agent
  href: https://artifacts.apis.io/microsoft-net/mcp/microsoft-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-net-mcp.yml
- group: build
  href: https://artifacts.apis.io/microsoft-net/mcp/microsoft-net-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-net-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-net/llms/microsoft-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-net-llms.txt
- group: design
  href: https://artifacts.apis.io/microsoft-net/conformance/microsoft-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-net-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-net/errors/microsoft-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-net/lifecycle/microsoft-net-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-net-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nuget.org/
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/dotnet/core/compatibility/
- group: design
  href: https://artifacts.apis.io/microsoft-net/conventions/microsoft-net-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-net-conventions.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-net/changelog/microsoft-net-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-net-changelog.yml
- group: build
  href: https://artifacts.apis.io/microsoft-net/cli/microsoft-net-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-net-cli.yml
- group: start
  href: https://artifacts.apis.io/microsoft-net/sandbox/microsoft-net-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-net-sandbox.yml
- group: design
  href: https://artifacts.apis.io/microsoft-net/data-model/microsoft-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-net-data-model.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-net/rate-limits/microsoft-net-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-net-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-net/plans/microsoft-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-net-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-net/finops/microsoft-net-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-net-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-net/overlays/microsoft-net-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-net-search-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-net/overlays/microsoft-net-serviceindex-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-net-serviceindex-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-net/overlays/microsoft-net-registration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-net-registration-overlay.yaml
- group: other
  href: https://artifacts.apis.io/microsoft-net/overlays/microsoft-net-packagecontent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-net-packagecontent-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/dotnet/api/
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/dotnet/core/blob/main/roadmap.md
- group: start
  title: ''
  type: SignUp
  url: https://www.nuget.org/users/account/LogOn
- group: operate
  title: ''
  type: Community
  url: https://dotnet.microsoft.com/en-us/platform/community
- group: agent
  href: https://artifacts.apis.io/microsoft-net/agentic-access/microsoft-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-net-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-net/security/microsoft-net-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-net-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-net/security/microsoft-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-net-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-net/authentication/microsoft-net-authentication.yml
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
- has_sources: true
  method: derived
  name: Microsoft Net Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-net-finops
  template: true
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
json_schemas:
- name: SearchResponse
  property_count: 2
  slug: microsoft-net-search-response
- name: ServiceIndex
  property_count: 2
  slug: microsoft-net-service-index
jsonld:
- class_count: 3
  name: Microsoft Net Context
  property_count: 17
  slug: microsoft-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at learn.microsoft.com; 3 tools listed.
  name: Microsoft .NET MCP Server
  slug: microsoft-net-mcp-yml
modified: '2026-08-29'
name: Microsoft .NET
nav: Providers
network: true
overview: 'Microsoft .NET is listed with 10 APIs on the [APIs.io](https://apis.io/) network, including PackageContent API, Registration API, Search API, and 7 more. Tagged areas include .NET, C#, Cloud, Cross-Platform, and Developer Tools.


  The Microsoft .NET catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft .NET''s developer surface includes changelog, CLI, sandbox, API reference, signup flow, authentication, developer portal, and 49 more developer resources.'
plans:
- name: Microsoft Net Plans Pricing
  plan_count: 0
  slug: microsoft-net-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 8
  name: Microsoft Net Rate Limits
  slug: microsoft-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Microsoft .NET API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-net-rules
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 35
    catalog_earned: 66.2
    catalog_earned_first_party: 12.0
    catalog_gap: 48.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 35.6
    contract_quality: 53.2
    developer_ergonomics: 80.4
    discoverability: 78.3
    operational_transparency: 89.5
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/microsoft-net/microsoft-net-2026-06-20T185509.png
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
- kind: trust-center
  name: Microsoft Net Trust Center
  slug: microsoft-net-trust-center
  summary_line: SOC 1, SOC 2, ISO/IEC 27001, ISO/IEC 27018, HIPAA, FedRAMP, GDPR
skill_count: 3
skills:
- name: audit-dotnet-dependencies-for-known-vulnerabilities
  slug: microsoft-net-audit-dependencies-for-vulnerabilities
- name: find-and-install-nuget-package
  slug: microsoft-net-find-and-install-a-package
- name: publish-and-unpublish-nuget-package
  slug: microsoft-net-publish-and-unpublish-a-package
slug: microsoft-net
tags:
- .NET
- C#
- Cloud
- Cross-Platform
- Developer Tools
- Microsoft
- Open Source
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
