---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Access groups API from ButterflyMX — 6 operation(s) for access groups.
  name: ButterflyMX Access groups API
  slug: butterflymx-access-groups-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Access Logs API from ButterflyMX — 2 operation(s) for access logs.
  name: ButterflyMX Access Logs API
  slug: butterflymx-access-logs-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Access Points API from ButterflyMX — 3 operation(s) for access points.
  name: ButterflyMX Access Points API
  slug: butterflymx-access-points-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Access Tools API from ButterflyMX — 5 operation(s) for access tools.
  name: ButterflyMX Access Tools API
  slug: butterflymx-access-tools-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Building Integrations API from ButterflyMX — 2 operation(s) for building integrations.
  name: ButterflyMX Building Integrations API
  slug: butterflymx-building-integrations-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Buildings API from ButterflyMX — 3 operation(s) for buildings.
  name: ButterflyMX Buildings API
  slug: butterflymx-buildings-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Calls API from ButterflyMX — 2 operation(s) for calls.
  name: ButterflyMX Calls API
  slug: butterflymx-calls-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Devices API from ButterflyMX — 2 operation(s) for devices.
  name: ButterflyMX Devices API
  slug: butterflymx-devices-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Door Release Requests API from ButterflyMX — 1 operation(s) for door release requests.
  name: ButterflyMX Door Release Requests API
  slug: butterflymx-door-release-requests-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Keychains API from ButterflyMX — 6 operation(s) for keychains.
  name: ButterflyMX Keychains API
  slug: butterflymx-keychains-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Tenant Integrations API from ButterflyMX — 2 operation(s) for tenant integrations.
  name: ButterflyMX Tenant Integrations API
  slug: butterflymx-tenant-integrations-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Tenants API from ButterflyMX — 3 operation(s) for tenants.
  name: ButterflyMX Tenants API
  slug: butterflymx-tenants-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Units API from ButterflyMX — 4 operation(s) for units.
  name: ButterflyMX Units API
  slug: butterflymx-units-api
- baseURL: https://api.butterflymx.com
  baseurl_source: declared
  description: The Virtual Keys API from ButterflyMX — 2 operation(s) for virtual keys.
  name: ButterflyMX Virtual Keys API
  slug: butterflymx-virtual-keys-api
artifact_total: 35
asyncapis:
- description: ''
  name: Butterflymx Webhooks
  slug: butterflymx-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ButterflyMX Access groups API
  slug: open-butterflymx-access-groups-api
- collection_type: open
  name: ButterflyMX Access Logs API
  slug: open-butterflymx-access-logs-api
- collection_type: open
  name: ButterflyMX Access Points API
  slug: open-butterflymx-access-points-api
- collection_type: open
  name: ButterflyMX Access Tools API
  slug: open-butterflymx-access-tools-api
- collection_type: open
  name: ButterflyMX Building Integrations API
  slug: open-butterflymx-building-integrations-api
- collection_type: open
  name: ButterflyMX Buildings API
  slug: open-butterflymx-buildings-api
- collection_type: open
  name: ButterflyMX Calls API
  slug: open-butterflymx-calls-api
- collection_type: open
  name: ButterflyMX Devices API
  slug: open-butterflymx-devices-api
- collection_type: open
  name: ButterflyMX Door Release Requests API
  slug: open-butterflymx-door-release-requests-api
- collection_type: open
  name: ButterflyMX Keychains API
  slug: open-butterflymx-keychains-api
- collection_type: open
  name: ButterflyMX Tenant Integrations API
  slug: open-butterflymx-tenant-integrations-api
- collection_type: open
  name: ButterflyMX Tenants API
  slug: open-butterflymx-tenants-api
- collection_type: open
  name: ButterflyMX Units API
  slug: open-butterflymx-units-api
- collection_type: open
  name: ButterflyMX Virtual Keys API
  slug: open-butterflymx-virtual-keys-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/butterflymx-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/butterflymx-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/butterflymx-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://butterflymx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.butterflymx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.butterflymx.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.butterflymx.com/reference/get_v4-buildings-1
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.butterflymx.com/docs/getting-started-in-the-sandbox
- group: operate
  title: ''
  type: Support
  url: https://help.butterflymx.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://butterflymx.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runslikebutter
- group: commercial
  title: ''
  type: Pricing
  url: https://butterflymx.com/cost/
- group: start
  title: ''
  type: Login
  url: https://accounts.butterflymx.com/login/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://butterflymx.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://butterflymx.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.butterflymx.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://apidocs.butterflymx.com/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.butterflymx.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/butterflymx-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/butterflymx-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/butterflymx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/butterflymx-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/butterflymx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/butterflymx-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/butterflymx-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/butterflymx-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/butterflymx-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/butterflymx-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/butterflymx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/butterflymx-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/butterflymx-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/butterflymx-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/butterflymx-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/butterflymx-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: 'ButterflyMX is a property-access technology company whose smart video intercoms, keypads, smart locks, elevator controls, vehicle-access readers, package rooms and front-desk stations are installed in more than 20,000 multifamily, commercial, gated-community, student-housing and senior-living buildings. Its public ButterflyMX API (v4) exposes the same access-control core to partners and property-technology platforms: buildings, units, tenants, access points, devices, access groups, permanent access tools (PINs and RFID tags), keychains and virtual keys for visitor passes, door-release requests for programmatic swipe-to-open, and access and video-call logs. Real-time delivery is handled by building- and tenant-scoped webhook integrations, and native iOS and Android SDKs add in-app video-call handling on top of the REST surface. Authorization is OAuth 2.0 authorization-code, issued by an OpenID-Connect-discoverable authorization server at accounts.butterflymx.com, with a full
  sandbox replica for pre-production testing.'
image: https://butterflymx.com/wp-content/uploads/2023/10/gated-community-intercom.webp
layout: provider
mcp_servers:
- description: ''
  name: ButterflyMX MCP Server
  slug: butterflymx-mcp-server
modified: '2026-08-08'
name: ButterflyMX
nav: Providers
network: true
overview: 'ButterflyMX publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Access groups API, Access Logs API, Access Points API, and 11 more. Tagged areas include Access Control, physical-access, smart-intercom, PropTech, and Property Management.


  The ButterflyMX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ButterflyMX''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 28 more developer resources.'
random_paper: 4
scopes:
- name: Butterflymx Scopes
  scope_count: 6
  slug: butterflymx-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 4.5
    contract_quality: 57.6
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 38.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/butterflymx/refs/heads/main/screenshots/butterflymx-2026-08-17T080748.png
security:
- kind: authentication
  name: Butterflymx Authentication
  slug: butterflymx-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Butterflymx Domain Security
  slug: butterflymx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Butterflymx Trust Center
  slug: butterflymx-trust-center
  summary_line: trust center published
slug: butterflymx
tags:
- Access Control
- physical-access
- smart-intercom
- PropTech
- Property Management
- Multifamily
- Building Automation
- Visitor Management
- IoT
- smart-locks
- Authentication
- Webhook
website: https://butterflymx.com/
---
