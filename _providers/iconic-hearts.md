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
  href: https://artifacts.apis.io/iconic-hearts/hosts/iconic-hearts-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iconic-hearts-hosts.yml
- group: other
  href: https://artifacts.apis.io/iconic-hearts/vendors/iconic-hearts-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iconic-hearts-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iconichearts.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iconichearts.com/privacy
- group: other
  title: ''
  type: Leadership
  url: https://www.iconichearts.com/sendit/team
- group: auth
  href: https://artifacts.apis.io/iconic-hearts/security/iconic-hearts-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iconic-hearts-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iconichearts.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.iconichearts.com/
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Iconic Hearts Inc builds a social platform for Generation Alpha, offering a suite of apps—Sendit, Noteit, Starmatch, Linkit—that enable young users to ask questions, share notes, match interests, and connect through heart‑shaped link chains. Launched in 2018, the service claims over 250 million users worldwide and aims to become the primary destination for all social interactions among Gen Alpha, fostering lifelong friendships through safe, playful digital experiences.
layout: provider
modified: '2026-10-25'
name: Iconic Hearts
nav: Providers
network: true
overview: Iconic Hearts is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social, Platform, Gen Alpha, and Mobile.
random_paper: 1
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iconic-hearts/iconic-hearts-2026-11-03T133615.png
security:
- kind: domain-security
  name: Iconic Hearts Domain Security
  slug: iconic-hearts-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iconic-hearts
tags:
- Company
- Social
- Platform
- Gen Alpha
- Mobile
website: https://www.iconichearts.com/
---
