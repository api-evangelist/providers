---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rugspull Read Api Agentic Access
  operation_count: 9
  slug: rugspull-read-api-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- baseURL: https://rugspull.com
  baseurl_source: spec
  description: Read-only indexer checkpoints and warnings.
  name: Rugspull Read API Indexer API
  slug: rugspull-read-api-indexer-api
- baseURL: https://rugspull.com
  baseurl_source: spec
  description: Event-derived market points and sparklines; not a price oracle.
  name: Rugspull Read API Market API
  slug: rugspull-read-api-market-api
- baseURL: https://rugspull.com
  baseurl_source: spec
  description: Public immutable metadata and image objects.
  name: Rugspull Read API Objects API
  slug: rugspull-read-api-objects-api
- baseURL: https://rugspull.com
  baseurl_source: spec
  description: Current-Factory discovery cache and indexed event records.
  name: Rugspull Read API Rugs API
  slug: rugspull-read-api-rugs-api
- baseURL: https://rugspull.com
  baseurl_source: spec
  description: Liveness and public configuration.
  name: Rugspull Read API Service API
  slug: rugspull-read-api-service-api
artifact_total: 15
collections:
- collection_type: open
  name: Rugspull Read API
  slug: open-rugspull-read-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://rugspull.com/feed.xml
- group: company
  title: ''
  type: Website
  url: https://rugspull.com
- group: agent
  href: https://artifacts.apis.io/rugspull-read-api/agentic-access/rugspull-read-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rugspull-read-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/rugspull-read-api/security/rugspull-read-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rugspull-read-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rugspull-read-api/security/rugspull-read-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rugspull-read-api-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pqchase/rugspull/blob/main/docs/INTEGRATION.md
- group: docs
  title: ''
  type: APIReference
  url: https://rugspull.com/api-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/pqchase/rugspull/blob/main/docs/INTEGRATION.md
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/pqchase/rugspull/blob/main/docs/INTEGRATION.md#read-the-public-cache
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pqchase/rugspull
- group: operate
  title: ''
  type: Support
  url: https://github.com/pqchase/rugspull/issues
- group: build
  href: https://artifacts.apis.io/rugspull-read-api/collections/rugspull-read-api.postman_collection.json
  title: ''
  type: Postman
  url: collections/rugspull-read-api.postman_collection.json
- group: agent
  href: https://artifacts.apis.io/rugspull-read-api/llms/rugspull-read-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rugspull-read-api-llms.txt
- group: agent
  href: https://artifacts.apis.io/rugspull-read-api/well-known/rugspull-read-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rugspull-read-api-well-known.yml
- group: other
  href: https://artifacts.apis.io/rugspull-read-api/well-known/rugspull-read-api-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/rugspull-read-api-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/rugspull-read-api/well-known/rugspull-read-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rugspull-read-api-security.txt
- group: auth
  href: https://artifacts.apis.io/rugspull-read-api/security/rugspull-read-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/rugspull-read-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/rugspull-read-api/authentication/rugspull-read-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rugspull-read-api-authentication.yml
- group: design
  href: https://artifacts.apis.io/rugspull-read-api/conventions/rugspull-read-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rugspull-read-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/rugspull-read-api/conventions/rugspull-read-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/rugspull-read-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/rugspull-read-api/errors/rugspull-read-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rugspull-read-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rugspull-read-api/lifecycle/rugspull-read-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rugspull-read-api-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/rugspull-read-api/changelog/rugspull-read-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rugspull-read-api-changelog.yml
- group: design
  href: https://artifacts.apis.io/rugspull-read-api/conformance/rugspull-read-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rugspull-read-api-conformance.yml
- group: build
  href: https://artifacts.apis.io/rugspull-read-api/packages/rugspull-read-api-packages.yml
  title: ''
  type: Packages
  url: packages/rugspull-read-api-packages.yml
- group: operate
  href: https://artifacts.apis.io/rugspull-read-api/rate-limits/rugspull-read-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rugspull-read-api-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rugspull-read-api/plans/rugspull-read-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rugspull-read-api-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rugspull-read-api/data-model/rugspull-read-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rugspull-read-api-data-model.yml
- group: build
  href: https://artifacts.apis.io/rugspull-read-api/examples/rugspull-read-api-examples.yml
  title: ''
  type: Examples
  url: examples/rugspull-read-api-examples.yml
- group: other
  href: https://artifacts.apis.io/rugspull-read-api/overlays/rugspull-read-api-read-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rugspull-read-api-read-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/rugspull-read-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-19'
description: A read-only, GET-only discovery-cache REST API for Rugspull, a self-described high-risk parody DeFi protocol on BNB Smart Chain (chain id 56). Exposes rebuildable discovery/indexed-event data with no write, settlement, or transaction-proxy operations; on-chain BSC contracts remain the source of financial truth. Unauthenticated, free, best-effort, with no published rate limits or SLA.
image: https://rugspull.com/assets/og-mechanism.png
layout: provider
modified: '2026-10-06'
name: Rugspull Read API
nav: Providers
network: true
overview: 'Rugspull Read API publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Indexer API, Market API, Objects API, and 2 more. Tagged areas include BNB Smart Chain, BSC, wbnb, Read Only, and OpenAPI.


  Rugspull Read API''s developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, code examples, and 24 more developer resources.'
plans:
- name: Rugspull Read Api Plans Pricing
  plan_count: 0
  slug: rugspull-read-api-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Rugspull Read Api Rate Limits
  slug: rugspull-read-api-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 45.8
    developer_ergonomics: 61.3
    discoverability: 57.1
    operational_transparency: 31.6
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rugspull-read-api/rugspull-read-api-2026-09-02T154200.png
security:
- kind: authentication
  name: Rugspull Read Api Authentication
  slug: rugspull-read-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rugspull Read Api Domain Security
  slug: rugspull-read-api-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Rugspull Read Api Vulnerability Disclosure
  slug: rugspull-read-api-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Discover and inspect a Rug
  slug: rugspull-read-api-discover-and-inspect-a-rug
- name: Reconstruct market data correctly
  slug: rugspull-read-api-reconstruct-market-data
- name: Verify before you integrate or list
  slug: rugspull-read-api-verify-before-you-integrate
slug: rugspull-read-api
tags:
- BNB Smart Chain
- BSC
- wbnb
- Read Only
- OpenAPI
- high-risk
- discovery-cache
- DeFi
- Web3
- crypto-market-data
- Indexer
website: https://rugspull.com
---
