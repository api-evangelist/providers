---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Zelto Agentic Access
  operation_count: 49
  slug: zelto-agentic-access
  summary_line: 49 operations · 23 acting
api_count: 1
apis:
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: The Action checks API from Zelto — 1 operation(s) for action checks.
  name: Zelto Action checks API
  slug: zelto-action-checks-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Voice and chat bots normalised through Zelto's ingestion pipeline.
  name: Zelto Agents API
  slug: zelto-agents-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Reviewer routing — group conversations for batched review.
  name: Zelto Buckets API
  slug: zelto-buckets-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Clients or brands your agents work for, and their logos.
  name: Zelto Companies API
  slug: zelto-companies-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Calls, chats, and voicemails — plus their transcripts and recordings.
  name: Zelto Conversations API
  slug: zelto-conversations-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Customer-provided evaluations attached to a call (requires metrics enabled).
  name: Zelto Customer Metrics API
  slug: zelto-customer-metrics-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Prospective measurement of two externally routed prompt versions across independent monitor outcomes.
  name: Zelto Experiments API
  slug: zelto-experiments-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Structured issues discovered during analysis, with optional conversation attachments and comments.
  name: Zelto Findings API
  slug: zelto-findings-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Headless org provisioning. Requires an admin/service API key (not a read-only org-scoped customer key).
  name: Zelto Organizations API
  slug: zelto-organizations-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: The Reports API from Zelto — 3 operation(s) for reports.
  name: Zelto Reports API
  slug: zelto-reports-api
- baseURL: https://api.zelto.ai
  baseurl_source: declared
  description: Human review state for conversations.
  name: Zelto Reviews API
  slug: zelto-reviews-api
artifact_total: 27
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.zelto.ai/docs/plans
- group: other
  href: https://artifacts.apis.io/zelto/capabilities/zelto-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zelto-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/zelto/agentic-access/zelto-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zelto-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/zelto/rules/zelto-rules.yml
  title: ''
  type: Spectral
  url: rules/zelto-rules.yml
- group: design
  href: https://artifacts.apis.io/zelto/json-ld/zelto-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zelto-context.jsonld
- group: design
  href: https://artifacts.apis.io/zelto/vocabulary/zelto-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zelto-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/zelto/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/zelto/data-model/zelto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zelto-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.inc/zelto
- group: design
  href: https://artifacts.apis.io/zelto/errors/zelto-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zelto-problem-types.yml
- group: design
  href: https://artifacts.apis.io/zelto/conformance/zelto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zelto-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zelto/llms/zelto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zelto-llms.txt
- group: other
  href: https://artifacts.apis.io/zelto/a2a/zelto-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/zelto-a2a.yml
- group: auth
  href: https://artifacts.apis.io/zelto/well-known/zelto-dashboard-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zelto-dashboard-security.txt
- group: auth
  href: https://artifacts.apis.io/zelto/well-known/zelto-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zelto-api-security.txt
- group: agent
  href: https://artifacts.apis.io/zelto/well-known/zelto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zelto-well-known.yml
- group: other
  href: https://artifacts.apis.io/zelto/hosts/zelto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zelto-hosts.yml
- group: other
  href: https://artifacts.apis.io/zelto/vendors/zelto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zelto-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://api.zelto.ai/signup
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zelto.ai/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/zelto/authentication/zelto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zelto-authentication.yml
- group: auth
  href: https://artifacts.apis.io/zelto/security/zelto-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zelto-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/zelto/security/zelto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zelto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zelto.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zelto.ai/api-reference
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zelto.ai/api-reference
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zelto.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zelto.ai/terms
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://docs.zelto.ai/mcp
  - status: null
    url: https://api.zelto.ai/openapi.json
  - status: null
    url: https://dashboard.zelto.ai/openapi.json
  - status: 401
    url: https://api.zelto.ai/mcp
  - status: 401
    url: https://dashboard.zelto.ai/mcp
  - status: 403
    url: https://trust.zelto.ai/mcp
  reason: partner-login
  state: gated
created: '2026-10-15'
description: Zelto AI provides production QA for voice AI agents, offering analytics and monitoring of conversational pipelines. It ingests calls, transcripts, messages, and LLM traces to surface failures, rank findings, and draft fixes, helping teams improve conversion and reliability at scale. The platform integrates with major voice AI services and offers a dashboard for debugging, testing, and continuous improvement.
image: https://zelto.ai/opengraph-image?4d5829a62bee824e
json_schemas:
- name: ActionCheckInput
  property_count: 5
  slug: zelto-action-check-input
- name: CallIngest
  property_count: 9
  slug: zelto-call-ingest
- name: CustomerMetric
  property_count: 13
  slug: zelto-customer-metric
- name: CustomerTransferReport
  property_count: 5
  slug: zelto-customer-transfer-report
- name: ExperimentCreate
  property_count: 16
  slug: zelto-experiment-create
- name: Finding
  property_count: 10
  slug: zelto-finding
jsonld:
- class_count: 21
  name: Zelto Context
  property_count: 93
  slug: zelto-context
layout: provider
modified: '2026-10-15'
name: Zelto
nav: Providers
network: true
overview: 'Zelto publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Action checks API, Agents API, Buckets API, and 8 more. Tagged areas include Company, Voice AI, QA, Production, and Analytics.


  The Zelto catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zelto''s developer surface includes pricing, signup flow, getting-started guide, authentication, documentation, API reference, and 22 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Zelto API Rules
  rule_count: 56
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 6
  slug: zelto-rules
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 39.5
    contract_governance: 35.6
    contract_quality: 62.5
    developer_ergonomics: 28.0
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 66.7
screenshot: https://apis.io/screenshots/zelto/zelto-2026-11-03T150443.png
security:
- kind: authentication
  name: Zelto Authentication
  slug: zelto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zelto Domain Security
  slug: zelto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Zelto Trust Center
  slug: zelto-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 4
skills:
- name: zelto-create-finding-with-conversation
  slug: zelto-create-finding-with-conversation
- name: zelto-fetch-conversation-transcript
  slug: zelto-fetch-conversation-transcript
- name: zelto-launch-experiment
  slug: zelto-launch-experiment
- name: zelto-list-and-get-agent
  slug: zelto-list-and-get-agent
slug: zelto
tags:
- Company
- Voice AI
- QA
- Production
- Analytics
- Monitoring
website: https://zelto.ai
---
