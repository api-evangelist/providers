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
  href: https://raw.githubusercontent.com/api-evangelist/arunabiomedical/refs/heads/main/hosts/arunabiomedical-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arunabiomedical-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arunabiomedical/refs/heads/main/vendors/arunabiomedical-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arunabiomedical-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arunabio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arunabio.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.arunabio.com/press
- group: other
  title: ''
  type: Leadership
  url: https://www.arunabio.com/leadership
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arunabiomedical/refs/heads/main/security/arunabiomedical-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arunabiomedical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arunabio.com
coverage:
  checked: 2026-09-26
  detail: No public API documentation or machine‑readable contract was found for Arunabiomedical.
  evidence:
  - status: 0
    url: https://api.arunabio.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Arunabiomedical, operating as Aruna Bio, is a privately held biotechnology company based in Athens, Georgia. It focuses on developing neural exosome therapeutics for neurological diseases, leveraging a proprietary platform to cross the blood‑brain barrier. The company offers research products and services derived from human stem cells, supporting drug discovery and basic research.
layout: provider
modified: '2026-09-26'
name: Arunabiomedical
nav: Providers
network: true
overview: Arunabiomedical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Neural Exosomes, Stem Cells, Research Services, and Georgia.
random_paper: 6
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arunabiomedical Domain Security
  slug: arunabiomedical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: arunabiomedical
tags:
- Biotechnology
- Neural Exosomes
- Stem Cells
- Research Services
- Georgia
- Healthcare
website: https://www.arunabio.com
---
