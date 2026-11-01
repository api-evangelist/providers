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
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/yandex-mail/plans/yandex-mail-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yandex-mail-plans-pricing.yml
- group: auth
  title: ''
  type: Security
  url: https://ya.cc/t/1cSZixjB3gkSva
- group: design
  href: https://artifacts.apis.io/yandex-mail/conformance/yandex-mail-conformance.yml
  title: ''
  type: Conformance
  url: conformance/yandex-mail-conformance.yml
- group: auth
  href: https://artifacts.apis.io/yandex-mail/well-known/yandex-mail-yandex-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yandex-mail-yandex-security.txt
- group: agent
  href: https://artifacts.apis.io/yandex-mail/well-known/yandex-mail-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yandex-mail-well-known.yml
- group: other
  href: https://artifacts.apis.io/yandex-mail/hosts/yandex-mail-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yandex-mail-hosts.yml
- group: auth
  href: https://artifacts.apis.io/yandex-mail/security/yandex-mail-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/yandex-mail-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/yandex-mail/security/yandex-mail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yandex-mail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mail.yandex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://360.yandex.com/mail/
- group: company
  title: ''
  type: Blog
  url: https://360.yandex.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://yandex.ru/support/yandex-360/customers/mail/ru/reg
- group: commercial
  title: ''
  type: Pricing
  url: https://360.yandex.com/premium-plans/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yandex.com/legal/privacy/
coverage:
  checked: '2026-10-28'
  detail: Docs page https://360.yandex.com/mail/ redirects to a captcha challenge, preventing access to API documentation.
  evidence:
  - status: 302
    url: https://360.yandex.com/mail/
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Yandex Mail is a free email service provided by Yandex, a Russian internet company. It offers personal and business email accounts with robust spam protection, security features, and integration with Yandex 360 suite. Users can access mail via web, mobile apps for iOS and Android, and desktop clients. The service includes customizable filters, forwarding, and a clean interface without ads. Yandex Mail supports corporate mailboxes, premium plans, and integrates with other Yandex services like Disk, Calendar, and Docs.
image: https://avatars.mds.yandex.net/get-bunker/118781/920adcaa2282314c641053958fd5140b170779aa/orig
layout: provider
modified: '2026-10-28'
name: Yandex Mail
nav: Providers
network: true
overview: 'Yandex Mail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Communication, Cloud, and Productivity.


  Yandex Mail''s developer surface includes documentation, engineering blog, support, pricing, and 10 more developer resources.'
plans:
- name: Yandex Mail Plans Pricing
  plan_count: 4
  slug: yandex-mail-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Yandex Mail Domain Security
  slug: yandex-mail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yandex Mail Vulnerability Disclosure
  slug: yandex-mail-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yandex-mail
tags:
- Company
- Email
- Communication
- Cloud
- Productivity
- Russian
website: https://mail.yandex.com/
---
