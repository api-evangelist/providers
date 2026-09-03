---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Client-side JavaScript/TypeScript Plugin API (the `snaptrude` global namespace) for extending the Snaptrude platform. Organized by namespace — Core, Design, Entity, Program, Presentation, Analysis — p
  name: Snaptrude Plugin API
  slug: snaptrude-plugin-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.snaptrude.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snaptrude.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.snaptrude.com/plugin-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snaptrude.com/plugin-api/plugin-development.html
- group: company
  title: ''
  type: Blog
  url: https://www.snaptrude.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.snaptrude.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.snaptrude.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.snaptrude.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://help.snaptrude.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.snaptrude.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snaptrude
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/snaptrude-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/snaptrude-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/snaptrude-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/snaptrude-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snaptrude-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/snaptrude-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/snaptrude-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/snaptrude-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/snaptrude-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snaptrude-domain-security.yml
created: '2026-07-17'
description: Snaptrude is a cloud-native design platform for architecture and interior design that unifies sketching, real-time collaboration, AI-assisted programming, and BIM into a single browser-based tool. Snaptrude 3.0 offers four integrated modes — Program, Design Canvas, Present, and BIM — that turn concept massing into Revit-ready assemblies while surfacing live metrics (GFA, FAR, cost, daylight). For developers, Snaptrude publishes a client-side Plugin API (the `snaptrude` namespace) documented at docs.snaptrude.com, with official @snaptrude npm packages and a create-snaptrude-plugin CLI to scaffold, register, and update React + TypeScript plugins. Backed by Accel.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snaptrude.png
layout: provider
modified: '2026-07-21'
name: Snaptrude
nav: Providers
network: true
overview: 'Snaptrude publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Design, Architecture, BIM, and 3D Modeling.


  Snaptrude''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, CLI, and 14 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 26.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snaptrude/refs/heads/main/screenshots/snaptrude-2026-09-02T160013.png
security:
- kind: authentication
  name: Snaptrude Authentication
  slug: snaptrude-authentication
  summary_line: session · 2 schemes
- kind: domain-security
  name: Snaptrude Domain Security
  slug: snaptrude-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: snaptrude
tags:
- Company
- Design
- Architecture
- BIM
- 3D Modeling
- AEC
- Plugins
- Developer Tools
- Software-as-a-Service
website: https://www.snaptrude.com/
---
