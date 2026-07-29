---
access_model:
  confidence: high
  label: Open Government Licence open data (no key) · self-serve API key for dataset service · licence + client certificate for Business Gateway
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - documentation
  - authentication
  - terms-of-use
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Hm Land Registry Agentic Access
  operation_count: 29
  slug: hm-land-registry-agentic-access
  summary_line: 29 operations · 11 acting
api_count: 10
apis:
- description: Live SPARQL 1.1 query endpoint over HM Land Registry's open linked data — Price Paid Data transaction records for every property sale in England and Wales lodged for registration, and the UK House Pri
  name: HM Land Registry Open Data SPARQL API
  slug: hm-land-registry-open-data-sparql-api
- description: W3C Linked Data API over the Price Paid Data dataset, exposing every property sale in England and Wales sold for value and lodged for registration since 1995. Resources resolve at /data/ppi/ with cont
  name: HM Land Registry Price Paid Data Linked Data API
  slug: hm-land-registry-price-paid-linked-data-api
- description: W3C Linked Data API over the UK House Price Index, the official house price statistic calculated by the Office for National Statistics from HM Land Registry, Registers of Scotland and Land and Propert
  name: UK House Price Index Linked Data API
  slug: uk-house-price-index-linked-data-api
- description: RESTful JSON API for the Use land and property data service, used to list the HM Land Registry bulk datasets available in the service, read dataset metadata and resources, and mint a signed S3 downloa
  name: Use Land and Property Data API
  slug: use-land-and-property-data-api
- description: The Business Gateway REST API through which conveyancers and their case management systems lodge applications to change the land register, upload and download supporting documents, add attachments and
  name: Business Gateway Submit an Application to Change the Land Register API
  slug: business-gateway-submit-an-application-to-change-the-register-api
- description: RESTful expansion of the long-standing Official Search of Whole SOAP service. An official search with priority by a purchaser against the whole of a registered title or a pending first registration ap
  name: Business Gateway Official Search of Whole (with Priority) with Data API
  slug: business-gateway-official-search-of-whole-with-data-api
- description: Returns OC1 document availability (title register and title plan) and a collection of OC2 document availability (documents referred to in the register) for a given title number, so a case management s
  name: Business Gateway Official Copy Document Availability Service
  slug: business-gateway-official-copy-document-availability-api
- description: Returns the registered proprietor names recorded against a supplied title number — the authoritative answer to "who owns this". Single GET operation on /titles/{title_number}/registered-proprietor-nam
  name: Business Gateway Registered Proprietor Names Service
  slug: business-gateway-registered-proprietor-names-api
- description: Returns HM Land Registry's estimated completion date for a lodged application, given its application reference, so a conveyancer's system can set client expectations on how long a registration will ta
  name: Business Gateway Estimate Completion Date API
  slug: business-gateway-estimate-completion-date-api
- description: An OpenAPI 3.0.1 contract, version 6.0.0, titled "Land Register API" and published in the public Business Gateway developer pack. It describes two GET operations — /title/{titleNumber} and /draft-titl
  name: Land Register API
  slug: land-register-api
artifact_total: 33
asyncapis:
- description: Event surface of the HM Land Registry Business Gateway. As an application to change the Land Register moves through HMLR processing, HMLR raises notifications about it. Business units retrieve their n
  name: HM Land Registry Business Gateway Notifications
  slug: hm-land-registry-business-gateway-notifications-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hm-land-registry-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hm-land-registry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hm-land-registry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hm-land-registry-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.gov.uk/government/organisations/land-registry
- group: docs
  title: ''
  type: Documentation
  url: https://landregistry.github.io/bgtechdoc/
- group: docs
  title: ''
  type: Documentation
  url: https://use-land-property-data.service.gov.uk/api-information
- group: docs
  title: ''
  type: APIReference
  url: https://use-land-property-data.service.gov.uk/api-documentation
- group: auth
  title: ''
  type: Authentication
  url: https://landregistry.github.io/bgtechdoc/rest/get_started/developer_guide/index.html
- group: other
  title: ''
  type: OpenData
  url: https://landregistry.data.gov.uk/
- group: other
  title: ''
  type: OpenData
  url: https://www.gov.uk/land-registry-public-data
- group: other
  title: ''
  type: BulkData
  url: https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads
- group: commercial
  title: ''
  type: TermsOfService
  url: https://use-land-property-data.service.gov.uk/service-terms-of-use
- group: commercial
  title: ''
  type: License
  url: https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
- group: start
  title: ''
  type: SignUp
  url: https://use-land-property-data.service.gov.uk/registration
