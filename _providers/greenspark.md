---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 38
  human_in_the_loop: 1
  name: Greenspark Agentic Access
  operation_count: 67
  slug: greenspark-agentic-access
  summary_line: 67 operations · 38 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.getgreenspark.com
  baseurl_source: declared
  description: The Account API from Greenspark — 3 operation(s) for account.
  name: Greenspark Account API
  slug: greenspark-account-api
- baseURL: https://api.getgreenspark.com
  baseurl_source: declared
  description: The Email API from Greenspark — 14 operation(s) for email.
  name: Greenspark Email API
  slug: greenspark-email-api
- baseURL: https://api.getgreenspark.com
  baseurl_source: declared
  description: The Estimations API from Greenspark — 4 operation(s) for estimations.
  name: Greenspark Estimations API
  slug: greenspark-estimations-api
- baseURL: https://api.getgreenspark.com
  baseurl_source: declared
  description: The Impacts API from Greenspark — 5 operation(s) for impacts.
  name: Greenspark Impacts API
  slug: greenspark-impacts-api
- baseURL: https://api.getgreenspark.com
  baseurl_source: declared
  description: The Projects API from Greenspark — 3 operation(s) for projects.
  name: Greenspark Projects API
  slug: greenspark-projects-api
- baseURL: https://api.getgreenspark.com
  baseurl_source: declared
  description: The Reports API from Greenspark — 15 operation(s) for reports.
  name: Greenspark Reports API
  slug: greenspark-reports-api
- baseURL: https://api.getgreenspark.com
  baseurl_source: declared
  description: The Widgets API from Greenspark — 17 operation(s) for widgets.
  name: Greenspark Widgets API
  slug: greenspark-widgets-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Greenspark Climate Account API
  slug: open-greenspark-account-api
- collection_type: open
  name: Greenspark Climate Account Email API
  slug: open-greenspark-email-api
- collection_type: open
  name: Greenspark Climate Account Estimations API
  slug: open-greenspark-estimations-api
- collection_type: open
  name: Greenspark Climate Account Impacts API
  slug: open-greenspark-impacts-api
- collection_type: open
  name: Greenspark Climate Account Projects API
  slug: open-greenspark-projects-api
- collection_type: open
  name: Greenspark Climate Account Reports API
  slug: open-greenspark-reports-api
- collection_type: open
  name: Greenspark Climate Account Widgets API
  slug: open-greenspark-widgets-api
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
- description: 'Greenspark operates an official remote MCP server hosted by ReadMe at https://docs.getgreenspark.com/mcp. v1 is read-only: it exposes the Greenspark OpenAPI specs and guides for schema-aware answers, '
  name: Greenspark MCP Server
  slug: greenspark-mcp-server
modified: '2026-07-19'
name: Greenspark
nav: Providers
network: true
overview: 'Greenspark publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Email API, Estimations API, and 4 more. Tagged areas include Sustainability, Carbon Offset, Climate, Impact, and Carbon Estimation.


  Greenspark''s developer surface includes documentation, API reference, support, pricing, signup flow, authentication, sandbox, and 21 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 41.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 59.0
    developer_ergonomics: 51.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 41.8
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
