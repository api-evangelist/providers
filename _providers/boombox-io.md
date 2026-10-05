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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boombox-io/refs/heads/main/plans/boombox-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boombox-io-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boombox-io/refs/heads/main/llms/boombox-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boombox-io-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boombox-io/refs/heads/main/well-known/boombox-io-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boombox-io-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boombox-io/refs/heads/main/well-known/boombox-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boombox-io-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boombox-io/refs/heads/main/hosts/boombox-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boombox-io-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boombox-io/refs/heads/main/vendors/boombox-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boombox-io-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.boombox.io/en/articles/6584477-getting-started-with-boombox-io
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boombox-io/refs/heads/main/security/boombox-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boombox-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boombox.io
- group: docs
  title: ''
  type: Documentation
  url: https://boombox.io/about/
- group: commercial
  title: ''
  type: Pricing
  url: https://boombox.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://boombox.io/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boombox.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boombox.io/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://help.boombox.io/
- group: start
  title: ''
  type: Login
  url: https://app.boombox.io/login?
coverage:
  checked: '2026-10-02'
  detail: No public API contract or developer documentation was found despite probing known hosts and documentation pages.
  evidence:
  - status: 200
    url: https://boombox.io/pricing/
  reason: no-developer-program
  state: none
created: '2026-10-02'
description: Boombox.io is an all‑in‑one platform for musicians, offering tools for distribution, AI‑powered mastering, stem splitting, lyric generation, and chord progression creation. It provides apps for macOS, iOS, and Android, along with a web portal for managing releases, collaborations, and monetization. The service aims to simplify music production and distribution for independent artists and producers.
image: https://boombox.io/wp-content/uploads/2025/01/boombox-tagline.jpg
layout: provider
modified: '2026-10-02'
name: boombox.io
nav: Providers
network: true
overview: 'boombox.io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Distribution, AI Tools, and Platform.


  boombox.io''s developer surface includes getting-started guide, documentation, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Boombox Io Plans Pricing
  plan_count: 4
  slug: boombox-io-plans-pricing
random_paper: 7
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boombox Io Domain Security
  slug: boombox-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boombox-io
tags:
- Company
- Music
- Distribution
- AI Tools
- Platform
website: https://boombox.io
---
