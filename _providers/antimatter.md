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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for Antimatter platform offering data ingestion, policy management, and encryption operations.
  name: Antimatter REST API
  slug: antimatter-rest-api
- baseURL: https://get.antimatter.io
  baseurl_source: declared
  description: 'Antimatter API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Antimatter API
  slug: antimatter-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/antimatter/rules/antimatter-rules.yml
  title: ''
  type: Spectral
  url: rules/antimatter-rules.yml
- group: design
  href: https://artifacts.apis.io/antimatter/vocabulary/antimatter-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/antimatter-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/antimatter/cli/antimatter-cli.yml
  title: ''
  type: CLI
  url: cli/antimatter-cli.yml
- group: design
  href: https://artifacts.apis.io/antimatter/conformance/antimatter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/antimatter-conformance.yml
- group: agent
  href: https://artifacts.apis.io/antimatter/llms/antimatter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/antimatter-llms.txt
- group: other
  href: https://artifacts.apis.io/antimatter/hosts/antimatter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antimatter-hosts.yml
- group: other
  href: https://artifacts.apis.io/antimatter/vendors/antimatter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/antimatter-vendors.yml
- group: build
  href: https://artifacts.apis.io/antimatter/packages/antimatter-packages.yml
  title: ''
  type: SDKs
  url: packages/antimatter-packages.yml
- group: build
  href: https://artifacts.apis.io/antimatter/packages/antimatter-packages.yml
  title: ''
  type: Packages
  url: packages/antimatter-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rs/antimatter/latest/antimatter/
- group: auth
  href: https://artifacts.apis.io/antimatter/security/antimatter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antimatter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.antimatter.io/
coverage:
  checked: '2026-10-26'
  detail: Documentation site provides HTML docs but no machine-readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://docs.antimatter.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-25'
description: Antimatter is a data platform product offering integrated analytics, AI, and machine learning capabilities, positioned within the Databricks ecosystem. It provides developers with APIs for data ingestion, processing, and model deployment, targeting enterprise workloads. The company is backed by NEA and appears as a subsidiary or product line of Databricks, with documentation hosted on docs.antimatter.io and related resources on Databricks sites.
image: https://www.databricks.com/sites/default/files/2023-11/databricks-og-universal.png
layout: provider
modified: '2026-10-25'
name: Antimatter
nav: Providers
network: true
overview: 'Antimatter is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Platform, Analytics, Artificial Intelligence, and Machine Learning.


  The Antimatter catalog on APIs.io includes 1 Spectral governance ruleset.


  Antimatter''s developer surface includes CLI and 11 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Antimatter API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: antimatter-rules
score:
  band: emerging
  composite: 14.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 19.0
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 15.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/antimatter/antimatter-2026-11-03T120856.png
security:
- kind: domain-security
  name: Antimatter Domain Security
  slug: antimatter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: antimatter
tags:
- Company
- Data Platform
- Analytics
- Artificial Intelligence
- Machine Learning
website: https://www.antimatter.io/
---
