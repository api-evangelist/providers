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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Adafruit Io Agentic Access
  operation_count: 71
  slug: adafruit-io-agentic-access
  summary_line: 71 operations · 42 acting
api_count: 12
apis:
- description: MQTT broker at io.adafruit.com for publish/subscribe access to Adafruit IO feeds and groups. TLS on port 8883, plaintext on 1883, and MQTT-over-WebSocket on port 443. Authenticate with your Adafruit I
  name: Adafruit IO MQTT API
  slug: adafruit-io-mqtt-api
- description: The Activities API from Adafruit IO — 2 operation(s) for activities.
  name: Adafruit IO Activities API
  slug: adafruit-io-activities-api
- description: The Blocks API from Adafruit IO — 2 operation(s) for blocks.
  name: Adafruit IO Blocks API
  slug: adafruit-io-blocks-api
- description: The Dashboards API from Adafruit IO — 2 operation(s) for dashboards.
  name: Adafruit IO Dashboards API
  slug: adafruit-io-dashboards-api
- description: The Data API from Adafruit IO — 14 operation(s) for data.
  name: Adafruit IO Data API
  slug: adafruit-io-data-api
- description: The Feeds API from Adafruit IO — 6 operation(s) for feeds.
  name: Adafruit IO Feeds API
  slug: adafruit-io-feeds-api
- description: The Groups API from Adafruit IO — 5 operation(s) for groups.
  name: Adafruit IO Groups API
  slug: adafruit-io-groups-api
- description: The Permissions API from Adafruit IO — 2 operation(s) for permissions.
  name: Adafruit IO Permissions API
  slug: adafruit-io-permissions-api
- description: The Tokens API from Adafruit IO — 2 operation(s) for tokens.
  name: Adafruit IO Tokens API
  slug: adafruit-io-tokens-api
- description: The Triggers API from Adafruit IO — 2 operation(s) for triggers.
  name: Adafruit IO Triggers API
  slug: adafruit-io-triggers-api
- description: The Users API from Adafruit IO — 2 operation(s) for users.
  name: Adafruit IO Users API
  slug: adafruit-io-users-api
- description: The Webhooks API from Adafruit IO — 2 operation(s) for webhooks.
  name: Adafruit IO Webhooks API
  slug: adafruit-io-webhooks-api
arazzos:
- description: Add an existing feed to a group, then list the group's feeds to confirm membership.
  name: Adafruit IO Attach Feed to Group
  slug: adafruit-io-attach-feed-to-group-workflow
- description: Bulk upload many data points to a feed, then fetch aggregated chart data for it.
  name: Adafruit IO Batch Ingest and Chart
  slug: adafruit-io-batch-ingest-and-chart-workflow
- description: Create a dashboard, add a visualization block to it, then read the block back.
  name: Adafruit IO Build Dashboard with Block
  slug: adafruit-io-build-dashboard-with-block-workflow
- description: Create a reactive trigger for the user, then read it back to confirm it exists.
  name: Adafruit IO Create and Verify Trigger
  slug: adafruit-io-create-and-verify-trigger-workflow
- description: Look up a feed by key and create it only when it is missing, then push a value.
  name: Adafruit IO Ensure Feed Exists
  slug: adafruit-io-ensure-feed-exists-workflow
- description: Create a group, add a new feed inside it, then write a data point to that grouped feed.
  name: Adafruit IO Group Feed Bootstrap
  slug: adafruit-io-group-feed-bootstrap-workflow
- description: Publish values to several feeds in a group at once, then read one feed's data back.
  name: Adafruit IO Group Multi-Feed Publish
  slug: adafruit-io-group-multifeed-publish-workflow
- description: Create a device token for the user, then read it back to confirm it was issued.
  name: Adafruit IO Issue and Verify Token
  slug: adafruit-io-issue-and-verify-token-workflow
- description: Create a feed, push an initial data point to it, then read the last value back.
  name: Adafruit IO Provision Feed and Seed Data
  slug: adafruit-io-provision-feed-and-seed-data-workflow
artifact_total: 60
collections:
- collection_type: postman
  name: Adafruit IO REST API
  slug: postman-adafruit-io-rest-api
