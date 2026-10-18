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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/biztex/refs/heads/main/well-known/biztex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/biztex-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biztex/refs/heads/main/hosts/biztex-hosts.yml
  title: ''
  type: Hosts
  url: hosts/biztex-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/biztex/refs/heads/main/vendors/biztex-vendors.yml
  title: ''
  type: Vendors
  url: vendors/biztex-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.biztex.co.jp/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.biztex.co.jp/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/biztex/refs/heads/main/security/biztex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/biztex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biztex.co.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://service.biztex.co.jp/
- group: operate
  title: ''
  type: Support
  url: https://www.biztex.co.jp/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.biztex.co.jp/privacy/
- group: company
  title: ''
  type: Blog
  url: https://note.com/biztex/
coverage:
  checked: '2026-10-16'
  detail: Documentation at https://service.biztex.co.jp/ provides only HTML pages with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://service.biztex.co.jp/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: BizteX株式会社はAIオートメーションカンパニーとして、RPA・AI-OCR・業務自動化プラットフォームを提供しています。企業の業務効率化を支援するため、インテリジェントフロー、BizteX robop、BizteX Connectなどのサービスを展開し、製造業から医療・不動産まで幅広い業界で導入実績があります。
image: https://www.biztex.co.jp/images/common/ogp.png
layout: provider
modified: '2026-10-16'
name: BizteX
nav: Providers
network: true
overview: 'BizteX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Automation, RPA, and OCR.


  BizteX''s developer surface includes documentation, support, engineering blog, and 8 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 41.1
    operational_transparency: 10.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Biztex Domain Security
  slug: biztex-domain-security
  summary_line: TLSv1.3 · DMARC
slug: biztex
tags:
- Company
- Artificial Intelligence
- Automation
- RPA
- OCR
website: https://www.biztex.co.jp/
---
