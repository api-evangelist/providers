---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - docs
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 87
  human_in_the_loop: 0
  name: Lawmatics Agentic Access
  operation_count: 177
  slug: lawmatics-agentic-access
  summary_line: 177 operations · 87 acting
api_count: 1
apis:
- description: An Address belongs to a Firm, a Contact, or Company.
  name: Lawmatics Addresses API
  slug: lawmatics-addresses-api
- description: The Collections API from Lawmatics — 4 operation(s) for collections.
  name: Lawmatics Collections API
  slug: lawmatics-collections-api
- description: The Companies API from Lawmatics — 5 operation(s) for companies.
  name: Lawmatics Companies API
  slug: lawmatics-companies-api
- description: 'A Contact can be thought of as a collection of data about a "Person". A Contact record is the base for all Contactables (Matters, Clients, and Companies). Since Contact data reflects a person, and is '
  name: Lawmatics Contacts API
  slug: lawmatics-contacts-api
- description: The Custom Emails API from Lawmatics — 2 operation(s) for custom emails.
  name: Lawmatics Custom Emails API
  slug: lawmatics-custom-emails-api
- description: The Custom Fields API from Lawmatics — 2 operation(s) for custom fields.
  name: Lawmatics Custom Fields API
  slug: lawmatics-custom-fields-api
- description: 'NOTE: Field IDs for fields that are not considered "Standard", such as General fields, and Custom fields, are referred to by special long-form uuids that are enumerated on the API details page of the '
  name: Lawmatics Custom Forms API
  slug: lawmatics-custom-forms-api
- description: A Email Address is contact information that belongs to a Firm, Contact, or Company.
  name: Lawmatics Email Addresses API
  slug: lawmatics-email-addresses-api
- description: The Email Campaign Stats API from Lawmatics — 1 operation(s) for email campaign stats.
  name: Lawmatics Email Campaign Stats API
  slug: lawmatics-email-campaign-stats-api
- description: The Email Campaigns API from Lawmatics — 2 operation(s) for email campaigns.
  name: Lawmatics Email Campaigns API
  slug: lawmatics-email-campaigns-api
- description: These are Firm related Locations (for events) that can be configured in Firm settings.
  name: Lawmatics Event Locations API
  slug: lawmatics-event-locations-api
- description: Event Types define Event defaults, and can trigger automations, for common types of Events created in Lawmatics. Configuring Calendar Availability defaults is not currently supported by the API. Go to
  name: Lawmatics Event Types API
  slug: lawmatics-event-types-api
- description: Events are also referred to in the app as "Appointments"
  name: Lawmatics Events (Appointments) API
  slug: lawmatics-events-appointments-api
- description: The Files API from Lawmatics — 3 operation(s) for files.
  name: Lawmatics Files API
  slug: lawmatics-files-api
- description: The Folders API from Lawmatics — 2 operation(s) for folders.
  name: Lawmatics Folders API
  slug: lawmatics-folders-api
- description: 'A Matter is a legal case, and the primary object in Lawmatics. NOTE: You may see Matters referenced as "Prospects" or "PNCs". This is for legacy reasons, and we are working to migrate away from these '
  name: Lawmatics Matters (Prospects) API
  slug: lawmatics-matters-prospects-api
- description: The Notes API from Lawmatics — 2 operation(s) for notes.
  name: Lawmatics Notes API
  slug: lawmatics-notes-api
- description: The Payment Expenses API from Lawmatics — 2 operation(s) for payment expenses.
  name: Lawmatics Payment Expenses API
  slug: lawmatics-payment-expenses-api
- description: The Payment Invoices API from Lawmatics — 2 operation(s) for payment invoices.
  name: Lawmatics Payment Invoices API
  slug: lawmatics-payment-invoices-api
- description: The Payment Time Entries API from Lawmatics — 2 operation(s) for payment time entries.
  name: Lawmatics Payment Time Entries API
  slug: lawmatics-payment-time-entries-api
- description: The Payment Transactions API from Lawmatics — 2 operation(s) for payment transactions.
  name: Lawmatics Payment Transactions API
  slug: lawmatics-payment-transactions-api
- description: A Phone Number is contact information that belongs to a Firm, Contact, or Company.
  name: Lawmatics Phone Numbers API
  slug: lawmatics-phone-numbers-api
