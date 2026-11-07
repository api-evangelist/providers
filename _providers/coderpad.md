---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Coderpad Agentic Access
  operation_count: 47
  slug: coderpad-agentic-access
  summary_line: 47 operations · 18 acting
api_count: 2
apis:
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: Information about the account the API key belongs to.
  name: CoderPad Account API
  slug: coderpad-account-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The Campaigns API from CoderPad — 4 operation(s) for campaigns.
  name: CoderPad Campaigns API
  slug: coderpad-campaigns-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The Me API from CoderPad — 1 operation(s) for me.
  name: CoderPad Me API
  slug: coderpad-me-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: Information about your organization, its users and its usage. Requires an organization account.
  name: CoderPad Organization API
  slug: coderpad-organization-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: The language environments of a pad, including their files.
  name: CoderPad Pad environments API
  slug: coderpad-pad-environments-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: A pad is a live interview or take-home session.
  name: CoderPad Pads API
  slug: coderpad-pads-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: The starter code of a question that can be taken in several languages or project templates. A question with variants has no language of its own; each variant carries one.
  name: CoderPad Question variants API
  slug: coderpad-question-variants-api
- baseURL: https://app.coderpad.io/api
  baseurl_source: declared
  description: Questions from your question bank, which you can use to start pads.
  name: CoderPad Questions API
  slug: coderpad-questions-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The TemporaryFile API from CoderPad — 1 operation(s) for temporaryfile.
  name: CoderPad Temporary File API
  slug: coderpad-temporaryfile-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The Tests API from CoderPad — 8 operation(s) for tests.
  name: CoderPad Tests API
  slug: coderpad-tests-api
- baseURL: https://screen.coderpad.io/assessment/api
  baseurl_source: declared
  description: The Webhook API from CoderPad — 1 operation(s) for webhook.
  name: CoderPad Webhook API
  slug: coderpad-webhook-api
artifact_total: 58
asyncapis:
- description: ''
  name: Coderpad Webhooks
  slug: coderpad-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/coderpad/well-known/coderpad-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coderpad-status-security.txt
- group: agent
  href: https://artifacts.apis.io/coderpad/agentic-access/coderpad-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coderpad-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/coderpad/plans/coderpad-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coderpad-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coderpad/rules/coderpad-rules.yml
  title: ''
  type: Spectral
  url: rules/coderpad-rules.yml
- group: design
  href: https://artifacts.apis.io/coderpad/json-ld/coderpad-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coderpad-context.jsonld
- group: design
  href: https://artifacts.apis.io/coderpad/vocabulary/coderpad-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coderpad-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coderpad/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coderpad/asyncapi/coderpad-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/coderpad-webhooks.yml
- group: design
  href: https://artifacts.apis.io/coderpad/data-model/coderpad-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coderpad-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://coderpad.io/security/
- group: design
  href: https://artifacts.apis.io/coderpad/errors/coderpad-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coderpad-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coderpad/conformance/coderpad-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coderpad-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coderpad/llms/coderpad-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coderpad-llms.txt
- group: auth
  href: https://artifacts.apis.io/coderpad/well-known/coderpad-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coderpad-security.txt
- group: agent
  href: https://artifacts.apis.io/coderpad/well-known/coderpad-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coderpad-well-known.yml
- group: other
  href: https://artifacts.apis.io/coderpad/hosts/coderpad-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coderpad-hosts.yml
- group: other
  href: https://artifacts.apis.io/coderpad/vendors/coderpad-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coderpad-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coderpad.io
- group: auth
  title: ''
  type: Security
  url: https://coderpad.io/security/
- group: start
  title: ''
  type: Sandbox
  url: https://app.coderpad.io/sandbox
- group: company
  title: ''
  type: Newsroom
  url: https://coderpad.io/press/
- group: start
  title: ''
  type: Login
  url: https://app.coderpad.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://coderpad.io/resources/docs/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://coderpad.io/resources/docs/screen/recruiters-quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CoderPad
- group: auth
  href: https://artifacts.apis.io/coderpad/authentication/coderpad-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coderpad-authentication.yml
- group: auth
  href: https://artifacts.apis.io/coderpad/security/coderpad-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/coderpad-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/coderpad/security/coderpad-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coderpad-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coderpad/security/coderpad-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coderpad-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coderpad.io/
- group: docs
  title: ''
  type: Documentation
  url: https://coderpad.io/resources/docs/
- group: company
  title: ''
  type: Blog
  url: https://coderpad.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://coderpad.io/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coderpad.io/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coderpad.io/privacy/
- group: operate
  title: ''
  type: Support
  url: https://coderpad.io/contact/support/
created: '2026-10-27'
description: CoderPad provides an AI‑ready technical assessment platform that enables companies to create, conduct, and evaluate coding interviews and screening tests. It supports real‑time collaborative coding, AI‑assisted candidate assistance, and integrates with hiring workflows. The service offers features such as interview templates, automated scoring, and detailed analytics to help technical hiring teams evaluate candidates efficiently and fairly across all stages of the hiring process.
image: https://coderpad.io/wp-content/uploads/2024/01/coderpad-hire-better-candidates-faster-opengraph-image.png
json_schemas:
- name: ai_assist_conversations
  property_count: 1
  slug: coderpad-ai-assist-conversations
