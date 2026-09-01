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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Weavix Agentic Access
  operation_count: 19
  slug: weavix-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
apis:
- description: The Channels & Messaging API from Weavix — 4 operation(s) for channels & messaging.
  name: Weavix Channels & Messaging API
  slug: weavix-channels-messaging-api
- description: The Crafts API from Weavix — 1 operation(s) for crafts.
  name: Weavix Crafts API
  slug: weavix-crafts-api
- description: The Forms API from Weavix — 1 operation(s) for forms.
  name: Weavix Forms API
  slug: weavix-forms-api
- description: The Geofences API from Weavix — 1 operation(s) for geofences.
  name: Weavix Geofences API
  slug: weavix-geofences-api
- description: The Mass Alerts API from Weavix — 2 operation(s) for mass alerts.
  name: Weavix Mass Alerts API
  slug: weavix-mass-alerts-api
- description: The Permission Groups API from Weavix — 1 operation(s) for permission groups.
  name: Weavix Permission Groups API
  slug: weavix-permission-groups-api
- description: The Sites API from Weavix — 1 operation(s) for sites.
  name: Weavix Sites API
  slug: weavix-sites-api
- description: The User Management API from Weavix — 5 operation(s) for user management.
  name: Weavix User Management API
  slug: weavix-user-management-api
artifact_total: 23
asyncapis:
- description: ''
  name: Weavix Webhooks
  slug: weavix-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: weavix REST Channels & Messaging API
  slug: open-weavix-channels-messaging-api
- collection_type: open
  name: weavix REST Channels & Messaging Crafts API
  slug: open-weavix-crafts-api
- collection_type: open
  name: weavix REST Channels & Messaging Forms API
  slug: open-weavix-forms-api
- collection_type: open
  name: weavix REST Channels & Messaging Geofences API
  slug: open-weavix-geofences-api
- collection_type: open
  name: weavix REST Channels & Messaging Mass Alerts API
  slug: open-weavix-mass-alerts-api
- collection_type: open
  name: weavix REST Channels & Messaging Permission Groups API
  slug: open-weavix-permission-groups-api
- collection_type: open
  name: weavix REST Channels & Messaging Sites API
  slug: open-weavix-sites-api
- collection_type: open
  name: weavix REST Channels & Messaging User Management API
  slug: open-weavix-user-management-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/weavix-rest-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/weavix-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weavix-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weavix-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://weavix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.weavix.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://help.weavix.com/hc/en-us/articles/23496154594573-weavix-REST-API-Documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://help.weavix.com/hc/en-us/articles/45825355414669-Weavix-API-s
- group: operate
  title: ''
  type: Support
  url: https://help.weavix.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://weavix.com/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://weavix.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://console.weavix.com
- group: start
  title: ''
  type: SignUp
  url: https://weavix.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://weavix.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weavix.com/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.weavix.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/weavix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/weavix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/weavix-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/weavix-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/weavix-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/weavix-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weavix-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/weavix-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/weavix-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/weavix-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'weavix is the "Internet of Workers" frontline communication and workforce productivity platform, built around walt, a purpose-built smart radio for industrial deskless workers. It replaces traditional two-way radios with a connected system offering push-to-talk voice, picture and video messaging, real-time AI language translation across 40+ languages, man-down detection, location tracking, geofencing, mass alerts, and searchable conversation capture, running over existing Wi-Fi or LTE without FCC licensing. weavix serves manufacturing, construction, oil and gas, food and beverage, warehousing, logistics, aviation and other industrial sectors. Its public REST API lets administrators automate the platform from outside systems: sync users from HR/workforce systems, manage crafts, sites, geofences and permission groups, send messages to channels and individual users, pull message history and form submissions, and trigger mass alerts. weavix is headquartered in Wichita, Kansas and
  is backed by Insight Partners and Koch Disruptive Technologies.'
image: https://weavix.com/wp-content/uploads/2023/03/weavix-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Weavix MCP Server
  slug: weavix-mcp-server
modified: '2026-07-21'
name: Weavix
nav: Providers
network: true
overview: 'Weavix publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Channels & Messaging API, Crafts API, Forms API, and 5 more. Tagged areas include Communications, Frontline Workers, Workforce Management, Messaging, and Push To Talk.


  The Weavix catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Weavix''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 21.8
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weavix/refs/heads/main/screenshots/weavix-2026-08-17T082852.png
security:
- kind: authentication
  name: Weavix Authentication
  slug: weavix-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Weavix Domain Security
  slug: weavix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Weavix Trust Center
  slug: weavix-trust-center
  summary_line: SOC 2
slug: weavix
tags:
- Communications
- Frontline Workers
- Workforce Management
- Messaging
- Push To Talk
- Industrial
- Internet of Things
- Location Tracking
- Alerts
- Company
website: https://weavix.com/
---
