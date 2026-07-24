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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Corelogic Agentic Access
  operation_count: 43
  slug: corelogic-agentic-access
  summary_line: 43 operations · 11 acting
api_count: 27
apis:
- description: Trestle's RETS endpoint implements the RETS 1.8 specification on top of the same data catalog as the RESO Web API. The service is session-less; authentication uses HTTP Basic with client credentials o
  name: Trestle RETS
  slug: trestle-rets
- description: 'The Direct Web API MLO reference exposes Member Loan Officer / lender-side data from the Matrix MLS platform via OData. Used to integrate originator and loan-officer profiles, branches, and licensing '
  name: Direct Web API — MLO
  slug: direct-webapi-mlo
- description: The Participant Reporting API allows MLS staff and brokerages to report broker/agent participation events back to Trestle. Documented in a published PDF reference; used for audit, compliance, and roya
  name: Participant Reporting API
  slug: participant-reporting-api
- description: 360 Property Data is Cotality's enterprise property data product covering structure, ownership, tax, mortgages, hazard risk, climate risk, and geospatial overlays across approximately 99% of U.S. resi
  name: 360 Property Data
  slug: 360-property-data
- description: 'Climate Risk Analytics (CRA) delivers parcel- and structure-level chronic climate risk indices and acute peril scores across the continental United States and the District of Columbia. Chronic Perils '
  name: Climate Risk Analytics
  slug: climate-risk-analytics
- description: CRM contact records (name, address, phone, email).
  name: CoreLogic (Cotality) Contacts API
  slug: corelogic-contacts-api
- description: MLS-specific extensions to the RESO Property resource.
  name: CoreLogic (Cotality) CustomProperty API
  slug: corelogic-customproperty-api
- description: Aggregated dashboard data for the agent home screen.
  name: CoreLogic (Cotality) DashboardAPI API
  slug: corelogic-dashboardapi-api
- description: Service-level metadata and available resources.
  name: CoreLogic (Cotality) DataSystem API
  slug: corelogic-datasystem-api
- description: Outbound messages sent to contacts.
  name: CoreLogic (Cotality) EmailHistory API
  slug: corelogic-emailhistory-api
- description: Metadata describing fields available on each resource.
  name: CoreLogic (Cotality) Field API
  slug: corelogic-field-api
- description: Transactional change history for tracked resources.
  name: CoreLogic (Cotality) HistoryTransactional API
  slug: corelogic-historytransactional-api
- description: Property lists / carts attached to contacts.
  name: CoreLogic (Cotality) Lists API
  slug: corelogic-lists-api
- description: Enumerated lookup values used across resources.
  name: CoreLogic (Cotality) Lookup API
  slug: corelogic-lookup-api
- description: Listing media (photos, videos, documents).
  name: CoreLogic (Cotality) Media API
  slug: corelogic-media-api
- description: MLS member (agent) records.
  name: CoreLogic (Cotality) Member API
  slug: corelogic-member-api
- description: Resource model definitions.
  name: CoreLogic (Cotality) Model API
  slug: corelogic-model-api
- description: MLS office (brokerage) records.
  name: CoreLogic (Cotality) Office API
  slug: corelogic-office-api
- description: Scheduled open-house events.
  name: CoreLogic (Cotality) OpenHouse API
  slug: corelogic-openhouse-api
- description: Contact-scoped listing notes, views, and preferences.
  name: CoreLogic (Cotality) PortalContents API
  slug: corelogic-portalcontents-api
- description: MLS property listings and detail records.
  name: CoreLogic (Cotality) Property API
  slug: corelogic-property-api
- description: Per-room detail for listed properties.
  name: CoreLogic (Cotality) PropertyRooms API
  slug: corelogic-propertyrooms-api
- description: Per-unit detail for multi-unit properties.
  name: CoreLogic (Cotality) PropertyUnitTypes API
  slug: corelogic-propertyunittypes-api
- description: Saved listing search criteria with auto-email schedules.
  name: CoreLogic (Cotality) SavedSearches API
  slug: corelogic-savedsearches-api
- description: Membership relationships between teams and members.
  name: CoreLogic (Cotality) TeamMembers API
  slug: corelogic-teammembers-api
- description: MLS team records.
  name: CoreLogic (Cotality) Teams API
  slug: corelogic-teams-api
- description: Per-user preference key/value store.
  name: CoreLogic (Cotality) UserRegistry API
  slug: corelogic-userregistry-api
artifact_total: 52
collections:
- collection_type: open
  name: CoreLogic Trestle Direct Web API — CRM
  slug: open-corelogic-direct-webapi-crm
- collection_type: open
  name: CoreLogic Trestle RESO Web API
  slug: open-corelogic-trestle-reso-web-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/corelogic-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corelogic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/corelogic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/corelogic-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/corelogic
- group: company
  title: ''
  type: Website
  url: https://www.cotality.com
- group: company
  title: ''
  type: LegacyWebsite
  url: https://www.corelogic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.corelogic.com
- group: start
  title: ''
  type: DeveloperPortalAPAC
  url: https://developer.corelogic.asia/
- group: docs
  title: ''
  type: Documentation
  url: https://trestle-documentation.corelogic.com/
- group: docs
  title: ''
  type: APIReference
  url: https://trestle-documentation.corelogic.com/webapi-reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://trestle-documentation.corelogic.com/webapi.html
- group: auth
  title: ''
  type: Authorization
  url: https://trestle-documentation.corelogic.com/webapi.html
