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
    agent_card: near-conformant
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
  score: 9.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agenty API for managing agent pages
  name: Agenty API
  slug: agenty-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/agenty-im/conformance/agenty-im-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenty-im-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenty-im/llms/agenty-im-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenty-im-llms.txt
- group: other
  href: https://artifacts.apis.io/agenty-im/a2a/agenty-im-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agenty-im-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agenty-im/well-known/agenty-im-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenty-im-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenty-im/hosts/agenty-im-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenty-im-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenty-im/vendors/agenty-im-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenty-im-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agenty-im/authentication/agenty-im-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agenty-im-authentication.yml
- group: auth
  href: https://artifacts.apis.io/agenty-im/security/agenty-im-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenty-im-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenty.im/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agenty.im/developers
- group: docs
  title: ''
  type: Documentation
  url: https://agenty.im/developers
- group: docs
  title: ''
  type: APIReference
  url: https://agenty.im/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://agenty.im/developers#quickstart
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/agenty-im/workspace
created: '2026-11-01'
description: 'agenty-im is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://agenty.im/og.png?v=2026-08-07
layout: provider
modified: '2026-11-01'
name: Agenty
nav: Providers
network: true
overview: 'Agenty is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Identity, Handle verification, and Agent API.


  Agenty''s developer surface includes authentication, documentation, API reference, getting-started guide, and 10 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 16.6
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenty Im Authentication
  slug: agenty-im-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Agenty Im Domain Security
  slug: agenty-im-domain-security
  summary_line: TLSv1.3
slug: agenty-im
tags:
- Identity
- Handle verification
- Agent API
website: https://agenty.im/
---