- group: start
  title: ''
  type: Onboarding
  url: https://www.gov.uk/guidance/direct-integration-with-business-gateway
- group: start
  title: ''
  type: Onboarding
  url: https://www.gov.uk/guidance/hm-land-registry-business-gateway
- group: other
  title: ''
  type: DeveloperPack
  url: https://www.gov.uk/guidance/business-gateway-developer-pack
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LandRegistry
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/LandRegistry/bgtechdoc
- group: other
  title: ''
  type: Glossary
  url: https://landregistry.github.io/bgtechdoc/support/glossary/
- group: operate
  title: ''
  type: Support
  url: https://use-land-property-data.service.gov.uk/contact
- group: other
  title: ''
  type: Accessibility
  url: https://use-land-property-data.service.gov.uk/accessibility-statement
- group: build
  title: ''
  type: Packages
  url: packages/hm-land-registry-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hm-land-registry-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hm-land-registry-gov-uk-security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hm-land-registry-use-land-property-data-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/hm-land-registry-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hm-land-registry-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hm-land-registry-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/hm-land-registry-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hm-land-registry-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hm-land-registry-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hm-land-registry-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/hm-land-registry-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hm-land-registry-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hm-land-registry-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/hm-land-registry-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hm-land-registry-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hm-land-registry-ppi.ttl
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hm-land-registry-ukhpi.ttl
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/hm-land-registry-common.ttl
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.gov.uk/guidance/report-a-vulnerability-on-an-hm-land-registry-service-or-system
- group: start
  title: ''
  type: DeveloperPortal
  url: https://landregistry.github.io/bg-dev-pack-redesign/
- group: docs
  title: ''
  type: Documentation
  url: https://landregistry.github.io/bg-dev-pack-redesign/
- group: docs
  title: ''
  type: APIReference
  url: https://landregistry.github.io/bg-dev-pack-redesign/find-a-service-api
- group: start
  title: ''
  type: GettingStarted
  url: https://landregistry.github.io/bg-dev-pack-redesign/how-to-access-business-gateway
- group: start
  title: ''
  type: GettingStarted
  url: https://landregistry.github.io/bgtechdoc/rest/get_started/developer_guide/index.html
- group: company
  title: ''
  type: Blog
  url: https://hmlandregistry.blog.gov.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gov.uk/guidance/hm-land-registry-registration-services-fees
- group: start
  title: ''
  type: SignUp
  url: https://www.gov.uk/guidance/apply-for-hm-land-registry-business-e-services
- group: commercial
  title: ''
  type: TermsOfService
  url: https://landregistry.github.io/bg-dev-pack-redesign/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gov.uk/government/organisations/land-registry/about/personal-information-charter
- group: operate
  title: ''
  type: Support
  url: https://landregistry.github.io/bg-dev-pack-redesign/contact-us
- group: operate
  title: ''
  type: Support
  url: https://www.gov.uk/guidance/join-the-business-gateway-community
- group: other
  title: ''
  type: Glossary
  url: https://landregistry.github.io/bg-dev-pack-redesign/glossary
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/LandRegistry/bg-dev-pack-redesign
- group: design
  title: ''
  type: Testing
  url: https://landregistry.github.io/bg-dev-pack-redesign/a-guide-to-testing
created: '2026-07-26'
description: 'HM Land Registry is the non-ministerial government department that registers the ownership of land and property in England and Wales, guaranteeing title to more than 26 million registered estates. In a United Kingdom market that has no MLS and no cooperative listing standard — residential listings are controlled by the Rightmove and Zoopla duopoly and reach them through agency CRM software — HMLR is the counterweight, and it sits at the legal foundation of the value chain rather than at the consumer end: it is the authoritative source of who owns what, what it sold for, and where its boundaries are, and every conveyancing transaction in England and Wales terminates at its register. Its API posture is genuinely and unusually good for a registry, but it is split into three tiers that should never be conflated. First, a real open layer: the landregistry.data.gov.uk platform serves a live, anonymous, unauthenticated SPARQL 1.1 endpoint plus a W3C Linked Data API over Price Paid
  Data and the UK House Price Index, with JSON/CSV/Turtle content negotiation, alongside bulk Price Paid CSVs and INSPIRE index polygons — all under the Open Government Licence v3.0 with no signup, no key and no fee. Second, a self-serve keyed tier: the Use land and property data service issues an API key automatically on account creation and exposes a documented REST API for dataset metadata and signed download URLs, but the datasets behind it require a signed licence per dataset and some are chargeable — the Registered Leases commercial licence is £5,000 a year plus VAT, and the National Polygon Service, which holds the title boundary polygons and the title number to UPRN lookup, is £20,000 a year plus VAT. A state registry selling the spatial extent of the public record back to the public is the finding, and it is recorded here plainly. Third, the Business Gateway: the B2B channel that conveyancers and their case management systems use to submit applications to change the register, order
  official copies and run priority searches. Its developer pack is fully public on GitHub Pages with eight downloadable OpenAPI 3.0/3.1 contracts and 37 SOAP XSDs, but the production host businessgateway.landregistry.gov.uk will not complete a TLS handshake without an HMLR-issued client certificate, and access requires signing a development licence and holding a business e-services account. There is no RESO Web API certification, no RESO Data Dictionary, no OData $metadata document and no Universal Property Identifier anywhere in HMLR''s stack — RESO is a North American NAR construct with no UK adoption, and HMLR''s machine-readable contracts are OpenAPI, XSD and W3C linked data instead.'
