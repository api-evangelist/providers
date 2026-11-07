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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ContentIn provides AI-powered LinkedIn ghostwriter tools accessible via a developer portal.
  name: ContentIn API
  slug: contentin-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/contentin-io/plans/contentin-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contentin-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/contentin-io/authentication/contentin-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contentin-io-authentication.yml
- group: agent
  href: https://artifacts.apis.io/contentin-io/llms/contentin-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contentin-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/contentin-io/well-known/contentin-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contentin-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/contentin-io/hosts/contentin-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contentin-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/contentin-io/vendors/contentin-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contentin-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/contentin-io/security/contentin-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contentin-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contentin.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://contentin.io/ai-linkedin-post-generator/
- group: commercial
  title: ''
  type: Pricing
  url: https://contentin.io/#pricing
- group: company
  title: ''
  type: Blog
  url: https://contentin.io/blog/
- group: operate
  title: ''
  type: Roadmap
  url: https://contentin.io/roadmap/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/58097432
coverage:
  checked: '2026-11-04'
  detail: The developer portal pages render via JavaScript and no machine‑readable OpenAPI spec is publicly available.
  evidence:
  - status: 200
    url: https://contentin.io/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: ContentIn provides an AI-powered LinkedIn ghostwriter that creates and schedules posts for founders and professionals. The platform learns a user’s voice from existing LinkedIn content and generates tailored posts, offering tools like idea manager, post scheduler, analytics, and image creation. It aims to streamline content creation, improve engagement, and continuously refine output through user feedback, with a free trial and paid plans starting at $39 per month.
image: https://contentin.io/share-image.png
layout: provider
modified: '2026-11-04'
name: ContentIn
nav: Providers
network: true
overview: 'ContentIn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LinkedIn, Ghostwriter, Content Creation, and Software-as-a-Service.


  ContentIn''s developer surface includes authentication, getting-started guide, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Contentin Io Plans Pricing
  plan_count: 3
  slug: contentin-io-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 5.3
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Contentin Io Authentication
  slug: contentin-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Contentin Io Domain Security
  slug: contentin-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contentin-io
tags:
- Artificial Intelligence
- LinkedIn
- Ghostwriter
- Content Creation
- Software-as-a-Service
- Company
website: https://contentin.io/
---
