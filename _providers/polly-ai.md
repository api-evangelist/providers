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
    event_surface_described: unknown
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.polly.ai/v1
  baseurl_source: declared
  description: 'Polly API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Polly API
  slug: polly-ai-api
artifact_total: 12
common:
- group: auth
  href: https://artifacts.apis.io/polly-ai/well-known/polly-ai-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/polly-ai-status-security.txt
- group: commercial
  href: https://artifacts.apis.io/polly-ai/plans/polly-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/polly-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/polly-ai/rules/polly-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/polly-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/polly-ai/json-ld/polly-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/polly-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/polly-ai/vocabulary/polly-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/polly-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/polly-ai/data-model/polly-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/polly-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.polly.ai/security
- group: design
  href: https://artifacts.apis.io/polly-ai/conformance/polly-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/polly-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/polly-ai/well-known/polly-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/polly-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/polly-ai/hosts/polly-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/polly-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/polly-ai/vendors/polly-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/polly-ai-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.polly.ai/help/slack/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.polly.ai/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.polly.ai/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.polly.ai/
- group: auth
  title: ''
  type: Security
  url: https://www.polly.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polly.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.polly.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.polly.ai/
- group: auth
  href: https://artifacts.apis.io/polly-ai/security/polly-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/polly-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/polly-ai/security/polly-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/polly-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://polly.ai
created: '2026-10-21'
description: Polly offers a participation platform that enables teams to run polls, surveys, pulse checks, quizzes, Q&A, and live interactive experiences directly within collaboration tools such as Slack, Microsoft Teams, Google Chat, and Zoom. It serves HR, People Ops, internal communications, L&D, product, and IT teams by providing ready‑to‑go templates and integrations for employee feedback, onboarding, meetings, and engagement programs.
image: https://f.hubspotusercontent00.net/hubfs/5957403/OG%20Fallback.jpg
json_schemas:
- name: PostPollsCreateRequest
  property_count: 12
  slug: polly-ai-post-polls-create-request
- name: PostSurveysCreateRequest
  property_count: 12
  slug: polly-ai-post-surveys-create-request
- name: PostSurveysCreateResponse
  property_count: 5
  slug: polly-ai-post-surveys-create-response
- name: PostSurveysListResponse
  property_count: 5
  slug: polly-ai-post-surveys-list-response
- name: PostWorkflowsResultsResponse
  property_count: 5
  slug: polly-ai-post-workflows-results-response
- name: PostWorkflowsTriggerResponse
  property_count: 5
  slug: polly-ai-post-workflows-trigger-response
jsonld:
- class_count: 20
  name: Polly Ai Context
  property_count: 25
  slug: polly-ai-context
layout: provider
modified: '2026-10-21'
name: Polly
nav: Providers
network: true
overview: 'Polly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Employee Engagement, Surveys, Polls, Internal Communications, and Learning and Development.


  The Polly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Polly''s developer surface includes support, engineering blog, documentation, and 19 more developer resources.'
plans:
- name: Polly Ai Plans Pricing
  plan_count: 5
  slug: polly-ai-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Polly API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: polly-ai-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 24.5
    developer_ergonomics: 8.3
    discoverability: 66.1
    operational_transparency: 17.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.4
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
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/polly-ai/polly-ai-2026-11-03T141349.png
security:
- kind: domain-security
  name: Polly Ai Domain Security
  slug: polly-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Polly Ai Trust Center
  slug: polly-ai-trust-center
  summary_line: SOC 2, GDPR
slug: polly-ai
tags:
- Employee Engagement
- Surveys
- Polls
- Internal Communications
- Learning and Development
- Meetings
- HR Tools
- Integration
website: https://polly.ai
---
