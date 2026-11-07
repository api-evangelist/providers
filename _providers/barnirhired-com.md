---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
api_count: 1
apis:
- description: Machine Control Protocol (MCP) API providing role guidance and how-it-works tools.
  name: Barnir Hired MCP API
  slug: barnir-hired-mcp-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/barnirhired-com/plans/barnirhired-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/barnirhired-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/barnirhired-com/llms/barnirhired-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barnirhired-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/barnirhired-com/mcp/barnirhired-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/barnirhired-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/barnirhired-com/hosts/barnirhired-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barnirhired-com-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://barnirhired.com/privacy
- group: auth
  href: https://artifacts.apis.io/barnirhired-com/security/barnirhired-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barnirhired-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barnirhired.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://barnirhired.com/pricing
- group: company
  title: ''
  type: About
  url: https://barnirhired.com/about
coverage:
  checked: '2026-11-02'
  detail: Provider only offers MCP JSON-RPC endpoint with no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://barnirhired.com/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Barnir Hired provides AI‑powered job fit analysis for technical roles. It helps candidates and hiring teams quickly assess fit by analyzing resumes, job descriptions, and public profiles without storing data. The service offers a free trial and paid plans, delivering detailed playbooks, interview strategies, and personalized feedback. Founded by a veteran technical go‑to‑market professional, Barnir Hired leverages proprietary methodology and domain expertise to improve hiring outcomes.
layout: provider
mcp_servers:
- description: Remote MCP server at barnirhired.com.
  name: Barnir Hired MCP Server
  slug: barnirhired-com-mcp-yml
modified: '2026-11-02'
name: Barnir Hired
nav: Providers
network: true
overview: 'Barnir Hired is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hiring, Artificial Intelligence, JobFit, TechnicalRoles, and Careers.


  Barnir Hired''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Barnirhired Com Plans Pricing
  plan_count: 4
  slug: barnirhired-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Barnirhired Com Domain Security
  slug: barnirhired-com-domain-security
  summary_line: TLSv1.3
slug: barnirhired-com
tags:
- Hiring
- Artificial Intelligence
- JobFit
- TechnicalRoles
- Careers
website: https://barnirhired.com/
---
