---
access_model:
  confidence: high
  label: Free, approval-gated — Data Security Agreement plus 30-60 day technical onboarding
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  - docs
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
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Consolidated Edison Agentic Access
  operation_count: 37
  slug: consolidated-edison-agentic-access
  summary_line: 37 operations · 2 acting
api_count: 2
apis:
- description: 'Customer-driven file export that lets Con Edison residential and small commercial accounts download up to one year of smart-meter interval data as CSV or ESPI XML directly from the My Account portal. '
  name: Green Button Download My Data
  slug: green-button-download
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The ApplicationInformation API from Consolidated Edison — 1 operation(s) for applicationinformation.
  name: Consolidated Edison Application Information API
  slug: consolidated-edison-applicationinformation-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The Authorization API from Consolidated Edison — 3 operation(s) for authorization.
  name: Consolidated Edison Authorization API
  slug: consolidated-edison-authorization-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The Batch API from Consolidated Edison — 4 operation(s) for batch.
  name: Consolidated Edison Batch API
  slug: consolidated-edison-batch-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The ElectricPowerUsageSummary API from Consolidated Edison — 2 operation(s) for electricpowerusagesummary.
  name: Consolidated Edison Electric Power Usage Summary API
  slug: consolidated-edison-electricpowerusagesummary-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The IntervalBlock API from Consolidated Edison — 2 operation(s) for intervalblock.
  name: Consolidated Edison Interval Block API
  slug: consolidated-edison-intervalblock-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The LocalTimeParameters API from Consolidated Edison — 2 operation(s) for localtimeparameters.
  name: Consolidated Edison Local Time Parameters API
  slug: consolidated-edison-localtimeparameters-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The MeterReading API from Consolidated Edison — 2 operation(s) for meterreading.
  name: Consolidated Edison Meter Reading API
  slug: consolidated-edison-meterreading-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The ReadingType API from Consolidated Edison — 2 operation(s) for readingtype.
  name: Consolidated Edison Reading Type API
  slug: consolidated-edison-readingtype-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The RealTimeBatch API from Consolidated Edison — 3 operation(s) for realtimebatch.
  name: Consolidated Edison Real Time Batch API
  slug: consolidated-edison-realtimebatch-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The RealTimeIntervalBlock API from Consolidated Edison — 2 operation(s) for realtimeintervalblock.
  name: Consolidated Edison Real Time Interval Block API
  slug: consolidated-edison-realtimeintervalblock-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The RealTimeReadingType API from Consolidated Edison — 2 operation(s) for realtimereadingtype.
  name: Consolidated Edison Real Time Reading Type API
  slug: consolidated-edison-realtimereadingtype-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The RetailCustomer API from Consolidated Edison — 9 operation(s) for retailcustomer.
  name: Consolidated Edison Retail Customer API
  slug: consolidated-edison-retailcustomer-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The UsagePoint API from Consolidated Edison — 2 operation(s) for usagepoint.
  name: Consolidated Edison Usage Point API
  slug: consolidated-edison-usagepoint-api
- baseURL: https://api.coned.com/gbc/espi/1_1
  baseurl_source: declared
  description: The Service Status API from Consolidated Edison — 1 operation(s) for service status.
  name: Consolidated Edison Service Status API
  slug: consolidated-edison-service-status-api
artifact_total: 23
asyncapis:
- description: ''
  name: Consolidated Edison Webhooks
  slug: consolidated-edison-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/agentic-access/consolidated-edison-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/consolidated-edison-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/security/consolidated-edison-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consolidated-edison-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Con-Edison
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/con-edison
- group: company
  title: ''
  type: Website
  url: https://www.coned.com
- group: start
  title: ''
  type: Login
  url: https://www.coned.com/en/accounts-billing/my-account
- group: other
  title: ''
  type: Registration
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party
- group: company
  title: ''
  type: About
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/share-my-data
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.conedison.com
- group: company
  title: ''
  type: Careers
  url: https://www.coned.com/en/about-us/careers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coned.com/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coned.com/en/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.coned.com/en/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party
- group: docs
  title: ''
  type: APIReference
  url: https://edge-e-dcx-downloads-prod-gjf6ega8bmh8crfh.a01.azurefd.net/gbc-api-defintions/swagger-cert.json?sp=r&st=2024-08-29T02:55:48Z&se=2031-08-29T10:55:48Z&spr=https&sv=2022-11-02&sr=b&sig=WAVltmTKe4OKqZWoO5je%2FUMTZSB5%2BdMk8FbgNHR%2FkCU%3D
- group: start
  title: ''
  type: GettingStarted
  url: https://edge-e-dcxprod-web-bechbkdqagefb9ge.a03.azurefd.net/-/media/files/coned/documents/accountandbilling/share-my-data/onboarding-doc.pdf
- group: start
  title: ''
  type: SignUp
  url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party/registration-form
- group: build
  title: ''
  type: Postman
  url: https://edge-e-dcx-downloads-prod-gjf6ega8bmh8crfh.a01.azurefd.net/gbc-api-defintions/postman-collection.json?sp=r&st=2026-04-28T15:40:29Z&se=2031-08-29T23:55:29Z&spr=https&sv=2025-11-05&sr=b&sig=rrSK9xQA4obHLvHoXI9Q2N61Z2KDHANFrKJp3cMoygU%3D
