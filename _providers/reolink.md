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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 65
  human_in_the_loop: 4
  name: Reolink Agentic Access
  operation_count: 65
  slug: reolink-agentic-access
  summary_line: 65 operations · 65 acting · 4 human-in-the-loop
api_count: 11
apis:
- description: AI-powered object detection, auto-tracking, and autofocus
  name: Reolink AI API
  slug: reolink-ai-api
- description: Motion detection, audio alarms, and detection zone configuration
  name: Reolink Alarm API
  slug: reolink-alarm-api
- description: Login, logout, and session token management
  name: Reolink Authentication API
  slug: reolink-authentication-api
- description: Video stream encoding parameters and compression settings
  name: Reolink Encoding API
  slug: reolink-encoding-api
- description: Infrared, white light, and power indicator LED control
  name: Reolink LED API
  slug: reolink-led-api
- description: Network configuration, WiFi, DDNS, NTP, email, FTP, and push notifications
  name: Reolink Network API
  slug: reolink-network-api
- description: Pan-tilt-zoom control, presets, patrols, and calibration
  name: Reolink PTZ API
  slug: reolink-ptz-api
- description: Recording schedules, search, and playback
  name: Reolink Recording API
  slug: reolink-recording-api
- description: User management and access control
  name: Reolink Security API
  slug: reolink-security-api
- description: Device information, maintenance, time settings, firmware, and storage
  name: Reolink System API
  slug: reolink-system-api
- description: Image quality, OSD, ISP settings, privacy masks, and snapshot capture
  name: Reolink Video API
  slug: reolink-video-api
artifact_total: 32
collections:
- collection_type: open
  name: Reolink Camera HTTP API
  slug: open-reolink-camera-api
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
random_paper: 60
rate_limits:
- limit_count: 5
  name: Reolink Rate Limits
  slug: reolink-rate-limits
rules:
- name: Reolink API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: reolink-jsonschema-spectral-rules
- name: Reolink API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 4
  slug: reolink-rules
score:
  band: thin
  composite: 38.3
  delta: -8.4
  facets:
    commercial_clarity: 15.8
    contract_quality: 65.7
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
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
