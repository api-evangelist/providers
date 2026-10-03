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
description: An index and topic collection covering industrial APIs across industrial IoT (IIoT), operational technology (OT), SCADA, manufacturing, smart factory, asset management, predictive maintenance, energy management, and building automation. This collection profiles industrial cloud platforms (Siemens MindSphere, PTC ThingWorx, AWS IoT SiteWise, AWS IoT TwinMaker, AWS IoT Greengrass, Bosch IoT), historians and asset performance management tools (OSIsoft PI, AspenTech), edge and connector platforms (Litmus, Node-RED, HiveMQ, Aklivity), and the broader ecosystem of automation vendors (Rockwell Automation, Honeywell, Emerson, Schneider Electric) that expose APIs for plant data, equipment telemetry, work orders, and production runs. It anchors the OPC UA, MQTT Sparkplug B, and Modbus protocol family alongside the asset registry, telemetry, maintenance, and production data models that underpin modern industrial integration.
examples:
- key_count: 14
  name: Industrial Asset Example
  slug: industrial-asset-example
- key_count: 10
  name: Industrial Telemetry Reading Example
  slug: industrial-telemetry-reading-example
features:
- description: Industrial APIs expose hierarchical asset models for plants, lines, machines, and components, enabling normalized identification and tagging of physical equipment across SCADA, MES, and ERP systems.
  name: Asset and Equipment Registries
- description: Platforms like AWS IoT SiteWise, Amazon Timestream, and OSIsoft PI ingest high-frequency sensor readings from PLCs, gateways, and historians and expose them through query and streaming APIs.
  name: Telemetry Ingestion and Time-Series Storage
- description: Edge gateways and brokers (Litmus, HiveMQ, Aklivity, AWS IoT Greengrass) bridge OT protocols such as OPC UA, MQTT Sparkplug B, and Modbus into cloud-native API surfaces.
  name: OPC UA, MQTT, and Sparkplug B Connectivity
- description: Services like Amazon Lookout for Equipment and Amazon Monitron apply ML to vibration, temperature, and current signals to predict equipment failures and surface maintenance work orders.
  name: Predictive Maintenance and Anomaly Detection
- description: AWS IoT TwinMaker, Siemens MindSphere, and PTC ThingWorx assemble digital twin graphs that combine real-time telemetry, 3D scenes, and asset metadata into queryable APIs.
  name: Digital Twins and 3D Operational Context
- description: APIs expose work orders, production runs, batch records, OEE, and quality events to coordinate MES, ERP, and shop-floor systems across discrete and process manufacturing.
  name: Production Runs and Manufacturing Execution
- description: Schneider Electric, Honeywell, and Emerson APIs expose meter readings, HVAC controls, and energy-management workflows for industrial and commercial facilities.
  name: Energy and Building Automation
- description: AWS IoT Greengrass, Node-RED, and Litmus run containers and flows on industrial gateways, exposing local APIs for protocol translation, store-and-forward, and on-device analytics.
  name: Edge Compute and Local Orchestration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Managed industrial data service that collects, organizes, and analyzes equipment telemetry with hierarchical asset models and time-series APIs.
  name: AWS IoT SiteWise
- description: Digital twin service that combines 3D scenes, real-time data, and entity-relationship graphs into APIs for industrial operations.
  name: AWS IoT TwinMaker
- description: Edge runtime that runs Lambda functions, ML models, and connectors on industrial gateways with local APIs for protocol translation and store-and-forward.
  name: AWS IoT Greengrass
- description: Industrial IoT cloud platform that connects machines and physical infrastructure to APIs for asset management, fleet analytics, and predictive services.
  name: Siemens MindSphere
- description: Industrial IoT platform with APIs for asset modeling, mashups, augmented-reality work instructions, and manufacturing analytics.
  name: PTC ThingWorx
- description: De-facto industrial data historian with PI Web API endpoints for streaming, querying, and contextualizing decades of process and equipment data.
  name: OSIsoft PI System
- description: Industrial edge platform that connects PLCs, OPC UA servers, and MQTT brokers and exposes normalized data through cloud APIs.
  name: Litmus Automation
- description: Enterprise MQTT broker widely used in industrial deployments for Sparkplug B telemetry, device management, and edge-to-cloud messaging.
  name: HiveMQ
json_schemas:
- name: IndustrialAsset
  property_count: 14
  slug: industrial-asset
- name: IndustrialTelemetryReading
  property_count: 10
  slug: industrial-telemetry-reading
json_structures:
- name: Industrial Asset Structure
  property_count: 14
  slug: industrial-asset-structure
- name: Industrial Telemetry Reading Structure
  property_count: 10
  slug: industrial-telemetry-reading-structure
jsonld:
- class_count: 11
  name: Industrial Context
  property_count: 20
  slug: industrial-context
layout: provider
modified: '2026-05-19'
name: Industrial
nav: Providers
network: true
overview: 'Industrial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Industrial IoT, Manufacturing, OT, SCADA, and Asset Management.


  The Industrial catalog on APIs.io includes 1 JSON-LD context.


  Industrial''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 9.7
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
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 4.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: industrial
tags:
- Industrial IoT
- Manufacturing
- OT
- SCADA
- Asset Management
- Edge
- Predictive Maintenance
- Energy Management
- Smart Factory
use_cases:
- description: Industrial operators unify asset data from OSIsoft PI, AWS IoT SiteWise, and AspenTech into APIs that power asset performance dashboards, reliability programs, and condition-based maintenance.
  name: Plant-Wide Asset Performance Management
- description: Vibration and current data from pumps, motors, and compressors flows through Amazon Lookout for Equipment or Amazon Monitron APIs to predict failures and trigger work orders in CMMS systems.
  name: Predictive Maintenance for Rotating Equipment
- description: Manufacturers use Litmus, AWS IoT Greengrass, or HiveMQ to map OPC UA tags to MQTT Sparkplug B and stream normalized telemetry through cloud APIs for analytics and digital twins.
  name: OPC UA to Cloud Telemetry Pipelines
- description: APIs from PTC ThingWorx, Rockwell FactoryTalk, and Siemens MindSphere expose production runs, downtime events, and OEE metrics to MES dashboards and ERP work-order systems.
  name: Manufacturing Execution and OEE
- description: Schneider Electric and Honeywell APIs aggregate sub-meter, HVAC, and process-energy data into normalized feeds for sustainability and carbon-reporting platforms.
  name: Energy Management and Sustainability Reporting
- description: AWS IoT TwinMaker, Siemens MindSphere, and PTC ThingWorx APIs combine 3D scenes, asset hierarchies, and live telemetry for remote operations, training, and root-cause analysis.
  name: Digital Twin Operations
- description: Operators expose decades of PI System and AspenTech historian data through cloud APIs to power machine learning, anomaly detection, and process-optimization workflows.
  name: Industrial Data Historian Modernization
- description: Edge platforms like Litmus and Node-RED ingest Modbus, EtherNet/IP, and serial protocols at the gateway and republish them as MQTT, OPC UA, or REST APIs for upstream systems.
  name: Edge Protocol Translation
website: https://apievangelist.com
---
