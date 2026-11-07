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
    agent_skills: derived
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
  score: 4.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP server providing remote job listings and tool list.
  name: AnywhereRoles MCP
  slug: anywhereroles-mcp
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/anywhereroles-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/anywhereroles-com/llms/anywhereroles-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anywhereroles-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/anywhereroles-com/mcp/anywhereroles-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anywhereroles-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/anywhereroles-com/well-known/anywhereroles-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anywhereroles-com-security.txt
- group: agent
  href: https://artifacts.apis.io/anywhereroles-com/well-known/anywhereroles-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anywhereroles-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anywhereroles-com/hosts/anywhereroles-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anywhereroles-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anywhereroles-com/vendors/anywhereroles-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anywhereroles-com-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://anywhereroles.com/jobs/tag/registered-nurse
- group: auth
  title: ''
  type: Security
  url: https://anywhereroles.com/jobs/tag/security
- group: other
  title: ''
  type: Leadership
  url: https://anywhereroles.com/jobs/tag/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://anywhereroles.com/jobs/tag/documentation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anywhereroles.com/developers
- group: auth
  href: https://artifacts.apis.io/anywhereroles-com/security/anywhereroles-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anywhereroles-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anywhereroles-com/security/anywhereroles-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anywhereroles-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anywhereroles.com/
- group: company
  title: ''
  type: Blog
  url: https://anywhereroles.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://anywhereroles.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anywhereroles.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anywhereroles.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://anywhereroles.com/support
created: '2026-11-01'
description: AnywhereRoles aggregates remote job listings from multiple sources, providing a searchable platform where users can compare salaries, filter by category, and apply directly. The service offers both a web interface and native mobile apps for iOS and Android, enabling users to save roles, track applications, and receive weekly curated newsletters. Built by an independent developer, the platform remains free to use, supported by voluntary tips, and emphasizes privacy with minimal data collection.
image: https://anywhereroles.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at anywhereroles.com.
  name: AnywhereRoles MCP Server
  slug: anywhereroles-com-mcp-yml
modified: '2026-11-01'
name: AnywhereRoles
nav: Providers
network: true
overview: 'AnywhereRoles is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Remote Jobs, Job Search, Aggregator, Software-as-a-Service, and Productivity.


  AnywhereRoles'' developer surface includes signup flow, documentation, engineering blog, pricing, support, and 15 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.9
    discoverability: 65.8
    operational_transparency: 5.3
  previous_composite: 23.3
  provenance:
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anywhereroles Com Domain Security
  slug: anywhereroles-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Anywhereroles Com Vulnerability Disclosure
  slug: anywhereroles-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: search-jobs
  slug: anywhereroles-com-search_jobs
slug: anywhereroles-com
tags:
- Remote Jobs
- Job Search
- Aggregator
- Software-as-a-Service
- Productivity
website: https://anywhereroles.com/
---
