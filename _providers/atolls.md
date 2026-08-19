---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/atolls-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://atolls.com/disclosure-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atolls-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atolls.com
- group: company
  title: ''
  type: About
  url: https://atolls.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://atolls.com/insights/
- group: company
  title: ''
  type: Careers
  url: https://atolls.com/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atolls.com/privacy-policy/
- group: other
  title: ''
  type: Imprint
  url: https://atolls.com/imprint/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/atolls-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/atolls-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/atolls-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/atolls-mydealz-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/atolls-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atolls-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atolls-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atolls-llms.txt
created: '2026-07-17'
description: 'Atolls (formerly Global Savings Group) is a Munich-based consumer commerce-content company that operates the world''s largest shopping engagement platform, running coupon, cashback, deals, and shopping-community destinations across more than 20 markets. Its brand portfolio includes Coupons.com, Cuponation, iGraal, Shoop, Pouch, mydealz, hotukdeals, and Deala, connecting millions of shoppers with offers from thousands of retailers and brands through affiliate marketing, cashback, and AI-enhanced shopping insights. Founded in 2012 as CupoNation with Rocket Internet and rebranded to Atolls in 2024, it is backed by investors including HV Capital, RTP Global, and Rocket Internet. Atolls publishes no public developer API, developer portal, OpenAPI document or SDK — api., developer. and docs.atolls.com do not resolve — but it does serve real machine-readable documents: RFC 9116 security.txt files on five owned hosts pointing at a single group-wide Intigriti vulnerability disclosure
  program, and OpenID Connect discovery documents on seven Pepper community properties (mydealz, hotukdeals, Dealabs, Preisjaeger, Chollometro, Pepper PL, Promodescuentos) that expose an OAuth 2.0 authorization server for consumer sign-in. This profile captures that security, identity, and legal surface for the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atolls.png
layout: provider
modified: '2026-08-13'
name: Atolls
nav: Providers
network: true
overview: 'Atolls is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Affiliate Marketing, and Cashback.


  Atolls'' developer surface includes engineering blog, authentication, and 15 more developer resources.'
random_paper: 59
scopes:
- name: Atolls Scopes
  scope_count: 0
  slug: atolls-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.4
  delta: 1.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 14.4
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atolls/refs/heads/main/screenshots/atolls-2026-07-25T201556.png
security:
- kind: authentication
  name: Atolls Authentication
  slug: atolls-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atolls Domain Security
  slug: atolls-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Atolls Vulnerability Disclosure
  slug: atolls-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: atolls
tags:
- Company
- Consumer
- E-Commerce
- Affiliate Marketing
- Cashback
- Coupons
- Shopping
- Retail
- Identity
- OpenID Connect
website: https://atolls.com
---
