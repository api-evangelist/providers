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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 65
  human_in_the_loop: 4
  name: Reolink Agentic Access
  operation_count: 65
  slug: reolink-agentic-access
  summary_line: 65 operations · 65 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: AI-powered object detection, auto-tracking, and autofocus
  name: Reolink AI API
  slug: reolink-ai-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Motion detection, audio alarms, and detection zone configuration
  name: Reolink Alarm API
  slug: reolink-alarm-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Login, logout, and session token management
  name: Reolink Authentication API
  slug: reolink-authentication-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Video stream encoding parameters and compression settings
  name: Reolink Encoding API
  slug: reolink-encoding-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Infrared, white light, and power indicator LED control
  name: Reolink LED API
  slug: reolink-led-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Network configuration, WiFi, DDNS, NTP, email, FTP, and push notifications
  name: Reolink Network API
  slug: reolink-network-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Pan-tilt-zoom control, presets, patrols, and calibration
  name: Reolink PTZ API
  slug: reolink-ptz-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Recording schedules, search, and playback
  name: Reolink Recording API
  slug: reolink-recording-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: User management and access control
  name: Reolink Security API
  slug: reolink-security-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Device information, maintenance, time settings, firmware, and storage
  name: Reolink System API
  slug: reolink-system-api
- baseURL_template: https://{camera_ip}
  baseurl_source: spec_template
  description: Image quality, OSD, ISP settings, privacy masks, and snapshot capture
  name: Reolink Video API
  slug: reolink-video-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reolink Camera HTTP AI API
  slug: open-reolink-ai-api
- collection_type: open
  name: Reolink Camera HTTP AI Alarm API
  slug: open-reolink-alarm-api
- collection_type: open
  name: Reolink Camera HTTP AI Authentication API
  slug: open-reolink-authentication-api
- collection_type: open
  name: Reolink Camera HTTP API
  slug: open-reolink-camera-api
- collection_type: open
  name: Reolink Camera HTTP AI Encoding API
  slug: open-reolink-encoding-api
- collection_type: open
  name: Reolink Camera HTTP AI LED API
  slug: open-reolink-led-api
- collection_type: open
  name: Reolink Camera HTTP AI Network API
  slug: open-reolink-network-api
- collection_type: open
  name: Reolink Camera HTTP AI PTZ API
  slug: open-reolink-ptz-api
- collection_type: open
  name: Reolink Camera HTTP AI Recording API
  slug: open-reolink-recording-api
- collection_type: open
  name: Reolink Camera HTTP AI Security API
  slug: open-reolink-security-api
- collection_type: open
  name: Reolink Camera HTTP AI System API
  slug: open-reolink-system-api
- collection_type: open
  name: Reolink Camera HTTP AI Video API
  slug: open-reolink-video-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reolink-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reolink-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reolink-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reolink-technology
- group: company
  title: ''
  type: Website
  url: https://reolink.com
- group: operate
  title: ''
  type: Forums
  url: https://community.reolink.com/
- group: operate
  title: ''
  type: Support
  url: https://support.reolink.com/
- group: company
  title: ''
  type: Blog
  url: https://reolink.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReolinkCameraAPI
created: '2025-01-01'
description: Reolink is a provider of security cameras and smart home surveillance technology. Their cameras offer an HTTP API that enables direct device control and configuration through JSON-based POST requests. The API supports comprehensive camera management including PTZ control, video encoding settings, recording search and playback, motion and AI-powered object detection, network configuration, LED control, and user authentication. The API is accessible on the local network via the device IP address.
examples:
- key_count: 4
  name: Reolink Login Example
  slug: reolink-login-example
- key_count: 4
  name: Reolink Ptz Control Example
  slug: reolink-ptz-control-example
finops:
- name: Reolink Finops
  service_category: API
  slug: reolink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reolink.png
json_schemas:
- name: Reolink Alarm Settings
  property_count: 6
  slug: alarm-settings
- name: Reolink Command Request
  property_count: 3
  slug: command-request
- name: Reolink Command Response
  property_count: 4
  slug: command-response
- name: Reolink Device Info
  property_count: 18
  slug: device-info
- name: Reolink Login
  property_count: 2
  slug: login
- name: Reolink Network Settings
  property_count: 3
  slug: network-settings
- name: Reolink PTZ Control
  property_count: 4
  slug: ptz-control
- name: Reolink Recording Search
  property_count: 5
  slug: recording-search
json_structures:
- name: Reolink Device Structure
  property_count: 0
  slug: reolink-device-structure
jsonld:
- class_count: 0
  name: Reolink Context
  property_count: 10
  slug: reolink-context
layout: provider
modified: '2026-05-19'
name: Reolink
nav: Providers
network: true
overview: 'Reolink publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AI API, Alarm API, Authentication API, and 8 more. Tagged areas include IoT, Security Cameras, Surveillance, Smart Home, and AI Detection.


  The Reolink catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Reolink''s developer surface includes authentication, support, engineering blog, and 6 more developer resources.'
plans:
- name: Reolink Plans Pricing
  plan_count: 3
  slug: reolink-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Reolink Rate Limits
  slug: reolink-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Reolink API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: reolink-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Reolink API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 4
  slug: reolink-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 63.5
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reolink/refs/heads/main/screenshots/reolink-2026-06-20T192902.png
security:
- kind: authentication
  name: Reolink Authentication
  slug: reolink-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reolink Domain Security
  slug: reolink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reolink
tags:
- IoT
- Security Cameras
- Surveillance
- Smart Home
- AI Detection
website: https://reolink.com
---
