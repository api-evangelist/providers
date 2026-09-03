---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 83
  human_in_the_loop: 0
  name: Golioth Agentic Access
  operation_count: 153
  slug: golioth-agentic-access
  summary_line: 153 operations · 83 acting
api_count: 1
apis:
- description: Per-device key/value state store. Devices and cloud services read and write structured state (JSON/CBOR) that is synchronized between device and cloud over CoAP.
  name: Golioth LightDB State
  slug: lightdb-state
- description: Time-series ingest endpoint for streaming sensor and telemetry data from devices. Stored data can be queried and routed downstream via Pipelines.
  name: Golioth LightDB Stream
  slug: lightdb-stream
- description: Bidirectional remote-procedure-call service. The cloud invokes device-side methods registered by firmware and receives the response, enabling on-demand diagnostics and control.
  name: Golioth Remote Procedure Call (RPC)
  slug: rpc
- description: Over-the-air firmware update service. Upload artifacts, group them into releases, target devices by tag or blueprint, and roll out updates with progress tracking and rollback.
  name: Golioth OTA Firmware Updates
  slug: ota
- description: Cloud-managed settings pushed to one device, a group, or an entire fleet. Firmware subscribes to settings keys and receives updates without requiring a firmware release.
  name: Golioth Device Settings
  slug: settings
- description: Centralized device logging. Firmware emits structured log lines that are collected, indexed, and made queryable via the console and API.
  name: Golioth Logging
  slug: logging
- description: Data routing and transformation engine. Pipelines describe how data arriving from devices is filtered, transformed, and forwarded to downstream destinations such as AWS S3, GCP Pub/Sub, Azure Event Hu
  name: Golioth Pipelines
  slug: pipelines
- description: Location service that resolves device position from cellular tower and Wi-Fi access-point observations submitted by firmware, returning latitude/longitude back to the device or downstream system.
  name: Golioth Location
  slug: location
- description: Open-source firmware SDK that connects embedded devices to the Golioth cloud over CoAP. Supports Zephyr RTOS, nRF Connect SDK, ESP-IDF, and ModusToolbox. Implements client APIs for LightDB State, Ligh
  name: Golioth Firmware SDK
  slug: firmware-sdk
- description: Python tooling that wraps the Management API for scripting, automation, and CLI-driven workflows against Golioth projects.
  name: Golioth Python Tools
  slug: python-tools
- description: Open-source implementation of the Model Context Protocol (MCP) for resource-constrained embedded devices, enabling large language models to observe and control firmware via MCP tools.
  name: Golioth tinymcp
  slug: tinymcp
- description: Non-IP device-to-cloud transport protocol from Golioth, with a companion Bluetooth gateway reference implementation (pouch-gateway) for relaying pouch traffic to the Golioth cloud.
  name: Golioth Pouch
  slug: pouch
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Access API from Golioth — 6 operation(s) for access.
  name: Golioth Access API
  slug: golioth-access-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The API Keys API from Golioth — 2 operation(s) for api keys.
  name: Golioth API Keys API
  slug: golioth-api-keys-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Artifacts API from Golioth — 3 operation(s) for artifacts.
  name: Golioth Artifacts API
  slug: golioth-artifacts-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Billing API from Golioth — 1 operation(s) for billing.
  name: Golioth Billing API
  slug: golioth-billing-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Blueprints API from Golioth — 2 operation(s) for blueprints.
  name: Golioth Blueprints API
  slug: golioth-blueprints-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Boards API from Golioth — 2 operation(s) for boards.
  name: Golioth Boards API
  slug: golioth-boards-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Certificates API from Golioth — 2 operation(s) for certificates.
  name: Golioth Certificates API
  slug: golioth-certificates-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Cohorts API from Golioth — 2 operation(s) for cohorts.
  name: Golioth Cohorts API
  slug: golioth-cohorts-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Credentials API from Golioth — 4 operation(s) for credentials.
  name: Golioth Credentials API
  slug: golioth-credentials-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Deployments API from Golioth — 2 operation(s) for deployments.
  name: Golioth Deployments API
  slug: golioth-deployments-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Devices API from Golioth — 2 operation(s) for devices.
  name: Golioth Devices API
  slug: golioth-devices-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Firmware API from Golioth — 1 operation(s) for firmware.
  name: Golioth Firmware API
  slug: golioth-firmware-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Integrations API from Golioth — 5 operation(s) for integrations.
  name: Golioth Integrations API
  slug: golioth-integrations-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The LightDB API from Golioth — 2 operation(s) for lightdb.
  name: Golioth LightDB API
  slug: golioth-lightdb-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The LightDB Stream API from Golioth — 2 operation(s) for lightdb stream.
  name: Golioth LightDB Stream API
  slug: golioth-lightdb-stream-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Location API from Golioth — 1 operation(s) for location.
  name: Golioth Location API
  slug: golioth-location-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Logs API from Golioth — 2 operation(s) for logs.
  name: Golioth Logs API
  slug: golioth-logs-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Networks API from Golioth — 4 operation(s) for networks.
  name: Golioth Networks API
  slug: golioth-networks-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Notifications API from Golioth — 1 operation(s) for notifications.
  name: Golioth Notifications API
  slug: golioth-notifications-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Organizations API from Golioth — 2 operation(s) for organizations.
  name: Golioth Organizations API
  slug: golioth-organizations-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The OTAEvents API from Golioth — 2 operation(s) for otaevents.
  name: Golioth OTAEvents API
  slug: golioth-otaevents-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Packages API from Golioth — 2 operation(s) for packages.
  name: Golioth Packages API
  slug: golioth-packages-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Pipelines API from Golioth — 5 operation(s) for pipelines.
  name: Golioth Pipelines API
  slug: golioth-pipelines-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The PKI API from Golioth — 5 operation(s) for pki.
  name: Golioth PKI API
  slug: golioth-pki-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Project Config API from Golioth — 2 operation(s) for project config.
  name: Golioth Project Config API
  slug: golioth-project-config-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Projects API from Golioth — 2 operation(s) for projects.
  name: Golioth Projects API
  slug: golioth-projects-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Provisioning API from Golioth — 2 operation(s) for provisioning.
  name: Golioth Provisioning API
  slug: golioth-provisioning-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Releases API from Golioth — 2 operation(s) for releases.
  name: Golioth Releases API
  slug: golioth-releases-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Remote Procedure Call API from Golioth — 1 operation(s) for remote procedure call.
  name: Golioth Remote Procedure Call API
  slug: golioth-remote-procedure-call-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Secrets API from Golioth — 2 operation(s) for secrets.
  name: Golioth Secrets API
  slug: golioth-secrets-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Settings API from Golioth — 4 operation(s) for settings.
  name: Golioth Settings API
  slug: golioth-settings-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Tags API from Golioth — 2 operation(s) for tags.
  name: Golioth Tags API
  slug: golioth-tags-api
