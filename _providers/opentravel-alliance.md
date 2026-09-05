---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Opentravel Alliance Agentic Access
  operation_count: 15
  slug: opentravel-alliance-agentic-access
  summary_line: 15 operations · 11 acting
api_count: 8
apis:
- baseURL: http://127.0.0.1/
  baseurl_source: spec
  description: The Facilities API from OpenTravel Alliance — 2 operation(s) for facilities.
  name: OpenTravel Alliance Facilities API
  slug: opentravel-alliance-facilities-api
- baseURL: http://127.0.0.1/
  baseurl_source: spec
  description: The HospitalityFindHospitalityAvailability API from OpenTravel Alliance — 1 operation(s) for hospitalityfindhospitalityavailability.
  name: OpenTravel Alliance Hospitality Find Hospitality Availability API
  slug: opentravel-alliance-hospitalityfindhospitalityavailability-api
- baseURL: http://127.0.0.1/
  baseurl_source: spec
  description: The HospitalityOffers API from OpenTravel Alliance — 1 operation(s) for hospitalityoffers.
  name: OpenTravel Alliance Hospitality Offers API
  slug: opentravel-alliance-hospitalityoffers-api
- baseURL: http://127.0.0.1/
  baseurl_source: spec
  description: The HospitalityPropertyOffers API from OpenTravel Alliance — 1 operation(s) for hospitalitypropertyoffers.
  name: OpenTravel Alliance Hospitality Property Offers API
  slug: opentravel-alliance-hospitalitypropertyoffers-api
- baseURL: http://127.0.0.1/
  baseurl_source: spec
  description: The HospitalityRetrieveFacilityAvailability API from OpenTravel Alliance — 1 operation(s) for hospitalityretrievefacilityavailability.
  name: OpenTravel Alliance Hospitality Retrieve Facility Availability API
  slug: opentravel-alliance-hospitalityretrievefacilityavailability-api
- baseURL: http://127.0.0.1/v1_0
  baseurl_source: spec
  description: The HotelDescriptiveContents API from OpenTravel Alliance — 3 operation(s) for hoteldescriptivecontents.
  name: OpenTravel Alliance Hotel Descriptive Contents API
  slug: opentravel-alliance-hoteldescriptivecontents-api
artifact_total: 37
asyncapis:
- description: ''
  name: Opentravel Alliance Notifications Webhooks
  slug: opentravel-alliance-notifications-webhooks
collections:
- collection_type: open
  name: FacilityResource
  slug: open-opentravel-2018a-facility-resource-defs
- collection_type: open
  name: FacilityResource
  slug: open-opentravel-2018a-facility-resource
- collection_type: open
  name: HospitalityOffersResource
  slug: open-opentravel-2018a-hospitality-offers-resource-defs
- collection_type: open
  name: HospitalityOffersResource
  slug: open-opentravel-2018a-hospitality-offers-resource
- collection_type: open
  name: FacilityResource
  slug: open-opentravel-2020a-facility-resource-defs
- collection_type: open
  name: FacilityResource
  slug: open-opentravel-2020a-facility-resource
- collection_type: open
  name: HotelDescriptiveContentResource
  slug: open-opentravel-2020a-hotel-descriptive-content-resource-defs
- collection_type: open
  name: HotelDescriptiveContentResource
  slug: open-opentravel-2020a-hotel-descriptive-content-resource
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/opentravel-alliance-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/OpenTravel/OpenTravel-Specifications/issues
- group: other
  title: ''
  type: Overlay
  url: overlays/opentravel-alliance-2020a-hotel-descriptive-content-resource-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/opentravel-alliance-hotel-descriptive-content.md
- group: other
  title: ''
  type: Overlay
  url: overlays/opentravel-alliance-2020a-facility-resource-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/opentravel-alliance-facility-resource.md
- group: other
  title: ''
  type: Overlay
  url: overlays/opentravel-alliance-2018a-hospitality-offers-resource-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/opentravel-alliance-hospitality-offers.md
- group: other
  title: ''
  type: Overlay
  url: overlays/opentravel-alliance-2018a-facility-resource-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/opentravel-alliance-hospitality-facility-availability.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opentravel-alliance-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.opentraveldevelopersnetwork.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://opentravel.org/download-otm-tool/
- group: operate
  title: ''
  type: Support
  url: https://opentravel.org/spec-assistance/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.opentraveldevelopersnetwork.com/schema-support
- group: operate
  title: ''
  type: Roadmap
  url: https://www.opentraveldevelopersnetwork.com/all-active-work-public
