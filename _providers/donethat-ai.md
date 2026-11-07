---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API reference for DoneThat platform
  name: DoneThat API
  slug: donethat-api
- baseURL: https://api.donethat.ai
  baseurl_source: declared
  description: 'DoneThat API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DoneThat API
  slug: donethat-ai-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/donethat-ai/plans/donethat-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/donethat-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/donethat-ai/rules/donethat-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/donethat-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/donethat-ai/json-ld/donethat-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/donethat-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/donethat-ai/vocabulary/donethat-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/donethat-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/donethat-ai/data-model/donethat-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/donethat-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.donethat.ai/
- group: auth
  href: https://artifacts.apis.io/donethat-ai/security/donethat-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/donethat-ai-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/donethat-ai/errors/donethat-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/donethat-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/donethat-ai/conformance/donethat-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/donethat-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/donethat-ai/llms/donethat-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/donethat-ai-llms.txt
- group: auth
  href: https://artifacts.apis.io/donethat-ai/well-known/donethat-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/donethat-ai-security.txt
- group: auth
  href: https://artifacts.apis.io/donethat-ai/well-known/donethat-ai-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/donethat-ai-app-security.txt
- group: agent
  href: https://artifacts.apis.io/donethat-ai/well-known/donethat-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/donethat-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/donethat-ai/hosts/donethat-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/donethat-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/donethat-ai/vendors/donethat-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/donethat-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://donethat.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://donethat.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://donethat.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://donethat.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://donethat.ai/blog
- group: docs
  title: ''
  type: APIReference
  url: https://donethat.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://donethat.ai/install/linux
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.donethat.ai</span
- group: auth
  href: https://artifacts.apis.io/donethat-ai/security/donethat-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/donethat-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/donethat-ai/security/donethat-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/donethat-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/donethat-ai/security/donethat-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/donethat-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://donethat.ai/
coverage:
  checked: '2026-11-05'
  detail: API reference page returns HTML without a machine‑readable OpenAPI or GraphQL spec.
  evidence:
  - status: 200
    url: https://donethat.ai/api-reference
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: DoneThat provides automatic AI-powered time tracking for remote workers, capturing activity privately without timers or meetings. The platform offers AI summaries, coaching, and integrates with tools like Slack, helping teams stay focused, visible, and trusted while respecting privacy.
image: https://donethat.ai/og/pages/home.png
json_schemas:
- name: GetProjectsIdResponse
  property_count: 2
  slug: donethat-ai-get-projects-id-response
- name: PostProjectsIdRequest
  property_count: 8
  slug: donethat-ai-post-projects-id-request
- name: PostProjectsIdResponse
  property_count: 2
  slug: donethat-ai-post-projects-id-response
- name: PostReportResponse
  property_count: 1
  slug: donethat-ai-post-report-response
jsonld:
- class_count: 5
  name: Donethat Ai Context
  property_count: 11
  slug: donethat-ai-context
layout: provider
modified: '2026-11-05'
name: DoneThat
nav: Providers
network: true
overview: 'DoneThat is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Time Tracking, Artificial Intelligence, Remote Work, and Productivity.


  The DoneThat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DoneThat''s developer surface includes support, pricing, engineering blog, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Donethat Ai Plans Pricing
  plan_count: 6
  slug: donethat-ai-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: DoneThat API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: donethat-ai-rules
score:
  band: developing
  composite: 43.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 35.6
    contract_quality: 25.2
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Donethat Ai Domain Security
  slug: donethat-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Donethat Ai Vulnerability Disclosure
  slug: donethat-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Donethat Ai Trust Center
  slug: donethat-ai-trust-center
  summary_line: SOC 2, GDPR
slug: donethat-ai
tags:
- Company
- Time Tracking
- Artificial Intelligence
- Remote Work
- Productivity
website: https://donethat.ai/
---
