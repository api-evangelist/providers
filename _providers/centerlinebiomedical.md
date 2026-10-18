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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API documentation not publicly available; no machine-readable spec found.
  name: Centerline Biomedical API
  slug: centerline-biomedical-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/centerlinebiomedical/refs/heads/main/hosts/centerlinebiomedical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centerlinebiomedical-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://centerlinebiomedical.com/2021/07/29/sign-up-for-a-demo-at-vam-2021/
- group: company
  title: ''
  type: Newsroom
  url: https://centerlinebiomedical.com/category/news/
- group: other
  title: ''
  type: Leadership
  url: https://centerlinebiomedical.com/leadership/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/centerlinebiomedical/refs/heads/main/security/centerlinebiomedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centerlinebiomedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centerlinebiomedical.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centerlinebiomedical.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://centerlinebiomedical.com/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://centerlinebiomedical.com
  - status: 403
    url: https://equityzen.com/company/centerlinebiomedical
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Centerline Biomedical develops FDA-cleared endovascular navigation technology (IOPS®) to reduce radiation exposure for clinicians and improve procedural accuracy. The company provides a real‑time 3‑D imaging and positioning system for minimally invasive cardiovascular interventions, serving hospitals and interventional specialists worldwide.
layout: provider
modified: '2026-10-07'
name: Centerlinebiomedical
nav: Providers
network: true
overview: 'Centerlinebiomedical is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical, Healthcare, Navigation, and Endovascular.


  Centerlinebiomedical''s developer surface includes signup flow and 7 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Centerlinebiomedical Domain Security
  slug: centerlinebiomedical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: centerlinebiomedical
tags:
- Company
- Medical
- Healthcare
- Navigation
- Endovascular
website: https://centerlinebiomedical.com
---