- group: start
  title: ''
  type: Login
  url: https://www.opentraveldevelopersnetwork.com/user
- group: other
  title: ''
  type: Download
  url: https://www.opentraveldevelopersnetwork.com/schema-products-page
- group: agent
  title: ''
  type: MCPServer
  url: mcp/opentravel-alliance-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/opentravel-alliance-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/opentravel-alliance-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/opentravel-alliance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/opentravel-alliance-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/opentravel-alliance-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/opentravel-alliance-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/opentravel-alliance-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/opentravel-alliance-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/opentravel-alliance-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/opentravel-alliance-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/opentravel-alliance-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/opentravel-alliance-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/opentravel-alliance-notifications-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opentravel-alliance-domain-security.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/opentravel-alliance-vocabulary.yml
- group: build
  title: ''
  type: CLI
  url: cli/opentravel-alliance-cli.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/opentravel-2020a-codelist-4-0-0.schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/opentravel-2020a-codelist-4-1-0.schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/opentravel-2018a-codelist-3-0-0.schema.json
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/OpenTravel/OpenTravel-Specifications/tree/master/OTA2.0/OTA2.0_2018A_ObjectSuite/OpenTravel_2018A_ObjectSuite_Resources/documentation
- group: company
  title: ''
  type: Website
  url: https://opentravel.org/
- group: company
  title: ''
  type: About
  url: https://opentravel.org/about-us/
- group: docs
  title: ''
  type: Specifications
  url: https://opentravel.org/specifications/
- group: docs
  title: ''
  type: Documentation
  url: https://opentravel.org/about-2-0-object-model/
- group: other
  title: ''
  type: Download
  url: https://opentravel.org/download-the-opentravel-specification/
- group: other
  title: ''
  type: Download
  url: https://opentravel.org/download-code-list/
- group: other
  title: ''
  type: Download
  url: https://opentravel.org/download-otm-tool/
- group: other
  title: ''
  type: Repository
  url: https://github.com/OpenTravel/OpenTravel-Specifications
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenTravel
- group: start
  title: ''
  type: Registry
  url: https://opentravelmodel.net/
- group: other
  title: ''
  type: Directory
  url: https://opentravel.org/opentravel-message-adopters-integrators/
- group: commercial
  title: ''
  type: Pricing
  url: https://opentravel.org/membership/
- group: start
  title: ''
  type: SignUp
  url: https://opentravel.org/join-opentravel/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://opentravel.org/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://opentravel.org/privacy-policy/
- group: commercial
  title: ''
  type: License
  url: https://opentravel.org/intellectual-property/
- group: other
  title: ''
  type: Governance
  url: https://opentravel.org/governance/
- group: company
  title: ''
  type: Partners
  url: https://opentravel.org/partners/
- group: company
  title: ''
  type: Blog
  url: https://opentravel.org/announcements/
- group: operate
  title: ''
  type: Contact
  url: https://opentravel.org/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://opentravel.org/frequently-asked-questions/
created: '2026-07-28'
description: 'The OpenTravel Alliance is a volunteer, non-profit travel technology standards body headquartered in Melbourne, Florida, United States. Since 1999 it has published the OpenTravel Specification — the OTA 1.0 XML message suite (releases 2001A through 2024A) and the model-driven OpenTravel 2.0 Object Model (OTM), which generates XML Schema, JSON Schema and Swagger 2.0 resource contracts — plus the OpenTravel Code Lists used across air, hospitality, car rental, cruise, rail, GDS, channel and technology-provider systems. OpenTravel does not operate a booking service or sit in the distribution chain itself; it supplies the message vocabulary that suppliers, GDSs, channel managers and OTAs implement between each other, which makes it a switching-cost reducer rather than a switching-cost holder. Its API posture is honest but thin: there is no OpenTravel-operated runtime API and no public certification registry, though it does run a free self-serve developer portal — the OpenTravel
  Developers Network at opentraveldevelopersnetwork.com — and, as of 2026, an OAuth 2.1 protected Model Context Protocol server on opentravel.org. Specifications are royalty-free and free of charge, but the canonical download is behind a name/company/email lead-capture form with terms acceptance, and the OTM repository and member review periods are membership-gated ($950–$11,250/yr by revenue band). A public, unlicensed GitHub mirror at github.com/OpenTravel/OpenTravel-Specifications carries the bulk of the corpus — including eight Swagger 2.0 resource contracts — and is the only ungated route to machine-readable artifacts. The organization has announced work with the Linux Foundation to form an Open Travel Foundation.'
