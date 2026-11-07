---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for AgentMesh platform, covering Connect, Control, and Combine services.
  name: AgentMesh API
  slug: agentmesh-api
artifact_total: 3
common:
- group: build
  href: https://artifacts.apis.io/agentmesh-ai/cli/agentmesh-ai-cli.yml
  title: ''
  type: CLI
  url: cli/agentmesh-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/agentmesh-ai/authentication/agentmesh-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentmesh-ai-authentication.yml
- group: agent
  href: https://artifacts.apis.io/agentmesh-ai/llms/agentmesh-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentmesh-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentmesh-ai/well-known/agentmesh-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentmesh-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentmesh-ai/hosts/agentmesh-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentmesh-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentmesh.ai/terms.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.agentmesh.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentmesh.ai/privacy.html
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.agentmesh.ai/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://dev.agentmesh.ai/
- group: auth
  href: https://artifacts.apis.io/agentmesh-ai/security/agentmesh-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentmesh-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentmesh.ai/
coverage:
  checked: '2026-11-01'
  detail: Developer docs are rendered with JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://dev.agentmesh.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: AgentMesh is a network for every agent your company runs, buys or works with. It offers Connect to make each agent known, Control to keep it managed, and Combine to put agents to work together. The platform is built by AgentMesh, Inc., based in Denver, CO, aiming to simplify multi‑agent orchestration across enterprises.
image: https://agentmesh.ai/brand/png/og-image.png
layout: provider
modified: '2026-11-01'
name: AgentMesh
nav: Providers
network: true
overview: 'AgentMesh is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Platform, and Orchestration.


  AgentMesh''s developer surface includes CLI, authentication, getting-started guide, documentation, and 8 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentmesh Ai Authentication
  slug: agentmesh-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Agentmesh Ai Domain Security
  slug: agentmesh-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentmesh-ai
tags:
- Company
- Artificial Intelligence
- Agents
- Platform
- Orchestration
website: https://agentmesh.ai/
---
