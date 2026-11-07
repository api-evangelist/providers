---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
asyncapis:
- description: ''
  name: Legalesign Webhooks
  slug: legalesign-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/legalesign/plans/legalesign-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/legalesign-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/legalesign/asyncapi/legalesign-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/legalesign-webhooks.yml
- group: design
  href: https://artifacts.apis.io/legalesign/conventions/legalesign-conventions.yml
  title: ''
  type: Conventions
  url: conventions/legalesign-conventions.yml
- group: auth
  href: https://artifacts.apis.io/legalesign/authentication/legalesign-authentication.yml
  title: ''
  type: Authentication
  url: authentication/legalesign-authentication.yml
- group: agent
  href: https://artifacts.apis.io/legalesign/llms/legalesign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/legalesign-llms.txt
- group: other
  href: https://artifacts.apis.io/legalesign/hosts/legalesign-hosts.yml
  title: ''
  type: Hosts
  url: hosts/legalesign-hosts.yml
- group: other
  href: https://artifacts.apis.io/legalesign/vendors/legalesign-vendors.yml
  title: ''
  type: Vendors
  url: vendors/legalesign-vendors.yml
- group: build
  href: https://artifacts.apis.io/legalesign/packages/legalesign-packages.yml
  title: ''
  type: SDKs
  url: packages/legalesign-packages.yml
- group: build
  href: https://artifacts.apis.io/legalesign/packages/legalesign-packages.yml
  title: ''
  type: Packages
  url: packages/legalesign-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legalesign.com/opn/terms/
- group: operate
  title: ''
  type: Support
  url: https://support.legalesign.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.legalesign.com/
- group: start
  title: ''
  type: SignUp
  url: https://legalesign.com/articles/app1/account-information/sign-up-for-a-plan-or-change-a-plan/
- group: operate
  title: ''
  type: Roadmap
  url: https://legalesign.com/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legalesign.com/opn/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://legalesign.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/legalesign
- group: company
  title: ''
  type: Blog
  url: https://legalesign.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.legalesign.com/tags/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.legalesign.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.legalesign.com/rest-api/tutorial/quickstart
- group: auth
  href: https://artifacts.apis.io/legalesign/security/legalesign-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/legalesign-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://legalesign.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://legalesign.com/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Legalesign provides AI-ready electronic signature software and agreement infrastructure, including comprehensive APIs, MCP-connected documentation, embeddable Components, real-time events and document workflow tools. It enables businesses to automate signing processes, embed signing components, and manage agreements securely at scale.
image: https://legalesign.com/og_image.jpg
layout: provider
modified: '2026-10-20'
name: Legalesign
nav: Providers
network: true
overview: 'Legalesign is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Signature, Automation, and Document Management.


  The Legalesign catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Legalesign''s developer surface includes authentication, support, signup flow, pricing, engineering blog, getting-started guide, documentation, and 16 more developer resources.'
plans:
- name: Legalesign Plans Pricing
  plan_count: 5
  slug: legalesign-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Legalesign Rate Limits
  slug: legalesign-rate-limits
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 34.0
    catalog_earned_first_party: 12.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 39.0
    developer_ergonomics: 36.9
    discoverability: 46.4
    operational_transparency: 21.1
  previous_composite: 45.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/legalesign/legalesign-2026-11-03T134758.png
security:
- kind: authentication
  name: Legalesign Authentication
  slug: legalesign-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Legalesign Domain Security
  slug: legalesign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: legalesign
tags:
- Company
- E-Signature
- Automation
- Document Management
website: https://legalesign.com/
---