examples:
- key_count: 5
  name: Hm Land Registry Application Information 1.0 Test Stubs
  slug: hm-land-registry-application-information-1.0-test-stubs
- key_count: 5
  name: Hm Land Registry Attach A Document 1.0 Test Stubs
  slug: hm-land-registry-attach-a-document-1.0-test-stubs
- key_count: 5
  name: Hm Land Registry Attach A Message 1.0 Test Stubs
  slug: hm-land-registry-attach-a-message-1.0-test-stubs
- key_count: 5
  name: Hm Land Registry Notifications 1.0 Test Stubs
  slug: hm-land-registry-notifications-1.0-test-stubs
- key_count: 5
  name: Hm Land Registry Send A Document 1.0 Test Stubs
  slug: hm-land-registry-send-a-document-1.0-test-stubs
- key_count: 5
  name: Hm Land Registry Submit An Application 1.0 Test Stubs
  slug: hm-land-registry-submit-an-application-1.0-test-stubs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
json_schemas:
- name: Hm Land Registry Application Accepted Priority Pending
  property_count: 1
  slug: hm-land-registry-application-accepted-priority-pending
- name: Hm Land Registry Application Accepted Priority Protected
  property_count: 1
  slug: hm-land-registry-application-accepted-priority-protected
- name: Hm Land Registry Application Attachment Failed
  property_count: 1
  slug: hm-land-registry-application-attachment-failed
- name: Hm Land Registry Application Attachment Success
  property_count: 1
  slug: hm-land-registry-application-attachment-success
- name: Hm Land Registry Application Cancelled
  property_count: 1
  slug: hm-land-registry-application-cancelled
- name: Hm Land Registry Application Completed
  property_count: 1
  slug: hm-land-registry-application-completed
- name: Hm Land Registry Application Correspondence Despatched
  property_count: 1
  slug: hm-land-registry-application-correspondence-despatched
- name: Hm Land Registry Application Error
  property_count: 1
  slug: hm-land-registry-application-error
- name: Hm Land Registry Application Message Failed
  property_count: 1
  slug: hm-land-registry-application-message-failed
- name: Hm Land Registry Application Message Success
  property_count: 1
  slug: hm-land-registry-application-message-success
- name: Hm Land Registry Application Validation Failed
  property_count: 1
  slug: hm-land-registry-application-validation-failed
layout: provider
mcp_servers:
- description: ''
  name: hm-land-registry-mcp.yml
  slug: hm-land-registry-mcpyml
modified: '2026-07-26'
name: HM Land Registry
nav: Providers
network: true
overview: 'HM Land Registry publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Use Land and Property Data API, Business Gateway Submit an Application to Change the Land Register API, Business Gateway Official Search of Whole (with Priority) with Data API, and 4 more. Tagged areas include Real Estate, United Kingdom, Land Registry, Open Data, and Title.


  The HM Land Registry catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HM Land Registry''s developer surface includes authentication, documentation, API reference, signup flow, support, sandbox, changelog, and 53 more developer resources.'
random_paper: 67
score:
  band: strong
  composite: 56.2
  delta: -3.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 77.8
    developer_ergonomics: 62.5
    discoverability: 83.3
    governance: 21.9
    operational_transparency: 31.6
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 36.4
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Hm Land Registry Authentication
  slug: hm-land-registry-authentication
  summary_line: http/apiKey/none · 5 schemes
- kind: domain-security
  name: Hm Land Registry Domain Security
  slug: hm-land-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hm Land Registry Vulnerability Disclosure
  slug: hm-land-registry-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hm-land-registry
tags:
- Real Estate
- United Kingdom
- Land Registry
- Open Data
- Title
- Conveyancing
- Property Records
- Price Paid Data
- Linked Data
- Geospatial
- Government
- PropTech
website: https://www.gov.uk/government/organisations/land-registry
---
