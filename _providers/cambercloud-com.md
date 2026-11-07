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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Camber API provides AI-powered data science platform capabilities. Documentation is at https://docs.cambercloud.com/.
  name: Camber API
  slug: camber-api
- baseURL: https://cli.cambercloud.com
  baseurl_source: declared
  description: 'Camber API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Camber API
  slug: cambercloud-com-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/cambercloud-com/rules/cambercloud-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cambercloud-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cambercloud-com/vocabulary/cambercloud-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cambercloud-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cambercloud-com/conformance/cambercloud-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cambercloud-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cambercloud-com/llms/cambercloud-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cambercloud-com-llms.txt
- group: other
  href: https://artifacts.apis.io/cambercloud-com/hosts/cambercloud-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cambercloud-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cambercloud-com/vendors/cambercloud-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cambercloud-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.cambercloud.com/docs/privacy-terms/
- group: start
  href: https://artifacts.apis.io/cambercloud-com/docs/sep-01-getting-started/
  title: ''
  type: GettingStarted
  url: /docs/sep-01-getting-started/
- group: auth
  href: https://artifacts.apis.io/cambercloud-com/security/cambercloud-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cambercloud-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cambercloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cambercloud.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cambercloud.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.cambercloud.com/login
coverage:
  checked: '2026-11-04'
  detail: The provider's documentation site does not publish any OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.cambercloud.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Camber provides AI for data science teams, enabling creation of custom AI agents in minutes with unlimited CPU/GPU on demand. It offers native connectors to Snowflake, Databricks, BigQuery, S3, Google Drive, and a free trial, targeting data science workflows and collaborative AI development.
image: https://cdn.prod.website-files.com/681a24354efe21a04772abd0/686fc5bf918e427c979115c0_clip.png
layout: provider
modified: '2026-11-04'
name: Camber
nav: Providers
network: true
overview: 'Camber is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data Science, Machine Learning, Cloud, and Platform.


  The Camber catalog on APIs.io includes 1 Spectral governance ruleset.


  Camber''s developer surface includes getting-started guide, documentation, pricing, signup flow, and 9 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 63
  extends:
  - spectral:oas
  name: Camber API Rules
  rule_count: 22
  severity_counts:
    error: 20
    hint: 0
    info: 1
    warn: 1
  slug: cambercloud-com-rules
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 10.7
    developer_ergonomics: 16.7
    discoverability: 57.1
    operational_transparency: 0.0
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
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cambercloud Com Domain Security
  slug: cambercloud-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cambercloud-com
tags:
- Artificial Intelligence
- Data Science
- Machine Learning
- Cloud
- Platform
- Company
website: https://cambercloud.com/
---
