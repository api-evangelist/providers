---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: La Poste Agentic Access
  operation_count: 12
  slug: la-poste-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 1
apis:
- description: Validates, standardises, and enriches postal addresses for users, customers, or prospects in France. Returns CEDEX-normalised address data including street, locality, postcode, and geocoordinates.
  name: La Poste ControlAdresse API
  slug: la-poste-controladresse-api
- description: Returns GPS coordinates for a given French postal address. Enables rapid and simple address geocoding integrated via the Okapi platform.
  name: La Poste Geolocalisation API
  slug: la-poste-geolocalisation-api
- description: Reverse-geocoding API that identifies the five closest French addresses from a given geographic point within a configurable radius.
  name: La Poste Geolocalisation Inversee API
  slug: la-poste-geolocalisation-inversee-api
- description: API for ordering online registered letters (LReL) — La Poste prints, envelopes, franks and distributes the physical letter on behalf of the requester. Uses OAuth2 authentication. Accessible via the Ok
  name: La Poste LReL (Lettre Recommandee en Ligne) API
  slug: la-poste-lrel-lettre-recommandee-en-ligne-api
- description: Enables business applications to send certified documents directly to a recipient's Digiposte digital safe and retrieve authenticated documents with probative value from Digiposte users (v3). Uses OAu
  name: La Poste Digiposte API
  slug: la-poste-digiposte-api
- description: Open data portal powered by OpenDataSoft exposing 18+ datasets including postal office locations, street mailbox listings, postal codes (HEXASMAL), business registrations (SIRENE), and postal tariff t
  name: La Poste dataNOVA Open Data API
  slug: la-poste-datanova-open-data-api
- baseURL: https://api.laposte.fr
  baseurl_source: declared
  description: 'The SlsInternalService : Services destinés aux applications internes API from La Poste — 3 operation(s) for slsinternalservice : services destinés aux applications internes.'
  name: 'La Poste SlsInternalService : Services destinés aux applications internes API'
  slug: la-poste-slsinternalservice-services-destin-s-aux-applications-internes-api
- baseURL: https://api.laposte.fr
  baseurl_source: declared
  description: 'The SlsServiceWS : documentation API from La Poste — 9 operation(s) for slsservicews : documentation.'
  name: 'La Poste SlsServiceWS : documentation API'
  slug: la-poste-slsservicews-documentation-api
artifact_total: 107
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'La Poste SlsInternalService : Services destinés aux applications internes API'
  slug: open-la-poste-slsinternalservice-services-destin-s-aux-applications-internes-api
- collection_type: open
  name: 'La Poste SlsInternalService : Services destinés aux applications internes SlsServiceWS : documentation API'
  slug: open-la-poste-slsservicews-documentation-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/la-poste-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/la-poste-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/la-poste-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/la-poste-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.laposte.fr/
- group: operate
  title: ''
  type: APIStatusPage
  url: https://developer.laposte.fr/status/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.laposte.fr/
- group: auth
  title: ''
  type: Authentication
  url: https://faq.developer.laposte.fr/kb/fr/souscrire-a-une-api-347839
- group: operate
  title: ''
  type: FAQ
  url: https://faq.developer.laposte.fr/
- group: start
  title: ''
  type: GettingStarted
  url: https://faq.developer.laposte.fr/
- group: build
  title: ''
  type: CLI
  url: https://github.com/DeveloperLaPoste/okapi-cli
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DeveloperLaPoste/okapi-sdk-js
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DeveloperLaPoste
created: '2026-06-13'
description: La Poste is the French national postal service, offering a developer platform called Okapi that exposes REST APIs for parcel tracking, address validation, geolocation, registered letter ordering, certified document exchange (Digiposte), and open data access (dataNOVA). APIs require an X-Okapi-Key obtained by registering a free developer account.
examples:
- key_count: 4
  name: Check Generate Label Request
  slug: check-generate-label-request
- key_count: 4
  name: Generate Label Request
  slug: generate-label-request
- key_count: 7
  name: Generate Label Response
  slug: generate-label-response
- key_count: 6
  name: Plan Pickup Request
  slug: plan-pickup-request