examples:
- key_count: 1
  name: Opentravel 2018A Hospitality Facility Facilityqueryfacilitysearch
  slug: opentravel-2018a-hospitality-facility-facilityqueryfacilitysearch
- key_count: 1
  name: Opentravel 2018A Hospitality Facility Facilityqueryfindhospitalityavailability
  slug: opentravel-2018a-hospitality-facility-facilityqueryfindhospitalityavailability
- key_count: 1
  name: Opentravel 2018A Hospitality Facility Facilityqueryretrievehospitalityavailability
  slug: opentravel-2018a-hospitality-facility-facilityqueryretrievehospitalityavailability
- key_count: 1
  name: Opentravel 2018A Hospitality Facility Hospitalityfacilities
  slug: opentravel-2018a-hospitality-facility-hospitalityfacilities
- key_count: 1
  name: Opentravel 2018A Hospitality Offers Hospitalityoffersqueryfindhospitalityoffers
  slug: opentravel-2018a-hospitality-offers-hospitalityoffersqueryfindhospitalityoffers
- key_count: 1
  name: Opentravel 2018A Hospitality Offers Multipropertyhospitalityoffers
  slug: opentravel-2018a-hospitality-offers-multipropertyhospitalityoffers
- key_count: 1
  name: Opentravel 2018A Hospitality Offers Singlepropertyhospitalityoffers
  slug: opentravel-2018a-hospitality-offers-singlepropertyhospitalityoffers
image: https://opentravel.org/wp-content/uploads/2025/08/opentravel-favicon2.png
json_schemas:
- name: CodeList
  property_count: 0
  slug: opentravel-2018a-codelist-3-0-0.schema
- name: HospitalityFacility
  property_count: 0
  slug: opentravel-2018a-hospitality-facility-trim.schema
- name: HospitalityOffers
  property_count: 0
  slug: opentravel-2018a-hospitality-offers-trim.schema
- name: CodeList
  property_count: 0
  slug: opentravel-2020a-codelist-4-0-0.schema
- name: CodeList
  property_count: 0
  slug: opentravel-2020a-codelist-4-1-0.schema
- name: Common
  property_count: 0
  slug: opentravel-2020a-common-5-0-0-trim.schema
- name: FacilityResource
  property_count: 0
  slug: opentravel-2020a-facility-resource-trim.schema
- name: HospitalityContent
  property_count: 0
  slug: opentravel-2020a-hospitality-content-hospitality-resources-trim.schema
- name: Organization
  property_count: 0
  slug: opentravel-2020a-organization-4-1-0-trim.schema
- name: OrganizationHospitality
  property_count: 0
  slug: opentravel-2020a-organization-hospitality-4-0-0-trim.schema
layout: provider
mcp_servers:
- description: ''
  name: OAuth 2.1 protected MCP server at https://opentravel.org/wp-json/mcp/mcp-oauth-server
  slug: oauth-21-protected-mcp-server-at-httpsopentravelorgwp-jsonmcpmcp-oauth-server
modified: '2026-07-28'
name: OpenTravel Alliance
nav: Providers
network: true
overview: 'OpenTravel Alliance publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Facilities API, Hospitality Find Hospitality Availability API, Hospitality Offers API, and 3 more. Tagged areas include Travel, United States, Standards, Aviation, and Hospitality.


  The OpenTravel Alliance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  OpenTravel Alliance''s developer surface includes getting-started guide, support, authentication, changelog, CLI, code examples, API reference, and 55 more developer resources.'
random_paper: 5
scopes:
- name: Opentravel Alliance Scopes
  scope_count: 1
  slug: opentravel-alliance-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 50.0
    catalog_earned_first_party: 5.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 19.7
    contract_quality: 58.4
    developer_ergonomics: 54.2
    discoverability: 64.8
    governance: 19.7
    operational_transparency: 31.6
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opentravel-alliance/refs/heads/main/screenshots/opentravel-alliance-2026-08-07T190651.png
security:
- kind: authentication
  name: Opentravel Alliance Authentication
  slug: opentravel-alliance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Opentravel Alliance Domain Security
  slug: opentravel-alliance-domain-security
  summary_line: TLSv1.3 · HSTS
slug: opentravel-alliance
tags:
- Travel
- United States
- Standards
- Aviation
- Hospitality
- Hotels
- Car Rental
- Rail
- Cruise
- Distribution
- GDS
- Booking
- Channel
- XML
- JSON-Schema
website: https://opentravel.org/
---
