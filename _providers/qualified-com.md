---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.9
  scored_at: '2026-10-04'
api_count: 1
apis:
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: (Legacy) A visitor's conversations with a bot, in a self-contained shape. Superseded by the Conversations and Messages endpoints, which are recommended for new integrations, and remains fully supporte
  name: Qualified Bot Conversations API
  phrasing_intents:
  - id: listBotConversations
    intent: List legacy bot conversation transcripts
    question: Where can I still pull chatbot conversation transcripts through the older v1 reporting endpoint?
  phrasing_ops: 1
  slug: qualified-com-bot-conversations-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Submit batches of writes for asynchronous processing.
  name: Qualified Bulk API
  phrasing_intents:
  - id: createBulkJob
    intent: Submit a batch of writes as a bulk job
    question: How do I push hundreds of record updates to Qualified in one asynchronous batch?
  - id: getBulkJob
    intent: Check a bulk job's status and results
    question: Has my bulk job finished processing yet?
  phrasing_ops: 2
  slug: qualified-com-bulk-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Cancel a booked meeting by its Salesforce Event ID.
  name: Qualified Cancel Meeting API
  phrasing_intents:
  - id: cancelMeeting
    intent: Cancel a booked meeting
    question: How do I cancel a meeting a prospect booked through Qualified?
  phrasing_ops: 1
  slug: qualified-com-cancel-meeting-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Create and update accounts by domain. Companies cannot be read back.
  name: Qualified Companies API
  phrasing_intents:
  - id: upsertCompany
    intent: Create or update a company by domain
    question: How do I set account-level values like tier or owner for a whole company domain in Qualified?
  - id: listCompanyFields
    intent: List custom company field definitions
    question: Which account-level custom fields can I set on a company?
  phrasing_ops: 2
  slug: qualified-com-companies-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Engaged chat conversations, meaning the visitor exchanged messages with a rep, bot, or AI assistant.
  name: Qualified Conversations API
  phrasing_intents:
  - id: listConversations
    intent: List engaged website conversations
    question: How do I pull every engaged chat conversation that ended last week?
  - id: getConversation
    intent: Get one conversation by id
    question: Can I look up the details of a single chat conversation by its id?
  - id: listConversationMessages
    intent: List the messages in one conversation
    question: How do I read the full transcript of one specific conversation?
  phrasing_ops: 3
  slug: qualified-com-conversations-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Outbound email activity sent from Qualified, with engagement timestamps.
  name: Qualified Emails API
  phrasing_intents:
  - id: listEmails
    intent: List outbound email activity
    question: How do I see which outbound emails were opened, clicked or bounced recently?
  - id: getEmail
    intent: Get one email activity by id
    question: Can I check the status of a single sent email by its id?
  phrasing_ops: 2
  slug: qualified-com-emails-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Submit GDPR deletion requests by email.
  name: Qualified GDPR API
  phrasing_intents:
  - id: createGdprDeletionRequest
    intent: Request GDPR deletion of people by email
    question: How do I erase people's data from Qualified for a GDPR request?
  phrasing_ops: 1
  slug: qualified-com-gdpr-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Create, update, and read lead (person) records and their custom field values.
  name: Qualified Leads API
  phrasing_intents:
  - id: listLeads
    intent: List known leads
    question: How do I pull all leads that are new or changed since yesterday?
  - id: upsertLead
    intent: Create or update a lead by email
    question: How do I add a new lead or update an existing one in Qualified?
  - id: listLeadFields
    intent: List custom lead field definitions
    question: Which person-level custom fields exist on leads?
  - id: getLead
    intent: Get one lead by id
    question: Can I retrieve a single lead's record using its lead id?
  phrasing_ops: 4
  slug: qualified-com-leads-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Meetings offered or booked with a visitor.
  name: Qualified Meetings API
  phrasing_intents:
  - id: listMeetings
    intent: List booked meetings
    question: How do I pull every meeting booked through Qualified last month?
  - id: getMeeting
    intent: Get one meeting by id
    question: Can I read a meeting's latest details in real time by its id?
  phrasing_ops: 2
  slug: qualified-com-meetings-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Individual messages, either across all conversations or within one.
  name: Qualified Messages API
  phrasing_intents:
  - id: listMessages
    intent: List messages across all conversations
    question: How do I export every chat message across all conversations for a date range?
  - id: getMessage
    intent: Get one chat message by id
    question: Can I fetch a single chat message by its id?
  phrasing_ops: 2
  slug: qualified-com-messages-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: (Legacy) A visitor's conversations with a human rep, in a self-contained shape. Superseded by the Conversations and Messages endpoints, which are recommended for new integrations, and remains fully su
  name: Qualified Rep Conversations API
  phrasing_intents:
  - id: listRepConversations
    intent: List legacy conversations with human reps
    question: How can I export chats visitors had with a live sales rep from the older v1 endpoint?
  phrasing_ops: 1
  slug: qualified-com-rep-conversations-api
