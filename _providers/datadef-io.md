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
  band: agent-ready
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Datadef provides an API documented at their developer portal, but no machine‑readable contract was found.
  name: Datadef API
  slug: datadef-api
- description: 'Datadef API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Datadef API
  slug: datadef-io-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/datadef-io/plans/datadef-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datadef-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datadef-io/rules/datadef-io-rules.yml
  title: ''
  type: Spectral
  url: rules/datadef-io-rules.yml
- group: design
  href: https://artifacts.apis.io/datadef-io/vocabulary/datadef-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datadef-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datadef-io/conformance/datadef-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datadef-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datadef-io/llms/datadef-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datadef-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/datadef-io/well-known/datadef-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datadef-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/datadef-io/hosts/datadef-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datadef-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/datadef-io/vendors/datadef-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datadef-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datadef.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datadef.io/privacy
- group: start
  title: ''
  type: Login
  url: https://datadef.io/auth/signin
- group: auth
  href: https://artifacts.apis.io/datadef-io/security/datadef-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datadef-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datadef.io/
- group: docs
  title: ''
  type: Documentation
  url: https://datadef.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://datadef.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://blog.datadef.io
- group: commercial
  title: ''
  type: Pricing
  url: https://datadef.io/pricing
coverage:
  checked: '2026-11-05'
  detail: Documentation pages are public but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found despite probing all known locations.
  evidence:
  - status: 200
    url: https://datadef.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Datadef provides AI‑powered diagram generation for architecture, ERD, and cloud infrastructure. It offers free tools and extensive icon libraries for AWS, GCP, and Azure, along with guides on data platforms, data mesh, medallion architecture, and best practices for data quality, lineage, and contracts. The service aims to help data engineers quickly document and visualize their data stacks.
image: https://datadef.io/datadef_logo_with_name_rectangle.png
layout: provider
modified: '2026-11-04'
name: Datadef
nav: Providers
network: true
overview: 'Datadef is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Engineering, AI Tools, Diagramming, Cloud Architecture, and Open Source.


  The Datadef catalog on APIs.io includes 1 Spectral governance ruleset.


  Datadef''s developer surface includes documentation, getting-started guide, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Datadef Io Plans Pricing
  plan_count: 3
  slug: datadef-io-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: Datadef API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: datadef-io-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 10.5
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datadef Io Domain Security
  slug: datadef-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: datadef-io
tags:
- Data Engineering
- AI Tools
- Diagramming
- Cloud Architecture
- Open Source
website: https://datadef.io/
---
