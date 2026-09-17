---
access_model:
  confidence: medium
  label: Request access — API key issued via a HubSpot form; no published API pricing
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://equipmentwatch.com/api/
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'Raw equipment sales activity (auction and resale transactions) and market-derived utilization and popularity benchmarks for the heavy equipment industry. Documented on the EquipmentWatch site but NOT '
  name: EquipmentWatch Market Data API
  slug: market-data
- description: Read and write access to user-saved asset and group data inside the EquipmentWatch application, allowing saved models and groups to be moved into and out of third-party platforms. The only EquipmentWa
  name: EquipmentWatch Integration API
  slug: integration
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: The Bulk API from Equipmentwatch — 2 operation(s) for bulk.
  name: Equipmentwatch Bulk API
  slug: equipmentwatch-bulk-api
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: The Cost API from Equipmentwatch — 3 operation(s) for cost.
  name: Equipmentwatch Cost API
  slug: equipmentwatch-cost-api
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: The Rental API from Equipmentwatch — 4 operation(s) for rental.
  name: Equipmentwatch Rental API
  slug: equipmentwatch-rental-api
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: The Specifications API from Equipmentwatch — 2 operation(s) for specifications.
  name: Equipmentwatch Specifications API
  slug: equipmentwatch-specifications-api
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: The Taxonomy API from Equipmentwatch — 6 operation(s) for taxonomy.
  name: Equipmentwatch Taxonomy API
  slug: equipmentwatch-taxonomy-api
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: The Values API from Equipmentwatch — 6 operation(s) for values.
  name: Equipmentwatch Values API
  slug: equipmentwatch-values-api
- baseURL: https://equipmentwatchapi.com/v1
  baseurl_source: declared
  description: The Verification API from Equipmentwatch — 1 operation(s) for verification.
  name: Equipmentwatch Verification API
  slug: equipmentwatch-verification-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.equipmentwatch.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/equipmentwatch
- group: start
  title: ''
  type: DeveloperPortal
  url: https://equipmentwatch.com/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.equipmentwatchapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.equipmentwatchapi.com/
- group: company
  title: ''
  type: Blog
  url: https://equipmentwatch.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://equipmentwatch.com/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://share.hsforms.com/12W-aoSkmR5eYntgAyyiPsAqjl7f
- group: start
  title: ''
  type: Login
  url: https://app.equipmentwatch.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://equipmentwatch.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://equipmentwatch.com/legal/website-terms-and-privacy-notice/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/authentication/equipmentwatch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/equipmentwatch-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/conventions/equipmentwatch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/equipmentwatch-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/conformance/equipmentwatch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/equipmentwatch-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/errors/equipmentwatch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/equipmentwatch-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/lifecycle/equipmentwatch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/equipmentwatch-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/data-model/equipmentwatch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/equipmentwatch-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/sandbox/equipmentwatch-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/equipmentwatch-sandbox.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/overlays/equipmentwatch-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/equipmentwatch-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/mcp/equipmentwatch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/equipmentwatch-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/llms/equipmentwatch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/equipmentwatch-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/plans/equipmentwatch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/equipmentwatch-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/rate-limits/equipmentwatch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/equipmentwatch-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/security/equipmentwatch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/equipmentwatch-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/finops/equipmentwatch-finops.yml
  title: ''
  type: FinOps
  url: finops/equipmentwatch-finops.yml
created: '2026-03-16'
description: EquipmentWatch (a Fusable brand, operated by Randall-Reilly, LLC) provides construction and equipment data APIs that deliver rental rates, ownership and operating costs, market values, machine specifications, serial-number verification and raw market transaction data for heavy equipment. Their data is used by contractors, equipment dealers, rental houses, lenders and insurance professionals to make informed decisions about equipment valuation, procurement, cost recovery and rental rate setting. The EquipmentWatch API is published as a single OpenAPI 3.0.3 contract at docs.equipmentwatchapi.com covering the Taxonomy, Values, Specifications, Rental, Verification, Cost and Bulk surfaces, served from equipmentwatchapi.com with a documented sandbox host, and authenticated with an x-api-key header issued through a request-an-API-key form.
finops:
- name: Equipmentwatch Finops
  service_category: API
  slug: equipmentwatch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/equipmentwatch.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface derived from the EquipmentWatch OpenAPI. Every tool below binds 1:1 to a real published GET operation. No endpoint is asserted, because none exists.
  name: Equipmentwatch MCP Server
  slug: equipmentwatch-mcp-server
modified: '2026-09-06'
name: Equipmentwatch
nav: Providers
network: true
overview: 'Equipmentwatch publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Cost API, Rental API, and 4 more. Tagged areas include Construction, Equipment, Rental Rates, Valuation, and Heavy Equipment.


  Equipmentwatch''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, sandbox, and 19 more developer resources.'
plans:
- name: Equipmentwatch Plans Pricing
  plan_count: 0
  slug: equipmentwatch-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Equipmentwatch Rate Limits
  slug: equipmentwatch-rate-limits
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 49.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 41.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/equipmentwatch/refs/heads/main/screenshots/equipmentwatch-2026-06-20T180808.png
security:
- kind: authentication
  name: Equipmentwatch Authentication
  slug: equipmentwatch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Equipmentwatch Domain Security
  slug: equipmentwatch-domain-security
  summary_line: TLSv1.3 · DMARC
slug: equipmentwatch
tags:
- Construction
- Equipment
- Rental Rates
- Valuation
- Heavy Equipment
- Equipment Data
- Market Data
website: https://www.equipmentwatch.com/
---
