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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine-first marketplace API for AI agents to purchase templates and credits.
  name: DACIX Store API
  slug: dacix-store-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/dacix-store/conformance/dacix-store-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dacix-store-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dacix-store/llms/dacix-store-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dacix-store-llms.txt
- group: other
  href: https://artifacts.apis.io/dacix-store/hosts/dacix-store-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dacix-store-hosts.yml
- group: other
  href: https://artifacts.apis.io/dacix-store/vendors/dacix-store-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dacix-store-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://dacix.store/blog/how-ai-agents-buy
- group: docs
  title: ''
  type: APIReference
  url: https://dacix.store/docs
- group: auth
  href: https://artifacts.apis.io/dacix-store/security/dacix-store-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dacix-store-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dacix.store/
created: '2026-11-04'
description: DACIX is a machine‑first marketplace where AI agents can purchase agent templates and API credits via a plain REST API. It offers JWT authentication, Stripe checkout, and a catalog of tools that agents can buy to extend their capabilities, targeting developers building autonomous AI services. The platform emphasizes seamless integration for agents to acquire resources programmatically, supporting a growing ecosystem of AI‑driven applications.
layout: provider
modified: '2026-11-04'
name: DACIX
nav: Providers
network: true
overview: 'DACIX is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Artificial Intelligence, and Agents.


  DACIX''s developer surface includes engineering blog, API reference, and 6 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dacix Store Domain Security
  slug: dacix-store-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dacix-store
tags:
- Company
- Marketplace
- Artificial Intelligence
- Agents
website: https://dacix.store/
---
