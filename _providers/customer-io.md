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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Customer Io Agentic Access
  operation_count: 52
  slug: customer-io-agentic-access
  summary_line: 52 operations · 29 acting
api_count: 4
apis:
- description: The Customer.io Track API allows developers to send behavioral data and customer profile information into Customer.io. It provides endpoints for identifying customers, tracking events, managing device
  name: Customer.io Track API
  slug: track-api
- description: Retrieve activity logs for your workspace.
  name: Customer.io Activities API
  slug: customer-io-activities-api
- description: Merge two user identities by creating an alias linking a new identity to an existing one.
  name: Customer.io Alias API
  slug: customer-io-alias-api
- description: Send multiple API calls in a single request for improved performance.
  name: Customer.io Batch API
  slug: customer-io-batch-api
- description: Trigger API-triggered broadcasts to send messages to groups of people based on segments or filters.
  name: Customer.io Broadcasts API
  slug: customer-io-broadcasts-api
- description: Retrieve information about campaigns, campaign actions, and campaign metrics in your workspace.
  name: Customer.io Campaigns API
  slug: customer-io-campaigns-api
- description: Manage collections of data used in message personalization.
  name: Customer.io Collections API
  slug: customer-io-collections-api
- description: Look up customer profiles, search for customers, and retrieve customer attributes and activity data.
  name: Customer.io Customers API
  slug: customer-io-customers-api
- description: Export customer data, deliveries, and other information from your workspace.
  name: Customer.io Exports API
  slug: customer-io-exports-api
- description: Associate people with groups or organizations.
  name: Customer.io Group API
  slug: customer-io-group-api
- description: Identify people and set their profile attributes. The identify call tells Customer.io who the current user is and assigns traits to them.
  name: Customer.io Identify API
  slug: customer-io-identify-api
- description: Retrieve information about individual messages sent to customers.
  name: Customer.io Messages API
  slug: customer-io-messages-api
- description: Retrieve information about newsletters and newsletter variants.
  name: Customer.io Newsletters API
  slug: customer-io-newsletters-api
- description: Record page views from web applications.
  name: Customer.io Page API
  slug: customer-io-page-api
- description: Record screen views from mobile applications.
  name: Customer.io Screen API
  slug: customer-io-screen-api
- description: Create and manage manual segments, and retrieve segment membership information.
  name: Customer.io Segments API
  slug: customer-io-segments-api
- description: Manage sender identities used for sending messages.
  name: Customer.io Sender Identities API
  slug: customer-io-sender-identities-api
- description: Manage reusable content snippets for use in messages.
  name: Customer.io Snippets API
  slug: customer-io-snippets-api
- description: Send transactional messages such as password resets, purchase receipts, and other important notifications triggered by user actions.
  name: Customer.io Transactional API
  slug: customer-io-transactional-api
- description: Customer.io's first-party hosted Model Context Protocol server. It exposes the full Journeys App API and CDP Data Pipelines API to any MCP client through eight tools — a context primer, a schema brows
  name: Customer.io MCP
  slug: mcp
- description: Manage file assets such as images and PDFs and organize them into folders.
  name: Customer.io Assets API
  slug: customer-io-assets-api
- description: The Customer.io App API API from Customer.io — 0 operation(s) for customer.io app api.
  name: Customer.io Customer.io App API
  slug: customer-io-customer-io-app-api-api
- description: Update descriptions for attributes and events in your workspace. This helps improve AI-generated content and segments.
  name: Customer.io Data Index API
  slug: customer-io-data-index-api
- description: Use these endpoints to manage emails, translations, and components made with Design Studio. You can programmatically manage Design Studio content and migrate templates from an external service. To man
  name: Customer.io Design Studio API
  slug: customer-io-design-studio-api
- description: If you use Customer.io as your email service provider (ESP), these endpoints help you retrieve information about email addresses suppressed directly by the ESP. ESP-based suppressions are different fr
  name: Customer.io ESP Suppression API
  slug: customer-io-esp-suppression-api
