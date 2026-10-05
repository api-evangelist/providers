---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.5
  scored_at: '2026-10-04'
api_count: 3
apis:
- description: Hosted Model Context Protocol server exposing 30 Paubox tools across email, forms and email marketing to MCP-compatible AI clients. Reachable over streamable HTTP at https://mcp.paubox.com/mcp with OA
  name: Paubox MCP Server
  slug: paubox-mcp-server
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Campaign analytics and reporting operations
  name: Paubox Analytics API
  phrasing_intents:
  - id: getCampaignAnalytics
    intent: Get send totals for marketing campaigns
    question: What are the overall delivery and engagement totals across the campaigns I've sent?
  - id: getCampaignTable
    intent: List sent campaigns as an analytics table
    question: Where can I see a row-by-row table of every campaign I've sent?
  - id: getTrackingLinksByUniqueLink
    intent: Get link interaction stats grouped by unique link
    question: Which links in a campaign got clicked, grouped per unique link?
  - id: getSubscribersByTrackingLink
    intent: List subscribers who interacted with a tracking link
    question: Who exactly clicked a particular link in my campaign email?
  - id: getCampaignDeliveriesTable
    intent: List per-recipient deliveries for a campaign
    question: How do I see the individual deliveries that went out for a campaign?
  phrasing_ops: 5
  slug: paubox-analytics-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Campaign mailing management and sending operations
  name: Paubox Campaign Mailings API
  phrasing_intents:
  - id: getCampaignMailings
    intent: List marketing campaign emails
    question: What marketing emails do I have saved in my account?
  - id: createCampaignMailing
    intent: Create a marketing campaign email
    question: How do I draft a new marketing email through the API before sending it?
  - id: getCampaignMailing
    intent: Get one campaign mailing with its content
    question: How can I see the HTML and text content of a specific campaign email?
  - id: updateCampaignMailing
    intent: Edit an existing campaign mailing
    question: How do I change the subject of a marketing email I already created?
  - id: sendCampaignMailingTestEmail
    intent: Send a test preview of a campaign email
    question: Can I send myself a preview of a campaign email to check how it renders?
  - id: bulkDeleteCampaignMailings
    intent: Permanently delete campaign mailings
    question: How do I delete marketing emails I no longer need?
  - id: sendCampaignMailing
    intent: Send a campaign email to recipients now
    question: How do I trigger an immediate send of a marketing email I built in the web interface?
  - id: scheduleCampaignMailing
    intent: Schedule a campaign email for a future time
    question: Can I schedule a marketing email to go out at a specific date and time?
  phrasing_ops: 8
  slug: paubox-campaign-mailings-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Drip campaign management and automation operations
  name: Paubox Drip Campaigns API
  phrasing_intents:
  - id: getDripCampaigns
    intent: List drip campaigns
    question: What drip campaigns do I have set up?
  - id: getDripCampaign
    intent: Get details of one drip campaign
    question: How do I see the configuration of a single drip campaign?
  - id: updateDripCampaign
    intent: Update a drip campaign's settings
    question: Can I change the settings of an existing drip campaign?
  - id: startDripCampaign
    intent: Start a drip campaign
    question: How do I turn on a drip campaign so it begins sending?
  - id: pauseDripCampaign
    intent: Pause a drip campaign
    question: Is there a way to temporarily stop a drip campaign from sending?
  phrasing_ops: 5
  slug: paubox-drip-campaigns-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Manage and use dynamic Handlebars templates for email content
  name: Paubox Dynamic Templates API
  phrasing_intents:
  - id: listDynamicTemplates
    intent: List dynamic email templates
    question: Which Handlebars templates has my organization uploaded?
  - id: createDynamicTemplate
    intent: Upload a new Handlebars email template
    question: How do I upload a Handlebars .hbs file to use for templated emails?
  - id: getDynamicTemplate
    intent: Get one dynamic template
    question: How can I view a specific dynamic template's contents?
  - id: deleteDynamicTemplate
    intent: Delete a dynamic template
    question: How do I remove a dynamic template I no longer use?
  - id: updateDynamicTemplate
    intent: Update a dynamic template's name or file
    question: Can I replace the .hbs file behind an existing dynamic template?
  - id: sendTemplatedMessage
    intent: Send an email rendered from a dynamic template
    question: How do I send an email that fills a template with my own variables?
  phrasing_ops: 6
  slug: paubox-dynamic-templates-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Create, list, update, copy, and archive forms (requires API key)
  name: Paubox Form management API
  phrasing_intents:
  - id: listForms
    intent: List forms for a customer
    question: What forms do I have, and can I see only the archived ones?
  - id: createForm
    intent: Create a new form
    question: How do I build a new form through the API?
  - id: getFormStats
    intent: Get form and submission statistics
    question: How many active forms do I have and how many submissions came in this past week?
  - id: copyForm
    intent: Duplicate a form under a new title
    question: Can I duplicate an existing form instead of building it from scratch?
  - id: getForm
    intent: Get a form's full definition as its owner
    question: How do I retrieve the full definition of one of my forms, even if it's archived?
  - id: updateForm
    intent: Update a form's settings or fields
    question: How do I change who gets notified when a form is submitted?
  - id: archiveForm
    intent: Archive a form and stop submissions
    question: How do I archive a form so it stops accepting responses?
  - id: unarchiveForm
    intent: Unarchive a form
    question: Can I restore a form I archived?
  phrasing_ops: 8
  slug: paubox-form-management-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Retrieve form definitions and accept submissions
  name: Paubox Forms API
  phrasing_intents:
  - id: getPublicForm
    intent: Get a form's public definition for rendering
    question: How does an embed load a form's HTML, schema and CSS before showing it to respondents?
  - id: createFormSubmission
    intent: Submit a response to a form
    question: How do I submit answers to a form on behalf of a respondent?
  phrasing_ops: 2
  slug: paubox-forms-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Send individual or bulk transactional email
  name: Paubox Messages API
  phrasing_intents:
  - id: sendMessage
    intent: Send a single secure email
    question: How do I send one HIPAA-compliant email through Paubox?
  - id: sendBulkMessages
    intent: Send a batch of emails in one request
    question: Can I send many emails in a single request?
  - id: getMessageReceipt
    intent: Check delivery and open status of a sent email
    question: Was my email delivered, and did the recipient open it?
  phrasing_ops: 3
  slug: paubox-messages-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: List and export form submissions (requires API key)
  name: Paubox Submissions API
  phrasing_intents:
  - id: listFormSubmissions
    intent: List submissions received by a form
    question: How do I see the responses people submitted to my form?
  - id: exportSubmissionsCsv
    intent: Export all of a form's submissions as CSV
    question: Can I download every response to a form as a spreadsheet?
  - id: exportSubmissionCsv
    intent: Export one form submission as CSV
    question: Can I export just one form response as a CSV row?
  - id: exportSubmissionPdf
    intent: Export one form submission as PDF
    question: Can I get a PDF copy of a form response, including the signature?
  phrasing_ops: 4
  slug: paubox-submissions-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Subscriber management operations
  name: Paubox Subscribers API
  phrasing_intents:
  - id: getSubscribers
    intent: List marketing subscribers
    question: Who are the contacts in my marketing audience?
  - id: createSubscriber
    intent: Add a single subscriber
    question: How do I add one new contact to my marketing audience?
  - id: getSubscriber
    intent: Get one subscriber's details
    question: How do I look up a single subscriber's record?
  - id: updateSubscriberPut
    intent: Replace a subscriber's record (PUT)
    question: How do I overwrite a subscriber's record using a PUT request?
  - id: updateSubscriberPatch
    intent: Partially update a subscriber (PATCH)
    question: Can I change just a subscriber's name with a PATCH request?
  - id: bulkCreateSubscribers
    intent: Add many subscribers at once
    question: Can I import a batch of contacts in a single request?
  - id: bulkDeleteSubscribers
    intent: Delete subscribers in bulk
    question: How do I delete several subscribers at once?
  phrasing_ops: 7
  slug: paubox-subscribers-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Subscription list management operations
  name: Paubox Subscription Lists API
  phrasing_intents:
  - id: getSubscriptionLists
    intent: List contact lists
    question: What subscription lists do I have in my marketing account?
  - id: createSubscriptionList
    intent: Create a contact list
    question: How do I create a new contact list for segmenting subscribers?
  - id: updateSubscriptionListPut
    intent: Rename a contact list (PUT)
    question: How do I rename a subscription list with a PUT request?
  - id: deleteSubscriptionList
    intent: Delete a contact list
    question: How do I delete a subscription list I no longer need?
  - id: updateSubscriptionListPatch
    intent: Rename a contact list (PATCH)
    question: Can I patch a subscription list's name instead of using PUT?
  phrasing_ops: 5
  slug: paubox-subscription-lists-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Subscriber opt-in and opt-out operations
  name: Paubox Subscriptions API
  phrasing_intents:
  - id: getSubscriptions
    intent: List all subscriber-to-list subscriptions
    question: How do I see every subscriber-to-list membership in my account?
  - id: createSubscription
    intent: Subscribe an existing subscriber to a list
    question: How do I put an existing subscriber onto a list using their internal numeric ID?
  - id: getSubscription
    intent: Get one subscription
    question: How do I look up a single subscription by its UUID?
  - id: deleteSubscription
    intent: Unsubscribe one list membership
    question: How do I unsubscribe someone from just one list using the subscription's UUID?
  - id: subscribeSubscribers
    intent: Re-subscribe specific subscribers
    question: How do I re-subscribe a few contacts who previously opted out?
  - id: unsubscribeSubscribers
    intent: Unsubscribe or opt out specific subscribers
    question: How do I unsubscribe a handful of contacts by their UUIDs?
  - id: bulkGlobalSubscribe
    intent: Clear global opt-out for a whole list
    question: Can I clear the global opt-out for everyone on a subscription list without listing each one?
  - id: bulkGlobalUnsubscribe
    intent: Globally opt out a whole subscription list
    question: How do I globally opt out every member of a subscription list in one call?
  phrasing_ops: 10
  slug: paubox-subscriptions-api
