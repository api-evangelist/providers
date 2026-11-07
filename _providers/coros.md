---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Programmatic access to COROS user data for established platforms, granted after an application to COROS (api@coros.com). Per the Partner API Access page it provides multi-user OAuth 2.0 credentials, w
  name: COROS Partner API
  slug: coros-partner-api
- description: Remote Model Context Protocol server that lets applications read a user's COROS training data and write workout plans after the user authorizes them through OAuth 2.0 (single-user scope, no applicatio
  name: COROS MCP Server
  slug: coros-mcp-server
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/coros/rate-limits/coros-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coros-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/coros/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/coros/cli/coros-cli.yml
  title: ''
  type: CLI
  url: cli/coros-cli.yml
- group: operate
  href: https://artifacts.apis.io/coros/changelog/coros-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coros-changelog.yml
- group: design
  href: https://artifacts.apis.io/coros/conventions/coros-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coros-conventions.yml
- group: auth
  href: https://artifacts.apis.io/coros/authentication/coros-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coros-authentication.yml
- group: design
  href: https://artifacts.apis.io/coros/lifecycle/coros-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/coros-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/coros/conformance/coros-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coros-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coros/mcp/coros-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coros-mcp.yml
- group: agent
  href: https://artifacts.apis.io/coros/well-known/coros-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coros-well-known.yml
- group: other
  href: https://artifacts.apis.io/coros/hosts/coros-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coros-hosts.yml
- group: other
  href: https://artifacts.apis.io/coros/vendors/coros-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coros-vendors.yml
- group: build
  href: https://artifacts.apis.io/coros/packages/coros-packages.yml
  title: ''
  type: SDKs
  url: packages/coros-packages.yml
- group: build
  href: https://artifacts.apis.io/coros/packages/coros-packages.yml
  title: ''
  type: Packages
  url: packages/coros-packages.yml
- group: auth
  href: https://artifacts.apis.io/coros/security/coros-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coros-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coros.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.coros.com/hc/en-us/sections/53180979524884-API-and-MCP-Connections
- group: docs
  title: ''
  type: Documentation
  url: https://support.coros.com/hc/en-us/articles/53181766856724-Partner-API-Access
- group: start
  title: ''
  type: SignUp
  url: https://support.coros.com/hc/en-us/articles/17085887816340-Submit-an-API-Application
- group: start
  title: ''
  type: Login
  url: https://t.coros.com
- group: operate
  title: ''
  type: Support
  url: https://support.coros.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://coros.com/stories
- group: operate
  title: ''
  type: StatusPage
  url: https://coros.com/cn/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coros.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coros.com/privacy
created: '2026-10-18'
description: COROS is a sports technology company that makes GPS sport watches (PACE, APEX, NOMAD, VERTIX), the DURA GPS bike computer, heart rate monitors and sensors, plus the COROS app and Training Hub for runners, cyclists, climbers and other endurance athletes. For developers, COROS publishes a Partner API for established platforms (multi-user OAuth 2.0, webhook push of workout data, two-way activity and workout/training-plan sync, GPX route import/export, daily health data and FIT file downloads, applied for via api@coros.com) and a COROS MCP server that apps can connect to through OAuth 2.0 without an application.
image: https://coros.com/public/images/COROS.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.coros.com over HTTP requiring OAuth; 34 tools listed.
  name: COROS MCP Server
  slug: coros-mcp-server
modified: '2026-10-18'
name: COROS
nav: Providers
network: true
overview: 'COROS is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wearables, Fitness, GPS Watches, and Sports Technology.


  COROS''s developer surface includes CLI, changelog, authentication, documentation, signup flow, support, engineering blog, and 18 more developer resources.'
random_paper: 22
rate_limits:
- limit_count: 1
  name: Coros Rate Limits
  slug: coros-rate-limits
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 46.4
    discoverability: 60.0
    operational_transparency: 50.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coros/coros-2026-11-03T125344.png
security:
- kind: authentication
  name: Coros Authentication
  slug: coros-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Coros Domain Security
  slug: coros-domain-security
  summary_line: TLSv1.2 · DMARC
skill_count: 1
skills:
- name: coros_mcp_login_gateway
  slug: coros-mcp-login-gateway
slug: coros
tags:
- Company
- Wearables
- Fitness
- GPS Watches
- Sports Technology
- Health Data
- Webhook
- Authentication
- MCP
website: https://coros.com
---
