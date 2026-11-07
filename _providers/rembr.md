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
    agent_card: flavored
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
  score: 23.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Rembr provides AI-powered agent memory and debugging tools via its API.
  name: Rembr API
  slug: rembr-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/rembr/conformance/rembr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rembr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rembr/llms/rembr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rembr-llms.txt
- group: other
  href: https://artifacts.apis.io/rembr/a2a/rembr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/rembr-a2a.yml
- group: agent
  href: https://artifacts.apis.io/rembr/well-known/rembr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rembr-well-known.yml
- group: other
  href: https://artifacts.apis.io/rembr/hosts/rembr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rembr-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://rembr.ai/security
- group: start
  title: ''
  type: Login
  url: https://rembr.ai/login
- group: company
  title: ''
  type: Blog
  url: https://rembr.ai/blog
- group: auth
  href: https://artifacts.apis.io/rembr/security/rembr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rembr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rembr.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://rembr.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://rembr.ai/docs/api-migration
- group: start
  title: ''
  type: GettingStarted
  url: https://rembr.ai/docs/agent-guide
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rembr.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rembr.ai/terms
coverage:
  checked: '2026-10-18'
  detail: Documentation is publicly available at https://rembr.ai/docs but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other spec was found.
  evidence:
  - status: 200
    url: https://rembr.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Rembr provides AI-powered agent memory and debugging tools, enabling developers to capture, store, and query contextual snapshots of AI agents. Their platform offers portable memory, bounded context snapshots, relationship search, and temporal queries to streamline agent handoffs and improve debugging efficiency. With a focus on agent intelligence, Rembr delivers documentation, quick start guides, and secure login for seamless integration into AI workflows.
layout: provider
modified: '2026-10-18'
name: Rembr
nav: Providers
network: true
overview: 'Rembr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Agents, Memory, and Debugging.


  Rembr''s developer surface includes engineering blog, documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 60.7
    operational_transparency: 5.3
  previous_composite: 23.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rembr/rembr-2026-11-03T142135.png
security:
- kind: domain-security
  name: Rembr Domain Security
  slug: rembr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rembr
tags:
- Company
- Artificial Intelligence
- Agents
- Memory
- Debugging
website: https://rembr.ai/
---
