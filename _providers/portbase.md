---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 149
  human_in_the_loop: 3
  name: Portbase Agentic Access
  operation_count: 213
  slug: portbase-agentic-access
  summary_line: 213 operations · 149 acting · 3 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: Manage and retrieve bookings for an organisation
  name: Portbase Bookings API
  slug: portbase-bookings-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Cargo Controller Import API API from Portbase — 2 operation(s) for cargo controller import api.
  name: Portbase Cargo Controller Import API
  slug: portbase-cargo-controller-import-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Commercial Release API API from Portbase — 6 operation(s) for commercial release api.
  name: Portbase Commercial Release API
  slug: portbase-commercial-release-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: This is a API for sending Bill of Ladings.
  name: Portbase Consignments API
  slug: portbase-consignments-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Event API API from Portbase — 1 operation(s) for event api.
  name: Portbase Event API
  slug: portbase-event-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Forwarder API API from Portbase — 3 operation(s) for forwarder api.
  name: Portbase Forwarder API
  slug: portbase-forwarder-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Harbour Dues API API from Portbase — 1 operation(s) for harbour dues api.
  name: Portbase Harbour Dues API
  slug: portbase-harbour-dues-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: This endpoint can be used by the integral planner Nextlogic to update the planning information.
  name: Portbase Integral Planning API
  slug: portbase-integral-planning-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: API for the declarant to create, update, move, detach or cancel attached handlings (handlings that are connected to a visit and voyage).
  name: Portbase Operator API - handlings API
  slug: portbase-operator-api-handlings-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Operator API - rail-only API from Portbase — 1 operation(s) for operator api - rail-only.
  name: Portbase Operator API - rail-only API
  slug: portbase-operator-api-rail-only-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Operator API - road-only API from Portbase — 4 operation(s) for operator api - road-only.
  name: Portbase Operator API - road-only API
  slug: portbase-operator-api-road-only-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: Endpoint to create new visits by a declarant, update, move or cancel them. A special operation to indicate the load-discharge list is finalized is also available, to let the terminal know that after r
  name: Portbase Operator API - visits API
  slug: portbase-operator-api-visits-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: API for the declarant to create new voyages, update or cancel them. Special operations are also available to indicate that the voyage contains visits where restrictions apply (i.e. due to reefers).
  name: Portbase Operator API - voyages API
  slug: portbase-operator-api-voyages-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: Api defining the operations a terminal/barge operator can do to retrieve organisation configuration. Basically these operations retrieve configuration data such as bollards, fixedwindows etc.
  name: Portbase Organisation Data API
  slug: portbase-organisation-data-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Port Authority API API from Portbase — 18 operation(s) for port authority api.
  name: Portbase Port Authority API
  slug: portbase-port-authority-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Port Call Optimization API API from Portbase — 1 operation(s) for port call optimization api.
  name: Portbase Port Call Optimization API
  slug: portbase-port-call-optimization-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Port to Port API API from Portbase — 3 operation(s) for port to port api.
  name: Portbase Port to Port API
  slug: portbase-port-to-port-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: Portbase uses reference data within the API calls for instance barges, shipping companies, container sizetypes etc. With this Reference Data API you can retrieve the data to be used in the API calls f
  name: Portbase Reference Data API
  slug: portbase-reference-data-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: Deprecated Road API. Please upgrade to Operator API endpoints.
  name: Portbase Road API V1 API
  slug: portbase-road-api-v1-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: Deprecated Road API. Please upgrade to Operator API endpoints.
  name: Portbase Road API V2 API
  slug: portbase-road-api-v2-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Secure Chain API API from Portbase — 2 operation(s) for secure chain api.
  name: Portbase Secure Chain API
  slug: portbase-secure-chain-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Ship Operator API - other API from Portbase — 5 operation(s) for ship operator api - other.
  name: Portbase Ship Operator API - other API
  slug: portbase-ship-operator-api-other-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: This api can be used for settling the terminal planning with the stevedores. <br>The happy flow consists preferably of the next steps:<ul> <li>declare terminal plannings</li> <li>update terminal plann
  name: Portbase Ship Operator API - terminal planning API
  slug: portbase-ship-operator-api-terminal-planning-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Ship Operator API - visit API from Portbase — 6 operation(s) for ship operator api - visit.
  name: Portbase Ship Operator API - visit API
  slug: portbase-ship-operator-api-visit-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Ship to Shore API API from Portbase — 2 operation(s) for ship to shore api.
  name: Portbase Ship to Shore API
  slug: portbase-ship-to-shore-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Terminal API API from Portbase — 1 operation(s) for terminal api.
  name: Portbase Terminal API
  slug: portbase-terminal-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: Api defining the operations a terminal can do for handlings. Basically these operations supply feedback to the declarant about the status of the handling.
  name: Portbase Terminal API - handlings API
  slug: portbase-terminal-api-handlings-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: Api defining the operations a terminal can do to respond on visit requests from the declarant. The terminal supplies feedback if a visit is accepted and can be planned, rejected or completed.
  name: Portbase Terminal API - visits API
  slug: portbase-terminal-api-visits-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: This API can be used to receive **real-time** updates about the voyages, visits and (detached) handlings. To achieve these real-time updates the API uses a mechanism called 'long polling'. When you se
  name: Portbase Tracking API
  slug: portbase-tracking-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Traction Supplier API API from Portbase — 1 operation(s) for traction supplier api.
  name: Portbase Traction Supplier API
  slug: portbase-traction-supplier-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Waste Collector API API from Portbase — 4 operation(s) for waste collector api.
  name: Portbase Waste Collector API
  slug: portbase-waste-collector-api-api
