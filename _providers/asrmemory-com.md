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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ASR Memory provides an MCP memory server allowing AI tools to store and retrieve memories via a JSON-RPC endpoint. Documentation is at https://asrmemory.com/docs.html.
  name: ASR Memory API
  slug: asr-memory-api
artifact_total: 6
common:
- group: auth
  href: https://artifacts.apis.io/asrmemory-com/authentication/asrmemory-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asrmemory-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/asrmemory-com/conformance/asrmemory-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asrmemory-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asrmemory-com/llms/asrmemory-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asrmemory-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/asrmemory-com/well-known/asrmemory-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asrmemory-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/asrmemory-com/hosts/asrmemory-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asrmemory-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/asrmemory-com/security/asrmemory-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asrmemory-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asrmemory.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asrmemory.com/docs.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asrmemory.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asrmemory.com/privacy.html
coverage:
  checked: '2026-11-02'
  detail: Public documentation exists but no machine-readable OpenAPI, GraphQL, AsyncAPI, or other spec is published.
  evidence:
  - status: 200
    url: https://asrmemory.com/docs.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ASR Memory provides an MCP memory server that lets multiple AI tools share a common memory store. Users can save up to 1,000 memories for free, enabling AI agents to retain context across sessions. The platform offers API keys, a dashboard, and supports tools like Claude, Codex, and Gemini. It emphasizes privacy, with raw content stored and optional summaries for search.
image: https://asrmemory.com/assets/og-image.png
layout: provider
modified: '2026-11-02'
name: ASR Memory
nav: Providers
network: true
overview: 'ASR Memory is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, MCP, Servers, and Collaboration.


  ASR Memory''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Asrmemory Com Plans Pricing
  plan_count: 0
  slug: asrmemory-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Asrmemory Com Rate Limits
  slug: asrmemory-com-rate-limits
scopes:
- name: Asrmemory Com Scopes
  scope_count: 0
  slug: asrmemory-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 19.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asrmemory Com Authentication
  slug: asrmemory-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Asrmemory Com Domain Security
  slug: asrmemory-com-domain-security
  summary_line: TLSv1.3
slug: asrmemory-com
tags:
- Artificial Intelligence
- Memory
- MCP
- Servers
- Collaboration
website: https://asrmemory.com/
---
