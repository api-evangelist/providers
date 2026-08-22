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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 53
  human_in_the_loop: 0
  name: Ironclad Agentic Access
  operation_count: 98
  slug: ironclad-agentic-access
  summary_line: 98 operations · 53 acting
api_count: 13
apis:
- description: The Ironclad Clickwrap (formerly PactSafe) API delivers programmatic clickwrap and browsewrap acceptance tracking for online agreements — terms of service, privacy policies, EULAs, and checkout-flow a
  name: Ironclad Clickwrap API
  slug: ironclad-clickwrap-api
- description: OAuth 2.0 authorization endpoints for token management and user authentication.
  name: Ironclad Authorization API
  slug: ironclad-authorization-api
- description: Documentation on Ironclad Entities.
  name: Ironclad Entities API
  slug: ironclad-entities-api
- description: Documentation on Ironclad Data Exports.
  name: Ironclad Exports API
  slug: ironclad-exports-api
- description: Documentation on SCIM Groups.
  name: Ironclad Groups API
  slug: ironclad-groups-api
- description: Documentation on Ironclad Obligations.
  name: Ironclad Obligations API
  slug: ironclad-obligations-api
- description: Documentation on Ironclad Records.
  name: Ironclad Records API
  slug: ironclad-records-api
- description: Resource access endpoints for retrieving user information and token details.
  name: Ironclad Resources API
  slug: ironclad-resources-api
- description: Documentation on SCIM Schemas.
  name: Ironclad Schemas API
  slug: ironclad-schemas-api
- description: Documentation on Ironclad Search.
  name: Ironclad Search API
  slug: ironclad-search-api
- description: Documentation on SCIM Users.
  name: Ironclad Users API
  slug: ironclad-users-api
- description: Documentation on Ironclad Webhooks.
  name: Ironclad Webhooks API
  slug: ironclad-webhooks-api
- description: Documentation on Ironclad Workflows.
  name: Ironclad Workflows API
  slug: ironclad-workflows-api
arazzos:
- description: Retrieve a workflow, then pull its turn history and comment thread for audit.
  name: Ironclad Audit a Workflow's Activity
  slug: ironclad-audit-workflow-activity
- description: Retrieve a workflow, add an explanatory comment, then cancel the workflow.
  name: Ironclad Cancel a Workflow with an Audit Comment
  slug: ironclad-cancel-workflow-with-comment
- description: Resolve the records schema, create a contract record, then read it back.
  name: Ironclad Create and Retrieve a Contract Record
  slug: ironclad-create-and-retrieve-record
- description: List workflow documents, reorder the signature packet, then re-check sign status.
  name: Ironclad Curate a Signature Packet
  slug: ironclad-curate-signature-packet
- description: List workflow launch schemas, then launch a workflow against a chosen template.
  name: Ironclad Discover a Template and Launch a Workflow
  slug: ironclad-discover-and-launch-from-schema
- description: Launch a contract workflow synchronously, then read back its data and documents.
  name: Ironclad Launch and Track a Workflow
  slug: ironclad-launch-and-track-workflow
- description: Launch a workflow async, poll the create job to completion, then retrieve the workflow.
  name: Ironclad Launch a Workflow Asynchronously and Poll
  slug: ironclad-launch-workflow-async-poll
- description: Retrieve a workflow, pause it with a comment, then resume it with a comment.
  name: Ironclad Pause and Resume a Workflow
  slug: ironclad-pause-and-resume-workflow
- description: Create a webhook, retrieve it to confirm, then list all webhooks.
  name: Ironclad Register and Verify a Webhook
  slug: ironclad-register-and-verify-webhook
- description: Inspect a workflow's approvals and approval requests, then approve the active role.
  name: Ironclad Review and Approve a Workflow
  slug: ironclad-review-and-approve-workflow
- description: Read sign status, schedule the signature request for a future time, then re-read the workflow.
  name: Ironclad Schedule a Signature Send
  slug: ironclad-schedule-signature-send
- description: Read sign-step status, send the signature request, then confirm the packet documents.
  name: Ironclad Send a Workflow for Signature
  slug: ironclad-send-workflow-for-signature
