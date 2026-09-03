---
access_model:
  confidence: high
  label: Free · Registration, Data Security Agreement and supervised onboarding required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - documentation
  - authentication
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Con Edison Agentic Access
  operation_count: 37
  slug: con-edison-agentic-access
  summary_line: 37 operations · 2 acting
api_count: 1
apis:
- description: Con Edison's distribution-grid open data, published as anonymously readable Esri ArcGIS REST feature services behind the public Hosting Capacity Map. Con Edison's own documentation states that "REST A
  name: Con Edison Hosting Capacity Map REST API
  slug: con-edison-hosting-capacity-map-rest-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The ApplicationInformation API from Con Edison — 1 operation(s) for applicationinformation.
  name: Con Edison Application Information API
  slug: con-edison-applicationinformation-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The Authorization API from Con Edison — 3 operation(s) for authorization.
  name: Con Edison Authorization API
  slug: con-edison-authorization-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The Batch API from Con Edison — 4 operation(s) for batch.
  name: Con Edison Batch API
  slug: con-edison-batch-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The ElectricPowerUsageSummary API from Con Edison — 2 operation(s) for electricpowerusagesummary.
  name: Con Edison Electric Power Usage Summary API
  slug: con-edison-electricpowerusagesummary-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The IntervalBlock API from Con Edison — 2 operation(s) for intervalblock.
  name: Con Edison Interval Block API
  slug: con-edison-intervalblock-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The LocalTimeParameters API from Con Edison — 2 operation(s) for localtimeparameters.
  name: Con Edison Local Time Parameters API
  slug: con-edison-localtimeparameters-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The MeterReading API from Con Edison — 2 operation(s) for meterreading.
  name: Con Edison Meter Reading API
  slug: con-edison-meterreading-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The ReadingType API from Con Edison — 2 operation(s) for readingtype.
  name: Con Edison Reading Type API
  slug: con-edison-readingtype-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The RealTimeBatch API from Con Edison — 3 operation(s) for realtimebatch.
  name: Con Edison Real Time Batch API
  slug: con-edison-realtimebatch-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The RealTimeIntervalBlock API from Con Edison — 2 operation(s) for realtimeintervalblock.
  name: Con Edison Real Time Interval Block API
  slug: con-edison-realtimeintervalblock-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The RealTimeReadingType API from Con Edison — 2 operation(s) for realtimereadingtype.
  name: Con Edison Real Time Reading Type API
  slug: con-edison-realtimereadingtype-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The RetailCustomer API from Con Edison — 9 operation(s) for retailcustomer.
  name: Con Edison Retail Customer API
  slug: con-edison-retailcustomer-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The ServiceStatus API from Con Edison — 1 operation(s) for servicestatus.
  name: Con Edison Service Status API
  slug: con-edison-servicestatus-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The UsagePoint API from Con Edison — 2 operation(s) for usagepoint.
  name: Con Edison Usage Point API
  slug: con-edison-usagepoint-api
artifact_total: 22
asyncapis:
- description: ''
  name: Con Edison Batch Notification Webhooks
  slug: con-edison-batch-notification-webhooks
collections:
- collection_type: open
  name: DCX GBC API V2
  slug: open-con-edison-green-button-connect-my-data-swagger
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/con-edison-green-button-connect-my-data-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/con-edison-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/con-edison-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/con-edison-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/con-edison-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/con-edison-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party
- group: operate
  title: ''
  type: Support
  url: mailto:dlsharemydatatech@coned.com
- group: company
  title: ''
  type: Website
  url: https://www.coned.com/
- group: company
  title: ''
  type: About
  url: https://www.coned.com/en/about-us/company-information
- group: other
  title: ''
  type: ParentCompany
  url: https://www.conedison.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.coned.com/en/business-partners/access-customer-data
- group: docs
  title: ''
  type: Documentation
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data
- group: docs
  title: ''
  type: Documentation
  url: https://www.coned.com/en/save-money/make-better-energychoices-with-green-button
- group: start
  title: ''
  type: SignUp
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party/registration-form
- group: auth
  title: ''
  type: Authentication
  url: https://www.coned.com/en/accounts-billing/dashboard
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coned.com/en/conedison-privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coned.com/en/accounts-billing/dashboard/billing-and-usage/terms-of-use
- group: other
  title: ''
  type: Email
  url: mailto:dlsharemydatatech@coned.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/con-edison
