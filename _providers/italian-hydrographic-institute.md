---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides marine hydrography and oceanographic data as described on the institute's website.
  name: Hydrographic Data API
  slug: hydrographic-data-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/italian-hydrographic-institute/hosts/italian-hydrographic-institute-hosts.yml
  title: ''
  type: Hosts
  url: hosts/italian-hydrographic-institute-hosts.yml
- group: auth
  href: https://artifacts.apis.io/italian-hydrographic-institute/security/italian-hydrographic-institute-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/italian-hydrographic-institute-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.marina.difesa.it/noi-siamo-la-marina/pilastro-logistico/scientifici/
coverage:
  checked: '2026-10-26'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found on the provider's documented hosts.
  evidence:
  - status: 0
    url: https://api.difesa.it/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: The Italian Hydrographic Institute (Istituto Idrografico della Marina Militare) is part of the Italian Navy, responsible for marine hydrography, oceanographic research, and supporting naval operations with nautical charts, tide predictions, and maritime safety data. It provides scientific and technical expertise in oceanography, hydrography, and related maritime domains, serving both military and civilian stakeholders.
image: https://www.marina.difesa.it/PublishingImages/pagine/logo-mmi-1260x630.jpg
layout: provider
modified: '2026-10-26'
name: Italian Hydrographic Institute
nav: Providers
network: true
overview: Italian Hydrographic Institute is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hydrography, Oceanography, Maritime, and Italy.
random_paper: 17
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Italian Hydrographic Institute Domain Security
  slug: italian-hydrographic-institute-domain-security
  summary_line: TLSv1.2
slug: italian-hydrographic-institute
tags:
- Company
- Hydrography
- Oceanography
- Maritime
- Italy
- Navy
website: https://www.marina.difesa.it/noi-siamo-la-marina/pilastro-logistico/scientifici/
---
