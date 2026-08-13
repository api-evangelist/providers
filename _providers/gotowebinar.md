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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Gotowebinar Agentic Access
  operation_count: 30
  slug: gotowebinar-agentic-access
  summary_line: 30 operations · 13 acting
api_count: 12
apis:
- description: Read attendees for past webinar sessions.
  name: GoToWebinar Attendees API
  slug: gotowebinar-attendees-api
- description: Manage co-organizers on a webinar.
  name: GoToWebinar Co-Organizers API
  slug: gotowebinar-co-organizers-api
- description: Manage panelists on a webinar.
  name: GoToWebinar Panelists API
  slug: gotowebinar-panelists-api
- description: Retrieve poll results from past sessions.
  name: GoToWebinar Polls API
  slug: gotowebinar-polls-api
- description: Retrieve Q&A from past sessions.
  name: GoToWebinar Questions API
  slug: gotowebinar-questions-api
- description: Retrieve webinar recording assets.
  name: GoToWebinar Recordings API
  slug: gotowebinar-recordings-api
- description: Manage registrants for upcoming webinars.
  name: GoToWebinar Registrants API
  slug: gotowebinar-registrants-api
- description: Inspect past and live webinar sessions.
  name: GoToWebinar Sessions API
  slug: gotowebinar-sessions-api
- description: Retrieve survey results from past sessions.
  name: GoToWebinar Surveys API
  slug: gotowebinar-surveys-api
- description: Manage per-user subscriptions to a webhook.
  name: GoToWebinar User Subscriptions API
  slug: gotowebinar-user-subscriptions-api
- description: Manage webhook definitions and secret keys.
  name: GoToWebinar Webhooks API
  slug: gotowebinar-webhooks-api
- description: Create, read, update, and delete webinars.
  name: GoToWebinar Webinars API
  slug: gotowebinar-webinars-api
artifact_total: 70
asyncapis:
- description: Outbound webhook events delivered by the GoToWebinar webhook infrastructure to a developer-supplied callback URL. All events are HTTP POSTs signed via the `X-Webhook-Signature` header so receivers can
  name: GoToWebinar Webhook Events
  slug: gotowebinar-webhooks-asyncapi
collections:
- collection_type: open
  name: GoToWebinar REST API
  slug: open-gotowebinar-rest
- collection_type: open
  name: GoToWebinar Webhooks Management API
  slug: open-gotowebinar-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gotowebinar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gotowebinar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gotowebinar-authentication.yml
- group: auth
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
  title: ''
  type: JSONLD
  url: json-ld/gotowebinar-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/gotowebinar-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gotowebinar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gotowebinar-rate-limits.yml
- group: commercial
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
overview: 'GoToWebinar publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Attendees API, Co-Organizers API, Panelists API, and 9 more. Tagged areas include Attendees, Collaboration, Communications, Events, and Meetings.


  The GoToWebinar catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  GoToWebinar''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, support, signup flow, and 14 more developer resources.'
plans:
- name: Gotowebinar Plans Pricing
  plan_count: 4
  slug: gotowebinar-plans-pricing
random_paper: 105
rate_limits:
- limit_count: 0
  name: Gotowebinar Rate Limits
  slug: gotowebinar-rate-limits
rules:
- name: GoToWebinar API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: gotowebinar-asyncapi-spectral-rules
- name: GoToWebinar API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gotowebinar-jsonschema-spectral-rules
- name: GoToWebinar API Rules
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
  band: strong
  composite: 57.0
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 68.7
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
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
slug: gotowebinar
tags:
- Attendees
- Collaboration
- Communications
- Events
- Meetings
- Registrants
- Sessions
- Surveys
- Video Conferencing
- Virtual Events
- Webhooks
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
website: https://developer.goto.com/
---
