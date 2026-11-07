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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 9.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/resmed/llms/resmed-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/resmed-llms.txt
- group: agent
  href: https://artifacts.apis.io/resmed/well-known/resmed-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/resmed-well-known.yml
- group: other
  href: https://artifacts.apis.io/resmed/hosts/resmed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/resmed-hosts.yml
- group: other
  href: https://artifacts.apis.io/resmed/vendors/resmed-vendors.yml
  title: ''
  type: Vendors
  url: vendors/resmed-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.resmed.com/en-us/security/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.resmed.com/en-us/health-professionals/solutions/resmed-resupply/onboarding/
- group: auth
  href: https://artifacts.apis.io/resmed/security/resmed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/resmed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.resmed.com/en-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ResMedOSS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/resmed
- group: company
  title: ''
  type: Blog
  url: https://www.resmed.com/en-us/sleep-health/blog/
- group: other
  title: ''
  type: RSS
  url: https://www.resmed.com/en-us/feed/
- group: operate
  title: ''
  type: Support
  url: https://support.resmed.com/en-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.resmed.com/en-us/contact-us/
- group: company
  title: ''
  type: AboutUs
  url: https://www.resmed.com/en-us/about-us/
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.resmed.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.resmed.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.resmed.com/en-us/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.resmed.com/en-us/terms-of-use/
created: '2026-05-05'
description: 'Resmed (ResMed Inc., NYSE: RMD) is a Fortune 1000 medical device and digital health company that calls itself the world leader in sleep health. It makes CPAP and bilevel devices, masks and ventilators for sleep apnea, COPD and other respiratory conditions, and runs connected-care software such as the myAir patient app and AirView for clinicians. Its site resmed.com publishes no public developer portal or API documentation; a GitHub organization (ResMedOSS) hosts its open source software.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resmed.png
layout: provider
modified: '2026-10-20'
name: Resmed
nav: Providers
network: true
overview: 'Resmed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Healthcare, Sleep Apnea, Respiratory Care, and Digital Health.


  Resmed''s developer surface includes getting-started guide, engineering blog, support, and 16 more developer resources.'
plans:
- name: Resmed Plans Pricing
  plan_count: 0
  slug: resmed-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Resmed Rate Limits
  slug: resmed-rate-limits
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 56.3
    operational_transparency: 7.9
  previous_composite: 15.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/resmed/resmed-2026-06-20T193000.png
security:
- kind: domain-security
  name: Resmed Domain Security
  slug: resmed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: resmed
tags:
- Medical Devices
- Healthcare
- Sleep Apnea
- Respiratory Care
- Digital Health
- Connected Care
- Fortune 1000
website: https://www.resmed.com/en-us/
---