- group: operate
  title: ''
  type: FAQ
  url: https://edge-e-dcxprod-web-bechbkdqagefb9ge.a03.azurefd.net/-/media/files/coned/documents/accountandbilling/share-my-data/faq.pdf
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/authentication/consolidated-edison-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consolidated-edison-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/scopes/consolidated-edison-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/consolidated-edison-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/conformance/consolidated-edison-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consolidated-edison-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/conventions/consolidated-edison-conventions.yml
  title: ''
  type: Conventions
  url: conventions/consolidated-edison-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/errors/consolidated-edison-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/consolidated-edison-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/lifecycle/consolidated-edison-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/consolidated-edison-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/sandbox/consolidated-edison-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/consolidated-edison-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/data-model/consolidated-edison-data-model.yml
  title: ''
  type: DataModel
  url: data-model/consolidated-edison-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/packages/consolidated-edison-packages.yml
  title: ''
  type: Packages
  url: packages/consolidated-edison-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/asyncapi/consolidated-edison-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/consolidated-edison-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/llms/consolidated-edison-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consolidated-edison-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/overlays/consolidated-edison-green-button-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/consolidated-edison-green-button-connect-overlay.yaml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/rate-limits/consolidated-edison-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/consolidated-edison-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/plans/consolidated-edison-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consolidated-edison-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/finops/consolidated-edison-finops.yml
  title: ''
  type: FinOps
  url: finops/consolidated-edison-finops.yml
created: '2026-03-21'
description: 'Consolidated Edison, Inc. (Con Edison) is a Fortune 500 investor-owned utility providing electric, natural gas and steam service to New York City and Westchester County. It runs no general-purpose developer portal; its one programmatic surface is Green Button Connect My Data - branded Share My Data - a NAESB ESPI (REQ.21) / Green Button V3.3 API that lets a registered third party retrieve a customer''s interval usage, billing and account data once that customer consents. The contract is published: Con Edison links a Swagger 2.0 definition (DCX GBC API V2, 37 operations over UsagePoint, MeterReading, IntervalBlock, ReadingType, UsageSummary, RetailCustomer, Batch and RealTime) and a Postman collection from its public onboarding document; production base is https://api.coned.com/gbc/espi/1_1. Access is free but not self-service - a Data Security Agreement and a 30-60 day onboarding come first. Orange & Rockland runs the identical contract.'
finops:
- name: Consolidated Edison Finops
  service_category: Regulated Utility / Energy
  slug: consolidated-edison-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/consolidated-edison.png
layout: provider
modified: '2026-09-05'
name: Consolidated Edison
nav: Providers
network: true
overview: 'Consolidated Edison publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Application Information API, Authorization API, Batch API, and 11 more. Tagged areas include AMI, Demand Response, ESPI, Energy, and Fortune 500.


  The Consolidated Edison catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Consolidated Edison''s developer surface includes support, documentation, API reference, getting-started guide, signup flow, FAQ, authentication, and 28 more developer resources.'
plans:
- name: Consolidated Edison Plans Pricing
  plan_count: 1
  slug: consolidated-edison-plans-pricing
press:
- date: '2026-05-25'
  title: 'Document 2 - file: ed-20251231xexx991.htm'
  url: https://www.sec.gov/Archives/edgar/data/1047862/000104786226000028/ed-20251231xexx991.htm
- date: '2026-05-25'
  title: CON EDISON REPORTS 2026 FIRST QUARTER EARNINGS
  url: https://www.prnewswire.com/news-releases/con-edison-reports-2026-first-quarter-earnings-302766258.html
- date: '2026-05-25'
  title: CON EDISON REPORTS 2026 FIRST QUARTER EARNINGS
  url: https://investor.conedison.com/news-releases/news-release-details/con-edison-reports-2026-first-quarter-earnings
- date: '2026-05-25'
  title: Con Edison Selects C3.ai for Big Data and Predictive ...
  url: https://c3.ai/utility-selects-c3-iot-big-data-predictive-analytics-platform-applications/
- date: '2026-05-25'
  title: Con Edison posts higher 2025 earnings, sets 2026 EPS view
  url: https://www.stocktitan.net/sec-filings/ED/8-k-consolidated-edison-inc-reports-material-event-0907b1b03c4d.html
random_paper: 2
rate_limits:
- limit_count: 2
  name: Consolidated Edison Rate Limits
  slug: consolidated-edison-rate-limits
scopes:
- name: Consolidated Edison Scopes
  scope_count: 17
  slug: consolidated-edison-scopes
  summary_line: 17 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.0
    catalog_earned_first_party: 16.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 58.9
    discoverability: 53.7
    operational_transparency: 31.6
  previous_composite: 55.1
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
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/screenshots/consolidated-edison-2026-07-25T210311.png
security:
- kind: authentication
  name: Consolidated Edison Authentication
  slug: consolidated-edison-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Consolidated Edison Domain Security
  slug: consolidated-edison-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: consolidated-edison
tags:
- AMI
- Demand Response
- ESPI
- Energy
- Fortune 500
- Green Button
- Interval Data
- NAESB
- Natural Gas
- New York
- Authentication
- Steam
- Utility
website: https://www.coned.com
---
