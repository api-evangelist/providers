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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Programmatic in‑game advertising platform for developers
  name: Anzu API
  slug: anzu-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anzuio/refs/heads/main/llms/anzuio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anzuio-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/anzuio/refs/heads/main/well-known/anzuio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anzuio-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anzuio/refs/heads/main/hosts/anzuio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anzuio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anzuio/refs/heads/main/vendors/anzuio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anzuio-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anzuio/refs/heads/main/security/anzuio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anzuio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/anzuio
- group: docs
  title: ''
  type: Documentation
  url: https://www.anzu.io/developers
- group: company
  title: ''
  type: Blog
  url: https://www.anzu.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anzu.io/advertisers
- group: operate
  title: ''
  type: Support
  url: https://www.anzu.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anzu.io/advertisers-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anzu.io/privacy-policy
coverage:
  checked: 2026-09-25
  detail: Developers page renders via JavaScript, no machine‑readable spec discovered.
  evidence:
  - status: 200
    url: https://www.anzu.io/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: Anzuio is a programmatic in‑game advertising platform that enables developers to monetize their games through intrinsic ad placements. Founded to provide a seamless SDK and API for integrating ads directly into game engines, Anzuio offers tools for ad selection, fraud detection, and brand uplift measurement. The company serves mobile, PC, and console developers, delivering real‑time ad serving and detailed analytics to maximize revenue while preserving player experience. Anzuio’s platform is built for scalability and compliance, supporting global ad networks and offering extensive documentation for developers.
layout: provider
modified: '2026-09-25'
name: Anzuio
nav: Providers
network: true
overview: 'Anzuio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Gaming, and SDK.


  Anzuio''s developer surface includes documentation, engineering blog, pricing, support, and 8 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 51.8
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anzuio Domain Security
  slug: anzuio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anzuio
tags:
- Company
- Advertising
- Gaming
- SDK
website: https://equityzen.com/company/anzuio
---
