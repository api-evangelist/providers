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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.5
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Gotowebinar Agentic Access
  operation_count: 63
  slug: gotowebinar-agentic-access
  summary_line: 63 operations · 25 acting
api_count: 3
apis:
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Read attendees for past webinar sessions.
  name: GoToWebinar Attendees API
  phrasing_intents:
  - id: getAttendees
    intent: List who attended one webinar session
    question: Who actually showed up to a specific session of my GoTo Webinar event?
  - id: getAttendee
    intent: Get one attendee's details for a session
    question: What registration details are kept for a single person who attended a session?
  - id: getAttendeePollAnswers
    intent: Get one attendee's poll answers
    question: How did a particular attendee vote in the polls during a session?
  - id: getAttendeeQuestions
    intent: Get questions one attendee asked in a session
    question: What questions did a specific attendee type in during the webinar session?
  - id: getAttendeeSurveyAnswers
    intent: Get one attendee's survey answers
    question: How did a particular attendee fill out the session survey?
  - id: listAllAttendees
    intent: List attendees across every session of a webinar
    question: Who attended any session of my webinar, across all of its sessions combined?
  phrasing_ops: 6
  slug: gotowebinar-attendees-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Manage co-organizers on a webinar.
  name: GoToWebinar Co-Organizers API
  phrasing_intents:
  - id: getCoorganizers
    intent: List a webinar's co-organizers
    question: Who are the co-organizers on my GoTo Webinar event?
  - id: createCoorganizers
    intent: Add co-organizers to a webinar
    question: How do I add a co-organizer to a webinar I'm running?
  - id: deleteCoorganizer
    intent: Remove a co-organizer from a webinar
    question: How do I take someone off the co-organizer list for a webinar?
  - id: resendCoorganizerInvitation
    intent: Resend a co-organizer's invitation email
    question: A co-organizer never got their invite email, can I send it again?
  phrasing_ops: 4
  slug: gotowebinar-co-organizers-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Manage panelists on a webinar.
  name: GoToWebinar Panelists API
  phrasing_intents:
  - id: getPanelists
    intent: List a webinar's panelists
    question: Who is on the panel for my GoTo Webinar event?
  - id: createPanelists
    intent: Add panelists to a webinar
    question: How do I add guest speakers as panelists to a webinar?
  - id: resendPanelistInvitation
    intent: Resend a panelist's invitation email
    question: A panelist lost their invite, how do I send it to them again?
  - id: deleteWebinarPanelist
    intent: Remove a panelist from a webinar
    question: How do I drop a speaker from a webinar's panel?
  phrasing_ops: 4
  slug: gotowebinar-panelists-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Retrieve poll results from past sessions.
  name: GoToWebinar Polls API
  phrasing_intents:
  - id: getSessionPolls
    intent: Get poll results for a webinar session
    question: What were the poll results from my last GoTo Webinar session?
  phrasing_ops: 1
  slug: gotowebinar-polls-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Retrieve Q&A from past sessions.
  name: GoToWebinar Questions API
  phrasing_intents:
  - id: getSessionQuestions
    intent: Get the Q&A from a webinar session
    question: What questions did the audience ask during my GoTo Webinar session, and how were they answered?
  phrasing_ops: 1
  slug: gotowebinar-questions-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Retrieve webinar recording assets.
  name: GoToWebinar Recordings API
  phrasing_intents:
  - id: listRecordingAssets
    intent: List an organizer's webinar recordings
    question: Which webinar recordings does an organizer have on GoTo Webinar?
  phrasing_ops: 1
  slug: gotowebinar-recordings-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Manage registrants for upcoming webinars.
  name: GoToWebinar Registrants API
  phrasing_intents:
  - id: createRegistrant
    intent: Register someone for a webinar
    question: How do I sign a person up for a webinar and get their join link?
  - id: getAllRegistrantsForWebinar
    intent: List everyone registered for a webinar
    question: Who has signed up for my upcoming GoTo Webinar event?
  - id: deleteRegistrant
    intent: Cancel someone's webinar registration
    question: How do I remove a person from the registration list of an upcoming webinar?
  - id: getRegistrant
    intent: Get one registrant's full registration
    question: What did a specific person fill in when they registered for my webinar?
  - id: getRegistrationFields
    intent: Get a webinar's registration form fields
    question: Which fields and custom questions does my webinar's registration form require?
  phrasing_ops: 5
  slug: gotowebinar-registrants-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Inspect past and live webinar sessions.
  name: GoToWebinar Sessions API
  phrasing_intents:
  - id: getOrganizerSessions
    intent: List an organizer's completed sessions
    question: Which webinar sessions has an organizer completed over the last quarter?
  - id: getAllSessions
    intent: List past sessions of one webinar
    question: How many times has my recurring GoTo Webinar series actually run?
  - id: getWebinarSession
    intent: Get attendance details for an ended session
    question: How many registrants attended a particular session that has ended?
  - id: getPerformance
    intent: Get performance metrics for a session
    question: How well did one specific session of my webinar perform?
  - id: getPolls
    intent: Get collated poll answers for a session
    question: What did the audience vote in the polls during a session?
  - id: getQuestions
    intent: Get the questions asked in a past session
    question: Which audience questions came up in a past webinar session and what were the answers?
  - id: getSurveys
    intent: Get surveys from a past session
    question: What survey feedback did attendees leave after a session?
  phrasing_ops: 7
  slug: gotowebinar-sessions-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Retrieve survey results from past sessions.
  name: GoToWebinar Surveys API
  phrasing_intents:
  - id: getSessionSurveys
    intent: Get survey results for a webinar session
    question: How did attendees rate my GoTo Webinar session in the survey?
  phrasing_ops: 1
  slug: gotowebinar-surveys-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Manage per-user subscriptions to a webhook.
  name: GoToWebinar User Subscriptions API
  phrasing_intents:
  - id: listUserSubscriptions
    intent: List my webhook user subscriptions
    question: Which webhook subscriptions do I currently have set up on GoTo Webinar?
  - id: createUserSubscription
    intent: Subscribe a callback URL to a webhook
    question: How do I start receiving webhook events at my own endpoint?
  - id: getUserSubscription
    intent: Get one webhook user subscription
    question: What callback URL and state does a particular user subscription have?
  - id: updateUserSubscription
    intent: Change a user subscription's callback or state
    question: How do I point an existing webhook subscription at a new callback URL?
  - id: deleteUserSubscription
    intent: Delete a webhook user subscription
    question: How do I stop receiving webhook events for one subscription for good?
  phrasing_ops: 5
  slug: gotowebinar-user-subscriptions-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Manage webhook definitions and secret keys.
  name: GoToWebinar Webhooks API
  phrasing_intents:
  - id: createSecretKey
    intent: Create a webhook signing secret key
    question: How do I get a secret key to verify the signature on webhook events?
  - id: createWebhooks
    intent: Create new webhooks with a callback URL
    question: How do I register a new webhook to receive webinar events?
  - id: updateWebhooks
    intent: Update webhooks' callback URL or state
    question: How do I change the callback URL on webhooks I already created?
  - id: getWebhooks
    intent: List my webhooks for a product
    question: Which webhooks have I registered for GoTo Webinar?
  - id: deleteWebhooks
    intent: Delete webhooks by key
    question: How do I delete webhooks I no longer use?
  - id: getWebhook
    intent: Get one webhook by key
    question: What callback URL and event is a particular webhook set up for?
  - id: createUserSubscriptions
    intent: Create user subscriptions for a webhook
    question: How do I subscribe users to a webhook I already created?
  - id: updateUserSubscriptions
    intent: Bulk update user subscriptions
    question: How do I change the callback URL on several user subscriptions together?
  phrasing_ops: 11
  slug: gotowebinar-webhooks-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Create, read, update, and delete webinars.
  name: GoToWebinar Webinars API
  phrasing_intents:
  - id: getAllAccountWebinars
    intent: List all webinars across an account
    question: Which webinars are scheduled across our whole GoTo Webinar account this month?
  - id: getWebinars
    intent: List an organizer's webinars in a date range
    question: What webinars do I have coming up or already held in a given period?
  - id: createWebinar
    intent: Schedule a new webinar
    question: How do I schedule a new webinar with a title and start and end time?
  - id: getInSessionWebinars
    intent: List webinars that are live right now
    question: Which of my webinars are currently in session?
  - id: getWebinar
    intent: Get a webinar's details
    question: What are the settings and scheduled times of one of my webinars?
  - id: updateWebinar
    intent: Update a webinar's title, times or description
    question: How do I reschedule or rename a webinar I already set up?
  - id: cancelWebinar
    intent: Cancel a webinar
    question: How do I cancel a scheduled webinar and let registrants know?
  - id: getAttendeesForAllWebinarSessions
    intent: Get attendees of all sessions of a webinar
    question: Who attended my webinar across all its sessions, page by page?
  phrasing_ops: 15
  slug: gotowebinar-webinars-api
