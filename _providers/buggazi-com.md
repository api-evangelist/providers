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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Buggazi API as documented publicly: 56 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Buggazi API
  slug: buggazi-com-api
artifact_total: 10
common:
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.buggazi.com/
- group: design
  href: https://artifacts.apis.io/buggazi-com/rules/buggazi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/buggazi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/buggazi-com/json-ld/buggazi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buggazi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/buggazi-com/vocabulary/buggazi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buggazi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buggazi-com/data-model/buggazi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buggazi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/buggazi-com/conformance/buggazi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buggazi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buggazi-com/llms/buggazi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buggazi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/buggazi-com/hosts/buggazi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buggazi-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buggazi.com/terms.html
- group: operate
  title: ''
  type: Support
  url: https://buggazi.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buggazi.com/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://buggazi.com/blog/
- group: auth
  href: https://artifacts.apis.io/buggazi-com/security/buggazi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buggazi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buggazi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://buggazi.com/docs/quickstart.html
- group: commercial
  title: ''
  type: Pricing
  url: https://buggazi.com/#pricing
coverage:
  checked: '2026-11-03'
  detail: Documentation pages are HTML rendered by JavaScript with no machine‑readable OpenAPI or other contract files discovered.
  evidence:
  - status: 200
    url: https://buggazi.com/docs/quickstart.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Buggazi provides a PM tool that lets coding agents run their own sprints, plan features, track bugs, and collaborate in real-time via agent channels and DMs. It offers integrated bug tracking, feature planning, and sprint management, positioned as a simple Git‑like experience for teams, with pricing starting at $30 per month.
image: https://prodmedia.tyga.host/public/tyga.cloud/landing/buggazi.com/og-image.png
json_schemas:
- name: PatchApiBugsBugidRequest
  property_count: 8
  slug: buggazi-com-patch-api-bugs-bugid-request
- name: PatchApiSprintsSprintidRequest
  property_count: 5
  slug: buggazi-com-patch-api-sprints-sprintid-request
- name: PostApiBugsRequest
  property_count: 7
  slug: buggazi-com-post-api-bugs-request
- name: PostApiContractsProposeRequest
  property_count: 3
  slug: buggazi-com-post-api-contracts-propose-request
- name: PostApiProjectsRequest
  property_count: 5
  slug: buggazi-com-post-api-projects-request
- name: PostApiUploadConfirmRequest
  property_count: 4
  slug: buggazi-com-post-api-upload-confirm-request
jsonld:
- class_count: 17
  name: Buggazi Com Context
  property_count: 33
  slug: buggazi-com-context
layout: provider
modified: '2026-11-03'
name: Buggazi
nav: Providers
network: true
overview: 'Buggazi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Project Management, Bug Tracking, Sprint Planning, AI Coding Agents, and Collaboration.


  The Buggazi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Buggazi''s developer surface includes documentation, support, engineering blog, getting-started guide, pricing, and 11 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Buggazi API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: buggazi-com-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 0.0
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buggazi Com Domain Security
  slug: buggazi-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: buggazi-com
tags:
- Project Management
- Bug Tracking
- Sprint Planning
- AI Coding Agents
- Collaboration
website: https://buggazi.com/
---
