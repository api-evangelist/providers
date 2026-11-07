---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/blinkhub-net/plans/blinkhub-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blinkhub-net-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/blinkhub-net/llms/blinkhub-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blinkhub-net-llms.txt
- group: other
  href: https://artifacts.apis.io/blinkhub-net/hosts/blinkhub-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blinkhub-net-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blinkhub.net/en/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://blinkhub.net/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blinkhub.net/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://blinkhub.net/en/pricing
- group: start
  title: ''
  type: Login
  url: https://blinkhub.net/login
- group: company
  title: ''
  type: Blog
  url: https://blinkhub.net/blog/press-release-examples
- group: auth
  href: https://artifacts.apis.io/blinkhub-net/security/blinkhub-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blinkhub-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blinkhub.net/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://blinkhub.net/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: BlinkHub Korea provides AI-powered press release creation and distribution through its own newsroom network spanning Korean and US media. Users generate announcements once, which are automatically formatted and sent via XML/FTP to multiple outlets. Features include card‑news and short‑form video generation, SEO audit, post optimization, and free article feeds for publishers. Targeted at PR teams, marketers, agencies, institutions, and companies expanding internationally.
image: https://blinkhub.net/opengraph-image.png
layout: provider
modified: '2026-11-02'
name: BlinkHub Korea
nav: Providers
network: true
overview: 'BlinkHub Korea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, PressRelease, Media Distribution, SEO, and Automation.


  BlinkHub Korea''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Blinkhub Net Plans Pricing
  plan_count: 5
  slug: blinkhub-net-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 7.9
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
  name: Blinkhub Net Domain Security
  slug: blinkhub-net-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: blinkhub-net
tags:
- Artificial Intelligence
- PressRelease
- Media Distribution
- SEO
- Automation
website: https://blinkhub.net/
---