- group: auth
  title: ''
  type: TokenEndpoint
  url: https://api.cotality.com/trestle/oidc/connect/token
- group: other
  title: ''
  type: BaseURL
  url: https://api.cotality.com/trestle/odata
- group: operate
  title: ''
  type: FAQ
  url: https://trestle-documentation.corelogic.com/faq.html
- group: build
  title: ''
  type: ClientLibraries
  url: https://trestle-documentation.corelogic.com/webapi-libraries.html
- group: operate
  title: ''
  type: SupportEmail
  url: mailto:trestlesupport@cotality.com
- group: operate
  title: ''
  type: SupportPage
  url: https://www.cotality.com/support
- group: start
  title: ''
  type: Login
  url: https://developer.corelogic.asia/user/sign-in
- group: start
  title: ''
  type: Signup
  url: https://developer.corelogic.asia/signup
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/corelogic-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/corelogic-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/corelogic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/corelogic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/corelogic-finops.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cotality.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cotality.com/terms-of-use
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cotality
- group: company
  title: ''
  type: News
  url: https://www.cotality.com/news
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.corelogic.asia/llms.txt
created: '2026-05-23'
description: CoreLogic — rebranded as Cotality in 2025 — is a property data and analytics company providing real estate, mortgage, tax, hazard, and climate-risk information across approximately 99% of U.S. residential properties plus operations in Australia, New Zealand, the United Kingdom, Canada, Germany, and India. The company was taken private by Stone Point Capital and Insight Partners in June 2021 in a $6B transaction. The primary public developer surface is Trestle (trestle-documentation.corelogic.com / api.cotality.com), which delivers MLS listing, member, office, media, and team data via a RESO Web API 2.0 / OData 4.0 endpoint, a RETS 1.8 endpoint, and a Direct Web API for Matrix CRM and MLO (member loan officer) integrations. Most other Cotality data products — 360 Property Data, Climate Risk Analytics, Discovery Platform — are delivered through cloud data shares (AWS, Databricks, Google Cloud, Azure, Snowflake) and SFTP rather than self-service REST APIs and are gated behind enterprise
  sales.
examples:
- key_count: 9
  name: Corelogic Climate Risk Score Example
  slug: corelogic-climate-risk-score-example
- key_count: 2
  name: Corelogic Direct Webapi Create Contact Example
  slug: corelogic-direct-webapi-create-contact-example
- key_count: 2
  name: Corelogic Trestle Oauth Token Example
  slug: corelogic-trestle-oauth-token-example
- key_count: 2
  name: Corelogic Trestle Query Media Example
  slug: corelogic-trestle-query-media-example
- key_count: 2
  name: Corelogic Trestle Query Property Example
  slug: corelogic-trestle-query-property-example
finops:
- name: Corelogic Finops
  service_category: Property & Climate Risk Data
  slug: corelogic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/corelogic.png
json_schemas:
- name: CoreLogic Climate Risk Score
  property_count: 9
  slug: corelogic-climate-risk
- name: Direct Web API CRM Contact
  property_count: 10
  slug: corelogic-contact
- name: RESO Media
  property_count: 9
  slug: corelogic-media
- name: RESO Member
  property_count: 11
  slug: corelogic-member
- name: RESO Office
  property_count: 10
  slug: corelogic-office
- name: RESO Property
  property_count: 27
  slug: corelogic-property
json_structures:
- name: Corelogic Property Structure
  property_count: 0
  slug: corelogic-property-structure
jsonld:
- class_count: 67
  name: Corelogic Context
  property_count: 0
  slug: corelogic-context
layout: provider
modified: '2026-05-23'
name: CoreLogic (Cotality)
nav: Providers
network: true
overview: 'CoreLogic (Cotality) publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, CustomProperty API, DashboardAPI API, and 19 more. Tagged areas include Climate Risk, CoreLogic, Cotality, Direct Web API, and Hazard Data.


  The CoreLogic (Cotality) catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  CoreLogic (Cotality)''s developer surface includes authentication, documentation, API reference, getting-started guide, FAQ, signup flow, product news, and 24 more developer resources.'
plans:
- name: Corelogic Plans Pricing
  plan_count: 4
  slug: corelogic-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 8
  name: Corelogic Rate Limits
  slug: corelogic-rate-limits
rules:
- name: CoreLogic (Cotality) API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 3
  slug: corelogic-direct-webapi-crm-rules
- name: CoreLogic (Cotality) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: corelogic-jsonschema-spectral-rules
- name: CoreLogic (Cotality) API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 4
  slug: corelogic-trestle-reso-web-api-rules
scopes:
- name: Corelogic Scopes
  scope_count: 1
  slug: corelogic-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 55.7
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 62.3
    developer_ergonomics: 45.7
    discoverability: 67.5
    governance: 39.5
    operational_transparency: 36.8
  previous_composite: 55.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corelogic/refs/heads/main/screenshots/corelogic-2026-06-20T175025.png
security:
- kind: authentication
  name: Corelogic Authentication
  slug: corelogic-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Corelogic Domain Security
  slug: corelogic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: corelogic
tags:
- Climate Risk
- CoreLogic
- Cotality
- Direct Web API
- Hazard Data
- Insurance Data
- Listings
- Matrix MLS
- Mortgage Data
- MLS
- OData
- OneHome
- OpenID Connect
- Participant Reporting
- Property Data
- Real Estate
- RESO Data Dictionary
- RESO Web API
- RETS
- Tax Data
- Trestle
website: https://www.cotality.com
---