- description: Find an existing webhook by target URL, retrieve it, then update its events.
  name: Ironclad Update a Webhook Subscription
  slug: ironclad-update-webhook-subscription
- description: Find a contract record by a filter and update it if found, otherwise create it.
  name: Ironclad Upsert a Contract Record
  slug: ironclad-upsert-contract-record
artifact_total: 105
collections:
- collection_type: postman
  name: Ironclad OAuth 2.0 API
  slug: postman-ironclad-oauth-20-api
- collection_type: postman
  name: Ironclad Public API
  slug: postman-ironclad-public-api
- collection_type: postman
  name: Ironclad SCIM API
  slug: postman-ironclad-scim-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization API
  slug: open-ironclad-authorization-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Entities API
  slug: open-ironclad-entities-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Exports API
  slug: open-ironclad-exports-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Groups API
  slug: open-ironclad-groups-api
- collection_type: open
  name: Ironclad OAuth 2.0 API
  slug: open-ironclad-oauth-20-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Obligations API
  slug: open-ironclad-obligations-api
- collection_type: open
  name: Ironclad Public API
  slug: open-ironclad-public-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Records API
  slug: open-ironclad-records-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Resources API
  slug: open-ironclad-resources-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Schemas API
  slug: open-ironclad-schemas-api
- collection_type: open
  name: Ironclad SCIM API
  slug: open-ironclad-scim-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Search API
  slug: open-ironclad-search-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Users API
  slug: open-ironclad-users-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Webhooks API
  slug: open-ironclad-webhooks-api
- collection_type: open
  name: Ironclad OAuth 2.0 Authorization Workflows API
  slug: open-ironclad-workflows-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ironclad-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/ironclad-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ironclad-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ironclad-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ironclad-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ironclad/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-audit-workflow-activity.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-cancel-workflow-with-comment.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-create-and-retrieve-record.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-curate-signature-packet.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-discover-and-launch-from-schema.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-launch-and-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-launch-workflow-async-poll.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-pause-and-resume-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-register-and-verify-webhook.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-review-and-approve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-schedule-signature-send.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-send-workflow-for-signature.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-update-webhook-subscription.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ironclad-upsert-contract-record.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.ironcladapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ironcladapp.com/reference/getting-started-api
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ironcladapp.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ironcladapp.com/reference
- group: auth
  title: ''
  type: Authentication
  url: https://developer.ironcladapp.com/reference/authentication-api
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.ironcladapp.com/reference/clm-api-rate-limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.ironcladapp.com/changelog/release-notes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ironcladapp.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ironclad
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ironclad/rivet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ironclad-inc-
- group: commercial
  title: ''
  type: Pricing
  url: https://ironcladapp.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ironcladapp.com/master-subscription-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ironcladapp.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://support.ironcladapp.com/
- group: company
  title: ''
  type: Blog
  url: https://ironcladapp.com/journal/
- group: commercial
  title: ''
  type: Plans
  url: plans/ironclad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ironclad-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ironclad-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/ironclad-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ironclad-vocabulary.yml
created: '2026-05-25'
description: Ironclad is the enterprise contract lifecycle management (CLM) platform used by legal, sales, procurement, and finance teams to draft, negotiate, approve, sign, store, and analyze contracts at scale. The platform combines a no-code Workflow Designer, AI-powered Jurist agentic assistant (contract review, redlining, drafting, repository search), a Records repository with smart import and metadata extraction, Clickwrap for online acceptance, and deep integrations with Salesforce, Microsoft 365, Slack, Workday, ServiceNow, Jira, HubSpot, NetSuite, Dynamics 365, and Power Automate. Ironclad publishes three first-party OpenAPI 3.1 specifications (Public API, OAuth 2.0, SCIM 2.0) plus the Clickwrap REST/JS surface, supports regional NA1/EU1 hosting, OAuth 2.0 with scoped tokens, SCIM-based provisioning, and event-driven webhooks. Ironclad reported surpassing $200M in ARR in February 2026.
examples:
- key_count: 2
  name: Ironclad Conversational Search Example
  slug: ironclad-conversational-search-example
