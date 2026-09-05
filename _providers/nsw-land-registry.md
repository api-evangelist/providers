---
access_model:
  confidence: high
  label: Broker licence agreement required · wholesale data solutions by commercial contact only · no developer portal
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - terms-of-use
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: A live Cantaloupe Image Server exposing the International Image Interoperability Framework (IIIF) Image API 2.x over the scanned NSW land record images behind the Historical Land Records Viewer. Verif
  name: NSW LRS Historical Land Records Viewer IIIF Image API
  slug: nsw-lrs-hlrv-iiif-image-api
- description: 'An Elasticsearch search proxy that backs the Historical Land Records Viewer and answers anonymously. Verified on 2026-07-26: POST https://api.lrsnative.com.au/hlrv/documents/_msearch with an ndjson bo'
  name: NSW LRS Historical Land Records Viewer Document Search API
  slug: nsw-lrs-hlrv-document-search-api
- description: 'The one documented, publicly callable API NSW Land Registry Services operates. The NSW LRS status page at status.nswlrs.com.au is an Atlassian Statuspage (page id jcfp2nmyt2j4) with the public v2 API '
  name: NSW LRS Status API
  slug: nsw-lrs-status-api
artifact_total: 12
asyncapis:
- description: ''
  name: Nsw Land Registry Status Webhooks
  slug: nsw-land-registry-status-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-nsw-land-registry-hlrv-iiif-image-information
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nsw-land-registry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nsw-land-registry-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nsw-land-registry-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nsw-land-registry-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nsw-land-registry-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nsw-land-registry-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nsw-land-registry-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://nswlrs.com.au/about-us/education-hub/lrs-connect-release-schedule
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nsw-land-registry-glossary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nsw-land-registry-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nsw-land-registry-status-webhooks.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nsw-land-registry-llms.txt
- group: company
  title: ''
  type: Blog
  url: https://nswlrs.com.au/about-us/announcements
- group: start
  title: ''
  type: Login
  url: https://connect.nswlrs.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://nswlrs.com.au/glossary-of-terms
- group: docs
  title: ''
  type: Documentation
  url: https://nswlrs.com.au/current-processing-times
- group: docs
  title: ''
  type: Documentation
  url: https://nswlrs.com.au/forms-guides/guides
- group: docs
  title: ''
  type: Documentation
  url: https://nswlrs.com.au/about-us/education-hub
- group: company
  title: ''
  type: Website
  url: https://nswlrs.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://nswlrs.com.au/services
- group: other
  title: ''
  type: XSD
  url: openapi/nsw-land-registry-eplan-cif-enumerated-types-4-0.xsd
- group: other
  title: ''
  type: Standard
  url: https://nswlrs.com.au/services/plans/digital-plans
- group: start
  title: ''
  type: Portal
  url: https://connect.nswlrs.com.au/
- group: start
  title: ''
  type: Portal
  url: https://online.nswlrs.com.au/
- group: start
  title: ''
  type: Portal
  url: https://hlrv.nswlrs.com.au/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nswlrs.com.au/
- group: commercial
  title: ''
  type: Pricing
  url: https://nswlrs.com.au/services/fees-payments/fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nswlrs.com.au/about-us/policies/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nswlrs.com.au/about-us/policies/privacy-policy
- group: other
  title: ''
  type: Copyright
  url: https://nswlrs.com.au/copyright
- group: operate
  title: ''
  type: Support
  url: https://nswlrs.com.au/about-us/contact-us
- group: docs
  title: ''
  type: Documentation
  url: https://nswlrs.com.au/services/record-searches/how-to-find-an-information-broker
- group: docs
  title: ''
  type: Documentation
  url: https://nswlrs.com.au/data-solutions
- group: docs
  title: ''
  type: Documentation
  url: https://www.registrargeneral.nsw.gov.au/property-and-conveyancing/eConveyancing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nsw-land-registry-services/
