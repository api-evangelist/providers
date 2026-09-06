---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Xoserve Agentic Access
  operation_count: 4
  slug: xoserve-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- baseURL: https://discoveryapi.correla.com/shipper/v1
  baseurl_source: declared
  description: Bundled by Xoserve as the Supply Point Quantities service. Lets gas Shippers view the proposed Formula Year (Billing) Annual Quantity value for a meter point ahead of the late-March notification to th
  name: Xoserve Shipper API
  slug: xoserve-shipper-api
- baseURL: https://discoveryapi.correla.com/supplier/v1
  baseurl_source: declared
  description: Bundled by Xoserve as the Supply Point Enquiry service, part of the Gas Enquiry Service (GES). Exposes detailed supply meter point information, filtered by MPRN, address_id or postcode combined with o
  name: Xoserve Supplier API
  slug: xoserve-supplier-api
artifact_total: 19
collections:
- collection_type: open
  name: Meter Asset
  slug: open-xoserve-meter-asset-api-v1
- collection_type: open
  name: Meter Asset
  slug: open-xoserve-meter-asset-api-v2
- collection_type: open
  name: Shipper
  slug: open-xoserve-shipper-api
- collection_type: open
  name: Supplier
  slug: open-xoserve-supplier-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xoserve-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/xoserve-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.xoserve.com/
- group: start
  title: ''
  type: Portal
  url: https://discoveryapiportal.correla.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.xoserve.com/products-services/data-products/gas-apis/
- group: docs
  title: ''
  type: APIReference
  url: https://discoveryapiportal.correla.com/apis
- group: start
  title: ''
  type: SignUp
  url: https://discoveryapiportal.correla.com/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xoserve.com/products-services/data-products/gas-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.xoserve.com/media/7975/xoserve-try-before-you-buy-api-service-subscription-guide.pdf
- group: company
  title: ''
  type: Blog
  url: https://www.xoserve.com/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xoserve/
- group: operate
  title: ''
  type: Support
  url: https://www.xoserve.com/help-and-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.xoserve.com/help-and-support/raise-a-new-support-request/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xoserve.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xoserve.com/privacy-notice/
- group: auth
  title: ''
  type: Compliance
  url: https://www.xoserve.com/about-us/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.xoserve.com/news-updates/news-and-updates/planned-outages/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.xoserve.com/change/uk-link-releases/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/xoserve-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/xoserve-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/xoserve-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/xoserve-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/xoserve-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/xoserve-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/xoserve-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/xoserve-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/xoserve-rate-limits.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/xoserve-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/xoserve-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/xoserve-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xoserve-llms.txt
- group: docs
  title: ''
  type: TechnicalSpecification
  url: https://discoveryapiportal.correla.com/api-details#api=shipper&operation=getShipper_1
- group: company
  title: ''
  type: Website
  url: https://www.findmysupplier.energy/
created: '2026-07-27'
description: 'Xoserve Limited is the Central Data Services Provider (CDSP) for Great Britain''s gas market — funded, governed and owned by the gas industry itself. From Solihull it operates the central register of every gas supply point in Britain and runs the systems the market clears through: UK Link, the Gemini transmission system, the Gas Enquiry Service, the Contact Management Service, SwitchStream and the Data Discovery Platform. It sits between the gas transporters, the independent gas transporters, the shippers and the retail suppliers under the Uniform Network Code (UNC) and the Data Services Contract (DSC), with further obligations under the Retail Energy Code. Britain mandated this data infrastructure, not a consumer data right: there is no CDR-style, consent-driven data portability obligation on Xoserve, and no Green Button or Consumer Data Standards implementation. Its API posture reflects that split exactly. Xoserve does publish a real developer portal — the Discovery API Platform,
  delivered by its service provider Correla at discoveryapiportal.correla.com — where four documented REST APIs (Shipper, Supplier, Meter Asset v1 and v2) expose meter-point-level information including proposed Formula Year Annual Quantity values, current supplier, network and meter asset detail. Anyone may browse that catalogue and export the OpenAPI documents anonymously, but nobody can call the gateway without being an eligible licensed GB gas industry party: every product requires a subscription AND approval, keys are issued only after a contract is countersigned, and the gateway returns 401 for everyone else. Consumer usage data is therefore reachable through a documented API, but only by accredited industry, never by a consumer or an agent acting on their behalf. On the other side, Xoserve publishes no open machine-readable market-data API at all — its public outputs are the free findmysupplier consumer lookup it operates and the Market Domain Data participant list as a spreadsheet
  download.'
examples:
- key_count: 1
  name: Xoserve Meter Asset Api V1 Response Example
  slug: xoserve-meter-asset-api-v1-response-example
- key_count: 1
  name: Xoserve Meter Asset Api V2 Response Example
  slug: xoserve-meter-asset-api-v2-response-example
- key_count: 1
  name: Xoserve Shipper Api Response Example
  slug: xoserve-shipper-api-response-example
- key_count: 1
  name: Xoserve Supplier Api Response Example
  slug: xoserve-supplier-api-response-example
image: https://www.xoserve.com/assets/images/Favicons/favicon-96x96.png
json_schemas:
- name: Xoserve Meter Asset Api V1 Components
  property_count: 0
  slug: xoserve-meter-asset-api-v1-components
- name: Xoserve Meter Asset Api V2 Components
  property_count: 0
  slug: xoserve-meter-asset-api-v2-components
- name: Xoserve Shipper Api Components
  property_count: 0
  slug: xoserve-shipper-api-components
- name: Xoserve Supplier Api Components
  property_count: 0
  slug: xoserve-supplier-api-components
layout: provider
modified: '2026-07-27'
name: Xoserve
nav: Providers
network: true
overview: 'Xoserve publishes 2 APIs on the [APIs.io](https://apis.io/) network: Shipper API and Supplier API. Tagged areas include Energy, United Kingdom, Gas, Utilities, and Energy Markets.


  Xoserve''s developer surface includes authentication, developer portal, documentation, API reference, signup flow, pricing, getting-started guide, and 27 more developer resources.'
plans:
- name: Xoserve Plans
  plan_count: 4
  slug: xoserve-plans
random_paper: 3
rate_limits:
- limit_count: 6
  name: Xoserve Rate Limits
  slug: xoserve-rate-limits
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 67.0
    catalog_earned_first_party: 24.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 38.8
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 64.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 67.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xoserve/refs/heads/main/screenshots/xoserve-2026-08-17T083012.png
security:
- kind: authentication
  name: Xoserve Authentication
  slug: xoserve-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Xoserve Domain Security
  slug: xoserve-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xoserve
tags:
- Energy
- United Kingdom
- Gas
- Utilities
- Energy Markets
- Meter Data
- Gas Networks
- Central Data Service Provider
- Data Services
website: https://www.xoserve.com/
---
