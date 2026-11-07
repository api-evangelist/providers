---
access_model:
  confidence: high
  label: Free plan, self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: true
  source:
  - https://loops.so/pricing
  - https://loops.so/docs/api-reference/intro
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Loops Agentic Access
  operation_count: 64
  slug: loops-agentic-access
  summary_line: 64 operations · 35 acting
api_count: 1
apis:
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Validate a Loops API key and discover which team it belongs to. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops API key API
  phrasing_intents:
  - id: testApiKey
    intent: Test an API key and see its team
    question: How can I check that my Loops API key is valid?
  phrasing_ops: 1
  slug: loops-api-key-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Read and create saved audience segments used to target campaigns and workflows. 3 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Audience segments API
  phrasing_intents:
  - id: getAudienceSegment
    intent: Get an audience segment
    question: How do I look up the details of one audience segment?
  - id: listAudienceSegments
    intent: List audience segments
    question: What audience segments have we set up?
  - id: createAudienceSegment
    intent: Create an audience segment
    question: How do I create a saved audience segment from filter conditions?
  phrasing_ops: 3
  slug: loops-audience-segments-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Organize campaigns into groups. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Campaign groups API
  phrasing_intents:
  - id: listCampaignGroups
    intent: List campaign groups
    question: Which groups are my campaigns organized into?
  - id: createCampaignGroup
    intent: Create a campaign group
    question: How do I make a new folder to organize campaigns?
  - id: getCampaignGroup
    intent: Get a campaign group
    question: How do I see the details of a single campaign group?
  - id: updateCampaignGroup
    intent: Rename or redescribe a campaign group
    question: How do I rename an existing campaign group?
  phrasing_ops: 4
  slug: loops-campaign-groups-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, target, schedule and update email campaigns. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Campaigns API
  phrasing_intents:
  - id: listCampaigns
    intent: List campaigns
    question: What email campaigns do I have in Loops?
  - id: createCampaign
    intent: Create a draft campaign
    question: How do I start a new draft email campaign?
  - id: getCampaign
    intent: Get a campaign
    question: How do I check the status and settings of one campaign?
  - id: updateCampaign
    intent: Update a campaign's audience, group or schedule
    question: How do I reschedule a draft campaign that already exists?
  phrasing_ops: 4
  slug: loops-campaigns-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, read and update reusable LMX email components. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Components API
  phrasing_intents:
  - id: getComponent
    intent: Get an email component
    question: How do I view the LMX body of a reusable email component?
  - id: updateComponent
    intent: Update an email component
    question: If I edit a shared component, do the emails using it change too?
  - id: listComponents
    intent: List email components
    question: Which reusable email components exist on my team?
  - id: createComponent
    intent: Create an email component
    question: How do I create a reusable block I can drop into emails?
  phrasing_ops: 4
  slug: loops-components-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Read team configuration, including dedicated sending IP addresses. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Configuration API
  phrasing_intents:
  - id: listDedicatedSendingIps
    intent: List dedicated sending IP addresses
    question: Which IP addresses does Loops send mail from?
  phrasing_ops: 1
  slug: loops-configuration-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create and list the custom properties available on contacts. 2 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Contact properties API
  phrasing_intents:
  - id: createContactProperty
    intent: Create a custom contact property
    question: How do I add a new custom field to my contacts?
  - id: listContactProperties
    intent: List contact properties
    question: What contact properties does my account have?
  phrasing_ops: 2
  slug: loops-contact-properties-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, update, find and delete contacts, and manage suppression status. 6 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Contacts API
  phrasing_intents:
  - id: createContact
    intent: Add a new contact
    question: How do I add a new subscriber to my audience?
  - id: updateContact
    intent: Update or upsert a contact
    question: How do I change an existing contact's name or properties?
  - id: findContact
    intent: Find a contact by email or user ID
    question: Is a given email address already a contact?
  - id: deleteContact
    intent: Delete a contact
    question: How do I permanently remove someone from my audience?
  - id: getContactSuppression
    intent: Check a contact's suppression status
    question: Is this contact suppressed from receiving emails?
  - id: removeContactSuppression
    intent: Remove a contact from the suppression list
    question: How do I unsuppress a contact so they can get emails again?
  phrasing_ops: 6
  slug: loops-contacts-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Read, update, preview and Guardian-validate the LMX body of campaigns, workflow emails and transactional templates. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Email messages API
  phrasing_intents:
  - id: getEmailMessage
    intent: Get an email message
    question: How do I read the subject, sender and content of an email message?
  - id: updateEmailMessage
    intent: Edit an email's subject, sender or content
    question: How do I set the subject line and sender on a draft email?
  - id: previewEmailMessage
    intent: Send a test preview of an email
    question: How do I send myself a test copy of an email before it goes out?
  - id: getEmailMessageGuardian
    intent: Check an email for publishing errors
    question: What errors are blocking this email from being published?
  phrasing_ops: 4
  slug: loops-email-messages-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Read the event patterns Loops has detected from incoming events, including their observed properties. 3 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Event patterns API
  phrasing_intents:
  - id: listEventPatterns
    intent: List event patterns for workflow triggers
    question: Which events can trigger a workflow?
  - id: getEventPatternByName
    intent: Look up an event pattern by event name
    question: What properties does the event named PaymentReceived carry?
  - id: getEventPattern
    intent: Get an event pattern by ID
    question: How do I fetch an event pattern when I only have its ID?
  phrasing_ops: 3
  slug: loops-event-patterns-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Send events that update contact activity and trigger published workflows. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Events API
  phrasing_intents:
  - id: sendEvent
    intent: Send an event to trigger workflows
    question: How do I fire an event that kicks off a workflow for a contact?
  phrasing_ops: 1
  slug: loops-events-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: List the mailing lists in your account. 1 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Mailing lists API
  phrasing_intents:
  - id: listMailingLists
    intent: List mailing lists
    question: What mailing lists does my account have?
  phrasing_ops: 1
  slug: loops-mailing-lists-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, read and update reusable email themes. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Themes API
  phrasing_intents:
  - id: getTheme
    intent: Get an email theme
    question: How do I see the styles in a particular email theme?
  - id: updateTheme
    intent: Update an email theme
    question: If I change a theme's styles, which emails are affected?
  - id: listThemes
    intent: List email themes
    question: Which email themes has my team created?
  - id: createTheme
    intent: Create an email theme
    question: How do I create a new theme to style my emails?
  phrasing_ops: 4
  slug: loops-themes-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, edit, publish, list and send transactional email templates with data variables. 8 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Transactional emails API
  phrasing_intents:
  - id: sendTransactionalEmail
    intent: Send a transactional email
    question: How do I send a password reset or receipt email to one person?
  - id: listPublishedTransactionalEmails
    intent: List published transactional emails
    question: Which transactional emails are published and ready to send?
  - id: listTransactionalEmails
    intent: List all transactional emails incl. drafts
    question: What transactional emails exist, including ones not yet published?
  - id: createTransactionalEmail
    intent: Create a transactional email
    question: How do I set up a new transactional email template?
  - id: getTransactionalEmail
    intent: Get a transactional email
    question: How do I look up one transactional email's details?
  - id: updateTransactionalEmail
    intent: Rename or regroup a transactional email
    question: How do I rename an existing transactional email?
  - id: ensureTransactionalDraft
    intent: Open a draft for a transactional email
    question: How do I start editing a published transactional email without changing the live version?
  - id: publishTransactionalEmail
    intent: Publish a transactional email draft
    question: How do I make my edited transactional draft go live?
  phrasing_ops: 8
  slug: loops-transactional-emails-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Organize transactional emails into groups. 4 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Transactional groups API
  phrasing_intents:
  - id: listTransactionalGroups
    intent: List transactional groups
    question: Which groups organize my transactional emails?
  - id: createTransactionalGroup
    intent: Create a transactional group
    question: How do I create a folder for transactional emails?
  - id: getTransactionalGroup
    intent: Get a transactional group
    question: How do I see one transactional group's details?
  - id: updateTransactionalGroup
    intent: Rename or redescribe a transactional group
    question: How do I rename an existing transactional group?
  phrasing_ops: 4
  slug: loops-transactional-groups-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Upload image assets for use in emails via a presigned-URL flow. 2 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Uploads API
  phrasing_intents:
  - id: createUpload
    intent: Request a pre-signed URL to upload an image
    question: How do I upload an image to use in my emails?
  - id: completeUpload
    intent: Finalize an image upload
    question: What do I do after putting the file to the pre-signed URL?
  phrasing_ops: 2
  slug: loops-uploads-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Create, read, update, delete and reroute the nodes of a workflow graph. 7 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Workflow nodes API
  phrasing_intents:
  - id: createWorkflowNode
    intent: Add a node to a workflow
    question: How do I insert a new step into a workflow?
  - id: addWorkflowBranch
    intent: Add a branch to a branch or experiment node
    question: How do I add another path under a branch node?
  - id: getWorkflowNode
    intent: Get a workflow node
    question: How do I see the settings of a single workflow step?
  - id: updateWorkflowNode
    intent: Update a workflow node's settings
    question: How do I change the configuration of one workflow step?
  - id: deleteWorkflowNode
    intent: Delete a single workflow node
    question: How do I remove just one step from a workflow?
  - id: rerouteNodeConnection
    intent: Reroute a node's outgoing connection
    question: How do I point a workflow step at a different next step?
  - id: deleteWorkflowNodeRecursively
    intent: Delete a node and everything below it
    question: How do I remove a whole branch of a workflow in one go?
  phrasing_ops: 7
  slug: loops-workflow-nodes-api
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: List, create, inspect and update automation workflows and their mailing-list targeting. 5 operation(s) in the Loops REST API v1 (OpenAPI 1.21.6).
  name: Loops Workflows API
  phrasing_intents:
  - id: listWorkflows
    intent: List workflows
    question: What automated workflows do I have?
  - id: createWorkflow
    intent: Create a draft workflow
    question: How do I start a new email automation workflow?
  - id: getWorkflow
    intent: Get a workflow's graph
    question: How do I see all the steps and connections in a workflow?
  - id: updateWorkflowProperties
    intent: Rename or redescribe a workflow
    question: How do I rename an existing workflow?
  - id: changeWorkflowMailingList
    intent: Change a workflow's mailing list
    question: How do I switch which mailing list a workflow sends to?
  phrasing_ops: 5
  slug: loops-workflows-api
