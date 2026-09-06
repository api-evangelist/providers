---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.zayzoon.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.zayzoon.com/customers/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.zayzoon.com/customers/sign_in
- group: operate
  title: ''
  type: Support
  url: https://www.zayzoon.com/employer/help-center
- group: company
  title: ''
  type: Blog
  url: https://www.zayzoon.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.zayzoon.com/blog/rss.xml
- group: company
  title: ''
  type: Newsroom
  url: https://www.zayzoon.com/press
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zayzoon.com/usaterms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zayzoon.com/usaprivacy
- group: auth
  title: ''
  type: Security
  url: https://www.zayzoon.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/zayzoon-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/zayzoon-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zayzoon-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zayzoon-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zayzoon-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zayzoon-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zayzoon-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/zayzoon-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zayzoon-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 'ZayZoon runs a real partner API — api.zayzoon.com resolves and its payroll/HCM integrations are marketed on its own partner pages — but the only published route to it is the "Partner with ZayZoon" inquiry form; there is no developer portal, no API reference and no machine-readable contract on any ZayZoon host, and the API host itself serves robots.txt "Disallow: /" and redirects anonymous requests to a customer sign-in page.'
  evidence:
  - status: 404
    url: https://api.zayzoon.com/
  - status: 404
    url: https://api.zayzoon.com/openapi.json
  - status: 200
    url: https://api.zayzoon.com/robots.txt
  - status: 200
    url: https://www.zayzoon.com/partners
  - status: 200
    url: https://info.zayzoon.com/partner-with-zayzoon
  - status: 0
    url: https://developers.zayzoon.com/
  reason: sales-gate
  state: gated
created: '2026-09-05'
description: ZayZoon is an Earned Wage Access (EWA) and financial-wellness provider, founded in 2014 with offices in Calgary, Alberta and Scottsdale, Arizona, that lets employees of participating businesses draw a portion of already-earned wages before payday. The product is distributed through payroll, PEO and HCM platforms — ZayZoon advertises 300+ payroll and HCM integrations and is listed on the ADP Marketplace, isolved Network, AllianceHCM, PrismHR, Paylocity and Execupay — and is free for employers, with employees paying a flat per-transfer processing fee or choosing a fee-free option (Boost gift cards, ZayZoon Visa prepaid card). ZayZoon operates a partner API used by payroll providers to exchange employee, hours-worked and deduction data, but it publishes no public developer portal, API reference or machine-readable specification; access is arranged through the partner program. NMLS ID 2635812.
image: https://www.zayzoon.com/hubfs/Featured_ZayZoon.png
layout: provider
modified: '2026-09-05'
name: ZayZoon
nav: Providers
network: true
overview: 'ZayZoon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Earned Wage Access, On-Demand Pay, Payroll, and Human Resources.


  ZayZoon''s developer surface includes signup flow, support, engineering blog, and 16 more developer resources.'
plans:
- name: Zayzoon Plans Pricing
  plan_count: 3
  slug: zayzoon-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Zayzoon Rate Limits
  slug: zayzoon-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Zayzoon Domain Security
  slug: zayzoon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zayzoon Vulnerability Disclosure
  slug: zayzoon-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Zayzoon Trust Center
  slug: zayzoon-trust-center
  summary_line: SOC 2 Type II
slug: zayzoon
tags:
- Company
- Earned Wage Access
- On-Demand Pay
- Payroll
- Human Resources
- Employee Benefits
- Financial Wellness
- Fintech
- Payments
- Embedded Finance
website: https://www.zayzoon.com/
---
