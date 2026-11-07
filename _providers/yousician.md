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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/yousician/security/yousician-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/yousician-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/yousician/well-known/yousician-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yousician-security.txt
- group: agent
  href: https://artifacts.apis.io/yousician/well-known/yousician-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yousician-well-known.yml
- group: other
  href: https://artifacts.apis.io/yousician/hosts/yousician-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yousician-hosts.yml
- group: other
  href: https://artifacts.apis.io/yousician/vendors/yousician-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yousician-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yousician.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yousician.com/privacy-notice
- group: company
  title: ''
  type: Newsroom
  url: https://yousician.com/press
- group: company
  title: ''
  type: Blog
  url: https://yousician.com/blog
- group: auth
  href: https://artifacts.apis.io/yousician/security/yousician-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/yousician-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/yousician/security/yousician-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yousician-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yousician.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://account.yousician.com/mcp
  - status: 200
    url: https://yousician.com
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Yousician is a fun, interactive music learning platform that helps users of all ages learn guitar, piano, ukulele, bass, and singing through a gamified experience with thousands of popular songs, personalized lessons, real-time feedback, and progress tracking, making music education engaging and accessible.
image: https://assets.yousician.com/app/uploads/2020/10/29174702/cropped-seo-image2-1.jpg
layout: provider
modified: '2026-10-24'
name: Yousician
nav: Providers
network: true
overview: 'Yousician is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Education, Learning, Gaming, and Platform.


  Yousician''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yousician Domain Security
  slug: yousician-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yousician Vulnerability Disclosure
  slug: yousician-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yousician
tags:
- Music
- Education
- Learning
- Gaming
- Platform
- Company
website: https://yousician.com
---
