---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Foreign Agricultural Service Agentic Access
  operation_count: 35
  slug: foreign-agricultural-service-agentic-access
  summary_line: 35 operations
api_count: 2
apis:
- baseURL: https://apps.fas.usda.gov/OpenData
  baseurl_source: declared
  description: The USDA Foreign Agricultural Service Open Data API provides programmatic access to U.S. agricultural trade data, including the Global Agricultural Trade System (GATS), Export Sales Reporting (ESR), a
  name: USDA FAS Open Data API
  slug: fas-open-data
- baseURL: https://apps.fas.usda.gov/OpenData
  baseurl_source: declared
  description: U.S. Weekly Export Sales of Agricultural Commodity Data
  name: Foreign Agricultural Service ESR API
  slug: foreign-agricultural-service-esr-api
- baseURL: https://apps.fas.usda.gov/OpenData
  baseurl_source: declared
  description: Global Agricultural Trade System
  name: Foreign Agricultural Service GATS API
  slug: foreign-agricultural-service-gats-api
- baseURL: https://apps.fas.usda.gov/OpenData
  baseurl_source: declared
  description: Production, Supply and Distribution
  name: Foreign Agricultural Service PSD API
  slug: foreign-agricultural-service-psd-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USDA FAS Open Data Services ESR API
  slug: open-foreign-agricultural-service-esr-api
- collection_type: open
  name: USDA FAS Open Data Services ESR GATS API
  slug: open-foreign-agricultural-service-gats-api
- collection_type: open
  name: USDA FAS Open Data Services ESR PSD API
  slug: open-foreign-agricultural-service-psd-api
- collection_type: open
  name: USDA FAS Open Data Services
  slug: open-foreign-agricultural-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/foreign-agricultural-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foreign-agricultural-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/foreign-agricultural-service-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-foreign-agricultural-service
- group: company
  title: ''
  type: Website
  url: https://www.fas.usda.gov/
- group: build
  title: ''
  type: Packages
  url: packages/foreign-agricultural-service-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/foreign-agricultural-service-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/foreign-agricultural-service-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/foreign-agricultural-service-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/foreign-agricultural-service-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/foreign-agricultural-service-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/foreign-agricultural-service-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/foreign-agricultural-service-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/foreign-agricultural-service-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/foreign-agricultural-service-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/foreign-agricultural-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.usda.gov/vulnerability-disclosure-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apps.fas.usda.gov/opendataweb/home
- group: docs
  title: ''
  type: APIReference
  url: https://apps.fas.usda.gov/opendata/swagger/ui/index
- group: start
  title: ''
  type: SignUp
  url: https://apps.fas.usda.gov/opendatawebv2/#/signup
- group: operate
  title: ''
  type: Support
  url: https://apps.fas.usda.gov/opendatawebv2/#/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usda.gov/privacy-policy
created: '2024-12-25'
description: 'The Foreign Agricultural Service (FAS) is the trade and export agency of the United States Department of Agriculture (USDA), working to promote U.S. agricultural exports and expand global markets for American agricultural products. FAS runs the Open Data Services at apps.fas.usda.gov, a free, key-gated HTTPS/JSON API publishing three datasets on U.S. and world agricultural trade: ESR (Export Sales Reporting — weekly U.S. export sales by commodity, destination and market year), GATS (the Global Agricultural Trade System — U.S. Census and UN ComTrade import, export and re-export flows, including trade by U.S. customs district), and PSD (Production, Supply and Distribution — world commodity production, supply and use forecasts). The surface is 35 read-only GET operations behind a single API_KEY header, described by a live Swagger 2.0 contract and rendered in Swagger UI.'
finops:
- name: Foreign Agricultural Service Finops
  service_category: API
  slug: foreign-agricultural-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foreign-agricultural-service.png
layout: provider
modified: '2026-09-10'
name: Foreign Agricultural Service
nav: Providers
network: true
overview: 'Foreign Agricultural Service publishes 4 APIs on the [APIs.io](https://apis.io/) network, including USDA FAS Open Data API, ESR API, GATS API, and 1 more. Tagged areas include Agriculture, Federal-Government, Trade, Open-Data, and Commodities.


  Foreign Agricultural Service''s developer surface includes authentication, API reference, signup flow, support, and 19 more developer resources.'
plans:
- name: Foreign Agricultural Service Plans Pricing
  plan_count: 1
  slug: foreign-agricultural-service-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Foreign Agricultural Service Rate Limits
  slug: foreign-agricultural-service-rate-limits
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.9
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 13.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/foreign-agricultural-service/refs/heads/main/screenshots/foreign-agricultural-service-2026-06-20T181418.png
security:
- kind: authentication
  name: Foreign Agricultural Service Authentication
  slug: foreign-agricultural-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Foreign Agricultural Service Domain Security
  slug: foreign-agricultural-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Foreign Agricultural Service Vulnerability Disclosure
  slug: foreign-agricultural-service-vulnerability-disclosure
  summary_line: Bugcrowd
slug: foreign-agricultural-service
tags:
- Agriculture
- Federal-Government
- Trade
- Open-Data
- Commodities
- Exports
- Government
website: https://www.fas.usda.gov/
---
