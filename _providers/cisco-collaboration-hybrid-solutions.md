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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Cisco Collaboration Hybrid Solutions Agentic Access
  operation_count: 25
  slug: cisco-collaboration-hybrid-solutions-agentic-access
  summary_line: 25 operations · 14 acting
api_count: 12
apis:
- description: Schedule, list, update, and cancel Webex meetings; manage participants, recordings, transcripts, and meeting templates.
  name: Webex Meetings API
  slug: webex-meetings
- description: Manage Webex Hybrid Calendar, Hybrid Call Service, Hybrid Message, Video Mesh nodes, and other connectors that bridge on-premises collaboration infrastructure to the Webex cloud.
  name: Webex Hybrid Services API
  slug: webex-hybrid-services
- description: Cloud calling capabilities including call control, dial plans, voicemail, voice portals, queues, hunt groups, and number provisioning.
  name: Webex Calling API
  slug: webex-calling
- description: Administer Webex organizations, users, licenses, audit events, and service settings programmatically.
  name: Control Hub API
  slug: control-hub
- description: Manage and control Webex Room and Desk Devices including remote configuration, status queries, and the device-side xAPI.
  name: Webex Devices API
  slug: webex-devices
- description: Create and manage Webex Webinars and large-format virtual events, including registration, panelists, and analytics.
  name: Webex Events API
  slug: webex-events
- description: The Devices API from Cisco Collaboration Hybrid Solutions — 1 operation(s) for devices.
  name: Cisco Collaboration Hybrid Solutions Devices API
  slug: cisco-collaboration-hybrid-solutions-devices-api
- description: The Memberships API from Cisco Collaboration Hybrid Solutions — 2 operation(s) for memberships.
  name: Cisco Collaboration Hybrid Solutions Memberships API
  slug: cisco-collaboration-hybrid-solutions-memberships-api
- description: The Messages API from Cisco Collaboration Hybrid Solutions — 2 operation(s) for messages.
  name: Cisco Collaboration Hybrid Solutions Messages API
  slug: cisco-collaboration-hybrid-solutions-messages-api
- description: The Rooms API from Cisco Collaboration Hybrid Solutions — 2 operation(s) for rooms.
  name: Cisco Collaboration Hybrid Solutions Rooms API
  slug: cisco-collaboration-hybrid-solutions-rooms-api
- description: The Teams API from Cisco Collaboration Hybrid Solutions — 2 operation(s) for teams.
  name: Cisco Collaboration Hybrid Solutions Teams API
  slug: cisco-collaboration-hybrid-solutions-teams-api
- description: The Webhooks API from Cisco Collaboration Hybrid Solutions — 2 operation(s) for webhooks.
  name: Cisco Collaboration Hybrid Solutions Webhooks API
  slug: cisco-collaboration-hybrid-solutions-webhooks-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cisco Webex Platform API (Collaboration Hybrid Solutions) Devices API
  slug: open-cisco-collaboration-hybrid-solutions-devices-api
- collection_type: open
  name: Cisco Webex Platform API (Collaboration Hybrid Solutions) Devices Memberships API
  slug: open-cisco-collaboration-hybrid-solutions-memberships-api
- collection_type: open
  name: Cisco Webex Platform API (Collaboration Hybrid Solutions) Devices Messages API
  slug: open-cisco-collaboration-hybrid-solutions-messages-api
- collection_type: open
  name: Cisco Webex Platform API (Collaboration Hybrid Solutions) Devices Rooms API
  slug: open-cisco-collaboration-hybrid-solutions-rooms-api
- collection_type: open
  name: Cisco Webex Platform API (Collaboration Hybrid Solutions) Devices Teams API
  slug: open-cisco-collaboration-hybrid-solutions-teams-api
- collection_type: open
  name: Cisco Webex Platform API (Collaboration Hybrid Solutions) Devices Webhooks API
  slug: open-cisco-collaboration-hybrid-solutions-webhooks-api
- collection_type: open
  name: Cisco Webex Platform API (Collaboration Hybrid Solutions)
  slug: open-cisco-collaboration-hybrid-solutions
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-collaboration-hybrid-solutions-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-collaboration-hybrid-solutions-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-collaboration-hybrid-solutions-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.webex.com/feed/
created: '2024-01-15'
description: APIs for Cisco's hybrid collaboration solutions that combine Webex cloud services with on-premises Unified Communications Manager (CUCM), Expressway, and supporting infrastructure. Hybrid Services let an organization keep calling, calendaring, and identity on-premises while using Webex for meetings, messaging, devices, and management.
finops:
- name: Cisco Collaboration Hybrid Solutions Finops
  service_category: API
  slug: cisco-collaboration-hybrid-solutions-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-collaboration-hybrid-solutions.png
jsonld:
- class_count: 0
  name: Cisco Collaboration Context
  property_count: 7
  slug: cisco-collaboration-context
layout: provider
modified: '2026-04-23'
name: Cisco Collaboration Hybrid Solutions
nav: Providers
network: true
overview: 'Cisco Collaboration Hybrid Solutions publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Memberships API, Messages API, and 3 more. Tagged areas include Calling, Collaboration, Hybrid Cloud, Meetings, and Messaging.


  The Cisco Collaboration Hybrid Solutions catalog on APIs.io includes 1 JSON-LD context.


  Cisco Collaboration Hybrid Solutions'' developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Cisco Collaboration Hybrid Solutions Plans Pricing
  plan_count: 3
  slug: cisco-collaboration-hybrid-solutions-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 5
  name: Cisco Collaboration Hybrid Solutions Rate Limits
  slug: cisco-collaboration-hybrid-solutions-rate-limits
score:
  band: thin
  composite: 28.9
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 59.0
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-collaboration-hybrid-solutions/refs/heads/main/screenshots/cisco-collaboration-hybrid-solutions-2026-06-20T174354.png
security:
- kind: authentication
  name: Cisco Collaboration Hybrid Solutions Authentication
  slug: cisco-collaboration-hybrid-solutions-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cisco Collaboration Hybrid Solutions Domain Security
  slug: cisco-collaboration-hybrid-solutions-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cisco-collaboration-hybrid-solutions
tags:
- Calling
- Collaboration
- Hybrid Cloud
- Meetings
- Messaging
- Unified Communications
- Webex
---
