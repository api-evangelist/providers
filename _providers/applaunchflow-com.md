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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for generating app store screenshots, icons, videos, and mockups.
  name: AppLaunchFlow Screenshot API
  slug: applaunchflow-screenshot-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/applaunchflow-com/plans/applaunchflow-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/applaunchflow-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/applaunchflow-com/llms/applaunchflow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/applaunchflow-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/applaunchflow-com/well-known/applaunchflow-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/applaunchflow-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/applaunchflow-com/hosts/applaunchflow-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/applaunchflow-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/applaunchflow-com/vendors/applaunchflow-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/applaunchflow-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.applaunchflow.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.applaunchflow.com/privacy
- group: auth
  href: https://artifacts.apis.io/applaunchflow-com/security/applaunchflow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/applaunchflow-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.applaunchflow.com/
- group: company
  title: ''
  type: Blog
  url: https://www.applaunchflow.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.applaunchflow.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.applaunchflow.com/app-store-screenshot-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.applaunchflow.com/login
coverage:
  checked: '2026-11-01'
  detail: Documentation page https://www.applaunchflow.com/app-store-screenshot-api provides HTML only with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://www.applaunchflow.com/app-store-screenshot-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AppLaunchFlow provides a store‑ready app store and Google Play assets platform, offering AI‑powered screenshot, icon, video, and mockup generation tools. It helps developers create marketing assets, manage ASO copy, and integrate with ChatGPT via MCP. The service includes pricing plans, a blog, and a developer API for automating asset creation.
image: https://www.applaunchflow.com/opengraph.png
layout: provider
modified: '2026-11-01'
name: AppLaunchFlow
nav: Providers
network: true
overview: 'AppLaunchFlow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Marketing, Artificial Intelligence, and Asset Generation.


  AppLaunchFlow''s developer surface includes engineering blog, pricing, documentation, and 10 more developer resources.'
plans:
- name: Applaunchflow Com Plans Pricing
  plan_count: 3
  slug: applaunchflow-com-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 23.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Applaunchflow Com Domain Security
  slug: applaunchflow-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: applaunchflow-com
tags:
- Company
- Software-as-a-Service
- Marketing
- Artificial Intelligence
- Asset Generation
website: https://www.applaunchflow.com/
---
