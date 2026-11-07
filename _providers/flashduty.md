---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    event_surface_described: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Flashduty API as documented publicly: 62 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Flashduty API
  slug: flashduty-api
artifact_total: 12
asyncapis:
- description: ''
  name: Flashduty Webhooks
  slug: flashduty-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/flashduty/plans/flashduty-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flashduty-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/flashduty/rules/flashduty-rules.yml
  title: ''
  type: Spectral
  url: rules/flashduty-rules.yml
- group: design
  href: https://artifacts.apis.io/flashduty/json-ld/flashduty-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/flashduty-context.jsonld
- group: design
  href: https://artifacts.apis.io/flashduty/vocabulary/flashduty-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/flashduty-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/flashduty/asyncapi/flashduty-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/flashduty-webhooks.yml
- group: design
  href: https://artifacts.apis.io/flashduty/data-model/flashduty-data-model.yml
  title: ''
  type: DataModel
  url: data-model/flashduty-data-model.yml
- group: build
  href: https://artifacts.apis.io/flashduty/cli/flashduty-cli.yml
  title: ''
  type: CLI
  url: cli/flashduty-cli.yml
- group: operate
  href: https://artifacts.apis.io/flashduty/changelog/flashduty-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/flashduty-changelog.yml
- group: design
  href: https://artifacts.apis.io/flashduty/conventions/flashduty-conventions.yml
  title: ''
  type: Conventions
  url: conventions/flashduty-conventions.yml
- group: design
  href: https://artifacts.apis.io/flashduty/conformance/flashduty-conformance.yml
  title: ''
  type: Conformance
  url: conformance/flashduty-conformance.yml
- group: agent
  href: https://artifacts.apis.io/flashduty/llms/flashduty-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/flashduty-llms.txt
- group: other
  href: https://artifacts.apis.io/flashduty/a2a/flashduty-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/flashduty-a2a.yml
- group: other
  href: https://artifacts.apis.io/flashduty/hosts/flashduty-hosts.yml
  title: ''
  type: Hosts
  url: hosts/flashduty-hosts.yml
- group: other
  href: https://artifacts.apis.io/flashduty/vendors/flashduty-vendors.yml
  title: ''
  type: Vendors
  url: vendors/flashduty-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.flashduty.com/en/compliance/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.flashduty.com/en/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.flashduty.com/en/compliance/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flashcatcloud
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.flashduty.com/en/now/changelog
- group: auth
  href: https://artifacts.apis.io/flashduty/security/flashduty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flashduty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flashduty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flashduty.com/en/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flashduty.com/en/openapi/introduction
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flashduty.com/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.flashduty.com/en/now/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flashduty.com/en/ai-sre/quickstart
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are JavaScript‑rendered and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://www.flashduty.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Flashduty provides an agent‑first incident response platform powered by AI. It aggregates alerts from over 60 sources, de‑duplicates them, and uses large‑language models to suggest root causes and guide remediation before engineers are paged. The service includes on‑call scheduling, status page integration, real‑time monitoring dashboards, and a flexible API for incident lifecycle automation. Customers benefit from reduced MTTA, lower noise, and faster recovery across cloud, SaaS, and on‑prem environments.
image: https://www.flashduty.com/og?title=Flashduty+%E2%80%94+Agent-first+Incident+Response+Platform&description=Flashduty+is+the+AI+SRE+that+correlates+alerts%2C+finds+likely+root+causes%2C+and+recommends+next+steps.+60%2B+integrations%2C+80%E2%80%9390%25+less+than+PagerDuty.
json_schemas:
- name: GetRumIssueInfoResponse
  property_count: 2
  slug: flashduty-get-rum-issue-info-response
- name: GetRumIssueListResponse
  property_count: 3
  slug: flashduty-get-rum-issue-list-response
- name: GetRumResourceInfoResponse
  property_count: 2
  slug: flashduty-get-rum-resource-info-response
- name: PostRumIssueInfoResponse
  property_count: 2
  slug: flashduty-post-rum-issue-info-response
- name: PostRumIssueListResponse
  property_count: 3
  slug: flashduty-post-rum-issue-list-response
- name: PostRumResourceInfoResponse
  property_count: 2
  slug: flashduty-post-rum-resource-info-response
jsonld:
- class_count: 60
  name: Flashduty Context
  property_count: 16
  slug: flashduty-context
layout: provider
modified: '2026-10-27'
name: Flashduty
nav: Providers
network: true
overview: 'Flashduty is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Incident Response, Artificial Intelligence, Monitoring, On-Call, and Observability.


  The Flashduty catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Flashduty''s developer surface includes CLI, changelog, documentation, API reference, pricing, engineering blog, getting-started guide, and 19 more developer resources.'
plans:
- name: Flashduty Plans Pricing
  plan_count: 3
  slug: flashduty-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Flashduty API Rules
  rule_count: 10
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 0
  slug: flashduty-rules
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 35.0
    developer_ergonomics: 22.6
    discoverability: 64.3
    operational_transparency: 23.7
  previous_composite: 44.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/flashduty/flashduty-2026-11-03T132124.png
security:
- kind: domain-security
  name: Flashduty Domain Security
  slug: flashduty-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: flashduty
tags:
- Incident Response
- Artificial Intelligence
- Monitoring
- On-Call
- Observability
- Company
website: https://flashduty.com/
---
