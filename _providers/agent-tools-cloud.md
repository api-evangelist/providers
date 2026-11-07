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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 8.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Discovery and MCP directory API as described in the OpenAPI spec.
  name: Agent Tools Cloud API
  slug: agent-tools-cloud-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/agent-tools-cloud/conformance/agent-tools-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-tools-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agent-tools-cloud/llms/agent-tools-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-tools-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/agent-tools-cloud/a2a/agent-tools-cloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agent-tools-cloud-a2a.yml
- group: other
  href: https://artifacts.apis.io/agent-tools-cloud/hosts/agent-tools-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-tools-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-tools-cloud/vendors/agent-tools-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-tools-cloud-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agent-tools.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agent-tools.cloud/privacy
- group: start
  title: ''
  type: Login
  url: https://agent-tools.cloud/auth/github/login
- group: docs
  title: ''
  type: APIReference
  url: https://agent-tools.cloud/docs/claim
- group: auth
  href: https://artifacts.apis.io/agent-tools-cloud/security/agent-tools-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-tools-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent-tools.cloud/
created: '2026-10-31'
description: Agent Tools provides an open discovery layer for the agent economy, indexing x402 paid APIs, MCP servers, and A2A agents. It aggregates data from sources like Smithery, the official MCP registry, Apify, Agenstry, Prowl, and community lists, offering searchable, safety‑scanned entries. The service is free, requires no signup for read access, and aims to help developers and AI agents find and evaluate callable services safely.
layout: provider
modified: '2026-10-31'
name: Agent Tools
nav: Providers
network: true
overview: 'Agent Tools is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Discovery, Directory, x402, MCP, and A2A.


  Agent Tools'' developer surface includes API reference and 10 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 15.6
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agent Tools Cloud Domain Security
  slug: agent-tools-cloud-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agent-tools-cloud
tags:
- Discovery
- Directory
- x402
- MCP
- A2A
website: https://agent-tools.cloud/
---
