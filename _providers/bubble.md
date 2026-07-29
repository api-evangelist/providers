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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Bubble Agentic Access
  operation_count: 19
  slug: bubble-agentic-access
  summary_line: 19 operations · 13 acting
api_count: 6
apis:
- description: REST API exposing the Bubble app database. Supports search with constraints, cursor-based pagination, single-record CRUD, bulk create (up to 1,000 records), and metadata discovery. Authentication uses
  name: Bubble Data API
  slug: bubble-data-api
- description: REST API for triggering backend workflows defined in the Bubble editor. Each workflow is exposed at `/api/1.1/wf/{workflow_name}` and can be configured for POST or GET, with authentication settings ra
  name: Bubble Workflow API
  slug: bubble-workflow-api
- description: Server-side and client-side action functions invoked by Bubble workflows.
  name: Bubble Action API
  slug: bubble-action-api
- description: Helpers exposed on the runtime context object.
  name: Bubble Context API
  slug: bubble-context-api
- description: Visual element lifecycle hooks invoked by the Bubble page renderer.
  name: Bubble Element API
  slug: bubble-element-api
- description: Database object accessors exposed to plugin code.
  name: Bubble Thing API
  slug: bubble-thing-api
arazzos:
- description: Bulk create many records of a data type, then search the type to verify they landed.
  name: Bubble Bulk Create Then Search
  slug: bubble-bulk-create-then-search-workflow
- description: Create a single record of a data type and read it back to confirm it persisted.
  name: Bubble Create and Verify a Thing
  slug: bubble-create-and-get-thing-workflow
- description: Create a record via the Data API, then trigger a backend workflow that processes it.
  name: Bubble Create a Thing Then Trigger a Backend Workflow
  slug: bubble-create-thing-then-trigger-workflow-workflow
- description: Read the Data API metadata to discover exposed types, then search one of them.
  name: Bubble Discover Data Types Then Search
  slug: bubble-discover-types-then-search-workflow
- description: Read a record by id to confirm it exists, then fully replace it with a new object.
  name: Bubble Get Then Replace a Thing
  slug: bubble-get-then-replace-thing-workflow
- description: Run the one-time detection call for a backend workflow, then trigger it with the same parameters.
  name: Bubble Initialize Then Trigger a Backend Workflow
  slug: bubble-initialize-then-trigger-workflow-workflow
- description: Search a data type for a record matching a constraint and delete the first match.
  name: Bubble Search Then Delete a Thing
  slug: bubble-search-then-delete-thing-workflow
- description: Search a data type for a record matching a constraint and modify the first match.
  name: Bubble Search Then Update a Thing
  slug: bubble-search-then-update-thing-workflow
- description: Trigger a backend workflow and record its result by creating a record via the Data API.
  name: Bubble Trigger a Workflow Then Log a Thing
  slug: bubble-trigger-workflow-then-log-thing-workflow
- description: Find a record by a key field and update it if it exists, otherwise create it.
  name: Bubble Upsert a Thing
  slug: bubble-upsert-thing-workflow
artifact_total: 71
collections:
- collection_type: postman
  name: Bubble Data API
  slug: postman-bubble-data-api
- collection_type: postman
  name: Bubble Plugin API
  slug: postman-bubble-plugin-api
- collection_type: postman
  name: Bubble Workflow API
  slug: postman-bubble-workflow-api
- collection_type: open
  name: Bubble Data API
  slug: open-bubble-data-api
- collection_type: open
  name: Bubble Plugin API
  slug: open-bubble-plugin-api
- collection_type: open
  name: Bubble Workflow API
  slug: open-bubble-workflow-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bubble-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bubble-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bubble-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bubble-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bubble/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-bulk-create-then-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-create-and-get-thing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-create-thing-then-trigger-workflow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-discover-types-then-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-get-then-replace-thing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-initialize-then-trigger-workflow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-search-then-delete-thing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-search-then-update-thing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-trigger-workflow-then-log-thing-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bubble-upsert-thing-workflow.yml
- group: docs
  title: ''
  type: Documentation
  url: https://manual.bubble.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://manual.bubble.io/getting-started.md
- group: docs
  title: ''
  type: APIReference
  url: https://manual.bubble.io/core-resources/api.md
