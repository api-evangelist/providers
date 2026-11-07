---
access_model:
  confidence: medium
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: build
  href: https://artifacts.apis.io/cronometer/integrations/cronometer-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/cronometer-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/cronometer/plans/cronometer-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cronometer-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/cronometer/well-known/cronometer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cronometer-security.txt
- group: agent
  href: https://artifacts.apis.io/cronometer/well-known/cronometer-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cronometer-well-known.yml
- group: other
  href: https://artifacts.apis.io/cronometer/hosts/cronometer-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cronometer-hosts.yml
- group: other
  href: https://artifacts.apis.io/cronometer/vendors/cronometer-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cronometer-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cronometer/security/cronometer-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cronometer-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cronometer/security/cronometer-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cronometer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cronometer.com
- group: company
  title: ''
  type: Blog
  url: https://blog.cronometer.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cronometer.com/hc/en-us
- group: operate
  title: ''
  type: Forum
  url: https://forums.cronometer.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://cronometer.com/gold/
- group: start
  title: ''
  type: SignUp
  url: https://cronometer.com/signup/
- group: start
  title: ''
  type: Login
  url: https://cronometer.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cronometer.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cronometer.com/privacy/
- group: company
  title: ''
  type: About
  url: https://cronometer.com/about/
- group: auth
  title: ''
  type: Security
  url: https://cronometer.com/features/data-security.html
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/cronometer
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCX4_3R4oVBU3Ff5Jmh1iJbw
created: '2026-10-18'
description: 'Cronometer is a Canadian nutrition tracking app and calorie counter, started in 2005 by founder Aaron Davidson. It tracks macronutrients, micronutrients, exercise and biometrics, using verified, lab-analyzed food data from sources such as the Nutrition Coordinating Center and the USDA rather than crowdsourced entries. It ships web, iOS and Android apps with a free Basic tier and a paid Gold subscription, plus Cronometer Pro for dietitians, nutritionists, trainers and health coaches, and an Enterprise offering for healthcare, research and education. It does not publish a public developer API: no developer portal or API documentation was found on cronometer.com, and community forum threads say API access is only given to select partners.'
image: https://cronometer.com/blog/wp-content/uploads/2022/07/crono-social-share-1.png
layout: provider
modified: '2026-10-18'
name: Cronometer
nav: Providers
network: true
overview: 'Cronometer is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Health, Fitness, and Calorie Counter.


  Cronometer''s developer surface includes engineering blog, support, pricing, signup flow, YouTube channel, and 16 more developer resources.'
plans:
- name: Cronometer Plans Pricing
  plan_count: 4
  slug: cronometer-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Cronometer Rate Limits
  slug: cronometer-rate-limits
scopes:
- name: Cronometer Scopes
  scope_count: 0
  slug: cronometer-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.1
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cronometer/cronometer-2026-11-03T125630.png
security:
- kind: authentication
  name: Cronometer Authentication
  slug: cronometer-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cronometer Domain Security
  slug: cronometer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cronometer Vulnerability Disclosure
  slug: cronometer-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cronometer
tags:
- Company
- Nutrition
- Health
- Fitness
- Calorie Counter
- Diet Tracking
- Mobile App
- Wellness
website: https://cronometer.com
---
