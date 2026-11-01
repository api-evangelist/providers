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
- description: FreshRSS provides a Google‑Reader‑compatible API for mobile clients and integrations.
  name: FreshRSS API
  slug: freshrss-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/freshrss/hosts/freshrss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/freshrss-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FreshRSS
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/FreshRSS/FreshRSS/releases/latest
- group: auth
  href: https://artifacts.apis.io/freshrss/security/freshrss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freshrss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://freshrss.org/
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found on the provider's hosts.
  evidence:
  - status: 200
    url: https://freshrss.org/
  - status: error
    url: https://api.freshrss.org/openapi.json
  - status: 404
    url: https://demo.freshrss.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: FreshRSS is a free, self‑hostable RSS and Atom feed aggregator. It is lightweight, powerful, and customizable, supporting multi‑user setups, extensions, WebSub push, and a Google‑Reader‑compatible API for mobile clients. The project is open‑source under AGPL‑3, with extensive documentation, demo instance, and community support.
image: https://freshrss.org/card.png
layout: provider
modified: '2026-10-28'
name: FreshRSS
nav: Providers
network: true
overview: 'FreshRSS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include RSS Aggregator, Self‑Hosted Software, Feed Reader, Web Scraping, and OPML.


  FreshRSS''s developer surface includes changelog and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Freshrss Domain Security
  slug: freshrss-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC
slug: freshrss
tags:
- RSS Aggregator
- Self‑Hosted Software
- Feed Reader
- Web Scraping
- OPML
- WebSub
- Open Source
website: https://freshrss.org/
---
