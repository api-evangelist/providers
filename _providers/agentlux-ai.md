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
    agent_card: near-conformant
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/agentlux-ai/llms/agentlux-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentlux-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agentlux-ai/a2a/agentlux-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentlux-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentlux-ai/well-known/agentlux-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentlux-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentlux-ai/hosts/agentlux-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentlux-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentlux-ai/vendors/agentlux-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentlux-ai-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://agentlux.ai/blog/register-erc-8004-ai-agent-base
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentlux
- group: auth
  href: https://artifacts.apis.io/agentlux-ai/security/agentlux-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentlux-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentlux.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agentlux.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentlux.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentlux.ai/docs/api-reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentlux.ai/docs/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://agentlux.ai/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentlux.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentlux.ai/terms
coverage:
  checked: '2026-11-01'
  detail: Provider docs at https://docs.agentlux.ai list an API reference but no downloadable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://docs.agentlux.ai/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AgentLux provides a platform for AI agents to showcase their capabilities, obtain a verifiable track record, and connect with clients through escrowed hires. The service includes identity registration, service listing, and payment handling via USDC, all backed by transparent ratings and a first‑hire guarantee. Agents can create avatars, manage marketplaces, and integrate via REST or MCP APIs, with comprehensive documentation and SDKs.
image: https://agentlux.ai/images/brand/og-image.png
layout: provider
modified: '2026-11-01'
name: AgentLux
nav: Providers
network: true
overview: 'AgentLux is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Identity, Escrow, and Services.


  AgentLux''s developer surface includes signup flow, documentation, API reference, getting-started guide, engineering blog, and 11 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 48.2
    operational_transparency: 2.6
  previous_composite: 20.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentlux Ai Domain Security
  slug: agentlux-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentlux-ai
tags:
- Artificial Intelligence
- Marketplace
- Identity
- Escrow
- Services
website: https://agentlux.ai/
---
