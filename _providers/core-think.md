---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
- description: Advanced agentic reasoning API providing state‑of‑the‑art accuracy for complex tasks, with observable reasoning traces and OpenAI‑compatible integration.
  name: CoreThink Reasoner API
  slug: reasoner-api
- description: 'Core Think API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Core Think API
  slug: core-think-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/core-think/rules/core-think-rules.yml
  title: ''
  type: Spectral
  url: rules/core-think-rules.yml
- group: design
  href: https://artifacts.apis.io/core-think/json-ld/core-think-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/core-think-context.jsonld
- group: design
  href: https://artifacts.apis.io/core-think/vocabulary/core-think-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/core-think-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/core-think/data-model/core-think-data-model.yml
  title: ''
  type: DataModel
  url: data-model/core-think-data-model.yml
- group: design
  href: https://artifacts.apis.io/core-think/conformance/core-think-conformance.yml
  title: ''
  type: Conformance
  url: conformance/core-think-conformance.yml
- group: other
  href: https://artifacts.apis.io/core-think/hosts/core-think-hosts.yml
  title: ''
  type: Hosts
  url: hosts/core-think-hosts.yml
- group: other
  href: https://artifacts.apis.io/core-think/vendors/core-think-vendors.yml
  title: ''
  type: Vendors
  url: vendors/core-think-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.corethink.ai/
- group: auth
  href: https://artifacts.apis.io/core-think/security/core-think-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/core-think-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://corethink.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://workbench.corethink.ai/app/
- group: operate
  title: ''
  type: Support
  url: https://corethink.ai/waitlist
- group: company
  title: ''
  type: Blog
  url: https://corethink.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoreThink-AI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://corethink.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corethink.ai/privacy
coverage:
  checked: '2026-10-29'
  detail: Documentation provides API overview and base URL but no machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://developer.corethink.ai/docs/overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Core Think builds a neurosymbolic AI platform that enables fine‑tuning of large language models through program synthesis. Their product lets users decompose model knowledge into explicit, typed modules that can be inspected, versioned, and kept private. The platform offers tools for building, verifying, and deploying AI chains, with open research papers and a developer workbench for custom builds.
image: https://corethink.ai
json_schemas:
- name: PostV1CompletionsRequest
  property_count: 4
  slug: core-think-post-v1-completions-request
jsonld:
- class_count: 1
  name: Core Think Context
  property_count: 4
  slug: core-think-context
layout: provider
modified: '2026-10-29'
name: Core Think
nav: Providers
network: true
overview: 'Core Think is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Neurosymbolic, Platform, and Machine Learning.


  The Core Think catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Core Think''s developer surface includes documentation, support, engineering blog, and 13 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Core Think API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: core-think-rules
scopes:
- name: Core Think Scopes
  scope_count: 0
  slug: core-think-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.6
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/core-think/core-think-2026-11-03T125316.png
security:
- kind: authentication
  name: Core Think Authentication
  slug: core-think-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Core Think Domain Security
  slug: core-think-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: core-think
tags:
- Company
- Artificial Intelligence
- Neurosymbolic
- Platform
- Machine Learning
website: https://corethink.ai
---
