---
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/scraptik-com/llms/scraptik-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scraptik-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/scraptik-com/well-known/scraptik-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scraptik-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/scraptik-com/hosts/scraptik-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scraptik-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/scraptik-com/vendors/scraptik-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scraptik-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://scraptik.com/login
- group: auth
  href: https://artifacts.apis.io/scraptik-com/security/scraptik-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scraptik-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://scraptik.com/
coverage:
  checked: '2026-10-31'
  detail: All attempted OpenAPI discovery URLs on scraptik.com returned 404, and no documentation host was found.
  evidence:
  - status: 404
    url: https://scraptik.com/openapi.json
  - status: 404
    url: https://scraptik.com/openapi.yaml
  - status: 404
    url: https://scraptik.com/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: ScrapTik provides an unofficial TikTok API that delivers creator analytics, video statistics, comments, and search capabilities. It offers data such as follower counts, video performance metrics, comment threads, hashtag trends, and sound usage, accessible via a REST API on RapidAPI, an Apify actor, or an MCP server for AI agents. The service supports pay‑per‑call pricing, custom volume plans, and integrates with platforms like Base for cryptocurrency payments. It is aimed at developers, marketers, and analysts needing public TikTok data without requiring an official TikTok account.
image: https://scraptik.com/assets/wordmark-3371ef81a6fa1016d41345ca14ef714099267df6a18215f3d21db38d34f46c77.png
layout: provider
modified: '2026-10-31'
name: scraptik-com
nav: Providers
network: true
overview: scraptik-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Social Media, Analytics, TikTok, and Data.
plans:
- name: Scraptik Com Plans Pricing
  plan_count: 0
  slug: scraptik-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Scraptik Com Rate Limits
  slug: scraptik-com-rate-limits
scopes:
- name: Scraptik Com Scopes
  scope_count: 0
  slug: scraptik-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Scraptik Com Authentication
  slug: scraptik-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Scraptik Com Domain Security
  slug: scraptik-com-domain-security
  summary_line: TLSv1.3
slug: scraptik-com
tags:
- Company
- Social Media
- Analytics
- TikTok
- Data
- Marketing
website: https://scraptik.com/
---
