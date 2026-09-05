---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lassen-peak-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lassenpeak.com/
- group: company
  title: ''
  type: About
  url: https://www.lassenpeak.com/about/
- group: operate
  title: ''
  type: Support
  url: https://www.lassenpeak.com/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.lassenpeak.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://www.lassenpeak.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.lassenpeak.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.lassenpeak.com/press-releases/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lassenpeak.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://www.lassenpeak.com/careers-at-lassen-peak/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lassen-peak/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/lassen_peak
- group: other
  title: ''
  type: Product
  url: https://www.lassenpeak.com/airfrisk/
- group: other
  title: ''
  type: Product
  url: https://www.lassenpeak.com/imagevault/
- group: commercial
  title: ''
  type: Plans
  url: plans/lassen-peak-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lassen-peak-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lassen-peak-llms.txt
coverage:
  checked: '2026-08-23'
  detail: Lassen Peak sells a handheld weapon-detection device (AirFrisk) plus a customer-tenant cloud console (ImageVault) to law-enforcement agencies; its entire 17-page WordPress site has no developer, docs or API section, api./developer./docs.lassenpeak.com do not resolve in DNS, and the only gated surface is a TalentLMS training tenant for end users, not an API.
  evidence:
  - status: 404
    url: https://www.lassenpeak.com/openapi.json
  - status: 404
    url: https://www.lassenpeak.com/.well-known/api-catalog
  - status: 200
    url: https://www.lassenpeak.com/sitemap_index.xml
  - status: 404
    url: https://api.github.com/orgs/lassenpeak
  - status: 200
    url: https://lassenpeak.talentlms.com/plus/login
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: Lassen Peak, Inc. is a Seattle-area public-safety technology company founded in 2019 by veterans of ultra-high-speed wireless, imaging radar, broadband communications and law enforcement. It builds AirFrisk, a handheld terahertz imaging-radar scanner that detects concealed weapons at a distance without a hands-on pat-down, and ImageVault, the companion cloud console that manages AirFrisk users, devices, scan data, retention policy, alerts, reporting and audit logs for an agency under FBI-CJIS compliant storage. The company has raised roughly $22M across Series A and A1 rounds and holds multiple issued US patents. Lassen Peak sells a device plus a customer-tenant cloud console to police, sheriff and security agencies; as of this profile it publishes no public developer program, no API documentation, no SDKs and no machine-readable contract of any kind on its own domain.
image: https://www.lassenpeak.com/wp-content/uploads/2023/12/LassesPeakLogo.svg
layout: provider
modified: '2026-08-23'
name: Lassen Peak
nav: Providers
network: true
overview: 'Lassen Peak is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Public Safety, Law Enforcement, Security, and Weapon Detection.


  Lassen Peak''s developer surface includes support, FAQ, engineering blog, and 14 more developer resources.'
plans:
- name: Lassen Peak Plans Pricing
  plan_count: 0
  slug: lassen-peak-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Lassen Peak Rate Limits
  slug: lassen-peak-rate-limits
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lassen-peak/refs/heads/main/screenshots/lassen-peak-2026-09-02T150211.png
security:
- kind: domain-security
  name: Lassen Peak Domain Security
  slug: lassen-peak-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lassen-peak
tags:
- Company
- Public Safety
- Law Enforcement
- Security
- Weapon Detection
- Imaging Radar
- Hardware
- Devices
- Cloud
- Government
website: https://www.lassenpeak.com/
---
