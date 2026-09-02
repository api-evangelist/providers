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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Moodys Corporation Agentic Access
  operation_count: 24
  slug: moodys-corporation-agentic-access
  summary_line: 24 operations · 8 acting
api_count: 2
apis:
- description: Programmatic access to the Scenario Studio macroeconomic scenario platform, enabling automatic retrieval of custom scenarios generated against the Moody's Analytics Global Macroeconomic Model. Support
  name: Moody's Analytics Scenario Studio API
  slug: scenario-studio-api
- description: Retrieves forecasts of vehicle prices from AutoCycle models, integrating Moody's Analytics economic data and scenarios for automotive residual value forecasting.
  name: Moody's AutoCycle API
  slug: autocycle-api
- description: Retrieves expected consumer credit loss forecasts under baseline and stress scenarios. Combines customer data, economic data from Moody's Analytics, and consumer credit data for credit risk modeling a
  name: Moody's Expected Consumer Credit Loss (ECCL) API
  slug: eccl-api
- description: Programmatic interface to ImpairmentStudio for CECL impairment estimation. Supports importing input datasets, triggering analyses, polling job status, and downloading analysis outputs via the apic Pyt
  name: Moody's ImpairmentStudio API
  slug: impairmentstudio-api
- description: 'Access to Orbis, the Bureau van Dijk company information database covering hundreds of millions of public and private companies worldwide with ownership, financials, officers, beneficial owners, ESG, '
  name: Moody's Orbis (Bureau van Dijk) API
  slug: orbis-api
- description: Verifies businesses against authoritative primary-source government registers in real time, returning legal entity records, ultimate beneficial owners, registered documents, and AML / sanctions screen
  name: Moody's KYC API (Kompany / Maxsight Entity Verification)
  slug: kyc-api
- description: Customer lifecycle and KYC orchestration platform enabling onboarding, perpetual KYC, customer due diligence, and supplier risk workflows. Exposes a Custom Check Framework so integrators can plug addi
  name: Moody's Passfort Lifecycle API
  slug: passfort-api
