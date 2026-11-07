---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
  band: agent-native
  dimensions:
    agent_card: conformant
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 71.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.onesignal.com
  baseurl_source: declared
  description: The Apps API from OneSignal — 21 operation(s) for apps.
  name: OneSignal Apps API
  phrasing_intents:
  - id: view-apps
    intent: List all apps in my OneSignal account
    question: Which OneSignal apps does my organization have?
  - id: create-an-app
    intent: Create a new app
    question: How do I create a new OneSignal app through the API?
  - id: view-an-app
    intent: View one app's details
    question: What settings and platform configuration does a single app have?
  - id: update-an-app
    intent: Update an app's name or push configuration
    question: How do I rename an existing app?
  - id: create-segments
    intent: Create an audience segment
    question: How do I build a new audience segment with filters?
  - id: view-segments
    intent: List an app's segments
    question: What audience segments exist in my app?
  - id: view-segment
    intent: View one segment and its subscriber count
    question: How many subscribers are in a particular segment right now?
  - id: update-segment
    intent: Rename or change the filters of a segment
    question: If I change a segment's filters, are the old filters replaced or merged?
  phrasing_ops: 42
  slug: onesignal-apps-api
- baseURL: https://api.onesignal.com
  baseurl_source: declared
  description: The Notifications API from OneSignal — 4 operation(s) for notifications.
  name: OneSignal Notifications API
  phrasing_intents:
  - id: message-history
    intent: See which subscriptions received a message
    question: Which subscriptions were sent or clicked a particular message?
  - id: export-csv-of-events
    intent: Export a message's audience activity as CSV
    question: How do I download delivered, clicked and unsubscribed data for a message across push, email and SMS?
  - id: email
    intent: Send an email message
    question: How do I send an email campaign to a segment through OneSignal?
  - id: push-notification
    intent: Send a push notification
    question: How do I send a push notification with an image and action buttons?
  - id: sms
    intent: Send an SMS or MMS message
    question: How do I text a message to specific phone numbers?
  - id: view-messages
    intent: List sent messages, filterable by template
    question: Which messages were sent using a particular template?
  - id: view-message
    intent: View one message with its outcome metrics
    question: How did a single message perform on clicks and conversion outcomes?
  - id: cancel-message
    intent: Cancel a scheduled or sending message
    question: How do I stop a message that's already going out?
  phrasing_ops: 14
  slug: onesignal-notifications-api
- baseURL: https://api.onesignal.com
  baseurl_source: declared
  description: The Players API from OneSignal — 1 operation(s) for players.
  name: OneSignal Players API
  phrasing_intents:
  - id: csv-export
    intent: Export subscriptions to a CSV file
    question: How do I download all my subscription data as a CSV?
  - id: export_subscriptions
    intent: Export all user data to CSV (legacy endpoint)
    question: Is there an older, faster alternative to paging through every user record?
  phrasing_ops: 2
  slug: onesignal-players-api
- baseURL: https://api.onesignal.com
  baseurl_source: declared
  description: The Templates API from OneSignal — 3 operation(s) for templates.
  name: OneSignal Templates API
  phrasing_intents:
  - id: view-template
    intent: View a message template's content
    question: What content and channel does one of my message templates hold?
  - id: delete-template
    intent: Permanently delete a message template
    question: Can I delete a template that's still used in a Journey?
  - id: update-template
    intent: Update a push, email or SMS template
    question: Do template edits take effect immediately for API sends?
  - id: view-templates
    intent: Browse an app's message templates
    question: Which message templates exist in my app?
  - id: create-template
    intent: Create a reusable message template
    question: How do I make a reusable template for push, email or SMS?
  - id: view_templates
    intent: List templates (legacy endpoint)
    question: Is there an older endpoint for listing an app's templates?
  - id: copy-template-to-another-app
    intent: Duplicate a template into another app
    question: Can I reuse a message template in a different app in my organization?
  - id: delete_template
    intent: Delete a template (legacy endpoint)
    question: Is there a legacy endpoint for deleting a template by ID?
  phrasing_ops: 11
  slug: onesignal-templates-api
