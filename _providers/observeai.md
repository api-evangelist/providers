---
access_model:
  confidence: high
  label: Sales-gated
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://api-docs.observe.ai/#tag/Authentication
  - https://api-docs.observe.ai/#tag/ReportingService-Overview
  - https://aws.amazon.com/marketplace/pp/prodview-q2xrm5ud6rkro
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://kong.observe.ai/
  baseurl_source: declared
  description: Ack Dispute API can be used to pull all evaluation related data which are sent for acknowledgment or dispute. Please note - <ol> <li>Allow 24 hrs to pass before pulling Ack Dispute Data. ie., For Eval
  name: Observe.AI Ack Dispute Flow API
  slug: observeai-ack-dispute-flow-api
- baseURL: https://kong.observe.ai/
  baseurl_source: declared
  description: 'OAuth 2.0, which stands for “Open Authorization”, is a standard design to allow a website or application to access resources hosted by other web apps on behalf of a user <b>Note</b>: If you have been '
  name: Observe.AI Authentication API
  slug: observeai-authentication-api
- baseURL: https://kong.observe.ai/
  baseurl_source: declared
  description: Coachings API can be used to pull all the Coaching sessions done on Observe AI platform. Please note - <ol> <li>Allow 24 hrs to pass before pulling Coaching sessions. ie., For Coaching sessions comple
  name: Observe.AI Coachings API
  slug: observeai-coachings-api
- baseURL: https://kong.observe.ai/
  baseurl_source: declared
  description: DSR (Data Subject Request) deletion APIs allow customers to submit metadata-based deletion requests and check the processing status of those requests. <h3>Authentication</h3> OAuth 2.0 Bearer Token is
  name: Observe.AI DSR API
  slug: observeai-dsr-api
- baseURL: https://kong.observe.ai/
  baseurl_source: declared
  description: Evaluations API can be used to pull all the Evaluations(Manual and Auto QA) done on Observe AI platform. Please note - <ol> <li>Allow 24 hrs to pass before pulling Evaluations. ie., For Evaluations co
  name: Observe.AI Evaluations API
  slug: observeai-evaluations-api
- baseURL: https://kong.observe.ai/
  baseurl_source: declared
  description: Interactions API is an omnichannel API can be used to obtain all the data related to the interactions like Moments, Transcripts and metadata related to Interactions(including Voice calls and Web chat)
  name: Observe.AI Interactions API
  slug: observeai-interactions-api
- baseURL: https://kong.observe.ai/
  baseurl_source: declared
  description: Summarization AI API can be used to pull the data related to summaries for a particular interaction including calls and chats. Please note - <ol> <li> Summaries can only be extracted if they are avail
  name: Observe.AI Summary API
  slug: observeai-summary-api
artifact_total: 29
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/observeai-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/observeai-reporting-apis-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.observe.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.observe.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://help.observe.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.observe.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.observe.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/observeai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.observe.ai/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/observeai-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/observeai-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.observe.ai/trust
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/observeai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.observe.ai/contact-center-security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/observeai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.observe.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.observe.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.observe.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.observe.ai/#tag/ReportingService-Overview
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/observeai-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://api-docs.observe.ai/#tag/CallsReportVsInteractions
- group: auth
  title: ''
  type: Authentication
  url: authentication/observeai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/observeai-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/observeai-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/observeai-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/observeai-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/observeai-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/observeai-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-q2xrm5ud6rkro
- group: start
  title: ''
  type: SignUp
  url: https://app.observe.ai/login
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/observeai-llms.txt
created: '2026-07-17'
description: Observe.AI is an agentic AI platform for the contact center, providing purpose-built AI agents that handle customer support end-to-end across voice and chat, real-time AI Copilot guidance that assists frontline agents during live interactions, and Conversation Intelligence that evaluates every interaction for quality assurance, compliance, and business insight. Its AI agents connect to CRM, CCaaS, knowledge base, and backend systems to read and write data and trigger workflows, backed by 250+ prebuilt integrations and API/integration toolkits. Observe.AI serves regulated industries including banking and financial services, healthcare, insurance, and travel and hospitality, and maintains SOC 2, ISO 27001, and HIPAA compliance. Its public developer surface is the Reporting APIs at api-docs.observe.ai — an OpenAPI 3.0.1 contract covering asynchronous export of interactions, GenAI summaries, Auto QA and manual evaluations, coachings and ack/dispute state, plus a Data Subject Request
  deletion API and a scheduled bulk export to Snowflake or S3 described by sixteen JSON Schemas. The company was added to the API Evangelist network as a portfolio company of Scale Venture Partners and the SoftBank Vision Fund.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/observeai.png
