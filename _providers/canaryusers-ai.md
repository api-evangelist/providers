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
- description: CanaryUsers provides AI‑driven user testing via an MCP endpoint. No public OpenAPI or other machine‑readable contract was found.
  name: CanaryUsers API
  slug: canaryusers-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/canaryusers-ai/mcp/canaryusers-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canaryusers-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/canaryusers-ai/hosts/canaryusers-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canaryusers-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/canaryusers-ai/vendors/canaryusers-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canaryusers-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canaryusers.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canaryusers.ai/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://www.canaryusers.ai/login
- group: company
  title: ''
  type: Blog
  url: https://www.canaryusers.ai/blog
- group: auth
  href: https://artifacts.apis.io/canaryusers-ai/security/canaryusers-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canaryusers-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.canaryusers.ai/
coverage:
  checked: '2026-11-04'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was discovered despite probing known hosts.
  evidence:
  - status: 405
    url: https://www.canaryusers.ai/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CanaryUsers provides AI‑driven user testing by sending lifelike simulated users through web applications on each deployment. Their platform captures clicks, typing, confusion points, and drop‑off moments, delivering actionable insights so developers can fix usability issues before real users encounter them. The service includes a scanning tool, detailed reports, and integrations for continuous testing, helping teams improve conversion, reduce friction, and ensure a smoother user experience.
layout: provider
mcp_servers:
- description: Remote MCP server at www.canaryusers.ai.
  name: CanaryUsers MCP Server
  slug: canaryusers-ai-mcp-yml
modified: '2026-11-04'
name: CanaryUsers
nav: Providers
network: true
overview: 'CanaryUsers is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Testing, User Experience, Software-as-a-Service, and CanaryUsers.


  CanaryUsers'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canaryusers Ai Domain Security
  slug: canaryusers-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: canaryusers-ai
tags:
- Artificial Intelligence
- Testing
- User Experience
- Software-as-a-Service
- CanaryUsers
website: https://www.canaryusers.ai/
---
