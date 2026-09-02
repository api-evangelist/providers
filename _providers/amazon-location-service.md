---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Amazon Location Service Agentic Access
  operation_count: 8
  slug: amazon-location-service-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- description: Map resource management
  name: Amazon Location Service Maps API
  slug: amazon-location-service-maps-api
arazzos:
- description: Reuse an existing map by name if present, otherwise create it.
  name: Amazon Location Service Find or Create Map
  slug: amazon-location-service-find-or-create-map-workflow
- description: Reuse a tracker if it exists, else create it, then push a position.
  name: Amazon Location Service Find or Create Tracker and Report Position
  slug: amazon-location-service-find-or-create-tracker-workflow
- description: Provision a map and a tracker, then report a first device position.
  name: Amazon Location Service Fleet Onboarding
  slug: amazon-location-service-fleet-onboarding-workflow
- description: Geocode free-form text and stand up a map to render the result.
  name: Amazon Location Service Geocode Address and Provision Map
  slug: amazon-location-service-geocode-and-map-workflow
- description: Geocode text to coordinates and record them as a device position.
  name: Amazon Location Service Geocode Address into Tracker Position
  slug: amazon-location-service-geocode-batch-positions-workflow
- description: List all map resources and pull full detail on the first entry.
  name: Amazon Location Service Map Inventory Audit
  slug: amazon-location-service-map-inventory-audit-workflow
- description: Create, inspect, and delete a map resource in a single guarded flow.
  name: Amazon Location Service Map Lifecycle Teardown
  slug: amazon-location-service-map-lifecycle-workflow
- description: Create a map resource and confirm it is queryable before use.
  name: Amazon Location Service Provision and Verify Map
  slug: amazon-location-service-provision-map-workflow
- description: Create a tracker then push an initial device position update to it.
  name: Amazon Location Service Provision Tracker and Update Position
  slug: amazon-location-service-provision-tracker-workflow
artifact_total: 47
collections:
- collection_type: postman
  name: Amazon Location Service API
  slug: postman-amazon-location-service
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Location Service Maps API
  slug: open-amazon-location-service-maps-api
- collection_type: open
  name: Amazon Location Service API
  slug: open-amazon-location-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-location-service-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-location-service-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-location-service-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-location-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-location-service-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-location-service/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-find-or-create-map-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-find-or-create-tracker-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-fleet-onboarding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-geocode-and-map-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-geocode-batch-positions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-map-inventory-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-map-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-provision-map-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-location-service-provision-tracker-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/location/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/location/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/mobile/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/location/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: other
  title: ''
  type: Knowledge Center
  url: https://repost.aws/knowledge-center
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-location-service
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-location-service-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-location-service-vocabulary.yaml
created: '2024-01-15'
description: Amazon Location Service provides location-based services including maps, places, routes, trackers, and geofences, enabling developers to add location functionality to applications securely and cost-effectively.
examples:
- key_count: 6
  name: Amazon Location Service Map Example
  slug: amazon-location-service-map-example
- key_count: 5
  name: Amazon Location Service Tracker Example
  slug: amazon-location-service-tracker-example
features:
- description: Render interactive maps with customizable styles using vector tiles and raster tiles.
  name: Maps
- description: Search for addresses, points of interest, and geographic coordinates.
  name: Places Search
- description: Calculate optimal routes with turn-by-turn directions and estimated travel time.
  name: Route Calculation
- description: Create virtual boundaries and detect when tracked devices enter or exit those areas.
  name: Geofencing
- description: Track the real-time position of assets, vehicles, and people.
  name: Asset Tracking
- description: Data does not leave AWS infrastructure, keeping location data private and secure.
  name: Data Privacy
finops:
- name: Amazon Location Service Finops
  service_category: API
  slug: amazon-location-service-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
integrations:
- description: Authenticate map and location requests using Cognito identity pools.
  name: Amazon Cognito
- description: Ingest device location data from IoT Core into Location Service tracking.
  name: AWS IoT Core
- description: Trigger events when geofences are entered or exited via EventBridge.
  name: Amazon EventBridge
- description: Use HERE maps and location data as a data provider within Location Service.
  name: HERE Technologies
- description: Access Esri basemaps and location data through Amazon Location Service.
  name: Esri
json_schemas:
- name: Amazon Location Service Geofence
  property_count: 6
  slug: amazon-location-service-geofence
- name: MapResource
  property_count: 6
  slug: amazon-location-service-map
- name: Tracker
  property_count: 5
  slug: amazon-location-service-tracker
json_structures:
- name: Amazon Location Service Map Structure
  property_count: 6
  slug: amazon-location-service-map-structure
- name: Amazon Location Service Tracker Structure
  property_count: 5
  slug: amazon-location-service-tracker-structure
jsonld:
- class_count: 2
  name: Amazon Location Service Context
  property_count: 7
  slug: amazon-location-service-context
layout: provider
modified: '2026-05-19'
name: Amazon Location Service
nav: Providers
network: true
overview: 'Amazon Location Service publishes 1 API on the [APIs.io](https://apis.io/) network: Maps API. Tagged areas include Geocoding, Geofencing, Location, Maps, and Routing.


  The Amazon Location Service catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Location Service''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 26 more developer resources.'
plans:
- name: Amazon Location Service Plans Pricing
  plan_count: 3
  slug: amazon-location-service-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Amazon Location Service Rate Limits
  slug: amazon-location-service-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Location Service API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-location-service-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon Location Service API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 15
  slug: amazon-location-service-spectral-rules
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 44.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-location-service/refs/heads/main/screenshots/amazon-location-service-2026-06-20T171726.png
security:
- kind: authentication
  name: Amazon Location Service Authentication
  slug: amazon-location-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Location Service Domain Security
  slug: amazon-location-service-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Location Service Vulnerability Disclosure
  slug: amazon-location-service-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Location Service Trust Center
  slug: amazon-location-service-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-location-service
tags:
- Geocoding
- Geofencing
- Location
- Maps
- Routing
use_cases:
- description: Track vehicle fleets in real time and optimize routes for delivery efficiency.
  name: Fleet Management
- description: Build store locators and proximity-based search for retail applications.
  name: Store Locator
- description: Send notifications when assets enter or exit defined geographic boundaries.
  name: Geofence Alerts
- description: Embed interactive maps in web and mobile applications.
  name: Map Visualization
website: https://aws.amazon.com/
---
