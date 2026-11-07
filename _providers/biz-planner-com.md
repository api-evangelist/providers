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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for BizPlanner's AI‑powered financial flight simulator. Documentation is available at the MCP page but no public machine‑readable contract was found.
  name: BizPlanner API
  slug: bizplanner-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/biz-planner-com/plans/biz-planner-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/biz-planner-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/biz-planner-com/llms/biz-planner-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/biz-planner-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/biz-planner-com/well-known/biz-planner-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biz-planner-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/biz-planner-com/hosts/biz-planner-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biz-planner-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/biz-planner-com/vendors/biz-planner-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biz-planner-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://biz-planner.com/en/auth/login
- group: auth
  href: https://artifacts.apis.io/biz-planner-com/security/biz-planner-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biz-planner-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://biz-planner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://biz-planner.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://biz-planner.com/en/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://biz-planner.com/en/
- group: company
  title: ''
  type: Blog
  url: https://biz-planner.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://biz-planner.com/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://biz-planner.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://biz-planner.com/en/privacy
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found despite probing known API hosts.
  evidence:
  - status: 0
    url: https://api.biz-planner.com/openapi.json
  - status: 404
    url: https://biz-planner.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BizPlanner provides an AI‑powered financial flight simulator for entrepreneurs, allowing users to input their business numbers and instantly see cash‑flow projections, break‑even analysis, and funding requirements. The platform offers free plan creation without signup, detailed reports for banks or investors, and a suite of tools to test viability before committing resources. It aims to give clear financial clarity, helping founders pivot or proceed with confidence.
image: https://biz-planner.com/og-image-en.png
layout: provider
modified: '2026-11-02'
name: BizPlanner
nav: Providers
network: true
overview: 'BizPlanner is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Artificial Intelligence, Simulation, Entrepreneurship, and Software-as-a-Service.


  BizPlanner''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Biz Planner Com Plans Pricing
  plan_count: 7
  slug: biz-planner-com-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biz Planner Com Domain Security
  slug: biz-planner-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: biz-planner-com
tags:
- Finance
- Artificial Intelligence
- Simulation
- Entrepreneurship
- Software-as-a-Service
website: https://biz-planner.com/
---
