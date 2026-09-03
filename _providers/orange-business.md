---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Orange Business Agentic Access
  operation_count: 21
  slug: orange-business-agentic-access
  summary_line: 21 operations · 17 acting
api_count: 12
apis:
- description: Manage Orange Business cellular IoT SIM fleets worldwide — activation, suspension, usage, location, diagnostics — across 200+ countries via a single REST surface. Backs the Orange Business Mobile Conn
  name: Orange Business IoT Managed Global Connectivity API
  slug: orange-business-iot-managed-global-connectivity-api
- description: Accept Orange Money mobile-wallet payments on web and mobile checkouts across Mali, Cameroon, Cote d'Ivoire, Senegal, Madagascar, Botswana, Guinea Conakry, Guinea Bissau, Sierra Leone, DR Congo, and C
  name: Orange Business Orange Money WebPay API
  slug: orange-business-orange-money-webpay-api
- description: Direct-carrier-billing API that lets merchants charge purchases to a customer's Orange mobile invoice. Aimed at digital goods, content, and microtransactions for Orange subscribers.
  name: Orange Business Pay With Orange Bill API
  slug: orange-business-pay-with-orange-bill-api
- description: A2P SMS delivery API for Orange Middle East and Africa footprint. Supports transactional, OTP, and marketing messages across Orange's African operating companies.
  name: Orange Business SMS Middle East and Africa API
  slug: orange-business-sms-mea-api
- description: Programmable voice / VoIP API for integrating outbound calls, IVR, and click-to-call into business applications on Orange's voice platform.
  name: Orange Business Voice as a Service API
  slug: orange-business-voice-as-a-service-api
- description: Multichannel contact and notification API — SMS, voice, email, and fax broadcast — used for crisis communications, mass notifications, and customer outreach campaigns by Orange Business enterprise cus
  name: Orange Business Contact Everyone API
  slug: orange-business-contact-everyone-api
- description: Programmable management for Business Talk, Orange Business's enterprise SIP trunking and IP voice service. Provision lines, manage sites, and integrate voice with UCaaS platforms.
  name: Orange Business Business Talk API
  slug: orange-business-business-talk-api
- description: REST API for Cloud Avenue, Orange Business's France-sovereign VMware-based managed IaaS — provision virtual datacenters, networks, storage, and compute resources programmatically.
  name: Orange Business Cloud Avenue API
  slug: orange-business-cloud-avenue-api
- description: Sandbox IaaS environment for testing applications on Orange Business's Evolution Platform with full REST API access to VMs, networks, and storage.
  name: Orange Business Evolution Platform IaaS API
  slug: orange-business-evolution-platform-iaas-api
- description: Order, manage, and monitor Ethernet Virtual Private Line connectivity services across Orange Business's global Ethernet backbone via REST.
  name: Orange Business EVPL Online API
  slug: orange-business-evpl-online-api
- description: Real-time monitoring API for EVPL and adjacent Orange Business network services — fetch link health, throughput, and incident state for managed enterprise connectivity.
  name: Orange Business EVPL Monitoring API
  slug: orange-business-evpl-monitoring-api
- description: Manage CDN edge caching, purge, and acceleration policies for content delivered over Orange's networks — primarily targeted at media and large enterprise customers.
  name: Orange Business Content Delivery Boost API
  slug: orange-business-content-delivery-boost-api
- description: Customer-facing inventory API for Orange Business Services — list contracts, sites, services, and product instances under a B2B account.
  name: Orange Business Core Information API
  slug: orange-business-core-information-api
- description: Place, modify, and cancel orders against the Orange Business Services product catalogue. Aligned with TM Forum Open APIs (TMF622-style product ordering).
  name: Orange Business Ordering API
  slug: orange-business-ordering-api
- description: Track the lifecycle and milestones of an Orange Business Services order — status, expected delivery, blocking issues, and milestone history.
  name: Orange Business Order Tracking API
  slug: orange-business-order-tracking-api
- description: Programmatic access to Orange Business Services M2M invoices, charges, and itemised usage records for enterprise finance and FinOps integration.
  name: Orange Business Billing API
  slug: orange-business-billing-api
- description: Open, update, and track Orange Business Services support tickets via REST. Aligned with TM Forum TMF621 Trouble Ticket conventions to plug into enterprise ITSM workflows.
  name: Orange Business Incident API
  slug: orange-business-incident-api