- baseURL: https://api.getgo.com/G2W/rest/v2
  baseurl_source: declared
  description: Operations available for assets of a given organizer.
  name: GoToWebinar Recording Assets API
  phrasing_intents:
  - id: searchAssets
    intent: Search completed recordings in an account
    question: How do I find a finished webinar recording by name in my GoTo Webinar account?
  - id: searchAssetsForAdmin
    intent: Search an organizer's recordings as an admin
    question: As an account admin, how can I search the recordings of one organizer on my team?
  phrasing_ops: 2
  slug: gotowebinar-recording-assets-api
artifact_total: 87
asyncapis:
- description: Outbound webhook events delivered by the GoToWebinar webhook infrastructure to a developer-supplied callback URL. All events are HTTP POSTs signed via the `X-Webhook-Signature` header so receivers can
  name: GoToWebinar Webhook Events
  slug: gotowebinar-webhooks-asyncapi
- description: ''
  name: Gotowebinar Webhooks
  slug: gotowebinar-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GoToWebinar REST Attendees API
  slug: open-gotowebinar-attendees-api
- collection_type: open
  name: GoToWebinar REST Attendees Co-Organizers API
  slug: open-gotowebinar-co-organizers-api
- collection_type: open
  name: GoToWebinar REST Attendees Panelists API
  slug: open-gotowebinar-panelists-api
