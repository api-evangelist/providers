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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Thingspeak Agentic Access
  operation_count: 21
  slug: thingspeak-agentic-access
  summary_line: 21 operations · 9 acting
api_count: 2
apis:
- description: List, create, read, update, and delete ThingSpeak channels — the primary container for time-series IoT data. Each channel holds up to eight numeric fields plus latitude, longitude, elevation, and a st
  name: ThingSpeak Channels API
  slug: thingspeak-channels-api
- description: Write a single channel entry via `/update` or push high-volume telemetry via `/channels/{channel_id}/bulk_update.json` (CSV or JSON batches). The write surface is the workhorse of every ThingSpeak dev
  name: ThingSpeak Update API
  slug: thingspeak-update-api
- description: Lightweight pub/sub MQTT broker at `mqtt3.thingspeak.com` over TCP (1883), TLS (8883), WebSocket (80), and secure WebSocket (443, path `/mqtt`). Publish to `channels/{channelID}/publish` and subscribe
  name: ThingSpeak MQTT API
  slug: thingspeak-mqtt-api
- description: 'React lets channels react to incoming data — running ThingHTTP requests, MATLAB Analysis snippets, TalkBack commands, or Twitter/Tweet posts when conditions (numeric threshold, string match, no-data) '
  name: ThingSpeak React API
  slug: thingspeak-react-api
- description: Send email alerts from a channel via the alerts API or React, and retrieve alert history. Useful for environmental monitoring, threshold-based warnings, and inactivity notifications.
  name: ThingSpeak Alerts API
  slug: thingspeak-alerts-api
- description: 'Server-rendered chart embeds for any channel/field — line, bar, column, spline — with parameters for color, scale, axis, timezone, title, bgcolor, transparent, and dynamic options. Returns embeddable '
  name: ThingSpeak Charts API
  slug: thingspeak-charts-api
- description: 'Run scheduled or React-triggered MATLAB code against channel data — the differentiator that separates ThingSpeak from generic MQTT brokers. Read channel data with `thingSpeakRead`, write results back '
  name: ThingSpeak MATLAB Analysis API
  slug: thingspeak-matlab-analysis-api
- description: Generate custom plots from MATLAB code and embed them on ThingSpeak channel pages or external dashboards. Supports `plotyy`, `geoplot`, `histogram`, custom colormaps, and any other MATLAB plotting pri
  name: ThingSpeak MATLAB Visualization API
  slug: thingspeak-matlab-visualization-api
- description: Outbound HTTP requests stored as named "ThingHTTP" actions and fired by React, TimeControl, or device pollers. Lets ThingSpeak push data into third-party services (Twilio, IFTTT, custom webhooks) with
  name: ThingSpeak ThingHTTP API
  slug: thingspeak-thinghttp-api
- description: Cron-style scheduler that fires ThingHTTP, TalkBack, or MATLAB Analysis actions at a chosen time, recurring frequency, or after a delay. Pairs with React and TalkBack to close the IoT control loop.
  name: ThingSpeak TimeControl API
  slug: thingspeak-timecontrol-api
- description: The Channels.json API from ThingSpeak — 1 operation(s) for channels.json.
  name: ThingSpeak Channels.json API
  slug: thingspeak-channels-json-api
- description: The Talkbacks API from ThingSpeak — 3 operation(s) for talkbacks.
  name: ThingSpeak Talkbacks API
  slug: thingspeak-talkbacks-api
arazzos:
- description: Upload a batch of cached readings, then read a single field's recent feed.
  name: ThingSpeak Bulk Update and Read Field Feed
  slug: thingspeak-bulk-update-and-read-field-feed-workflow
- description: Clear all feed entries from a channel, then delete the channel itself.
  name: ThingSpeak Decommission Channel
  slug: thingspeak-decommission-channel-workflow
- description: Search public channels by tag, then read the feed of the first match.
  name: ThingSpeak Discover Public Channel and Read Feed
  slug: thingspeak-discover-public-channel-and-read-feed-workflow
- description: Read a channel's settings, then pull an averaged feed over a recent window.
  name: ThingSpeak Inspect Channel and Aggregate Feed
  slug: thingspeak-inspect-channel-and-aggregate-feed-workflow
- description: List the user's channels, then read recent feed entries from the first channel.
  name: ThingSpeak List Channels and Read Feed
  slug: thingspeak-list-channels-and-read-feed-workflow
- description: Write an entry carrying a status message, then read the channel's status update feed.
  name: ThingSpeak Post Status and Read Status Updates
  slug: thingspeak-post-status-and-read-status-updates-workflow
- description: Create a new channel, write an initial entry to it, then read that entry back.
  name: ThingSpeak Provision Channel and Seed First Reading
  slug: thingspeak-provision-channel-and-seed-reading-workflow
