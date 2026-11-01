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
- group: agent
  href: https://artifacts.apis.io/fever-energy/llms/fever-energy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fever-energy-llms.txt
- group: other
  href: https://artifacts.apis.io/fever-energy/hosts/fever-energy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fever-energy-hosts.yml
- group: other
  href: https://artifacts.apis.io/fever-energy/vendors/fever-energy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fever-energy-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.fever.energy/platform/console
- group: company
  title: ''
  type: Newsroom
  url: https://www.fever.energy/news
- group: auth
  href: https://artifacts.apis.io/fever-energy/security/fever-energy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fever-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fever.energy/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's API host.
  evidence:
  - status: 0
    url: https://api.fever.energy/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Fever Energy provides a cloud-based platform for distributed energy resources, enabling utilities and energy service providers to aggregate, manage, and monetize customer‑owned assets such as solar, storage, and smart thermostats. The platform offers APIs for device connectivity, data ingestion, analytics, optimization, and marketplace trading, helping clients launch energy‑as‑a‑service offerings at scale.
image: https://cdn.prod.website-files.com/6a1ea3d2fadda55965f01117/6a3bec1ee12fbef0b37a2548_fever-home-thumb.jpg
layout: provider
modified: '2026-10-29'
name: Fever
nav: Providers
network: true
overview: 'Fever is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Platform, Distributed-Resources, and API.


  Fever''s developer surface includes sandbox and 6 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fever Energy Domain Security
  slug: fever-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fever-energy
tags:
- Company
- Energy
- Platform
- Distributed-Resources
- API
website: https://www.fever.energy/
---
