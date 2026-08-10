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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 445
  human_in_the_loop: 88
  name: Cisco Meraki Agentic Access
  operation_count: 957
  slug: cisco-meraki-agentic-access
  summary_line: 957 operations · 445 acting · 88 human-in-the-loop
api_count: 17
apis:
- description: Webhooks API for receiving real-time alerts and events from Meraki networks, including device, network, and security events delivered to configured HTTPS endpoints.
  name: Meraki Webhooks
  slug: webhooks
- description: The administered product area of the Cisco Meraki Dashboard API — 4 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Administered
  slug: administered
- description: The appliance product area of the Cisco Meraki Dashboard API — 157 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Appliance
  slug: appliance
- description: The camera product area of the Cisco Meraki Dashboard API — 46 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Camera
  slug: camera
- description: The campusGateway product area of the Cisco Meraki Dashboard API — 4 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — campusGateway
  slug: campusgateway
- description: The cellularGateway product area of the Cisco Meraki Dashboard API — 24 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — cellularGateway
  slug: cellulargateway
- description: The devices product area of the Cisco Meraki Dashboard API — 41 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Devices
  slug: devices
- description: The insight product area of the Cisco Meraki Dashboard API — 7 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Insight
  slug: insight
- description: The licensing product area of the Cisco Meraki Dashboard API — 8 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Licensing
  slug: licensing
- description: The networks product area of the Cisco Meraki Dashboard API — 115 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Networks
  slug: networks
- description: The organizations product area of the Cisco Meraki Dashboard API — 228 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Organizations
  slug: organizations
- description: The sensor product area of the Cisco Meraki Dashboard API — 19 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Sensor
  slug: sensor
- description: The sm product area of the Cisco Meraki Dashboard API — 49 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Sm
  slug: sm
- description: The spaces product area of the Cisco Meraki Dashboard API — 2 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Spaces
  slug: spaces
- description: The switch product area of the Cisco Meraki Dashboard API — 102 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Switch
  slug: switch
- description: The wireless product area of the Cisco Meraki Dashboard API — 136 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — Wireless
  slug: wireless
- description: The wirelessController product area of the Cisco Meraki Dashboard API — 15 operations, from Cisco's published OpenAPI definition (v1.72.0).
  name: Cisco Meraki Dashboard API — wirelessController
  slug: wirelesscontroller
artifact_total: 21
collections:
- collection_type: open
  name: Cisco Meraki Dashboard API
  slug: open-cisco-meraki
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-meraki-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-meraki-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-meraki-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cisco-meraki
- group: company
  title: ''
  type: Website
  url: https://meraki.cisco.com
- group: other
  title: ''
  type: Developer Hub
  url: https://developer.cisco.com/meraki/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.meraki.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meraki
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://github.com/meraki/openapi
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/meraki/dashboard-api-python
- group: operate
  title: ''
  type: Community
  url: https://community.meraki.com
- group: company
  title: ''
  type: Blog
  url: https://meraki.cisco.com/blog/feed/
created: '2026-05-11'
description: Cisco Meraki is a cloud-managed networking platform that provides wireless access points, switches, security appliances, cameras, sensors, and mobile device management from a single dashboard. The Meraki Dashboard API is a RESTful interface for programmatically managing and monitoring Meraki networks at scale, automating organization provisioning, device configuration, network operations, and analytics.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-meraki.png
layout: provider
modified: '2026-07-31'
name: Cisco Meraki
nav: Providers
network: true
overview: 'Cisco Meraki publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Dashboard API — Administered, Dashboard API — Appliance, Dashboard API — Camera, and 13 more. Tagged areas include Networking, Wireless, Switching, Security Appliances, and Cloud-Managed Networking.


  Cisco Meraki''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
random_paper: 47
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 63.6
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 16
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-meraki/refs/heads/main/screenshots/cisco-meraki-2026-06-20T174358.png
security:
- kind: authentication
  name: Cisco Meraki Authentication
  slug: cisco-meraki-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cisco Meraki Domain Security
  slug: cisco-meraki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cisco-meraki
tags:
- Networking
- Wireless
- Switching
- Security Appliances
- Cloud-Managed Networking
- MDM
- Cameras
- IoT
website: https://meraki.cisco.com
---
