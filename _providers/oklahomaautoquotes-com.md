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
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Indicative US personal auto insurance prices for AI agents acting as customers.
  name: Oklahoma Insurance API
  slug: oklahoma-insurance-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/oklahomaautoquotes-com/rules/oklahomaautoquotes-com-rules.yml
  title: ''
  type: Spectral
  url: rules/oklahomaautoquotes-com-rules.yml
- group: design
  href: https://artifacts.apis.io/oklahomaautoquotes-com/conformance/oklahomaautoquotes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/oklahomaautoquotes-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/oklahomaautoquotes-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/oklahomaautoquotes-com/errors/oklahomaautoquotes-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/oklahomaautoquotes-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/oklahomaautoquotes-com/llms/oklahomaautoquotes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/oklahomaautoquotes-com-llms.txt
- group: other
  href: https://artifacts.apis.io/oklahomaautoquotes-com/a2a/oklahomaautoquotes-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/oklahomaautoquotes-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/oklahomaautoquotes-com/mcp/oklahomaautoquotes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/oklahomaautoquotes-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/oklahomaautoquotes-com/hosts/oklahomaautoquotes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oklahomaautoquotes-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/oklahomaautoquotes-com/vendors/oklahomaautoquotes-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oklahomaautoquotes-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/oklahomaautoquotes-com/security/oklahomaautoquotes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oklahomaautoquotes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oklahomaautoquotes.com/
- group: docs
  title: ''
  type: APIReference
  url: https://oklahomaautoquotes.com/openapi.json
- group: agent
  title: ''
  type: WellKnown
  url: https://oklahomaautoquotes.com/.well-known/api-catalog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oklahomaautoquotes.com/privacy
created: '2026-10-30'
description: Oklahoma Auto Quotes provides auto insurance quotes for residents of Oklahoma. The service connects users with licensed insurance agents to obtain personalized quotes without requiring a phone call. It emphasizes transparency, allowing customers to compare options and choose coverage that fits their needs, with a focus on simplicity and no-pressure sales.
layout: provider
mcp_servers:
- description: Remote MCP server at oklahomaautoquotes.com.
  name: oklahomaautoquotes-com MCP Server
  slug: oklahomaautoquotes-com-mcp-yml
modified: '2026-10-30'
name: oklahomaautoquotes-com
nav: Providers
network: true
overview: 'oklahomaautoquotes-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Auto, Quotes, and Oklahoma.


  The oklahomaautoquotes-com catalog on APIs.io includes 1 Spectral governance ruleset.


  oklahomaautoquotes-com''s developer surface includes API reference and 13 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: oklahomaautoquotes-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: oklahomaautoquotes-com-rules
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 5.4
    discoverability: 73.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/oklahomaautoquotes-com/oklahomaautoquotes-com-2026-11-03T140505.png
security:
- kind: domain-security
  name: Oklahomaautoquotes Com Domain Security
  slug: oklahomaautoquotes-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: oklahomaautoquotes-com-contact-agent
  slug: oklahomaautoquotes-com-contact-agent
slug: oklahomaautoquotes-com
tags:
- Company
- Insurance
- Auto
- Quotes
- Oklahoma
website: https://oklahomaautoquotes.com/
---
