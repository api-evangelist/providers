---
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: AI-driven tools for goal tracking, business reviews, risk catching and decision follow‑up across teams.
  name: Rhythms API
  slug: rhythms-api
- baseURL: https://api.rhythms.ai
  baseurl_source: declared
  description: 'Rhythms API as documented publicly: 30 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Rhythms API
  slug: getrhythms-ai-api
artifact_total: 11
common:
- group: other
  href: https://artifacts.apis.io/getrhythms-ai/vendors/getrhythms-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getrhythms-ai-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.rhythms.ai/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.rhythms.ai/
- group: design
  href: https://artifacts.apis.io/getrhythms-ai/rules/getrhythms-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/getrhythms-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/getrhythms-ai/json-ld/getrhythms-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getrhythms-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/getrhythms-ai/vocabulary/getrhythms-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getrhythms-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getrhythms-ai/data-model/getrhythms-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getrhythms-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/getrhythms-ai/changelog/getrhythms-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/getrhythms-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/getrhythms-ai/conformance/getrhythms-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getrhythms-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getrhythms-ai/llms/getrhythms-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getrhythms-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/getrhythms-ai/well-known/getrhythms-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getrhythms-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/getrhythms-ai/hosts/getrhythms-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getrhythms-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rhythms.ai/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://help.rhythms.ai/articles/2761750109-rhythms-mcp-is-now-available-in-claude-chatgpt-and-cursor
- group: start
  title: ''
  type: SignUp
  url: https://app.rhythms.ai/auth/signup?returnTo=%2F
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rhythms.ai/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.rhythms.ai/company/press
- group: auth
  href: https://artifacts.apis.io/getrhythms-ai/security/getrhythms-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getrhythms-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rhythms.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.rhythms.ai/blog/
coverage:
  checked: '2026-10-21'
  detail: Main website renders via Framer and provides no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://www.rhythms.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: Rhythms provides AI-driven tools to keep goals and priorities on track, gathering updates, preparing business reviews, catching risks, and following decisions across teams and systems. Their platform integrates with existing workflows to ensure alignment and visibility, helping organizations make data‑driven decisions and maintain operational momentum.
image: https://framerusercontent.com/assets/EXR92mOH2i67FysmJAiWLFdmLY.png
json_schemas:
- name: PostRestV2CheckinsRequest
  property_count: 9
  slug: getrhythms-ai-post-rest-v2-checkins-request
- name: PostRestV2InitiativesRequest
  property_count: 14
  slug: getrhythms-ai-post-rest-v2-initiatives-request
- name: PostRestV2KeyResultsRequest
  property_count: 14
  slug: getrhythms-ai-post-rest-v2-key-results-request
- name: PostRestV2ObjectivesRequest
  property_count: 14
  slug: getrhythms-ai-post-rest-v2-objectives-request
- name: PutRestV2InitiativesIdRequest
  property_count: 16
  slug: getrhythms-ai-put-rest-v2-initiatives-id-request
- name: PutRestV2ObjectivesIdRequest
  property_count: 16
  slug: getrhythms-ai-put-rest-v2-objectives-id-request
jsonld:
- class_count: 17
  name: Getrhythms Ai Context
  property_count: 30
  slug: getrhythms-ai-context
layout: provider
modified: '2026-10-21'
name: Rhythms
nav: Providers
network: true
overview: 'Rhythms is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Productivity, Workflow, and Business-Intelligence.


  The Rhythms catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rhythms'' developer surface includes getting-started guide, documentation, changelog, support, signup flow, engineering blog, and 14 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Rhythms API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: getrhythms-ai-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 26.3
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Getrhythms Ai Domain Security
  slug: getrhythms-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getrhythms-ai
tags:
- Company
- AI
- Productivity
- Workflow
- Business-Intelligence
website: https://www.rhythms.ai/
---