- collection_type: open
  name: Adafruit IO REST API
  slug: open-adafruit-io-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adafruit-io-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adafruit-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adafruit-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adafruit-io-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adafruit-io/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-attach-feed-to-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-batch-ingest-and-chart-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-build-dashboard-with-block-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-create-and-verify-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-ensure-feed-exists-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-group-feed-bootstrap-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-group-multifeed-publish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-issue-and-verify-token-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adafruit-io-provision-feed-and-seed-data-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://io.adafruit.com
- group: docs
  title: ''
  type: Documentation
  url: https://io.adafruit.com/api/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://io.adafruit.com/api/docs/cookbook.html
- group: docs
  title: ''
  type: Documentation
  url: https://io.adafruit.com/api/docs/mqtt.html
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.adafruit.com/series/adafruit-io-basics
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.adafruit.com/welcome-to-adafruit-io
- group: company
  title: ''
  type: Blog
  url: https://io.adafruit.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://io.adafruit.com/blog/changelog/
- group: operate
  title: ''
  type: Forums
  url: https://forums.adafruit.com/viewforum.php?f=56
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/adafruit
- group: start
  title: ''
  type: Signup
  url: https://io.adafruit.com/signup
- group: start
  title: ''
  type: Login
  url: https://io.adafruit.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.adafruit.com/iot
- group: commercial
  title: ''
  type: Pricing
  url: https://io.adafruit.com/plus
- group: operate
  title: ''
  type: RateLimits
  url: https://io.adafruit.com/api/docs/#rate-limiting
- group: design
  title: ''
  type: ErrorCodes
  url: https://io.adafruit.com/api/docs/#errors
- group: auth
  title: ''
  type: Authentication
  url: https://io.adafruit.com/api/docs/#authentication
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adafruit.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adafruit.com/termsofservice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adafruit
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/adafruit/io-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/adafruit/Adafruit_IO_Python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/adafruit/Adafruit_IO_Arduino
- group: build
  title: ''
  type: SDKs
  url: https://github.com/adafruit/Adafruit_CircuitPython_AdafruitIO
- group: build
  title: ''
  type: SDKs
  url: https://github.com/adafruit/io-client-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/adafruit/adafruit-io-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/adafruit/io-client-go
- group: build
  title: ''
  type: Tools
  url: https://github.com/adafruit/Adafruit_MQTT_Library
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/adafruit/adafruit-io-basics
- group: build
  title: ''
  type: Tools
  url: https://github.com/adafruit/io-swagger-templates
- group: build
  title: ''
  type: Tools
  url: https://github.com/adafruit/adafruit-io-node-tunnel
- group: docs
  title: ''
  type: Documentation
  url: https://www.adafruit.com/category/1011
- group: docs
  title: ''
  type: Documentation
  url: https://www.adafruit.com/category/943
- group: docs
  title: ''
  type: Documentation
  url: https://learn.adafruit.com/welcome-to-circuitpython
- group: commercial
  title: ''
  type: Plans
  url: https://io.adafruit.com/plus
- group: commercial
  title: ''
  type: Plans
  url: plans/adafruit-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adafruit-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/adafruit-io-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Adafruit IO is a cloud Internet of Things platform from Adafruit Industries built for makers, hobbyists, students, and STEM educators. It provides feed-based time-series storage, drag-and-drop dashboards with 20+ visualization block types, actions/triggers for SMS/voice/email/webhook notifications, built-in services (time, weather, randomizer, air quality), and a complete REST + MQTT API surface for Adafruit Feather and Metro boards, ESP32 / ESP8266 / Pico microcontrollers, Raspberry Pi, and any other HTTP- or MQTT-capable hardware. First-class Arduino, CircuitPython, and Python client libraries plus the no-code Wippersnapper firmware make it the easiest way for hobbyists to get their projects onto the Internet of Things.
examples:
- key_count: 2
  name: Adafruit Io Batch Data Example
  slug: adafruit-io-batch-data-example
- key_count: 2
  name: Adafruit Io Create Data Example
  slug: adafruit-io-create-data-example
