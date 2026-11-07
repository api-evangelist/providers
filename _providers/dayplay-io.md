---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/dayplay-io/plans/dayplay-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dayplay-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dayplay-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dayplay-io/conformance/dayplay-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dayplay-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dayplay-io/llms/dayplay-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dayplay-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/dayplay-io/well-known/dayplay-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dayplay-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/dayplay-io/hosts/dayplay-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dayplay-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dayplay-io/vendors/dayplay-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dayplay-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dayplay-io/security/dayplay-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dayplay-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dayplay.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dayplay.io/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dayplay.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dayplay.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dayplay.io/policy
- group: agent
  title: ''
  type: MCPTerms
  url: https://www.dayplay.io/mcp-terms
- group: agent
  title: ''
  type: llms.txt
  url: https://www.dayplay.io/llms.txt
coverage:
  checked: '2026-11-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.dayplay.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dayplay provides a live local intelligence layer for major US metros, offering verified places, real-time events, and walkable itineraries. It serves both human users via an app and AI agents through a 40‑tool Model Context Protocol (MCP) server, ensuring accurate, up‑to‑date location data without hallucinations.
image: https://www.dayplay.io/og.jpg
layout: provider
modified: '2026-11-05'
name: Dayplay
nav: Providers
network: true
overview: 'Dayplay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Location Data, Real-Time, and Artificial Intelligence.


  Dayplay''s developer surface includes documentation, pricing, and 13 more developer resources.'
plans:
- name: Dayplay Io Plans Pricing
  plan_count: 3
  slug: dayplay-io-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 24.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dayplay Io Domain Security
  slug: dayplay-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dayplay-io
tags:
- Company
- Travel
- Location Data
- Real-Time
- Artificial Intelligence
website: https://www.dayplay.io/
---
