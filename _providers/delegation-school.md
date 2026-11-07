---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote Model Context Protocol server that delivers the delegation.school course inside the learner's AI assistant. Per the Connect page it is added in Claude as a custom connector at https://delegatio
  name: delegation.school MCP Server
  slug: delegation-school-mcp-server
artifact_total: 6
common:
- group: build
  href: https://artifacts.apis.io/delegation-school/integrations/delegation-school-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/delegation-school-integration-edges.yml
- group: commercial
  href: https://artifacts.apis.io/delegation-school/plans/delegation-school-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delegation-school-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/delegation-school/changelog/delegation-school-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/delegation-school-changelog.yml
- group: design
  href: https://artifacts.apis.io/delegation-school/conventions/delegation-school-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delegation-school-conventions.yml
- group: design
  href: https://artifacts.apis.io/delegation-school/lifecycle/delegation-school-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/delegation-school-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/delegation-school/conformance/delegation-school-conformance.yml
  title: ''
  type: Conformance
  url: conformance/delegation-school-conformance.yml
- group: agent
  href: https://artifacts.apis.io/delegation-school/llms/delegation-school-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/delegation-school-llms.txt
- group: agent
  href: https://artifacts.apis.io/delegation-school/mcp/delegation-school-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/delegation-school-mcp.yml
- group: other
  href: https://artifacts.apis.io/delegation-school/hosts/delegation-school-hosts.yml
  title: ''
  type: Hosts
  url: hosts/delegation-school-hosts.yml
- group: other
  href: https://artifacts.apis.io/delegation-school/vendors/delegation-school-vendors.yml
  title: ''
  type: Vendors
  url: vendors/delegation-school-vendors.yml
- group: auth
  href: https://artifacts.apis.io/delegation-school/security/delegation-school-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delegation-school-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://delegation.school/
- group: start
  title: ''
  type: GettingStarted
  url: https://delegation.school/connect/
- group: docs
  title: ''
  type: Documentation
  url: https://delegation.school/course.md
- group: operate
  title: ''
  type: Support
  url: https://delegation.school/help/
- group: operate
  title: ''
  type: ChangeLog
  url: https://delegation.school/changelog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://delegation.school/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://delegation.school/terms/
created: '2026-11-05'
description: 'delegation.school is an interactive course from Capital Thought, LLC (a Capital Factory project built by Joshua Baer) that teaches working professionals to delegate real work to AI rather than just chat with it. The course runs inside the learner''s own AI assistant: Claude connects to it as a custom connector via the remote MCP server at https://delegation.school/mcp, and a portable course.md version works in ChatGPT, Gemini or Grok. Its 15 lessons cover briefings, decision rules, memory, saved skills, subagents, multi-model verification and building MCP servers.'
image: https://delegation.school/og/home.png
layout: provider
mcp_servers:
- description: 'Official remote MCP server for the delegation.school course (Capital Thought, LLC). Tool list captured live via MCP initialize + tools/list on the endpoint the provider advertises in its llms.txt and '
  name: delegation.school MCP Server
  slug: delegation-school
modified: '2026-11-05'
name: delegation.school
nav: Providers
network: true
overview: 'delegation.school is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Education, Online Courses, and MCP.


  delegation.school''s developer surface includes changelog, getting-started guide, documentation, support, and 14 more developer resources.'
plans:
- name: Delegation School Plans Pricing
  plan_count: 1
  slug: delegation-school-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Delegation School Rate Limits
  slug: delegation-school-rate-limits
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Delegation School Authentication
  slug: delegation-school-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Delegation School Domain Security
  slug: delegation-school-domain-security
  summary_line: TLSv1.3
slug: delegation-school
tags:
- Company
- Artificial Intelligence
- Education
- Online Courses
- MCP
- AI Agents
- Productivity
website: https://delegation.school/
---