finops:
- name: La Poste Finops
  service_category: ''
  slug: la-poste-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/la-poste.png
json_schemas:
- name: ActivationDataFlavor
  property_count: 2
  slug: activationdataflavor
- name: Address
  property_count: 18
  slug: address
- name: Addressee
  property_count: 5
  slug: addressee
- name: AddressPCH
  property_count: 7
  slug: addresspch
- name: AddressPickupLocation
  property_count: 8
  slug: addresspickuplocation
- name: Article
  property_count: 12
  slug: article
- name: BelgiumLabel
  property_count: 4
  slug: belgiumlabel
- name: Category
  property_count: 1
  slug: category
- name: CheckGenerateLabelRequest
  property_count: 6
  slug: checkgeneratelabelrequest
- name: CheckInfoPlanPickupInternalRequest
  property_count: 3
  slug: checkinfoplanpickupinternalrequest
- name: CheckInfoPlanPickupResponse
  property_count: 2
  slug: checkinfoplanpickupresponse
- name: CodeVAS
  property_count: 4
  slug: codevas
- name: CommandInfo
  property_count: 2
  slug: commandinfo
- name: CommandMap
  property_count: 1
  slug: commandmap
- name: Contents
  property_count: 4
  slug: contents
- name: CustomizationField
  property_count: 5
  slug: customizationfield
- name: CustomizationFields
  property_count: 2
  slug: customizationfields
- name: CustomizationTemplate
  property_count: 2
  slug: customizationtemplate
- name: CustomsDeclarations
  property_count: 12
  slug: customsdeclarations
- name: DataHandler
  property_count: 10
  slug: datahandler
- name: DataSource
  property_count: 4
  slug: datasource
- name: ElementVisual
  property_count: 3
  slug: elementvisual
- name: EntityTag
  property_count: 2
  slug: entitytag
- name: Field
  property_count: 2
  slug: field
- name: Fields
  property_count: 2
  slug: fields
- name: GenerateBordereauByParcelsNumbersRequest
  property_count: 4
  slug: generatebordereaubyparcelsnumbersrequest
- name: generateBordereauParcelNumberList
  property_count: 1
  slug: generatebordereauparcelnumberlist
- name: GenerateCN23Request
  property_count: 4
  slug: generatecn23request
- name: GenerateLabelRequest
  property_count: 6
  slug: generatelabelrequest
- name: GenerateLabelRequestV3
  property_count: 6
  slug: generatelabelrequestv3
- name: GenerateLabelRequestV31
  property_count: 6
  slug: generatelabelrequestv31
- name: GenerateLabelV2Response
  property_count: 3
  slug: generatelabelv2response
- name: GetLabelInternalRequest
  property_count: 4
  slug: getlabelinternalrequest
- name: GetLabelRequest
  property_count: 2
  slug: getlabelrequest
- name: GetListMailBoxPickingDatesResponse
  property_count: 4
  slug: getlistmailboxpickingdatesresponse
- name: GetListMailBoxPickingDatesRetourRequest
  property_count: 3
  slug: getlistmailboxpickingdatesretourrequest
- name: GetListMailBoxPickingDatesSender
  property_count: 7
  slug: getlistmailboxpickingdatessender
- name: GetProductInterRequest
  property_count: 9
  slug: getproductinterrequest
- name: GetProductInterResponse
  property_count: 4
  slug: getproductinterresponse
- name: LabelV2Response
  property_count: 6
  slug: labelv2response
- name: Letter
  property_count: 6
  slug: letter
- name: LetterRequestV31
  property_count: 6
  slug: letterrequestv31
- name: Link
  property_count: 7
  slug: link
- name: ListMailBoxPickingDatesRetourOnlineResponse
  property_count: 4
  slug: listmailboxpickingdatesretouronlineresponse
- name: MediaType
  property_count: 5
  slug: mediatype
- name: Message
  property_count: 3
  slug: message
- name: MessageRest
  property_count: 4
  slug: messagerest
- name: MultivaluedMapStringObject
  property_count: 1
  slug: multivaluedmapstringobject