json_schemas:
- name: AGENT_PERFORMANCE_ASSIGNMENT_V1
  property_count: 16
  slug: observeai-bulk-export-agent-performance-assignment-v1.schema
- name: AUDIT_ASSIGNMENT_V1
  property_count: 18
  slug: observeai-bulk-export-audit-assignment-v1.schema
- name: AUTOQA_ACK_DISPUTE_V1
  property_count: 6
  slug: observeai-bulk-export-autoqa-ack-dispute-v1.schema
- name: AUTOQA_EVALUATION_V1
  property_count: 27
  slug: observeai-bulk-export-autoqa-evaluation-v1.schema
- name: CALIBRATION_ASSIGNMENT_V1
  property_count: 29
  slug: observeai-bulk-export-calibration-assignment-v1.schema
- name: COACHING_V1
  property_count: 25
  slug: observeai-bulk-export-coaching-v1.schema
- name: CONTACT_REASON_V1
  property_count: 4
  slug: observeai-bulk-export-contact-reason-v1.schema
- name: EVALUATION_TEMPLATE_V1
  property_count: 5
  slug: observeai-bulk-export-evaluation-template-v1.schema
- name: INTERACTION_SUMMARY_V1
  property_count: 5
  slug: observeai-bulk-export-interaction-summary-v1.schema
- name: INTERACTION_V1
  property_count: 20
  slug: observeai-bulk-export-interaction-v1.schema
- name: MANUAL_ACK_DISPUTE_V1
  property_count: 6
  slug: observeai-bulk-export-manual-ack-dispute-v1.schema
- name: MANUAL_EVALUATION_V1
  property_count: 29
  slug: observeai-bulk-export-manual-evaluation-v1.schema
- name: SENTIMENT_METRIC_V1
  property_count: 5
  slug: observeai-bulk-export-sentiment-metric-v1.schema
- name: TEAM_V1
  property_count: 4
  slug: observeai-bulk-export-team-v1.schema
- name: USER_LOGIN_ACTIVITY_V1
  property_count: 13
  slug: observeai-bulk-export-user-login-activity-v1.schema
- name: USER_V1
  property_count: 8
  slug: observeai-bulk-export-user-v1.schema
layout: provider
modified: '2026-08-14'
name: Observe.AI
nav: Providers
network: true
overview: 'Observe.AI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Ack Dispute Flow API, Authentication API, Coachings API, and 4 more. Tagged areas include Company, Ai Apps, Contact Center, Conversation Intelligence, and Customer-Support.


  Observe.AI''s developer surface includes engineering blog, support, documentation, API reference, getting-started guide, changelog, authentication, and 25 more developer resources.'
plans:
- name: Observeai Plans Pricing
  plan_count: 1
  slug: observeai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Observeai Rate Limits
  slug: observeai-rate-limits
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 67.0
    catalog_earned_first_party: 20.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 51.3
    developer_ergonomics: 48.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 80.3
  previous_composite: 53.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/observeai/refs/heads/main/screenshots/observeai-2026-08-07T185911.png
security:
- kind: authentication
  name: Observeai Authentication
  slug: observeai-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Observeai Domain Security
  slug: observeai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Observeai Vulnerability Disclosure
  slug: observeai-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Observeai Trust Center
  slug: observeai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: observeai
tags:
- Company
- Ai Apps
- Contact Center
- Conversation Intelligence
- Customer-Support
- Agentic AI
- Voice AI
- Quality Assurance
- Reporting
- OpenAPI
- Speech Analytics
website: https://www.observe.ai/
---
