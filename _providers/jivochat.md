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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/jivochat/hosts/jivochat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jivochat-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jivochat.com/security/
- group: auth
  href: https://artifacts.apis.io/jivochat/security/jivochat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jivochat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jivochat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.jivochat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jivochat.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.jivochat.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jivochat.com/docs/widget/
- group: operate
  title: ''
  type: Support
  url: https://www.jivochat.com/help/
- group: company
  title: ''
  type: Blog
  url: https://www.jivochat.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jivochat.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jivochat.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jivochat.com/files/privacy_policy.pdf
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are served as JavaScript-rendered HTML, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://www.jivochat.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: JivoChat provides live chat, messaging, and AI‑powered customer support software for websites and mobile apps. Its platform enables businesses to engage visitors via chat widgets, WhatsApp, Instagram, Telegram, and other channels, offering features such as chatbot integration, webhooks, and a robust API for developers to customize and automate interactions. The service includes AI assistants, analytics, and multi‑channel communication tools, helping companies improve conversion, support efficiency, and customer satisfaction.
image: https://www.jivochat.com/images/layout/og/card-en.png
layout: provider
modified: '2026-10-26'
name: JivoChat
nav: Providers
network: true
overview: 'JivoChat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LiveChat, Messaging, AI, and CustomerSupport.


  JivoChat''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 7 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: derived
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
  name: Jivochat Domain Security
  slug: jivochat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: jivochat
tags:
- Company
- LiveChat
- Messaging
- AI
- CustomerSupport
website: https://jivochat.com/
---