- description: Marketplace surface for discovering Orange Business APIs — programmatic catalogue access for the Orange Business API portfolio.
  name: Orange Business API Place
  slug: orange-business-api-place-api
- description: Check broadband and fibre eligibility at a French address for operator partners — feeds B2B onboarding flows.
  name: Orange Business Operator Eligibility (France) API
  slug: orange-business-operator-eligibility-fr-api
- description: Public-initiative network (RIP) fibre eligibility check for French regional fibre rollouts, used by alternative operators to qualify customer addresses.
  name: Orange Business RIP Operator Eligibility (France) API
  slug: orange-business-rip-operator-eligibility-fr-api
- description: Real-time identity verification combining ID-document capture, liveness detection, and biometric match against the document. Targets remote onboarding for regulated industries.
  name: Orange Business Live Identity Verify API
  slug: orange-business-live-identity-verify-api
- description: Behavioural and challenge-based human-verification (captcha) API used inside Orange's Live Identity suite to gate sensitive flows against automated abuse.
  name: Orange Business Live Identity Captcha API
  slug: orange-business-live-identity-captcha-api
- description: Cameroon-specific A2P messaging platform for enterprise SMS, USSD, and rich messaging deliveries to Orange Cameroon subscribers.
  name: Orange Business Messaging Pro Cameroon API
  slug: orange-business-messagingpro-cameroon-api
- baseURL: https://api.orange.com/camara/playground/api/device-swap/v0.2
  baseurl_source: declared
  description: Validate if the SIM of the end-user has been installed in a different device during a past period
  name: Orange Business Check Device Swap API
  slug: orange-business-check-device-swap-api
- baseURL: https://api.orange.com/camara/playground/api/sim-swap/v1
  baseurl_source: declared
  description: The Check SIM swap API from Orange Business — 1 operation(s) for check sim swap.
  name: Orange Business Check SIM swap API
  slug: orange-business-check-sim-swap-api
- baseURL: https://api.orange.com/camara/playground/api/device-reachability-status/v0.6
  baseurl_source: declared
  description: Operations to get the current reachability status of a device
  name: Orange Business Device reachability status API
  slug: orange-business-device-reachability-status-api
- baseURL: https://api.orange.com/camara/playground/api/geofencing-subscriptions/v0.3
  baseurl_source: declared
  description: Operations to manage event subscriptions on geofencing events for leaving and entering an area.
  name: Orange Business Geofencing subscriptions API
  slug: orange-business-geofencing-subscriptions-api
- baseURL: https://api.orange.com/camara/playground/api/location-retrieval/v0.3
  baseurl_source: declared
  description: Retrieve the location of a device
  name: Orange Business Location retrieval API
  slug: orange-business-location-retrieval-api
- baseURL: https://api.orange.com/camara/playground/api/location-verification/v1
  baseurl_source: declared
  description: Verification of the location of a device
  name: Orange Business Location verification API
  slug: orange-business-location-verification-api
- baseURL: https://api.orange.com/camara/playground/api/kyc-match/v0.2
  baseurl_source: declared
  description: Operations to match a customer identity against the account data bound to their phone number.
  name: Orange Business Match API
  slug: orange-business-match-api
- baseURL: https://api.orange.com/camara/playground/api/number-verification/v1
  baseurl_source: declared
  description: API operation to return the phone number associated to the access token.
  name: Orange Business Phone number share API
  slug: orange-business-phone-number-share-api
- baseURL: https://api.orange.com/camara/playground/api/number-verification/v1
  baseurl_source: declared
  description: API operation to verify a phone number received as input. It can be received either in plain text or hashed format.
  name: Orange Business Phone number verify API
  slug: orange-business-phone-number-verify-api
- baseURL: https://api.orange.com/camara/playground/api/population-density-data/v0.3
  baseurl_source: declared
  description: Operations to retrieve population density information.
  name: Orange Business Population Density Data API
  slug: orange-business-population-density-data-api
- baseURL: https://api.orange.com/camara/playground/api/quality-on-demand/v0.11
  baseurl_source: declared
  description: Manage QoS sessions
  name: Orange Business QoS Sessions API
  slug: orange-business-qos-sessions-api
