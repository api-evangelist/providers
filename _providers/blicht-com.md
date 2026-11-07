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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Official MCP endpoint providing site info, topics, search, and articles.
  name: BLICHT Knowledge Platform
  slug: blicht-knowledge-platform
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/blicht-com/llms/blicht-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blicht-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/blicht-com/mcp/blicht-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blicht-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/blicht-com/well-known/blicht-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blicht-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blicht-com/hosts/blicht-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blicht-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blicht-com/vendors/blicht-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blicht-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/blicht-com/security/blicht-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blicht-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blicht.com/
coverage:
  checked: '2026-11-02'
  detail: Only an MCP markdown endpoint is available, no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://blicht.com/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BLICHT ist eine deutschsprachige Wissens‑Plattform an der Schnittstelle von Technologie, Wirtschaft und Alltag. Sie beleuchtet, wie Technologie Wirtschaft und Leben verändert – mit Fokus auf E‑Commerce, Künstliche Intelligenz und praxisnahe Analysen, ohne Hype. Herausgeber ist der E‑Commerce‑Unternehmer Boaz Lichtenstein, Mitgründer der Fashion‑Marke SASSYCLASSY.
image: https://blicht.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at blicht.com.
  name: BLICHT MCP Server
  slug: blicht-com-mcp-yml
modified: '2026-11-02'
name: BLICHT
nav: Providers
network: true
overview: BLICHT is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, KI, Alltag, Technologie, and Wirtschaft.
random_paper: 10
score:
  band: minimal
  composite: 4.3
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
    developer_ergonomics: 0.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
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
  name: Blicht Com Domain Security
  slug: blicht-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blicht-com
tags:
- E-Commerce
- KI
- Alltag
- Technologie
- Wirtschaft
website: https://blicht.com/
---
