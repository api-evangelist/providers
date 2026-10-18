---
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aymo/refs/heads/main/plans/aymo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aymo-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aymo/refs/heads/main/hosts/aymo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aymo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aymo/refs/heads/main/vendors/aymo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aymo-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://aymo.ai/signup
- group: operate
  title: ''
  type: ChangeLog
  url: https://aymo.ai/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aymo/refs/heads/main/security/aymo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aymo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aymo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://aymo.ai/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://aymo.ai/docs/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://aymo.ai/docs/quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://aymo.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://aymo.ai/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://aymo.ai/roadmap
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aymo.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aymo.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://aymo.ai/support
coverage:
  checked: '2026-10-16'
  detail: Documentation pages are HTML without machine‑readable OpenAPI/AsyncAPI specs.
  evidence:
  - status: 200
    url: https://aymo.ai/docs/introduction
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-16'
description: Pimjo, operating under the brand Aymo AI, offers an all‑in‑one AI platform for teams, providing access to leading large language models such as Claude, GPT, Gemini, DeepSeek, Grok, and Seedream. The platform includes tools for text summarization, paraphrasing, paragraph generation, SEO title creation, YouTube hashtag generation, speech writing, song lyric composition, and more. It features a private, secure workspace for collaborative AI‑assisted brainstorming, model comparison, and result sharing, targeting teams seeking integrated AI capabilities across multiple use‑cases.
image: https://aymo.ai/-/opengraph-image.png?opengraph-image.3-shuximuvkq5.png
layout: provider
modified: '2026-10-16'
name: Pimjo
nav: Providers
network: true
overview: 'Pimjo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Platform, Team Collaboration, and LLM.


  Pimjo''s developer surface includes signup flow, changelog, documentation, API reference, getting-started guide, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Aymo Plans Pricing
  plan_count: 1
  slug: aymo-plans-pricing
random_paper: 20
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aymo Domain Security
  slug: aymo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aymo
tags:
- Company
- Artificial Intelligence
- Platform
- Team Collaboration
- LLM
- Software-as-a-Service
website: https://aymo.ai/
---
