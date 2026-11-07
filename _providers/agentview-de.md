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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/agentview-de/llms/agentview-de-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentview-de-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentview-de/mcp/agentview-de-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentview-de-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentview-de/well-known/agentview-de-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentview-de-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentview-de/hosts/agentview-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentview-de-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentview-de/security/agentview-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentview-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentview.de/
coverage:
  checked: '2026-11-01'
  detail: Documentation redirects to a Swagger UI page that does not expose a machine‑readable OpenAPI spec.
  evidence:
  - status: 302
    url: https://agentview.de/swagger/index.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: agentView provides AI-powered digital signage solutions, allowing users to control screen content via natural language prompts. Based in Germany, the platform offers a no‑installation, cloud‑based service for businesses to display menus, promotions, and custom messages on any screen. It emphasizes GDPR compliance, free tier access, and integrates with large language models like ChatGPT and Claude. The service includes live preview, logging, and rollback features, targeting sectors such as gastronomy, retail, and enterprises.
image: https://agentview.de/assets/logo_premium.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentview.de.
  name: agentView MCP Server
  slug: agentview-de-mcp-yml
modified: '2026-11-01'
name: agentView
nav: Providers
network: true
overview: agentView is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Digital Signage, GDPR, and Cloud.
random_paper: 16
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 4.2
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentview De Domain Security
  slug: agentview-de-domain-security
  summary_line: no transport/DNS hardening detected
slug: agentview-de
tags:
- Company
- Artificial Intelligence
- Digital Signage
- GDPR
- Cloud
website: https://agentview.de/
---
