---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Filevine Agentic Access
  operation_count: 25
  slug: filevine-agentic-access
  summary_line: 25 operations · 14 acting
api_count: 9
apis:
- description: Exchange a Filevine Personal Access Token (PAT) for a short-lived bearer access token used to call the Filevine API Gateway. Tokens are issued at https://identity.filevine.io/connect/token with grant_
  name: Filevine Identity API
  slug: filevine-identity-api
- description: 'List, create, read, and update Filevine projects (matters/cases). Each project belongs to a project type, carries a primary client contact, has a phase, and a customizable set of sections and fields. '
  name: Filevine Projects API
  slug: filevine-projects-api
- description: Manage the global Filevine contact list and project-scoped contact attachments. Contacts represent clients, opposing parties, witnesses, experts, and adjusters with structured emails, phones, and orga
  name: Filevine Contacts API
  slug: filevine-contacts-api
- description: Upload, list, and read documents attached to Filevine projects. Documents support folders, tags, versioning, locking, and optional sharing to the secure client portal.
  name: Filevine Documents API
  slug: filevine-documents-api
- description: Append, edit, and read project notes and activity items. Notes carry a typed kind (note, task, portal message, phone call, text) and support @mentions, pinning, and attached documents.
  name: Filevine Notes API
  slug: filevine-notes-api
- description: Manage the date-driven legal milestones on a project — statutes of limitations, court dates, response deadlines — with assignees and reminder notifications. Deadlines can chain off a parent deadline.
  name: Filevine Deadlines API
  slug: filevine-deadlines-api
- description: List, create, and update assignable to-do items on a project with status, priority, due dates, and completion tracking. Tasks are produced by workflow automation and by direct user assignment.
  name: Filevine Tasks API
  slug: filevine-tasks-api