- group: auth
  title: ''
  type: Authentication
  url: https://manual.bubble.io/help-guides/integrations/api/the-bubble-api/authentication/how-to-authenticate.md
- group: commercial
  title: ''
  type: Pricing
  url: https://bubble.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/bubble-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bubble-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: https://manual.bubble.io/account-and-marketplace/account-and-billing/pricing-plans.md
- group: start
  title: ''
  type: Signup
  url: https://bubble.io/signup
- group: start
  title: ''
  type: Login
  url: https://bubble.io/login
- group: start
  title: ''
  type: Portal
  url: https://bubble.io/
- group: other
  title: ''
  type: Marketplace
  url: https://bubble.io/plugins
- group: other
  title: ''
  type: Customers
  url: https://bubble.io/showcase
- group: other
  title: ''
  type: Showcase
  url: https://bubble.io/showcase
- group: company
  title: ''
  type: Blog
  url: https://bubble.io/blog
- group: operate
  title: ''
  type: Support
  url: https://bubble.io/contact
- group: operate
  title: ''
  type: ChangeLog
  url: https://bubble.io/release-notes
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://bubble.io/release-notes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bubble.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bubble.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bubble.io/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://manual.bubble.io/help-guides/security.md
- group: auth
  title: ''
  type: Security
  url: https://manual.bubble.io/help-guides/security/api-security.md
- group: auth
  title: ''
  type: TrustCenter
  url: https://bubble.io/trust
- group: other
  title: ''
  type: Glossary
  url: https://manual.bubble.io/glossary.md
- group: learn
  title: ''
  type: Academy
  url: https://bubble.io/academy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Bubble
- group: other
  title: ''
  type: X
  url: https://twitter.com/bubble
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bubble-group
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bubblegroup
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://manual.bubble.io/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bubble-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/bubble-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bubble-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/bubble-data-search-example.json
- group: build
  title: ''
  type: Examples
  url: examples/bubble-data-create-example.json
- group: build
  title: ''
  type: Examples
  url: examples/bubble-data-modify-example.json
- group: build
  title: ''
  type: Examples
  url: examples/bubble-data-bulk-create-example.json
- group: build
  title: ''
  type: Examples
  url: examples/bubble-workflow-trigger-example.json
- group: commercial
  title: ''
  type: FinOps
  url: finops/bubble-finops.yml
created: '2026-05-06'
description: Bubble is a no-code application development platform that lets builders ship full-stack web and mobile apps without writing code. Bubble exposes three developer APIs — the Data API for CRUD against the app database, the Workflow API for triggering backend automations, and a JavaScript Plugin API for extending the platform with custom actions and elements. Server-side consumption is metered in Workload Units (WU) bundled into a tiered subscription (Free, Starter, Growth, Team, Enterprise) with overage pricing for additional WU and storage.
examples:
- key_count: 2
  name: Bubble Data Bulk Create Example
  slug: bubble-data-bulk-create-example
- key_count: 2
  name: Bubble Data Create Example
  slug: bubble-data-create-example
- key_count: 2
  name: Bubble Data Modify Example
  slug: bubble-data-modify-example
- key_count: 2
  name: Bubble Data Search Example
  slug: bubble-data-search-example
- key_count: 2
  name: Bubble Workflow Trigger Example
  slug: bubble-workflow-trigger-example
features:
- description: Drag-and-drop application designer with responsive layouts and reusable element groups.
  name: Visual Editor
- description: Type-safe app database with privacy rules, search constraints, and Data API exposure.
  name: Built-In Database
- description: Server-side automation engine with scheduling, recurring events, and webhook triggers.
  name: Backend Workflows
- description: Public catalog of plugins exposing custom actions, elements, and integrations to Bubble apps.
  name: Plugin Marketplace
- description: Built-in HTTP client for calling external REST APIs from Bubble workflows and elements.
  name: API Connector
- description: Connect a custom domain on paid plans, with automatic SSL.
  name: Custom Domains
- description: Editor-level version control with branches and rollback (Growth, Team, Enterprise).
  name: Version Control
- description: Real-time visibility into Workload Unit consumption per activity, page, and workflow.
  name: Workload Dashboard
