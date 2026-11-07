---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/askagent-dev/plans/askagent-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askagent-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/askagent-dev/llms/askagent-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askagent-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/askagent-dev/mcp/askagent-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/askagent-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/askagent-dev/hosts/askagent-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askagent-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/askagent-dev/vendors/askagent-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askagent-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askagent.dev/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askagent.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://askagent.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://askagent.dev/login
- group: auth
  href: https://artifacts.apis.io/askagent-dev/security/askagent-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askagent-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askagent.dev/
coverage:
  checked: '2026-11-01'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were discoverable despite documented API reference pages.
  evidence:
  - status: 404
    url: https://api.askagent.dev/openapi.json
  - status: 404
    url: https://api.askagent.dev/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AskAgent provides a platform where developers can submit, share, and monetize AI agent solutions. The service offers a searchable repository of agents that solve specific problems, with detailed error logs, fixes, and community insights. Pricing starts at $1 per month, with annual plans available. The site includes documentation, pricing, and a signup flow, emphasizing rapid access to AI-driven tooling for developers.
layout: provider
mcp_servers:
- description: Remote MCP server at askagent.dev.
  name: AskAgent MCP Server
  slug: askagent-dev-mcp-yml
modified: '2026-11-01'
name: AskAgent
nav: Providers
network: true
overview: 'AskAgent is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Documentation, Pricing, and Community.


  AskAgent''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Askagent Dev Plans Pricing
  plan_count: 2
  slug: askagent-dev-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.0
    operational_transparency: 0.0
  previous_composite: 17.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askagent Dev Domain Security
  slug: askagent-dev-domain-security
  summary_line: TLSv1.3
slug: askagent-dev
tags:
- Artificial Intelligence
- Platform
- Documentation
- Pricing
- Community
website: https://askagent.dev/
---
