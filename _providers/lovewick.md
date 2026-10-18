---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lovewick/refs/heads/main/well-known/lovewick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lovewick-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lovewick/refs/heads/main/hosts/lovewick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lovewick-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lovewick.com/terms-of-service/
- group: start
  title: ''
  type: SignUp
  url: https://lovewick.com/sign-up-for-beta/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lovewick.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://lovewick.com/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lovewick/refs/heads/main/security/lovewick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lovewick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lovewick.com/
coverage:
  checked: '2026-10-12'
  detail: No public API documentation or developer program was found on the site.
  evidence:
  - status: 0
    url: https://api.lovewick.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Lovewick is a relationship app designed for couples, offering the internet’s largest library of fun couple questions, fresh date ideas, and research‑inspired relationship advice. The free app helps partners build lasting connections through on‑demand home dates, long‑distance date planning, shared to‑do lists, and personalized reminders. With over 350,000 happy couples, Lovewick combines science‑backed insights with engaging features to improve communication, intimacy, and overall relationship satisfaction.
image: https://lovewick.com/wp-content/uploads/2023/02/lovewick-relationship-app-for-couples.webp
layout: provider
modified: '2026-10-12'
name: Lovewick
nav: Providers
network: true
overview: 'Lovewick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Relationship, App, Couples, Dating, and Wellness.


  Lovewick''s developer surface includes signup flow, engineering blog, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lovewick Domain Security
  slug: lovewick-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lovewick
tags:
- Relationship
- App
- Couples
- Dating
- Wellness
website: https://lovewick.com/
---