- baseURL: https://api.paubox.com/v1/email
  baseurl_source: declared
  description: Tracking link analytics and data operations
  name: Paubox Tracking Links API
  phrasing_intents:
  - id: getTrackingLinks
    intent: List tracking links in a sent campaign
    question: Which links were included in the emails of a sent campaign, with their tracking info?
  phrasing_ops: 1
  slug: paubox-tracking-links-api
artifact_total: 21
asyncapis:
- description: ''
  name: Paubox Email Webhooks
  slug: paubox-email-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/capabilities/paubox-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/paubox-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/overlays/paubox-email-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/paubox-email-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/overlays/paubox-marketing-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/paubox-marketing-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/overlays/paubox-forms-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/paubox-forms-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.paubox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.paubox.com/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.paubox.com/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.paubox.com/email-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paubox.com/email-api/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.paubox.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://github.com/Paubox/community/discussions
- group: company
  title: ''
  type: Blog
  url: https://www.paubox.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Paubox
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paubox.com/pricing/paubox-email-api
- group: start
  title: ''
  type: SignUp
  url: https://www.paubox.com/pricing/paubox-email-api
- group: start
  title: ''
  type: Login
  url: https://next.paubox.com/users/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paubox.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paubox.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paubox.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.paubox.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/security/paubox-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/paubox-trust-center.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/llms/paubox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/paubox-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/a2a/paubox-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/paubox-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/mcp/paubox-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/paubox-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/packages/paubox-packages.yml
  title: ''
  type: Packages
  url: packages/paubox-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/packages/paubox-packages.yml
  title: ''
  type: SDKs
  url: packages/paubox-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/cli/paubox-cli.yml
  title: ''
  type: CLI
  url: cli/paubox-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/authentication/paubox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/paubox-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/conventions/paubox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/paubox-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/errors/paubox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/paubox-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/lifecycle/paubox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/paubox-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/conformance/paubox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/paubox-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/security/paubox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/paubox-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/plans/paubox-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/paubox-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/rate-limits/paubox-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/paubox-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/data-model/paubox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/paubox-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/asyncapi/paubox-email-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/paubox-email-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/well-known/paubox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/paubox-well-known.yml
