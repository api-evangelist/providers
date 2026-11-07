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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: 53On Com Agentic Access
  operation_count: 3
  slug: 53on-com-agentic-access
  summary_line: 3 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://53on.com
  baseurl_source: declared
  description: The S {service} API from 53ON — 1 operation(s) for s {service}.
  name: 53ON S {service} API
  slug: 53on-com-s-service-api
- baseURL: https://53on.com
  baseurl_source: declared
  description: The Xsite API from 53ON — 2 operation(s) for xsite.
  name: 53ON Xsite API
  slug: 53on-com-xsite-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/53on-com/agentic-access/53on-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/53on-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/53on-com/rules/53on-com-rules.yml
  title: ''
  type: Spectral
  url: rules/53on-com-rules.yml
- group: design
  href: https://artifacts.apis.io/53on-com/errors/53on-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/53on-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/53on-com/conformance/53on-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/53on-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/53on-com/llms/53on-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/53on-com-llms.txt
- group: other
  href: https://artifacts.apis.io/53on-com/a2a/53on-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/53on-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/53on-com/mcp/53on-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/53on-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/53on-com/mcp/53on-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/53on-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/53on-com/well-known/53on-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/53on-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/53on-com/hosts/53on-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/53on-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/53on-com/vendors/53on-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/53on-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/53on-com/security/53on-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/53on-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://53on.com/
created: '2026-10-31'
description: 53ON is a directory and marketplace of local businesses and independent professionals. It allows users to search by service and area, view ratings and prices, and book and pay in one place, providing a unified platform for discovering and hiring local service providers. The platform supports multiple languages and integrates with various payment gateways, aiming to simplify the process of finding and engaging local expertise.
image: https://53on.com/xsite/public/assets/img/53ONmeta.png
layout: provider
mcp_servers:
- description: Remote MCP server at 53on.com.
  name: 53ON MCP Server
  slug: 53on-com-mcp-yml
modified: '2026-10-31'
name: 53ON
nav: Providers
network: true
overview: '53ON publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: S {service} API and Xsite API. Tagged areas include Marketplace, Directory, Local Business, Services, and Consumer.


  The 53ON catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: 53ON API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: 53on-com-rules
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 47.1
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 19.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
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
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 53On Com Domain Security
  slug: 53on-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 53on-com
tags:
- Marketplace
- Directory
- Local Business
- Services
- Consumer
- Company
website: https://53on.com/
---