- group: other
  title: ''
  type: Regulator
  url: https://dps.ny.gov/
- group: other
  title: ''
  type: Standard
  url: https://www.greenbuttonalliance.org/
- group: other
  title: ''
  type: Standard
  url: https://www.naesb.org/espi_standards.asp
- group: other
  title: ''
  type: SisterCompany
  url: https://www.oru.com/en/accounts-billing/share-energy-usage-data/become-a-third-party
created: '2026-07-27'
description: 'Consolidated Edison Company of New York, Inc. (CECONY, trading as Con Edison) is the investor-owned electric, gas and steam utility that serves New York City and Westchester County, and together with its sibling Orange & Rockland Utilities (ORU) forms the regulated utility core of Consolidated Edison, Inc. It is a wires-and-pipes distribution utility rather than a competitive retailer: it owns and operates the distribution system, meters the customer and bills the customer, while wholesale energy markets are run by NYISO and competitive supply is sold by ESCOs. It is rate-regulated by the New York State Public Service Commission. Its API posture is the most interesting in the United States sample because both halves are real and they are gated completely differently. On the consumer side Con Edison runs a genuine, verified Green Button Connect My Data implementation — the NAESB REQ.21 ESPI standard, branded "Share My Data" — with a live production base URI at https://api.coned.com/gbc/espi/1_1
  that answers anonymously with HTTP 401 "Unauthorized. Access token is missing or invalid.", a publicly downloadable 37-path Swagger 2.0 definition ("DCX GBC API V2"), a public Postman collection titled "GBC Certification Third party V3.3", OAuth 2.0 authorization-code and client-credentials flows, ESPI functional-block scopes, batch and real-time interval endpoints, and a 35-page technical onboarding document last revised 2026-05-07. The United States has no federal energy consumer data right; Con Edison''s adoption sits under New York PSC supervision (the Joint Utilities DSIP proceeding, Case 16-M-0411, in which it committed to implement the first phase of GBC by end of 2017, the Data Access Framework in Case 20-M-0082, and a Customer Data Access Tariff) rather than under a statutory mandate like Australia''s Consumer Data Right or Ontario Regulation 633/21. That data is not self-serve: a third party must register, sign a Data Security Agreement, submit a technical onboarding form and
  pass 30 to 60 days of supervised testing before production credentials are issued, and Con Edison states plainly that it "is unable to support API development for third parties." On the market side, by contrast, Con Edison publishes distribution-grid data openly and anonymously: the Hosting Capacity Map documents REST API access, and its ArcGIS feature services for segmented and network hosting capacity, EV transformer capacity, 33kV feeders, non-wires-solutions networks and disadvantaged communities all answer unauthenticated. Open on the grid, accredited on the customer — that split is the finding.'
layout: provider
modified: '2026-07-27'
name: Con Edison
nav: Providers
network: true
overview: 'Con Edison publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Application Information API, Authorization API, Batch API, and 11 more. Tagged areas include Energy, United States, New York, Utilities, and Electricity.


  The Con Edison catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Con Edison''s developer surface includes support, documentation, signup flow, authentication, and 21 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 2
  name: Con Edison Rate Limits
  slug: con-edison-rate-limits
scopes:
- name: Con Edison Scopes
  scope_count: 17
  slug: con-edison-scopes
  summary_line: 17 scopes
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 42.3
    developer_ergonomics: 68.5
    discoverability: 59.3
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/con-edison/refs/heads/main/screenshots/con-edison-2026-08-07T163921.png
security:
- kind: authentication
  name: Con Edison Authentication
  slug: con-edison-authentication
  summary_line: oauth2/http · 5 schemes
- kind: domain-security
  name: Con Edison Domain Security
  slug: con-edison-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: con-edison
tags:
- Energy
- United States
- New York
- Utilities
- Electricity
- Gas
- Steam
- Smart Metering
- Green Button
- Energy Data
- Grid
- Distribution
- Hosting Capacity
- Distributed Energy Resources
- Solar
- EV Charging
- Demand Response
website: https://www.coned.com/
---
