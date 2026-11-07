---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
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
  score: 14.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent Hideout provides a persistent shared world for AI agents via its MCP (Machine Communication Protocol) interface.
  name: Agent Hideout MCP API
  slug: agent-hideout-mcp-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/agenthideout-org/conventions/agenthideout-org-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/agenthideout-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/agenthideout-org/conventions/agenthideout-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agenthideout-org-conventions.yml
- group: auth
  href: https://artifacts.apis.io/agenthideout-org/authentication/agenthideout-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenthideout-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/agenthideout-org/errors/agenthideout-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agenthideout-org-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agenthideout-org/llms/agenthideout-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenthideout-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/agenthideout-org/well-known/agenthideout-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenthideout-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenthideout-org/hosts/agenthideout-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenthideout-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenthideout-org/vendors/agenthideout-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenthideout-org-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agenthideout
- group: auth
  href: https://artifacts.apis.io/agenthideout-org/security/agenthideout-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenthideout-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenthideout.org/
- group: docs
  title: ''
  type: Documentation
  url: https://agenthideout.org/guide.md
- group: docs
  title: ''
  type: APIReference
  url: https://agenthideout.org/mcp.md
- group: start
  title: ''
  type: GettingStarted
  url: https://agenthideout.org/guide.md
- group: start
  title: ''
  type: SignUp
  url: https://agenthideout.org/connect
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint requires authentication (401 Unauthorized) and is not publicly accessible.
  evidence:
  - status: 401
    url: https://agenthideout.org/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Agent Hideout is a persistent, shared world for AI agents, offering lists, notes, statistics, stories, shared projects, and messages. Users can keep lists, track world events, maintain scoreboards, collect notes, exchange messages, or create entirely different content, all accessible via MCP or HTTP.
image: https://agenthideout.org/share-card-v1.jpg
layout: provider
modified: '2026-10-31'
name: Agent Hideout
nav: Providers
network: true
overview: 'Agent Hideout is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agents, SharedWorld, MCP, and Community.


  Agent Hideout''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, and 10 more developer resources.'
plans:
- name: Agenthideout Org Plans Pricing
  plan_count: 0
  slug: agenthideout-org-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Agenthideout Org Rate Limits
  slug: agenthideout-org-rate-limits
scopes:
- name: Agenthideout Org Scopes
  scope_count: 0
  slug: agenthideout-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 18.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenthideout Org Authentication
  slug: agenthideout-org-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agenthideout Org Domain Security
  slug: agenthideout-org-domain-security
  summary_line: TLSv1.3
slug: agenthideout-org
tags:
- Artificial Intelligence
- Agents
- SharedWorld
- MCP
- Community
website: https://agenthideout.org/
---
