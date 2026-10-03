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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aqemia/refs/heads/main/hosts/aqemia-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aqemia-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aqemia/refs/heads/main/vendors/aqemia-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aqemia-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aqemia.com/terms-of-use
- group: company
  title: ''
  type: Newsroom
  url: https://aqemia.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aqemia
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aqemia/refs/heads/main/security/aqemia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aqemia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aqemia.com/
coverage:
  checked: 2026-09-25
  detail: No API developer program or public API documentation was found for AQEMIA.
  evidence:
  - status: DNS_ERROR
    url: https://api.aqemia.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-09-25'
description: AQEMIA is a physics‑based AI drug discovery company that leverages generative AI and deep physics to accelerate the creation of new medicines. Based in Paris and London, the firm offers a platform that integrates advanced computational models, high‑throughput simulations, and data‑driven pipelines to discover and optimize therapeutic candidates at scale. Their mission is to reinvent drug discovery by combining cutting‑edge science with AI to reduce time and cost, aiming to bring innovative treatments to patients faster.
image: https://aqemia.com/img/opengraph-image.png
layout: provider
modified: '2026-09-25'
name: AQEMIA
nav: Providers
network: true
overview: AQEMIA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Drug Discovery, Biotechnology, and Platform.
random_paper: 6
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aqemia Domain Security
  slug: aqemia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: aqemia
tags:
- Company
- Artificial Intelligence
- Drug Discovery
- Biotechnology
- Platform
website: https://aqemia.com/
---
