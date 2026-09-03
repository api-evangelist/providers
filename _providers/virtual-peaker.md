---
access_model:
  confidence: high
  label: Paid · Partner-only onboarding
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - documentation
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Virtual Peaker Agentic Access
  operation_count: 23
  slug: virtual-peaker-agentic-access
  summary_line: 23 operations · 15 acting
api_count: 2
apis:
- baseURL: https://partner.virtualpeaker.io/v1
  baseurl_source: declared
  description: Command specific endpoints
  name: Virtual Peaker Commands API
  slug: virtual-peaker-commands-api
- baseURL: https://partner.virtualpeaker.io/v1
  baseurl_source: declared
  description: Device specific endpoints
  name: Virtual Peaker Devices API
  slug: virtual-peaker-devices-api
- baseURL: https://partner.virtualpeaker.io/v1
  baseurl_source: declared
  description: The Energy Interval Endpoint API from Virtual Peaker — 1 operation(s) for energy interval endpoint.
  name: Virtual Peaker Energy Interval Endpoint API
  slug: virtual-peaker-energy-interval-endpoint-api
- baseURL: https://partner.virtualpeaker.io/v1
  baseurl_source: declared
  description: Virtual Peaker supports managing groups of devices, in addition to individual device control. Grouping enables utilities to target clusters of devices together in demand response events.While device t
  name: Virtual Peaker Group Management API
  slug: virtual-peaker-group-management-api
- baseURL: https://partner.virtualpeaker.io/v1
  baseurl_source: declared
  description: 'The OAuth device discovery flow works as follows: 1. The device owner fills out an onboarding form on Virtual Peaker''s site. 2. At the end of the form, we redirect them to the Device Partner''s OAuth a'
  name: Virtual Peaker OAuth Device Discovery (Preferred) API
  slug: virtual-peaker-oauth-device-discovery-preferred-api
- baseURL: https://partner.virtualpeaker.io/v1
  baseurl_source: declared
  description: 'The [pairing code](./device-partner-api.html#section/Pairing-Codes) device discovery flow works as follows: 1. The device owner fills out an onboarding form on Virtual Peaker''s site. 2. At the end of '
  name: Virtual Peaker Pairing Code Device Discovery - End User App API
  slug: virtual-peaker-pairing-code-device-discovery-end-user-app-api
- baseURL: https://partner.virtualpeaker.io/v1
  baseurl_source: declared
  description: 'The utility commissioned [pairing code](./device-partner-api.html#section/Pairing-Codes) flow could work as follows: 1. The device owner fills out an onboarding form on Virtual Peaker''s site. 2. The u'
  name: Virtual Peaker Pairing Code Device Discovery - Utility Commissioned Installation API
  slug: virtual-peaker-pairing-code-device-discovery-utility-commissioned-installation-api
- baseURL: https://partner.virtualpeaker.io/v1
  baseurl_source: declared
  description: 'All of the endpoints below allow the Device Partner to publish data to the Virtual Peaker platform, which avoids Virtual Peaker having to constantly poll the data when there haven''t been any changes. '
  name: Virtual Peaker Publishing API
  slug: virtual-peaker-publishing-api
artifact_total: 17
asyncapis:
- description: ''
  name: Virtual Peaker Gravity Connect Webhooks
  slug: virtual-peaker-gravity-connect-webhooks
collections:
- collection_type: postman
  name: Gravity Connect API
  slug: postman-virtual-peaker-gravity-connect-api
- collection_type: open
  name: Gravity Connect API (Device Partner)
  slug: open-virtual-peaker-gravity-connect-device-partner-api
- collection_type: open
  name: Gravity Connect API (Virtual Peaker)
  slug: open-virtual-peaker-gravity-connect-vpp-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/virtual-peaker-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/virtual-peaker-gravity-connect-device-partner-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/virtual-peaker-gravity-connect-vpp-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/virtual-peaker-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/virtual-peaker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtual-peaker-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/virtual-peaker-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtual-peaker-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://virtual-peaker.com/
- group: docs
  title: ''
  type: Documentation
  url: https://virtual-peaker.com/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://assets.virtualpeaker.io/gravity-connect/device-partner-api.html
- group: company
  title: ''
  type: Blog
  url: https://virtual-peaker.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://virtual-peaker.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://support.virtual-peaker.com/knowledge
