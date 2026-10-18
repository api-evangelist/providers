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
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/japan-post/refs/heads/main/llms/japan-post-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/japan-post-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/japan-post/refs/heads/main/hosts/japan-post-hosts.yml
  title: ''
  type: Hosts
  url: hosts/japan-post-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mypage.jpid.pf.japanpost.jp/register/terms?_gl=1*1m33ffs*_ga*NDEwODQwNTg3LjE3NDg0OTQxMzM.*_ga_SHH42S0D3Z*czE3Njg0MDI3NTIkbzE2JGcxJHQxNzY4NDAyNzk0JGoxOCRsMCRoMA..
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.post.japanpost.jp/privacy.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/japan-post/refs/heads/main/security/japan-post-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/japan-post-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.post.japanpost.jp
coverage:
  checked: '2026-10-13'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at api.japanpost.jp.
  evidence:
  - status: 0
    url: https://api.japanpost.jp/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: Japan Post (日本郵便株式会社) is Japan's national postal service provider, offering mail, parcel, logistics, financial and insurance services. It operates an extensive domestic and international network, providing online tools for postage calculation, tracking, address lookup, and e‑services for individuals and businesses. The corporation also runs digital platforms for e‑mail, banking, and e‑commerce support, reflecting its modernized operations beyond traditional mail.
image: https://www.post.japanpost.jp/assets/images/logo-yubin-text.svg
layout: provider
modified: '2026-10-13'
name: Japan Post
nav: Providers
network: true
overview: Japan Post is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Postal, Logistics, Finance, and E‑services.
random_paper: 9
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Japan Post Domain Security
  slug: japan-post-domain-security
  summary_line: TLSv1.3 · DMARC
slug: japan-post
tags:
- Company
- Postal
- Logistics
- Finance
- E‑services
website: https://www.post.japanpost.jp
---
