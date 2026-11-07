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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only graph API providing access to compounds, proteins, outcomes and their relationships.
  name: Catalyst Graph API
  slug: catalyst-graph-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/catalystproject-ai/hosts/catalystproject-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catalystproject-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/catalystproject-ai/vendors/catalystproject-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catalystproject-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/catalystproject-ai/security/catalystproject-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catalystproject-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catalystproject.ai/
coverage:
  checked: '2026-11-04'
  detail: The provider offers a read‑only graph API but does not publish any OpenAPI, GraphQL, AsyncAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://catalystproject.ai/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Catalyst provides computational infrastructure for human biology, offering a graph of compounds, proteins, and outcomes linked to scientific evidence. The platform enables researchers to explore data, run simulations, and integrate the API and MCP connector for bulk export and analysis. It showcases detailed compound information, evidence strength, and tools for building on the graph.
image: https://catalystproject.ai/opengraph-image?ea98fe8ebba562fd
layout: provider
modified: '2026-11-04'
name: Catalyst
nav: Providers
network: true
overview: Catalyst is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Computational Biology, Data Platform, Graph API, Human Biology, and Research Tools.
random_paper: 3
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catalystproject Ai Domain Security
  slug: catalystproject-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: catalystproject-ai
tags:
- Computational Biology
- Data Platform
- Graph API
- Human Biology
- Research Tools
website: https://catalystproject.ai/
---
