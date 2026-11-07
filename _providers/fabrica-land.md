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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 2
  name: Fabrica Land Agentic Access
  operation_count: 37
  slug: fabrica-land-agentic-access
  summary_line: 37 operations · 16 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: API for Fabrica.land providing access to land parcel data and marketplace operations.
  name: Fabrica API
  slug: fabrica-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Change-of-Ownership API from fabrica-land — 1 operation(s) for change-of-ownership.
  name: fabrica-land Change Of Ownership API
  slug: fabrica-land-change-of-ownership-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Document API from fabrica-land — 1 operation(s) for document.
  name: fabrica-land Document API
  slug: fabrica-land-document-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Media API from fabrica-land — 4 operation(s) for media.
  name: fabrica-land Media API
  slug: fabrica-land-media-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Metadata API from fabrica-land — 1 operation(s) for metadata.
  name: fabrica-land Metadata API
  slug: fabrica-land-metadata-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Off-Ramp API from fabrica-land — 3 operation(s) for off-ramp.
  name: fabrica-land Off Ramp API
  slug: fabrica-land-off-ramp-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The On-Ramp API from fabrica-land — 7 operation(s) for on-ramp.
  name: fabrica-land On Ramp API
  slug: fabrica-land-on-ramp-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Pool Lending API from fabrica-land — 2 operation(s) for pool lending.
  name: fabrica-land Pool Lending API
  slug: fabrica-land-pool-lending-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Proof-of-Ownership API from fabrica-land — 2 operation(s) for proof-of-ownership.
  name: fabrica-land Proof Of Ownership API
  slug: fabrica-land-proof-of-ownership-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Regrid API from fabrica-land — 1 operation(s) for regrid.
  name: fabrica-land Regrid API
  slug: fabrica-land-regrid-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Syndication API from fabrica-land — 1 operation(s) for syndication.
  name: fabrica-land Syndication API
  slug: fabrica-land-syndication-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Terrain Project API from fabrica-land — 2 operation(s) for terrain project.
  name: fabrica-land Terrain Project API
  slug: fabrica-land-terrain-project-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Token API from fabrica-land — 3 operation(s) for token.
  name: fabrica-land Token API
  slug: fabrica-land-token-api
- baseURL: https://api.fabrica.land
  baseurl_source: declared
  description: The Valuation API from fabrica-land — 2 operation(s) for valuation.
  name: fabrica-land Valuation API
  slug: fabrica-land-valuation-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/fabrica-land/agentic-access/fabrica-land-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fabrica-land-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fabrica-land/rules/fabrica-land-rules.yml
  title: ''
  type: Spectral
  url: rules/fabrica-land-rules.yml
- group: design
  href: https://artifacts.apis.io/fabrica-land/json-ld/fabrica-land-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fabrica-land-context.jsonld
- group: design
  href: https://artifacts.apis.io/fabrica-land/vocabulary/fabrica-land-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fabrica-land-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/fabrica-land/data-model/fabrica-land-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fabrica-land-data-model.yml
- group: operate
  href: https://artifacts.apis.io/fabrica-land/changelog/fabrica-land-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fabrica-land-changelog.yml
- group: auth
  href: https://artifacts.apis.io/fabrica-land/authentication/fabrica-land-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fabrica-land-authentication.yml
- group: design
  href: https://artifacts.apis.io/fabrica-land/errors/fabrica-land-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fabrica-land-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fabrica-land/conformance/fabrica-land-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fabrica-land-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fabrica-land/llms/fabrica-land-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fabrica-land-llms.txt
- group: auth
  href: https://artifacts.apis.io/fabrica-land/well-known/fabrica-land-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fabrica-land-help-security.txt
- group: agent
  href: https://artifacts.apis.io/fabrica-land/well-known/fabrica-land-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fabrica-land-well-known.yml
- group: other
  href: https://artifacts.apis.io/fabrica-land/hosts/fabrica-land-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fabrica-land-hosts.yml
- group: other
  href: https://artifacts.apis.io/fabrica-land/vendors/fabrica-land-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fabrica-land-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fabrica.land/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.fabrica.land
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fabrica.land/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fabrica-land
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fabrica.land/changelog
- group: company
  title: ''
  type: Blog
  url: https://blog.fabrica.land
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fabrica.land/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fabrica.land/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fabrica.land/
- group: auth
  href: https://artifacts.apis.io/fabrica-land/security/fabrica-land-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fabrica-land-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fabrica.land/
created: '2026-10-30'
description: Fabrica.land is a digital marketplace that enables users to buy, sell, and borrow against real-world land parcels tokenized on the blockchain. Leveraging NFTs and decentralized finance, the platform lists properties across the United States, providing detailed parcel data, location maps, and pricing. It aims to democratize access to land ownership and collateralization, bridging traditional real estate with crypto technology for a broader audience.
image: https://fabrica.land/og/home?v=iuqekf
jsonld:
- class_count: 25
  name: Fabrica Land Context
  property_count: 92
  slug: fabrica-land-context
layout: provider
modified: '2026-10-30'
name: fabrica-land
nav: Providers
network: true
overview: 'fabrica-land publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Change Of Ownership API, Document API, Media API, and 11 more. Tagged areas include Company, Real Estate, Blockchain, Marketplace, and Fintech.


  The fabrica-land catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  fabrica-land''s developer surface includes changelog, authentication, support, engineering blog, API reference, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: fabrica-land API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 3
  slug: fabrica-land-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 57.1
    developer_ergonomics: 29.8
    discoverability: 73.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 41.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fabrica-land/fabrica-land-2026-11-03T131801.png
security:
- kind: authentication
  name: Fabrica Land Authentication
  slug: fabrica-land-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fabrica Land Domain Security
  slug: fabrica-land-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fabrica-land
tags:
- Company
- Real Estate
- Blockchain
- Marketplace
- Fintech
website: https://fabrica.land/
---
