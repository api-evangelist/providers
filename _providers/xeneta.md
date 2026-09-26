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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Airline reports API (Selfie) serving rates, chargeable weight, load factor, and capacity reports as CSV files in ZIP archives. Airlines use a branded host (https://{airline}.useselfie.com/api/selfie/v
  name: Xeneta Airline Data API
  slug: xeneta-airline-data-api
- baseURL: https://api.xeneta.com/v3.0
  baseurl_source: declared
  description: The Air API from Xeneta — 1 operation(s) for air.
  name: Xeneta Air API
  slug: xeneta-air-api
- baseURL: https://api.xeneta.com/v3.0
  baseurl_source: declared
  description: The Ocean API from Xeneta — 13 operation(s) for ocean.
  name: Xeneta Ocean API
  slug: xeneta-ocean-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: xeneta-api-30 Air API
  slug: open-xeneta-air-api
- collection_type: open
  name: xeneta-api-30 Air Ocean API
  slug: open-xeneta-ocean-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/capabilities/xeneta-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/xeneta-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/overlays/xeneta-api-30-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xeneta-api-30-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/security/xeneta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xeneta-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/authentication/xeneta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xeneta-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.xeneta.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.xeneta.com/reference
- group: docs
  title: ''
  type: Documentation
  url: https://help.xeneta.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://help.xeneta.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.xeneta.com/reference/api
- group: operate
  title: ''
  type: Support
  url: https://help.xeneta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.xeneta.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xeneta
- group: start
  title: ''
  type: Login
  url: https://app.xeneta.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xeneta.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xeneta.com/xeneta-privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.xeneta.com/xeneta-data-security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/security/xeneta-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/xeneta-trust-center.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/packages/xeneta-packages.yml
  title: ''
  type: Packages
  url: packages/xeneta-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/well-known/xeneta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xeneta-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/mcp/xeneta-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/xeneta-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/llms/xeneta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xeneta-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/conformance/xeneta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xeneta-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/errors/xeneta-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xeneta-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/lifecycle/xeneta-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xeneta-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://help.xeneta.com/reference/versioning
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/conventions/xeneta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xeneta-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/changelog/xeneta-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/xeneta-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/data-model/xeneta-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xeneta-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Xeneta is an ocean and air freight rate benchmarking and market analytics platform headquartered in Oslo, Norway. It crowdsources contracted freight rates from shippers and forwarders into the world's largest rate database, and its REST API (v3.0) exposes ocean and air market rates, your own contracted prices, carrier spread, estimated rates, capacity, carbon emissions, and schedule reliability data, plus a separate airline reports API for airlines, shippers, and freight forwarders.
image: https://files.readme.io/f8b1664-xeneta-favicon.ico
layout: provider
modified: '2026-07-21'
name: Xeneta
nav: Providers
network: true
overview: 'Xeneta publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Air API, Ocean API, and 1 more. Tagged areas include Freight, Shipping, Logistics, Ocean Freight, and Air Freight.


  Xeneta''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, changelog, and 22 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 22.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 44.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 27.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/xeneta/refs/heads/main/screenshots/xeneta-2026-08-17T083005.png
security:
- kind: authentication
  name: Xeneta Authentication
  slug: xeneta-authentication
  summary_line: apiKey/sessionCookie · 2 schemes
- kind: domain-security
  name: Xeneta Domain Security
  slug: xeneta-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Xeneta Trust Center
  slug: xeneta-trust-center
  summary_line: ISO 27001:2022
slug: xeneta
tags:
- Freight
- Shipping
- Logistics
- Ocean Freight
- Air Freight
- Benchmarking
- Market Data
- Supply Chain
- Rates
- Emissions
website: https://www.xeneta.com/
---
