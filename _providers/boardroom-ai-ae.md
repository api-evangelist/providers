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
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/boardroom-ai-ae/plans/boardroom-ai-ae-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boardroom-ai-ae-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/boardroom-ai-ae/llms/boardroom-ai-ae-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boardroom-ai-ae-llms.txt
- group: agent
  href: https://artifacts.apis.io/boardroom-ai-ae/mcp/boardroom-ai-ae-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boardroom-ai-ae-mcp.yml
- group: agent
  href: https://artifacts.apis.io/boardroom-ai-ae/well-known/boardroom-ai-ae-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boardroom-ai-ae-well-known.yml
- group: other
  href: https://artifacts.apis.io/boardroom-ai-ae/hosts/boardroom-ai-ae-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boardroom-ai-ae-hosts.yml
- group: other
  href: https://artifacts.apis.io/boardroom-ai-ae/vendors/boardroom-ai-ae-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boardroom-ai-ae-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boardroom-ai.ae/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://control.boardroom-ai.ae/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boardroom-ai.ae/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.boardroom-ai.ae/pricing
- group: auth
  href: https://artifacts.apis.io/boardroom-ai-ae/security/boardroom-ai-ae-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boardroom-ai-ae-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boardroom-ai.ae/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found on any discovered host.
  evidence:
  - status: 302
    url: https://boardroom-ai.ae/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Boardroom AI is a UAE‑based AI revenue‑operations platform that builds and runs AI sales agents, CRM automation, follow‑up recovery, executive dashboards and media‑factory tools for businesses across the GCC and international markets. It offers modular AI agents, multi‑channel messaging, integration with major CRMs and a revenue control OS to capture, qualify and convert inbound leads.
image: https://www.boardroom-ai.ae/og/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at control.boardroom-ai.ae.
  name: Boardroom AI MCP Server
  slug: boardroom-ai-ae-mcp-yml
modified: '2026-11-02'
name: Boardroom AI
nav: Providers
network: true
overview: 'Boardroom AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Revenue, CRM, United Arab Emirates, and Software-as-a-Service.


  Boardroom AI''s developer surface includes signup flow, pricing, and 10 more developer resources.'
plans:
- name: Boardroom Ai Ae Plans Pricing
  plan_count: 12
  slug: boardroom-ai-ae-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boardroom Ai Ae Domain Security
  slug: boardroom-ai-ae-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boardroom-ai-ae
tags:
- Artificial Intelligence
- Revenue
- CRM
- United Arab Emirates
- Software-as-a-Service
website: https://boardroom-ai.ae/
---
