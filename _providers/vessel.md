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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 304
  human_in_the_loop: 0
  name: Vessel Agentic Access
  operation_count: 376
  slug: vessel-agentic-access
  summary_line: 376 operations · 304 acting
api_count: 20
apis:
- description: The accounts API from Vessel — 7 operation(s) for accounts.
  name: Vessel Accounts API
  slug: vessel-accounts-api
- description: The Actions API from Vessel — 115 operation(s) for actions.
  name: Vessel Actions API
  slug: vessel-actions-api
- description: The attendees API from Vessel — 5 operation(s) for attendees.
  name: Vessel Attendees API
  slug: vessel-attendees-api
- description: The Auth API from Vessel — 6 operation(s) for auth.
  name: Vessel Auth API
  slug: vessel-auth-api
- description: The Connection API from Vessel — 1 operation(s) for connection.
  name: Vessel Connection API
  slug: vessel-connection-api
- description: The connections API from Vessel — 5 operation(s) for connections.
  name: Vessel Connections API
  slug: vessel-connections-api
- description: The contactCustomFields API from Vessel — 1 operation(s) for contactcustomfields.
  name: Vessel Contact Custom Fields API
  slug: vessel-contactcustomfields-api
- description: The contacts API from Vessel — 5 operation(s) for contacts.
  name: Vessel Contacts API
  slug: vessel-contacts-api
- description: The Crm API from Vessel — 9 operation(s) for crm.
  name: Vessel CRM API
  slug: vessel-crm-api
- description: The deals API from Vessel — 5 operation(s) for deals.
  name: Vessel Deals API
  slug: vessel-deals-api
- description: The emails API from Vessel — 5 operation(s) for emails.
  name: Vessel Emails API
  slug: vessel-emails-api
- description: The engAccounts API from Vessel — 2 operation(s) for engaccounts.
  name: Vessel Eng Accounts API
  slug: vessel-engaccounts-api
- description: The engAccountss API from Vessel — 1 operation(s) for engaccountss.
  name: Vessel Eng Accountss API
  slug: vessel-engaccountss-api
- description: The engActions API from Vessel — 3 operation(s) for engactions.
  name: Vessel Eng Actions API
  slug: vessel-engactions-api
- description: The engCalls API from Vessel — 2 operation(s) for engcalls.
  name: Vessel Eng Calls API
  slug: vessel-engcalls-api
- description: The engContacts API from Vessel — 3 operation(s) for engcontacts.
  name: Vessel Eng Contacts API
  slug: vessel-engcontacts-api
- description: The engCustomFields API from Vessel — 2 operation(s) for engcustomfields.
  name: Vessel Eng Custom Fields API
  slug: vessel-engcustomfields-api
- description: The engDispositions API from Vessel — 1 operation(s) for engdispositions.
  name: Vessel Eng Dispositions API
  slug: vessel-engdispositions-api
- description: The engEmails API from Vessel — 3 operation(s) for engemails.
  name: Vessel Eng Emails API
  slug: vessel-engemails-api
- description: The engMailboxes API from Vessel — 1 operation(s) for engmailboxes.
  name: Vessel Eng Mailboxes API
  slug: vessel-engmailboxes-api
- description: The engPassthrough API from Vessel — 1 operation(s) for engpassthrough.
  name: Vessel Eng Passthrough API
  slug: vessel-engpassthrough-api
- description: The engSequences API from Vessel — 4 operation(s) for engsequences.
  name: Vessel Eng Sequences API
  slug: vessel-engsequences-api
- description: The engTasks API from Vessel — 3 operation(s) for engtasks.
  name: Vessel Eng Tasks API
  slug: vessel-engtasks-api
- description: The engUsers API from Vessel — 2 operation(s) for engusers.
  name: Vessel Eng Users API
  slug: vessel-engusers-api
- description: The events API from Vessel — 5 operation(s) for events.
  name: Vessel Events API
  slug: vessel-events-api
- description: The integrations API from Vessel — 2 operation(s) for integrations.
  name: Vessel Integrations API
  slug: vessel-integrations-api
- description: The leadCustomFields API from Vessel — 1 operation(s) for leadcustomfields.
  name: Vessel Lead Custom Fields API
  slug: vessel-leadcustomfields-api
- description: The leads API from Vessel — 5 operation(s) for leads.
  name: Vessel Leads API
  slug: vessel-leads-api
- description: The links API from Vessel — 1 operation(s) for links.
  name: Vessel Links API
  slug: vessel-links-api
- description: The lists API from Vessel — 2 operation(s) for lists.
  name: Vessel Lists API
  slug: vessel-lists-api
- description: The notes API from Vessel — 5 operation(s) for notes.
  name: Vessel Notes API
  slug: vessel-notes-api
- description: The passthrough API from Vessel — 2 operation(s) for passthrough.
  name: Vessel Passthrough API
  slug: vessel-passthrough-api
- description: The tasks API from Vessel — 5 operation(s) for tasks.
  name: Vessel Tasks API
  slug: vessel-tasks-api
- description: The tokens API from Vessel — 1 operation(s) for tokens.
  name: Vessel Tokens API
  slug: vessel-tokens-api
