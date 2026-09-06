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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 10.8
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.byheart.com
- group: start
  title: ''
  type: SignUp
  url: https://byheart.com/account/login
- group: start
  title: ''
  type: Login
  url: https://byheart.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://byheart.com/pages/byheart-faqs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://byheart.com/pages/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://byheart.com/pages/terms-and-conditions
- group: agent
  title: ''
  type: WellKnown
  url: well-known/byheart-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/byheart-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/byheart-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/byheart-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/byheart-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/byheart-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/byheart-domain-security.yml
created: '2026-07-17'
description: ByHeart is a US infant-nutrition company founded in 2016 that makes Whole Nutrition Infant Formula, marketed on the promise of better science, better ingredients, and better quality. It sells direct-to-consumer through a Shopify storefront at byheart.com as well as through retail. The company ran its own clinical program and built its own manufacturing. In November 2025 ByHeart recalled all batches after Clostridium botulinum contamination linked to infant-botulism cases and paused production pending FDA clearance to resume. ByHeart is a portfolio company of D1 Capital. It publishes no first-party developer API; its only machine-discoverable surface is the Shopify Customer Account API (OpenID Connect / OAuth 2.0) advertised under its domain.
image: https://www.byheart.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: ByHeart MCP Server
  slug: byheart-mcp-server
modified: '2026-07-18'
name: ByHeart
nav: Providers
network: true
overview: 'ByHeart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Infant Nutrition, Baby Formula, and Direct to Consumer.


  ByHeart''s developer surface includes signup flow, support, authentication, and 10 more developer resources.'
random_paper: 16
scopes:
- name: Byheart Scopes
  scope_count: 4
  slug: byheart-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 7
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
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.4
  provenance:
    conformance: first-party
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
screenshot: https://raw.githubusercontent.com/api-evangelist/byheart/refs/heads/main/screenshots/byheart-2026-08-07T162852.png
security:
- kind: authentication
  name: Byheart Authentication
  slug: byheart-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Byheart Domain Security
  slug: byheart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: byheart
tags:
- Company
- Consumer
- Infant Nutrition
- Baby Formula
- Direct to Consumer
- E-Commerce
- Health
- Shopify
website: https://www.byheart.com
---
