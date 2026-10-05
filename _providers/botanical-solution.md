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
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/botanical-solution/refs/heads/main/well-known/botanical-solution-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botanical-solution-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/botanical-solution/refs/heads/main/hosts/botanical-solution-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botanical-solution-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://botanical-solution.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/botanical-solution/refs/heads/main/security/botanical-solution-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botanical-solution-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botanical-solution.com/
coverage:
  checked: '2026-10-03'
  detail: API documentation pages return JavaScript-rendered shells, preventing machine-readable contract discovery.
  evidence:
  - status: 0
    url: https://api.botanical-solution.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Botanical Solution provides advanced botanical data integration services, offering APIs that deliver plant taxonomy, phytochemical composition, and cultivation insights for agritech, research, and wellness applications. Their platform aggregates curated botanical datasets, enabling developers to build applications that require accurate plant identification, health benefits analysis, and supply chain traceability. By focusing on data quality and comprehensive coverage, Botanical Solution aims to support innovative solutions in agriculture, pharmaceuticals, and consumer products.
image: https://botanical-solution.com/wp-content/uploads/2023/12/cropped-bsi-favicon.png
layout: provider
modified: '2026-10-03'
name: Botanical Solution
nav: Providers
network: true
overview: Botanical Solution is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Botany, Agriculture, and Pharma.
random_paper: 9
score:
  band: minimal
  composite: 3.8
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
    developer_ergonomics: 0.0
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
  name: Botanical Solution Domain Security
  slug: botanical-solution-domain-security
  summary_line: TLSv1.3
slug: botanical-solution
tags:
- Company
- Data
- Botany
- Agriculture
- Pharma
website: https://botanical-solution.com/
---
