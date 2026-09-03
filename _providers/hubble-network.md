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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Hubble Network Agentic Access
  operation_count: 39
  slug: hubble-network-agentic-access
  summary_line: 39 operations · 19 acting
api_count: 2
apis:
- baseURL: https://api.hubble.com
  baseurl_source: declared
  description: The API Keys API from Hubble Network — 4 operation(s) for api keys.
  name: Hubble Network API Keys API
  slug: hubble-network-api-keys-api
- baseURL: https://api.hubble.com
  baseurl_source: declared
  description: The Billing API from Hubble Network — 6 operation(s) for billing.
  name: Hubble Network Billing API
  slug: hubble-network-billing-api
- baseURL: https://api.hubble.com
  baseurl_source: declared
  description: The Devices API from Hubble Network — 3 operation(s) for devices.
  name: Hubble Network Devices API
  slug: hubble-network-devices-api
- baseURL: https://api.hubble.com
  baseurl_source: declared
  description: The Organizations API from Hubble Network — 4 operation(s) for organizations.
  name: Hubble Network Organizations API
  slug: hubble-network-organizations-api
- baseURL: https://api.hubble.com
  baseurl_source: declared
  description: The Packet Webhooks API from Hubble Network — 3 operation(s) for packet webhooks.
  name: Hubble Network Packet Webhooks API
  slug: hubble-network-packet-webhooks-api
- baseURL: https://api.hubble.com
  baseurl_source: declared
  description: The Packets API from Hubble Network — 2 operation(s) for packets.
  name: Hubble Network Packets API
  slug: hubble-network-packets-api
- baseURL: https://api.hubble.com
  baseurl_source: declared
  description: The Platform Metrics API from Hubble Network — 4 operation(s) for platform metrics.
  name: Hubble Network Platform Metrics API
  slug: hubble-network-platform-metrics-api
artifact_total: 33
asyncapis:
- description: ''
  name: Hubble Network Packet Webhooks
  slug: hubble-network-packet-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hubble Platform API Keys API
  slug: open-hubble-network-api-keys-api
- collection_type: open
  name: Hubble Platform Billing API
  slug: open-hubble-network-billing-api
- collection_type: open
  name: Hubble Platform Devices API
  slug: open-hubble-network-devices-api
- collection_type: open
  name: Hubble Platform Organizations API
  slug: open-hubble-network-organizations-api
- collection_type: open
  name: Hubble Platform Packet Webhooks API
  slug: open-hubble-network-packet-webhooks-api
- collection_type: open
  name: Hubble Platform Packets API
  slug: open-hubble-network-packets-api
- collection_type: open
  name: Hubble Platform Platform Metrics API
  slug: open-hubble-network-platform-metrics-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hubble-network-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hubble-network-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hubble-network-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hubble-network-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://hubble.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hubble.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://hubble.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://hubble.com/docs/api-specification/hubble-platform-api
- group: start
  title: ''
  type: GettingStarted
  url: https://hubble.com/docs/intro
- group: operate
  title: ''
  type: Support
  url: https://hubble.com/docs/support
- group: operate
  title: ''
  type: Community
  url: https://github.com/HubbleNetwork/community-discussions
- group: company
  title: ''
  type: Blog
  url: https://hubble.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HubbleNetwork
- group: commercial
  title: ''
  type: Pricing
  url: https://hubble.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dash.hubble.com/create-account
- group: start
  title: ''
  type: Login
  url: https://dash.hubble.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hubble.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hubble.com/legal/privacy-policy
- group: operate
  title: ''
  type: SLA
  url: https://hubble.com/legal/sla
- group: other
  title: ''
  type: CoverageMap
  url: https://network.hubble.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hubble.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://hubble.com/docs/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/hubble-network-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://hubble.com/docs/api-specification/hubble-platform-api
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hubble-network-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://hubble.com/docs/security/sdk/vulnerability-handling
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hubble-network-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/hubble-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/hubble-network-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/hubble-network-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/hubble-network-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/hubble-network-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/hubble-network-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hubble-network-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/hubble-network-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/hubble-network-platform-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hubble-network-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hubble-network-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/hubble-network-packet-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/hubble-network-cloud-api-SKILL.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hubble-network-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/hubble-network-platform-overlay.yaml
- group: auth
  title: ''
  type: Scopes
  url: scopes/hubble-network-scopes.yml
- group: agent
  title: ''
  type: MCPServerCandidate
  url: mcp/hubble-network-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/hubble-network-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/hubble-network-well-known.yml
created: '2026-08-04'
description: 'Hubble Network is a Seattle-based IoT connectivity company, founded in 2021 by Alex Haro (Life360) and Ben Wild (Amazon Sidewalk), building a dual-stack global network that any standard Bluetooth Low Energy 5.0+ chip can reach with no modem and no custom radio hardware. The Terrestrial Network aggregates 100M+ BLE scanning gateways across 2,500+ cities, and a low-Earth-orbit Satellite Network is rolling out on the same silicon. The platform is built API-first: the Hubble Platform (Cloud) API at api.hubble.com covers device registration and lifecycle, encrypted packet retrieval and streaming, packet webhooks, platform metrics, organization and user administration, scoped API keys, and billing. Hubble publishes a public OpenAPI definition, an open-source Device SDK in C, a Python SDK/CLI, gateway SDKs for Linux, iOS and Android, and an official Claude Code agent skill for its Cloud API.'
image: https://hubble.com/favicon.ico
json_schemas:
- name: Hubble API Key
  property_count: 5
  slug: hubble-network-api-key
- name: Hubble Billing Subscription
  property_count: 9
  slug: hubble-network-billing-subscription
- name: Hubble Device
  property_count: 8
  slug: hubble-network-device
- name: Hubble Error Response
  property_count: 3
  slug: hubble-network-error
- name: Hubble Invitation
  property_count: 5
  slug: hubble-network-invitation
- name: Hubble Organization User
  property_count: 8
  slug: hubble-network-organization-user
- name: Hubble Organization
  property_count: 7
  slug: hubble-network-organization
- name: Hubble Packet Batch
  property_count: 1
  slug: hubble-network-packet-batch
- name: Hubble Packet
  property_count: 4
  slug: hubble-network-packet
- name: Hubble Packet Webhook
  property_count: 0
  slug: hubble-network-webhook
layout: provider
modified: '2026-08-04'
name: Hubble Network
nav: Providers
network: true
overview: 'Hubble Network publishes 7 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Billing API, Devices API, and 4 more. Tagged areas include Company, IoT, Bluetooth, Satellite, and Connectivity.


  The Hubble Network catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Hubble Network''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 40 more developer resources.'
plans:
- name: Hubble Network Plans Pricing
  plan_count: 4
  slug: hubble-network-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 7
  name: Hubble Network Rate Limits
  slug: hubble-network-rate-limits
scopes:
- name: Hubble Network Scopes
  scope_count: 16
  slug: hubble-network-scopes
  summary_line: 16 scopes
score:
  band: exemplar
  composite: 69.2
  coverage:
    artifact_dirs: 28
    catalog_gap: 44.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 72.2
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 92.1
  previous_composite: 69.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hubble-network/refs/heads/main/screenshots/hubble-network-2026-08-17T075400.png
security:
- kind: authentication
  name: Hubble Network Authentication
  slug: hubble-network-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hubble Network Domain Security
  slug: hubble-network-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Hubble Network Vulnerability Disclosure
  slug: hubble-network-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: hubble-network
tags:
- Company
- IoT
- Bluetooth
- Satellite
- Connectivity
- Asset Tracking
- Devices
- Networks
- Telemetry
- Logistics
website: https://hubble.com/
---
