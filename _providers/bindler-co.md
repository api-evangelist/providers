---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bindler Co Agentic Access
  operation_count: 9
  slug: bindler-co-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- baseURL: https://bindler.co/api/v1
  baseurl_source: declared
  description: The Ai Act Classify API from Bindler — 1 operation(s) for ai act classify.
  name: Bindler Ai Act Classify API
  slug: bindler-co-ai-act-classify-api
- baseURL: https://bindler.co/api/v1
  baseurl_source: declared
  description: The Cbam Cost API from Bindler — 1 operation(s) for cbam cost.
  name: Bindler Cbam Cost API
  slug: bindler-co-cbam-cost-api
- baseURL: https://bindler.co/api/v1
  baseurl_source: declared
  description: The Uae Corporate Tax API from Bindler — 1 operation(s) for uae corporate tax.
  name: Bindler Uae Corporate Tax API
  slug: bindler-co-uae-corporate-tax-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/bindler-co/agentic-access/bindler-co-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bindler-co-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bindler-co/rules/bindler-co-rules.yml
  title: ''
  type: Spectral
  url: rules/bindler-co-rules.yml
- group: design
  href: https://artifacts.apis.io/bindler-co/errors/bindler-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bindler-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bindler-co/conformance/bindler-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bindler-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bindler-co/llms/bindler-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bindler-co-llms.txt
- group: build
  href: https://artifacts.apis.io/bindler-co/mcp/bindler-co-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bindler-co-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/bindler-co/mcp/bindler-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bindler-co-mcp.yml
- group: other
  href: https://artifacts.apis.io/bindler-co/hosts/bindler-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bindler-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/bindler-co/vendors/bindler-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bindler-co-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://bindler.co/status/
- group: docs
  title: ''
  type: Documentation
  url: https://bindler.co/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://bindler.co/whats-new/
- group: auth
  href: https://artifacts.apis.io/bindler-co/authentication/bindler-co-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bindler-co-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bindler-co/security/bindler-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bindler-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bindler.co/
created: '2026-11-02'
description: Bindler provides Excel workbooks, decks and datasets covering regulations such as the EU AI Act, CSRD, CBAM, IFRS S2, UAE tax and e‑invoicing, plus startup and project finance models. These tools help small companies comply by offering live‑formula spreadsheets, fully sourced data, and fixed‑price services sold through Gumroad.
image: https://bindler.co/img/aiact-cover.png
layout: provider
mcp_servers:
- description: Remote MCP server at bindler.co.
  name: Bindler MCP Server
  slug: bindler-co-mcp-yml
modified: '2026-11-02'
name: Bindler
nav: Providers
network: true
overview: 'Bindler publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Ai Act Classify API, Cbam Cost API, and Uae Corporate Tax API. Tagged areas include Company, Data, Finance, Regulations, and Tools.


  The Bindler catalog on APIs.io includes 1 Spectral governance ruleset.


  Bindler''s developer surface includes documentation, API reference, authentication, and 12 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Bindler API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: bindler-co-rules
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 45.5
    developer_ergonomics: 20.2
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bindler Co Authentication
  slug: bindler-co-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Bindler Co Domain Security
  slug: bindler-co-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bindler-co
tags:
- Company
- Data
- Finance
- Regulations
- Tools
website: https://bindler.co/
---
