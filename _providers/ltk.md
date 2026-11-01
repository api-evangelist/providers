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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: LTK's partner/affiliate API served from the rewardStyle Developer Portal, secured with OAuth2 (client-credentials token endpoint at /oauth/token). The full API reference and specification are gated be
  name: rewardStyle Developer Portal
  slug: rewardstyle-developer-portal
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/ltk/hosts/ltk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ltk-hosts.yml
- group: other
  href: https://artifacts.apis.io/ltk/vendors/ltk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ltk-vendors.yml
- group: build
  href: https://artifacts.apis.io/ltk/packages/ltk-packages.yml
  title: ''
  type: SDKs
  url: packages/ltk-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://company.shopltk.com/press
- group: other
  title: ''
  type: Leadership
  url: https://company.shopltk.com/zh-cn/influencergrowthservices/team
- group: start
  title: ''
  type: GettingStarted
  url: https://company.shopltk.com/uk/influencergrowthservices/getting-started
- group: auth
  href: https://artifacts.apis.io/ltk/security/ltk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ltk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://company.shopltk.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.rewardstyle.com/
- group: start
  title: ''
  type: SignUp
  url: https://api.rewardstyle.com/register
- group: operate
  title: ''
  type: Support
  url: https://company.shopltk.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://company.shopltk.com/ltk-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://company.shopltk.com/ltk-privacy-policy
- group: auth
  href: https://artifacts.apis.io/ltk/authentication/ltk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ltk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ltk/well-known/ltk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ltk-security.txt
- group: agent
  href: https://artifacts.apis.io/ltk/well-known/ltk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ltk-well-known.yml
- group: auth
  href: https://artifacts.apis.io/ltk/security/ltk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ltk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://shopltk.com/.well-known/security.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rewardStyle
- group: company
  title: ''
  type: Blog
  url: https://company.shopltk.com/us/creatorsuccess/creator-blog
- group: build
  href: https://artifacts.apis.io/ltk/packages/ltk-packages.yml
  title: ''
  type: Packages
  url: packages/ltk-packages.yml
- group: design
  href: https://artifacts.apis.io/ltk/lifecycle/ltk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ltk-lifecycle.yml
coverage:
  checked: '2026-10-20'
  detail: The rewardStyle Developer Portal at api.rewardstyle.com answers HTTP 200 with a sign-in form for every documentation path (/docs, /documentation, /openapi, /swagger, /api/v1), so the API reference and specification are only visible after partner registration; the OAuth2 token endpoint is the only part of the API that can be verified anonymously.
  evidence:
  - status: 200
    url: https://api.rewardstyle.com/
  - status: 404
    url: https://api.rewardstyle.com/openapi.json
  - status: 404
    url: https://api.rewardstyle.com/swagger.json
  - status: 404
    url: https://api.rewardstyle.com/llms.txt
  reason: partner-login
  state: gated
created: '2026-07-17'
description: LTK (formerly rewardStyle / LIKEtoKNOW.it) is a creator commerce platform that connects shoppers, content creators, and brands, driving more than $6B in annual sales. Founded in 2011 by Amber and Baxter Box and headquartered in Dallas, LTK operates a shoppable-content network spanning 44M+ monthly shoppers, 1M+ brands, and 8,000+ integrated retailers, and has generated nearly 1,100 creator millionaires. For brand and affiliate partners, LTK exposes a partner API through the rewardStyle Developer Portal at api.rewardstyle.com, secured with OAuth2 and gated behind partner registration. This profile enriches the LTK company record with its verifiable public developer, security, and identity surface.
image: https://company.shopltk.com/hubfs/LinkedInLTKlogo1-1.jpg
layout: provider
modified: '2026-08-13'
name: LTK
nav: Providers
network: true
overview: 'LTK is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Creator Commerce, Affiliates, and E-Commerce.


  LTK''s developer surface includes getting-started guide, signup flow, support, authentication, engineering blog, and 17 more developer resources.'
plans:
- name: Ltk Plans Pricing
  plan_count: 0
  slug: ltk-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Ltk Rate Limits
  slug: ltk-rate-limits
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 69.6
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 29.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ltk/ltk-2026-07-25T225629.png
security:
- kind: authentication
  name: Ltk Authentication
  slug: ltk-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ltk Domain Security
  slug: ltk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ltk Vulnerability Disclosure
  slug: ltk-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ltk
tags:
- Company
- Consumer
- Creator Commerce
- Affiliates
- E-Commerce
- Influencer Marketing
- Retail
- Shopping
website: https://company.shopltk.com/
---
