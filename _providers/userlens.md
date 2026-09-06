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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://events.userlens.io
  baseurl_source: declared
  description: User identification, company grouping, and event ingestion
  name: Userlens Events API
  slug: userlens-events-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Userlens Events API
  slug: open-userlens-events-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/userlens-events-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/userlens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://userlens.io
- group: docs
  title: ''
  type: Documentation
  url: https://userlens.gitbook.io/userlens-analytics
- group: docs
  title: ''
  type: APIReference
  url: https://userlens.gitbook.io/userlens-analytics/guides/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://userlens.gitbook.io/userlens-analytics/getting-started/http-api
- group: commercial
  title: ''
  type: Pricing
  url: https://userlens.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://userlens.io/blog
- group: start
  title: ''
  type: Login
  url: https://app.userlens.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://userlens.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://userlens.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wudpecker
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/userlens-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/userlens-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/userlens-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/userlens-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/userlens-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/userlens-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://userlens.io/llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/userlens-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/userlens-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/userlens-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/userlens-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/userlens-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Userlens is an AI-native customer success platform for B2B SaaS that deploys LLM-powered agents to monitor every customer account, predict churn from actual product usage, and surface expansion opportunities. It ingests product analytics, CRM data, and business context for AI health scores, account-level analytics, and proactive alerts, and exposes a Write-Code-authenticated Events API (identify, group, track, and batched SDK event forwarding) plus JavaScript SDKs for instrumentation. Founded in 2025 (Y Combinator Spring 2026 batch), based in San Francisco and Helsinki.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/userlens.png
layout: provider
mcp_servers:
- description: ''
  name: Userlens MCP Server
  slug: userlens-mcp-server
modified: '2026-07-21'
name: Userlens
nav: Providers
network: true
overview: 'Userlens publishes 1 API on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Company, Customer Success, Product Analytics, AI Agents, and Churn Prediction.


  Userlens'' developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, authentication, and 19 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 14.8
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 35.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/userlens/refs/heads/main/screenshots/userlens-2026-09-02T165238.png
security:
- kind: authentication
  name: Userlens Authentication
  slug: userlens-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Userlens Domain Security
  slug: userlens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: userlens
tags:
- Company
- Customer Success
- Product Analytics
- AI Agents
- Churn Prediction
- Event Tracking
- B2B SaaS
- Account Intelligence
website: https://userlens.io
---
