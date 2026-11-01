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
- group: agent
  href: https://artifacts.apis.io/yomitasu-jp/llms/yomitasu-jp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yomitasu-jp-llms.txt
- group: other
  href: https://artifacts.apis.io/yomitasu-jp/hosts/yomitasu-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yomitasu-jp-hosts.yml
- group: other
  href: https://artifacts.apis.io/yomitasu-jp/vendors/yomitasu-jp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yomitasu-jp-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.yomitasu.jp/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yomitasu.jp/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yomitasu.jp/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.yomitasu.jp/news/
- group: start
  title: ''
  type: Login
  url: https://www.yomitasu.jp/login/
- group: auth
  href: https://artifacts.apis.io/yomitasu-jp/security/yomitasu-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yomitasu-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yomitasu.jp/
coverage:
  checked: '2026-10-29'
  detail: No public API or developer documentation was found; all attempted contract URLs returned 404 or were unreachable.
  evidence:
  - status: 404
    url: https://www.yomitasu.jp/openapi.json
  - status: 0
    url: https://api.yomitasu.jp/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Yomitasu (https://www.yomitasu.jp/) offers a free service that transforms an entire website into an MCP (Machine‑Callable Page) server, enabling AI applications to read and interact with site content via a single instruction. Users can register sites, have AI answer questions, and retrieve page data without writing code. The platform emphasizes simplicity, free usage, and AI‑driven content extraction for Japanese‑language sites.
image: https://www.yomitasu.jp/images/og-default-v2.png
layout: provider
modified: '2026-10-29'
name: yomitasu-jp
nav: Providers
network: true
overview: 'yomitasu-jp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, MCP, Website-Transformation, and Free-Service.


  yomitasu-jp''s developer surface includes pricing and 9 more developer resources.'
random_paper: 2
scopes:
- name: Yomitasu Jp Scopes
  scope_count: 0
  slug: yomitasu-jp-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Yomitasu Jp Authentication
  slug: yomitasu-jp-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Yomitasu Jp Domain Security
  slug: yomitasu-jp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: yomitasu-jp
tags:
- Company
- AI
- MCP
- Website-Transformation
- Free-Service
- Japanese
website: https://yomitasu.jp/
---
