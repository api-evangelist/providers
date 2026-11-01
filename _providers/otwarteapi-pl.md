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
  href: https://artifacts.apis.io/otwarteapi-pl/llms/otwarteapi-pl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/otwarteapi-pl-llms.txt
- group: other
  href: https://artifacts.apis.io/otwarteapi-pl/hosts/otwarteapi-pl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/otwarteapi-pl-hosts.yml
- group: other
  href: https://artifacts.apis.io/otwarteapi-pl/vendors/otwarteapi-pl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/otwarteapi-pl-vendors.yml
- group: auth
  href: https://artifacts.apis.io/otwarteapi-pl/security/otwarteapi-pl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/otwarteapi-pl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://otwarteapi.pl/
- group: docs
  title: ''
  type: Documentation
  url: https://otwarteapi.pl/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://otwarteapi.pl/.well-known/ai-catalog.json
coverage:
  checked: '2026-10-31'
  detail: The provider offers a public HTML catalog but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications are available.
  evidence:
  - status: 200
    url: https://otwarteapi.pl/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: otwarteapi.pl is a Polish public API catalog that aggregates open government and international datasets. It provides machine‑readable listings of APIs across 40 jurisdictions, covering tax registers, company registries, statistical data, weather, and more, all without mandatory authentication for most endpoints. The platform offers an AI‑friendly llms.txt and a .well-known/ai-catalog.json manifest, enabling agents to discover and query APIs automatically.
image: https://otwarteapi.pl/brand/og-image.png
layout: provider
modified: '2026-10-30'
name: otwarteapi-pl
nav: Providers
network: true
overview: 'otwarteapi-pl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenData, Government, API-Catalog, and Poland.


  otwarteapi-pl''s developer surface includes documentation, API reference, and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 7.1
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
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Otwarteapi Pl Domain Security
  slug: otwarteapi-pl-domain-security
  summary_line: TLSv1.3 · HSTS
slug: otwarteapi-pl
tags:
- Company
- OpenData
- Government
- API-Catalog
- Poland
website: https://otwarteapi.pl/
---
