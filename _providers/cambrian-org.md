---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_server: documented
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
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cambrian's API provides real-time and historical blockchain data for DeFi agents.
  name: Cambrian API
  slug: cambrian-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/cambrian-org/plans/cambrian-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cambrian-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cambrian-org/json-ld/cambrian-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cambrian-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/cambrian-org/vocabulary/cambrian-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cambrian-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cambrian-org/data-model/cambrian-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cambrian-org-data-model.yml
- group: build
  href: https://artifacts.apis.io/cambrian-org/cli/cambrian-org-cli.yml
  title: ''
  type: CLI
  url: cli/cambrian-org-cli.yml
- group: design
  href: https://artifacts.apis.io/cambrian-org/conventions/cambrian-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cambrian-org-conventions.yml
- group: auth
  href: https://artifacts.apis.io/cambrian-org/authentication/cambrian-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cambrian-org-authentication.yml
- group: design
  href: https://artifacts.apis.io/cambrian-org/conformance/cambrian-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cambrian-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cambrian-org/llms/cambrian-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cambrian-org-llms.txt
- group: agent
  href: https://artifacts.apis.io/cambrian-org/well-known/cambrian-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cambrian-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/cambrian-org/hosts/cambrian-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cambrian-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/cambrian-org/vendors/cambrian-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cambrian-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cambrian.org/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cambrian.org/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.cambrian.org/team
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cambrian.org
- group: auth
  href: https://artifacts.apis.io/cambrian-org/security/cambrian-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cambrian-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cambrian.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cambrian.org/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cambrian.org/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.cambrian.org/blog
created: '2026-11-04'
description: Cambrian Network provides financial intelligence for the age of digital assets, offering fast, comprehensive, and verifiable on‑chain data for agents, institutions, and protocols. It aims to deliver evolving market insights through a robust data layer, supporting analytics, compliance, and strategic decision‑making across the digital asset ecosystem.
image: https://www.cambrian.org/redesign/metadata-image.jpg
jsonld:
- class_count: 2
  name: Cambrian Org Context
  property_count: 6
  slug: cambrian-org-context
layout: provider
modified: '2026-11-04'
name: Cambrian Network
nav: Providers
network: true
overview: 'Cambrian Network is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Digital Assets, On-Chain Data, Market Intelligence, and Cryptocurrency.


  The Cambrian Network catalog on APIs.io includes 1 JSON-LD context.


  Cambrian Network''s developer surface includes CLI, authentication, API reference, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Cambrian Org Plans Pricing
  plan_count: 1
  slug: cambrian-org-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.3
    catalog_earned_first_party: 8.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 8.3
    contract_quality: 6.7
    developer_ergonomics: 28.6
    discoverability: 67.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cambrian Org Authentication
  slug: cambrian-org-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cambrian Org Domain Security
  slug: cambrian-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cambrian-org
tags:
- Finance
- Digital Assets
- On-Chain Data
- Market Intelligence
- Cryptocurrency
website: https://www.cambrian.org/
---
