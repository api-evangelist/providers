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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://casper.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/casper-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/casper-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/casper-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/casper-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/casper-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/casper-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/casper-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://casper.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://casper.com/policies/terms-of-service
created: '2026-07-17'
description: 'Casper (Casper Sleep Inc.) is a direct-to-consumer sleep and home goods brand that sells mattresses, bedding, pillows, and sleep accessories online at casper.com and through retail partners. Its casper.com storefront runs on Shopify and exposes a modern agentic-commerce surface: a published llms.txt/agents.md with agent instructions, the Universal Commerce Protocol (UCP) merchant profile, a UCP shopping MCP endpoint for AI agents to search, cart, and check out, and Shopify Customer Account API OpenID Connect authentication. Casper was added to the API Evangelist network as a portfolio company of IVP and Slow Ventures and enriched from its live public agent/commerce surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/casper.png
layout: provider
mcp_servers:
- description: ''
  name: Casper UCP shopping MCP
  slug: casper-ucp-shopping-mcp
modified: '2026-07-18'
name: Casper
nav: Providers
network: true
overview: 'Casper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Sleep, and Mattresses.


  Casper''s developer surface includes authentication and 9 more developer resources.'
random_paper: 8
scopes:
- name: Casper Scopes
  scope_count: 4
  slug: casper-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.3
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/casper/refs/heads/main/screenshots/casper-2026-08-07T163102.png
security:
- kind: authentication
  name: Casper Authentication
  slug: casper-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Casper Domain Security
  slug: casper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: casper
tags:
- Company
- E-Commerce
- Retail
- Sleep
- Mattresses
- Direct to Consumer
- Agentic Commerce
- Shopify
website: https://casper.com
---
