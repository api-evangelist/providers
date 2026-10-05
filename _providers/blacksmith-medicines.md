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
  href: https://raw.githubusercontent.com/api-evangelist/blacksmith-medicines/refs/heads/main/hosts/blacksmith-medicines-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blacksmith-medicines-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blacksmith-medicines/refs/heads/main/vendors/blacksmith-medicines-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blacksmith-medicines-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blacksmith-medicines/refs/heads/main/security/blacksmith-medicines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blacksmith-medicines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blacksmithmedicines.com
- group: docs
  title: ''
  type: Documentation
  url: https://blacksmithmedicines.com/about-us/
- group: other
  title: ''
  type: Technology
  url: https://blacksmithmedicines.com/technology/
- group: other
  title: ''
  type: Pipeline
  url: https://blacksmithmedicines.com/pipeline-targets/
- group: company
  title: ''
  type: News
  url: https://blacksmithmedicines.com/news/
coverage:
  checked: '2026-09-29'
  detail: Blacksmith Medicines is a biotech company with no public API surface.
  evidence:
  - status: 404
    url: https://blacksmithmedicines.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-09-29'
description: Blacksmith Medicines is a biotech company focused on developing human metalloenzyme‑targeted medicines. Based in San Diego, the firm leverages a purpose‑built platform to discover and advance novel therapeutics for a range of diseases. Their pipeline includes innovative candidates addressing unmet medical needs, supported by a team of experts in chemistry, biology, and drug development. The company aims to translate cutting‑edge science into safe and effective treatments for patients worldwide.
image: https://blacksmithmedicines.com/wp-content/uploads/2019/12/Blacksmith-medicines.png
layout: provider
modified: '2026-09-29'
name: Blacksmith Medicines
nav: Providers
network: true
overview: 'Blacksmith Medicines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharma, Metalloenzyme, and Drug Discovery.


  Blacksmith Medicines'' developer surface includes documentation, product news, and 6 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blacksmith Medicines Domain Security
  slug: blacksmith-medicines-domain-security
  summary_line: TLSv1.3
slug: blacksmith-medicines
tags:
- Company
- Biotechnology
- Pharma
- Metalloenzyme
- Drug Discovery
- San Diego
website: https://blacksmithmedicines.com
---
