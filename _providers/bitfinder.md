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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bitfinder Agentic Access
  operation_count: 6
  slug: bitfinder-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: Time-series indoor air quality readings
  name: Bitfinder Air Data API
  slug: bitfinder-air-data-api
- description: Devices registered to the authenticated user
  name: Bitfinder Devices API
  slug: bitfinder-devices-api
- description: Authenticated Awair user profile
  name: Bitfinder User API
  slug: bitfinder-user-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://getawair.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.getawair.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.getawair.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developer.getawair.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.getawair.com/hc/en-us/articles/360049982333-Using-Awair-Developer-APIs
- group: operate
  title: ''
  type: Support
  url: https://support.getawair.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.getawair.com/authors/awair
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getawair
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getawair.com/
- group: start
  title: ''
  type: SignUp
  url: https://developer.getawair.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getawair.com/pages/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getawair.com/pages/legal
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitfinder-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bitfinder-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitfinder-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitfinder-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bitfinder-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bitfinder-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bitfinder-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bitfinder-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bitfinder-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bitfinder-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bitfinder-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bitfinder-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitfinder-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitfinder-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/bitfinder-awair-overlay.yaml
created: '2026-07-17'
description: Bitfinder, Inc., doing business as Awair, builds indoor air quality (IAQ) monitors and a cloud platform used across homes, offices, schools, and commercial spaces. Its devices (Awair Element, Awair Omni, and 2nd Edition) measure the Awair Score along with temperature, humidity, CO2, chemicals (VOC), and fine dust (PM2.5). The Awair Home & OAuth Developer API lets developers, partners, and hobbyists read a user's registered devices and their air-data time series (latest, raw per-second, 5-minute-average, and 15-minute-average) on behalf of Awair users, authorized with an OAuth 2.0 or Developer Console Bearer token. Bitfinder was a Techstars portfolio company.
image: https://cdn.prod.website-files.com/606ca67e54e3f68fa1be1f6b/652df95bec0aa957aba241bd_Frame%201060.png
layout: provider
mcp_servers:
- description: ''
  name: bitfinder-mcp.yml
  slug: bitfinder-mcpyml
modified: '2026-07-18'
name: Bitfinder
nav: Providers
network: true
overview: 'Bitfinder publishes 3 APIs on the [APIs.io](https://apis.io/) network: Air Data API, Devices API, and User API. Tagged areas include Company, Air Quality, Internet of Things, IoT, and Environmental Monitoring.


  Bitfinder''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
random_paper: 71
rate_limits:
- limit_count: 0
  name: Bitfinder Rate Limits
  slug: bitfinder-rate-limits
scopes:
- name: Bitfinder Scopes
  scope_count: 0
  slug: bitfinder-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.0
  delta: -7.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 49.2
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bitfinder/refs/heads/main/screenshots/bitfinder-2026-07-25T203146.png
security:
- kind: authentication
  name: Bitfinder Authentication
  slug: bitfinder-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Bitfinder Domain Security
  slug: bitfinder-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bitfinder
tags:
- Company
- Air Quality
- Internet of Things
- IoT
- Environmental Monitoring
- Smart Home
- Sensors
- Health
- Developer API
website: https://getawair.com/
---
