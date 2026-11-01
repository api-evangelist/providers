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
- description: Data service and API management platform
  name: DataAPI
  slug: dataapi
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/dtstack/hosts/dtstack-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dtstack-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dtstack.com/zh-cn/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dtstack.com/zh-cn/privacy/
- group: auth
  href: https://artifacts.apis.io/dtstack/security/dtstack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dtstack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dtstack.com
coverage:
  checked: '2026-10-24'
  detail: Documentation pages are HTML without published OpenAPI or other machine-readable contracts.
  evidence:
  - status: 200
    url: https://www.dtstack.com/zh-cn/products/dataapi/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Dtstack provides a leading multimodal big data infrastructure platform and AI application services. It offers data storage, computing, governance, and analytics solutions for enterprises, covering AI data foundations, data pipelines, and intelligent operations across industries such as energy, finance, and manufacturing.
image: https://www.dtstack.com/cms-media/2026-newweb-dt/OG_0a5c9f9a33.png
layout: provider
modified: '2026-10-24'
name: Dtstack
nav: Providers
network: true
overview: Dtstack is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, BigData, AI, Cloud, and Enterprise.
random_paper: 6
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dtstack Domain Security
  slug: dtstack-domain-security
  summary_line: TLSv1.3
slug: dtstack
tags:
- Company
- BigData
- AI
- Cloud
- Enterprise
website: https://www.dtstack.com
---