- description: Manage organization webhook subscriptions and receive event callbacks (project.created, project.updated, document.uploaded, note.created, deadline.created, task.completed, payment.created, payment.upd
  name: Filevine Webhooks API
  slug: filevine-webhooks-api
- description: Billable time tracking.
  name: Filevine TimeEntries API
  slug: filevine-timeentries-api
artifact_total: 82
asyncapis:
- description: Filevine emits webhook events to subscribed callback URLs when activity occurs in the platform. Subscriptions are configured per organization and select from a curated event catalog. Each subscription
  name: Filevine Webhook Events
  slug: filevine-events-asyncapi
collections:
- collection_type: postman
  name: Filevine Contacts API
  slug: postman-filevine-contacts-api
- collection_type: postman
  name: Filevine Contacts Deadlines API
  slug: postman-filevine-deadlines-api
- collection_type: postman
  name: Filevine Contacts Documents API
  slug: postman-filevine-documents-api
- collection_type: postman
  name: Filevine Contacts Identity API
  slug: postman-filevine-identity-api
- collection_type: postman
  name: Filevine Contacts Notes API
  slug: postman-filevine-notes-api
- collection_type: postman
  name: Filevine Contacts Projects API
  slug: postman-filevine-projects-api
- collection_type: postman
  name: Filevine Contacts Tasks API
  slug: postman-filevine-tasks-api
- collection_type: postman
  name: Filevine Contacts TimeEntries API
  slug: postman-filevine-timeentries-api
- collection_type: postman
  name: Filevine Contacts Webhooks API
  slug: postman-filevine-webhooks-api
- collection_type: open
  name: Filevine Contacts API
  slug: open-filevine-contacts-api
- collection_type: open
  name: Filevine Deadlines API
  slug: open-filevine-deadlines-api
- collection_type: open
  name: Filevine Documents API
  slug: open-filevine-documents-api
- collection_type: open
  name: Filevine Identity API
  slug: open-filevine-identity-api
- collection_type: open
  name: Filevine Notes API
  slug: open-filevine-notes-api
- collection_type: open
  name: Filevine Projects API
  slug: open-filevine-projects-api
- collection_type: open
  name: Filevine Tasks API
  slug: open-filevine-tasks-api
- collection_type: open
  name: Filevine Time Entries API
  slug: open-filevine-time-entries-api
- collection_type: open
  name: Filevine Webhooks API
  slug: open-filevine-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/filevine/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/filevine-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/filevine-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/filevine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/filevine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/filevine-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.filevine.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.filevine.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.filevine.io/docs/v2-us/branches/main/31e991e1bfac1-filevine-api-v2
- group: docs
  title: ''
  type: Documentation
  url: https://developer.filevine.io/docs/v2-ca/branches/main/31e991e1bfac1-filevine-api-v2
- group: docs
  title: ''
  type: Documentation
  url: https://support.filevine.com/hc/en-us/sections/28543097895835-API
- group: docs
  title: ''
  type: Documentation
  url: https://support.filevine.com/hc/en-us/articles/27944810461851-Authenticate-Requests-to-the-API-Gateway
- group: docs
  title: ''
  type: Documentation
  url: https://support.filevine.com/hc/en-us/articles/29259311975707-General-API-Q-A
- group: docs
  title: ''
  type: Documentation
  url: https://support.filevine.com/hc/en-us/articles/29937964706203-API-Authentication-Q-A
- group: docs
  title: ''
  type: Documentation
  url: https://support.filevine.com/hc/en-us/articles/13644331859611-Webhooks-Subscriptions
- group: docs
  title: ''
  type: Documentation
  url: https://support.filevine.com/hc/en-us/articles/18053591346331-Intraday-Data-Feed
- group: start
  title: ''
  type: Portal
  url: https://www.filevine.com/platform/case-management-software/
- group: docs
  title: ''
  type: Documentation
  url: https://www.filevine.com/platform/case-management-software/client-portal-software/
- group: docs
  title: ''
  type: Documentation
  url: https://www.filevine.com/features/docsplus/
- group: docs
  title: ''
  type: Documentation
  url: https://www.filevine.com/integrations/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.filevine.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://www.filevine.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.paramify.com/filevine
- group: company
  title: ''
  type: Blog
  url: https://www.filevine.com/blog/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.filevine.com/customers/
- group: company
  title: ''
  type: Jobs
  url: https://www.filevine.com/company/jobs/
- group: operate
  title: ''
  type: Support
  url: https://support.filevine.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://support.filevine.com/hc/en-us/articles/8671232852507-Status-Page
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.filevine.com/subscription-agreement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.filevine.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.filevine.com/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://www.filevine.com/subprocessors/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Filevine
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Filevine/filevine-api-examples
- group: build
  title: ''
  type: Tools
  url: https://github.com/Filevine/migration-helpers
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Filevine/fedramp20x-low-submission
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/filevine
- group: other
  title: ''
  type: X
  url: https://x.com/filevine
- group: commercial
  title: ''
  type: Plans
  url: plans/filevine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/filevine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/filevine-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/filevine-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/filevine-rules.yml
created: '2026-05-25'
description: Filevine is the leading legal case management and operating intelligence platform for plaintiff, personal-injury, mass-tort, family, immigration, criminal-defense, estate-planning, and government legal teams. The platform combines a customizable matter / project system with intake (Lead Docket), documents (Docs+), eSignature (Vinesign), contract management (Outlaw), deadline calendaring, time and billing, a secure client portal, and the LOIS Legal Operating Intelligence System for AI-assisted drafting, deposition prep, and case analysis. Filevine exposes a public REST API v2 with US and Canada gateways, PAT-based OAuth bearer authentication, and webhook subscriptions for event-driven integrations.
examples:
- key_count: 2
  name: Filevine Create Deadline Example
  slug: filevine-create-deadline-example
- key_count: 2
  name: Filevine Create Note Example
  slug: filevine-create-note-example
- key_count: 2
  name: Filevine Create Project Example
  slug: filevine-create-project-example
features:
- Matters / Projects — customizable per-practice-area templates with sections, custom fields, phases, and workflow automation
- Intake (Lead Docket) — lead capture, referrals, source tracking, conversion to matters
- LOIS — Legal Operating Intelligence System with Ask LOIS, LOIS for Word, AI Drafting, Depo CoPilot, Depo Summaries, MedChron, Phase Validation
- Docs+ — document storage, PDF editing, versioning, tags, folders, locking
- Vinesign — eSignature packets
- Outlaw — contract lifecycle management
- Client Portal — 24/7 case access, status updates, secure messaging
- Two-way SMS and captured email
- Timekeeping with context-aware timer, billable rates, expense tracking, invoice generation
- Deadlines and deadline chains with reminders
- Tasks with auto-assignment, priority, and completion tracking
- Periscope — analytics and reporting
- Timely — deadline calculation engine
- DataBridge — data integration platform
- REST API v2 with US (api.filevine.io) and Canada (api.filevineapp.ca) gateways
- PAT-based OAuth 2.0 bearer flow at https://identity.filevine.io/connect/token
- Webhook subscriptions for project, document, note, deadline, task, and payment events with signing keys
- Default rate limit of 320 req/min/endpoint; 250 req/min for billing endpoints; 5 req/min for report endpoints
- SOC 2 Type II (with HIPAA), CJIS 5.9.3/5.9.4, ISO 27001, HIPAA, GDPR, CCPA/CPRA, PCI DSS via Stripe
- FedRAMP Moderate authorization in progress; FIPS 140-3 in progress; ISO 27701/27017/27018 in progress
- AES-256 at rest, TLS 1.2/1.3 in transit, 2FA, RBAC, WAF, DDoS protection, public bug bounty
- Bilingual region support — US and Canada deployments
- Sample SDKs: C#, JavaScript, Python (Filevine/filevine-api-examples)
finops:
- name: Filevine Finops
  service_category: Legal Technology / Case Management
  slug: filevine-finops
graphqls:
- description: This conceptual GraphQL schema maps the Filevine REST API v2 surface onto a unified GraphQL type system. Filevine is a legal case management platform serving plaintiff law firms in personal injury, ma
  name: Filevine GraphQL Schema
  slug: filevine-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/filevine.png
integrations:
- description: Legal software with data insights and automated workflows for busy law firms.
  name: Lawmatics
- description: Court filing and process serving with smart document extraction synced to Filevine.
  name: InfoTrack
- description: Manage medical and billing record retrieval directly within Filevine.
  name: Record Retrieval Solutions
- description: Data transfer to Lead Docket and Filevine from inside Teams.
  name: Microsoft Teams
- description: Centralized client communication and call logging.
  name: Dialpad
- description: Physical mailing of letters and notices.
  name: DocuPost
- description: Personal injury settlement and lien resolution workflows.
  name: MoveDocs
- description: Copy and print cost tracking.
  name: Copitrak
- description: Postage and shipping integration.
  name: FedEx / Stamps
- description: Outlook Add-In for drag-and-drop email attachments into projects.
  name: Microsoft Outlook
- description: Custom Filevine API requests via Zapier custom request action.
  name: Zapier
json_schemas:
- name: Filevine Contact
  property_count: 9
  slug: filevine-contact
- name: Filevine Document
  property_count: 12
  slug: filevine-document
- name: Filevine Project
  property_count: 9
  slug: filevine-project
json_structures:
- name: Filevine Project Structure
  property_count: 10
  slug: filevine-project-structure
jsonld:
- class_count: 0
  name: Filevine Context
  property_count: 7
  slug: filevine-context
layout: provider
modified: '2026-05-25'
name: Filevine
nav: Providers
network: true
overview: 'Filevine publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Identity API, Projects API, Contacts API, and 6 more. Tagged areas include Legal, Case Management, Matters, Intake, and Documents.


  The Filevine catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Filevine''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, support, code examples, and 36 more developer resources.'
plans:
- name: Filevine Plans Pricing
  plan_count: 10
  slug: filevine-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 3
  name: Filevine Rate Limits
  slug: filevine-rate-limits
rules:
- name: Filevine API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: filevine-asyncapi-spectral-rules
- name: Filevine API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: filevine-jsonschema-spectral-rules
- name: Filevine API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: filevine-rules
score:
  band: strong
  composite: 62.8
  delta: -2.9
  facets:
    commercial_clarity: 78.9
    contract_quality: 78.4
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 52.1
    operational_transparency: 52.6
  previous_composite: 65.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/filevine/refs/heads/main/screenshots/filevine-2026-06-20T181208.png
security:
- kind: authentication
  name: Filevine Authentication
  slug: filevine-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Filevine Domain Security
  slug: filevine-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Filevine Vulnerability Disclosure
  slug: filevine-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Filevine Trust Center
  slug: filevine-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: filevine
tags:
- Legal
- Case Management
- Matters
- Intake
- Documents
- LOIS
- Webhooks
- Legal AI
- Personal Injury
- Mass Torts
website: https://www.filevine.com
---
