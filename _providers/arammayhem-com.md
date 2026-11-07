---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/arammayhem-com/llms/arammayhem-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arammayhem-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/arammayhem-com/mcp/arammayhem-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arammayhem-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/arammayhem-com/hosts/arammayhem-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arammayhem-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arammayhem-com/vendors/arammayhem-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arammayhem-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arammayhem
- group: auth
  href: https://artifacts.apis.io/arammayhem-com/security/arammayhem-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arammayhem-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arammayhem.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arammayhem.com/privacy/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, or GraphQL specification found at standard endpoints (e.g., /openapi.json) on the provider's API host.
  evidence:
  - status: 404
    url: https://arammayhem.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ARAM Mayhem is a community‑run statistics hub for the League of Legends ARAM Mayhem game mode. The site provides up‑to‑date tier lists, champion builds, curated combos and augments for the current patch (26.21). It aggregates data on 173 champion builds, 674 combos and 207 augments, showing pick rates and tier rankings. The hub also offers patch notes, tier‑list explanations and visual guides for players looking to improve their performance in ARAM Mayhem.
image: https://arammayhem.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at arammayhem.com.
  name: ARAM Mayhem MCP Server
  slug: arammayhem-com-mcp-yml
modified: '2026-11-01'
name: ARAM Mayhem
nav: Providers
network: true
overview: ARAM Mayhem is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, League of Legends, Gaming, Stats, and Builds.
plans:
- name: Arammayhem Com Plans Pricing
  plan_count: 0
  slug: arammayhem-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Arammayhem Com Rate Limits
  slug: arammayhem-com-rate-limits
scopes:
- name: Arammayhem Com Scopes
  scope_count: 0
  slug: arammayhem-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 2.6
  previous_composite: 8.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arammayhem Com Authentication
  slug: arammayhem-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arammayhem Com Domain Security
  slug: arammayhem-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arammayhem-com
tags:
- Company
- League of Legends
- Gaming
- Stats
- Builds
- Augments
website: https://arammayhem.com/
---
