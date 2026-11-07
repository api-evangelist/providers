---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: BuyLater provides an MCP server for AI assistants to save and list products. Documentation is at https://buylater.com/docs. No public OpenAPI spec is available.
  name: BuyLater API
  slug: buylater-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/buylater-com/authentication/buylater-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buylater-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/buylater-com/mcp/buylater-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/buylater-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/buylater-com/well-known/buylater-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buylater-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/buylater-com/hosts/buylater-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buylater-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/buylater-com/vendors/buylater-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buylater-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buylater.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buylater.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://buylater.com/docs
- group: auth
  href: https://artifacts.apis.io/buylater-com/security/buylater-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buylater-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buylater.com/
coverage:
  checked: '2026-11-03'
  detail: Docs page renders via JavaScript and provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://buylater.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: BuyLater is a service that lets users save products they intend to purchase later, providing notifications when items are back in stock, price drops, or new models release. It offers an MCP server for AI assistants like Claude and ChatGPT to interact, using OAuth 2.1 via Clerk for password‑less sign‑in. The platform is currently in beta, with email support via hello@buylater.com.
image: https://buylater.com/opengraph-image?5302567b386c0d21
layout: provider
mcp_servers:
- description: Remote MCP server at buylater.com requiring OAuth.
  name: BuyLater MCP Server
  slug: buylater-com-mcp-yml
modified: '2026-11-03'
name: BuyLater
nav: Providers
network: true
overview: 'BuyLater is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Notification, AI Assistant, MCP, and Shopping.


  BuyLater''s developer surface includes authentication, documentation, and 8 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Buylater Com Authentication
  slug: buylater-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Buylater Com Domain Security
  slug: buylater-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buylater-com
tags:
- E-Commerce
- Notification
- AI Assistant
- MCP
- Shopping
website: https://buylater.com/
---