- group: operate
  title: ''
  type: Contact
  url: mailto:support@paubox.com
created: '2026-08-26'
description: Paubox is a HIPAA compliant, HITRUST certified email infrastructure company serving healthcare organizations in the United States. Its products encrypt outbound email without recipient portals, passwords, or plugins, and work alongside Google Workspace and Microsoft 365. The developer surface is three REST APIs on api.paubox.com — the Paubox Email API for transactional email (send, bulk send, message receipt, Handlebars dynamic templates, templated messages) with an SMTP relay alternative at smtp.paubox.com:587; the Paubox Marketing API for HIPAA compliant campaign mailings, drip campaigns, subscribers, subscription lists, tracking links and campaign analytics; and the Paubox Forms API for building, hosting and processing secure patient intake forms with public respondent endpoints and scoped management endpoints. Paubox publishes OpenAPI 3.0 definitions for all three, official SDKs for ten languages, a Node-based CLI, delivery webhooks, an llms.txt, an A2A agent card, a published
  Agent Skill, and a hosted MCP server at mcp.paubox.com exposing 30 tools across email, forms and marketing.
image: https://www.paubox.com/hubfs/Logos/Paubox_Primary_color.svg
layout: provider
mcp_servers:
- description: 'Paubox ships a first-party Model Context Protocol server exposing 30 tools across the Email API, Forms API and Marketing API. It is offered over two transports: a hosted streamable-HTTP endpoint at ht'
  name: Paubox MCP Server
  slug: paubox-mcp-server
modified: '2026-08-26'
name: Paubox
nav: Providers
network: true
overview: 'Paubox publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Campaign Mailings API, Drip Campaigns API, and 10 more. Tagged areas include Email, HIPAA, Healthcare, Compliance, and Transactional Email.


  The Paubox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Paubox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Paubox Plans Pricing
  plan_count: 6
  slug: paubox-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Paubox Rate Limits
  slug: paubox-rate-limits
score:
  band: exemplar
  composite: 68.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 60.1
    developer_ergonomics: 78.6
    discoverability: 80.0
    operational_transparency: 57.9
  previous_composite: 68.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitech
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/paubox/refs/heads/main/screenshots/paubox-2026-09-02T150917.png
security:
- kind: authentication
  name: Paubox Authentication
  slug: paubox-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Paubox Domain Security
  slug: paubox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Paubox Vulnerability Disclosure
  slug: paubox-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Paubox Trust Center
  slug: paubox-trust-center
  summary_line: paubox_own, inherited_from_infrastructure
slug: paubox
tags:
- Email
- HIPAA
- Healthcare
- Compliance
- Transactional Email
- Email Marketing
- Forms
- Security
- Encryption
- Messaging
- A2A
website: https://www.paubox.com/
---
