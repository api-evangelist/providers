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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cureverse/refs/heads/main/hosts/cureverse-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cureverse-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cureverse/refs/heads/main/vendors/cureverse-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cureverse-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.cureverse.co.kr/News
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cureverse/refs/heads/main/security/cureverse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cureverse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cureverse.co.kr
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found after probing known hosts.
  evidence:
  - status: 0
    url: https://api.co.kr/openapi.json
  - status: 404
    url: https://www.cureverse.co.kr/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Cureverse (큐어버스) is a Korean biotechnology and research organization focused on developing innovative solutions in the fields of neuroscience, drug discovery, and clinical pipelines. The website offers sections such as About Us, R&D, Core Technologies, Research Areas, Pipeline, Investor Relations, News, Articles, Videos, Careers, and Contact. It provides information on collaborations, funded projects, and publications, reflecting a broad engagement with academic and industry partners.
image: https://cdn.imweb.me/upload/S202603243a76bc2950bb3/dfcc71f0e8826.png
layout: provider
modified: '2026-10-12'
name: Cureverse
nav: Providers
network: true
overview: Cureverse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 12
score:
  band: minimal
  composite: 2.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cureverse Domain Security
  slug: cureverse-domain-security
  summary_line: TLSv1.3
slug: cureverse
tags:
- Company
website: https://www.cureverse.co.kr
---
