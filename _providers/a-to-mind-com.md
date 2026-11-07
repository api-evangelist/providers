---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Void's public API provides code review, MCP server functions, and sports scores.
  name: Void API
  slug: void-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/a-to-mind-com/security/a-to-mind-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/a-to-mind-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/a-to-mind-com/conformance/a-to-mind-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/a-to-mind-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/a-to-mind-com/llms/a-to-mind-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a-to-mind-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/a-to-mind-com/mcp/a-to-mind-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/a-to-mind-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/a-to-mind-com/well-known/a-to-mind-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/a-to-mind-com-security.txt
- group: agent
  href: https://artifacts.apis.io/a-to-mind-com/well-known/a-to-mind-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/a-to-mind-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/a-to-mind-com/hosts/a-to-mind-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a-to-mind-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/a-to-mind-com/vendors/a-to-mind-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/a-to-mind-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://a-to-mind.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://a-to-mind.com/news/
- group: other
  title: ''
  type: Leadership
  url: https://a-to-mind.com/team/
- group: auth
  href: https://artifacts.apis.io/a-to-mind-com/security/a-to-mind-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/a-to-mind-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/a-to-mind-com/security/a-to-mind-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a-to-mind-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a-to-mind.com/
created: '2026-10-31'
description: Verse by A-to-Mind is an AI‑powered personal assistant platform that lets users ask for anything and get instant results – from clocks and notes to maps, weather, translations, calculations, or detailed pages on any topic. It operates without requiring an account, offering a seamless, on‑demand knowledge and productivity service.
image: https://a-to-mind.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at a-to-mind.com.
  name: A-to-Mind MCP Server
  slug: a-to-mind-com-mcp-yml
modified: '2026-10-31'
name: A-to-Mind
nav: Providers
network: true
overview: A-to-Mind publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Productivity, Personal Assistant, Knowledge Base, and Automation.
plans:
- name: A To Mind Com Plans Pricing
  plan_count: 0
  slug: a-to-mind-com-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: A To Mind Com Rate Limits
  slug: a-to-mind-com-rate-limits
scopes:
- name: A To Mind Com Scopes
  scope_count: 0
  slug: a-to-mind-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 5.3
    contract_governance: 4.5
    contract_quality: 6.0
    developer_ergonomics: 0.0
    discoverability: 66.7
    operational_transparency: 10.5
  previous_composite: 14.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: A To Mind Com Authentication
  slug: a-to-mind-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: A To Mind Com Domain Security
  slug: a-to-mind-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: A To Mind Com Vulnerability Disclosure
  slug: a-to-mind-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: get-scores
  slug: a-to-mind-com-get-scores
- name: review-code
  slug: a-to-mind-com-review-code
slug: a-to-mind-com
tags:
- Artificial Intelligence
- Productivity
- Personal Assistant
- Knowledge Base
- Automation
website: https://a-to-mind.com/
---
