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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asherbio/refs/heads/main/hosts/asherbio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asherbio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/asherbio/refs/heads/main/vendors/asherbio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asherbio-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://asherbio.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/asherbio/refs/heads/main/security/asherbio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asherbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asherbio.com
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://asherbio.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asherbio.com/privacy-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/asherbio
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Asherbio is a biopharmaceutical company focused on developing cis‑targeted immunotherapies that selectively activate immune cells to treat cancer and other diseases. Their platform aims to improve efficacy and reduce side effects by precisely targeting the immune response. Asher Bio’s pipeline includes candidates such as Etakafusp alfa, AB821, and AB359, with ongoing clinical collaborations and presentations at major oncology meetings. The company emphasizes innovative approaches to immune cell targeting, aiming to restore hope, health, and happiness for patients.
image: https://asherbio.com/wp-content/uploads/2021/03/home-page-card-Asher-032221.jpg
layout: provider
modified: '2026-09-26'
name: Asherbio
nav: Providers
network: true
overview: Asherbio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biopharma, Immunotherapy, Oncology, Cis-targeted, and Biotechnology.
random_paper: 9
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asherbio Domain Security
  slug: asherbio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asherbio
tags:
- Biopharma
- Immunotherapy
- Oncology
- Cis-targeted
- Biotechnology
website: https://asherbio.com
---