- description: OneSignal's hosted Model Context Protocol server at https://api.onesignal.com/mcp/oauth, connected over browser-based OAuth 2.1 with PKCE. Listed in the Cursor marketplace and Claude's connector direc
  name: OneSignal MCP Server
  slug: onesignal-mcp
- baseURL: https://api.onesignal.com
  baseurl_source: declared
  description: The Organizations API from OneSignal — 1 operation(s) for organizations.
  name: OneSignal Organizations API
  phrasing_intents:
  - id: list-audit-logs
    intent: List an organization's audit log events
    question: Who changed settings in my OneSignal organization last week?
  phrasing_ops: 1
  slug: onesignal-organizations-api
artifact_total: 28
asyncapis:
- description: ''
  name: Onesignal Webhooks
  slug: onesignal-webhooks
collections:
- collection_type: open
  name: OneSignal Apps API
  slug: open-onesignal-apps-api
- collection_type: open
  name: OneSignal Notifications API
  slug: open-onesignal-notifications-api
- collection_type: open
  name: OneSignal Players API
  slug: open-onesignal-players-api
- collection_type: open
  name: OneSignal Templates API
  slug: open-onesignal-templates-api
- collection_type: open
  name: OneSignal
  slug: open-onesignal
common:
- group: other
  href: https://artifacts.apis.io/onesignal/capabilities/onesignal-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/onesignal-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/onesignal/authentication/onesignal-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onesignal-authentication.yml
- group: auth
  href: https://artifacts.apis.io/onesignal/security/onesignal-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/onesignal-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/onesignal/security/onesignal-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onesignal-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneSignal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onesignal
- group: company
  title: ''
  type: Website
  url: https://onesignal.com/
- group: commercial
  href: https://artifacts.apis.io/onesignal/plans/onesignal-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onesignal-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/onesignal/rate-limits/onesignal-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/onesignal-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/onesignal/finops/onesignal-finops.yml
  title: ''
  type: FinOps
  url: finops/onesignal-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://onesignal.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://onesignal.com/blog/feed
- group: build
  href: https://artifacts.apis.io/onesignal/packages/onesignal-packages.yml
  title: ''
  type: Packages
  url: packages/onesignal-packages.yml
- group: build
  href: https://artifacts.apis.io/onesignal/packages/onesignal-packages.yml
  title: ''
  type: SDKs
  url: packages/onesignal-packages.yml
- group: agent
  href: https://artifacts.apis.io/onesignal/well-known/onesignal-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onesignal-well-known.yml
- group: auth
  href: https://artifacts.apis.io/onesignal/well-known/onesignal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/onesignal-security.txt
- group: agent
  href: https://artifacts.apis.io/onesignal/mcp/onesignal-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/onesignal-mcp.yml
- group: build
  href: https://artifacts.apis.io/onesignal/mcp/onesignal-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/onesignal-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/onesignal/a2a/onesignal-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/onesignal-a2a.yml
- group: agent
  href: https://artifacts.apis.io/onesignal/llms/onesignal-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onesignal-llms.txt
- group: design
  href: https://artifacts.apis.io/onesignal/conformance/onesignal-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onesignal-conformance.yml
- group: auth
  href: https://artifacts.apis.io/onesignal/security/onesignal-trust-center.yml
  title: ''
  type: Compliance
  url: security/onesignal-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/onesignal/security/onesignal-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/onesignal-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/onesignal/security/onesignal-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/onesignal-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/onesignal/errors/onesignal-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/onesignal-problem-types.yml
- group: design
  href: https://artifacts.apis.io/onesignal/lifecycle/onesignal-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/onesignal-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.onesignal.com
- group: design
  href: https://artifacts.apis.io/onesignal/conventions/onesignal-conventions.yml
  title: ''
  type: Conventions
  url: conventions/onesignal-conventions.yml
- group: design
  href: https://artifacts.apis.io/onesignal/conventions/onesignal-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/onesignal-conventions.yml
- group: operate
  href: https://artifacts.apis.io/onesignal/changelog/onesignal-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/onesignal-changelog.yml
- group: build
  href: https://artifacts.apis.io/onesignal/cli/onesignal-cli.yml
  title: ''
  type: CLI
  url: cli/onesignal-cli.yml