- name: MultivaluedMapStringString
  property_count: 1
  slug: multivaluedmapstringstring
- name: NewCookie
  property_count: 11
  slug: newcookie
- name: Original
  property_count: 4
  slug: original
- name: OutputFormat
  property_count: 6
  slug: outputformat
- name: ParcelRequestV2
  property_count: 15
  slug: parcelrequestv2
- name: ParcelRequestV31
  property_count: 19
  slug: parcelrequestv31
- name: PickupLocation
  property_count: 10
  slug: pickuplocation
- name: PlanPickupRequest
  property_count: 5
  slug: planpickuprequest
- name: PlanPickupResponse
  property_count: 1
  slug: planpickupresponse
- name: PlanPickupSender
  property_count: 12
  slug: planpickupsender
- name: ReplacementValue
  property_count: 4
  slug: replacementvalue
- name: Response
  property_count: 17
  slug: response
- name: ReturnAddressBelgium
  property_count: 3
  slug: returnaddressbelgium
- name: Routing
  property_count: 29
  slug: routing
- name: Sender
  property_count: 2
  slug: sender
- name: Service
  property_count: 13
  slug: service
- name: Site
  property_count: 4
  slug: site
- name: StatusType
  property_count: 3
  slug: statustype
- name: SwissLabel
  property_count: 4
  slug: swisslabel
- name: UriBuilder
  property_count: 0
  slug: uribuilder
- name: XmlV2Response
  property_count: 20
  slug: xmlv2response
- name: ZoneCABRoutage
  property_count: 2
  slug: zonecabroutage
- name: ZoneInfosRoutage
  property_count: 14
  slug: zoneinfosroutage
- name: ZoneRouting
  property_count: 2
  slug: zonerouting
jsonld:
- class_count: 45
  name: context Context
  property_count: 9
  slug: context
layout: provider
modified: '2026-06-13'
name: La Poste
nav: Providers
network: true
overview: 'La Poste publishes 2 APIs on the [APIs.io](https://apis.io/) network: SlsInternalService : Services destinés aux applications internes API and SlsServiceWS : documentation API. Tagged areas include Postal, Parcel Tracking, Address Validation, Geolocation, and Shipping.


  The La Poste catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  La Poste''s developer surface includes developer portal, authentication, FAQ, getting-started guide, CLI, and 8 more developer resources.'
plans:
- name: Colissimo Plans
  plan_count: 1
  slug: colissimo-plans
- name: Controladresse Plans
  plan_count: 2
  slug: controladresse-plans
- name: Datanova Plans
  plan_count: 1
  slug: datanova-plans
- name: Digiposte Plans
  plan_count: 1
  slug: digiposte-plans
- name: Geolocalisation Plans
  plan_count: 2
  slug: geolocalisation-plans
- name: Lrel Plans
  plan_count: 1
  slug: lrel-plans
- name: Suivi Plans
  plan_count: 2
  slug: suivi-plans
random_paper: 7
rate_limits:
- limit_count: 0
  name: Colissimo Rate Limits
  slug: colissimo-rate-limits
- limit_count: 1
  name: Controladresse Rate Limits
  slug: controladresse-rate-limits
- limit_count: 0
  name: Datanova Rate Limits
  slug: datanova-rate-limits
- limit_count: 1
  name: Digiposte Rate Limits
  slug: digiposte-rate-limits
- limit_count: 1
  name: Geolocalisation Rate Limits
  slug: geolocalisation-rate-limits
- limit_count: 1
  name: Lrel Rate Limits
  slug: lrel-rate-limits
- limit_count: 1
  name: Suivi Rate Limits
  slug: suivi-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: La Poste API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: la-poste-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 43.9
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/la-poste/refs/heads/main/screenshots/la-poste-2026-06-20T184234.png
security:
- kind: domain-security
  name: La Poste Domain Security
  slug: la-poste-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: La Poste Vulnerability Disclosure
  slug: la-poste-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: la-poste
tags:
- Postal
- Parcel Tracking
- Address Validation
- Geolocation
- Shipping
- Open Data
- France
website: https://developer.laposte.fr/
---
