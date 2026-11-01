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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/atolls/well-known/atolls-shoop-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atolls-shoop-security.txt
- group: auth
  href: https://artifacts.apis.io/atolls/well-known/atolls-mydealz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atolls-mydealz-security.txt
- group: auth
  href: https://artifacts.apis.io/atolls/well-known/atolls-igraal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atolls-igraal-security.txt
- group: auth
  href: https://artifacts.apis.io/atolls/well-known/atolls-hotukdeals-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atolls-hotukdeals-security.txt
- group: other
  href: https://artifacts.apis.io/atolls/hosts/atolls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atolls-hosts.yml
- group: other
  href: https://artifacts.apis.io/atolls/vendors/atolls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atolls-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://atolls.com/insights/category/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://atolls.com/insights/feed/
- group: auth
  href: https://artifacts.apis.io/atolls/security/atolls-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/atolls-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://atolls.com/disclosure-policy
- group: auth
  href: https://artifacts.apis.io/atolls/security/atolls-domain-security.yml
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
  href: https://artifacts.apis.io/atolls/well-known/atolls-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/atolls-security.txt
- group: agent
  href: https://artifacts.apis.io/atolls/well-known/atolls-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atolls-well-known.yml
- group: other
  href: https://artifacts.apis.io/atolls/well-known/atolls-mydealz-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/atolls-mydealz-openid-configuration.json
- group: auth
  href: https://artifacts.apis.io/atolls/scopes/atolls-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/atolls-scopes.yml
- group: design
  href: https://artifacts.apis.io/atolls/conformance/atolls-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atolls-conformance.yml
coverage:
  checked: '2026-10-20'
  detail: Atolls runs consumer coupon and cashback brands and publishes no developer API, portal or contract; api.atolls.com does not resolve and only security.txt and Pepper OIDC discovery documents are machine-readable.
  evidence:
  - status: 0
    url: https://api.atolls.com/
  - status: 200
    url: https://atolls.com
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'Atolls (formerly Global Savings Group) is a Munich-based consumer commerce-content company that operates the world''s largest shopping engagement platform, running coupon, cashback, deals, and shopping-community destinations across more than 20 markets. Its brand portfolio includes Coupons.com, Cuponation, iGraal, Shoop, Pouch, mydealz, hotukdeals, and Deala, connecting millions of shoppers with offers from thousands of retailers and brands through affiliate marketing, cashback, and AI-enhanced shopping insights. Founded in 2012 as CupoNation with Rocket Internet and rebranded to Atolls in 2024, it is backed by investors including HV Capital, RTP Global, and Rocket Internet. Atolls publishes no public developer API, developer portal, OpenAPI document or SDK — api., developer. and docs.atolls.com do not resolve — but it does serve real machine-readable documents: RFC 9116 security.txt files on five owned hosts pointing at a single group-wide Intigriti vulnerability disclosure
  program, and OpenID Connect discovery documents on seven Pepper community properties (mydealz, hotukdeals, Dealabs, Preisjaeger, Chollometro, Pepper PL, Promodescuentos) that expose an OAuth 2.0 authorization server for consumer sign-in. This profile captures that security, identity, and legal surface for the API Evangelist network.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atolls.png
layout: provider
modified: '2026-10-06'
name: Atolls
nav: Providers
network: true
overview: 'Atolls is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, E-Commerce, Affiliate Marketing, and Cashback.


  Atolls'' developer surface includes engineering blog and 21 more developer resources.'
random_paper: 7
scopes:
- name: Atolls Scopes
  scope_count: 3
  slug: atolls-scopes
  summary_line: 3 scopes · authorization_code/client_credentials/refresh_token
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 16.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/atolls/atolls-2026-07-25T201556.png
security:
- kind: authentication
  name: Atolls Authentication
  slug: atolls-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atolls Domain Security
  slug: atolls-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Atolls Vulnerability Disclosure
  slug: atolls-vulnerability-disclosure
  summary_line: security.txt · contact published
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
website: https://atolls.com
---
