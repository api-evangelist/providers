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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/nationalgrid-com/refs/heads/main/well-known/nationalgrid-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nationalgrid-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nationalgrid-com/refs/heads/main/hosts/nationalgrid-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nationalgrid-com-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nationalgrid-com/refs/heads/main/vendors/nationalgrid-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nationalgrid-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.nationalgrid.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nationalgrid-com/refs/heads/main/security/nationalgrid-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nationalgrid-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nationalgrid.com/
coverage:
  checked: '2026-10-15'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found on api.nationalgrid.com despite probing common spec endpoints.
  evidence:
  - status: 404
    url: https://api.nationalgrid.com/openapi.json
  - status: 404
    url: https://api.nationalgrid.com/openapi.yaml
  - status: 404
    url: https://api.nationalgrid.com/swagger.json
  - status: 404
    url: https://api.nationalgrid.com/v1/openapi.json
  - status: 404
    url: https://api.nationalgrid.com/api-docs
  - status: 404
    url: https://api.nationalgrid.com/docs
  - status: 404
    url: https://api.nationalgrid.com/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: National Grid is a multinational electricity and gas utility company that delivers energy to millions of customers across the United Kingdom and the United States. It operates transmission and distribution networks, provides energy services, and invests in sustainable infrastructure and innovation. The company focuses on reliable power delivery, renewable energy integration, and customer support, while maintaining regulatory compliance and environmental stewardship.
image: https://www.nationalgrid.com/sites/default/files/2025-11/Crane%20at%20night%201.png
layout: provider
modified: '2026-10-14'
name: National Grid
nav: Providers
network: true
overview: National Grid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Electricity, Gas, and Infrastructure.
random_paper: 12
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 5
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
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nationalgrid Com Domain Security
  slug: nationalgrid-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nationalgrid-com
tags:
- Energy
- Utilities
- Electricity
- Gas
- Infrastructure
website: https://www.nationalgrid.com/
---
