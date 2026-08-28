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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Con Edison Agentic Access
  operation_count: 37
  slug: con-edison-agentic-access
  summary_line: 37 operations · 2 acting
api_count: 2
apis:
- description: Con Edison and Orange & Rockland's Green Button Connect My Data (CMD) implementation, branded "Share My Data" — the NAESB REQ.21 Energy Services Provider Interface (ESPI) machine-to-machine API throug
  name: Con Edison Green Button Connect My Data API
  slug: con-edison-green-button-connect-my-data-api
- description: Con Edison's distribution-grid open data, published as anonymously readable Esri ArcGIS REST feature services behind the public Hosting Capacity Map. Con Edison's own documentation states that "REST A
  name: Con Edison Hosting Capacity Map REST API
  slug: con-edison-hosting-capacity-map-rest-api
artifact_total: 10
asyncapis:
- description: ''
  name: Con Edison Batch Notification Webhooks
  slug: con-edison-batch-notification-webhooks
collections:
- collection_type: open
  name: DCX GBC API V2
  slug: open-con-edison-green-button-connect-my-data-swagger
common:
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
mcp_servers:
- description: ''
  name: Candidate MCP tool list derived from the published Swagger definition (no server exists)
  slug: candidate-mcp-tool-list-derived-from-the-published-swagger-definition-no-server-exists
modified: '2026-07-27'
name: Con Edison
nav: Providers
network: true
overview: 'Con Edison publishes 1 API on the [APIs.io](https://apis.io/) network: Green Button Connect My Data API. Tagged areas include Energy, United States, New York, Utilities, and Electricity.


  The Con Edison catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Con Edison''s developer surface includes support, documentation, signup flow, authentication, and 19 more developer resources.'
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
  composite: 51.2
  delta: 6.8
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 30.3
    contract_quality: 44.9
    developer_ergonomics: 68.5
    discoverability: 64.8
    governance: 30.3
    operational_transparency: 28.9
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 56.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
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
