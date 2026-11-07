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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/nova-fertility/hosts/nova-fertility-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nova-fertility-hosts.yml
- group: other
  href: https://artifacts.apis.io/nova-fertility/vendors/nova-fertility-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nova-fertility-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.novaivf.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.novaivf.com/blog
- group: auth
  href: https://artifacts.apis.io/nova-fertility/security/nova-fertility-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nova-fertility-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.novaivf.com
- group: other
  title: ''
  type: Image
  url: https://www.novaivf.com/_astro/nova-logo-white_1PFvHf.webp
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.novaivf.com/mcp
  - status: 200
    url: https://www.novaivf.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Nova IVF is a leading fertility clinic offering personalized IVF and reproductive health services. The company provides patient-centered care, advanced reproductive technologies, and a range of treatment options to help individuals and couples achieve their family building goals. Their website offers detailed information about clinics, doctors, success rates, and resources for prospective patients.
image: https://a.storyblok.com/f/290132/1733x1155/121c9f5059/baby-and-dog.jpg
layout: provider
modified: '2026-10-22'
name: Nova Fertility
nav: Providers
network: true
overview: 'Nova Fertility is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fertility, Healthcare, IVF, and Reproductive Health.


  Nova Fertility''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nova-fertility/nova-fertility-2026-11-03T140321.png
security:
- kind: domain-security
  name: Nova Fertility Domain Security
  slug: nova-fertility-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nova-fertility
tags:
- Company
- Fertility
- Healthcare
- IVF
- Reproductive Health
website: https://www.novaivf.com
---
