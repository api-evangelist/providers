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
    agent_skills: unknown
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
    mcp_server: false
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Affiliate MCP is an open-source, local-first automation platform that connects every affiliate network to large language models.
  name: Affiliate MCP
  slug: affiliate-mcp
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/agenticaffiliate-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://agenticaffiliate.ai/security
- group: other
  href: https://artifacts.apis.io/agenticaffiliate-ai/hosts/agenticaffiliate-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticaffiliate-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticaffiliate-ai/vendors/agenticaffiliate-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticaffiliate-ai-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/bobberrisford/affiliatemcp/releases/latest/download/affiliate-networks-mcp.mcpb
- group: start
  title: ''
  type: GettingStarted
  url: https://agenticaffiliate.ai/hosted-setup.html
- group: auth
  href: https://artifacts.apis.io/agenticaffiliate-ai/security/agenticaffiliate-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/agenticaffiliate-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/agenticaffiliate-ai/security/agenticaffiliate-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticaffiliate-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticaffiliate.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenticaffiliate.ai/privacy
coverage:
  checked: '2026-11-01'
  detail: Public documentation exists but no machine-readable OpenAPI, GraphQL, AsyncAPI, or other spec is published.
  evidence:
  - status: 200
    url: https://agenticaffiliate.ai/get-started.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Affiliate MCP is an open-source, local-first automation platform that connects every affiliate network to large language models such as Claude or Codex. Users can ask plain-English questions to retrieve affiliate performance data, generate reports, and approve actions. The service runs locally, ensuring data never leaves the user’s environment, and is free to use. It aims to streamline repetitive affiliate checks and empower marketers with AI-driven insights.
image: https://agenticaffiliate.ai/og.png
layout: provider
modified: '2026-11-01'
name: Affiliate MCP
nav: Providers
network: true
overview: 'Affiliate MCP is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Affiliates, Automation, Artificial Intelligence, Open Source, and Local-First.


  Affiliate MCP''s developer surface includes changelog, getting-started guide, and 8 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 12.4
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 16.5
  provenance:
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agenticaffiliate Ai Domain Security
  slug: agenticaffiliate-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Agenticaffiliate Ai Trust Center
  slug: agenticaffiliate-ai-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: agenticaffiliate-ai
tags:
- Affiliates
- Automation
- Artificial Intelligence
- Open Source
- Local-First
website: https://agenticaffiliate.ai/
---
