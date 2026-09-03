---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 41
  human_in_the_loop: 3
  name: Assembled Agentic Access
  operation_count: 70
  slug: assembled-agentic-access
  summary_line: 70 operations · 41 acting · 3 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Manage agents (people) in the Assembled workforce. List, retrieve, create, and update agents along with their roles, channels, skills, and team assignments. The People API is the entry point for synci
  name: Assembled People API
  slug: assembled-people-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Read and write real-time agent state used to drive adherence reporting, live dashboards, and dynamic routing. Supports bulk state ingestion from upstream telephony and CRM platforms, a condensed non-o
  name: Assembled Agent State API
  slug: assembled-agent-state-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: 'Create, list, and delete activities — the scheduled shifts, breaks, time off, training, and meetings that make up an agent''s calendar. Includes bulk creation, soft-delete semantics, and management of '
  name: Assembled Activities API
  slug: assembled-activities-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Retrieve Assembled's ML-generated forecasts, forecast totals, manual adjustments, and detected outliers. The forecasted-vs-actuals endpoint compares predicted to realised volume so support leaders can
  name: Assembled Forecasts API
  slug: assembled-forecasts-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Programmatically create, list, and cancel time-off requests, and pull a stream of time-off updates for downstream HRIS or payroll synchronisation. The endpoint underpins the automated time-off and shi
  name: Assembled Time Off API
  slug: assembled-time-off-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Create and list staffing requirements that express how many agents are needed by queue, site, team, or skill across time intervals. Requirement types describe the family of need (for example, headcoun
  name: Assembled Requirements API
  slug: assembled-requirements-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Bulk-ingest and bulk-update customer conversation records — phone, email, chat, SMS, social, and back-office — so they can be associated with agents, queues, and channels for reporting, QA, and analyt
  name: Assembled Conversations API
  slug: assembled-conversations-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Asynchronously generate and retrieve structured reports including adherence, ticket statistics, and handle times. Reports are kicked off with a POST /v0/reports/:reportType call and polled via GET /v0
  name: Assembled Reports API
  slug: assembled-reports-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Types/categories of activity
  name: Assembled Activity Types API
  slug: assembled-activity-types-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Map platform IDs to Assembled people
  name: Assembled Agent Associations API
  slug: assembled-agent-associations-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Assist Articles API from Assembled — 2 operation(s) for assist articles.
  name: Assembled Assist Articles API
  slug: assembled-assist-articles-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Assist Conversations API from Assembled — 2 operation(s) for assist conversations.
  name: Assembled Assist Conversations API
  slug: assembled-assist-conversations-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Assist Replies API from Assembled — 1 operation(s) for assist replies.
  name: Assembled Assist Replies API
  slug: assembled-assist-replies-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Assist Responses API from Assembled — 2 operation(s) for assist responses.
  name: Assembled Assist Responses API
  slug: assembled-assist-responses-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Audit trail of schedule modifications
  name: Assembled Event Changes API
  slug: assembled-event-changes-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Forecast Adjustments API from Assembled — 3 operation(s) for forecast adjustments.
  name: Assembled Forecast Adjustments API
  slug: assembled-forecast-adjustments-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Forecast Outliers API from Assembled — 3 operation(s) for forecast outliers.
  name: Assembled Forecast Outliers API
  slug: assembled-forecast-outliers-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Forecast Totals API from Assembled — 2 operation(s) for forecast totals.
  name: Assembled Forecast Totals API
  slug: assembled-forecast-totals-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Forecasts Vs Actuals API from Assembled — 1 operation(s) for forecasts vs actuals.
  name: Assembled Forecasts Vs Actuals API
  slug: assembled-forecasts-vs-actuals-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Quality Assurance API from Assembled — 1 operation(s) for quality assurance.
  name: Assembled Quality Assurance API
  slug: assembled-quality-assurance-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Queues API from Assembled — 2 operation(s) for queues.
  name: Assembled Queues API
  slug: assembled-queues-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Requirement Types API from Assembled — 1 operation(s) for requirement types.
  name: Assembled Requirement Types API
  slug: assembled-requirement-types-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: Available roles that can be assigned to people
  name: Assembled Roles API
  slug: assembled-roles-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Sites API from Assembled — 2 operation(s) for sites.
  name: Assembled Sites API
  slug: assembled-sites-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Skills API from Assembled — 2 operation(s) for skills.
  name: Assembled Skills API
  slug: assembled-skills-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Teams API from Assembled — 2 operation(s) for teams.
  name: Assembled Teams API
  slug: assembled-teams-api
- baseURL: https://api.assembledhq.com
  baseurl_source: spec
  description: The Working Hours API from Assembled — 2 operation(s) for working hours.
  name: Assembled Working Hours API
  slug: assembled-working-hours-api
arazzos:
- description: Find an agent in the workforce, read their full profile, then patch their attributes.
  name: Assembled Update an Agent Profile
  slug: assembled-agent-profile-update-workflow
- description: Confirm an agent exists, map upstream platform identifiers to them, then read back the linked record.
  name: Assembled Associate Platform IDs to an Agent
  slug: assembled-associate-agent-platforms-workflow
- description: List the activities scheduled in a window, then pull the audit trail of changes to them.
  name: Assembled Audit Schedule Changes
  slug: assembled-audit-schedule-changes-workflow
- description: List pending time-off requests and cancel the first one, branching on whether any exist.
  name: Assembled Review and Cancel a Time Off Request
  slug: assembled-cancel-time-off-workflow
- description: Read the volume forecast for a window, resolve a requirement type, then create a staffing requirement.
  name: Assembled Turn a Forecast into a Staffing Requirement
  slug: assembled-forecast-to-requirement-workflow
- description: Start an async report job, then fetch the result, branching on completion status.
  name: Assembled Generate and Retrieve a Report
  slug: assembled-generate-report-workflow
- description: Bulk-upsert customer conversation records, then bulk-update them with enriched fields.
  name: Assembled Ingest and Enrich Conversations
  slug: assembled-ingest-conversations-workflow
- description: Create a forecast total for a queue window, list totals to find it, then fetch it in full.
  name: Assembled Create and Read a Forecast Total
  slug: assembled-manage-forecast-total-workflow
- description: Resolve an available role, create a new agent, then read back the created record.
  name: Assembled Provision a New Agent
  slug: assembled-provision-agent-workflow
- description: Create a routing queue, pick an active agent, then schedule an activity routed to that queue.
  name: Assembled Provision a Queue and Staff It
  slug: assembled-provision-queue-and-staff-workflow
- description: Confirm the agent exists, create a time-off request, then verify it in the request list.
  name: Assembled Request Time Off for an Agent
  slug: assembled-request-time-off-workflow
- description: List the working-hours rules for an agent, then fetch the first rule in full.
  name: Assembled Review an Agent's Working Hours
  slug: assembled-review-working-hours-workflow
- description: Resolve an activity type, create a scheduled activity, then list it back on the calendar.
  name: Assembled Schedule an Agent Shift
  slug: assembled-schedule-agent-shift-workflow
- description: Pick an active agent from the workforce, then schedule a shift activity for them.
  name: Assembled Staff a Shift for a Workforce Agent
  slug: assembled-staff-agent-shift-workflow
- description: Confirm an agent exists, push a batch of state records, then read back the condensed timeline.
  name: Assembled Stream and Verify Agent State
  slug: assembled-stream-agent-state-workflow
artifact_total: 126
collections:
- collection_type: postman
  name: Assembled Activities API
  slug: postman-assembled-activities-api
- collection_type: postman
  name: Assembled Agent State API
  slug: postman-assembled-agent-state-api
- collection_type: postman
  name: Assembled Assist API
  slug: postman-assembled-assist-api
- collection_type: postman
  name: Assembled Conversations API
  slug: postman-assembled-conversations-api
- collection_type: postman
  name: Assembled Filters API
  slug: postman-assembled-filters-api
- collection_type: postman
  name: Assembled Forecasts API
  slug: postman-assembled-forecasts-api
- collection_type: postman
  name: Assembled People API
  slug: postman-assembled-people-api
- collection_type: postman
  name: Assembled QA API
  slug: postman-assembled-qa-api
- collection_type: postman
  name: Assembled Reports API
  slug: postman-assembled-reports-api
- collection_type: postman
  name: Assembled Requirements API
  slug: postman-assembled-requirements-api
- collection_type: postman
  name: Assembled Scheduling Rules API
  slug: postman-assembled-scheduling-rules-api
- collection_type: postman
  name: Assembled Time Off API
  slug: postman-assembled-time-off-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Assembled Activities API
  slug: open-assembled-activities-api
- collection_type: open
  name: Assembled Activities Activity Types API
  slug: open-assembled-activity-types-api
- collection_type: open
  name: Assembled Activities Agent Associations API
  slug: open-assembled-agent-associations-api
- collection_type: open
  name: Assembled Activities Agent State API
  slug: open-assembled-agent-state-api
- collection_type: open
  name: Assembled Assist API
  slug: open-assembled-assist-api
- collection_type: open
  name: Assembled Activities Assist Articles API
  slug: open-assembled-assist-articles-api
- collection_type: open
  name: Assembled Activities Assist Conversations API
  slug: open-assembled-assist-conversations-api
- collection_type: open
  name: Assembled Activities Assist Replies API
  slug: open-assembled-assist-replies-api
- collection_type: open
  name: Assembled Activities Assist Responses API
  slug: open-assembled-assist-responses-api
- collection_type: open
  name: Assembled Activities Conversations API
  slug: open-assembled-conversations-api
- collection_type: open
  name: Assembled Activities Event Changes API
  slug: open-assembled-event-changes-api
- collection_type: open
  name: Assembled Filters API
  slug: open-assembled-filters-api
- collection_type: open
  name: Assembled Activities Forecast Adjustments API
  slug: open-assembled-forecast-adjustments-api
- collection_type: open
  name: Assembled Activities Forecast Outliers API
  slug: open-assembled-forecast-outliers-api
- collection_type: open
  name: Assembled Activities Forecast Totals API
  slug: open-assembled-forecast-totals-api
- collection_type: open
  name: Assembled Activities Forecasts API
  slug: open-assembled-forecasts-api
- collection_type: open
  name: Assembled Activities Forecasts Vs Actuals API
  slug: open-assembled-forecasts-vs-actuals-api
- collection_type: open
  name: Assembled Activities People API
  slug: open-assembled-people-api
- collection_type: open
  name: Assembled QA API
  slug: open-assembled-qa-api
- collection_type: open
  name: Assembled Activities Quality Assurance API
  slug: open-assembled-quality-assurance-api
- collection_type: open
  name: Assembled Activities Queues API
  slug: open-assembled-queues-api
- collection_type: open
  name: Assembled Activities Reports API
  slug: open-assembled-reports-api
- collection_type: open
  name: Assembled Activities Requirement Types API
  slug: open-assembled-requirement-types-api
- collection_type: open
  name: Assembled Activities Requirements API
  slug: open-assembled-requirements-api
- collection_type: open
  name: Assembled Activities Roles API
  slug: open-assembled-roles-api
- collection_type: open
  name: Assembled Scheduling Rules API
  slug: open-assembled-scheduling-rules-api
- collection_type: open
  name: Assembled Activities Sites API
  slug: open-assembled-sites-api
- collection_type: open
  name: Assembled Activities Skills API
  slug: open-assembled-skills-api
- collection_type: open
  name: Assembled Activities Teams API
  slug: open-assembled-teams-api
- collection_type: open
  name: Assembled Activities Time Off API
  slug: open-assembled-time-off-api
- collection_type: open
  name: Assembled Activities Working Hours API
  slug: open-assembled-working-hours-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/assembled-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/assembled-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/assembled-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/assembled-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/assembled-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/assembled-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/assembled/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-agent-profile-update-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-associate-agent-platforms-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-audit-schedule-changes-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-cancel-time-off-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-forecast-to-requirement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-generate-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-ingest-conversations-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-manage-forecast-total-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-provision-agent-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-provision-queue-and-staff-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-request-time-off-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-review-working-hours-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-schedule-agent-shift-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-staff-agent-shift-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/assembled-stream-agent-state-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.assembled.com
- group: start
  title: ''
  type: Portal
  url: https://docs.assembled.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.assembled.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.assembled.com/
- group: start
  title: ''
  type: Signup
  url: https://app.assembledhq.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.assembledhq.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.assembled.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/assembled-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/assembled-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/assembled-finops.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.assembled.com
- group: company
  title: ''
  type: Blog
  url: https://www.assembled.com/blog
- group: other
  title: ''
  type: Customers
  url: https://www.assembled.com/customers
- group: company
  title: ''
  type: About
  url: https://www.assembled.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.assembled.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.assembled.com/contact
- group: operate
  title: ''
  type: Support
  url: https://support.assembled.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.assembled.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.assembled.com/terms
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.assembled.com
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.assembled.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/assembledhq
- group: build
  title: ''
  type: SDKs
  url: https://github.com/assembledhq/assembled-chat-ios-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/assembledhq/assembled-chat-android-sdk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/assembledhq
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/assembledhq
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@assembledhq
- group: other
  title: ''
  type: AppExchange
  url: https://appexchange.salesforce.com/appxListingDetail?listingId=22604eaa-c6cf-4357-bec0-297e4236345f
- group: other
  title: ''
  type: Product
  url: https://www.assembled.com/products/workforce-management
- group: other
  title: ''
  type: Product
  url: https://www.assembled.com/products/ai-agents
- group: other
  title: ''
  type: Product
  url: https://www.assembled.com/products/ai-copilot
- group: other
  title: ''
  type: Product
  url: https://www.assembled.com/products/vendor-management
- group: design
  title: ''
  type: JSONLD
  url: json-ld/assembled-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/assembled-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/assembled-rules.yml
created: '2026-05-24'
description: Assembled is a San Francisco-headquartered support operations platform that unifies workforce management (WFM), AI agents, and AI Copilot for modern customer support teams. Founded in 2020 by former Stripe operations engineers, Assembled lets support leaders plan, schedule, and orchestrate a hybrid workforce of in-house agents, BPO vendors, and AI agents from a single system. The platform delivers ML-based volume forecasting, automated schedule generation, real-time adherence, time-off and shift-swap automation, vendor capacity planning, multichannel routing, and structured reporting across phone, email, chat, SMS, social, and back-office channels. Its AI surface includes autonomous AI Agents that resolve customer conversations end-to-end across chat, email, SMS, and voice, plus AI Copilot, which drafts replies, translates in real time, and surfaces knowledge for human agents. The Assembled REST API (api.assembledhq.com/v0) exposes people, queues, sites, teams, skills, activities,
  agent states, forecasts, time-off requests, requirements, working hours, QA scores, structured reports, and the Assist endpoints for AI chat responses and knowledge articles. Assembled is used by Stripe, Etsy, Robinhood, Webflow, Canva, Duolingo, Autodesk, HubSpot, Intercom, and Ramp, and integrates with Zendesk, Salesforce Service Cloud, Intercom, Kustomer, Gladly, Gorgias, Dixa, ServiceNow, Five9, Genesys Cloud, Talkdesk, Amazon Connect, NiCE, UJET, Zoom Contact Center, Slack, Okta, Workday, HiBob, Google Calendar, Shopify, Notion, Confluence, Guru, SharePoint, Fivetran, and quality tools like Klaus, Rippit (MaestroQA), evaluagent, and Observe.AI.
examples:
- key_count: 9
  name: Assembled Assist Response Example
  slug: assembled-assist-response-example
- key_count: 1
  name: Assembled Bulk Agent State Example
  slug: assembled-bulk-agent-state-example
- key_count: 8
  name: Assembled Create Activity Example
  slug: assembled-create-activity-example
- key_count: 1
  name: Assembled Forecasted Vs Actuals Example
  slug: assembled-forecasted-vs-actuals-example
- key_count: 2
  name: Assembled List People Example
  slug: assembled-list-people-example
features:
- ML-based forecasting with >90% accuracy across phone, email, chat, SMS, social, and back-office channels
- AI-powered schedule generation that accounts for both human and AI agent coverage
- Real-time adherence and live performance dashboards with intelligent case routing
- Unified workforce management for in-house agents, BPO vendors, and AI agents
- Automated time-off and shift-swap workflows (Pro and Enterprise)
- Custom API integrations and white-glove onboarding (Enterprise)
- AI Agents — autonomous multichannel resolution across chat, email, SMS, and voice with smart handoffs
- AI Copilot — reply drafting, real-time translation, summarisation, agent guidance, and tone modifiers
- Agentic workflows, escalation rules, custom style guides, and built-in QA tools for AI Agents
- Vendor Management add-on with capacity planning, scheduling integration, coverage heatmaps, and billing reports
- Structured reports for adherence, ticket statistics, and handle times via async report jobs
- Quality assurance score ingestion from Klaus, Rippit (MaestroQA), evaluagent, Observe.AI
- REST API at https://api.assembledhq.com/v0/ with HTTP Basic Auth (sk_live_ API keys)
- Date-based API versioning via the API-Version request header
- Default rate limit of 300 requests per minute (5 req/s) with bursts up to 20
- Bulk operations supported across most write endpoints, plus soft-delete semantics
- Native integrations across CCaaS (Five9, Genesys Cloud, Talkdesk, Amazon Connect, NiCE, UJET, Zoom), CRM/helpdesk (Zendesk, Salesforce, Intercom, Kustomer, Gladly, Gorgias, Dixa, ServiceNow), HRIS (Workday, HiBob), knowledge bases (Notion, Confluence, Guru, SharePoint, Google Drive), Fivetran data pipeline, Slack, Okta, Google Calendar, and Shopify
- Official iOS and Android SDKs for embedding the Assembled chat widget into mobile applications
- SOC 2, GDPR, and HIPAA compliance with enterprise-grade security and policy guardrails
- Scheduling 4.5+ billion events per year for ~100,000 agents across 50+ countries (2025)
finops:
- name: Assembled Finops
  service_category: Customer Support and Workforce Management
  slug: assembled-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/assembled.png
json_schemas:
- name: AssembledActivity
  property_count: 11
  slug: assembled-activity
- name: AssembledAssistResponse
  property_count: 9
  slug: assembled-assist-response
- name: AssembledConversation
  property_count: 16
  slug: assembled-conversation
- name: AssembledPerson
  property_count: 15
  slug: assembled-person
jsonld:
- class_count: 0
  name: Assembled Context
  property_count: 6
  slug: assembled-context
layout: provider
modified: '2026-05-24'
name: Assembled
nav: Providers
network: true
overview: 'Assembled publishes 27 APIs on the [APIs.io](https://apis.io/) network, including People API, Agent State API, Activities API, and 24 more. Tagged areas include Customer-Support, Workforce Management, WFM, AI Agents, and AI Copilot.


  The Assembled catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Assembled''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 50 more developer resources.'
plans:
- name: Assembled Plans Pricing
  plan_count: 6
  slug: assembled-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Assembled Rate Limits
  slug: assembled-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Assembled API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: assembled-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Assembled API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 4
  slug: assembled-rules
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 36.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 28.8
    contract_quality: 61.9
    developer_ergonomics: 61.9
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 50.0
  previous_composite: 55.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/assembled/refs/heads/main/screenshots/assembled-2026-06-20T172502.png
security:
- kind: authentication
  name: Assembled Authentication
  slug: assembled-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Assembled Domain Security
  slug: assembled-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Assembled Vulnerability Disclosure
  slug: assembled-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Assembled Trust Center
  slug: assembled-trust-center
  summary_line: SOC 2, GDPR
slug: assembled
tags:
- Customer-Support
- Workforce Management
- WFM
- AI Agents
- AI Copilot
- Contact Center
- Customer Experience
- Support Operations
- Scheduling
- Forecasting
- Quality Assurance
- Vendor Management
- BPO
website: https://www.assembled.com
---