- name: CampaignDetails
  property_count: 5
  slug: coderpad-campaign-details
- name: CampaignInsightsResult
  property_count: 6
  slug: coderpad-campaign-insights-result
- name: campaigns_page
  property_count: 2
  slug: coderpad-campaigns-page
- name: CampaignsResult
  property_count: 5
  slug: coderpad-campaigns-result
- name: CreateCampaignRequest
  property_count: 4
  slug: coderpad-create-campaign-request
- name: detailed_result
  property_count: 19
  slug: coderpad-detailed-result
- name: me
  property_count: 3
  slug: coderpad-me
- name: Ok
  property_count: 1
  slug: coderpad-ok
- name: OrganizationResponse
  property_count: 10
  slug: coderpad-organization-response
- name: OrganizationStatsResponse
  property_count: 5
  slug: coderpad-organization-stats-response
- name: PadCreateRequest
  property_count: 15
  slug: coderpad-pad-create-request
- name: PadEnvironment
  property_count: 8
  slug: coderpad-pad-environment
- name: PadEvent
  property_count: 6
  slug: coderpad-pad-event
- name: PadResponse
  property_count: 32
  slug: coderpad-pad-response
- name: Pad
  property_count: 26
  slug: coderpad-pad
- name: PadUpdateRequest
  property_count: 11
  slug: coderpad-pad-update-request
- name: PaginatedResponse
  property_count: 4
  slug: coderpad-paginated-response
- name: playback_events
  property_count: 1
  slug: coderpad-playback-events
- name: QuestionDetailsResult
  property_count: 26
  slug: coderpad-question-details-result
- name: QuestionInsightsResult
  property_count: 5
  slug: coderpad-question-insights-result
- name: QuestionList
  property_count: 5
  slug: coderpad-question-list
- name: QuestionMultipartRequest
  property_count: 6
  slug: coderpad-question-multipart-request
- name: QuestionVariantResponse
  property_count: 12
  slug: coderpad-question-variant-response
- name: QuestionVariant
  property_count: 11
  slug: coderpad-question-variant
- name: QuestionVariantWriteRequest
  property_count: 4
  slug: coderpad-question-variant-write-request
- name: QuestionWriteRequest
  property_count: 10
  slug: coderpad-question-write-request
- name: questions_page
  property_count: 2
  slug: coderpad-questions-page
- name: QuotaResponse
  property_count: 8
  slug: coderpad-quota-response
- name: result_page
  property_count: 2
  slug: coderpad-result-page
- name: SaveQuestionRequest
  property_count: 18
  slug: coderpad-save-question-request
- name: SendParameters
  property_count: 7
  slug: coderpad-send-parameters
- name: Team
  property_count: 2
  slug: coderpad-team
- name: TemporaryFileResult
  property_count: 1
  slug: coderpad-temporary-file-result
- name: webhook
  property_count: 1
  slug: coderpad-webhook
jsonld:
- class_count: 120
  name: Coderpad Context
  property_count: 317
  slug: coderpad-context
layout: provider
modified: '2026-10-27'
name: CoderPad
nav: Providers
network: true
overview: 'CoderPad publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Campaigns API, Me API, and 8 more. Tagged areas include Company, Artificial Intelligence, Hiring, Technical Assessment, and InterviewPlatform.


  The CoderPad catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CoderPad''s developer surface includes sandbox, changelog, getting-started guide, authentication, documentation, engineering blog, pricing, and 29 more developer resources.'
plans:
- name: Coderpad Plans Pricing
  plan_count: 7
  slug: coderpad-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: CoderPad API Rules
  rule_count: 58
  severity_counts:
    error: 40
    hint: 0
    info: 3
    warn: 15
  slug: coderpad-rules
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 77.5
    developer_ergonomics: 31.5
    discoverability: 65.2
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 64.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: derived
    skills: derived
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
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/coderpad/coderpad-2026-11-03T124727.png
security:
- kind: authentication
  name: Coderpad Authentication
  slug: coderpad-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Coderpad Domain Security
  slug: coderpad-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Coderpad Vulnerability Disclosure
  slug: coderpad-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Coderpad Trust Center
  slug: coderpad-trust-center
  summary_line: SOC 2, GDPR
skill_count: 3
skills:
- name: coderpad-create-and-retrieve-question
  slug: coderpad-create-and-retrieve-question
- name: coderpad-manage-question-variants
  slug: coderpad-manage-question-variants
- name: coderpad-pads-create-and-retrieve
  slug: coderpad-pads-create-and-retrieve
slug: coderpad
tags:
- Company
- Artificial Intelligence
- Hiring
- Technical Assessment
- InterviewPlatform
website: https://coderpad.io/
---