- description: Add a command to a TalkBack queue, then dequeue it as a device would.
  name: ThingSpeak Queue and Execute TalkBack Command
  slug: thingspeak-queue-and-execute-talkback-command-workflow
- description: Update a channel's field label, then read the last value for that field.
  name: ThingSpeak Relabel Field and Read Last Field Entry
  slug: thingspeak-relabel-field-and-read-last-field-entry-workflow
- description: Queue a command, revise its text before a device runs it, then read it back.
  name: ThingSpeak Revise Queued TalkBack Command
  slug: thingspeak-revise-queued-talkback-command-workflow
- description: List a TalkBack queue, then delete the first command to keep the queue tidy.
  name: ThingSpeak Sweep Executed TalkBack Commands
  slug: thingspeak-sweep-executed-talkback-commands-workflow
- description: Post a new feed entry via the form-encoded update endpoint, then read the last entry back.
  name: ThingSpeak Write Update and Read Last Entry
  slug: thingspeak-write-update-and-read-last-entry-workflow
artifact_total: 72
asyncapis:
- description: ThingSpeak's MQTT broker at `mqtt3.thingspeak.com`. Devices publish channel updates and subscribe to channel/field feeds using MQTT credentials (Client ID, Username, Password) provisioned in the Thing
  name: ThingSpeak MQTT API
  slug: thingspeak-mqtt-asyncapi
collections:
- collection_type: postman
  name: ThingSpeak Channels API
  slug: postman-thingspeak-channels-api
- collection_type: postman
  name: ThingSpeak Feeds API
  slug: postman-thingspeak-feeds-api
- collection_type: postman
  name: ThingSpeak TalkBack API
  slug: postman-thingspeak-talkback-api
- collection_type: postman
  name: ThingSpeak Update API
  slug: postman-thingspeak-update-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ThingSpeak Channels API
  slug: open-thingspeak-channels-api
- collection_type: open
  name: ThingSpeak Channels Channels.json API
  slug: open-thingspeak-channels-json-api
- collection_type: open
  name: ThingSpeak Feeds API
  slug: open-thingspeak-feeds-api
- collection_type: open
  name: ThingSpeak TalkBack API
  slug: open-thingspeak-talkback-api
- collection_type: open
  name: ThingSpeak Channels Talkbacks API
  slug: open-thingspeak-talkbacks-api
- collection_type: open
  name: ThingSpeak Channels Update API
  slug: open-thingspeak-update-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thingspeak-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thingspeak-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thingspeak-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thingspeak/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-bulk-update-and-read-field-feed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-decommission-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-discover-public-channel-and-read-feed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-inspect-channel-and-aggregate-feed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-list-channels-and-read-feed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-post-status-and-read-status-updates-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-provision-channel-and-seed-reading-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-queue-and-execute-talkback-command-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-relabel-field-and-read-last-field-entry-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-revise-queued-talkback-command-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-sweep-executed-talkback-commands-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/thingspeak-write-update-and-read-last-entry-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://thingspeak.mathworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mathworks.com/help/thingspeak/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mathworks.com/help/thingspeak/rest-api.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.mathworks.com/help/thingspeak/mqtt-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mathworks.com/help/thingspeak/get-started-with-thingspeak.html
- group: start
  title: ''
  type: Signup
  url: https://thingspeak.mathworks.com/login
- group: start
  title: ''
  type: Signup
  url: https://www.mathworks.com/mwaccount/register
- group: commercial
  title: ''
  type: Pricing
  url: https://thingspeak.mathworks.com/prices
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thingspeak.mathworks.com/pages/license_faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mathworks.com/company/aboutus/policies_statements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mathworks.com/company/aboutus/policies_statements/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.mathworks.com/support/contact_us.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mathworks
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mathworks/thingspeak-arduino
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mathworks/thingspeak-particle
- group: build
  title: ''
  type: SDKs
  url: https://www.mathworks.com/matlabcentral/fileexchange/52244-thingspeak-support-from-desktop-matlab
- group: learn
  title: ''
  type: Tutorials
  url: https://www.mathworks.com/help/thingspeak/use-arduino-client-to-publish-to-a-channel.html
- group: learn
  title: ''
  type: Tutorials
  url: https://www.mathworks.com/help/thingspeak/raspberry-pi-tutorials.html
- group: learn
  title: ''
  type: Tutorials
  url: https://www.mathworks.com/help/thingspeak/esp32-tutorials.html
- group: learn
  title: ''
  type: Tutorials
  url: https://www.mathworks.com/help/thingspeak/esp8266-tutorials.html
- group: learn
  title: ''
  type: Tutorials
  url: https://www.mathworks.com/help/thingspeak/particle-photon-tutorials.html
- group: operate
  title: ''
  type: Forums
  url: https://www.mathworks.com/matlabcentral/answers/index?term=tag%3Athingspeak
- group: operate
  title: ''
  type: Community
  url: https://www.mathworks.com/matlabcentral/communitycontests/contests/4/entries