- baseURL: https://api.orange.com/camara/playground/api/device-swap/v0.2
  baseurl_source: declared
  description: Receive the last date in which the device of the end-user was swapped
  name: Orange Business Retrieve Device Swap Date API
  slug: orange-business-retrieve-device-swap-date-api
- baseURL: https://api.orange.com/camara/playground/api/sim-swap/v1
  baseurl_source: declared
  description: The Retrieve SIM swap date API from Orange Business — 1 operation(s) for retrieve sim swap date.
  name: Orange Business Retrieve SIM swap date API
  slug: orange-business-retrieve-sim-swap-date-api
- baseURL: https://api.orange.com/camara/playground/api/device-roaming-status/v0.6
  baseurl_source: declared
  description: Operation to get device roaming status and country information (if roaming) synchronously
  name: Orange Business Roaming status retrieval API
  slug: orange-business-roaming-status-retrieval-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: get your accounting metrics
  name: Orange Business Accounting - V1 API
  slug: orange-business-accounting-v1-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage your alarm rules
  name: Orange Business Alarm rules API
  slug: orange-business-alarm-rules-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: API key management
  name: Orange Business Api keys API
  slug: orange-business-api-keys-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: API self key management
  name: Orange Business Api self keys API
  slug: orange-business-api-self-keys-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Search through your AuditLog messages
  name: Orange Business Audit Log API
  slug: orange-business-audit-log-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Cellular subscriptions and providers management
  name: Orange Business Beta - Cellular networks management API
  slug: orange-business-beta-cellular-networks-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Search network metrics
  name: Orange Business Beta - Network metrics API
  slug: orange-business-beta-network-metrics-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage lwm2m bootstrap config
  name: Orange Business Bootstrap Config API
  slug: orange-business-bootstrap-config-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage LwM2M bootstrap entries
  name: Orange Business Bootstrap Entry API
  slug: orange-business-bootstrap-entry-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage LwM2M bootstrap master entries
  name: Orange Business Bootstrap Master Entry API
  slug: orange-business-bootstrap-master-entry-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: CA certificates for MQTT client cert. authentication
  name: Orange Business CA certificates API
  slug: orange-business-ca-certificates-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Management of actions on a fleet of devices
  name: Orange Business Campaign management API
  slug: orange-business-campaign-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: APIs to inject a bulk of data
  name: Orange Business Data bulk injection API
  slug: orange-business-data-bulk-injection-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: APIs to manage dataMessage custom pipelines
  name: Orange Business Data management custom pipelines API
  slug: orange-business-data-management-custom-pipelines-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: APIs to search through injected data
  name: Orange Business Data management data search API
  slug: orange-business-data-management-data-search-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: APIs to store and retrieve data
  name: Orange Business Data management data store API
  slug: orange-business-data-management-data-store-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: list all decoders for a tenant
  name: Orange Business Decoders API
  slug: orange-business-decoders-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: binary decoder provisioning
  name: Orange Business Decoders - binary API
  slug: orange-business-decoders-binary-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: CSV decoder provisioning
  name: Orange Business Decoders - CSV API
  slug: orange-business-decoders-csv-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: public decoder management
  name: Orange Business Decoders - public API
  slug: orange-business-decoders-public-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: FIFO are now automatically managed with FifoPublish Action in Trigger & Actions
  name: Orange Business Deprecated - Bus management API
  slug: orange-business-deprecated-bus-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: use data search V1 instead
  name: Orange Business Deprecated - Data management data search - V0 API
  slug: orange-business-deprecated-data-management-data-search-v0-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage your device analytics rules
  name: Orange Business Device Analytics API
  slug: orange-business-device-analytics-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Devices commands
  name: Orange Business Device management - Commands API
  slug: orange-business-device-management-commands-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Devices configuration
  name: Orange Business Device management - Configuration API
  slug: orange-business-device-management-configuration-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: LoRa connector specificity
  name: Orange Business Device management - Connector nodes - LoRa specific API
  slug: orange-business-device-management-connector-nodes-lora-specific-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Connector nodes management
  name: Orange Business Device management - Connector nodes - V1 API
  slug: orange-business-device-management-connector-nodes-v1-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Group management
  name: Orange Business Device management - Groups - V1 API
  slug: orange-business-device-management-groups-v1-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Devices' interfaces management
  name: Orange Business Device management - Interfaces API
  slug: orange-business-device-management-interfaces-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Devices inventory
  name: Orange Business Device management - Inventory - V1 API
  slug: orange-business-device-management-inventory-v1-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Devices resources and firmware
  name: Orange Business Device management - Resources API
  slug: orange-business-device-management-resources-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Resources management and firmware
  name: Orange Business Device management - Resources management API
  slug: orange-business-device-management-resources-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: ActivityRule management
  name: Orange Business Event processing - Activity API
  slug: orange-business-event-processing-activity-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Context management
  name: Orange Business Event processing - Context API
  slug: orange-business-event-processing-context-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: FiringRules and FiringGuards management
  name: Orange Business Event processing - Firing API
  slug: orange-business-event-processing-firing-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Geozone management
  name: Orange Business Event processing - Geozone API
  slug: orange-business-event-processing-geozone-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: MatchingRules management
  name: Orange Business Event processing - Matching API
  slug: orange-business-event-processing-matching-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: State processing Rules management
  name: Orange Business Event processing - State processing API
  slug: orange-business-event-processing-state-processing-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Gateway management
  name: Orange Business Gateway management for LoRa API
  slug: orange-business-gateway-management-for-lora-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Inventory explorer management
  name: Orange Business Inventory Explorer API
  slug: orange-business-inventory-explorer-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: sending email or sms notifications
  name: Orange Business Notification API
  slug: orange-business-notification-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage notification channels
  name: Orange Business Notification channels API
  slug: orange-business-notification-channels-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Self tenant account management
  name: Orange Business Self tenant account API
  slug: orange-business-self-tenant-account-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: manage self user
  name: Orange Business Self User management API
  slug: orange-business-self-user-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Action policies on event and messages
  name: Orange Business Triggers and Actions API
  slug: orange-business-triggers-and-actions-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Test api for actions
  name: Orange Business Triggers and Actions - Test API
  slug: orange-business-triggers-and-actions-test-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage twin data rules
  name: Orange Business Twin data rules management API
  slug: orange-business-twin-data-rules-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage twin device
  name: Orange Business Twin devices management API
  slug: orange-business-twin-devices-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage twin model
  name: Orange Business Twin models management API
  slug: orange-business-twin-models-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage twin observations
  name: Orange Business Twin observations API
  slug: orange-business-twin-observations-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: Manage twin device operations
  name: Orange Business Twin operations management API
  slug: orange-business-twin-operations-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: authentication
  name: Orange Business User authentication API
  slug: orange-business-user-authentication-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: authentication management
  name: Orange Business User authentication management API
  slug: orange-business-user-authentication-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: manage user profile and get access list
  name: Orange Business User Profile and Access Management API
  slug: orange-business-user-profile-and-access-management-api