- group: design
  href: https://artifacts.apis.io/onesignal/components/onesignal-components.yml
  title: ''
  type: Components
  url: components/onesignal-components.yml
- group: design
  href: https://artifacts.apis.io/onesignal/data-model/onesignal-data-model.yml
  title: ''
  type: DataModel
  url: data-model/onesignal-data-model.yml
- group: design
  href: https://artifacts.apis.io/onesignal/asyncapi/onesignal-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/onesignal-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/onesignal/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.onesignal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.onesignal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.onesignal.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.onesignal.com/docs/en/quickstart-guide
- group: operate
  title: ''
  type: Support
  url: https://onesignal.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://onesignal.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.onesignal.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.onesignal.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://onesignal.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onesignal.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/onesignaldevs
- group: build
  href: https://artifacts.apis.io/onesignal/collections/onesignal.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/onesignal.postman_collection.json
created: '2026-05-08'
description: OneSignal is a lifecycle customer engagement platform for mobile push, web push, email, SMS/RCS, in-app messaging and iOS Live Activities, orchestrated through Journeys, segments and a single REST API at api.onesignal.com. It reports 1.3 trillion messages a year across 200k apps and 1.5 billion monthly active users. The developer surface is a published OpenAPI 3.1 contract, a full set of first-party server and client SDKs, a hosted OAuth-authenticated MCP server, an A2A agent card and six provider-published Agent Skills.
finops:
- has_sources: true
  method: derived
  name: Onesignal Finops
  primary_unit: subscription
  service_category: ''
  slug: onesignal-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onesignal.png
layout: provider
mcp_servers:
- description: OneSignal ships two distinct remote MCP servers. The product server at api.onesignal.com/mcp/oauth is the one Cursor, Claude, Copilot and ChatGPT connect to; it is OAuth-gated, so its tool schemas req
  name: OneSignal MCP
  slug: onesignal-mcp
modified: '2026-08-13'
name: OneSignal
nav: Providers
network: true
overview: 'OneSignal publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Notifications API, Players API, and 3 more. Tagged areas include Notification, Push, Email, SMS, and Mobile.


  The OneSignal catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  OneSignal''s developer surface includes authentication, engineering blog, changelog, CLI, documentation, API reference, getting-started guide, and 40 more developer resources.'
plans:
- name: Onesignal Plans Pricing
  plan_count: 4
  slug: onesignal-plans-pricing
- name: Onesignal Price Estimates
  plan_count: 0
  slug: onesignal-price-estimates
random_paper: 0
rate_limits:
- limit_count: 6
  name: Onesignal Rate Limits
  slug: onesignal-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: OneSignal API Rules
  rule_count: 57
  severity_counts:
    error: 36
    hint: 0
    info: 7
    warn: 14
  slug: onesignal-rules
score:
  band: exemplar
  composite: 78.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 62.4
    developer_ergonomics: 81.0
    discoverability: 75.0
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 78.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 30.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/onesignal/onesignal-2026-06-20T190717.png
security:
- kind: authentication
  name: Onesignal Authentication
  slug: onesignal-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Onesignal Domain Security
  slug: onesignal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Onesignal Vulnerability Disclosure
  slug: onesignal-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Onesignal Trust Center
  slug: onesignal-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27701, EU-U.S. Data Privacy Framework
skill_count: 6
skills:
- name: onesignal-iam-html-composer
  slug: onesignal-iam-html-composer
- name: onesignal-journeys
  slug: onesignal-journeys
- name: onesignal-mobile-sdk-setup
  slug: onesignal-mobile-sdk-setup
- name: Onesignal
  slug: onesignal-platform
- name: onesignal-segments
  slug: onesignal-segments
- name: onesignal-skill-creator
  slug: onesignal-skill-creator
slug: onesignal
tags:
- Notification
- Push
- Email
- SMS
- Mobile
- Push Notifications
- Web Push
- Customer Engagement
- Marketing Automation
- Live Activities
- RCS
- In-App Messaging
- Journeys
- Lifecycle Marketing
- MCP
- Agent Ready
- A2A
website: https://onesignal.com/
---
