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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SlashYear provides a free, keyless API delivering a curated historical record of yearly events sourced from Wikipedia revisions.
  name: SlashYear API
  slug: slashyear-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/slashyear-com/rules/slashyear-com-rules.yml
  title: ''
  type: Spectral
  url: rules/slashyear-com-rules.yml
- group: design
  href: https://artifacts.apis.io/slashyear-com/errors/slashyear-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/slashyear-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/slashyear-com/conformance/slashyear-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/slashyear-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/slashyear-com/llms/slashyear-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/slashyear-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/slashyear-com/mcp/slashyear-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/slashyear-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/slashyear-com/hosts/slashyear-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/slashyear-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/slashyear-com/vendors/slashyear-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/slashyear-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/slashyear-com/security/slashyear-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slashyear-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slashyear.com
coverage:
  checked: '2026-10-27'
  detail: The provider's website serves HTML only and no OpenAPI, GraphQL, or other machine‑readable contract was found.
  evidence:
  - status: 404
    url: https://slashyear.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: SlashYear provides a free, keyless API delivering a curated historical record of yearly events sourced from Wikipedia revisions. Users can query by year, date, subject, or country, and access supporting data such as world leaders, Nobel prizes, and Billboard charts. The service is open, CORS-enabled, and includes OpenAPI 3.1 documentation.
image: https://slashyear.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at slashyear.com.
  name: SlashYear MCP Server
  slug: slashyear-com-mcp-yml
modified: '2026-10-27'
name: SlashYear
nav: Providers
network: true
overview: 'SlashYear publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include History, Data, Open, and Free.


  The SlashYear catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: SlashYear API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: slashyear-com-rules
score:
  band: minimal
  composite: 7.4
  coverage:
    artifact_dirs: 12
    catalog_earned: 31.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.3
    operational_transparency: 0.0
  previous_composite: 9.7
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/slashyear-com/slashyear-com-2026-11-03T143325.png
security:
- kind: domain-security
  name: Slashyear Com Domain Security
  slug: slashyear-com-domain-security
  summary_line: TLSv1.3
slug: slashyear-com
tags:
- History
- Data
- Open
- Free
website: https://slashyear.com
---