- baseURL: https://api.cargo-controller-export.pcs.portbase.com/api
  baseurl_source: declared
  description: The Webhook Events API from Portbase — 0 operation(s) for webhook events.
  name: Portbase Webhook Events API
  slug: portbase-webhook-events-api
artifact_total: 71
asyncapis:
- description: ''
  name: Portbase Webhooks
  slug: portbase-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/portbase/well-known/portbase-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/portbase-status-security.txt
- group: auth
  href: https://artifacts.apis.io/portbase/well-known/portbase-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/portbase-security.txt
- group: auth
  href: https://artifacts.apis.io/portbase/well-known/portbase-portbase-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/portbase-portbase-security.txt
- group: build
  href: https://artifacts.apis.io/portbase/integrations/portbase-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/portbase-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/portbase/agentic-access/portbase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/portbase-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/portbase/rules/portbase-rules.yml
  title: ''
  type: Spectral
  url: rules/portbase-rules.yml
- group: design
  href: https://artifacts.apis.io/portbase/json-ld/portbase-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/portbase-context.jsonld
- group: design
  href: https://artifacts.apis.io/portbase/vocabulary/portbase-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/portbase-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/portbase/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/portbase/asyncapi/portbase-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/portbase-webhooks.yml
- group: design
  href: https://artifacts.apis.io/portbase/data-model/portbase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/portbase-data-model.yml
- group: operate
  href: https://artifacts.apis.io/portbase/changelog/portbase-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/portbase-changelog.yml
- group: design
  href: https://artifacts.apis.io/portbase/conventions/portbase-conventions.yml
  title: ''
  type: Conventions
  url: conventions/portbase-conventions.yml
- group: auth
  href: https://artifacts.apis.io/portbase/security/portbase-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/portbase-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/portbase/lifecycle/portbase-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/portbase-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/portbase/errors/portbase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/portbase-problem-types.yml
- group: design
  href: https://artifacts.apis.io/portbase/conformance/portbase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/portbase-conformance.yml
- group: other
  href: https://artifacts.apis.io/portbase/overlays/portbase-cargo-controller-export-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/portbase-cargo-controller-export-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/portbase/well-known/portbase-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/portbase-well-known.yml
- group: other
  href: https://artifacts.apis.io/portbase/hosts/portbase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/portbase-hosts.yml
- group: other
  href: https://artifacts.apis.io/portbase/vendors/portbase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/portbase-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.portbase.com/en/news/interview-goreefers/
- group: auth
  href: https://artifacts.apis.io/portbase/authentication/portbase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/portbase-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.portbase.com/en/
- group: auth
  href: https://artifacts.apis.io/portbase/security/portbase-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/portbase-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/portbase/security/portbase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/portbase-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.portbase.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.portbase.com/en/community-solutions/getting-started-with-portbase/system-links/
- group: operate
  title: ''
  type: Support
  url: https://support.portbase.com/hc/en-gb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.portbase.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.portbase.com/en/release-notes/
- group: company
  title: ''
  type: Blog
  url: https://www.portbase.com/en/news-knowledge/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.portbase.com/en/community-solutions/costs/
- group: start
  title: ''
  type: SignUp
  url: https://www.portbase.com/en/register/
- group: start
  title: ''
  type: Login
  url: https://login.pcs.portbase.com/?lang=en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.portbase.com/en/general-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.portbase.com/en/privacy-statement/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/portbase
- group: operate
  title: ''
  type: Contact
  url: https://www.portbase.com/en/contact/
