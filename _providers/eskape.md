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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Subscriber API providing football odds, fixtures, pricing, and live updates via SignalR.
  name: ESKape Sportsbook Feed API
  slug: eskape-sportsbook-feed-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/eskape/hosts/eskape-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eskape-hosts.yml
- group: auth
  href: https://artifacts.apis.io/eskape/security/eskape-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eskape-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eskape.pro/feed
- group: start
  title: ''
  type: DeveloperPortal
  url: https://eskape.pro
- group: docs
  title: ''
  type: Documentation
  url: https://eskape.pro
- group: docs
  title: ''
  type: APIReference
  url: https://eskape.pro/openapi/public.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eskape.pro/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eskape.pro/privacy
created: '2026-10-23'
description: ESKape Sportsbook Feed provides a B2B football odds API for licensed betting operators and platforms. It offers RESTful JSON endpoints for pre‑match odds, risk management, and live updates via SignalR on paid plans. The free 90‑day plan includes access to the full pre‑match catalogue, with quota limits and clear error handling. Designed for business‑to‑business integration, it is not for private individuals or consumer betting sites.
image: https://eskape.pro/brand/og-card.png
layout: provider
modified: '2026-10-23'
name: ESKape Sportsbook Feed
nav: Providers
network: true
overview: 'ESKape Sportsbook Feed is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sportsbook, OddsAPI, B2B, Football, and Betting.


  ESKape Sportsbook Feed''s developer surface includes documentation, API reference, and 6 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Eskape Domain Security
  slug: eskape-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: eskape
tags:
- Sportsbook
- OddsAPI
- B2B
- Football
- Betting
website: https://eskape.pro/feed
---
