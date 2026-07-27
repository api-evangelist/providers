---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 40.4
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: FBS's proprietary REST API over Flexmls MLS content. Documented services include Listings (plus photos, documents, floor plans, videos, virtual tours, open houses, rooms, units, history and rules), Co
  name: Spark API
  slug: spark-api
- description: Spark's implementation of the RESO Web API, exposed as an OData service at the /Reso/OData endpoint and serving data shaped by the RESO Data Dictionary. Version 3 is the recommended service root; vers
  name: Spark RESO Web API
  slug: spark-reso-web-api
- description: 'Outbound webhook delivery from the Spark platform. When a Property, Member or Office record changes in an upstream MLS, Spark POSTs a RESO Web API Entity Event payload over HTTPS to a subscriber URL, '
  name: Spark Webhooks
  slug: spark-webhooks
artifact_total: 9
asyncapis:
- description: ''
  name: Spark Platform Webhooks
  slug: spark-platform-webhooks
collections:
- collection_type: postman
  name: Spark Web API Queries
  slug: postman-spark-platform-spark-web-api-queries
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spark-platform-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sparkapi.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sparkplatform.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://sparkplatform.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://sparkplatform.com/docs/api_services/read_first
- group: start
  title: ''
  type: GettingStarted
  url: https://sparkplatform.com/docs/overview/set_up_access
- group: operate
  title: ''
  type: Support
  url: https://www.sparkapi.io/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.sparkapi.io/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.sparkapi.io/feed/
- group: start
  title: ''
  type: SignUp
  url: https://sparkplatform.com/register/developers
- group: start
  title: ''
  type: Login
  url: https://sparkplatform.com/ticket
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sparkapi
- group: auth
  title: ''
  type: Authentication
  url: https://sparkplatform.com/docs/authentication/authentication
- group: auth
  title: ''
  type: Authentication
  url: authentication/spark-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spark-platform-scopes.yml
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: authentication/spark-platform-openid-configuration.json
- group: other
  title: ''
  type: JSONWebKeySet
  url: authentication/spark-platform-openid-jwks.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spark-platform-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/spark-platform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spark-platform-packages.yml
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/25548936/2s935snM26
- group: build
  title: ''
  type: PostmanCollection
  url: postman/spark-platform-spark-web-api-queries.postman_collection.json
- group: build
  title: ''
  type: Examples
  url: examples/spark-platform-request-examples.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spark-platform-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spark-platform-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spark-platform-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spark-platform-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spark-platform-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/spark-platform-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spark-platform-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spark-platform-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://services.reso.org/orgs?showStats=true&showEndorsements=true
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spark-platform-llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sparkplatform.com/docs/terms_of_use/developer_agreement_and_terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sparkplatform.com/docs/terms_of_use/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sparkapi.io/developers/
- group: auth
  title: ''
  type: Certification
  url: https://services.reso.org/orgs?showStats=true&showEndorsements=true
created: '2026-07-26'
description: 'Spark Platform is the MLS data platform built by FBS, a 100% employee-owned company in Fargo, North Dakota that has served the US Multiple Listing Service industry for over 30 years and operates the Flexmls MLS system for more than 120 MLS organizations. Spark sits in the distribution layer of US residential real estate: it takes MLS content out of Flexmls and exposes it to third-party developers through two documented interfaces — the proprietary Spark API (https://sparkapi.com/v1, SparkQL filtering, listings, contacts, saved searches, market statistics, portals/VOW accounts) and a RESO Web API implementation at the /Reso/OData endpoint (https://replication.sparkapi.com/Version/3/Reso/OData/) serving Property, Member, Office, Media, OpenHouse, Room, Unit, GreenVerification, PowerProduction and Lookup resources against the RESO Data Dictionary. FBS is a RESO Certified technology provider (Unique Organization Identifier T00000052, status "Certified Current") and appears as the
  certifying provider on RESO Web API Core 2.0.0 and Data Dictionary 1.7 / 2.0 endorsements for 138 MLS organizations plus one commercial board in the public RESO organizations feed; FBS itself additionally holds RESO webhooks 1.0.0 and RESO Common Format 2.0 endorsements. The API posture must be stated honestly: the documentation is genuinely public and unusually complete, developer registration is a free public form, and the endpoints are live — but they are not open. Every probed data endpoint, including the OData $metadata document, returns HTTP 401 "Invalid API key and/or request signed improperly" anonymously. Real data requires a Developer Agreement with FBS, an MLS-approved data plan purchased through the Spark Datamart under an IDX, VOW or Private role, and a per-MLS fee. Certification here is real and verifiable; reachability is licensed. Home market is the United States.'
image: https://www.sparkapi.io/wp-content/uploads/2023/07/cropped-Spark_Pin_Favicon-192x192.png
layout: provider
modified: '2026-07-26'
name: Spark Platform
nav: Providers
network: true
overview: 'Spark Platform publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United States, MLS, RESO, and Property Listings.


  The Spark Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spark Platform''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 30 more developer resources.'
random_paper: 31
rate_limits:
- limit_count: 4
  name: Spark Platform Rate Limits
  slug: spark-platform-rate-limits
scopes:
- name: Spark Platform Scopes
  scope_count: 7
  slug: spark-platform-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: thin
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 22.6
    developer_ergonomics: 63.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 44.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Spark Platform Authentication
  slug: spark-platform-authentication
  summary_line: http-bearer/oauth2/openIdConnect/saml/apiKey-signed · 4 schemes
- kind: domain-security
  name: Spark Platform Domain Security
  slug: spark-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spark-platform
tags:
- Real Estate
- United States
- MLS
- RESO
- Property Listings
- IDX
- PropTech
- Listing Data Infrastructure
- OData
website: https://www.sparkapi.io/
---
