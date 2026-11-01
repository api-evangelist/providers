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
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/common-com/hosts/common-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/common-com-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://common.com
- group: auth
  href: https://artifacts.apis.io/common-com/security/common-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/common-com-domain-security.yml
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://common.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Common is a technology platform that provides a unified API gateway for integrating disparate services across enterprises. It enables developers to access a catalog of standardized endpoints for data retrieval, transaction processing, and analytics, simplifying the creation of cross‑system applications. Backed by Norwest Venture Partners, Common focuses on scalability, security, and developer experience, offering comprehensive documentation, SDKs, and support resources to accelerate integration projects for businesses of all sizes.
image: https://a.mpcdn.io/hilcodigital/2023/06/Web3@2x.png?fm=png&ixlib=php-3.3.1
layout: provider
modified: '2026-10-22'
name: Common
nav: Providers
network: true
overview: Common is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, API-Gateway, Enterprise, and Platform.
random_paper: 5
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
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
  name: Common Com Domain Security
  slug: common-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: common-com
tags:
- Company
- Integration
- API-Gateway
- Enterprise
- Platform
website: https://common.com
---
