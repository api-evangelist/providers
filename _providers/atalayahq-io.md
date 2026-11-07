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
api_count: 1
apis:
- description: MCP (Multi-Channel Platform) API allowing AI assistants to interact with Atalaya tasks, sprints, and resources.
  name: Atalaya MCP API
  slug: atalaya-mcp-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/atalayahq-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/atalayahq-io/llms/atalayahq-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atalayahq-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/atalayahq-io/mcp/atalayahq-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atalayahq-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/atalayahq-io/hosts/atalayahq-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atalayahq-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/atalayahq-io/vendors/atalayahq-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atalayahq-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/atalayahq-io/security/atalayahq-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atalayahq-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atalayahq.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atalayahq.io/condiciones/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atalayahq.io/privacidad/
- group: operate
  title: ''
  type: Support
  url: https://atalayahq.io/para/soporte/
- group: start
  title: ''
  type: GettingStarted
  url: https://atalayahq.io/para/sdd/
- group: docs
  title: ''
  type: Documentation
  url: https://atalayahq.io/mcp/
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint https://app.atalayahq.io/api/mcp requires an Authorization token (401).
  evidence:
  - status: 401
    url: https://app.atalayahq.io/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Atalaya provides an AI‑powered work management platform for product managers and product teams. It enables teams to plan, prioritize, and execute projects using AI agents that translate natural‑language requests into actionable development plans, generate code, and automate testing. Users can create tasks, approve plans, and track progress without directly interacting with GitHub, leveraging large language models such as Claude Code and any MCP‑compatible assistant. The platform includes sprint boards, backlog management, automated code generation, and integration with communication tools, aiming to increase productivity and reduce manual coordination.
image: https://atalayahq.io/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.atalayahq.io.
  name: Atalaya MCP Server
  slug: atalayahq-io-mcp-yml
modified: '2026-11-01'
name: Atalaya
nav: Providers
network: true
overview: 'Atalaya is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Project Management, Automation, Productivity, and Collaboration.


  Atalaya''s developer surface includes support, getting-started guide, documentation, and 9 more developer resources.'
plans:
- name: Atalayahq Io Plans Pricing
  plan_count: 0
  slug: atalayahq-io-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Atalayahq Io Rate Limits
  slug: atalayahq-io-rate-limits
scopes:
- name: Atalayahq Io Scopes
  scope_count: 0
  slug: atalayahq-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.5
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 17.4
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atalayahq Io Authentication
  slug: atalayahq-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atalayahq Io Domain Security
  slug: atalayahq-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atalayahq-io
tags:
- Artificial Intelligence
- Project Management
- Automation
- Productivity
- Collaboration
website: https://atalayahq.io/
---
