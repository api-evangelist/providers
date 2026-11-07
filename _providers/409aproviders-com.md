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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Compare 409A valuation providers for US startups, includes pricing and audit support details.
  name: 409A Providers API
  slug: 409a-providers-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/409aproviders-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://409aproviders.com/terms
- group: design
  href: https://artifacts.apis.io/409aproviders-com/conformance/409aproviders-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/409aproviders-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/409aproviders-com/llms/409aproviders-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/409aproviders-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/409aproviders-com/mcp/409aproviders-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/409aproviders-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/409aproviders-com/well-known/409aproviders-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/409aproviders-com-security.txt
- group: agent
  href: https://artifacts.apis.io/409aproviders-com/well-known/409aproviders-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/409aproviders-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/409aproviders-com/hosts/409aproviders-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/409aproviders-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/409aproviders-com/vendors/409aproviders-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/409aproviders-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/409aproviders-com/security/409aproviders-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/409aproviders-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/409aproviders-com/security/409aproviders-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/409aproviders-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://409aproviders.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://409aproviders.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://409aproviders.com/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://409aproviders.com/contact/
created: '2026-10-31'
description: 409A Providers is an information site that compares 409A valuation providers for US startups. It publishes list prices, turnaround times, audit support details, and who signs the reports, based on each provider’s own published pages as of the date shown.
image: https://409aproviders.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at 409aproviders.com.
  name: 409A Providers MCP Server
  slug: 409aproviders-com-mcp-yml
modified: '2026-10-31'
name: 409A Providers
nav: Providers
network: true
overview: 409A Providers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 0
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 56.7
    operational_transparency: 5.3
  previous_composite: 14.5
  provenance:
    conformance: derived
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: 409Aproviders Com Domain Security
  slug: 409aproviders-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 409Aproviders Com Vulnerability Disclosure
  slug: 409aproviders-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: getting-started
  slug: 409aproviders-com-getting_started
slug: 409aproviders-com
tags:
- Company
website: https://409aproviders.com/
---
