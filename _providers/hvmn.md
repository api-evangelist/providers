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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Agent-native commerce surface for the Ketone-IQ (HVMN) Shopify store: a Universal Commerce Protocol (UCP) merchant profile and live MCP endpoint for catalog search, cart, and buyer-approved checkout, '
  name: Ketone-IQ Agent Commerce (UCP)
  slug: ketone-iq-agent-commerce-ucp
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hvmn-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hvmn-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hvmn-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hvmn-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hvmn-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/hvmn-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hvmn-conformance.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ketone.com/agents.md
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ketone.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ketone.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://account.ketone.com
- group: commercial
  title: ''
  type: Pricing
  url: https://ketone.com/collections/all
- group: company
  title: ''
  type: Website
  url: https://ketone.com
created: '2026-07-17'
description: 'HVMN (Health Via Modern Nutrition), now operating as Ketone-IQ, is an a16z-backed human-performance nutrition company founded by Geoffrey Woo and Michael Brandt. It pioneered exogenous ketone products, including the Ketone-IQ drinkable ketone shot and ketone ester, sold direct-to-consumer through its Shopify-powered online store at ketone.com (hvmn.com now redirects to ketone.com). The storefront is agent-native: it publishes /llms.txt and /agents.md agent instructions and implements the Universal Commerce Protocol (UCP) with a live MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout, backed by Shopify Customer Account OAuth 2.0 / OpenID Connect authentication.'
image: https://ketone.com/cdn/shop/files/OG_Home_Page_1200x1200.jpg?v=1781009088
layout: provider
mcp_servers:
- description: ''
  name: HVMN MCP Server
  slug: hvmn-mcp-server
modified: '2026-07-19'
name: HVMN
nav: Providers
network: true
overview: 'HVMN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Nutrition, Ketones, and Supplements.


  HVMN''s developer surface includes authentication, documentation, pricing, and 10 more developer resources.'
random_paper: 0
scopes:
- name: Hvmn Scopes
  scope_count: 4
  slug: hvmn-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hvmn/refs/heads/main/screenshots/hvmn-2026-08-07T170422.png
security:
- kind: authentication
  name: Hvmn Authentication
  slug: hvmn-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Hvmn Domain Security
  slug: hvmn-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hvmn
tags:
- Company
- Health
- Nutrition
- Ketones
- Supplements
- E-Commerce
- Shopify
- Agentic Commerce
- Consumer
- MCP
website: https://ketone.com
---
