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
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://tincan.kids/
- group: operate
  title: ''
  type: Support
  url: https://faq.tincan.com/
- group: company
  title: ''
  type: Blog
  url: https://tincan.kids/blogs/news
- group: start
  title: ''
  type: Login
  url: https://tincan.kids/account/login
- group: commercial
  title: ''
  type: Pricing
  url: https://tincan.kids/products/tin-can
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tincan.kids/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tincan.kids/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tin-can-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tin-can-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tin-can-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tin-can-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tin-can-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tin-can-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tin-can-domain-security.yml
created: '2026-07-17'
description: Tin Can is a Seattle-based consumer hardware company behind a screen-free, landline-style Wi-Fi phone for kids — no apps, texting, or games, just voice calls with contacts that parents approve through a companion mobile app, with free unlimited calling between Tin Can devices. Backed by Greylock (which led a $12M round in 2025, bringing total funding to roughly $15.5M). Tin Can publishes no first-party developer API; its agent-facing surface is the Shopify-hosted storefront, which exposes a live MCP server, a UCP merchant profile, an llms.txt, and Shopify Customer Accounts OIDC on the tincan.kids domain.
image: https://tincan.kids/cdn/shop/files/tinothy-icon.svg
layout: provider
mcp_servers:
- description: ''
  name: Tin Can MCP Server
  slug: tin-can-mcp-server
modified: '2026-07-21'
name: Tin Can
nav: Providers
network: true
overview: 'Tin Can is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Hardware, Telecommunications, and Voice.


  Tin Can''s developer surface includes support, engineering blog, pricing, authentication, and 10 more developer resources.'
random_paper: 10
scopes:
- name: Tin Can Scopes
  scope_count: 4
  slug: tin-can-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 23.7
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 58.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tin-can/refs/heads/main/screenshots/tin-can-2026-09-02T163811.png
security:
- kind: authentication
  name: Tin Can Authentication
  slug: tin-can-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Tin Can Domain Security
  slug: tin-can-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tin-can
tags:
- Company
- Consumer
- Hardware
- Telecommunications
- Voice
- Kids
- Phones
website: https://tincan.kids/
---