- description: APIs for the RMS Intelligent Risk Platform covering catastrophe modeling, exposure management, and event response across natural perils (hurricane, earthquake, flood, severe convective storm, wildfire
  name: Moody's RMS Intelligent Risk Platform (IRP) API
  slug: rms-irp-api
- description: OAuth2 client-credentials token issuance and HMAC signing helpers
  name: Moody's Corporation Authentication API
  slug: moodys-corporation-authentication-api
- description: Operations for creating and managing collections of series requests
  name: Moody's Corporation Baskets API
  slug: moodys-corporation-baskets-api
- description: Discovery of available products, datasets, and entitlements
  name: Moody's Corporation Catalog API
  slug: moodys-corporation-catalog-api
- description: Platform availability and version metadata
  name: Moody's Corporation Health API
  slug: moodys-corporation-health-api
- description: Asynchronous analysis-job submission, polling, and output retrieval
  name: Moody's Corporation Jobs API
  slug: moodys-corporation-jobs-api
- description: Operations for managing data generation orders from baskets
  name: Moody's Corporation Orders API
  slug: moodys-corporation-orders-api
- description: Operations for retrieving frequency, vintage, and file type metadata
  name: Moody's Corporation Reference API
  slug: moodys-corporation-reference-api
- description: Operations for searching available datasets and series
  name: Moody's Corporation Search API
  slug: moodys-corporation-search-api
- description: Operations for retrieving individual and multi-series time series data
  name: Moody's Corporation Series API
  slug: moodys-corporation-series-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Moody's Analytics Developer Platform API
  slug: open-moodys-analytics-developer
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication API
  slug: open-moodys-corporation-authentication-api
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication Baskets API
  slug: open-moodys-corporation-baskets-api
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication Catalog API
  slug: open-moodys-corporation-catalog-api
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication Health API
  slug: open-moodys-corporation-health-api
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication Jobs API
  slug: open-moodys-corporation-jobs-api
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication Orders API
  slug: open-moodys-corporation-orders-api
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication Reference API
  slug: open-moodys-corporation-reference-api
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication Search API
  slug: open-moodys-corporation-search-api
- collection_type: open
  name: Moody's Analytics Developer Platform Authentication Series API
  slug: open-moodys-corporation-series-api
- collection_type: open
  name: Moody's Data Buffet API
  slug: open-moodys-data-buffet-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moodys-corporation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moodys-corporation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moodys-corporation-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/moodys-corporation-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.moodys.com/
- group: company
  title: ''
  type: Blog
  url: https://www.moodys.com/web/en/us/insights.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moodys.com/web/en/us/about/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moodys.com/web/en/us/about/legal/privacy-policy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moodysanalytics
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.moodys.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.moodys.com/web/en/us/about/contact.html
- group: other
  title: ''
  type: Insights
  url: https://www.moodys.com/web/en/us/insights/all.html
- group: company
  title: ''
  type: Investors
  url: https://ratings.moodys.com/
description: 'Moody''s Corporation (NYSE: MCO) is a global integrated risk-assessment firm operating through two segments: Moody''s Ratings (Moody''s Investors Service), which publishes credit ratings and assessment services on debt obligations, and Moody''s Analytics, which provides data, software, research, and APIs spanning economic data, credit risk, KYC/AML, ESG, climate, and catastrophe modeling. Moody''s Analytics products are exposed through multiple developer APIs and a portal at developer.moodys.com, with deeper API surfaces published at api.economy.com (Data Buffet, Scenario Studio, AutoCycle, ECCL) and through subsidiary brands including Bureau van Dijk (Orbis), RMS (catastrophe risk), Kompany / Passfort (KYC), and Four Twenty Seven (climate).'
examples:
- key_count: 8
  name: Moodys Corporation Cat Event Example
  slug: moodys-corporation-cat-event-example
- key_count: 12
  name: Moodys Corporation Credit Rating Example
  slug: moodys-corporation-credit-rating-example
- key_count: 13
  name: Moodys Corporation Entity Example
  slug: moodys-corporation-entity-example
- key_count: 9
  name: Moodys Corporation Time Series Example
  slug: moodys-corporation-time-series-example
- key_count: 2
  name: Moodys Corporation Token Example
  slug: moodys-corporation-token-example
finops:
- name: Moodys Corporation Finops
  service_category: ''
  slug: moodys-corporation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moodys-corporation.png
json_schemas:
- name: Moody's RMS Catastrophe Event
  property_count: 8
  slug: moodys-corporation-cat-event
- name: Moody's Credit Rating
  property_count: 15
  slug: moodys-corporation-credit-rating
- name: Moody's Orbis / KYC Entity
  property_count: 16
  slug: moodys-corporation-entity
- name: Moody's Analytics Time Series
  property_count: 11
  slug: moodys-corporation-time-series
json_structures:
- name: Moodys Corporation Credit Rating Structure
  property_count: 0
  slug: moodys-corporation-credit-rating-structure
- name: Moodys Corporation Entity Structure
  property_count: 0
  slug: moodys-corporation-entity-structure
- name: Moodys Corporation Time Series Structure
  property_count: 0
  slug: moodys-corporation-time-series-structure
jsonld:
- class_count: 34
  name: Moodys Corporation Context
  property_count: 0
  slug: moodys-corporation-context
layout: provider
modified: '2026-07-25'
name: Moody's Corporation
nav: Providers
network: true
overview: 'Moody''s Corporation publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Baskets API, Catalog API, and 6 more. Tagged areas include Analytics, Catastrophe Risk, Climate Risk, Compliance, and Credit Ratings.


  The Moody''s Corporation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Moody''s Corporation''s developer surface includes authentication, developer portal, engineering blog, and 10 more developer resources.'
plans:
- name: Moodys Corporation Plans Pricing
  plan_count: 2
  slug: moodys-corporation-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Moodys Corporation Rate Limits
  slug: moodys-corporation-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Moody's Corporation API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: moodys-analytics-developer-rules
- effective_rule_count: 5
  extends: []
  name: Moody's Corporation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: moodys-corporation-jsonschema-spectral-rules
scopes:
- name: Moodys Corporation Scopes
  scope_count: 2
  slug: moodys-corporation-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 41.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 54.5
    contract_quality: 64.6
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 54.5
    operational_transparency: 2.6
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moodys-corporation/refs/heads/main/screenshots/moodys-corporation-2026-08-17T081109.png
security:
- kind: authentication
  name: Moodys Corporation Authentication
  slug: moodys-corporation-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Moodys Corporation Domain Security
  slug: moodys-corporation-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: moodys-corporation
tags:
- Analytics
- Catastrophe Risk
- Climate Risk
- Compliance
- Credit Ratings
- Economic Data
- ESG
- Financial Data
- KYC
- Risk
- Fortune 1000
website: https://www.moodys.com/
---