- baseURL: https://liveobjects.orange-business.com/api/v1
  baseurl_source: declared
  description: manage users
  name: Orange Business Users management API
  slug: orange-business-users-management-api
artifact_total: 127
asyncapis:
- description: ''
  name: Orange Business Webhooks
  slug: orange-business-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Device Location Retrieval Check Device Swap API
  slug: open-orange-business-check-device-swap-api
- collection_type: open
  name: Device Location Retrieval Check Device Swap Check SIM swap API
  slug: open-orange-business-check-sim-swap-api
- collection_type: open
  name: Device Location Retrieval
  slug: open-orange-business-device-location-retrieval
- collection_type: open
  name: Device Location Verification
  slug: open-orange-business-device-location-verification
- collection_type: open
  name: Device Location Retrieval Check Device Swap Device reachability status API
  slug: open-orange-business-device-reachability-status-api
- collection_type: open
  name: Device Reachability Status
  slug: open-orange-business-device-reachability-status
- collection_type: open
  name: Device Roaming Status
  slug: open-orange-business-device-roaming-status
- collection_type: open
  name: Device Swap
  slug: open-orange-business-device-swap
- collection_type: open
  name: Device Location Retrieval Check Device Swap Geofencing subscriptions API
  slug: open-orange-business-geofencing-subscriptions-api
- collection_type: open
  name: Device Geofencing Subscriptions
  slug: open-orange-business-geofencing
