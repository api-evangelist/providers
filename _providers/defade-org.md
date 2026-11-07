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
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: DeFade provides a multi‑chain memecoin rug‑pull detection and scanning service. It scans tokens across Solana, Ethereum, Base, BSC, Robinhood, Arc, Hyperliquid & Monad, offering free daily scans and p
  name: DeFade API
  slug: defade-api
- description: 'DeFade API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DeFade API
  slug: defade-org-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/defade-org/plans/defade-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/defade-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/defade-org/rules/defade-org-rules.yml
  title: ''
  type: Spectral
  url: rules/defade-org-rules.yml
- group: design
  href: https://artifacts.apis.io/defade-org/json-ld/defade-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/defade-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/defade-org/vocabulary/defade-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/defade-org-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/defade-org/data-model/defade-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/defade-org-data-model.yml
- group: design
  href: https://artifacts.apis.io/defade-org/conformance/defade-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/defade-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/defade-org/llms/defade-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/defade-org-llms.txt
- group: other
  href: https://artifacts.apis.io/defade-org/hosts/defade-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/defade-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/defade-org/vendors/defade-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/defade-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://defade.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://defade.org/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://defade.org/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DeFadeLtd
- group: docs
  title: ''
  type: Documentation
  url: https://api.defade.org/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://defade.org/developers
- group: company
  title: ''
  type: Blog
  url: https://defade.org/blog
- group: auth
  href: https://artifacts.apis.io/defade-org/security/defade-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/defade-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://defade.org/
created: '2026-11-05'
description: DeFade provides a multi‑chain memecoin rug‑pull detection and scanning service. It scans tokens across Solana, Ethereum, Base, BSC, Robinhood, Arc, Hyperliquid & Monad, offering free daily scans and paid Pro plans from $24/mo. The platform highlights rug pulls, whale wallets, snipers, insider networks, and offers tools for developers to integrate detection via its API.
image: https://defade.org/og-image.jpg?v=10
json_schemas:
- name: PostApiStripeBuyCreditsRequest
  property_count: 2
  slug: defade-org-post-api-stripe-buy-credits-request
- name: PostApiStripeBuyCreditsResponse
  property_count: 1
  slug: defade-org-post-api-stripe-buy-credits-response
- name: PostMcpRequest
  property_count: 3
  slug: defade-org-post-mcp-request
jsonld:
- class_count: 3
  name: Defade Org Context
  property_count: 6
  slug: defade-org-context
layout: provider
modified: '2026-11-05'
name: DeFade
nav: Providers
network: true
overview: 'DeFade is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Security, Analytics, and Multi-Chain.


  The DeFade catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DeFade''s developer surface includes pricing, documentation, engineering blog, and 15 more developer resources.'
plans:
- name: Defade Org Plans Pricing
  plan_count: 3
  slug: defade-org-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: DeFade API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: defade-org-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 35.6
    contract_quality: 20.1
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Defade Org Domain Security
  slug: defade-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: defade-org
tags:
- Company
- Cryptocurrency
- Security
- Analytics
- Multi-Chain
- DeFi
website: https://defade.org/
---