- group: operate
  title: ''
  type: SupportCenter
  url: https://support.virtual-peaker.com/knowledge
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/virtual-peaker
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virtual-peaker/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virtual-peaker.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virtual-peaker.com/terms-of-use/
- group: operate
  title: ''
  type: ContactForm
  url: https://virtual-peaker.com/company/contact/
- group: start
  title: ''
  type: PartnerPortal
  url: https://virtual-peaker.com/partners/device-partners/
- group: start
  title: ''
  type: GettingStarted
  url: https://assets.virtualpeaker.io/gravity-connect/device-partner-api.html#section/Getting-Started
- group: start
  title: ''
  type: Login
  url: https://utility.virtualpeaker.io/
- group: build
  title: ''
  type: Postman
  url: https://assets.virtualpeaker.io/gravity-connect/Gravity%20Connect%20API.postman_collection.json
- group: agent
  title: ''
  type: LLMsTxt
  url: https://virtual-peaker.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtual-peaker-llms.txt
- group: agent
  title: ''
  type: llmsTxt
  url: https://virtual-peaker.com/llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/virtual-peaker-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virtual-peaker-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtual-peaker-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virtual-peaker-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virtual-peaker-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virtual-peaker-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/virtual-peaker-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/virtual-peaker-gravity-connect-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/virtual-peaker-packages.yml
created: '2026-07-27'
description: 'Virtual Peaker is a Louisville, Kentucky software company selling grid-edge DERMS and virtual power plant software to United States and Canadian electric utilities — investor-owned utilities, municipal utilities, and rural electric cooperatives. Its platform is sold as three suites: Shift (grid-edge DERMS device control and demand response event dispatch), Relay (customer engagement, enrollment, and incentive processing), and Envision (demand forecasting). Virtual Peaker sits in the private DER-orchestration layer of the energy value chain, between device OEMs behind the meter and the utility back office — it is a vendor, not a utility, not a retailer, and not a data holder, so no consumer energy data right attaches to it. There is no Green Button / ESPI implementation here, no Consumer Data Right obligation, and no open market or grid data of any kind. What it does publish is its own API specification: Gravity Connect, an OpenAPI 3.0.0 contract (v2.0.6) that Virtual Peaker
  authored and openly published as a vendor-agnostic alternative to OpenADR and IEEE 2030.5 for onboarding and controlling DER devices. Gravity Connect is two-sided — the device OEM implements one half, the VPP platform implements the other — and both halves are readable anonymously as full Redoc API references. The honest posture: a real, downloadable, standards-ambitious API contract that is effectively undiscoverable (it is linked from nowhere on the marketing site) and whose credentials are partner-only, issued per utility program by emailing the Gravity Connect team. The commercial Shift API is named and sold on the marketing site but has no public documentation at all.'
image: https://assets.virtualpeaker.io/gravity-connect/assets/vp_logo.png
layout: provider
mcp_servers:
- description: ''
  name: Virtual Peaker MCP Server
  slug: virtual-peaker-mcp-server
modified: '2026-07-27'
name: Virtual Peaker
nav: Providers
network: true
overview: 'Virtual Peaker publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Commands API, Devices API, Energy Interval Endpoint API, and 5 more. Tagged areas include Energy, United States, Utilities, Electricity, and Grid.


  The Virtual Peaker catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Virtual Peaker''s developer surface includes authentication, documentation, API reference, engineering blog, support, getting-started guide, changelog, and 30 more developer resources.'
random_paper: 3
scopes:
- name: Virtual Peaker Scopes
  scope_count: 3
  slug: virtual-peaker-scopes
  summary_line: 3 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 24
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 57.8
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 12.5
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 74.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/virtual-peaker/refs/heads/main/screenshots/virtual-peaker-2026-08-17T082758.png
security:
- kind: authentication
  name: Virtual Peaker Authentication
  slug: virtual-peaker-authentication
  summary_line: oauth2/hmac · 3 schemes
- kind: domain-security
  name: Virtual Peaker Domain Security
  slug: virtual-peaker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virtual-peaker
tags:
- Energy
- United States
- Utilities
- Electricity
- Grid
- Demand Response
- DER
- DERMS
- Virtual Power Plant
- EV Charging
- Smart Thermostats
- Energy Storage
website: https://virtual-peaker.com/
---