- baseURL: https://api.golioth.io
  baseurl_source: declared
  description: The Usage API from Golioth — 5 operation(s) for usage.
  name: Golioth Usage API
  slug: golioth-usage-api
artifact_total: 99
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Golioth Management Access API
  slug: open-golioth-access-api
- collection_type: open
  name: Golioth Management Access API Keys API
  slug: open-golioth-api-keys-api
- collection_type: open
  name: Golioth Management Access Artifacts API
  slug: open-golioth-artifacts-api
- collection_type: open
  name: Golioth Management Access Billing API
  slug: open-golioth-billing-api
- collection_type: open
  name: Golioth Management Access Blueprints API
  slug: open-golioth-blueprints-api
- collection_type: open
  name: Golioth Management Access Boards API
  slug: open-golioth-boards-api
- collection_type: open
  name: Golioth Management Access Certificates API
  slug: open-golioth-certificates-api
- collection_type: open
  name: Golioth Management Access Cohorts API
  slug: open-golioth-cohorts-api
- collection_type: open
  name: Golioth Management Access Credentials API
  slug: open-golioth-credentials-api
- collection_type: open
  name: Golioth Management Access Deployments API
  slug: open-golioth-deployments-api
- collection_type: open
  name: Golioth Management Access Devices API
  slug: open-golioth-devices-api
- collection_type: open
  name: Golioth Management Access Firmware API
  slug: open-golioth-firmware-api
- collection_type: open
  name: Golioth Management Access Integrations API
  slug: open-golioth-integrations-api
- collection_type: open
  name: Golioth Management Access LightDB API
  slug: open-golioth-lightdb-api
- collection_type: open
  name: Golioth Management Access LightDB Stream API
  slug: open-golioth-lightdb-stream-api
- collection_type: open
  name: Golioth Management Access Location API
  slug: open-golioth-location-api
- collection_type: open
  name: Golioth Management Access Logs API
  slug: open-golioth-logs-api
- collection_type: open
  name: Golioth Management Access Networks API
  slug: open-golioth-networks-api
- collection_type: open
  name: Golioth Management Access Notifications API
  slug: open-golioth-notifications-api
- collection_type: open
  name: Golioth Management Access Organizations API
  slug: open-golioth-organizations-api
- collection_type: open
  name: Golioth Management Access OTAEvents API
  slug: open-golioth-otaevents-api
- collection_type: open
  name: Golioth Management Access Packages API
  slug: open-golioth-packages-api
- collection_type: open
  name: Golioth Management Access Pipelines API
  slug: open-golioth-pipelines-api
- collection_type: open
  name: Golioth Management Access PKI API
  slug: open-golioth-pki-api
