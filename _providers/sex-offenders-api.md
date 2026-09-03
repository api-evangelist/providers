---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sex Offenders Api Agentic Access
  operation_count: 2
  slug: sex-offenders-api-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Sex Offenders API Definition. The Sex Offenders API lets you request registered sex offenders across the US by name or zip code (Disclaimer).
  name: Sex Offenders API
  slug: sex-offenders-api
- baseURL: https://api.crimeometer.com/v5
  baseurl_source: declared
  description: The CrimeoMeter Sex Offenders API — 2 published operations (record search and radius search) over US state sex offender registry data, transcribed from CrimeoMeter's public Postman collection.
  name: Sex Offenders API Sex Offenders API
  slug: sex-offenders-api-sex-offenders-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crimeometer Sex Offenders API
  slug: open-sex-offenders-api-sex-offenders-api
- collection_type: open
  name: Crimeometer Sex Offenders API
  slug: open-sex-offenders-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.crimeometer.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sex-offenders-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sex-offenders-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sex-offenders-api-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/sex-offenders-api-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sex-offenders-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sex-offenders-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sex-offenders-api-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sex-offenders-api-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sex-offenders-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sex-offenders-api-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sex-offenders-api-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sex-offenders-api-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sex-offenders-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sex-offenders-api-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/12755833/TzK2auPn
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.crimeometer.com/products
- group: docs
  title: ''
  type: Documentation
  url: https://www.crimeometer.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/12755833/TzK2auPn
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crimeometer.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.crimeometer.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.crimeometer.com/blog-feed.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crimeometer.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crimeometer.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.crimeometer.com/#contactus
- group: start
  title: ''
  type: SignUp
  url: https://www.crimeometer.com/#contactus
created: '2024-11-13'
description: The Sex Offenders API from CrimeoMeter (CityCop Corporation dba CrimeoMeter, San Francisco) returns registered sex offender records from US state registries, searchable by zip code, first/last name, alias, birthdate, a last-updated window, or a latitude/longitude radius. Records carry identity, physical description, charges, registry status (predator, absconder) and geocoded address, plus created/last-updated/last-synced timestamps that expose how fresh each record is against its source registry. Access is a private x-api-key issued by hand through the Contact Us form; there is no self-service signup. CrimeoMeter publishes no OpenAPI, but does publish a public Postman collection covering v5 of this API.
finops:
- name: Sex Offenders Api Finops
  service_category: API
  slug: sex-offenders-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sex-offenders-api.png
layout: provider
mcp_servers:
- description: 'CrimeoMeter serves a live, anonymous, remote MCP endpoint from its own domain. IMPORTANT SCOPE NOTE: this is the Wix Site MCP that the Wix platform provisions for every site it hosts (crimeometer.com '
  name: CrimeoMeter Site MCP
  slug: crimeometer-site-mcp
modified: '2026-08-28'
name: Sex Offenders API
nav: Providers
network: true
overview: 'Sex Offenders API publishes 1 API on the [APIs.io](https://apis.io/) network: Sex Offenders API. Tagged areas include Sex Offenders, Public Safety, Crime Data, Background Checks, and Criminal Justice.


  Sex Offenders API''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, signup flow, and 20 more developer resources.'
plans:
- name: Sex Offenders Api Plans Pricing
  plan_count: 2
  slug: sex-offenders-api-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Sex Offenders Api Rate Limits
  slug: sex-offenders-api-rate-limits
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 4.5
    contract_quality: 59.9
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sex-offenders-api/refs/heads/main/screenshots/sex-offenders-api-2026-06-20T193740.png
security:
- kind: authentication
  name: Sex Offenders Api Authentication
  slug: sex-offenders-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sex Offenders Api Domain Security
  slug: sex-offenders-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sex-offenders-api
tags:
- Sex Offenders
- Public Safety
- Crime Data
- Background Checks
- Criminal Justice
- Government Data
- Geospatial
- Real-Estate
- Risk
- People Data
website: https://www.crimeometer.com/
---
