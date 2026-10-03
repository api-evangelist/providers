---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 31
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering consumer and commercial Internet of Things (IoT) platforms, smart home ecosystems, connected device APIs, and the messaging and edge protocols that bind them together. This collection focuses on cloud IoT services such as AWS IoT Core, smart home and connected device platforms like Google Nest, Tuya, IFTTT, and Reolink, MQTT brokers like HiveMQ and Mosquitto, edge runtimes like KubeEdge and LF Edge, and the standards and SDKs that connect millions of devices to APIs every day. Distinct from the Industrial topic, which focuses on OT and manufacturing systems.
examples:
- key_count: 12
  name: Internet Of Things Device Example
  slug: internet-of-things-device-example
- key_count: 11
  name: Internet Of Things Telemetry Event Example
  slug: internet-of-things-telemetry-event-example
features:
- description: IoT platforms issue per-device credentials, X.509 certificates, and identities so connected devices can authenticate to cloud services and to each other across the network.
  name: Device Identity and Provisioning
- description: Lightweight publish/subscribe messaging via MQTT, CoAP, and similar protocols is the dominant pattern for moving telemetry from constrained devices to cloud backends.
  name: MQTT and Pub/Sub Messaging
- description: Cloud IoT services maintain a virtual representation (shadow or twin) of each device that mirrors and synchronizes desired and reported state across intermittent connectivity.
  name: Device Shadows and State Synchronization
- description: IoT platforms include rules engines that filter, transform, and route incoming telemetry to databases, analytics services, notification channels, and downstream APIs.
  name: Rules Engines and Telemetry Routing
- description: Connected device platforms offer managed OTA firmware update delivery, rollout orchestration, and rollback for fleets ranging from a few units to millions.
  name: Over-the-Air (OTA) Firmware Updates
- description: Runtimes like AWS Greengrass, KubeEdge, and LF Edge push compute, ML inference, and message brokering to gateways and devices for low-latency local control.
  name: Edge Computing and Local Runtimes
- description: Smart home platforms expose device APIs and event triggers that enable cross-vendor automation, voice control, and consumer-facing routines like "good morning" or geofenced actions.
  name: Smart Home Integration and Automation
- description: LoRaWAN, cellular IoT, and similar long-range low-power networks connect battery-powered sensors and trackers that operate for years on a single charge.
  name: Long-Range Low-Power Connectivity
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Managed cloud service that brokers MQTT, HTTPS, and WebSocket connections from devices and routes messages to AWS services through a rules engine.
  name: AWS IoT Core
- description: Enterprise-grade MQTT broker platform used for connecting millions of IoT devices with extensions for Kafka, security, and observability.
  name: HiveMQ
- description: API platform for thermostats, cameras, and doorbells in the Google smart home ecosystem, exposing device state, events, and control.
  name: Google Nest
- description: Global IoT platform powering tens of thousands of branded smart home devices through unified cloud APIs and SDKs.
  name: Tuya
- description: Consumer automation platform that connects IoT devices, web apps, and services through user-authored conditional recipes.
  name: IFTTT
- description: Cloud-managed networking and IoT platform with APIs for cameras, environmental sensors, and Wi-Fi-connected device telemetry.
  name: Cisco Meraki
- description: Connected operations platform for vehicles, equipment, and sites with APIs for telemetry, video, and driver safety data.
  name: Samsara
- description: Open-source CNCF project extending Kubernetes orchestration to edge nodes and IoT devices for managed edge workloads.
  name: KubeEdge
json_schemas:
- name: Device
  property_count: 12
  slug: internet-of-things-device
- name: TelemetryEvent
  property_count: 11
  slug: internet-of-things-telemetry-event
json_structures:
- name: Internet Of Things Device Structure
  property_count: 12
  slug: internet-of-things-device-structure
- name: Internet Of Things Telemetry Event Structure
  property_count: 11
  slug: internet-of-things-telemetry-event-structure
jsonld:
- class_count: 14
  name: Internet Of Things Context
  property_count: 19
  slug: internet-of-things-context
layout: provider
modified: '2026-05-19'
name: Internet of Things
nav: Providers
network: true
overview: 'Internet of Things is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Smart Home, Connected Devices, MQTT, and LoRaWAN.


  The Internet of Things catalog on APIs.io includes 1 JSON-LD context.


  Internet of Things'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: internet-of-things
tags:
- IoT
- Smart Home
- Connected Devices
- MQTT
- LoRaWAN
- Edge
use_cases:
- description: Consumers connect lights, locks, cameras, thermostats, and voice assistants through platforms like Google Nest, Tuya, and IFTTT to create cross-device routines and remote control.
  name: Smart Home Automation
- description: Platforms like Reolink and Neolink expose APIs for live video, motion events, and recording management so security cameras can be integrated into broader home and business workflows.
  name: Connected Camera and Security
- description: Commercial IoT platforms like Samsara stream vehicle telemetry, location, and driver behavior to cloud dashboards and APIs for logistics and fleet management.
  name: Fleet and Asset Tracking
- description: AWS IoT Device Management and similar services let operators register, organize, monitor, and update millions of connected devices through a single API surface.
  name: Industrial-Grade Device Management at Scale
- description: MQTT brokers like HiveMQ and Mosquitto, combined with stream processors, ingest billions of telemetry events per day from devices into analytics and storage systems.
  name: Real-Time Telemetry Pipelines
- description: Edge runtimes like AWS Greengrass and KubeEdge run ML models close to devices for fast local decisions in industrial cameras, vehicles, and smart appliances.
  name: Edge AI and Local Inference
- description: Vehicle platforms and OEM APIs expose location, charging, and diagnostic data for electric vehicles and connected cars, enabling routing, charging, and maintenance integrations.
  name: Connected Mobility and EVs
- description: IFTTT and similar platforms let consumers wire IoT devices to web APIs through if-this-then-that recipes that span dozens of vendors and services.
  name: Event-Driven Consumer Automation
website: https://apievangelist.com
---
