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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API surface referenced by developer portal but requires login to access documentation.
  name: Cymosoft API
  slug: cymosoft-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/cymosoft-com/llms/cymosoft-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cymosoft-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cymosoft-com/mcp/cymosoft-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cymosoft-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/cymosoft-com/hosts/cymosoft-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cymosoft-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cymosoft-com/vendors/cymosoft-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cymosoft-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.cymosoft.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cymosoft
- group: auth
  href: https://artifacts.apis.io/cymosoft-com/security/cymosoft-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cymosoft-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cymosoft.com/
created: '2026-11-04'
description: Cymosoft JSC is an AI‑first engineering partner based in Hanoi, Vietnam. We specialize in turning generative AI, large language models, and enterprise data into production‑grade systems. Our services include AI offshore development centers, custom model integration, prompt engineering, and end‑to‑end deployment pipelines, helping clients accelerate AI adoption while managing cost, security, and scalability.
image: https://cymosoft.com/images/backgrounds/hero-area.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at cymosoft.com.
  name: Cymosoft JSC MCP Server
  slug: cymosoft-com-mcp-yml
modified: '2026-11-04'
name: Cymosoft JSC
nav: Providers
network: true
overview: Cymosoft JSC is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Engineering, Services, Vietnam, and Company.
random_paper: 0
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 56.7
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - vietnam
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cymosoft Com Domain Security
  slug: cymosoft-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cymosoft-com
tags:
- Artificial Intelligence
- Engineering
- Services
- Vietnam
- Company
website: https://cymosoft.com/
---