- description: The Tags API from Lawmatics — 4 operation(s) for tags.
  name: Lawmatics Tags API
  slug: lawmatics-tags-api
- description: The Task Statuses API from Lawmatics — 2 operation(s) for task statuses.
  name: Lawmatics Task Statuses API
  slug: lawmatics-task-statuses-api
- description: The Tasks API from Lawmatics — 6 operation(s) for tasks.
  name: Lawmatics Tasks API
  slug: lawmatics-tasks-api
- description: The Timeline Activities API from Lawmatics — 2 operation(s) for timeline activities.
  name: Lawmatics Timeline Activities API
  slug: lawmatics-timeline-activities-api
- description: The Users API from Lawmatics — 3 operation(s) for users.
  name: Lawmatics Users API
  slug: lawmatics-users-api
artifact_total: 37
asyncapis:
- description: ''
  name: Lawmatics Webhooks
  slug: lawmatics-webhooks
collections:
- collection_type: postman
  name: Lawmatics OAuth API v1.22.0
  slug: postman-lawmatics-oauth-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lawmatics-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lawmatics-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lawmatics-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lawmatics-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/lawmatics-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lawmatics-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/lawmatics-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/lawmatics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lawmatics.com/security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lawmatics-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lawmatics-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lawmatics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lawmatics-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lawmatics-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lawmatics-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/lawmatics-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: postman/lawmatics-oauth-api.postman_collection.json
- group: company
  title: ''
  type: Website
  url: https://www.lawmatics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lawmatics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lawmatics.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.lawmatics.com/en/articles/10699983-lawmatics-open-api
- group: operate
  title: ''
  type: Support
  url: https://help.lawmatics.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boost-legal
- group: start
  title: ''
  type: Login
  url: https://app.lawmatics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lawmatics.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lawmatics.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.lawmatics.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lawmatics.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lawmatics.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lawmatics
- group: other
  title: ''
  type: X
  url: https://x.com/lawmatics
- group: commercial
  title: ''
  type: Plans
  url: plans/lawmatics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lawmatics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lawmatics-finops.yml
created: '2026-06-13'
description: Lawmatics is a legal CRM, client-intake and marketing-automation platform for law firms, from solo practices to multi-office firms. Its public developer surface is the Lawmatics OAuth API — a REST API of 177 operations across matters (called prospects in the API), contacts, companies, custom intake forms and form entries, custom fields, collections, pipelines, stages, practice areas, marketing sources and campaigns, events, tasks, notes, files, tags, users, time entries, expenses, invoices and transactions — plus a set of signed outbound webhooks. Access is OAuth 2.0 authorization code, gated on a Lawmatics support representative enabling developer settings on the account, and the resulting access token is non-expiring, unscoped and grants full CRUD over the firm.
finops:
- name: Lawmatics Finops
  service_category: ''
  slug: lawmatics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lawmatics.png
jsonld:
- class_count: 5
  name: Lawmatics Context
  property_count: 26
  slug: lawmatics-context
layout: provider
modified: '2026-08-13'
name: Lawmatics
nav: Providers
network: true
overview: 'Lawmatics publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Collections API, Companies API, and 24 more. Tagged areas include Legal, CRM, Law Firms, Client Intake, and Marketing Automation.


  The Lawmatics catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Lawmatics'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 28 more developer resources.'
plans:
- name: Lawmatics Plans Pricing
  plan_count: 3
  slug: lawmatics-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Lawmatics Rate Limits
  slug: lawmatics-rate-limits
scopes:
- name: Lawmatics Scopes
  scope_count: 0
  slug: lawmatics-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.3
  coverage:
    artifact_dirs: 26
    catalog_gap: 44.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 32.5
    developer_ergonomics: 54.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 27
      marker_coverage: 100.0
      total: 27
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lawmatics/refs/heads/main/screenshots/lawmatics-2026-06-20T184337.png
security:
- kind: authentication
  name: Lawmatics Authentication
  slug: lawmatics-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Lawmatics Domain Security
  slug: lawmatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lawmatics
tags:
- Legal
- CRM
- Law Firms
- Client Intake
- Marketing Automation
- Matter Management
- E-Signature
- Workflow-Automation
- Legal Tech
- Time and Billing
- Webhook
- Authentication
website: https://www.lawmatics.com/
---
