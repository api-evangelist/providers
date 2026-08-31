---
access_model:
  confidence: high
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-08-30'
api_count: 17
apis:
- description: RESTful JSON API returning Zillow property, rental and foreclosure Zestimates for approximately 100 million US properties. Zillow Group documents it on its own developer portal and routes the referenc
  name: Zillow Zestimate API
  slug: zestimates-api
- description: RESTful JSON API over parcel, assessment and transaction records covering roughly 148 million properties across about 3,200 US counties, with around 15 years of history. Documented by Zillow Group and
  name: Zillow Public Records API
  slug: public-records-api
- description: 'RESTful JSON listing API serving MLS and broker data normalized to the RESO Data Dictionary standard. Documented by Zillow Group and served through the Bridge platform, a Zillow Group company. Access '
  name: Zillow Group MLS Listings API
  slug: mls-listings-api
- description: Self-serve API for MLS and broker partners to be notified when a prospect creates a review, retrieve prospect reviews in bulk, and respond to them. Access tokens are issued from the Bridge dashboard u
  name: Zillow Reviews API
  slug: reviews-api
- description: Web-service API returning Zillow agent review data as JSON from URI query-string requests, authenticated with an API key issued on the Bridge dashboard. Governed by the Zillow Data Terms of Use with b
  name: Zillow Agent Reviews API
  slug: agent-reviews-api
- description: 'Read-only mortgage pricing API from Mortech, a Zillow Group company, allowing online lead generators to submit loan criteria over HTTP POST and receive lender pricing back as JSON. Authenticated with '
  name: Mortech Rate Cloud API
  slug: rate-cloud-api
- description: Read/write API from Mortech, a Zillow Group company, for sending and receiving updates on pricing activity for every prospect in the Mortech system. Requests are HTTP POST and responses are XML, authe
  name: Mortech Prospect Sync API
  slug: prospect-sync-api
- description: Mortech prospect trigger API, part of the Zillow Group mortgage developer program alongside Prospect Sync and Rate Cloud. Access is requested through the Zillow Group developer portal under a Partner/
  name: Mortech Prospect Trigger API
  slug: prospect-trigger-api
- description: Read/write API from Mortech, a Zillow Group company, allowing partners to submit prospect information for pricing and lead routing. Requests are HTTP POST and responses are XML, authenticated with a t
  name: Mortech Lead Posting API
  slug: lead-posting-api
- description: Integration API from Mortech, a Zillow Group company, for connecting loan origination systems to Mortech pricing. Listed on the Zillow Group mortgage developer program with a request-access form; no b
  name: Mortech LOS Plug-In Integration API
  slug: los-plug-in-integration-api
- description: API for accessing Zillow lender review data, listed under the Zillow Group mortgage developer program. Access is requested through the Zillow Group developer portal; no base URL or public reference do
  name: Zillow Lender Reviews API
  slug: lender-reviews-api
- description: 'API for retrieving current mortgage rate data, listed under the Zillow Group mortgage developer program. Access is requested through the Zillow Group developer portal; no base URL or public reference '
  name: Zillow Get Current Rates API
  slug: get-current-rates-api
- description: Outbound webhook API that delivers Zillow Rentals lead information to a customer-supplied endpoint as URL-encoded HTTP POST callbacks. Zillow Group states the data format is fixed and that it cannot c
  name: Zillow Rentals Lead API
  slug: rentals-lead-api
- description: Rental listing feed ingestion for property managers and rental software partners, documented under the Zillow Group rentals developer program. A feed-delivery integration rather than a keyed request/r
  name: Zillow Rentals Feed Integrations
  slug: rentals-feed-integrations
- description: RESTful JSON CRUD API for real-estate transaction management - loops, loop details, folders, documents, participants, tasks, activities, contacts and loop templates - secured with three-legged OAuth 2
  name: dotloop Transaction Management API
  slug: transaction-management-api
- description: Zillow housing market metrics - median home values, rents and inventory - published from the national level down to the neighborhood level. Despite being listed as an API on the Zillow Group developer
  name: Zillow Real Estate Metrics
  slug: real-estate-metrics
- description: Aggregate neighborhood-level housing statistics from Zillow, listed on the Zillow Group developer portal but delivered as free CSV downloads through the Zillow Research data portal rather than as a ke
  name: Zillow Neighborhood Data
  slug: neighborhood-data
artifact_total: 24
asyncapis:
- description: ''
  name: Zillow Group Webhooks
  slug: zillow-group-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.zillowgroup.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zillow-group-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zillow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zillow-group
- group: company
  title: ''
  type: Blog
  url: https://www.zillowgroup.com/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zillowgroup.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zillowgroup.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://bridgedataoutput.com/docs/platform
- group: auth
  title: ''
  type: Authentication
  url: authentication/zillow-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zillow-group-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zillow-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zillow-group-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/zillow-group-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zillow-group-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zillow-group-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zillow-group-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zillow-group-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zillow-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.zillow.com/corporate/security-disclosure/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zillow.com/corporate/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zillow.com/corporate/zg-privacy-notice/
- group: operate
  title: ''
  type: Support
  url: https://help.zillowrentalmanager.com/hc/en-us
created: '2025-03-01'
description: Zillow Group is a leading real estate and rental marketplace that aims to make the process of buying, selling, and renting homes more streamlined and efficient. The company offers a wide range of services, including an online platform where users can search for properties, view listings, and connect with real estate agents. Zillow Group also provides tools and resources for homeowners, such as Zestimate, an automated valuation model that estimates the market value of a property.
finops:
- name: Zillow Group Finops
  service_category: API
  slug: zillow-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zillow-group.png
layout: provider
modified: '2026-08-28'
name: Zillow Group
nav: Providers
network: true
overview: 'Zillow Group publishes 17 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Property Data, MLS, Mortgage, and Rentals.


  The Zillow Group catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zillow Group''s developer surface includes engineering blog, documentation, API reference, authentication, support, and 17 more developer resources.'
plans:
- name: Zillow Group Plans Pricing
  plan_count: 0
  slug: zillow-group-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Zillow Group Rate Limits
  slug: zillow-group-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 45.2
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 40.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zillow-group/refs/heads/main/screenshots/zillow-group-2026-06-20T201913.png
security:
- kind: authentication
  name: Zillow Group Authentication
  slug: zillow-group-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Zillow Group Domain Security
  slug: zillow-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zillow Group Vulnerability Disclosure
  slug: zillow-group-vulnerability-disclosure
  summary_line: Bugcrowd
slug: zillow-group
tags:
- Real-Estate
- Property Data
- MLS
- Mortgage
- Rentals
- Valuation
- Housing-Data
- Transaction Management
website: https://www.zillowgroup.com/
---