- key_count: 2
  name: Ironclad Create Record Example
  slug: ironclad-create-record-example
- key_count: 2
  name: Ironclad Create Webhook Example
  slug: ironclad-create-webhook-example
- key_count: 2
  name: Ironclad Launch Workflow Example
  slug: ironclad-launch-workflow-example
features:
- description: Jurist agentic AI assistant reviews redlines, drafts clauses, summarizes contracts, and answers natural-language questions across the executed-contract repository.
  name: AI-Powered Contract Review
- description: Business users design contract workflows — conditional approvals, signature packets, counterparty negotiation, and CRM/ERP fanout — without engineering.
  name: No-Code Workflow Designer
- description: ML-driven metadata extraction that ingests legacy contract PDFs and predicts record metadata (counterparty, effective date, term length, renewal, obligations).
  name: Smart Import
- description: Centralized contract repository with versioned attachments, structured metadata, configurable schemas, and full-text + conversational search.
  name: Repository and Records
- description: Subscribe to workflow, record, and entity events for event-driven integration with downstream systems (CRM, ERP, ITSM, data warehouse).
  name: Webhooks
- description: Asynchronous bulk-export jobs deliver contract metadata and content to a data lake or warehouse — Snowflake, BigQuery, Databricks, Redshift.
  name: Data Exports
- description: Embed enforceable online acceptance flows (terms, EULAs, policies) into web, mobile, and checkout experiences with court-ready acceptance records.
  name: Clickwrap and Browsewrap
- description: First-class counterparty and entity records linked to workflows, records, and obligations, with reference-type modeling.
  name: Entity Management
- description: Extract and track post-signature commitments — renewal dates, SLAs, payment terms, regulatory deadlines.
  name: Obligation Tracking
- description: Standards-based authentication (Authorization Code + Client Credentials) and provisioning from any SCIM-compliant identity provider.
  name: OAuth 2.0 and SCIM 2.0
- description: North America (na1) and EU (eu1) hosting for data-residency compliance, plus a demo region for testing.
  name: Regional Hosting
- description: Optional Hold-Your-Own-Key (HYOK) encryption via Antimatter and GCP for the Security & Data Pro add-on.
  name: Per-Tenant Encryption
finops:
- name: Ironclad Finops
  service_category: Business Applications
  slug: ironclad-finops
graphqls:
- description: 'This conceptual GraphQL schema represents the Ironclad digital contracting platform API surface. Ironclad''s public REST API (base URL: `https://na1.ironcladapp.com/public/api/v1`) exposes contract lif'
  name: Ironclad GraphQL Schema
  slug: ironclad-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ironclad.png
integrations:
- description: Bi-directional CRM integration — launch workflows from opportunities, sync record fields, update opportunity stage on contract execution.
  name: Salesforce
- description: Native Word add-in for in-editor AI drafting, redlining, and clause comparison powered by Jurist.
  name: Microsoft Word
- description: Power Automate connector for low-code Microsoft 365 workflow orchestration.
  name: Microsoft 365 / Power Automate
- description: Bi-directional contract status and document sync with Dynamics 365.
  name: Microsoft Dynamics 365
- description: Procurement-process integration — request intake, approval routing, and contract record back-fill.
  name: ServiceNow
- description: Approval notifications, signature reminders, and contract-status messages in Slack.
  name: Slack
- description: Launch contract workflows from HubSpot deals via Tray.io connector.
  name: HubSpot
- description: Launch Ironclad workflows from Jira tickets and update Jira on contract progression (Zapier + Jira Automation patterns).
  name: Jira
- description: Sync vendor contracts and obligations with NetSuite via Tray.io.
  name: NetSuite
- description: 5,000+ app connector library via Zapier for low-code automation.
  name: Zapier
- description: Anypoint-Exchange connector for enterprise iPaaS integration.
  name: MuleSoft
- description: Smart-import contracts from Box folders into the Ironclad Records repository.
  name: Box
