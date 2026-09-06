---
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-09-05'
api_count: 10
apis:
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: Newsroom posts — FDA clearances, clinical milestones, leadership announcements — served as JSON.
  name: Virtual Incision News Posts API
  slug: virtual-incision-posts-api
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: 'Marketing and clinical pages: MIRA, miniRAS, For Surgeons, safety information and leadership profiles.'
  name: Virtual Incision Pages API
  slug: virtual-incision-pages-api
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: The virtualincision.com media library — MIRA imagery, video posters and press assets.
  name: Virtual Incision Media API
  slug: virtual-incision-media-api
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: The `event` custom post type and `event-type` taxonomy — conferences and clinical events.
  name: Virtual Incision Events API
  slug: virtual-incision-events-api
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: The `jobpost` custom post type plus its category, job-type, location and tag taxonomies — the machine-readable careers surface.
  name: Virtual Incision Careers API
  slug: virtual-incision-careers-api
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: Post categories, tags and the taxonomy registry behind the newsroom.
  name: Virtual Incision Taxonomy API
  slug: virtual-incision-taxonomy-api
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: Site authors — the leadership and communications bylines behind newsroom posts.
  name: Virtual Incision People API
  slug: virtual-incision-people-api
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: Site-wide search across posts, pages and the custom post types.
  name: Virtual Incision Search API
  slug: virtual-incision-search-api
- baseURL: https://virtualincision.com/wp-json
  baseurl_source: declared
  description: Route, post-type and status discovery plus the comment surface.
  name: Virtual Incision Discovery API
  slug: virtual-incision-discovery-api
- description: A Model Context Protocol endpoint registered under the "mcp" namespace of the virtualincision.com WordPress REST route index and served at /wp-json/mcp/mcp-oauth-server (with a second endpoint at /wp-
  name: Virtual Incision MCP Server (WordPress MCP Adapter)
  slug: mcp
artifact_total: 17
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
  title: ''
  type: WellKnown
  url: well-known/virtual-incision-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virtual-incision-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/virtual-incision-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/virtual-incision-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/virtual-incision-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/virtual-incision-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virtual-incision-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virtual-incision-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virtual-incision-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/virtual-incision-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virtual-incision-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virtual-incision-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/virtual-incision-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/virtual-incision-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/virtual-incision-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/virtual-incision-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/virtual-incision-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/virtual-incision-posts-api-overlay.yaml
created: '2026-09-04'
description: 'Virtual Incision Corporation is a Lincoln, Nebraska surgical robotics company, spun out of the University of Nebraska in 2006, that builds MIRA — the Miniaturized In vivo Robotic Assistant — and defined the miniaturized robotic-assisted surgery (miniRAS) category. MIRA is a roughly two-pound, tray-to-table robot inserted through a single umbilical incision, designed to make any operating room robot-ready in minutes. It won FDA De Novo authorization for colectomy in 2024 and 510(k) clearance for benign hysterectomy in 2026. Virtual Incision publishes no product or developer API: MIRA is regulated capital equipment, not a platform. The machine-readable surface on virtualincision.com is the anonymously readable WordPress REST API (newsroom, MIRA pages, events, jobs, media) plus a live but OAuth-gated WordPress MCP Adapter endpoint advertised by RFC 8414 and RFC 9728 discovery documents. The company publishes a coordinated vulnerability disclosure policy under FDA Section 524B.'
image: https://virtualincision.com/wp-content/uploads/2022/07/VIC-logo-icon-400.png
layout: provider
mcp_servers:
- description: ''
  name: Virtual Incision MCP Server
  slug: virtual-incision-mcp-server
modified: '2026-09-04'
name: Virtual Incision
nav: Providers
network: true
overview: 'Virtual Incision publishes 9 APIs on the [APIs.io](https://apis.io/) network, including News Posts API, Pages API, Media API, and 6 more. Tagged areas include Company, Medical Devices, Surgical Robotics, Robotics, and Healthcare.


  Virtual Incision''s developer surface includes engineering blog, support, authentication, code examples, and 27 more developer resources.'
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
  scope_count: 0
  slug: virtual-incision-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 20.6
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 30.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
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
  summary_line: disclosure policy published
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
- Content
- News
- Careers
- Events
- Model Context Protocol
website: https://virtualincision.com/
---
