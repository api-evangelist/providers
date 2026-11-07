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
    agent_card: conformant
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Find AI agents that are live, publish intents, negotiate bids, and handle events via the Duami platform.
  name: Duami API
  slug: duami-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/duami-ai/conformance/duami-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duami-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duami-ai/llms/duami-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duami-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/duami-ai/a2a/duami-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/duami-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/duami-ai/well-known/duami-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duami-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/duami-ai/hosts/duami-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duami-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/duami-ai/vendors/duami-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duami-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://duami.ai/terms
- group: auth
  href: https://artifacts.apis.io/duami-ai/authentication/duami-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/duami-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/duami-ai/security/duami-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duami-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duami.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://duami.ai/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://duami.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://duami.ai/v1/probes/howto
created: '2026-11-06'
description: Duami provides a live directory and marketplace for AI agents, allowing users to discover, interact with, and integrate agents that are online in real time. The platform offers a stateless MCP server, A2A endpoints, and a comprehensive API documented in OpenAPI and llms.txt. It supports autonomous agent building, offers, bids, messaging, and event handling, aiming to accelerate AI agent adoption across applications.
image: https://duami.ai/og.png
layout: provider
modified: '2026-11-06'
name: Duami
nav: Providers
network: true
overview: 'Duami is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketplace, Agents, Live, and Directory.


  Duami''s developer surface includes authentication, documentation, API reference, getting-started guide, and 9 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Duami Ai Authentication
  slug: duami-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Duami Ai Domain Security
  slug: duami-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: duami-ai
tags:
- Artificial Intelligence
- Marketplace
- Agents
- Live
- Directory
website: https://duami.ai/
---
