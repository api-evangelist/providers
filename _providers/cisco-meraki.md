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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Cisco Meraki Agentic Access
  operation_count: 24
  slug: cisco-meraki-agentic-access
  summary_line: 24 operations · 11 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Webhooks API for receiving real-time alerts and events from Meraki networks, including device, network, and security events delivered to configured HTTPS endpoints.
  name: Meraki Webhooks
  slug: webhooks
- description: The Appliance API from Cisco Meraki — 1 operation(s) for appliance.
  name: Cisco Meraki Appliance API
  slug: cisco-meraki-appliance-api
- description: The Camera API from Cisco Meraki — 1 operation(s) for camera.
  name: Cisco Meraki Camera API
  slug: cisco-meraki-camera-api
- description: The Devices API from Cisco Meraki — 4 operation(s) for devices.
  name: Cisco Meraki Devices API
  slug: cisco-meraki-devices-api
- description: The LiveTools API from Cisco Meraki — 1 operation(s) for livetools.
  name: Cisco Meraki LiveTools API
  slug: cisco-meraki-livetools-api
- description: The Networks API from Cisco Meraki — 3 operation(s) for networks.
  name: Cisco Meraki Networks API
  slug: cisco-meraki-networks-api
- description: The Organizations API from Cisco Meraki — 2 operation(s) for organizations.
  name: Cisco Meraki Organizations API
  slug: cisco-meraki-organizations-api
- description: The Switch API from Cisco Meraki — 2 operation(s) for switch.
  name: Cisco Meraki Switch API
  slug: cisco-meraki-switch-api
- description: The Wireless API from Cisco Meraki — 2 operation(s) for wireless.
  name: Cisco Meraki Wireless API
  slug: cisco-meraki-wireless-api
artifact_total: 13
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
modified: '2026-05-11'
name: Cisco Meraki
nav: Providers
network: true
overview: 'Cisco Meraki publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Appliance API, Camera API, Devices API, and 5 more. Tagged areas include Networking, Wireless, Switching, Security Appliances, and Cloud-Managed Networking.


  Cisco Meraki''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
random_paper: 51
score:
  band: thin
  composite: 30.0
  delta: 3.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 51.3
    developer_ergonomics: 32.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.8
  schema_version: 0.5
  scored_at: '2026-07-27'
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
