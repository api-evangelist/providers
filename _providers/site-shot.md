---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Capture website screenshots via HTTP API.
  name: Site-Shot Screenshot API
  slug: site-shot-screenshot-api
artifact_total: 5
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.site-shot.com/api/v1/agent/docs/mcp.md
- group: commercial
  href: https://artifacts.apis.io/site-shot/plans/site-shot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/site-shot-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/site-shot/authentication/site-shot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/site-shot-authentication.yml
- group: design
  href: https://artifacts.apis.io/site-shot/conformance/site-shot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/site-shot-conformance.yml
- group: agent
  href: https://artifacts.apis.io/site-shot/llms/site-shot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/site-shot-llms.txt
- group: other
  href: https://artifacts.apis.io/site-shot/a2a/site-shot-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/site-shot-a2a.yml
- group: agent
  href: https://artifacts.apis.io/site-shot/mcp/site-shot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/site-shot-mcp.yml
- group: agent
  href: https://artifacts.apis.io/site-shot/well-known/site-shot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/site-shot-well-known.yml
- group: other
  href: https://artifacts.apis.io/site-shot/hosts/site-shot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/site-shot-hosts.yml
- group: other
  href: https://artifacts.apis.io/site-shot/vendors/site-shot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/site-shot-vendors.yml
- group: build
  href: https://artifacts.apis.io/site-shot/packages/site-shot-packages.yml
  title: ''
  type: SDKs
  url: packages/site-shot-packages.yml
- group: build
  href: https://artifacts.apis.io/site-shot/packages/site-shot-packages.yml
  title: ''
  type: Packages
  url: packages/site-shot-packages.yml
- group: auth
  href: https://artifacts.apis.io/site-shot/security/site-shot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/site-shot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.site-shot.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.site-shot.com/start/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.site-shot.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.site-shot.com/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.site-shot.com/account/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.site-shot.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.site-shot.com/privacy-policy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://www.site-shot.com/openapi.json
  - status: 401
    url: https://www.site-shot.com/mcp
  - status: 401
    url: https://api.site-shot.com/mcp
  - status: 200
    url: https://www.site-shot.com
  reason: partner-login
  state: gated
created: '2026-10-27'
description: Site-Shot provides a website screenshot service that captures any URL as an image (PNG, JPEG, WebP) via a simple HTTP API. The service offers free online screenshots without signup, as well as paid plans for higher volume, custom viewport, geolocation, scheduling, and API key access. It supports multiple programming languages with code samples, and runs on a real Chromium engine for pixel‑perfect results. The platform emphasizes reliability with 99.9% uptime, scalable infrastructure, and worldwide proxy locations.
image: https://static.site-shot.com/static/android-chrome-512x512.caf5492fd04f.png
layout: provider
mcp_servers:
- description: ''
  name: Site-Shot MCP Server
  slug: site-shot-mcp-yml
modified: '2026-10-27'
name: Site-Shot
nav: Providers
network: true
overview: 'Site-Shot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Screenshots, Automation, and Web.


  Site-Shot''s developer surface includes documentation, authentication, getting-started guide, pricing, engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Site Shot Plans Pricing
  plan_count: 4
  slug: site-shot-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 63.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 34.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/site-shot/site-shot-2026-11-03T143241.png
security:
- kind: authentication
  name: Site Shot Authentication
  slug: site-shot-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Site Shot Domain Security
  slug: site-shot-domain-security
  summary_line: TLSv1.3 · HSTS
slug: site-shot
tags:
- Company
- Screenshots
- Automation
- Web
website: https://www.site-shot.com
---