- collection_type: open
  name: Know Your Customer Match
  slug: open-orange-business-kyc-match
- collection_type: open
  name: Device Check Device Swap Location retrieval API
  slug: open-orange-business-location-retrieval-api
- collection_type: open
  name: Device Location Retrieval Check Device Swap Location verification API
  slug: open-orange-business-location-verification-api
- collection_type: open
  name: Device Location Retrieval Check Device Swap Match API
  slug: open-orange-business-match-api
- collection_type: open
  name: Number Verification
  slug: open-orange-business-number-verification
- collection_type: open
  name: Device Location Retrieval Check Device Swap Phone number share API
  slug: open-orange-business-phone-number-share-api
- collection_type: open
  name: Device Location Retrieval Check Device Swap Phone number verify API
  slug: open-orange-business-phone-number-verify-api
- collection_type: open
  name: Device Location Retrieval Check Device Swap Population Density Data API
  slug: open-orange-business-population-density-data-api
- collection_type: open
  name: Population Density Data
  slug: open-orange-business-population-density-data
- collection_type: open
  name: Device Location Retrieval Check Device Swap QoS Sessions API
  slug: open-orange-business-qos-sessions-api
- collection_type: open
  name: Quality-On-Demand
  slug: open-orange-business-quality-on-demand
- collection_type: open
  name: Device Location Retrieval Check Device Swap Retrieve Device Swap Date API
  slug: open-orange-business-retrieve-device-swap-date-api
- collection_type: open
  name: Device Location Retrieval Check Device Swap Retrieve SIM swap date API
  slug: open-orange-business-retrieve-sim-swap-date-api
- collection_type: open
  name: Device Location Retrieval Check Device Swap Roaming status retrieval API
  slug: open-orange-business-roaming-status-retrieval-api
- collection_type: open
  name: SIM Swap
  slug: open-orange-business-sim-swap
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/orange-business-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/camaraproject/NumberVerification/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/camaraproject/NumberVerification/releases
- group: other
  title: ''
  type: Overlay
  url: overlays/orange-business-live-objects-overlay.yaml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/orange-business-scopes.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/camaraproject/NumberVerification/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/orange-business-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orange-business-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orange-business-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/orange-business-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.orange.com/
- group: start
  title: ''
  type: Portal
  url: https://www.orange-business.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.orange.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orange.com/products/network-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orange.com/blog/orange-open-gateway-the-new-era-of-digital-services/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.orange.com/blog/orange-livenet-a-new-business-unit-to-market-network-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma_orgs/orange-2/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/camaraproject
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Orange-OpenSource
- group: build
  title: ''
  type: Tools
  url: https://github.com/Orange-OpenSource/hurl
- group: build
  title: ''
  type: Tools
  url: https://github.com/Orange-OpenSource/Orange-Boosted-Bootstrap
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Orange-OpenSource/ouds-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Orange-OpenSource/ouds-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Orange-OpenSource/ouds-flutter
- group: build
  title: ''
  type: Tools
  url: https://github.com/Orange-OpenSource/towards5gs-helm
- group: company
  title: ''
  type: Blog
  url: https://developer.orange.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://www.orange-business.com/en/blogs
- group: docs
  title: ''
  type: Documentation
  url: https://5glab.orange.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.orange.com/en/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orange-business/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/orange/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/orangebusiness
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orange-business.com/en/legal-information
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orange-business.com/en/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://developer.orange.com/contact
- group: operate
  title: ''
  type: Support
  url: https://developer.orange.com/talk-to-sales/
- group: start
  title: ''
  type: Signup
  url: https://developer.orange.com/signup
- group: docs
  title: ''
  type: Documentation
  url: https://www.orange-business.com/en/products/live-intelligence
- group: start
  title: ''
  type: Portal
  url: https://liveobjects.orange-business.com/
- group: start
  title: ''
  type: Portal
  url: https://cloud.orange-business.com/
- group: build
  title: ''
  type: Packages
  url: packages/orange-business-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/orange-business-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/orange-business-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/orange-business-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/orange-business-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/orange-business-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orange-business-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/orange-business-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/orange-business-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orange-business-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/orange-business-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/orange-business-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orange-business-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orange-business-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/orange-business-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/orange-business-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/orange-business-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orange-business-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: security/orange-business-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.orange.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developer.orange.com/network-apis/api-catalog/number-verification/playground/1.0/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developer.orange.com/network-apis/practical-guides/try-it-for-free/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.orange.com/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.orange.com/talk-to-sales/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.orange.com/terms-and-conditions
