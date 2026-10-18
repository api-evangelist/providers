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
api_count: 1
apis:
- description: Cate and Company is a dynamic and growing HVAC distributor focusing on residential, commercial and multi‑family markets in Texas.
  name: Cate API
  slug: cate-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cate/refs/heads/main/hosts/cate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cate-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cate/refs/heads/main/security/cate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catehvac.com
coverage:
  checked: '2026-10-07'
  detail: The provider's website serves only HTML pages with no discoverable OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://catehvac.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: Cate & Company is a Texas‑based HVAC distributor focusing on residential, commercial and multi‑family markets. It offers a broad catalog of ductwork, fans, dampers, grilles, and related equipment, providing online shopping, detailed product information, and customer support. The company maintains an e‑commerce site with a login portal for account management and order tracking, and it serves the Texas HVAC market with a network of suppliers and installers.
layout: provider
modified: '2026-10-07'
name: Cate
nav: Providers
network: true
overview: Cate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 17
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
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
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Cate Domain Security
  slug: cate-domain-security
  summary_line: TLSv1.2 · DMARC
slug: cate
tags:
- Company
website: https://catehvac.com
---
