---
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 3
  name: Dsrv Agentic Access
  operation_count: 11
  slug: dsrv-agentic-access
  summary_line: 11 operations · 3 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: API reference page (not found)
  name: Dsrv API
  slug: dsrv-api
- baseURL: https://api.dev.dsrv.com/api/v1/staking
  baseurl_source: spec
  description: Ethereum staking endpoints
  name: Dsrv Ethereum API
  slug: dsrv-ethereum-api
- baseURL: https://api.dev.dsrv.com/api/v1/staking
  baseurl_source: spec
  description: Health check endpoints
  name: Dsrv Health API
  slug: dsrv-health-api
artifact_total: 8
common:
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dsrv.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dsrv.com/
- group: agent
  href: https://artifacts.apis.io/dsrv/agentic-access/dsrv-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dsrv-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dsrv/rules/dsrv-rules.yml
  title: ''
  type: Spectral
  url: rules/dsrv-rules.yml
- group: design
  href: https://artifacts.apis.io/dsrv/json-ld/dsrv-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dsrv-context.jsonld
- group: design
  href: https://artifacts.apis.io/dsrv/vocabulary/dsrv-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dsrv-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dsrv/data-model/dsrv-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dsrv-data-model.yml
- group: design
  href: https://artifacts.apis.io/dsrv/errors/dsrv-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dsrv-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dsrv/conformance/dsrv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dsrv-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dsrv/llms/dsrv-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dsrv-llms.txt
- group: agent
  href: https://artifacts.apis.io/dsrv/well-known/dsrv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dsrv-well-known.yml
- group: other
  href: https://artifacts.apis.io/dsrv/hosts/dsrv-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dsrv-hosts.yml
- group: other
  href: https://artifacts.apis.io/dsrv/vendors/dsrv-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dsrv-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.dsrv.com/en/story/news
- group: auth
  href: https://artifacts.apis.io/dsrv/authentication/dsrv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dsrv-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dsrv/security/dsrv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dsrv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dsrv.com/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.dsrv.com/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/dsrv
- group: operate
  title: ''
  type: Support
  url: https://www.dsrv.com/en/contact
created: '2026-10-24'
description: Dsrv is a blockchain infrastructure company based in Seoul, South Korea, founded in 2019. It provides staking, custody, RPC nodes, and Web3 solutions across more than 170 protocols, serving institutional and enterprise clients worldwide. The company focuses on inclusivity, reliability, and scalability, positioning itself as a next‑generation digital finance platform.
image: https://www.dsrv.com/og-images/default.png
jsonld:
- class_count: 50
  name: Dsrv Context
  property_count: 96
  slug: dsrv-context
layout: provider
modified: '2026-10-24'
name: Dsrv
nav: Providers
network: true
overview: 'Dsrv publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ethereum API, Health API, and 1 more. Tagged areas include Company, Blockchain, Infrastructure, Staking, and Web3.


  The Dsrv catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dsrv''s developer surface includes API reference, documentation, authentication, engineering blog, support, and 15 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Dsrv API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: dsrv-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 52.2
    developer_ergonomics: 45.2
    discoverability: 58.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dsrv Authentication
  slug: dsrv-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dsrv Domain Security
  slug: dsrv-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dsrv
tags:
- Company
- Blockchain
- Infrastructure
- Staking
- Web3
website: https://www.dsrv.com/en
---
