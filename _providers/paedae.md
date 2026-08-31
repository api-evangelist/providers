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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Applications API from Paedae — 5 operation(s) for applications.
  name: Paedae Applications API
  slug: paedae-applications-api
- description: The Beacon Configurations API from Paedae — 5 operation(s) for beacon configurations.
  name: Paedae Beacon Configurations API
  slug: paedae-beacon-configurations-api
- description: The Beacons API from Paedae — 9 operation(s) for beacons.
  name: Paedae Beacons API
  slug: paedae-beacons-api
- description: The Communications API from Paedae — 16 operation(s) for communications.
  name: Paedae Communications API
  slug: paedae-communications-api
- description: The Places API from Paedae — 5 operation(s) for places.
  name: Paedae Places API
  slug: paedae-places-api
artifact_total: 18
asyncapis:
- description: ''
  name: Paedae Webhooks
  slug: paedae-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gimbal REST Applications API
  slug: open-paedae-applications-api
- collection_type: open
  name: Gimbal REST Applications Beacon Configurations API
  slug: open-paedae-beacon-configurations-api
- collection_type: open
  name: Gimbal REST Applications Beacons API
  slug: open-paedae-beacons-api
- collection_type: open
  name: Gimbal REST Applications Communications API
  slug: open-paedae-communications-api
- collection_type: open
  name: Gimbal REST Applications Places API
  slug: open-paedae-places-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/paedae-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paedae-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/paedae-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.gimbal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gimbal.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gimbal.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gimbal.com/rest.html
- group: start
  title: ''
  type: Portal
  url: https://manager.gimbal.com
- group: start
  title: ''
  type: SignUp
  url: https://manager.gimbal.com
- group: operate
  title: ''
  type: Support
  url: https://support.gimbal.com/hc/en-us/
- group: operate
  title: ''
  type: StatusPage
  url: http://status.gimbal.com
- group: build
  title: ''
  type: Packages
  url: packages/paedae-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/paedae-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paedae-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/paedae-well-known.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/paedae-tool-crosswalk.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/paedae-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/paedae-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/paedae-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/paedae-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gimbalinc
- group: company
  title: ''
  type: Blog
  url: https://infillion.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infillion.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infillion.com/terms-of-use/
created: '2026-07-17'
description: Paedae is the company behind the Gimbal proximity and location platform (a 500 Global portfolio company; paedae.com now redirects to gimbal.com, operated under Infillion). Gimbal provides beacons, geofencing, and a proximity SDK for iOS and Android, plus a Gimbal Manager REST API to manage applications, places, beacons, beacon configurations, and location-triggered communications. Beacon sighting events (Arrived/Departed/Sighted) are delivered via HTTP callbacks. This profile was enriched from the live Gimbal developer surface at docs.gimbal.com and manager.gimbal.com.
image: https://raw.githubusercontent.com/api-evangelist/paedae/refs/heads/main/apis.yml
layout: provider
mcp_servers:
- description: ''
  name: Paedae MCP Server
  slug: paedae-mcp-server
modified: '2026-08-13'
name: Paedae
nav: Providers
network: true
overview: 'Paedae publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Beacon Configurations API, Beacons API, and 2 more. Tagged areas include Company, Proximity, Location, Beacons, and Geofencing.


  The Paedae catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paedae''s developer surface includes documentation, API reference, developer portal, signup flow, support, changelog, engineering blog, and 18 more developer resources.'
plans:
- name: Paedae Plans Pricing
  plan_count: 0
  slug: paedae-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Paedae Rate Limits
  slug: paedae-rate-limits
scopes:
- name: Paedae Scopes
  scope_count: 0
  slug: paedae-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 61.4
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 47.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paedae/refs/heads/main/screenshots/paedae-2026-08-07T191301.png
security:
- kind: authentication
  name: Paedae Authentication
  slug: paedae-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Paedae Domain Security
  slug: paedae-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paedae
tags:
- Company
- Proximity
- Location
- Beacons
- Geofencing
- Mobile SDK
- Advertising
- Marketing
website: https://www.gimbal.com
---
