---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DarkFunnels provides a WhatsApp AI sales‑agent platform; the documentation is markdown and does not expose a machine‑readable API specification.
  name: DarkFunnels API
  slug: darkfunnels-api
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/darkfunnels-ai/rate-limits/darkfunnels-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/darkfunnels-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/darkfunnels-ai/plans/darkfunnels-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/darkfunnels-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/darkfunnels-ai/llms/darkfunnels-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/darkfunnels-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/darkfunnels-ai/a2a/darkfunnels-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/darkfunnels-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/darkfunnels-ai/mcp/darkfunnels-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/darkfunnels-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/darkfunnels-ai/well-known/darkfunnels-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/darkfunnels-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/darkfunnels-ai/hosts/darkfunnels-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/darkfunnels-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/darkfunnels-ai/vendors/darkfunnels-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/darkfunnels-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/darkfunnels-ai/security/darkfunnels-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/darkfunnels-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://darkfunnels.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.darkfunnels.ai/en
- group: docs
  title: ''
  type: Documentation
  url: https://docs.darkfunnels.ai/en
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.darkfunnels.ai/en/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.darkfunnels.ai/en/getting-started/pricing
- group: start
  title: ''
  type: SignUp
  url: https://optimind.darkfunnels.ai/register
- group: operate
  title: ''
  type: Support
  url: https://darkfunnels.ai/agents
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://darkfunnels.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://darkfunnels.ai/terminos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/darkfunnels-ai
coverage:
  checked: '2026-10-30'
  detail: Documentation is provided as markdown pages without any OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://docs.darkfunnels.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: DarkFunnels AI provides AI‑powered sales agents for WhatsApp, enabling businesses in Peru and Latin America to automate customer interactions, quote products, process payments, and record orders without needing Meta’s Business API. The platform offers a remote MCP server for integration with Claude, ChatGPT, or other tools, and includes a 7‑day trial with credit. It emphasizes human control, privacy, and compliance, targeting Spanish‑speaking merchants.
image: https://darkfunnels.ai/favicon.ico?v=20260924-1
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.darkfunnels.ai.
  name: darkfunnels-ai MCP Server
  slug: darkfunnels-ai-mcp-yml
modified: '2026-10-29'
name: darkfunnels-ai
nav: Providers
network: true
overview: 'darkfunnels-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, WhatsApp, SalesAutomation, Peru, and Automation.


  darkfunnels-ai''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, and 14 more developer resources.'
plans:
- name: Darkfunnels Ai Plans Pricing
  plan_count: 2
  slug: darkfunnels-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Darkfunnels Ai Rate Limits
  slug: darkfunnels-ai-rate-limits
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 56.7
    operational_transparency: 36.8
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Darkfunnels Ai Domain Security
  slug: darkfunnels-ai-domain-security
  summary_line: TLSv1.3
slug: darkfunnels-ai
tags:
- AI
- WhatsApp
- SalesAutomation
- Peru
- Automation
website: https://darkfunnels.ai/
---