- collection_type: open
  name: GoToWebinar REST Attendees Polls API
  slug: open-gotowebinar-polls-api
- collection_type: open
  name: GoToWebinar REST Attendees Questions API
  slug: open-gotowebinar-questions-api
- collection_type: open
  name: GoToWebinar REST Attendees Recordings API
  slug: open-gotowebinar-recordings-api
- collection_type: open
  name: GoToWebinar REST Attendees Registrants API
  slug: open-gotowebinar-registrants-api
- collection_type: open
  name: GoToWebinar REST API
  slug: open-gotowebinar-rest
- collection_type: open
  name: GoToWebinar REST Attendees Sessions API
  slug: open-gotowebinar-sessions-api
- collection_type: open
  name: GoToWebinar REST Attendees Surveys API
  slug: open-gotowebinar-surveys-api
- collection_type: open
  name: GoToWebinar REST Attendees User Subscriptions API
  slug: open-gotowebinar-user-subscriptions-api
- collection_type: open
  name: GoToWebinar REST Attendees Webhooks API
  slug: open-gotowebinar-webhooks-api
- collection_type: open
  name: GoToWebinar Webhooks Management API
  slug: open-gotowebinar-webhooks
- collection_type: open
  name: GoToWebinar REST Attendees Webinars API
  slug: open-gotowebinar-webinars-api
common:
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/openapi/_original/gotowebinar-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/gotowebinar-openapi.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/packages/gotowebinar-packages.yml
  title: ''
  type: Packages
  url: packages/gotowebinar-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/packages/gotowebinar-packages.yml
  title: ''
  type: SDKs
  url: packages/gotowebinar-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/well-known/gotowebinar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gotowebinar-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/mcp/gotowebinar-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gotowebinar-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/llms/gotowebinar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gotowebinar-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/overlays/gotowebinar-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gotowebinar-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/conformance/gotowebinar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gotowebinar-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.goto.com/company/trust/compliance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/security/gotowebinar-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gotowebinar-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/security/gotowebinar-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gotowebinar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.goto.com/company/trust/security-measures
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/errors/gotowebinar-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gotowebinar-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/lifecycle/gotowebinar-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gotowebinar-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/conventions/gotowebinar-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gotowebinar-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/data-model/gotowebinar-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gotowebinar-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/asyncapi/gotowebinar-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gotowebinar-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/collections/gotowebinar-v2-provider.postman_collection.json
  title: ''
  type: Postman
  url: collections/gotowebinar-v2-provider.postman_collection.json