created: '2026-05-25'
description: Orange Business is the B2B, telco-cloud, and developer arm of Orange S.A. — France's leading telecommunications group operating across Europe, the Middle East, and Africa. The company markets itself as "an operator, integrator, and platform player" and serves 30,000+ enterprise customers across 65 countries with cloud, cybersecurity, SD-WAN/SASE, 5G, IoT, data, AI, and digital-workplace services. Orange's developer surface is split across two tracks. The Orange Developer portal (developer.orange.com) publishes the Orange Open Gateway — Orange's implementation of GSMA Open Gateway / CAMARA standardised network APIs (Number Verification, SIM Swap, Device Swap, KYC Match, Device Location, Geofencing, Device Status, Quality on Demand, Population Density Data) — alongside Orange-specific APIs for IoT (Live Objects, IoT Global Connectivity), payments (Orange Money WebPay, Pay With Orange Bill, carrier billing across Orange Africa), communications (Voice, SMS MEA, Business Talk, Contact
  Everyone), cloud (Cloud Avenue sovereign IaaS, Evolution Platform), and identity (Live Identity Verify, Live Identity Captcha). The Orange Business Services portfolio adds a B2B TM Forum–aligned API track for ordering, billing, incident management, eligibility, and order tracking. The Orange-OpenSource GitHub org backs the developer ecosystem with 427+ repos including Hurl (the popular Rust HTTP testing CLI with 18K+ stars), the Boosted accessible Bootstrap framework, the OUDS Orange Unified Design System for iOS / Android / Flutter, and 5G Kubernetes Helm charts. Orange has also stood up Orange LiveNet, a business unit dedicated to commercialising programmable network capabilities, and is one of the founding operators of the GSMA Open Gateway initiative with the CAMARA Linux Foundation project.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orange-business.png
layout: provider
mcp_servers:
- description: 'A Model Context Protocol server exposing Orange''s CAMARA Network APIs — SIM swap, device location, reachability, roaming, KYC match, population density and quality-on-demand — plus the Orange Network '
  name: Orange CAMARA MCP Enablement PI1 server
  slug: orange-camara-mcp-enablement-pi1-server
modified: '2026-08-26'
name: Orange Business
nav: Providers
network: true
overview: 'Orange Business publishes 69 APIs on the [APIs.io](https://apis.io/) network, including Check Device Swap API, Check SIM swap API, Device reachability status API, and 66 more. Tagged areas include 5G, Artificial Intelligence, B2B, CAMARA, and Cloud.


  The Orange Business catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Orange Business'' developer surface includes authentication, developer portal, documentation, tooling, engineering blog, support, signup flow, and 59 more developer resources.'
plans:
- name: Orange Business Plans Pricing
  plan_count: 2
  slug: orange-business-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Orange Business Rate Limits
  slug: orange-business-rate-limits
scopes:
- name: Orange Business Scopes
  scope_count: 23
  slug: orange-business-scopes
  summary_line: 23 scopes · authorizationCode
score:
  band: exemplar
  composite: 68.4
  coverage:
    artifact_dirs: 31
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.7
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 67.4
    developer_ergonomics: 82.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 78.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 67.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 79.7
      derived: 0
      marker_coverage: 0.0
      total: 69
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 75.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orange-business/refs/heads/main/screenshots/orange-business-2026-06-20T191153.png
security:
- kind: authentication
  name: Orange Business Authentication
  slug: orange-business-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Orange Business Domain Security
  slug: orange-business-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Orange Business Vulnerability Disclosure
  slug: orange-business-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: orange-business
tags:
- 5G
- Artificial Intelligence
- B2B
- CAMARA
- Cloud
- Communications
- Cybersecurity
- Developer Platform
- Digital Workplace
- Enterprise
- France
- IoT
- Identity
- Mobile Money
- Network APIs
- Open Gateway
- Orange
- Payments
- SD-WAN
- SMS
- SASE
- Telco
- Voice
website: https://developer.orange.com/
---
