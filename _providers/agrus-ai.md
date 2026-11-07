---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
- description: Agrus.ai MCP server providing public read tools and one write tool.
  name: Agrus MCP
  slug: agrus-mcp
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/agrus-ai/plans/agrus-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agrus-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agrus-ai/llms/agrus-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agrus-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/agrus-ai/mcp/agrus-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agrus-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/agrus-ai/hosts/agrus-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agrus-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agrus-ai/vendors/agrus-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agrus-ai-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://agrus.ai/team/
- group: auth
  href: https://artifacts.apis.io/agrus-ai/security/agrus-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agrus-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agrus.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.agrus.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://agrus.ai/book/
- group: operate
  title: ''
  type: Support
  url: https://agrus.ai/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://agrus.ai/pricing/
created: '2026-11-01'
description: Agrus provides private LLM compliance engineering services, helping enterprises deploy AI agents within their own secure perimeter. Their offerings include compliance audits, self‑hosted LLM deployments, and industry‑specific solutions for healthcare, insurance, legal, private equity, and more. Agrus emphasizes data residency, security certifications such as HIPAA, SOC 2, ISO 27001, and compliance with regulations like the EU AI Act.
image: https://agrus.ai/opengraph-image?c28047ec10527269
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.agrus.ai.
  name: Agrus MCP Server
  slug: agrus-ai-mcp-yml
modified: '2026-11-01'
name: Agrus
nav: Providers
network: true
overview: 'Agrus is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Compliance, Enterprise, and Private-LLM.


  Agrus'' developer surface includes API reference, getting-started guide, support, pricing, and 8 more developer resources.'
plans:
- name: Agrus Ai Plans Pricing
  plan_count: 5
  slug: agrus-ai-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.8
    operational_transparency: 0.0
  previous_composite: 18.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agrus Ai Domain Security
  slug: agrus-ai-domain-security
  summary_line: TLSv1.3
slug: agrus-ai
tags:
- Company
- Artificial Intelligence
- Compliance
- Enterprise
- Private-LLM
website: https://agrus.ai/
---