created: '2026-10-18'
description: Portbase is the Port Community System (PCS) organisation of the Port of Rotterdam Authority and the Port of Amsterdam, digitally connecting the Dutch port community - terminals, shipping companies, transporters, forwarders and government - so that goods and data flows through the Dutch ports and connected chains run efficiently, sustainably and securely. It offers web services and system interfaces (APIs, AS2, sFTP, SMTP and webhooks) for services such as Cargo Controller Import/Export, notifications and cargo declarations, documented in its support centre.
image: https://www.portbase.com/wp-content/uploads/2024/04/20180206-_H4A8907-1-scaled.jpg
json_schemas:
- name: ApiOrganisationBL
  property_count: 8
  slug: portbase-api-organisation-bl
- name: BatchTrackRequest
  property_count: 1
  slug: portbase-batch-track-request
- name: BookingDossier
  property_count: 6
  slug: portbase-booking-dossier
- name: InputCommercialReleaseData
  property_count: 13
  slug: portbase-com-portbase-bezoekschip-common-api-commercialrelease-input-input-commercial-release-data
- name: BezoekschipOrganisation
  property_count: 19
  slug: portbase-com-portbase-bezoekschip-common-api-common-authentication-bezoekschip-organisation
- name: GetAnyUpdates
  property_count: 7
  slug: portbase-com-portbase-bezoekschip-common-api-common-get-any-updates
- name: Visit
  property_count: 22
  slug: portbase-com-portbase-bezoekschip-common-api-external-visit-api-visit
- name: GetVisitUpdates
  property_count: 5
  slug: portbase-com-portbase-bezoekschip-common-api-visit-get-visit-updates
- name: ContainerListItem
  property_count: 17
  slug: portbase-container-list-item
- name: EquipmentCreateRequest
  property_count: 14
  slug: portbase-equipment-create-request
- name: EquipmentUpdateRequest
  property_count: 14
  slug: portbase-equipment-update-request
- name: GetHinterlandUpdates
  property_count: 5
  slug: portbase-get-hinterland-updates
- name: GetRoadVoyageUpdates
  property_count: 5
  slug: portbase-get-road-voyage-updates
- name: ImportConsignment
  property_count: 10
  slug: portbase-import-consignment
- name: Shipment
  property_count: 6
  slug: portbase-shipment
- name: SubscribeDto
  property_count: 3
  slug: portbase-subscribe-dto
- name: SubscriptionId
  property_count: 1
  slug: portbase-subscription-id
- name: Terminal
  property_count: 24
  slug: portbase-terminal
- name: TrackResponse
  property_count: 3
  slug: portbase-track-response
- name: TransferRequest
  property_count: 3
  slug: portbase-transfer-request
jsonld:
- class_count: 120
  name: Portbase Context
  property_count: 295
  slug: portbase-context
layout: provider
modified: '2026-10-18'
name: Portbase
nav: Providers
network: true
overview: 'Portbase publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bookings API, Cargo Controller Import API, Commercial Release API, and 29 more. Tagged areas include Company, Port Community System, Logistics, Maritime, and Shipping.


  The Portbase catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Portbase''s developer surface includes changelog, authentication, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Portbase Plans Pricing
  plan_count: 0
  slug: portbase-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Portbase Rate Limits
  slug: portbase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Portbase API Rules
  rule_count: 60
  severity_counts:
    error: 42
    hint: 0
    info: 3
    warn: 15
  slug: portbase-rules
scopes:
- name: Portbase Scopes
  scope_count: 0
  slug: portbase-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 36
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 70.9
    developer_ergonomics: 32.7
    discoverability: 72.3
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 6.3
      total: 32
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/portbase/portbase-2026-11-03T141413.png
security:
- kind: authentication
  name: Portbase Authentication
  slug: portbase-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Portbase Domain Security
  slug: portbase-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Portbase Vulnerability Disclosure
  slug: portbase-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 9
skills:
- name: portbase-bookings-subscribe-and-retrieve
  slug: portbase-bookings-subscribe-and-retrieve
- name: declare-a-barge-voyage
  slug: portbase-declare-a-barge-voyage
- name: declare-a-vessel-visit
  slug: portbase-declare-a-vessel-visit
- name: file-a-bill-of-lading-consignment
  slug: portbase-file-a-bill-of-lading-consignment
- name: portbase-forward-shipment
  slug: portbase-forward-shipment
- name: prenotify-a-road-container-visit
  slug: portbase-prenotify-a-road-container-visit
- name: subscribe-to-an-export-booking
  slug: portbase-subscribe-to-an-export-booking
- name: track-bills-of-lading-for-import
  slug: portbase-track-bills-of-lading-for-import
- name: portbase-track-cargo-import
  slug: portbase-track-cargo-import
slug: portbase
tags:
- Company
- Port Community System
- Logistics
- Maritime
- Shipping
- Supply Chain
- Customs
- Netherlands
website: https://www.portbase.com/en/
---
