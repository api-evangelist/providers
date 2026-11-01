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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Quuu provides an AI‑powered social media automation platform with endpoints for content generation and scheduling.
  name: Quuu API
  slug: quuu-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/quuu/llms/quuu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quuu-llms.txt
- group: other
  href: https://artifacts.apis.io/quuu/hosts/quuu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quuu-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://quuu.co/blog/tag/webhook
- group: start
  title: ''
  type: Login
  url: https://app.quuu.co/login
- group: auth
  href: https://artifacts.apis.io/quuu/security/quuu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quuu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quuu.co/
- group: docs
  title: ''
  type: Documentation
  url: https://quuu.co/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://quuu.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://quuu.co/blog
- group: operate
  title: ''
  type: Support
  url: https://quuu.co/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quuu.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quuu.co/privacy
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://quuu.co/documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Quuu provides an AI‑powered social media automation platform that creates, schedules, and publishes posts across X (Twitter), LinkedIn, Facebook, and Bluesky. The service learns a brand’s voice from existing content, generates AI‑crafted captions and images, and offers a dashboard for review and control. It targets creators, agencies, small teams, and businesses seeking consistent online presence without hiring a social media manager. Pricing is per connected profile with a free trial and no credit‑card required.
image: https://quuu.co/base/images/opengraph-generic-app.png
layout: provider
modified: '2026-10-26'
name: Quuu
nav: Providers
network: true
overview: 'Quuu is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Social Media, Automation, and Marketing.


  Quuu''s developer surface includes documentation, pricing, engineering blog, support, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 7.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Quuu Domain Security
  slug: quuu-domain-security
  summary_line: TLSv1.2 · DMARC
slug: quuu
tags:
- Company
- AI
- Social Media
- Automation
- Marketing
website: https://quuu.co/
---
