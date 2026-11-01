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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/aveo-oncology/hosts/aveo-oncology-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aveo-oncology-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aveooncology.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aveooncology.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.aveooncology.com/newsroom/
- group: auth
  href: https://artifacts.apis.io/aveo-oncology/security/aveo-oncology-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aveo-oncology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aveooncology.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.aveooncology.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: 'AVEO Oncology is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by nea) and added to the network as a stub for full-pipeline profiling.'
image: https://www.aveooncology.com/wp-content/uploads/2026/10/aveo-lg-chem-logo.png
layout: provider
modified: '2026-10-22'
name: AVEO Oncology
nav: Providers
network: true
overview: AVEO Oncology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Oncology, Biopharmaceutical, Cancer, Pharmaceuticals, and Partnerships.
random_paper: 2
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aveo Oncology Domain Security
  slug: aveo-oncology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aveo-oncology
tags:
- Oncology
- Biopharmaceutical
- Cancer
- Pharmaceuticals
- Partnerships
website: https://www.aveooncology.com/
---
