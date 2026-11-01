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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/american-pathology-partners/hosts/american-pathology-partners-hosts.yml
  title: ''
  type: Hosts
  url: hosts/american-pathology-partners-hosts.yml
- group: other
  href: https://artifacts.apis.io/american-pathology-partners/vendors/american-pathology-partners-vendors.yml
  title: ''
  type: Vendors
  url: vendors/american-pathology-partners-vendors.yml
- group: auth
  href: https://artifacts.apis.io/american-pathology-partners/security/american-pathology-partners-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/american-pathology-partners-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ap2.com/
coverage:
  checked: '2026-10-22'
  detail: The provider website does not expose any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.ap2.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: American Pathology Partners (AP2) provides pathology and laboratory services across the United States, serving physicians and patients with diagnostic testing, clinical pathology, and specialized cytology. The company recently announced the sale of its Colorado and Texas operations, including UniPath, Alliance Health Sciences, and Cytology Associates, to Labcorp. AP2 focuses on delivering high-quality, timely results and supports healthcare providers through integrated lab solutions and innovative technologies.
layout: provider
modified: '2026-10-22'
name: American Pathology Partners
nav: Providers
network: true
overview: American Pathology Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pathology, Laboratory Services, Healthcare, and Diagnostics.
random_paper: 0
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: American Pathology Partners Domain Security
  slug: american-pathology-partners-domain-security
  summary_line: TLSv1.3
slug: american-pathology-partners
tags:
- Company
- Pathology
- Laboratory Services
- Healthcare
- Diagnostics
website: https://www.ap2.com/
---
