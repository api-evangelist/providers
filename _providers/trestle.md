---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.5
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: The primary Trestle interface — a RESO Web API 2.0 / OData 4.0 endpoint that republishes MLS data mapped to the RESO Data Dictionary. The anonymously readable OData service document advertises 18 enti
  name: Trestle RESO Web API
  slug: trestle-reso-web-api
- description: A bidirectional OData interface into the Matrix MLS database, separate from the RESO feed. The CRM reference documents Contacts, EmailHistory, Lists, PortalContents, SavedSearches, UserRegistry and an
  name: Trestle Direct Web API
  slug: trestle-direct-web-api
- description: 'A compliance API that lets technology providers report to each MLS which brokers they hold contracts with — the mechanism by which the licence relationship behind a data feed is evidenced. Documented '
  name: Trestle Participant Reporting API
  slug: trestle-participant-reporting-api
- description: Trestle's legacy Real Estate Transaction Standard interface, documented as compliant with RETS 1.8. RESO no longer updates the RETS specification, but Trestle continues to serve it for customers who c
  name: Trestle RETS
  slug: trestle-rets
artifact_total: 12
collections:
- collection_type: postman
  name: Trestle WebAPI Demonstration
  slug: postman-trestle-webapi
- collection_type: open
  name: API Collection
  slug: open-trestle-odata-service-document
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trestle-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trestle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cotality.com/products/trestle
- group: docs
  title: ''
  type: Documentation
  url: https://trestle-documentation.corelogic.com/
- group: operate
  title: ''
  type: FAQ
  url: https://trestle-documentation.corelogic.com/faq.html
- group: start
  title: ''
  type: SignUp
  url: https://trestle.corelogic.com/SubscriptionWizard
- group: start
  title: ''
  type: Login
  url: https://trestle.corelogic.com/Login
- group: operate
  title: ''
  type: Support
  url: https://www.cotality.com/support
- group: other
  title: ''
  type: Email
  url: mailto:trestlesupport@cotality.com
- group: auth
  title: ''
  type: Certification
  url: https://www.cotality.com/resources/article/corelogic-achieves-reso-data-dictionary-v2-0-vendor-certification
- group: auth
  title: ''
  type: Certification
  url: https://www.reso.org/blog/corelogic-trestle-achieves-reso-platinum-certification-2/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://trestle-documentation.corelogic.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://trestle-documentation.corelogic.com/webapi.html
- group: docs
  title: ''
  type: APIReference
  url: https://trestle-documentation.corelogic.com/webapi-reference.html
- group: company
  title: ''
  type: Blog
  url: https://www.cotality.com/insights
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cotality.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cotality.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cotality.com
- group: operate
  title: ''
  type: Deprecation
  url: https://trestle-documentation.corelogic.com/
- group: auth
  title: ''
  type: Security
  url: https://www.cotality.com/legal/responsible-disclosure-policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trestle-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cotality.com/resources/article/corelogic-achieves-reso-data-dictionary-v2-0-vendor-certification
- group: design
  title: ''
  type: Conformance
  url: conformance/trestle-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trestle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trestle-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/trestle-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trestle-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/trestle-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trestle-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trestle-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trestle-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://trestle-documentation.corelogic.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/trestle-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trestle-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trestle-rate-limits.yml
- group: build
  title: ''
  type: Postman
  url: postman/trestle-webapi.postman_collection.json
- group: build
  title: ''
  type: Examples
  url: examples/trestle-webapi-examples.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trestle-llms.txt
created: '2026-07-26'
description: 'Trestle is the real estate data distribution platform operated by CoreLogic (rebranded Cotality in 2025), sitting between roughly 500 US Multiple Listing Services and the technology providers, brokers and aggregators that consume their listing data. Its home market is the United States. Trestle occupies the licensing-and-transport layer of the residential real estate value chain: it maps each participating MLS into the RESO Data Dictionary and republishes it through a RESO Web API 2.0 / OData 4.0 endpoint and a legacy RETS 1.8 endpoint, plus a bidirectional Direct Web API into the Matrix MLS CRM and a Participant Reporting API used to prove broker relationships back to the MLSs. Its API posture is unusually honest for this sector: the documentation portal at trestle-documentation.corelogic.com is fully public and needs no login, the OAuth2 client-credentials flow and every OData query convention are published openly, and the OData service document at api.cotality.com/trestle/odata
  answers anonymously with a 200. But nothing behind it is reachable. The $metadata document and every entity set return 401 Bearer, and credentials are only issued after a developer registers a Technology Provider or Broker account, requests a connection to a specific multiple listing organization, and completes an e-signed data licence contract that all parties sign — a contract most MLSs will only ratify if a licensed broker or agent sponsors it or the technology provider files periodic participant reports. Trestle is RESO-certified and publicly documented, and still effectively uncallable without a signed licence. Certification is not reachability.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/corelogic.png
layout: provider
mcp_servers:
- description: ''
  name: trestle-mcp.yml
  slug: trestle-mcpyml
modified: '2026-07-26'
name: Trestle
nav: Providers
network: true
overview: 'Trestle publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United States, MLS, RESO, and Property Listings.


  Trestle''s developer surface includes documentation, FAQ, signup flow, support, getting-started guide, API reference, engineering blog, and 32 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 4
  name: Trestle Rate Limits
  slug: trestle-rate-limits
scopes:
- name: Trestle Scopes
  scope_count: 3
  slug: trestle-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.0
  delta: 1.1
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 7.0
    developer_ergonomics: 63.7
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 40.9
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Trestle Authentication
  slug: trestle-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Trestle Domain Security
  slug: trestle-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Trestle Vulnerability Disclosure
  slug: trestle-vulnerability-disclosure
  summary_line: Bugcrowd
slug: trestle
tags:
- Real Estate
- United States
- MLS
- RESO
- Property Listings
- IDX
- PropTech
- Data Distribution
- OData
- RETS
- Listing Syndication
website: https://www.cotality.com/products/trestle
---
