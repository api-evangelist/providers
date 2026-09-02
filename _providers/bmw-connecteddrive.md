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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bmw Connecteddrive Agentic Access
  operation_count: 11
  slug: bmw-connecteddrive-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- description: The BMW CarData Streaming API delivers near-real-time vehicle telematics over MQTT 3.1.1 with TLS. Clients connect to `customer.streaming-cardata.bmwgroup.com` on port 9000, authenticate with their GC
  name: BMW CarData Streaming API
  slug: bmw-cardata-streaming-api
- description: The third-party variant of BMW CarData targets independent service providers — repair shops, charging operators, fleet platforms, insurance, and aftermarket integrators — who consume vehicle data on b
  name: BMW CarData Third-Party API
  slug: bmw-cardata-thirdparty-api
- description: Management of containers
  name: BMW ConnectedDrive Containers API
  slug: bmw-connecteddrive-containers-api
- description: Access vehicle data and information
  name: BMW ConnectedDrive Vehicles API
  slug: bmw-connecteddrive-vehicles-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CARDATA API
  slug: open-bmw-cardata-customer-api
- collection_type: open
  name: CARDATA Containers API
  slug: open-bmw-connecteddrive-containers-api
- collection_type: open
  name: CARDATA Containers Vehicles API
  slug: open-bmw-connecteddrive-vehicles-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/bmw-connecteddrive-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bmw-connecteddrive-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bmw-connecteddrive-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bmw-connecteddrive-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bmw.com
- group: start
  title: ''
  type: Portal
  url: https://www.bmwgroup.com
- group: start
  title: ''
  type: Portal
  url: https://bmw-cardata.bmwgroup.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bmw-cardata.bmwgroup.com/customer/public/api-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://bmw-cardata.bmwgroup.com/customer/public/api-specification
- group: docs
  title: ''
  type: Documentation
  url: https://bmw-cardata.bmwgroup.com/thirdparty/public/car-data/technical-configuration/api-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://bmw-cardata.bmwgroup.com/thirdparty/public/car-data/technical-configuration/api-specification
- group: docs
  title: ''
  type: Documentation
  url: https://bmw-cardata.bmwgroup.com/thirdparty/public/repair-and-maintenance/technical-configuration/api-documentation
- group: start
  title: ''
  type: Signup
  url: https://bmw-cardata.bmwgroup.com/customer
- group: start
  title: ''
  type: Signup
  url: https://bmw-cardata.bmwgroup.com/thirdparty
- group: company
  title: ''
  type: Blog
  url: https://www.press.bmwgroup.com/global/rss
- group: auth
  title: ''
  type: Authentication
  url: https://customer.bmwgroup.com/oneid/login
- group: other
  title: ''
  type: ConnectedDrive
  url: https://www.bmw.com/en/explore-bmw/connected-drive.html
- group: other
  title: ''
  type: ConnectedDriveStore
  url: https://customer.bmwgroup.com/store/
- group: other
  title: ''
  type: MyBMW
  url: https://www.bmw.com/en/footer/my-bmw-app.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bmwcarit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bmwgroup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bmw.com/en/footer/metanavigation/privacy-policy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bmw.com/en/footer/metanavigation/legal-notice-pool/legal-notice.html
- group: company
  title: ''
  type: Press
  url: https://www.press.bmwgroup.com
- group: company
  title: ''
  type: Newsroom
  url: https://www.bmwgroup.com/en/news.html
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/BMWGroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bmw-group
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@BMWGroup
created: '2026-05-25'
description: BMW ConnectedDrive is BMW Group's umbrella for connected vehicle services spanning navigation, remote services, intelligent emergency call, ConnectedDrive Store add-ons, and the My BMW app. Programmatic access for customers, third-party developers, and the repair-and-maintenance ecosystem is consolidated under the BMW Open Data Platform / BMW CarData. CarData exposes an OAuth 2.0 Device Code Flow protected REST API at api-cardata.bmwgroup.com for retrieving static vehicle metadata (basicData), telematics, charging history, smart maintenance tyre diagnosis, location-based charging settings, vehicle images, and managing data "containers" that scope which telematics descriptors a client is authorized to read. A companion MQTT 3.1.1 streaming service at customer.streaming-cardata.bmwgroup.com:9000 (TLS) pushes live container data on the per-VIN topic `{gcid}/{vin}`. CarData is the EU regulatory successor to the legacy BMW ConnectedDrive REST endpoints used by the My BMW app and
  is the canonical surface for third-party automotive integrations, including independent repair, fleet, charging, and home-automation use cases.
features:
- OAuth 2.0 Device Code Flow against GCDM for customer consent
- Scoped client subscriptions — `cardata:api:read` and `cardata:streaming:read`
- CarData "containers" let customers scope which telematics descriptors flow to each client
- REST endpoints for basic data, telematic data, charging history, smart maintenance tyre diagnosis, location-based charging settings, vehicle images, and vehicle mappings
- MQTT 3.1.1 streaming over TLS for near-real-time per-VIN telematics on topic `{gcid}/{vin}`
- GCID-based identity model for both REST bearer tokens and MQTT credentials
- One-hour ID tokens with refresh-token rotation
- Third-party developer track aligned with EU Data Act / right-to-repair
- Separate Repair & Maintenance API track for independent workshops
- Companion BMW Car IT open-source stack (joynr, ramses, MoCOCrW, python-dlt) underpinning connected-vehicle middleware
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bmw-connecteddrive.png
layout: provider
modified: '2026-05-25'
name: BMW ConnectedDrive
nav: Providers
network: true
overview: 'BMW ConnectedDrive publishes 2 APIs on the [APIs.io](https://apis.io/) network: Containers API and Vehicles API. Tagged areas include Automotive, Connected Vehicle, Telematics, Vehicle Data, and CarData.


  BMW ConnectedDrive''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, YouTube channel, and 22 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bmw-connecteddrive/refs/heads/main/screenshots/bmw-connecteddrive-2026-06-20T173542.png
security:
- kind: authentication
  name: Bmw Connecteddrive Authentication
  slug: bmw-connecteddrive-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bmw Connecteddrive Domain Security
  slug: bmw-connecteddrive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bmw-connecteddrive
tags:
- Automotive
- Connected Vehicle
- Telematics
- Vehicle Data
- CarData
- ConnectedDrive
- Electric Vehicles
- Charging
- MQTT
- Streaming
- Authentication
- Device Code Flow
- GDPR
- Right To Repair
- Mobility
website: https://www.bmw.com
---