- collection_type: open
  name: Golioth Management Access Project Config API
  slug: open-golioth-project-config-api
- collection_type: open
  name: Golioth Management Access Projects API
  slug: open-golioth-projects-api
- collection_type: open
  name: Golioth Management Access Provisioning API
  slug: open-golioth-provisioning-api
- collection_type: open
  name: Golioth Management Access Releases API
  slug: open-golioth-releases-api
- collection_type: open
  name: Golioth Management Access Remote Procedure Call API
  slug: open-golioth-remote-procedure-call-api
- collection_type: open
  name: Golioth Management Access Secrets API
  slug: open-golioth-secrets-api
- collection_type: open
  name: Golioth Management Access Settings API
  slug: open-golioth-settings-api
- collection_type: open
  name: Golioth Management Access Tags API
  slug: open-golioth-tags-api
- collection_type: open
  name: Golioth Management Access Usage API
  slug: open-golioth-usage-api
- collection_type: open
  name: Golioth Management API
  slug: open-golioth
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/golioth-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/golioth/golioth-firmware-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/golioth/golioth-firmware-sdk/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/golioth/golioth-firmware-sdk/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/golioth/golioth-firmware-sdk/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/golioth/golioth-firmware-sdk/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/golioth-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/golioth-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/golioth-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://golioth.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.golioth.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/golioth
- group: start
  title: ''
  type: Console
  url: https://console.golioth.io/
- group: operate
  title: ''
  type: Forums
  url: https://forum.golioth.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.golioth.io/
- group: learn
  title: ''
  type: Training
  url: https://training.golioth.io/
- group: docs
  title: ''
  type: ReferenceDesigns
  url: https://projects.golioth.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://golioth.io/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/golioth/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.golioth.io/llms.txt
created: '2026-05-23'
description: Golioth is an IoT device management cloud and firmware SDK for connected hardware. The platform pairs an open-source Firmware SDK (Zephyr RTOS, nRF Connect SDK, ESP-IDF, ModusToolbox, Linux) with a REST Management API at api.golioth.io, a web console, and services for OTA firmware updates, device settings, remote procedure calls (RPC), structured time-series data (LightDB Stream), key/value device state (LightDB State), logs, location, and a Pipelines data-routing engine that forwards device data to downstream cloud services. Authentication to the Management API is via project-scoped API keys passed in the x-api-key header.
examples:
- key_count: 4
  name: Golioth Create Device Example
  slug: golioth-create-device-example
- key_count: 4
  name: Golioth Create Pipeline Example
  slug: golioth-create-pipeline-example
- key_count: 4
  name: Golioth Create Release Example
  slug: golioth-create-release-example
- key_count: 4
  name: Golioth Invoke Rpc Example
  slug: golioth-invoke-rpc-example
- key_count: 4
  name: Golioth Query Stream Example
  slug: golioth-query-stream-example
finops:
- name: Golioth Finops
  service_category: API
  slug: golioth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/golioth.png
json_schemas:
- name: Golioth Device
  property_count: 11
  slug: golioth-device
- name: Golioth Release
  property_count: 9
  slug: golioth-release
- name: Golioth Stream Record
  property_count: 3
  slug: golioth-stream-record
json_structures:
- name: Golioth Device Structure
  property_count: 0
  slug: golioth-device-structure
- name: Golioth Release Structure
  property_count: 0
  slug: golioth-release-structure
jsonld:
- class_count: 0
  name: Golioth Context
  property_count: 15
  slug: golioth-context
layout: provider
modified: '2026-05-25'
name: Golioth
nav: Providers
network: true
overview: 'Golioth publishes 33 APIs on the [APIs.io](https://apis.io/) network, including Access API, API Keys API, Artifacts API, and 30 more. Tagged areas include IoT, Device Management, Firmware, Zephyr, and OTA.


  The Golioth catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Golioth''s developer surface includes authentication, documentation, GitHub presence, developer console, engineering blog, training material, pricing, and 13 more developer resources.'
plans:
- name: Golioth Plans Pricing
  plan_count: 1
  slug: golioth-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Golioth Rate Limits
  slug: golioth-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Golioth API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: golioth-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Golioth API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 2
    info: 0
    warn: 5
  slug: golioth-rules
score:
  band: developing
  composite: 47.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 34.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 64.6
    developer_ergonomics: 28.6
    discoverability: 70.4
    governance: 28.8
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 65.0
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 33
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/golioth/refs/heads/main/screenshots/golioth-2026-06-20T181951.png
security:
- kind: authentication
  name: Golioth Authentication
  slug: golioth-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Golioth Domain Security
  slug: golioth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: golioth
tags:
- IoT
- Device Management
- Firmware
- Zephyr
- OTA
- Embedded
- Connectivity
website: https://golioth.io/
---
