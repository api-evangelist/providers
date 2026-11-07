---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.0
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'Martini is Lonti''s low-code integration platform (iPaaS) that allows developers to create, consume, publish, integrate, and automate APIs. It supports Git integration, professional IDEs, and provides '
  name: Lonti Martini
  slug: martini
- description: Bellini is Lonti's data modeling and management product designed to help organizations effectively model and manage data assets across their integration landscape.
  name: Lonti Bellini
  slug: bellini
- description: Negroni is Lonti's product for building intelligent applications on top of integrated data sources, enabling data-driven insights and decision making.
  name: Lonti Negroni
  slug: negroni
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/lonti/plans/lonti-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lonti-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lonti/rate-limits/lonti-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lonti-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lonti/finops/lonti-finops.yml
  title: ''
  type: FinOps
  url: finops/lonti-finops.yml
- group: auth
  href: https://artifacts.apis.io/lonti/security/lonti-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lonti-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lonti/security/lonti-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lonti-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lonti
- group: company
  title: ''
  type: Website
  url: https://www.lonti.com
- group: docs
  title: ''
  type: Documentation
  url: https://community.lonti.com/docs
- group: operate
  title: ''
  type: Community
  url: https://community.lonti.com
- group: operate
  title: ''
  type: Support
  url: https://community.lonti.com/support
- group: start
  title: ''
  type: Login
  url: https://console.lonti.com/login
- group: start
  title: ''
  type: Signup
  url: https://console.lonti.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lonti.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.lonti.com/blog
created: '2025-05-02'
description: Lonti is a low-code integration and API platform offering Martini (iPaaS for building, consuming, publishing, and automating APIs), Bellini (data modeling and management), and Negroni (intelligent applications), enabling organizations to integrate data sources, create intelligent applications, and unlock the full potential of their data assets.
finops:
- has_sources: false
  method: generated
  name: Lonti Finops
  primary_unit: request
  service_category: API
  slug: lonti-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lonti.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.lonti.com over HTTP; 9 tools listed.
  name: Lonti MCP Server
  slug: lonti
modified: '2026-04-28'
name: Lonti
nav: Providers
network: true
overview: 'Lonti is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Data Integration, iPaaS, and Low-Code.


  Lonti''s developer surface includes documentation, support, signup flow, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Lonti Plans Pricing
  plan_count: 3
  slug: lonti-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Lonti Rate Limits
  slug: lonti-rate-limits
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 18.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lonti/lonti-2026-06-20T184707.png
security:
- kind: domain-security
  name: Lonti Domain Security
  slug: lonti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lonti Trust Center
  slug: lonti-trust-center
  summary_line: SOC 2, ISO 27001
slug: lonti
tags:
- Automation
- Data Integration
- iPaaS
- Low-Code
website: https://www.lonti.com
---
