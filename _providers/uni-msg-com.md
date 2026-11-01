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
api_count: 1
apis:
- description: WhatsApp bulk messaging platform API (REST) providing messaging, webhooks, and automation.
  name: uni-msg
  slug: uni-msg
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/uni-msg-com/plans/uni-msg-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uni-msg-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/uni-msg-com/llms/uni-msg-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uni-msg-com-llms.txt
- group: other
  href: https://artifacts.apis.io/uni-msg-com/hosts/uni-msg-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/uni-msg-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/uni-msg-com/vendors/uni-msg-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/uni-msg-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uni-msg.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://support.uni-msg.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uni-msg.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://uni-msg.com/login
- group: auth
  href: https://artifacts.apis.io/uni-msg-com/security/uni-msg-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uni-msg-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uni-msg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://uni-msg.com/dashboard/docs
- group: company
  title: ''
  type: Blog
  url: https://uni-msg.com/blog
coverage:
  checked: '2026-10-31'
  detail: Documentation pages are rendered via JavaScript and contain no machine‑readable OpenAPI or AsyncAPI spec.
  evidence:
  - status: 200
    url: https://uni-msg.com/dashboard/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: uni-msg provides a WhatsApp bulk messaging platform with a unified inbox, AI conversation insights, a full REST API and webhooks, enabling users to connect their own numbers quickly without Meta approval, per‑message fees, or bans, and includes automation workflows, multi‑device support, and built‑in warm‑up controls.
image: https://uni-msg.com/icon.png
layout: provider
modified: '2026-10-31'
name: uni-msg-com
nav: Providers
network: true
overview: 'uni-msg-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Messaging, WhatsApp, API, Automation, and BulkMessaging.


  uni-msg-com''s developer surface includes support, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Uni Msg Com Plans Pricing
  plan_count: 5
  slug: uni-msg-com-plans-pricing
random_paper: 12
scopes:
- name: Uni Msg Com Scopes
  scope_count: 0
  slug: uni-msg-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 62.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Uni Msg Com Authentication
  slug: uni-msg-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Uni Msg Com Domain Security
  slug: uni-msg-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uni-msg-com
tags:
- Messaging
- WhatsApp
- API
- Automation
- BulkMessaging
website: https://uni-msg.com/
---
