---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Bavlio platform
  name: Bavlio API
  slug: bavlio-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/bavlio-com/rules/bavlio-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bavlio-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bavlio-com/errors/bavlio-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bavlio-com-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/bavlio-com/rate-limits/bavlio-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bavlio-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bavlio-com/plans/bavlio-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bavlio-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bavlio-com/conventions/bavlio-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bavlio-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bavlio-com/authentication/bavlio-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bavlio-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/bavlio-com/conformance/bavlio-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bavlio-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bavlio-com/llms/bavlio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bavlio-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bavlio-com/hosts/bavlio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bavlio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bavlio-com/vendors/bavlio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bavlio-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bavlio.com/terms
- group: operate
  title: ''
  type: Support
  url: https://bavlio.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bavlio.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bavlio.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://bavlio.com/docs/api-reference/workspaces/update-workspace-setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bavlio
- group: auth
  href: https://artifacts.apis.io/bavlio-com/security/bavlio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bavlio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bavlio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bavlio.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://bavlio.com/docs/api-reference/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://bavlio.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://bavlio.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://bavlio.com/auth
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.bavlio.com/openapi.json
  - status: 401
    url: https://api.bavlio.com/mcp
  - status: 200
    url: https://bavlio.com/
  reason: partner-login
  state: gated
created: '2026-11-02'
description: Bavlio is an AI-powered sales outreach platform that researches every lead and writes personalized cold email and LinkedIn campaigns for your team. It automates prospecting, enabling sales teams to scale outreach with AI-generated content, improving response rates and saving time.
image: https://bavlio.com/og/default-v4.png
layout: provider
modified: '2026-11-02'
name: Bavlio
nav: Providers
network: true
overview: 'Bavlio publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sales, Outreach, Automation, and Lead Generation.


  The Bavlio catalog on APIs.io includes 1 Spectral governance ruleset.


  Bavlio''s developer surface includes authentication, support, getting-started guide, documentation, API reference, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Bavlio Com Plans Pricing
  plan_count: 5
  slug: bavlio-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Bavlio Com Rate Limits
  slug: bavlio-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: Bavlio API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: bavlio-com-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 29.8
    discoverability: 66.1
    operational_transparency: 42.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bavlio Com Authentication
  slug: bavlio-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bavlio Com Domain Security
  slug: bavlio-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bavlio-com
tags:
- Artificial Intelligence
- Sales
- Outreach
- Automation
- Lead Generation
- Company
website: https://bavlio.com/
---