- group: company
  title: ''
  type: Website
  url: https://www.goto.com/webinar
- group: docs
  title: ''
  type: APIReference
  url: https://developer.goto.com/GoToWebinarV2
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoTo-Developers
- group: company
  title: ''
  type: Blog
  url: https://www.goto.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://developer.goto.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goto.com/company/legal/api-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goto.com/company/legal/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goto
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/agentic-access/gotowebinar-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gotowebinar-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/security/gotowebinar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gotowebinar-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/authentication/gotowebinar-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gotowebinar-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/scopes/gotowebinar-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gotowebinar-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.goto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.goto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.goto.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.goto.com/guides/Get%20Started/00_Quickstart_GettingStarted/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.goto.com/guides/Authentication/New_Token_Retrieval_Migration_Guide/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.goto.com/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goto.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.goto.com/support
- group: start
  title: ''
  type: Signup
  url: https://developer.goto.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goto.com/pricing/webinar
- group: other
  title: ''
  type: Marketplace
  url: https://www.goto.com/integrations
- group: company
  title: ''
  type: Partners
  url: https://www.goto.com/partners
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/json-ld/gotowebinar-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gotowebinar-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/vocabulary/gotowebinar-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gotowebinar-vocabulary.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/plans/gotowebinar-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gotowebinar-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/rate-limits/gotowebinar-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gotowebinar-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/finops/gotowebinar-finops.yml
  title: ''
  type: FinOps
  url: finops/gotowebinar-finops.yml
created: '2026-05-23'
description: GoToWebinar is GoTo's (formerly LogMeIn) webinar and virtual event platform. The GoToWebinar REST API lets developers create and manage webinars, organizers, registrants, attendees, sessions, panelists, co-organizers, polls, surveys, and recordings, and subscribe to real-time webhook events for registrant and webinar lifecycle activity.
examples:
- key_count: 8
  name: Gotowebinar Create Registrant Request
  slug: gotowebinar-create-registrant-request
- key_count: 3
  name: Gotowebinar Create Registrant Response
  slug: gotowebinar-create-registrant-response
- key_count: 5
  name: Gotowebinar Create Webhook Request
  slug: gotowebinar-create-webhook-request
- key_count: 7
  name: Gotowebinar Create Webinar Request
  slug: gotowebinar-create-webinar-request
- key_count: 1
  name: Gotowebinar Create Webinar Response
  slug: gotowebinar-create-webinar-response
- key_count: 13
  name: Gotowebinar Webhook Registrant Joined
  slug: gotowebinar-webhook-registrant-joined
- key_count: 15
  name: Gotowebinar Webhook Webinar Created
  slug: gotowebinar-webhook-webinar-created
features:
- REST API for webinars, registrants, attendees, sessions, polls, surveys, recordings
- OAuth 2.0 authorization-code, password (deprecated), and refresh-token grants
- Token endpoint migrated to https://authentication.logmeininc.com/oauth/token
- Base URL https://api.getgo.com/G2W/rest/v2 for all V2 REST resources
- Webhooks for registrant.added, registrant.joined, webinar.created, webinar.changed
- X-Webhook-Signature HMAC header for callback validation
- User-subscription model layering webhook subscriptions per user (organizer)
- Single-session, recurring, and series webinar experience types
- Co-organizer and panelist management endpoints
- Pre-webinar registration with configurable custom questions
- Post-webinar polls, surveys, and Q&A retrieval
- Recording download URLs for post-event distribution
- Past-webinar deletion (deleteAll flag) introduced 03/25/2025
- Breakout session support for webinar creation added 01/21/2025
- Postman collections and OpenAPI download from developer.goto.com
- Integrates with Salesforce, Slack, Microsoft Teams, Zoho CRM, Google Workspace via GoTo marketplace
finops:
- name: Gotowebinar Finops
  service_category: ''
  slug: gotowebinar-finops
image: https://www.goto.com/-/media/images/logos/goto-logo.svg
integrations:
- description: Sync GoToWebinar registrants, attendees, and engagement data into Salesforce campaigns and leads.
  name: Salesforce
