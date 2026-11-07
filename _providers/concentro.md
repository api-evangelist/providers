---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/concentro/llms/concentro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/concentro-llms.txt
- group: agent
  href: https://artifacts.apis.io/concentro/well-known/concentro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/concentro-well-known.yml
- group: other
  href: https://artifacts.apis.io/concentro/hosts/concentro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/concentro-hosts.yml
- group: other
  href: https://artifacts.apis.io/concentro/vendors/concentro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/concentro-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.concentro.io/blog
- group: auth
  href: https://artifacts.apis.io/concentro/security/concentro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/concentro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.concentro.io
coverage:
  checked: '2026-10-10'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.concentro.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-10'
description: Concentro makes tax credit transactions seamless and accessible for developers and corporate buyers, handling diligence, insurance, and transaction management. It offers a platform to buy, sell, and manage tax credit assets with an API-driven approach.
image: https://cdn.prod.website-files.com/6763d6cf120b46189e34bf8c/6786467699801f0d4c40ace0_opengraph.png
layout: provider
modified: '2026-10-10'
name: Concentro
nav: Providers
network: true
overview: 'Concentro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Tax Credits, API Platform, B2B, and Marketplace.


  Concentro''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 10.5
  previous_composite: 6.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/concentro/concentro-2026-11-03T125041.png
security:
- kind: domain-security
  name: Concentro Domain Security
  slug: concentro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: concentro
tags:
- Finance
- Tax Credits
- API Platform
- B2B
- Marketplace
website: https://www.concentro.io
---
