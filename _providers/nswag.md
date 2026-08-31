---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: NSwag is an open source .NET toolchain for generating C# and TypeScript API clients and Swagger/OpenAPI specifications from ASP.NET controllers and vice versa. It ships as NuGet packages, MSBuild targ
  name: NSwag
  slug: nswag
artifact_total: 6
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/RicoSuter/NSwag/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/RicoSuter/NSwag/blob/master/CONTRIBUTING.md
- group: company
  title: ''
  type: Website
  url: https://github.com/RicoSuter/NSwag
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/RicoSuter/NSwag/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/RicoSuter/NSwag/wiki/Getting-Started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RicoSuter/NSwag
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/RicoSuter/NSwag
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/RicoSuter/NSwag/wiki/Roadmap
- group: operate
  title: ''
  type: Support
  url: https://github.com/RicoSuter/NSwag/issues
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/BxQNy25WF6
- group: commercial
  title: ''
  type: License
  url: https://github.com/RicoSuter/NSwag/blob/master/LICENSE.md
- group: build
  title: ''
  type: Packages
  url: packages/nswag-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nswag-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nswag-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nswag-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nswag-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nswag-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nswag-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nswag-llms.txt
created: '2026-03-25'
description: 'NSwag is the Swagger/OpenAPI toolchain for .NET, ASP.NET Core and TypeScript, written in C# and maintained by Rico Suter under an MIT licence. It runs the contract in both directions: generating Swagger 2.0 and OpenAPI 3.0 documents from ASP.NET (Core) controllers, Web API assemblies and plain .NET types, and generating C# clients, ASP.NET Web API controllers and TypeScript clients back out of those documents. It combines what Swashbuckle and AutoRest do separately into a single toolchain, which is how it avoids the incompatibility seams between the two and gets better fidelity on inheritance, enums and reference handling via NJsonSchema. NSwag operates no hosted API of its own — it is consumed as NuGet packages, MSBuild targets, an npm-distributed CLI and NSwagStudio, a Windows GUI that authors and executes the same nswag.json configuration document the CLI runs.'
finops:
- name: Nswag Finops
  service_category: API
  slug: nswag-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nswag.png
json_schemas:
- name: Nswag Configuration Document.Schema
  property_count: 2
  slug: nswag-configuration-document.schema
layout: provider
modified: '2026-08-06'
name: NSwag
nav: Providers
network: true
overview: 'NSwag publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, ASP.NET Core, C#, Code Generation, and Developer Tools.


  NSwag''s developer surface includes documentation, getting-started guide, support, CLI, changelog, and 14 more developer resources.'
plans:
- name: Nswag Plans Pricing
  plan_count: 3
  slug: nswag-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Nswag Rate Limits
  slug: nswag-rate-limits
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 2.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 31.6
  open_source:
    applies: true
    score: 50.0
  previous_composite: 24.2
  provenance:
    conformance: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nswag/refs/heads/main/screenshots/nswag-2026-06-20T190459.png
security:
- kind: domain-security
  name: Nswag Domain Security
  slug: nswag-domain-security
  summary_line: no transport/DNS hardening detected
slug: nswag
tags:
- .NET
- ASP.NET Core
- C#
- Code Generation
- Developer Tools
- JSON-Schema
- Open-Source
- OpenAPI
- SDK
- Swagger
- TypeScript
---