- description: Event-driven and bulk data-warehouse loads via the Data Exports surface.
  name: Snowflake / BigQuery / Databricks / Redshift
json_schemas:
- name: Ironclad Entity
  property_count: 8
  slug: ironclad-entity
- name: Ironclad Record
  property_count: 14
  slug: ironclad-record
- name: Ironclad SCIM User
  property_count: 9
  slug: ironclad-user
- name: Ironclad Webhook
  property_count: 0
  slug: ironclad-webhook
- name: Ironclad Workflow
  property_count: 17
  slug: ironclad-workflow
jsonld:
- class_count: 0
  name: Ironclad Context
  property_count: 6
  slug: ironclad-context
layout: provider
modified: '2026-05-25'
name: Ironclad
nav: Providers
network: true
overview: 'Ironclad publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Entities API, Exports API, and 9 more. Tagged areas include Contract Lifecycle Management, CLM, Contracts, Legal Tech, and LegalOps.


  The Ironclad catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ironclad''s developer surface includes authentication, developer portal, documentation, API reference, changelog, pricing, support, and 34 more developer resources.'
plans:
- name: Ironclad Plans Pricing
  plan_count: 5
  slug: ironclad-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Ironclad Rate Limits
  slug: ironclad-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Ironclad API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: ironclad-jsonschema-spectral-rules
- effective_rule_count: 76
  extends:
  - spectral:oas
  - spectral:asyncapi
  name: Ironclad API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: ironclad-rules
scopes:
- name: Ironclad Scopes
  scope_count: 60
  slug: ironclad-scopes
  summary_line: 60 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 57.8
  delta: -11.2
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 77.1
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 57.9
  previous_composite: 69.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ironclad/refs/heads/main/screenshots/ironclad-2026-06-20T183610.png
security:
- kind: authentication
  name: Ironclad Authentication
  slug: ironclad-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Ironclad Domain Security
  slug: ironclad-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ironclad Trust Center
  slug: ironclad-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR, CSA STAR
slug: ironclad
solutions:
- description: Core contract lifecycle management — workflows, records, repository, AI assistant.
  name: Ironclad CLM Platform
- description: Agentic AI for contract review, redlining, drafting, summarization, and conversational repository search.
  name: Jurist AI Assistant
- description: Online-agreement acceptance and acceptance-record management for terms, EULAs, and checkout flows.
  name: Ironclad Clickwrap
- description: Per-tenant encryption (HYOK via Antimatter or GCP) and elevated data-protection controls for regulated industries.
  name: Security & Data Pro
- description: Reporting, dashboards, and BI over contract metadata.
  name: Ironclad Insights
tags:
- Contract Lifecycle Management
- CLM
- Contracts
- Legal Tech
- LegalOps
- Enterprise
- Workflows
- eSignature
- Clickwrap
- AI
- OAuth
- SCIM
- Webhooks
use_cases:
- description: Salesforce-triggered NDA, MSA, and order-form workflows that fan out for legal approval, counterparty signature, and CRM record update.
  name: Sales Contract Automation
- description: Sync vendor onboarding, intake forms, and approval gating with procurement systems (Workday, NetSuite, Coupa, ServiceNow).
  name: Procurement Lifecycle
- description: Centralize matter-management, contract review queues, and clause libraries; offload first-pass review to Jurist AI.
  name: Legal Operations
- description: Offer letters, NDAs, separation agreements, and contractor agreements with conditional-routing approvals and esignature.
  name: HR and Employment Agreements
- description: Smart-import legacy PDF contracts into the structured Records repository with ML-extracted metadata.
  name: Repository Migration
- description: Embed clickwrap acceptance into SaaS sign-up, checkout, and policy-acknowledgement flows with court-ready evidence.
  name: Online Agreement Acceptance
- description: Surface renewal dates, payment milestones, SLAs, and regulatory commitments from executed contracts.
  name: Compliance and Obligation Management
- description: Run conversational queries ("show every MSA expiring in Q3 with auto-renew") across the contract repository using Jurist.
  name: AI-Augmented Repository Search
website: https://developer.ironcladapp.com/
---