- key_count: 2
  name: Adafruit Io Create Feed Example
  slug: adafruit-io-create-feed-example
features:
- Feed-centric time-series datastore for IoT sensor and actuator values
- Drag-and-drop dashboards with 20+ block types (gauges, charts, toggles, sliders, maps, color pickers, image, indicators, text, number pad, selector, etc.)
- Feed groups for organizing related feeds and batch group writes
- Actions/Triggers — reactive triggers (threshold, equal, change) and scheduled actions (every N minutes, hours, daily, weekly)
- Webhook-in endpoints (standard, raw, notify) for ingesting data without an API key
- SMS, voice, email, and webhook notifications via actions (Plus tier)
- Built-in services — time service, randomizer, weather forecasts, air quality
- MQTT broker at io.adafruit.com with TLS (8883), plain (1883), and WebSocket (443) transports
- Adafruit IO Wippersnapper firmware — no-code MQTT firmware for ESP32, ESP8266, and Pico
- First-class Arduino and CircuitPython client libraries
- Public feed sharing and embeddable dashboards
- Permission/ACL primitive for fine-grained sharing of feeds, dashboards, and groups
- Personal access tokens for scoped, revocable credentials separate from the main API key
- Account activities log with type filtering
- Throttle topic to monitor rate-limit pressure programmatically
- Single comprehensive Swagger 2.0 / OpenAPI spec published in adafruit/io-api on GitHub
- IFTTT and Zapier integrations for cross-service automation
- Optimized for makers, hobbyists, and STEM education with Adafruit Feather, Metro, and Raspberry Pi hardware
finops:
- name: Adafruit Io Finops
  service_category: ''
  slug: adafruit-io-finops
graphqls:
- description: Conceptual GraphQL schema for the Adafruit IO IoT cloud platform. Adafruit IO provides feed-based time-series storage, drag-and-drop dashboards, reactive and scheduled triggers, MQTT and REST APIs, an
  name: Adafruit IO GraphQL Schema
  slug: adafruit-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/adafruit-io.png
json_schemas:
- name: Adafruit IO Dashboard
  property_count: 9
  slug: adafruit-io-dashboard
- name: Adafruit IO Data Point
  property_count: 13
  slug: adafruit-io-data
- name: Adafruit IO Feed
  property_count: 15
  slug: adafruit-io-feed
json_structures:
- name: Adafruit Io Dashboard Structure
  property_count: 0
  slug: adafruit-io-dashboard-structure
- name: Adafruit Io Feed Structure
  property_count: 0
  slug: adafruit-io-feed-structure
jsonld:
- class_count: 38
  name: Adafruit Io Context
  property_count: 8
  slug: adafruit-io-context
layout: provider
modified: '2026-05-25'
name: Adafruit IO
nav: Providers
network: true
overview: 'Adafruit IO publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Blocks API, Dashboards API, and 8 more. Tagged areas include IoT, Internet of Things, MQTT, Maker, and Hobbyist.


  The Adafruit IO catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Adafruit IO''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, signup flow, and 45 more developer resources.'
plans:
- name: Adafruit Io Plans Pricing
  plan_count: 3
  slug: adafruit-io-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 4
  name: Adafruit Io Rate Limits
  slug: adafruit-io-rate-limits
rules:
- name: Adafruit IO API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: adafruit-io-jsonschema-spectral-rules
- name: Adafruit IO API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 2
    info: 0
    warn: 5
  slug: adafruit-io-rules
score:
  band: exemplar
  composite: 67.6
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 69.3
    developer_ergonomics: 60.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 67.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adafruit-io/refs/heads/main/screenshots/adafruit-io-2026-06-20T164505.png
security:
- kind: authentication
  name: Adafruit Io Authentication
  slug: adafruit-io-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Adafruit Io Domain Security
  slug: adafruit-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Adafruit Io Vulnerability Disclosure
  slug: adafruit-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: adafruit-io
tags:
- IoT
- Internet of Things
- MQTT
- Maker
- Hobbyist
- CircuitPython
- Arduino
- ESP32
- Feather
- Dashboards
- Time Series
website: https://io.adafruit.com
---