- description: Schedule and launch GoToWebinar sessions from Microsoft Teams workspaces.
  name: Microsoft Teams
- description: Receive webinar registration notifications and start sessions from Slack channels.
  name: Slack
- description: Connect Google Calendar invites and Gmail follow-ups with scheduled webinars.
  name: Google Workspace
- description: Push registrant.added webhook events into Zoho CRM lead pipelines.
  name: Zoho CRM
- description: Trigger HubSpot workflows from GoToWebinar registration and attendance events.
  name: HubSpot
- description: Sync webinar engagement back into Marketo nurture programs.
  name: Marketo
- description: Connect GoToWebinar to thousands of apps via no-code Zapier automations.
  name: Zapier
json_schemas:
- name: GoToWebinar Attendee
  property_count: 8
  slug: gotowebinar-attendee
- name: GoToWebinar Registrant
  property_count: 13
  slug: gotowebinar-registrant
- name: GoToWebinar Session
  property_count: 7
  slug: gotowebinar-session
- name: GoToWebinar Webhook
  property_count: 8
  slug: gotowebinar-webhook
- name: GoToWebinar Webinar
  property_count: 11
  slug: gotowebinar-webinar
json_structures:
- name: Gotowebinar Registrant Structure
  property_count: 0
  slug: gotowebinar-registrant-structure
- name: Gotowebinar Webinar Structure
  property_count: 0
  slug: gotowebinar-webinar-structure
jsonld:
- class_count: 34
  name: Gotowebinar Context
  property_count: 7
  slug: gotowebinar-context
layout: provider
modified: '2026-05-23'
name: GoToWebinar
nav: Providers
network: true
overview: 'GoToWebinar publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Co-Organizers API, Panelists API, and 10 more. Tagged areas include Attendees, Collaboration, Communications, Event, and Meetings.


  The GoToWebinar catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  GoToWebinar''s developer surface includes API reference, engineering blog, signup flow, authentication, developer portal, documentation, getting-started guide, and 41 more developer resources.'
plans:
- name: Gotowebinar Plans Pricing
  plan_count: 4
  slug: gotowebinar-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Gotowebinar Rate Limits
  slug: gotowebinar-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: GoToWebinar API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: gotowebinar-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: GoToWebinar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gotowebinar-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: GoToWebinar API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 3
  slug: gotowebinar-rules
scopes:
- name: Gotowebinar Scopes
  scope_count: 2
  slug: gotowebinar-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 0.0
    catalog_gap: 44.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 96.8
    contract_governance: 31.8
    contract_quality: 60.4
    developer_ergonomics: 55.4
    discoverability: 71.4
    operational_transparency: 52.6
  previous_composite: 67.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/gotowebinar/refs/heads/main/screenshots/gotowebinar-2026-06-20T182257.png
security:
- kind: authentication
  name: Gotowebinar Authentication
  slug: gotowebinar-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Gotowebinar Domain Security
  slug: gotowebinar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gotowebinar Vulnerability Disclosure
  slug: gotowebinar-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Gotowebinar Trust Center
  slug: gotowebinar-trust-center
  summary_line: SOC 2 (Type II), SOC 3, C5 (BSI Cloud Computing Compliance Criteria Catalogue)
slug: gotowebinar
tags:
- Attendees
- Collaboration
- Communications
- Event
- Meetings
- Registrants
- Sessions
- Surveys
- Video Conferencing
- Virtual Events
- Webhook
- Webinars
use_cases:
- description: Marketing teams capture qualified leads via registration forms and sync attendee data into their CRM through the GoToWebinar REST API.
  name: Lead Generation Webinars
- description: Customer success teams deliver scheduled product training webinars and pull attendance and survey data for engagement reporting.
  name: Customer Education
- description: Event teams host multi-session webinars with co-organizers, panelists, and breakout rooms for up to 3,000 attendees per session.
  name: Virtual Events at Scale
- description: Sales orgs run product demos as webinars and push registrant.joined webhook events into CRM workflows in real time.
  name: Sales Enablement
- description: HR and executive teams broadcast company-wide updates and use polls and surveys to capture employee feedback.
  name: Internal Town Halls
- description: Professional associations deliver accredited training webinars and export attendance data for CEU credit reporting.
  name: Continuing Education
website: https://www.goto.com/webinar
---
