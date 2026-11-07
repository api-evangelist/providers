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
  href: https://artifacts.apis.io/voxy/hosts/voxy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/voxy-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voxy.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voxy.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.voxy.com/go/login
- group: company
  title: ''
  type: Blog
  url: https://voxy.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voxy
- group: auth
  href: https://artifacts.apis.io/voxy/security/voxy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voxy.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://voxy.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Voxy provides AI‑personalized corporate English training for global teams, offering live tutors 24/7, measurable ROI, and a platform that adapts to each learner’s needs. Founded to help businesses communicate confidently in English, Voxy combines language science with technology to deliver scalable, data‑driven language education for enterprises worldwide.
image: https://voxy.com/wp-content/uploads/2024/05/Voxy-Language-Training-for-Business-2.webp
layout: provider
modified: '2026-10-24'
name: Voxy
nav: Providers
network: true
overview: 'Voxy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Language Learning, Artificial Intelligence, Corporate Training, and Education.


  Voxy''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/voxy/voxy-2026-11-03T145935.png
security:
- kind: domain-security
  name: Voxy Domain Security
  slug: voxy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: voxy
tags:
- Company
- Language Learning
- Artificial Intelligence
- Corporate Training
- Education
website: https://voxy.com/
---
