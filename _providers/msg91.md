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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Messaging API providing SMS, voice, email, WhatsApp, and OTP services.
  name: MSG91 API
  slug: msg91-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/msg91/refs/heads/main/plans/msg91-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/msg91-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/msg91/refs/heads/main/llms/msg91-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/msg91-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/msg91/refs/heads/main/hosts/msg91-hosts.yml
  title: ''
  type: Hosts
  url: hosts/msg91-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/msg91/refs/heads/main/vendors/msg91-vendors.yml
  title: ''
  type: Vendors
  url: vendors/msg91-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/msg91/refs/heads/main/packages/msg91-packages.yml
  title: ''
  type: SDKs
  url: packages/msg91-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/msg91/refs/heads/main/packages/msg91-packages.yml
  title: ''
  type: Packages
  url: packages/msg91-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://msg91.com/help/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://msg91.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://msg91.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://control.msg91.com/signin/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.msg91.com\\\
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/msg91/refs/heads/main/security/msg91-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/msg91-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://msg91.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.msg91.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.msg91.com/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://msg91.com/signup
- group: operate
  title: ''
  type: Support
  url: https://msg91.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://msg91.com/pricing/hello
coverage:
  checked: '2026-10-14'
  detail: API documentation returns 403/404 for common OpenAPI URLs, no machine-readable spec found.
  evidence:
  - status: 403
    url: https://api.msg91.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: MSG91 provides a comprehensive cloud communications platform offering SMS, voice, email, WhatsApp, RCS, and OTP services. It enables businesses to engage customers across multiple channels via robust APIs, supporting dynamic messaging, campaign automation, and contact management. With global reach and high volume handling, MSG91 serves over 30,000 businesses worldwide, delivering reliable, scalable communication solutions for enterprises of all sizes.
image: https://msg91.com/assets/brand/favicon.svg
layout: provider
modified: '2026-10-13'
name: MSG91
nav: Providers
network: true
overview: 'MSG91 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Communications, Cloud, Messaging, and SMS.


  MSG91''s developer surface includes documentation, API reference, getting-started guide, support, pricing, and 13 more developer resources.'
plans:
- name: Msg91 Plans Pricing
  plan_count: 5
  slug: msg91-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 64.3
    operational_transparency: 7.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 11.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Msg91 Domain Security
  slug: msg91-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: msg91
tags:
- Communications
- Cloud
- Messaging
- SMS
website: https://msg91.com
---
