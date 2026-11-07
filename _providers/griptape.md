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
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://cloud.griptape.ai
  baseurl_source: declared
  description: 'Foundry API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Foundry API
  slug: griptape-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/griptape/rules/griptape-rules.yml
  title: ''
  type: Spectral
  url: rules/griptape-rules.yml
- group: design
  href: https://artifacts.apis.io/griptape/json-ld/griptape-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/griptape-context.jsonld
- group: design
  href: https://artifacts.apis.io/griptape/vocabulary/griptape-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/griptape-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/griptape/data-model/griptape-data-model.yml
  title: ''
  type: DataModel
  url: data-model/griptape-data-model.yml
- group: design
  href: https://artifacts.apis.io/griptape/conformance/griptape-conformance.yml
  title: ''
  type: Conformance
  url: conformance/griptape-conformance.yml
- group: agent
  href: https://artifacts.apis.io/griptape/llms/griptape-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/griptape-llms.txt
- group: other
  href: https://artifacts.apis.io/griptape/hosts/griptape-hosts.yml
  title: ''
  type: Hosts
  url: hosts/griptape-hosts.yml
- group: other
  href: https://artifacts.apis.io/griptape/vendors/griptape-vendors.yml
  title: ''
  type: Vendors
  url: vendors/griptape-vendors.yml
- group: build
  href: https://artifacts.apis.io/griptape/packages/griptape-packages.yml
  title: ''
  type: SDKs
  url: packages/griptape-packages.yml
- group: build
  href: https://artifacts.apis.io/griptape/packages/griptape-packages.yml
  title: ''
  type: Packages
  url: packages/griptape-packages.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.griptape.ai/team
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.griptape.ai/stable/griptape-cloud/data-sources/getting-started-with-data-sources
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.griptapenodes.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.griptape.ai/stable/griptape-cloud/api/api-reference/
- group: auth
  href: https://artifacts.apis.io/griptape/security/griptape-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/griptape-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://griptape.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.griptape.ai/stable/
- group: company
  title: ''
  type: Blog
  url: https://www.griptape.ai/blog
created: '2026-10-20'
description: Griptape is a platform that enables developers and creative professionals to orchestrate multiple AI models and agents within secure, professional workflows. It offers a visual node‑based builder, a Python framework, and cloud deployment options, allowing users to build, scale, and manage AI‑powered applications without deep prompt‑engineering expertise. Griptape focuses on flexibility, security, and collaboration, providing tools for both code‑first developers and no‑code creators to integrate generative AI into their products.
image: https://cdn.prod.website-files.com/65d658559223871198e78bca/69a6e732e154609786d9e9cc_feb9d9ee07bfd00b321c90c53f7cfe3d_Open-Graph.png
json_schemas:
- name: PostApiKnowledgeBasesRequest
  property_count: 1
  slug: griptape-post-api-knowledge-bases-request
jsonld:
- class_count: 1
  name: Griptape Context
  property_count: 1
  slug: griptape-context
layout: provider
modified: '2026-10-20'
name: Foundry
nav: Providers
network: true
overview: 'Foundry is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Workflows, Automation, and Open Source.


  The Foundry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Foundry''s developer surface includes getting-started guide, API reference, documentation, engineering blog, and 14 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Foundry API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: griptape-rules
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 18.1
    developer_ergonomics: 27.4
    discoverability: 74.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/griptape/griptape-2026-11-03T133105.png
security:
- kind: domain-security
  name: Griptape Domain Security
  slug: griptape-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: griptape
tags:
- Artificial Intelligence
- Platform
- Workflows
- Automation
- Open Source
website: https://griptape.ai/
---
