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
  href: https://artifacts.apis.io/national-states-geographic-information-council-nsgic/hosts/national-states-geographic-information-council-nsgic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/national-states-geographic-information-council-nsgic-hosts.yml
- group: other
  href: https://artifacts.apis.io/national-states-geographic-information-council-nsgic/vendors/national-states-geographic-information-council-nsgic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/national-states-geographic-information-council-nsgic-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nsgic.org/privacy-policy/
- group: other
  title: ''
  type: Leadership
  url: https://nsgic.org/about-us/leadership/committees/
- group: auth
  href: https://artifacts.apis.io/national-states-geographic-information-council-nsgic/security/national-states-geographic-information-council-nsgic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/national-states-geographic-information-council-nsgic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nsgic.org/
coverage:
  checked: '2026-10-23'
  detail: The provider's website returns HTML pages but no discoverable OpenAPI, GraphQL, or other machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://nsgic.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: The National States Geographic Information Council (NSGIC) is a state‑led forum that develops, exchanges, and endorses geospatial technology and policy best practices. It shares solutions across the geospatial ecosystem, providing guidance, standards, and resources for state GIS programs and stakeholders. NSGIC operates as a collaborative council of state GIS professionals, fostering interoperability and innovation in geographic information systems.
image: https://nsgic.org/wp-content/uploads/2023/05/Dot_Map_NSGIC_blue.png
layout: provider
modified: '2026-10-23'
name: National States Geographic Information Council (NSGIC)
nav: Providers
network: true
overview: National States Geographic Information Council (NSGIC) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geospatial, GIS, Government, and Standards.
random_paper: 3
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: National States Geographic Information Council Nsgic Domain Security
  slug: national-states-geographic-information-council-nsgic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: national-states-geographic-information-council-nsgic
tags:
- Company
- Geospatial
- GIS
- Government
- Standards
website: https://nsgic.org/
---