- description: The Unifications API from Vessel — 107 operation(s) for unifications.
  name: Vessel Unifications API
  slug: vessel-unifications-api
- description: The users API from Vessel — 5 operation(s) for users.
  name: Vessel Users API
  slug: vessel-users-api
- description: The webhooks API from Vessel — 5 operation(s) for webhooks.
  name: Vessel Webhooks API
  slug: vessel-webhooks-api
artifact_total: 55
asyncapis:
- description: ''
  name: Vessel Webhooks
  slug: vessel-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vessel-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/vesselapi/all-api-docs/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/vesselapi/integrations/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vessel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vessel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vessel-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vesselapi
- group: company
  title: ''
  type: Website
  url: https://www.vessel.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vesselapi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/vesselapi/integrations
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vesselapi/client-sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@vesselapi/sdk
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@vesselapi/react-vessel-link
- group: company
  title: ''
  type: Blog
  url: https://www.vessel.dev/blog
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/vesselapi/all-api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/vesselapi/all-api-docs/tree/main/docs/pages
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/vesselapi/all-api-docs/blob/main/docs/pages/home/getting-started.mdx
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vessel.dev/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vessel.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drive.google.com/file/d/1MAhix9lfQdMW7B600vYeMNtdY3vnQzIQ/view
- group: operate
  title: ''
  type: Support
  url: https://www.vessel.dev/contact
- group: operate
  title: ''
  type: Roadmap
  url: https://vesselapi.canny.io/
- group: build
  title: ''
  type: Packages
  url: packages/vessel-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vessel-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vessel-crm-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/vessel-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vessel-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vessel-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vessel-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vessel-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vessel-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/vessel-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vessel-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vessel-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/vessel-list-crm-contacts-example.json
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vessel-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vessel-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vessel-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vessel-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/vessel-api-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vessel-contact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vessel-deal-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vessel-account-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/vessel-contact-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vessel-context.jsonld
- group: other
  title: ''
  type: Overlay
  url: overlays/vessel-platform-overlay.yaml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/vessel-jsonschema-spectral-rules.yml
created: '2026-05-03'
description: 'Vessel (Kinit Inc.) is a developer-first embedded integrations platform for go-to-market software. It gives a product team one contract to read and write an end customer''s CRM, sales engagement, chat, dialer and marketing automation tools, plus a drop-in browser component — Vessel Link — that handles the end user''s authorization so the host application never touches downstream credentials. Three modules sit on an open-source integrations library: Unification (one normalized schema per vertical), Actions (typed, validated wrappers over a single provider''s native API), and Managed ETL. An /api/passthrough endpoint forwards arbitrary authenticated requests for anything the modules do not cover. Vessel publishes 20 OpenAPI 3.1.0 definitions covering 376 operations in its own documentation repository. As of 2026-08-13 those contracts are still public but the operational surface is not: api.vessel.dev does not answer, api.vessel.land has no DNS record, and both docs.vessel.dev
  and app.vessel.dev are unreachable.'
examples:
- key_count: 5
  name: Vessel Get Session Token Example
  slug: vessel-get-session-token-example
- key_count: 5
  name: Vessel List Connections Example
  slug: vessel-list-connections-example
- key_count: 5
  name: Vessel List Crm Contacts Example
  slug: vessel-list-crm-contacts-example
- key_count: 5
  name: Vessel List Integrations Example
  slug: vessel-list-integrations-example
finops:
- name: Vessel Finops
  service_category: Unified API / Integrations
  slug: vessel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vessel.png
json_schemas:
- name: Account
  property_count: 13
  slug: vessel-account
- name: Contact
  property_count: 11
  slug: vessel-contact
- name: Deal
  property_count: 14
  slug: vessel-deal
json_structures:
- name: Vessel Contact Structure
  property_count: 0
  slug: vessel-contact-structure
jsonld:
- class_count: 9
  name: Vessel Context
  property_count: 20
  slug: vessel-context
layout: provider
modified: '2026-08-13'
name: Vessel
nav: Providers
network: true
overview: 'Vessel publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Actions API, Attendees API, and 34 more. Tagged areas include CRM, Chat, Dialer, Embedded Integrations, and Go-To-Market.


  The Vessel catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Vessel''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, support, and 41 more developer resources.'
plans:
- name: Vessel Plans Pricing
  plan_count: 3
  slug: vessel-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Vessel Rate Limits
  slug: vessel-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Vessel API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: vessel-api-rules
- effective_rule_count: 5
  extends: []
  name: Vessel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vessel-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 30
    catalog_gap: 17.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 87.9
    contract_quality: 72.3
    developer_ergonomics: 73.2
    discoverability: 68.5
    governance: 87.9
    operational_transparency: 50.0
  open_source:
    applies: true
    score: 0.0
  previous_composite: 65.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 95.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/screenshots/vessel-2026-06-20T200959.png
security:
- kind: authentication
  name: Vessel Authentication
  slug: vessel-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Vessel Domain Security
  slug: vessel-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vessel
tags:
- CRM
- Chat
- Dialer
- Embedded Integrations
- Go-To-Market
- Integration
- iPaaS
- Marketing Automation
- Sales Engagement
- Unified-API
- Webhook
website: https://www.vessel.dev/
---
