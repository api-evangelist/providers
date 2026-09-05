---
access_model:
  confidence: medium
  label: Sales-led — custom quote
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.imagineai.me/pricing
  - https://form.typeform.com/to/wexUi8lH
  - '{''url'': ''https://www.imagineai.me/'', ''status'': 301, ''note'': ''declared website redirects to https://useimagine.ai/ — a different registrable domain (imagineai.me -> useimagine.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imagine-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.imagineai.me/
- group: company
  title: ''
  type: Blog
  url: https://www.imagineai.me/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.imagineai.me/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imagineai.me/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imagineai.me/privacy-policy
- group: start
  title: ''
  type: Demo
  url: https://form.typeform.com/to/wexUi8lH
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ai-imagine/
- group: other
  title: ''
  type: X
  url: https://x.com/imagineagi
- group: other
  title: ''
  type: CompanyProfile
  url: https://www.ycombinator.com/companies/imagine-ai
- group: other
  title: ''
  type: Product
  url: https://benchmark.imagineai.me/dashboard
- group: start
  title: ''
  type: Login
  url: https://app.imagineai.me/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/imagine-ai-inc
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/profile.php?id=61573966311744
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/imagineagi/
- group: commercial
  title: ''
  type: Plans
  url: plans/imagine-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imagine-ai-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imagine-ai-llms.txt
coverage:
  checked: '2026-08-13'
  detail: 'Imagine AI sells a seat-based managed content service and ships one free public product (the Benchmark dashboard) — the only HTTP API on a host it controls is that dashboard''s own backend at benchmark.imagineai.me/api/*, which is Disallow''d in robots.txt and answers 401 "Authentication required. Provide Authorization: Bearer <token> or X-API-Key header." with no developer portal, reference or spec anywhere, and api.imagineai.me / developer.imagineai.me do not resolve at all.'
  evidence:
  - status: 401
    url: https://benchmark.imagineai.me/api/companies
  - status: 200
    url: https://benchmark.imagineai.me/robots.txt
  - status: 404
    url: https://www.imagineai.me/openapi.json
  - status: 404
    url: https://www.imagineai.me/.well-known/agent-card.json
  - status: 307
    url: https://app.imagineai.me/llms.txt
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Imagine AI (YC F25) is a San Francisco B2B content platform, founded in 2025 by Neo Lee and Sky Yang, that reverse-engineers modern B2B growth starting with LinkedIn. It builds a persona-driven AI clone of a founder or executive by deeply analyzing their writing, speaking style, and market context, then uses that persona to plan content strategy, write LinkedIn posts, draft comments and DMs, and schedule coordinated distribution across an executive team (CEO, VP of Sales, Head of Marketing) from a single shared content calendar. Each client is paired with a dedicated content engineer, and the platform tracks engagement-quality analytics and inbound lead generation; early customers include MongoDB, Rippling, and Conduit. It also publishes Benchmark by Imagine AI, a free public LinkedIn competitor-benchmark dashboard covering 96 companies and 32,500+ analyzed posts with a documented statistical methodology. Imagine AI is a sales-led SaaS — three seat-based tiers, every one a custom
  quote — with no developer portal, API reference, SDK, MCP server or OpenAPI/AsyncAPI/GraphQL definition published on any host it controls as of August 2026; this profile captures the company's identity and public web properties for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imagine-ai.png
layout: provider
modified: '2026-08-13'
name: Imagine Ai
nav: Providers
network: true
overview: 'Imagine Ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, B2B, Content Marketing, and LinkedIn.


  Imagine Ai''s developer surface includes engineering blog, pricing, and 16 more developer resources.'
plans:
- name: Imagine Ai Plans Pricing
  plan_count: 3
  slug: imagine-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Imagine Ai Rate Limits
  slug: imagine-ai-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 19.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imagine-ai/refs/heads/main/screenshots/imagine-ai-2026-07-25T222121.png
security:
- kind: domain-security
  name: Imagine Ai Domain Security
  slug: imagine-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imagine-ai
tags:
- Company
- Artificial Intelligence
- B2B
- Content Marketing
- LinkedIn
- Thought Leadership
- Social-Media
- Lead Generation
- Persona
- Y Combinator
- Software-as-a-Service
website: https://www.imagineai.me/
---
