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
  href: https://artifacts.apis.io/navteca/hosts/navteca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/navteca-hosts.yml
- group: other
  href: https://artifacts.apis.io/navteca/vendors/navteca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/navteca-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Navteca
- group: auth
  href: https://artifacts.apis.io/navteca/security/navteca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/navteca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://navteca.com/
coverage:
  checked: '2026-10-26'
  detail: OpenAPI spec endpoints return 403, indicating no public machine‑readable contract.
  evidence:
  - status: 403
    url: https://api.navteca.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: Navteca is a woman- and minority-owned technology services company focused on emerging technologies and IT innovation. It solves real‑world problems through innovative applications in high‑performance computing, cloud solutions, and scientific collaboration. Navteca partners with organizations like NASA to accelerate science, offering services that span cloud infrastructure, data analytics, and custom software development, all driven by a commitment to push boundaries and deliver practical, technology‑for‑good solutions.
layout: provider
modified: '2026-10-26'
name: Navteca
nav: Providers
network: true
overview: Navteca is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, EmergingTech, CloudComputing, and ScientificComputing.
random_paper: 18
score:
  band: minimal
  composite: 3.8
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
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Navteca Domain Security
  slug: navteca-domain-security
  summary_line: TLSv1.3 · DMARC
slug: navteca
tags:
- Company
- Technology
- EmergingTech
- CloudComputing
- ScientificComputing
website: https://navteca.com/
---
