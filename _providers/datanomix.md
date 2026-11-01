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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/datanomix/llms/datanomix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datanomix-llms.txt
- group: other
  href: https://artifacts.apis.io/datanomix/hosts/datanomix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datanomix-hosts.yml
- group: other
  href: https://artifacts.apis.io/datanomix/vendors/datanomix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datanomix-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datanomix.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datanomix.io/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://datanomix.io/press/
- group: auth
  href: https://artifacts.apis.io/datanomix/security/datanomix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datanomix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datanomix.io
- group: operate
  title: ''
  type: Support
  url: https://datanomix.io/support
- group: company
  title: ''
  type: Blog
  url: https://datanomix.io/blog
coverage:
  checked: '2026-10-22'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.datanomix.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: DataNomix provides a data‑powered manufacturing platform that connects shop‑floor equipment, ERP systems, and analytics to enable real‑time production monitoring, quality control, and operational insights. Their solutions include production monitoring dashboards, ERP integration, G‑Code cloud services, and AI‑driven tooling analytics, helping manufacturers improve efficiency, reduce downtime, and make data‑driven decisions across the shop floor.
image: https://datanomix.io/wp-content/uploads/2021/09/AssetLibrary_Datanomix_YouTubeIcon2-06-06.png
layout: provider
modified: '2026-10-22'
name: DataNomix
nav: Providers
network: true
overview: 'DataNomix is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Manufacturing, Data Analytics, IoT, ERP Integration, and Real-Time Monitoring.


  DataNomix''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
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
  name: Datanomix Domain Security
  slug: datanomix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: datanomix
tags:
- Manufacturing
- Data Analytics
- IoT
- ERP Integration
- Real-Time Monitoring
website: https://datanomix.io
---
