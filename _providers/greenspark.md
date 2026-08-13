---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Greenspark Agentic Access
  operation_count: 67
  slug: greenspark-agentic-access
  summary_line: 67 operations · 38 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: The Account API from Greenspark — 3 operation(s) for account.
  name: Greenspark Account API
  slug: greenspark-account-api
- description: The Email API from Greenspark — 14 operation(s) for email.
  name: Greenspark Email API
  slug: greenspark-email-api
- description: The Estimations API from Greenspark — 4 operation(s) for estimations.
  name: Greenspark Estimations API
  slug: greenspark-estimations-api
- description: The Impacts API from Greenspark — 5 operation(s) for impacts.
  name: Greenspark Impacts API
  slug: greenspark-impacts-api
- description: The Projects API from Greenspark — 3 operation(s) for projects.
  name: Greenspark Projects API
  slug: greenspark-projects-api
- description: The Reports API from Greenspark — 15 operation(s) for reports.
  name: Greenspark Reports API
  slug: greenspark-reports-api
- description: The Widgets API from Greenspark — 17 operation(s) for widgets.
  name: Greenspark Widgets API
  slug: greenspark-widgets-api
artifact_total: 11
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.getgreenspark.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getgreenspark.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.getgreenspark.com/reference
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getgreenspark
- group: operate
  title: ''
  type: Support
  url: mailto:support@getgreenspark.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getgreenspark.com/pricing/business
- group: start
  title: ''
  type: SignUp
  url: https://app.getgreenspark.com/login
- group: start
  title: ''
  type: Login
  url: https://app.getgreenspark.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getgreenspark.com/utility/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.privasee.io/privacy-portal/61a7587adcff740014657fbf
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/greenspark-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/greenspark-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/greenspark-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greenspark-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/greenspark-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/greenspark-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/greenspark-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/greenspark-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/greenspark-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/greenspark-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/greenspark-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/greenspark-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/greenspark-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/greenspark-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/greenspark-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/greenspark-changelog.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/greenspark-openapi-overlay.yaml
created: '2026-07-17'
description: Greenspark is an Impact-as-a-Service platform that lets businesses embed climate and environmental action into their products and customer journeys. Its Climate API programmatically funds verified impacts — carbon offset, tree planting, ocean-plastic recovery, kelp restoration, clean water and bee protection — and provides carbon-footprint estimation (by Merchant Category Code or Open Banking category), impact reporting, email/notification templates, and embeddable impact widgets for storefronts. Authentication is a single x-api-key header with separate sandbox, demo and production environments. Greenspark ships six first-party TypeScript SDKs, a ReadMe-hosted MCP server, and packaged Agent Skills. Backed by Anthemis; profiled and enriched by the API Evangelist network.
image: https://cdn.prod.website-files.com/611391a1477389e3857d8014/64cb3773a1ba8a68d73a88ad_greenspark-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: greenspark-mcp.yml
  slug: greenspark-mcpyml
modified: '2026-07-19'
name: Greenspark
nav: Providers
network: true
overview: 'Greenspark publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Email API, Estimations API, and 4 more. Tagged areas include Sustainability, Carbon Offset, Climate, Impact, and Carbon Estimation.


  Greenspark''s developer surface includes documentation, API reference, support, pricing, signup flow, authentication, sandbox, and 21 more developer resources.'
random_paper: 114
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 62.0
    developer_ergonomics: 67.4
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/greenspark/refs/heads/main/screenshots/greenspark-2026-07-25T220317.png
security:
- kind: authentication
  name: Greenspark Authentication
  slug: greenspark-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Greenspark Domain Security
  slug: greenspark-domain-security
  summary_line: TLSv1.3 · DMARC
slug: greenspark
tags:
- Sustainability
- Carbon Offset
- Climate
- Impact
- Carbon Estimation
- Reporting
- ESG
- Fintech
website: https://docs.getgreenspark.com
---