created: '2026-07-26'
description: 'NSW Land Registry Services (NSW LRS) operates the Torrens Title Register for New South Wales, Australia''s largest property market, under a concession granted by the NSW Government on 1 July 2017 and held by Australian Registry Investments Pty Ltd (ACN 617 926 020) as trustee for the Australian Registry Investments Trust. It is a privatised operator of a public record: the Registrar General retains the statutory authority and the Office of the Registrar General regulates the concession, while NSW LRS runs the register, examines and registers dealings and plans, and sells access to the resulting data. It sits at the legal foundation of the Australian value chain, beneath the REA Group and Domain portal duopoly, beneath PropTrack and CoreLogic valuation, and beneath PEXA and Sympli, the Electronic Lodgment Network Operators through which every Real Property Act dealing must now be lodged. Its API posture is the sharpest example in this study of a registry that is technically
  modern and commercially closed. There is no developer portal, no developer or docs subdomain, no published API programme, no OpenAPI or Swagger document, no SDK, no Postman workspace and no GitHub organization. One documented, anonymously callable API does exist, and it is not about land: the NSW LRS status page is an Atlassian Statuspage with the public v2 API enabled and referenced at status.nswlrs.com.au/api, publishing 27 components — among them an "API Service" component under Information Broker Services that confirms from the registry''s own mouth that a production API estate sits behind the broker licence — plus RSS and Atom incident feeds and webhook notifications on incident and component changes. Access to the register itself is gated behind a licence: the site states plainly that "Only an information broker we''ve authorised can access our records", and those brokers — InfoTrack, Dye & Durham, Equifax, CITEC Confirm, TriSearch, Landchecker, Fynd, PSI Global and others — "deliver
  and on-sell land titling and related property information through an official licence agreement with NSW LRS". Wholesale data products (Property Alerts, Lease Notifications, Mortgage Insights, Mortgage Verifications) are sold by emailing datasolutions@nswlrs.com.au, with no self-serve path and no published technical contract. What does exist, and what this profile records, are three genuinely reachable machine-readable surfaces that NSW LRS never advertises to developers: a Cantaloupe IIIF Image API 2.0 Level 2 endpoint serving the scanned historical land records behind the Historical Land Records Viewer, an anonymously callable Elasticsearch search proxy over 7,160,622 indexed historical documents, and a publicly downloadable W3C XML Schema for the ICSM ePlan Cadastral Information File enumerated types that pins the NSW LandXML jurisdictional vocabulary now mandatory for digital plan lodgment. The contracts are open; the licence is not — the HLRV terms of use prohibit on-supply, data
  aggregation, republishing and "any device, software or routine to abuse the service of HLRV or emulate human interaction and operation". RESO is entirely absent: NSW LRS appears nowhere in RESO''s certified-organizations list, there is no RESO Web API or Data Dictionary certification, no OData $metadata document and no Universal Property Identifier, which is the expected answer for Australia, where RESO is a North American NAR construct with no adoption. No open, unlicensed dataset is published — NSW LRS is not a publishing organization on data.nsw.gov.au — and a privatised registry selling the public record back through a licensed broker channel is itself the finding. The registry does publish its language: a 257-term glossary of NSW land titling definitions, harvested here as the controlled vocabulary that stands in for the data dictionary it never wrote.'
examples:
- key_count: 1
  name: Nsw Land Registry Hlrv Msearch Response
  slug: nsw-land-registry-hlrv-msearch-response
- key_count: 2
  name: Nsw Land Registry Status Components
  slug: nsw-land-registry-status-components
- key_count: 2
  name: Nsw Land Registry Status Incidents Unresolved
  slug: nsw-land-registry-status-incidents-unresolved
- key_count: 2
  name: Nsw Land Registry Status Scheduled Maintenances Upcoming
  slug: nsw-land-registry-status-scheduled-maintenances-upcoming
- key_count: 2
  name: Nsw Land Registry Status Status
  slug: nsw-land-registry-status-status
image: https://nswlrs.com.au/assets/f/1129775276948026/1a96a055c4/new_nsw-lrs-logo_colour.png
layout: provider
modified: '2026-07-26'
name: NSW Land Registry Services
nav: Providers
network: true
overview: 'NSW Land Registry Services publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Australia, Land Registry, Title, and Conveyancing.


  The NSW Land Registry Services catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  NSW Land Registry Services'' developer surface includes authentication, changelog, code examples, engineering blog, documentation, developer portal, pricing, and 29 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 5.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 33.3
    contract_quality: 48.1
    developer_ergonomics: 45.2
    discoverability: 74.1
    governance: 33.3
    operational_transparency: 39.5
  previous_composite: 49.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nsw-land-registry/refs/heads/main/screenshots/nsw-land-registry-2026-07-27T125345.png
security:
- kind: authentication
  name: Nsw Land Registry Authentication
  slug: nsw-land-registry-authentication
  summary_line: none/contract-gated/session-login · 6 schemes
- kind: domain-security
  name: Nsw Land Registry Domain Security
  slug: nsw-land-registry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: nsw-land-registry
tags:
- Real-Estate
- Australia
- Land Registry
- Title
- Conveyancing
- Property Records
- Torrens Title
- eConveyancing
- Government
- Geospatial
- PropTech
website: https://nswlrs.com.au/
---