- baseURL: https://api.qualified.com
  baseurl_source: declared
  description: Website sessions, with page views and the conversations and meetings that occurred in them.
  name: Qualified Sessions API
  phrasing_intents:
  - id: listSessions
    intent: List website visitor sessions
    question: How do I list website sessions that ended in a given time window?
  - id: getSession
    intent: Get one website session by id
    question: Can I get the latest data for a single website session by id?
  phrasing_ops: 2
  slug: qualified-com-sessions-api
artifact_total: 19
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/capabilities/qualified-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/qualified-com-capability-edges.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/security/qualified-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qualified-com-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/authentication/qualified-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qualified-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.qualified.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.qualified.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://app.qualified.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://app.qualified.com/docs/api
- group: operate
  title: ''
  type: Support
  url: https://university.qualified.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://university.qualified.com/
- group: company
  title: ''
  type: Blog
  url: https://www.qualified.com/plus/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qualified.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.qualified.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qualified.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qualified.com/legal/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.qualified.com/trust
- group: auth
  title: ''
  type: Compliance
  url: https://www.qualified.com/trust
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qualified.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/llms/qualified-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qualified-com-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/scopes/qualified-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/qualified-com-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/conventions/qualified-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qualified-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/errors/qualified-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qualified-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/lifecycle/qualified-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qualified-com-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/lifecycle/qualified-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/qualified-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/conformance/qualified-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qualified-com-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/security/qualified-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qualified-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/security/qualified-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/qualified-com-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/data-model/qualified-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qualified-com-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/overlays/qualified-com-enterprise-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qualified-com-enterprise-api-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/packages/qualified-com-packages.yml
  title: ''
  type: Packages
  url: packages/qualified-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/components/qualified-com-components.yml
  title: ''
  type: Components
  url: components/qualified-com-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/changelog/qualified-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/qualified-com-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/plans/qualified-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qualified-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/rate-limits/qualified-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qualified-com-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: Qualified is a San Francisco based B2B agentic marketing platform built around Piper, an AI SDR agent that engages website visitors in real time with chat, voice, video, email, meeting booking and personalized offers, and works natively alongside Salesforce, HubSpot, Marketo, Eloqua, Outreach, Salesloft, 6sense, Demandbase and Slack. The company publishes the Qualified Enterprise API, a versioned REST contract at api.qualified.com that exposes the underlying records behind the platform — leads, website sessions, conversations, messages, meetings and outbound emails — plus write endpoints for leads and companies, a bulk job endpoint and a GDPR deletion request endpoint, so customers can pipe engagement data into Snowflake, Databricks, BigQuery, Adobe AEP or Eloqua and write enriched records back. The API is bearer-token authenticated with named OAuth-style scopes, cursor paginated, documented for incremental (delta) sync, and is available on the Enterprise and Ultimate plan tiers.
image: https://www.qualified.com/favicon.ico
layout: provider
modified: '2026-08-26'
name: Qualified
nav: Providers
network: true
overview: 'Qualified publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Bot Conversations API, Bulk API, Cancel Meeting API, and 9 more. Tagged areas include Company, Conversational Marketing, Sales, Marketing, and Artificial Intelligence.


  Qualified''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Qualified Com Plans Pricing
  plan_count: 3
  slug: qualified-com-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 4
  name: Qualified Com Rate Limits
  slug: qualified-com-rate-limits
scopes:
- name: Qualified Com Scopes
  scope_count: 11
  slug: qualified-com-scopes
  summary_line: 11 scopes
score:
  band: exemplar
  composite: 66.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 49.3
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 81.6
  previous_composite: 66.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
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
    score: 41.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/qualified-com/refs/heads/main/screenshots/qualified-com-2026-09-02T152601.png
security:
- kind: authentication
  name: Qualified Com Authentication
  slug: qualified-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qualified Com Domain Security
  slug: qualified-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Qualified Com Vulnerability Disclosure
  slug: qualified-com-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Qualified Com Trust Center
  slug: qualified-com-trust-center
  summary_line: SOC 2 Type II, EU-US Privacy Shield
slug: qualified-com
tags:
- Company
- Conversational Marketing
- Sales
- Marketing
- Artificial Intelligence
- AI Agents
- Lead Generation
- Customer Engagement
- Salesforce
- Analytics
website: https://www.qualified.com/
---
