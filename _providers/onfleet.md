---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Onfleet Agentic Access
  operation_count: 54
  slug: onfleet-agentic-access
  summary_line: 54 operations · 33 acting · 1 human-in-the-loop
api_count: 9
apis:
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: Create, list, fetch, update, clone, force-complete, and delete pickup/dropoff tasks. Tasks are the atomic unit of work in Onfleet — each has a destination, recipient, completion window, optional depen
  name: Onfleet Tasks API
  slug: onfleet-tasks-api
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: Manage drivers — create, list, update, delete, fetch a worker's assigned tasks, and pull a delivery manifest for compliance reporting. Workers are bound to teams, have vehicle metadata (CAR/MOTORCYCLE
  name: Onfleet Workers API
  slug: onfleet-workers-api
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: Create and manage route plans — ordered sequences of tasks assigned to a worker for a time window — and kick off asynchronous route optimization jobs (task-based, vehicle-based, or auto-dispatch). Opt
  name: Onfleet Route Plans API
  slug: onfleet-route-plans-api
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: Orders represent a pickup-dropoff task pair shared between a courier organization and its clients on the Onfleet Connect network. Clients can quote, create, update, clone, cancel, or reject orders; co
  name: Onfleet Orders API
  slug: onfleet-orders-api
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: Look up your own organization and connected delegatee organizations on Onfleet Connect, manage administrators (Super and Standard, optionally read-only), create and list teams, and trigger Team Auto-D
  name: Onfleet Organizations & Teams API
  slug: onfleet-organizations-api
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: Create and look up end customers (recipients) by ID, name, or E.164 phone number. Recipients carry SMS notification preferences and metadata, and can be reused across tasks.
  name: Onfleet Recipients API
  slug: onfleet-recipients-api
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: Manage geocoded physical addresses used as task pickup/dropoff locations. Accepts a parsed address structure or a single `unparsed` field; coordinates are returned as GeoJSON [longitude, latitude].
  name: Onfleet Destinations API
  slug: onfleet-destinations-api
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: Register HTTPS callbacks against 27 trigger types covering task lifecycle, worker duty/CRUD, route plan state changes, SMS recipient events, and async job completions (auto-dispatch, task batch create
  name: Onfleet Webhooks API
  slug: onfleet-webhooks-api
- baseURL: https://onfleet.com/api/v2
  baseurl_source: declared
  description: The Route Optimization API from Onfleet — 5 operation(s) for route optimization.
  name: Onfleet Route Optimization API
  slug: onfleet-route-optimization-api
arazzos:
- description: Create a task and explicitly assign it to a worker's container, then verify.
  name: Onfleet Assign Task to Worker
  slug: onfleet-assign-task-to-worker-workflow
- description: Create a task with auto-assignment to a team, then confirm a worker was assigned.
  name: Onfleet Auto-Assign Task
  slug: onfleet-auto-assign-task-workflow
- description: Submit a batch of tasks asynchronously, then list tasks to verify the load.
  name: Onfleet Batch Create and List Tasks
  slug: onfleet-batch-create-and-list-tasks-workflow
- description: Create a route plan for a worker, append tasks to it, then read it back.
  name: Onfleet Build Route Plan
  slug: onfleet-build-route-plan-workflow
- description: Read a task, clone it for a redelivery, then force-complete the original.
  name: Onfleet Clone and Force-Complete Task
  slug: onfleet-clone-and-complete-task-workflow
- description: Survey unassigned tasks, trigger team auto-dispatch, then re-check what remains.
  name: Onfleet Dispatch Team Tasks
  slug: onfleet-dispatch-team-tasks-workflow
- description: Quote a pickup-and-dropoff order, create it, then read back its status.
  name: Onfleet Fulfill Courier Order
  slug: onfleet-fulfill-courier-order-workflow
- description: Create a team, add a new worker to it, then confirm the worker's membership.
  name: Onfleet Onboard Worker to Team
  slug: onfleet-onboard-worker-to-team-workflow
- description: Initialize and start a route optimization, poll its status, then apply the result.
  name: Onfleet Optimize Team Routes
  slug: onfleet-optimize-team-routes-workflow
- description: Create an administrator, create a team they manage, then confirm the team list.
  name: Onfleet Provision Administrator and Team
  slug: onfleet-provision-admin-and-team-workflow
- description: Create a recipient and destination, then create a delivery task and confirm it.
  name: Onfleet Provision Delivery Task
  slug: onfleet-provision-delivery-task-workflow
- description: Register a webhook, fetch the signing secret, then confirm it is listed.
  name: Onfleet Register Task Webhook
  slug: onfleet-register-task-webhook-workflow
- description: Look up a recipient by phone, create one if missing, then create a task for them.
  name: Onfleet Upsert Recipient and Create Task
  slug: onfleet-upsert-recipient-and-create-task-workflow
artifact_total: 88
asyncapis:
- description: Real-time event stream delivered as HTTPS POST callbacks from Onfleet to a URL you register via the Webhooks API. Each webhook is bound to a single triggerId; payloads share a common envelope with `ti
  name: Onfleet Webhooks
  slug: onfleet-webhooks-asyncapi
collections:
- collection_type: postman
  name: Onfleet Destinations API
  slug: postman-onfleet-destinations-api
- collection_type: postman
  name: Onfleet Orders API
  slug: postman-onfleet-orders-api
- collection_type: postman
  name: Onfleet Organizations API
  slug: postman-onfleet-organizations-api
- collection_type: postman
  name: Onfleet Recipients API
  slug: postman-onfleet-recipients-api
- collection_type: postman
  name: Onfleet Route Plans API
  slug: postman-onfleet-route-plans-api
- collection_type: postman
  name: Onfleet Tasks API
  slug: postman-onfleet-tasks-api
- collection_type: postman
  name: Onfleet Webhooks API
  slug: postman-onfleet-webhooks-api
- collection_type: postman
  name: Onfleet Workers API
  slug: postman-onfleet-workers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Onfleet Destinations API
  slug: open-onfleet-destinations-api
- collection_type: open
  name: Onfleet Destinations Orders API
  slug: open-onfleet-orders-api
- collection_type: open
  name: Onfleet Destinations Organizations API
  slug: open-onfleet-organizations-api
- collection_type: open
  name: Onfleet Destinations Recipients API
  slug: open-onfleet-recipients-api
- collection_type: open
  name: Onfleet Destinations Route Optimization API
  slug: open-onfleet-route-optimization-api
- collection_type: open
  name: Onfleet Destinations Route Plans API
  slug: open-onfleet-route-plans-api
- collection_type: open
  name: Onfleet Destinations Tasks API
  slug: open-onfleet-tasks-api
- collection_type: open
  name: Onfleet Destinations Webhooks API
  slug: open-onfleet-webhooks-api
- collection_type: open
  name: Onfleet Destinations Workers API
  slug: open-onfleet-workers-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/onfleet-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/onfleet-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/onfleet-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/onfleet-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onfleet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onfleet-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/onfleet/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-assign-task-to-worker-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-auto-assign-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-batch-create-and-list-tasks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-build-route-plan-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-clone-and-complete-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-dispatch-team-tasks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-fulfill-courier-order-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-onboard-worker-to-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-optimize-team-routes-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-provision-admin-and-team-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-provision-delivery-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-register-task-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/onfleet-upsert-recipient-and-create-task-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://onfleet.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onfleet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onfleet.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.onfleet.com/reference/setup-tutorial
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onfleet.com/reference/data-types-and-response-formats
- group: docs
  title: ''
  type: Documentation
  url: https://docs.onfleet.com/reference/querying-by-metadata
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.onfleet.com/changelog/api-documentation-updates-may-2026
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.onfleet.com/changelog/order-endpoints
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.onfleet.com/changelog/custom-fields
- group: operate
  title: ''
  type: StatusPage
  url: https://status.onfleet.com
- group: company
  title: ''
  type: Blog
  url: https://onfleet.com/blog
- group: start
  title: ''
  type: Signup
  url: https://onfleet.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://onfleet.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onfleet.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onfleet.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://onfleet.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onfleet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onfleet/pyonfleet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onfleet/node-onfleet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onfleet/php-onfleet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onfleet/java-onfleet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onfleet/gonfleet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/onfleet/ruby-onfleet
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/onfleet/developer
- group: docs
  title: ''
  type: Documentation
  url: https://app.getpostman.com/run-collection/14168007-2dc047db-9556-442a-b643-e913027a74cf
- group: commercial
  title: ''
  type: Plans
  url: plans/onfleet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onfleet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/onfleet-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/onfleet-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/onfleet-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/onfleet-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: Onfleet is an AI-powered last-mile delivery management platform that orchestrates fleet operations, dispatch, route optimization, and customer experience across internal and outsourced delivery fleets. The platform powers 400M+ deliveries for brands including Eaze, Total Wine & More, Pizza Hut, Kroger, and Urbanstems across industries from prepared meals and grocery to cannabis, pharmacy, and furniture. Onfleet exposes a comprehensive REST API v2.7 for tasks, workers, route plans, route optimization, orders, recipients, destinations, organizations/teams, and webhooks — backed by official SDKs in Python, Node.js, PHP, Java, and Go, plus the 150+ courier Onfleet Connect network.
examples:
- key_count: 3
  name: Onfleet Create Task Example
  slug: onfleet-create-task-example
- key_count: 3
  name: Onfleet Create Worker Example
  slug: onfleet-create-worker-example
- key_count: 3
  name: Onfleet Webhook Task Completed Example
  slug: onfleet-webhook-task-completed-example
features:
- REST API v2.7 over HTTPS with Basic Auth using the API key as the username and an empty password
- Base URL https://onfleet.com/api/v2; JSON-only request and response bodies
- 24-character URL-safe resource IDs; GeoJSON [longitude, latitude] coordinates; Unix-millisecond timestamps; E.164 phone numbers
- Tasks API with create, batch create (100 per request), clone, force-complete, dependencies, custom fields, and metadata search
- Workers API with vehicle metadata (CAR / MOTORCYCLE / BICYCLE / TRUCK), capacity, additionalCapacities, and route delivery manifest
- Route Plans API for hub-to-hub routes plus asynchronous Route Optimization (task-based, vehicle-based, auto-dispatch) — Enterprise plan endpoints
- Orders API for pickup-dropoff pair workflows on the Onfleet Connect courier network (quote, create, update, clone, cancel, reject)
- Recipients and Destinations APIs with geocoding and reusable resource lookup by name/phone
- Team Auto-Dispatch (Beta) for batched assignment of unassigned tasks to a team
- Webhooks API with 27 trigger types — full task lifecycle, worker duty/CRUD, route plan events, SMS opt-out, predictive delay, and async job completions
- HMAC-SHA256 webhook signing via /webhooks/secret with X-Onfleet-Signature header
- lastId-based pagination on List Tasks (up to 64 per page); 70-second server timeout on long-running queries
- Official SDKs for Python, Node.js, PHP, Java, and Go; archived Ruby SDK; Postman collection
- AI-powered route optimization trained on 400M+ deliveries; predictive ETA and delay alerts
- Proof of delivery with photos, signatures, timestamps, barcode scanning, and ID verification (Scale+)
- Branded customer tracking pages and two-way driver-customer chat
- Driver mobile apps (iOS and Android) rated 4.7 stars on both stores
- 150+ courier partners via Onfleet Connect
- Native integrations with Shopify, Zapier, GigSmart, Dutchie, Zendrive
finops:
- name: Onfleet Finops
  service_category: ''
  slug: onfleet-finops
graphqls:
- description: Conceptual GraphQL schema for the [Onfleet](https://onfleet.com) last-mile delivery management platform. Derived from the [Onfleet REST API v2.7](https://docs.onfleet.com/reference/introduction).
  name: Onfleet GraphQL Schema
  slug: onfleet-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onfleet.png
integrations:
- Shopify
- Zapier
- Dutchie
- GigSmart
- Zendrive
- Onfleet Connect (150+ courier partners)
json_schemas:
- name: OnfleetDestination
  property_count: 5
  slug: onfleet-destination
- name: OnfleetRecipient
  property_count: 7
  slug: onfleet-recipient
- name: OnfleetRoutePlan
  property_count: 14
  slug: onfleet-route-plan
- name: OnfleetTask
  property_count: 19
  slug: onfleet-task
- name: OnfleetWorker
  property_count: 13
  slug: onfleet-worker
json_structures:
- name: Onfleet Task Structure
  property_count: 0
  slug: onfleet-task-structure
jsonld:
- class_count: 28
  name: Onfleet Context
  property_count: 18
  slug: onfleet-context
layout: provider
modified: '2026-05-25'
name: Onfleet
nav: Providers
network: true
overview: 'Onfleet publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Tasks API, Workers API, Route Plans API, and 6 more. Tagged areas include Last Mile Delivery, Logistics, Fleet Management, Dispatch, and Route Optimization.


  The Onfleet catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Onfleet''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, signup flow, and 44 more developer resources.'
plans:
- name: Onfleet Plans Pricing
  plan_count: 3
  slug: onfleet-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Onfleet Rate Limits
  slug: onfleet-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Onfleet API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: onfleet-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Onfleet API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: onfleet-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Onfleet API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: onfleet-rules
score:
  band: strong
  composite: 61.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 81.5
    catalog_earned_first_party: 0.0
    catalog_gap: 33.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 28.8
    contract_quality: 78.6
    developer_ergonomics: 57.1
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onfleet/refs/heads/main/screenshots/onfleet-2026-06-20T190721.png
security:
- kind: authentication
  name: Onfleet Authentication
  slug: onfleet-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Onfleet Domain Security
  slug: onfleet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Onfleet Vulnerability Disclosure
  slug: onfleet-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Onfleet Trust Center
  slug: onfleet-trust-center
  summary_line: ISO 27001, GDPR, FIPS 140
slug: onfleet
tags:
- Last Mile Delivery
- Logistics
- Fleet Management
- Dispatch
- Route Optimization
- Couriers
- Drivers
- Tracking
- Geocoding
- Webhook
- Artificial Intelligence
- Software-as-a-Service
website: https://onfleet.com
---