- description: Native iOS and Android builds via the Mobile add-on bundles.
  name: Mobile Builds
- description: Multiple editors and multi-app dashboards for agencies and teams.
  name: Multi-App Editing
finops:
- name: Bubble Finops
  service_category: Application Platform
  slug: bubble-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bubble.png
integrations:
- description: Built-in Stripe plugin for payments, subscriptions, and Connect.
  name: Stripe
- description: Transactional and marketing email via the SendGrid plugin.
  name: SendGrid
- description: SMS and programmable voice via the Twilio plugin.
  name: Twilio
- description: Maps, OAuth, Calendar, Sheets, and Drive integrations via plugins.
  name: Google APIs
- description: S3 file storage, Lambda, and SES integrations.
  name: AWS
- description: Hosted search backed by Algolia for high-volume Bubble data.
  name: Algolia
- description: Bubble Workflow API endpoints triggered by Zapier zaps.
  name: Zapier
- description: Bubble Workflow API endpoints triggered by Make scenarios.
  name: Make (Integromat)
- description: AI-powered features via OpenAI plugin actions.
  name: OpenAI
- description: Outbound notifications and inbound webhooks for team collaboration.
  name: Slack
json_schemas:
- name: Bubble Data Search Response
  property_count: 1
  slug: bubble-data-search-response
- name: Bubble Data Thing
  property_count: 5
  slug: bubble-data-thing
- name: Bubble API Error
  property_count: 2
  slug: bubble-error
- name: Bubble Workflow Response
  property_count: 2
  slug: bubble-workflow-response
jsonld:
- class_count: 24
  name: Bubble Context
  property_count: 7
  slug: bubble-context
layout: provider
modified: '2026-05-19'
name: Bubble
nav: Providers
network: true
overview: 'Bubble publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Data API, Workflow API, Action API, and 3 more. Tagged areas include No-Code, Application Platform, Database, Workflow Automation, and Plugins.


  The Bubble catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bubble''s developer surface includes authentication, documentation, getting-started guide, API reference, pricing, signup flow, developer portal, and 48 more developer resources.'
plans:
- name: Bubble Plans Pricing
  plan_count: 7
  slug: bubble-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 12
  name: Bubble Rate Limits
  slug: bubble-rate-limits
rules:
- name: Bubble API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bubble-jsonschema-spectral-rules
- name: Bubble API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 6
  slug: bubble-rules
score:
  band: exemplar
  composite: 75.6
  delta: -4.7
  facets:
    commercial_clarity: 100.0
    contract_quality: 73.4
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 78.9
  previous_composite: 80.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bubble/refs/heads/main/screenshots/bubble-2026-06-20T173737.png
security:
- kind: authentication
  name: Bubble Authentication
  slug: bubble-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bubble Domain Security
  slug: bubble-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bubble Trust Center
  slug: bubble-trust-center
  summary_line: SOC 2, GDPR
slug: bubble
solutions:
- description: Ship a SaaS or marketplace MVP without hiring engineers; iterate with users in real time.
  name: For Founders
- description: White-label client apps with multi-app editor, version control, and sub-app architecture.
  name: For Agencies
- description: Dedicated infrastructure, SSO, custom rate limits, advanced security, and SLA-backed support.
  name: For Enterprise
- description: Build and publish plugins to the marketplace; extend Bubble apps with custom JavaScript actions and elements.
  name: For Developers
tags:
- No-Code
- Application Platform
- Database
- Workflow Automation
- Plugins
use_cases:
- description: Build admin dashboards, CRM panels, and operations consoles without engineering headcount.
  name: Internal Tools
- description: Two-sided marketplace MVPs with user roles, listings, search, and payments.
  name: Marketplaces
- description: Subscription-billed SaaS products with multi-tenant data, auth, and Stripe integration.
  name: SaaS MVPs
- description: Use a Bubble app as a managed backend for separately built mobile or web clients.
  name: Headless Backend
- description: Webhook ingestion and back-office automation triggered from third-party tools.
  name: Internal API Integrations
- description: Authenticated portals with privacy-rule-controlled data access and document upload.
  name: Customer Portals
website: https://bubble.io/
---