- group: company
  title: ''
  type: Blog
  url: https://blogs.mathworks.com/iot/
- group: other
  title: ''
  type: ProductPage
  url: https://www.mathworks.com/products/thingspeak.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-mathworks_2/
- group: other
  title: ''
  type: X
  url: https://x.com/MATLAB
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/MATLAB
- group: commercial
  title: ''
  type: Plans
  url: https://plans/thingspeak-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://rate-limits/thingspeak-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://finops/thingspeak-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: ThingSpeak is an IoT analytics platform from MathWorks that lets devices aggregate, visualize, and analyze live data streams in the cloud. Devices push telemetry to channels via a REST update endpoint or the `mqtt3.thingspeak.com` MQTT broker, and the platform layers in MATLAB Analysis for compute, MATLAB Visualizations for plotting, React for rules, TalkBack for cloud-to-device commands, ThingHTTP for outbound webhooks, and TimeControl for scheduling. ThingSpeak is the only mainstream IoT platform with first-class MATLAB and Simulink integration, making it widely used in academic research, environmental monitoring, smart agriculture, and energy applications. Compatible with Arduino, ESP8266/ESP32, Raspberry Pi, Particle, LoRaWAN gateways, and industrial controllers.
examples:
- key_count: 2
  name: Thingspeak Bulk Update Example
  slug: thingspeak-bulk-update-example
- key_count: 6
  name: Thingspeak Mqtt Publish Example
  slug: thingspeak-mqtt-publish-example
- key_count: 2
  name: Thingspeak Read Channel Feed Example
  slug: thingspeak-read-channel-feed-example
- key_count: 2
  name: Thingspeak Talkback Execute Example
  slug: thingspeak-talkback-execute-example
- key_count: 2
  name: Thingspeak Update Channel Example
  slug: thingspeak-update-channel-example
features:
- IoT analytics platform from MathWorks integrating natively with MATLAB and Simulink
- Channels with up to eight numeric fields plus latitude, longitude, elevation, and status string
- REST API over `api.thingspeak.com` for channel CRUD, feed read/write, and bulk updates
- MQTT broker at `mqtt3.thingspeak.com` on ports 1883 / 8883 / 80 / 443 (WebSocket path `/mqtt`)
- MATLAB Analysis app for scheduled/triggered compute against channel data
- MATLAB Visualizations app for custom embeddable plots
- React app providing a rules engine triggered by channel data conditions
- TalkBack queue for asynchronous cloud-to-device command delivery
- ThingHTTP for outbound webhooks to third-party services
- TimeControl scheduler (cron-like) for periodic actions
- Server-rendered chart embeds via the Charts API
- Email alerts via the Alerts surface
- Public and private channels with read/write API keys
- Bulk update endpoint for high-volume devices (JSON and CSV batches)
- Native client libraries for Arduino, ESP8266, ESP32, and Particle
- Free tier (~3M messages/year) plus Standard, Home, Academic, and Student licenses
- 33M messages/year per paid unit (~90,400 messages/day)
- Inactivity monitoring and last-entry timestamps for device health
- Sharing channels publicly via read-only links and embedding charts in third-party sites
finops:
- name: Thingspeak Finops
  service_category: ''
  slug: thingspeak-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thingspeak.png
json_schemas:
- name: ThingSpeak Channel
  property_count: 21
  slug: thingspeak-channel
- name: ThingSpeak Feed Entry
  property_count: 14
  slug: thingspeak-feed
jsonld:
- class_count: 26
  name: Thingspeak Context
  property_count: 3
  slug: thingspeak-context
layout: provider
modified: '2026-05-25'
name: ThingSpeak
nav: Providers
network: true
overview: 'ThingSpeak publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Update API, MQTT API, and 2 more. Tagged areas include IoT, Internet of Things, Analytics, Time Series, and MQTT.


  The ThingSpeak catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  ThingSpeak''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, support, and 40 more developer resources.'
plans:
- name: Thingspeak Plans Pricing
  plan_count: 5
  slug: thingspeak-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 8
  name: Thingspeak Rate Limits
  slug: thingspeak-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: ThingSpeak API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 7
  slug: thingspeak-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: ThingSpeak API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: thingspeak-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: ThingSpeak API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: thingspeak-rules
score:
  band: strong
  composite: 62.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 32.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 13.6
    contract_quality: 71.2
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 36.8
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thingspeak/refs/heads/main/screenshots/thingspeak-2026-06-20T195303.png
security:
- kind: authentication
  name: Thingspeak Authentication
  slug: thingspeak-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Thingspeak Domain Security
  slug: thingspeak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: thingspeak
tags:
- IoT
- Internet of Things
- Analytics
- Time Series
- MQTT
- MATLAB
- Sensors
- Telemetry
website: https://thingspeak.mathworks.com/
---
