---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
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
  score: 25.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Ecommerce extraction Jobs API for searching products and extracting data.
  name: datawebot Jobs API
  slug: datawebot-jobs-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/datawebot-com/plans/datawebot-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datawebot-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/datawebot-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/datawebot-com/cli/datawebot-com-cli.yml
  title: ''
  type: CLI
  url: cli/datawebot-com-cli.yml
- group: design
  href: https://artifacts.apis.io/datawebot-com/conventions/datawebot-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/datawebot-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/datawebot-com/conventions/datawebot-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/datawebot-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/datawebot-com/authentication/datawebot-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datawebot-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/datawebot-com/conformance/datawebot-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datawebot-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datawebot-com/llms/datawebot-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datawebot-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/datawebot-com/well-known/datawebot-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datawebot-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datawebot-com/hosts/datawebot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datawebot-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datawebot-com/vendors/datawebot-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datawebot-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datawebot.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.datawebot.com/support
- group: start
  title: ''
  type: Sandbox
  url: https://www.datawebot.com/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datawebot.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.datawebot.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.datawebot.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.datawebot.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datawebot.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.datawebot.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.datawebot.com/docs/api/reference
- group: auth
  href: https://artifacts.apis.io/datawebot-com/security/datawebot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datawebot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datawebot.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://datawebot.com/openapi.json
  - status: null
    url: https://www.datawebot.com/openapi.json
  - status: null
    url: https://api.datawebot.com/openapi.json
  - status: 401
    url: https://mcp.datawebot.com/mcp
  - status: 401
    url: https://api.datawebot.com/graphql
  - status: 401
    url: https://api.datawebot.com/mcp
  reason: partner-login
  state: gated
created: '2026-11-05'
description: datawebot provides an ecommerce MCP server and API that enables AI agents to search products across worldwide online shops, compare seller prices, and extract detailed product data from platforms such as Amazon, eBay, Walmart, and Zalando. The service offers 200 free credits with no subscription required, targeting developers and AI applications seeking comprehensive ecommerce data.
image: https://www.datawebot.com/opengraph-image
layout: provider
modified: '2026-11-05'
name: datawebot
nav: Providers
network: true
overview: 'datawebot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Artificial Intelligence, Data, and Marketplace.


  datawebot''s developer surface includes CLI, authentication, support, sandbox, documentation, changelog, engineering blog, and 16 more developer resources.'
plans:
- name: Datawebot Com Plans Pricing
  plan_count: 5
  slug: datawebot-com-plans-pricing
random_paper: 23
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 66.0
    discoverability: 57.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datawebot Com Authentication
  slug: datawebot-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Datawebot Com Domain Security
  slug: datawebot-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: main-flow
  slug: datawebot-com-main-skill
slug: datawebot-com
tags:
- E-Commerce
- Artificial Intelligence
- Data
- Marketplace
website: https://datawebot.com/
---
