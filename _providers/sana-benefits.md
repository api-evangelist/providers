---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
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
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sana-benefits-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sanabenefits.com/
- group: company
  title: ''
  type: About
  url: https://www.sanabenefits.com/who-we-are/
- group: company
  title: ''
  type: Blog
  url: https://www.sanabenefits.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.sanabenefits.com/feed/
- group: company
  title: ''
  type: Press
  url: https://www.sanabenefits.com/press/
- group: operate
  title: ''
  type: Support
  url: https://help.sanabenefits.com/hc/en-us
- group: other
  title: ''
  type: SignIn
  url: https://secure.sanabenefits.com/
- group: company
  title: ''
  type: Partners
  url: https://www.sanabenefits.com/sana-partners/
- group: operate
  title: ''
  type: Contact
  url: https://www.sanabenefits.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sanabenefits.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sanabenefits.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sana-benefits/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sanabenefits
- group: start
  title: ''
  type: Login
  url: https://secure.sanabenefits.com/
- group: commercial
  title: ''
  type: Plans
  url: https://www.sanabenefits.com/plans/
- group: operate
  title: ''
  type: FAQ
  url: https://www.sanabenefits.com/employer-faqs/
- group: docs
  title: ''
  type: Guides
  url: https://www.sanabenefits.com/guides/
- group: other
  title: ''
  type: Testimonials
  url: https://www.sanabenefits.com/testimonials/
- group: company
  title: ''
  type: Careers
  url: https://www.sanabenefits.com/careers/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.sanabenefits.com/notice-of-privacy-practices/
- group: auth
  title: ''
  type: Compliance
  url: https://www.sanabenefits.com/notice-of-privacy-practices/
- group: design
  title: ''
  type: Conformance
  url: conformance/sana-benefits-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/sana-benefits-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sana-benefits-llms.txt
created: '2026-07-25'
description: 'Sana Benefits is an Austin, Texas health benefits company founded in 2017 that sells level-funded and self-funded small-group health plans to small and midsize employers in the United States, bundling medical, dental and vision coverage with Sana Care, its in-house virtual-first primary care and care navigation service. Sana distributes almost entirely through licensed benefits brokers, underwrites and administers the plan itself with stop-loss insurance included, and prices provider claims off a reference-based percentage of the Medicare fee schedule. State landing pages confirm sales in Texas, Arizona, Illinois, Indiana, Kentucky, Ohio, Oklahoma, Virginia, Wisconsin and Alabama. Its API posture is closed: as of July 2026 Sana publishes no public developer portal, no API reference, no OpenAPI or Postman artifacts, no GraphQL surface and no webhook or event catalog. The developer.*, developers.*, docs.* and api.* subdomains do not resolve, and every /developers, /api, /developer,
  /partners and /integrations path on sanabenefits.com returns 404. The only machine surface is secure.sanabenefits.com, a login-walled JSON application serving the member, employer and broker dashboards; its /openapi.json and /swagger.json paths answer 401 login_required, confirming an internal-only API. No ACORD, AL3, IVANS, NGDS or X12 834 reference appears anywhere in public marketing or FAQ content. Quoting is a human broker workflow — "rates in 48 hours" from a web form — not an API. This is a partner-gated, broker-mediated benefits carrier with zero public self-serve API surface, which is the typical posture for the US benefits-admin tier in a market with no open-insurance mandate.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Sana Benefits
nav: Providers
network: true
overview: 'Sana Benefits is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, United States, Health Insurance, Employee Benefits, and Benefits Administration.


  Sana Benefits'' developer surface includes engineering blog, support, FAQ, privacy policy, and 21 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 47.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sana-benefits/refs/heads/main/screenshots/sana-benefits-2026-09-02T154347.png
security:
- kind: domain-security
  name: Sana Benefits Domain Security
  slug: sana-benefits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sana-benefits
tags:
- Insurance
- United States
- Health Insurance
- Employee Benefits
- Benefits Administration
- Small Business
- Level-Funded Plans
- Insurtech
- Brokers
- Virtual Primary Care
website: https://www.sanabenefits.com/
---
