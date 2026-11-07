---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/mertech/hosts/mertech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mertech-hosts.yml
- group: other
  href: https://artifacts.apis.io/mertech/vendors/mertech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mertech-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mertech.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://support.mertech.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mertech.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mertech.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.mertech.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mertech.com/
- group: auth
  href: https://artifacts.apis.io/mertech/security/mertech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mertech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mertech.com/
coverage:
  checked: '2026-10-18'
  detail: Documentation at docs.mertech.com provides only HTML pages with no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract files.
  evidence:
  - status: 200
    url: https://docs.mertech.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Mertech Data Systems provides software and solutions for companies trapped in legacy applications, databases, and infrastructure, helping them modernize and migrate to cloud platforms. Their offerings include data migration, application modernization, and multi-protocol API services supporting REST, SOAP, JSON-RPC, Thrift, and gRPC.
layout: provider
modified: '2026-10-18'
name: Mertech Data Systems
nav: Providers
network: true
overview: 'Mertech Data Systems is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Application Modernization, Database Migration, Reporting Tools, Web Services, and DataFlex.


  Mertech Data Systems'' developer surface includes support, engineering blog, documentation, and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 44.6
    operational_transparency: 7.9
  previous_composite: 13.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/mertech/mertech-2026-11-03T135510.png
security:
- kind: domain-security
  name: Mertech Domain Security
  slug: mertech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mertech
tags:
- Application Modernization
- Database Migration
- Reporting Tools
- Web Services
- DataFlex
- Btrieve
website: https://mertech.com/
---
