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
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-06'
  detail: Academic Capital Exchange, a 2008 Chicago peer-to-peer student loan marketplace, is gone and its domain was never re-registered — whois returns "No match for domain ACADEMICCAPITALEXCHANGE.COM" and DNS returns NXDOMAIN, so there is no host on which an OpenAPI, /.well-known/ document, agent card or MCP endpoint could be probed, and the Internet Archive holds exactly one snapshot of the site, from February 2008.
  evidence:
  - status: 0
    url: https://academiccapitalexchange.com/
  - status: 0
    url: https://www.academiccapitalexchange.com/
  - status: 404
    url: https://api.github.com/orgs/academiccapitalexchange
  - status: 404
    url: https://api.github.com/orgs/academic-capital-exchange
  - status: 200
    url: http://archive.org/wayback/available?url=academiccapitalexchange.com
  - status: 200
    url: https://equityzen.com/company/academiccapitalexchange/
  reason: defunct
  state: none
created: '2026-09-06'
description: 'Academic Capital Exchange (ACE) was a Chicago, Illinois online peer-to-peer student loan marketplace founded in 2008 by Shawn Bercuson, built to link students to the financial support and professional guidance needed to succeed in the classroom and beyond by matching student borrowers directly with individual lenders rather than routing them through a bank or a federal loan servicer. It followed CapAlly, an earlier peer-to-peer student lending marketplace and social network the same founder started in 2007 and sold before taking it to market. ACE was a consumer-facing lending marketplace, not a developer platform: it never operated a developer portal, never published a machine-readable API contract, and never shipped client SDKs, and no GitHub organization under the company name exists. The company is no longer operating. Its host academiccapitalexchange.com is not merely offline but entirely unregistered — whois returns "No match" and DNS returns NXDOMAIN for the .com, .net,
  .co and .io labels — and the Internet Archive holds a single snapshot of the site, from February 2008. The only surviving public record of the company is a secondary-market listing page on EquityZen, which is a trading venue and not the company''s own web presence, so it is deliberately not wired as a Website pointer. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-09-06'
name: Academic Capital Exchange
nav: Providers
network: true
overview: Academic Capital Exchange is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Financial Services, Lending, and Student Loans.
random_paper: 0
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: academiccapitalexchange
tags:
- Company
- Defunct
- Financial Services
- Lending
- Student Loans
- Peer-to-Peer Lending
- Education Finance
- Marketplace
---