- description: Connect forms to your workspace to identify people, apply form responses to people, and trigger campaigns for people who fill out forms on your website or in your app.
  name: Customer.io Forms API
  slug: customer-io-forms-api
- description: APIs to upload CSV files containing lists of people. These endpoints provide a convenient way to add and update people without having to make an `identify` call for each individual person.
  name: Customer.io Imports API
  slug: customer-io-imports-api
- description: Returns the list of addresses used by Customer.io. You must add add these addresses to your allowlist when using a custom SMTP provider and blocking unknown IP addresses.
  name: Customer.io Info API
  slug: customer-io-info-api
- description: 'Start, update, and end live notifications—real-time activities on the iOS Lock Screen and Dynamic Island, and in the Android notification shade. Your server drives the activity''s content; Customer.io '
  name: Customer.io Live Notifications API
  slug: customer-io-live-notifications-api
- description: 'Newsletter metrics include metrics for translations, A/B tests, and links. These endpoints return information about newsletter metrics including metrics for translations and A/B tests. You can update '
  name: Customer.io Newsletter Metrics API
  slug: customer-io-newsletter-metrics-api
- description: A newsletter variant is a translation or an A/B test. You can create, update, or delete variants in newsletters from these endpoints. You can also create a new A/B test group. If your newsletters incl
  name: Customer.io Newsletter Variants API
  slug: customer-io-newsletter-variants-api
- description: Objects are "groups" that you can relate people to in Customer.io—like the companies they work for, the online classes they take, and so on. These APIs help you find objects, their attributes, the peo
  name: Customer.io Objects API
  slug: customer-io-objects-api
- description: The Opt-outs API from Customer.io — 2 operation(s) for opt-outs.
  name: Customer.io Opt Outs API
  slug: customer-io-opt-outs-api
- description: Set up webhooks to inform an external service about Customer.io events. Webhooks can notify you immediately when immediately when customer attributes change or when people open your messages.
  name: Customer.io Reporting Webhooks API
  slug: customer-io-reporting-webhooks-api
- description: Use these endpoints to send broadcasts or transactional messages to your audience. They use the same authentication method, but review the limits for both types of workflows to make sure you'll succes
  name: Customer.io Send Messages API
  slug: customer-io-send-messages-api
- description: 'A subscription center differentiates the types of messages available for your product. Your audience sets subscription preferences by name, but we record subscription preferences by topic ID. You can '
  name: Customer.io Subscription Center API
  slug: customer-io-subscription-center-api
- description: Add, modify, suppress, or unsuppress people (referred to as "customers" in our APIs). You can also use these endpoints to set attributes on people.
  name: Customer.io Track Customers API
  slug: customer-io-track-customers-api
- description: Use customer events to trigger campaigns or add users to segments. You can attribute events directly to customers or send anonymous events and associate them with users later when you identify them.
  name: Customer.io Track Events API
  slug: customer-io-track-events-api
- description: Manual segments are lists of people that you incorporate using the API or by uploading CSVs. You can add people to, or remove people from, manual segments with these endpoints. These endpoints do _not
  name: Customer.io Track Segments API
  slug: customer-io-track-segments-api
- description: 'This version of our edge API has only two endpoints, but supports the majority of our traditional v1 track operations and then some based on the `type` and `action` keys that you set in your request. '
  name: Customer.io Track V2 API
  slug: customer-io-track-v2-api
