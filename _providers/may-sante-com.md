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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/may-sante-com/hosts/may-sante-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/may-sante-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/may-sante-com/vendors/may-sante-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/may-sante-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.may.app/en/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/may-sante-com/security/may-sante-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/may-sante-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://may-sante.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.may.app/
- group: company
  title: ''
  type: Blog
  url: https://www.may.app/blog
created: '2026-10-24'
description: May is a French digital health company offering a parenting app that supports families from pregnancy through early childhood. The platform provides personalized guidance, educational content, and tools for tracking development milestones, sleep, nutrition, and health. May leverages AI to deliver tailored advice and connects parents with experts, aiming to improve child wellbeing and parental confidence.
image: https://www.may.app/wp-content/uploads/2025/05/logo_may_sapin_fond_transparent.png
layout: provider
modified: '2026-10-24'
name: May
nav: Providers
network: true
overview: 'May is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Parenting, Digital Health, and Artificial Intelligence.


  May''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/may-sante-com/may-sante-com-2026-11-03T135357.png
security:
- kind: domain-security
  name: May Sante Com Domain Security
  slug: may-sante-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: may-sante-com
tags:
- Company
- Health
- Parenting
- Digital Health
- Artificial Intelligence
website: https://may-sante.com/
---
