---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Virtual Incision website at virtualincision.com: the route index of the site''s content management system, catalogued as one site surface rather than as s'
  name: Virtual Incision Website (WordPress REST)
  slug: virtualincision-com-website-wordpress-rest
- description: A Model Context Protocol endpoint registered under the "mcp" namespace of the virtualincision.com WordPress REST route index and served at /wp-json/mcp/mcp-oauth-server (with a second endpoint at /wp-
  name: Virtual Incision MCP Server (WordPress MCP Adapter)
  slug: mcp
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://virtualincision.com/
- group: company
  title: ''
  type: Blog
  url: https://virtualincision.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://virtualincision.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://virtualincision.com/customer-support/
- group: company
  title: ''
  type: Careers
  url: https://virtualincision.com/careers/
- group: other
  title: ''
  type: Technology
  url: https://virtualincision.com/mira/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://virtualincision.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://virtualincision.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://virtualincision.com/coordinated-disclosure/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/virtualincision
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/virtual-incision-corporation/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/virtual-incision_stock/
- group: agent
  href: https://artifacts.apis.io/virtual-incision/well-known/virtual-incision-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/virtual-incision-well-known.yml
- group: agent
  href: https://artifacts.apis.io/virtual-incision/llms/virtual-incision-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/virtual-incision-llms.txt
- group: build
  href: https://artifacts.apis.io/virtual-incision/packages/virtual-incision-packages.yml
  title: ''
  type: Packages
  url: packages/virtual-incision-packages.yml
- group: auth
  href: https://artifacts.apis.io/virtual-incision/authentication/virtual-incision-authentication.yml
  title: ''
  type: Authentication
  url: authentication/virtual-incision-authentication.yml
- group: auth
  href: https://artifacts.apis.io/virtual-incision/scopes/virtual-incision-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/virtual-incision-scopes.yml
- group: design
  href: https://artifacts.apis.io/virtual-incision/conventions/virtual-incision-conventions.yml
  title: ''
  type: Conventions
  url: conventions/virtual-incision-conventions.yml
- group: design
  href: https://artifacts.apis.io/virtual-incision/conformance/virtual-incision-conformance.yml
  title: ''
  type: Conformance
  url: conformance/virtual-incision-conformance.yml
- group: design
  href: https://artifacts.apis.io/virtual-incision/lifecycle/virtual-incision-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/virtual-incision-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/virtual-incision/security/virtual-incision-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/virtual-incision-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/virtual-incision/security/virtual-incision-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/virtual-incision-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/virtual-incision/errors/virtual-incision-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/virtual-incision-problem-types.yml
- group: design
  href: https://artifacts.apis.io/virtual-incision/data-model/virtual-incision-data-model.yml
  title: ''
  type: DataModel
  url: data-model/virtual-incision-data-model.yml
- group: build
  href: https://artifacts.apis.io/virtual-incision/examples/virtual-incision-examples.yml
  title: ''
  type: Examples
  url: examples/virtual-incision-examples.yml
- group: operate
  href: https://artifacts.apis.io/virtual-incision/rate-limits/virtual-incision-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/virtual-incision-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/virtual-incision/plans/virtual-incision-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/virtual-incision-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/virtual-incision/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/virtual-incision/mcp/virtual-incision-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/virtual-incision-mcp.yml
- group: build
  href: https://artifacts.apis.io/virtual-incision/mcp/virtual-incision-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/virtual-incision-tool-crosswalk.yml
created: '2026-09-04'
description: 'Virtual Incision Corporation is a Lincoln, Nebraska surgical robotics company, spun out of the University of Nebraska in 2006, that builds MIRA — the Miniaturized In vivo Robotic Assistant — and defined the miniaturized robotic-assisted surgery (miniRAS) category. MIRA is a roughly two-pound, tray-to-table robot inserted through a single umbilical incision, designed to make any operating room robot-ready in minutes. It won FDA De Novo authorization for colectomy in 2024 and 510(k) clearance for benign hysterectomy in 2026. Virtual Incision publishes no product or developer API: MIRA is regulated capital equipment, not a platform. The machine-readable surface on virtualincision.com is the anonymously readable WordPress REST API (newsroom, MIRA pages, events, jobs, media) plus a live but OAuth-gated WordPress MCP Adapter endpoint advertised by RFC 8414 and RFC 9728 discovery documents. The company publishes a coordinated vulnerability disclosure policy under FDA Section 524B.'
image: https://virtualincision.com/wp-content/uploads/2022/07/VIC-logo-icon-400.png
layout: provider
mcp_servers:
- description: Remote MCP server at virtualincision.com over HTTP requiring OAuth.
  name: Virtual Incision MCP Server
  slug: mcp-oauth-server
modified: '2026-09-04'
name: Virtual Incision
nav: Providers
network: true
overview: 'Virtual Incision is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Surgical Robotics, Robotics, and Healthcare.


  Virtual Incision''s developer surface includes engineering blog, support, authentication, code examples, and 26 more developer resources.'
plans:
- name: Virtual Incision Plans Pricing
  plan_count: 0
  slug: virtual-incision-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Virtual Incision Rate Limits
  slug: virtual-incision-rate-limits
scopes:
- name: Virtual Incision Scopes
  scope_count: 1
  slug: virtual-incision-scopes
  summary_line: 1 scope · authorization_code
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 6.5
    developer_ergonomics: 25.6
    discoverability: 66.7
    operational_transparency: 13.2
  previous_composite: 26.3
  provenance:
    conformance: first-party
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/virtual-incision/virtual-incision-2026-10-11T133018.png
security:
- kind: authentication
  name: Virtual Incision Authentication
  slug: virtual-incision-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Virtual Incision Domain Security
  slug: virtual-incision-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Virtual Incision Vulnerability Disclosure
  slug: virtual-incision-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 3
skills:
- name: virtual-incision-careers-watch
  slug: virtual-incision-careers-watch
- name: virtual-incision-media-assets
  slug: virtual-incision-media-assets
- name: virtual-incision-newsroom-monitor
  slug: virtual-incision-newsroom-monitor
slug: virtual-incision
tags:
- Company
- Medical Devices
- Surgical Robotics
- Robotics
- Healthcare
- Health
- Life Sciences
- Medical Technology
- News
- Careers
- Event
- MCP
website: https://virtualincision.com/
---