- description: Determine whether your account and data are hosted in the US or EU data center using your [Track API Key](https://fly.customer.io/settings/api_credentials).
  name: Customer.io Track Region API
  slug: customer-io-trackregion-api
- description: An API to retrieve information about your workspaces in your account. You can use this to look up counts for messages sent, monthly billable emails sent, people, and objects.
  name: Customer.io Workspaces API
  slug: customer-io-workspaces-api
artifact_total: 87
asyncapis:
- description: Customer.io Reporting Webhooks send real-time message activity events as JSON payloads via HTTP POST to a configured endpoint. These events include message sends, deliveries, opens, clicks, bounces, u
  name: Customer.io Reporting Webhooks
  slug: customer-io-reporting-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Customer.io App Activities API
  slug: open-customer-io-activities-api
- collection_type: open
  name: Customer.io App Activities Alias API
  slug: open-customer-io-alias-api
- collection_type: open
  name: Customer.io App API
  slug: open-customer-io-app-api
- collection_type: open
  name: Customer.io App Activities Batch API
  slug: open-customer-io-batch-api
- collection_type: open
  name: Customer.io App Activities Broadcasts API
  slug: open-customer-io-broadcasts-api
- collection_type: open
  name: Customer.io App Activities Campaigns API
  slug: open-customer-io-campaigns-api
- collection_type: open
  name: Customer.io App Activities Collections API
  slug: open-customer-io-collections-api
- collection_type: open
  name: Customer.io App Activities Customers API
  slug: open-customer-io-customers-api
- collection_type: open
  name: Customer.io App Activities Devices API
  slug: open-customer-io-devices-api
- collection_type: open
  name: Customer.io App Activities Entity API
  slug: open-customer-io-entity-api
- collection_type: open
  name: Customer.io App Activities Events API
  slug: open-customer-io-events-api
- collection_type: open
  name: Customer.io App Activities Exports API
  slug: open-customer-io-exports-api
- collection_type: open
  name: Customer.io App Activities Group API
  slug: open-customer-io-group-api
- collection_type: open
  name: Customer.io App Activities Identify API
  slug: open-customer-io-identify-api
- collection_type: open
  name: Customer.io App Activities Merge API
  slug: open-customer-io-merge-api
- collection_type: open
  name: Customer.io App Activities Messages API
  slug: open-customer-io-messages-api
- collection_type: open
  name: Customer.io App Activities Newsletters API
  slug: open-customer-io-newsletters-api
- collection_type: open
  name: Customer.io App Activities Page API
  slug: open-customer-io-page-api
- collection_type: open
  name: Customer.io Pipelines API
  slug: open-customer-io-pipelines-api
- collection_type: open
  name: Customer.io App Activities Screen API
  slug: open-customer-io-screen-api
- collection_type: open
  name: Customer.io App Activities Segments API
  slug: open-customer-io-segments-api
- collection_type: open
  name: Customer.io App Activities Sender Identities API
  slug: open-customer-io-sender-identities-api
- collection_type: open
  name: Customer.io App Activities Snippets API
  slug: open-customer-io-snippets-api
- collection_type: open
  name: Customer.io App Activities Track API
  slug: open-customer-io-track-api
- collection_type: open
  name: Customer.io App Activities Transactional API
  slug: open-customer-io-transactional-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/customer-io-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/customer-io-pipelines-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/customer-io-reporting-webhooks-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/customer-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/customer-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/customer-io-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/customer-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/customer-io-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/customer-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/customer-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/customer-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/customerio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customer-io
- group: company
  title: ''
  type: Website
  url: https://customer.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.customer.io
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/customer-io-reporting-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-customer-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/customer-io-webhook-payload-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/customer-io-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/customer-io-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/customer-io-rules.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.customer.io/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/customer-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/customer-io-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/customer-io-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/customer-io-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/customer-io-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/customer-io-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/customer-io-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/customer-io-llms.txt
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/customer-io-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/customer-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/customer-io-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/customer-io-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.customerio.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/customer-io-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/customer-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/customer-io-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://customer.io/legal/reporting-vulnerability
- group: design
  title: ''
  type: DataModel
  url: data-model/customer-io-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/customer-io-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: openapi/_original/customer-io-reporting-webhooks-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/customer-io-app-api-overlay.yaml
- group: other
  title: ''
  type: APICatalog
  url: well-known/customer-io-api-catalog.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.customer.io/integrations/api/customerio-apis/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.customer.io/integrations/api/customerio-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.customer.io/get-started/
- group: operate
  title: ''
  type: Support
  url: https://customer.io/contact
- group: company
  title: ''
  type: Blog
  url: https://customer.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://customer.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://fly.customer.io/signup
- group: start
  title: ''
  type: Login
  url: https://fly.customer.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://customer.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://customer.io/legal/privacy-policy
- group: learn
  title: ''
  type: Academy
  url: https://academy.customer.io/pages/get-started
created: '2024-01-01'
description: Customer.io is a customer engagement platform that combines a customer data platform, marketing automation, and messaging delivery to send behavior-triggered email, push, SMS, and in-app messages. Its API surface includes the Track API for sending behavioral data and customer profile updates, the App API for managing workspace resources and sending transactional and broadcast messages, the Pipelines API which is a Segment-spec data ingestion interface, and outbound reporting webhooks that deliver message lifecycle events.
finops:
- name: Customer Io Finops
  service_category: Marketing and Customer Engagement
  slug: customer-io-finops
graphqls:
- description: 'This conceptual GraphQL schema represents the Customer.io messaging and marketing automation platform. Customer.io provides APIs for tracking behavioral data, managing customer profiles and segments, '
  name: Customer.io GraphQL Schema
  slug: customer-io-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/customer-io.png
json_schemas:
- name: Customer.io Customer
  property_count: 8
  slug: customer-io-customer
- name: Customer.io Event
  property_count: 7
  slug: customer-io-event
- name: Customer.io Reporting Webhook Payload
  property_count: 4
  slug: customer-io-webhook-payload
jsonld:
- class_count: 0
  name: Customer Io Context
  property_count: 11
  slug: customer-io-context
layout: provider
mcp_servers:
- description: 'Customer.io operates a first-party, hosted Model Context Protocol server that exposes the full Journeys App API and the CDP Data Pipelines API to any MCP client. It is a remote HTTP endpoint an agent '
  name: Customer.io MCP
  slug: customerio-mcp
modified: '2026-08-13'
name: Customer.io
nav: Providers
network: true
overview: 'Customer.io publishes 41 APIs on the [APIs.io](https://apis.io/) network, including Track API, Activities API, Alias API, and 38 more. Tagged areas include Behavioral Data, Broadcasts, Campaigns, CDP, and Customer Data.


  The Customer.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Customer.io''s developer surface includes authentication, documentation, CLI, changelog, sandbox, API reference, getting-started guide, and 50 more developer resources.'
plans:
- name: Customer Io Plans Pricing
  plan_count: 4
  slug: customer-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 6
  name: Customer Io Rate Limits
  slug: customer-io-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Customer.io API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: customer-io-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Customer.io API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: customer-io-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Customer.io API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: customer-io-rules
scopes:
- name: Customer Io Scopes
  scope_count: 0
  slug: customer-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 83.6
  coverage:
    artifact_dirs: 33
    catalog_gap: 33.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.4
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 47.0
    contract_quality: 72.0
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 47.0
    operational_transparency: 84.2
  previous_composite: 84.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 2.2
      total: 45
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/customer-io/refs/heads/main/screenshots/customer-io-2026-06-20T175348.png
security:
- kind: authentication
  name: Customer Io Authentication
  slug: customer-io-authentication
  summary_line: http/oauth2 · 5 schemes
- kind: domain-security
  name: Customer Io Domain Security
  slug: customer-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Customer Io Vulnerability Disclosure
  slug: customer-io-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Customer Io Trust Center
  slug: customer-io-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CCPA
slug: customer-io
tags:
- Behavioral Data
- Broadcasts
- Campaigns
- CDP
- Customer Data
- Customer Data Platform
- Data Ingestion
- Email
- Event Tracking
- Marketing Automation
- Messaging
- Push Notifications
- Segments
- SMS
- Transactional Email
website: https://customer.io
---