- description: Remote Model Context Protocol server for Loops, reachable at https://mcp.loops.so over Streamable HTTP with OAuth 2.0 (PKCE, scope "mcp"). Exposes four meta-tools — search, describe, execute and teams
  name: Loops MCP Server
  slug: loops-mcp-server
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: Outbound event surface. Seventeen signed event types covering contact lifecycle, mailing-list membership, and email delivery, engagement and complaint signals, delivered by HTTP POST to one subscriber
  name: Loops Webhooks
  slug: loops-webhooks
- baseURL: https://app.loops.so/api/v1
  baseurl_source: declared
  description: 'Events Loops sends to your configured webhook endpoint when certain events happen in your account. Configure an endpoint in Settings → Webhooks. Each account supports one webhook endpoint. Events are '
  name: Loops Webhooks API
  slug: loops-webhooks-api
artifact_total: 48
asyncapis:
- description: Event catalog for the Loops webhook surface, derived operation-for-operation from the `webhooks` block of the Loops OpenAPI 3.1 document (info.version 1.21.6, published at https://app.loops.so/openapi
  name: Loops Webhooks
  slug: loops-webhooks-asyncapi
collections:
- collection_type: open
  name: Loops OpenAPI Spec API key API
  slug: open-loops-api-key-api
- collection_type: open
  name: Loops OpenAPI Spec API key Campaigns API
  slug: open-loops-campaigns-api
- collection_type: open
  name: Loops OpenAPI Spec API key Components API
  slug: open-loops-components-api
- collection_type: open
  name: Loops OpenAPI Spec API key Contact properties API
  slug: open-loops-contact-properties-api
- collection_type: open
  name: Loops OpenAPI Spec API key Contacts API
  slug: open-loops-contacts-api
- collection_type: open
  name: Loops OpenAPI Spec API key Dedicated sending IPs API
  slug: open-loops-dedicated-sending-ips-api
- collection_type: open
  name: Loops OpenAPI Spec API key Email messages API
  slug: open-loops-email-messages-api
- collection_type: open
  name: Loops OpenAPI Spec API key Events API
  slug: open-loops-events-api
- collection_type: open
  name: Loops OpenAPI Spec API key Mailing lists API
  slug: open-loops-mailing-lists-api
- collection_type: open
  name: Loops OpenAPI Spec API key Themes API
  slug: open-loops-themes-api
- collection_type: open
  name: Loops OpenAPI Spec API key Transactional emails API
  slug: open-loops-transactional-emails-api
common:
- group: other
  href: https://artifacts.apis.io/loops/capabilities/loops-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/loops-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/loops/agentic-access/loops-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/loops-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/loops/authentication/loops-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loops-authentication.yml
- group: auth
  href: https://artifacts.apis.io/loops/scopes/loops-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/loops-scopes.yml
- group: design
  href: https://artifacts.apis.io/loops/conventions/loops-conventions.yml
  title: ''
  type: Conventions
  url: conventions/loops-conventions.yml
- group: design
  href: https://artifacts.apis.io/loops/conventions/loops-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/loops-conventions.yml
- group: design
  href: https://artifacts.apis.io/loops/errors/loops-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/loops-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/loops/rate-limits/loops-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/loops-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/loops/plans/loops-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loops-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/loops/finops/loops-finops.yml
  title: ''
  type: FinOps
  url: finops/loops-finops.yml
- group: design
  href: https://artifacts.apis.io/loops/data-model/loops-data-model.yml
  title: ''
  type: DataModel
  url: data-model/loops-data-model.yml
- group: build
  href: https://artifacts.apis.io/loops/examples/loops-examples.yml
  title: ''
  type: Examples
  url: examples/loops-examples.yml
- group: build
  href: https://artifacts.apis.io/loops/packages/loops-packages.yml
  title: ''
  type: Packages
  url: packages/loops-packages.yml
- group: build
  href: https://artifacts.apis.io/loops/packages/loops-packages.yml
  title: ''
  type: SDKs
  url: packages/loops-packages.yml
- group: build
  href: https://artifacts.apis.io/loops/cli/loops-cli.yml
  title: ''
  type: CLI
  url: cli/loops-cli.yml
- group: agent
  href: https://artifacts.apis.io/loops/mcp/loops-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/loops-mcp.yml
- group: build
  href: https://artifacts.apis.io/loops/mcp/loops-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/loops-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/loops/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/loops/asyncapi/loops-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/loops-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/loops/asyncapi/loops-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/loops-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/loops/well-known/loops-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loops-well-known.yml
- group: design
  href: https://artifacts.apis.io/loops/lifecycle/loops-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/loops-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loops.so
- group: operate
  href: https://artifacts.apis.io/loops/changelog/loops-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/loops-changelog.yml
- group: design
  href: https://artifacts.apis.io/loops/conformance/loops-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loops-conformance.yml
- group: auth
  href: https://artifacts.apis.io/loops/conformance/loops-conformance.yml
  title: ''
  type: Compliance
  url: conformance/loops-conformance.yml
- group: auth
  href: https://artifacts.apis.io/loops/security/loops-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/loops-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/loops/security/loops-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loops-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/loops/llms/loops-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loops-llms.txt
- group: company
  title: ''
  type: Website
  url: https://loops.so/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://loops.so/docs
- group: docs
  title: ''
  type: Documentation
  url: https://loops.so/docs
- group: docs
  title: ''
  type: APIReference
  url: https://loops.so/docs/api-reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://loops.so/docs/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://loops.so/docs/quickstart-agents
- group: operate
  title: ''
  type: Support
  url: https://app.loops.so/settings?page=support
- group: company
  title: ''
  type: Blog
  url: https://loops.so/engineering
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Loops-so
- group: commercial
  title: ''
  type: Pricing
  url: https://loops.so/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.loops.so/register
- group: start
  title: ''
  type: Login
  url: https://app.loops.so/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loops.so/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loops.so/privacy
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://loops.so/dpa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendwithloops
- group: other
  title: ''
  type: Glossary
  url: https://loops.so/glossary
created: '2026-05-08'
description: Loops is an email platform built for software companies, combining marketing campaigns, product and lifecycle automation, and transactional email on one contact model. Its REST API v1 exposes 64 operations across contacts, contact properties, mailing lists, audience segments, events and event patterns, campaigns, transactional emails, email messages authored in its own LMX markup, themes, components, uploads and workflow graphs, plus a 17-event signed webhook surface. Loops publishes its OpenAPI 3.1 document openly, ships first-party SDKs for JavaScript, Go, PHP, Ruby and Nuxt, a Go CLI, four versioned Agent Skills, and a hosted OAuth-protected MCP server at mcp.loops.so. Pricing is based on stored subscribed contacts rather than send volume, with a permanent free tier. The operating company is Astrodon Corporation.
finops:
- has_sources: true
  method: derived
  name: Loops Finops
  primary_unit: subscribed contacts
  service_category: ''
  slug: loops-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loops.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.loops.so over streamable HTTP requiring OAuth; 4 tools listed.
  name: Loops MCP Server
  slug: loops
modified: '2026-08-13'
name: Loops
nav: Providers
network: true
overview: 'Loops publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including API key API, Audience segments API, Campaign groups API, and 18 more. Tagged areas include Email, Email API, Marketing Automation, Transactional Email, and Lifecycle Email.


  The Loops catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Loops'' developer surface includes authentication, code examples, CLI, changelog, documentation, API reference, getting-started guide, and 39 more developer resources.'
plans:
- name: Loops Plans Pricing
  plan_count: 3
  slug: loops-plans-pricing
- name: Loops Price Estimates
  plan_count: 0
  slug: loops-price-estimates
random_paper: 5
rate_limits:
- limit_count: 8
  name: Loops Rate Limits
  slug: loops-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Loops API Rules
  rule_count: 56
  severity_counts:
    error: 45
    hint: 0
    info: 2
    warn: 9
  slug: loops-rules
scopes:
- name: Loops Scopes
  scope_count: 1
  slug: loops-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 76.6
  coverage:
    artifact_dirs: 34
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 63.7
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 73.7
  previous_composite: 75.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 94.7
      total: 19
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/loops/loops-2026-06-20T184718.png
security:
- kind: authentication
  name: Loops Authentication
  slug: loops-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Loops Domain Security
  slug: loops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Loops Trust Center
  slug: loops-trust-center
  summary_line: SOC 2, EU-U.S. Data Privacy Framework, Swiss-U.S. Data Privacy Framework
skill_count: 4
skills:
- name: loops-api
  slug: loops-api
- name: loops-cli
  slug: loops-cli
- name: loops-email-sending-best-practices
  slug: loops-email-sending-best-practices
- name: loops-lmx
  slug: loops-lmx
slug: loops
tags:
- Email
- Email API
- Marketing Automation
- Transactional Email
- Lifecycle Email
- Webhook
- Software-as-a-Service
- Communications
- Developer Tools
- MCP
- Agents
- Campaigns
website: https://loops.so/
---
