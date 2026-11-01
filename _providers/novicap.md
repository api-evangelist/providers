---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.novicap.com/v1
  baseurl_source: declared
  description: Confirming (reverse factoring) invoices and payment instructions.
  name: Novicap Confirming Standard API
  slug: novicap-confirming-standard-api
- baseURL: https://api.novicap.com/v1
  baseurl_source: declared
  description: Dynamic discounting suppliers, invoices, payment instructions and adjustments.
  name: Novicap Dynamic Discounting API
  slug: novicap-dynamic-discounting-api
artifact_total: 8
collections:
- collection_type: open
  name: Novicap Confirming Standard API
  slug: open-novicap-confirming-standard-api
- collection_type: open
  name: Novicap Confirming Standard Dynamic Discounting API
  slug: open-novicap-dynamic-discounting-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://novicap.com/feed/
- group: other
  href: https://artifacts.apis.io/novicap/overlays/novicap-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/novicap-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://novicap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.novicap.com/
- group: company
  title: ''
  type: Blog
  url: https://novicap.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.novicap.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: mailto:support@novicap.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://novicap.com/aviso-legal/
- group: auth
  href: https://artifacts.apis.io/novicap/authentication/novicap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/novicap-authentication.yml
- group: design
  href: https://artifacts.apis.io/novicap/conventions/novicap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/novicap-conventions.yml
- group: design
  href: https://artifacts.apis.io/novicap/errors/novicap-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/novicap-problem-types.yml
- group: design
  href: https://artifacts.apis.io/novicap/lifecycle/novicap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/novicap-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/novicap/data-model/novicap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/novicap-data-model.yml
- group: design
  href: https://artifacts.apis.io/novicap/conformance/novicap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/novicap-conformance.yml
- group: agent
  href: https://artifacts.apis.io/novicap/mcp/novicap-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/novicap-mcp.yml
- group: agent
  href: https://artifacts.apis.io/novicap/llms/novicap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/novicap-llms.txt
- group: agent
  href: https://artifacts.apis.io/novicap/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/novicap/well-known/novicap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/novicap-well-known.yml
- group: auth
  href: https://artifacts.apis.io/novicap/well-known/novicap-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/novicap-security.txt
- group: auth
  href: https://artifacts.apis.io/novicap/security/novicap-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/novicap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://novicap.com/.well-known/security.txt
created: '2026-07-17'
description: 'Novicap is a Spanish working-capital and supply-chain-finance fintech that helps companies optimize their circulating capital. Its REST API (base URL https://api.novicap.com/v1) lets partners programmatically register suppliers, submit and manage invoices, and create payment instructions and adjustments across two products: Dynamic Discounting and Confirming Standard (reverse factoring). The API uses Bearer API-key authentication with a required product_id scope, JSON payloads, and URI-path versioning, and is documented in a public developer reference. Novicap is backed by Partech and Techstars.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novicap.png
layout: provider
modified: '2026-10-06'
name: Novicap
nav: Providers
network: true
overview: 'Novicap publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Confirming Standard API and Dynamic Discounting API. Tagged areas include Company, Financial Services, Fintech, Working Capital, and Invoice Finance.


  Novicap''s developer surface includes engineering blog, support, authentication, and 18 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 12.9
    developer_ergonomics: 47.0
    discoverability: 66.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - spain
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 27.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/novicap/novicap-2026-08-07T185613.png
security:
- kind: authentication
  name: Novicap Authentication
  slug: novicap-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: vulnerability-disclosure
  name: Novicap Vulnerability Disclosure
  slug: novicap-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 2
skills:
- name: Submit and reconcile confirming (reverse factoring) invoices
  slug: novicap-confirming-invoices
- name: Submit dynamic-discounting invoices and create a payment instruction
  slug: novicap-submit-and-fund-invoices
slug: novicap
tags:
- Company
- Financial Services
- Fintech
- Working Capital
- Invoice Finance
- Supply Chain Finance
- Dynamic Discounting
- Confirming
- Reverse Factoring
- Spain
website: https://novicap.com/
---
