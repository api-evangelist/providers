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
    agent_skills: true
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
  score: 23.9
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://becausemarket.com
- group: company
  title: ''
  type: Blog
  url: https://becausemarket.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://becausemarket.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://becausemarket.com/pages/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://becausemarket.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://becausemarket.com/policies/terms-of-service
- group: start
  title: ''
  type: SignUp
  url: https://becausemarket.com/account/register
- group: start
  title: ''
  type: Login
  url: https://becausemarket.com/account/login
- group: agent
  title: ''
  type: MCPServer
  url: mcp/because-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/because-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/because-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/because-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/because-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/because-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/because-domain-security.yml
created: '2026-07-17'
description: 'Because (Because Market) is a direct-to-consumer retail brand selling bladder protection, incontinence products, skincare, supplements and other everyday health essentials for older adults, trusted by over one million customers and also distributed through Walmart, CVS, Amazon and Target. The storefront runs on Shopify at becausemarket.com and exposes a modern agentic-commerce surface: a published llms.txt / agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a hosted MCP shopping endpoint, and Shopify Customer Account OIDC. Surfaced as an Index Ventures portfolio company and profiled by the API Evangelist enrichment pipeline. It has no separately published first-party developer API; agents transact via the UCP shopping service with human approval required at payment.'
image: https://becausemarket.com/cdn/shop/files/logo_0dbfcfd7-0598-4066-b687-a768edfab4ca.webp?crop=center&height=1200&v=1669043821&width=1200
layout: provider
mcp_servers:
- description: ''
  name: Because UCP shopping MCP
  slug: because-ucp-shopping-mcp
modified: '2026-07-18'
name: Because
nav: Providers
network: true
overview: 'Because is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Health, and Incontinence.


  Because''s developer surface includes engineering blog, support, signup flow, authentication, and 12 more developer resources.'
random_paper: 14
scopes:
- name: Because Scopes
  scope_count: 4
  slug: because-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/because/refs/heads/main/screenshots/because-2026-08-07T162251.png
security:
- kind: authentication
  name: Because Authentication
  slug: because-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Because Domain Security
  slug: because-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: because
tags:
- Company
- Retail
- E-Commerce
- Health
- Incontinence
- Senior Care
- Agentic Commerce
- Shopify
website: https://becausemarket.com
---
