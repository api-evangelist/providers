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
- group: agent
  href: https://artifacts.apis.io/datazip/llms/datazip-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datazip-llms.txt
- group: other
  href: https://artifacts.apis.io/datazip/hosts/datazip-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datazip-hosts.yml
- group: other
  href: https://artifacts.apis.io/datazip/vendors/datazip-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datazip-vendors.yml
- group: auth
  href: https://artifacts.apis.io/datazip/security/datazip-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datazip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datazip.io/
- group: docs
  title: ''
  type: Documentation
  url: https://olake.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://olake.io/docs/getting-started/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://olake.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datazip-inc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://olake.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://olake.io/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://olake.io/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://olake.io/compare/
coverage:
  checked: '2026-10-20'
  detail: Documentation at https://olake.io/docs/ provides API reference but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec was found.
  evidence:
  - status: 0
    url: https://api.datazip.io/openapi.json
  - status: 0
    url: https://api.olake.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Datazip, Inc. provides the OLake platform, an open‑source solution for ingesting, maintaining, and querying Apache Iceberg tables. The company focuses on simplifying data pipelines, offering tools for replication, real‑time streaming, and data lake management across Kafka, S3, and various databases. With a strong community, extensive documentation, and enterprise‑grade features, Datazip helps organizations accelerate data engineering workflows and ensure reliable, scalable analytics.
layout: provider
modified: '2026-10-20'
name: Datazip, Inc.
nav: Providers
network: true
overview: 'Datazip, Inc. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Engineering, Open Source, Apache Iceberg, and Data Platform.


  Datazip, Inc.''s developer surface includes documentation, getting-started guide, engineering blog, support, pricing, and 8 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 51.8
    operational_transparency: 2.6
  previous_composite: 17.7
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
screenshot: https://apis.io/screenshots/datazip/datazip-2026-11-03T130300.png
security:
- kind: domain-security
  name: Datazip Domain Security
  slug: datazip-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: datazip
tags:
- Company
- Data Engineering
- Open Source
- Apache Iceberg
- Data Platform
website: https://datazip.io/
---
