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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
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
  score: 35.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agenticweb Wiki Agentic Access
  operation_count: 11
  slug: agenticweb-wiki-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: Every record, CC BY 4.0, as JSON, CSV, NDJSON and per-record files, with a schema and an OpenAPI description.
  name: Data API
  slug: data-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/agenticweb-wiki/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/agenticweb-wiki/agentic-access/agenticweb-wiki-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agenticweb-wiki-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agenticweb-wiki/rules/agenticweb-wiki-rules.yml
  title: ''
  type: Spectral
  url: rules/agenticweb-wiki-rules.yml
- group: operate
  href: https://artifacts.apis.io/agenticweb-wiki/changelog/agenticweb-wiki-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/agenticweb-wiki-changelog.yml
- group: design
  href: https://artifacts.apis.io/agenticweb-wiki/conformance/agenticweb-wiki-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenticweb-wiki-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenticweb-wiki/llms/agenticweb-wiki-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenticweb-wiki-llms.txt
- group: other
  href: https://artifacts.apis.io/agenticweb-wiki/a2a/agenticweb-wiki-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agenticweb-wiki-a2a.yml
- group: build
  href: https://artifacts.apis.io/agenticweb-wiki/mcp/agenticweb-wiki-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agenticweb-wiki-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agenticweb-wiki/mcp/agenticweb-wiki-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenticweb-wiki-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agenticweb-wiki/well-known/agenticweb-wiki-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agenticweb-wiki-security.txt
- group: agent
  href: https://artifacts.apis.io/agenticweb-wiki/well-known/agenticweb-wiki-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenticweb-wiki-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenticweb-wiki/hosts/agenticweb-wiki-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticweb-wiki-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticweb-wiki/vendors/agenticweb-wiki-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticweb-wiki-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://agenticweb.wiki/status/
- group: auth
  title: ''
  type: Security
  url: https://agenticweb.wiki/security/
- group: build
  title: ''
  type: Postman
  url: https://agenticweb.wiki/check/postman.com/
- group: company
  title: ''
  type: Newsroom
  url: https://agenticweb.wiki/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://agenticweb.wiki/changelog/
- group: auth
  href: https://artifacts.apis.io/agenticweb-wiki/security/agenticweb-wiki-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agenticweb-wiki-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agenticweb-wiki/security/agenticweb-wiki-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticweb-wiki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticweb.wiki/
- group: docs
  title: ''
  type: APIReference
  url: https://agenticweb.wiki/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenticweb.wiki/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenticweb.wiki/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Belgravia-Labs
created: '2026-11-01'
description: 'agenticweb.wiki is a reference for the standards that let software agents use the web: how an agent finds what a site offers, proves who it is, learns what it may do, reads, acts, coordinates, pays, presents, and is held to account. It provides a wiki of 132 standards across nine steps (discover, identify, permit, read, act, coordinate, pay, present, account), each article written from the primary specification with numbered references. The site also offers a live Model Context Protocol (MCP) probe that returns what a domain publishes for agents, and publishes data in markdown, JSON, and Open Knowledge Format bundles.'
image: https://agenticweb.wiki/static/brand/og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at agenticweb.wiki.
  name: agenticweb-wiki MCP Server
  slug: agenticweb-wiki-mcp-yml
modified: '2026-11-01'
name: agenticweb-wiki
nav: Providers
network: true
overview: 'agenticweb-wiki is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web Standards, Agents, API Documentation, Open Knowledge, and MCP.


  The agenticweb-wiki catalog on APIs.io includes 1 Spectral governance ruleset.


  agenticweb-wiki''s developer surface includes changelog, API reference, and 23 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: agenticweb-wiki API Rules
  rule_count: 5
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 1
  slug: agenticweb-wiki-rules
scopes:
- name: Agenticweb Wiki Scopes
  scope_count: 0
  slug: agenticweb-wiki-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.1
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 12.4
    discoverability: 65.8
    operational_transparency: 23.7
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenticweb Wiki Authentication
  slug: agenticweb-wiki-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agenticweb Wiki Domain Security
  slug: agenticweb-wiki-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Agenticweb Wiki Vulnerability Disclosure
  slug: agenticweb-wiki-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agenticweb-wiki
tags:
- Web Standards
- Agents
- API Documentation
- Open Knowledge
- MCP
- Data
website: https://agenticweb.wiki/
---
