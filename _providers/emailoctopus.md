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
- acting_count: 15
  human_in_the_loop: 0
  name: Emailoctopus Agentic Access
  operation_count: 25
  slug: emailoctopus-agentic-access
  summary_line: 25 operations · 15 acting
api_count: 2
apis:
- description: Enqueue an existing contact into an EmailOctopus automation. Write-only — the v2 API exposes no operation to list or read automations, so the automation id must come from the dashboard. 1 operation(s)
  name: EmailOctopus Automation API
  slug: emailoctopus-automation-api
- description: 'Read campaigns and their three report projections — summary counters, per-link clicks, and per-contact engagement rows. Read-only: campaigns cannot be created, scheduled or sent through the v2 API. 5 '
  name: EmailOctopus Campaign API
  slug: emailoctopus-campaign-api
- description: 'Manage subscribers on a list: create, read, update, delete, upsert by email address, and update many at once through the batch endpoint. The upsert (PUT /lists/{list_id}/contacts) is the safe-retry pa'
  name: EmailOctopus Contact API
  slug: emailoctopus-contact-api
- description: 'Define the per-list custom fields contact records are written against. Fields are keyed by a stable tag slug and typed text, number or date, with optional choices and a fallback value. 3 operation(s) '
  name: EmailOctopus Field API
  slug: emailoctopus-field-api
- description: 'Create and manage subscriber lists, the aggregate root of the EmailOctopus data model. Fields, tags and contacts are all owned by a list and addressed through list-scoped paths. 5 operation(s) in the '
  name: EmailOctopus List API
  slug: emailoctopus-list-api
- description: Create, rename, delete and list the tags used to segment contacts on a list. Tags are keyed by slug rather than an id. 4 operation(s) in the EmailOctopus v2 OpenAPI 3.1.0.
  name: EmailOctopus Tag API
  slug: emailoctopus-tag-api
artifact_total: 21
asyncapis:
- description: ''
  name: Emailoctopus Webhooks
  slug: emailoctopus-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: EmailOctopus v2 Automation API
  slug: open-emailoctopus-automation-api
- collection_type: open
  name: EmailOctopus v2 Automation Campaign API
  slug: open-emailoctopus-campaign-api
- collection_type: open
  name: EmailOctopus v2 Automation Contact API
  slug: open-emailoctopus-contact-api
- collection_type: open
  name: EmailOctopus v2 Automation Field API
  slug: open-emailoctopus-field-api
- collection_type: open
  name: EmailOctopus v2 Automation List API
  slug: open-emailoctopus-list-api
- collection_type: open
  name: EmailOctopus v2 Automation Tag API
  slug: open-emailoctopus-tag-api
- collection_type: open
  name: EmailOctopus v2 API
  slug: open-emailoctopus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/emailoctopus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/emailoctopus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/emailoctopus-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emailoctopus
- group: company
  title: ''
  type: Website
  url: https://emailoctopus.com
- group: docs
  title: ''
  type: Documentation
  url: https://emailoctopus.com/api-documentation/v2
- group: commercial
  title: ''
  type: Plans
  url: plans/emailoctopus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/emailoctopus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/emailoctopus-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/emailoctopus-v2-openapi.json
- group: build
  title: ''
  type: Packages
  url: packages/emailoctopus-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/emailoctopus-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/emailoctopus-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/emailoctopus-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/emailoctopus-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/emailoctopus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/emailoctopus-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emailoctopus.com
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/emailoctopus-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Components
  url: components/emailoctopus-components.yml
- group: docs
  title: ''
  type: APIReference
  url: https://emailoctopus.com/api-documentation/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://emailoctopus.com/api-documentation/v2#section/Authentication
- group: operate
  title: ''
  type: Support
  url: https://help.emailoctopus.com
- group: company
  title: ''
  type: Blog
  url: https://emailoctopus.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://emailoctopus.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://emailoctopus.com/account/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emailoctopus.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emailoctopus.com/legal/privacy
created: '2026-06-25'
description: EmailOctopus is an affordable email-marketing platform for newsletters, campaigns, automations and audience management, built on a low-cost sending model that undercuts the incumbent ESPs. Its v2 REST API is served from a single host, https://api.emailoctopus.com, with no version segment in the path, and is authenticated with a Bearer API key. The API covers subscriber lists, contacts, per-list custom fields and tags, campaigns and three campaign report projections, plus an operation to enqueue a contact into an automation. EmailOctopus publishes a real OpenAPI 3.1.0 document (25 operations, 19 schemas) at its v2 reference URL, documents an RFC 7807 error envelope with dereferenceable type URIs, cursor pagination, a token-bucket rate limit of 10 requests per second with a burst of 100, and an HMAC-SHA256-signed webhook surface carrying eight contact event types. It ships no official client SDK, no CLI and no MCP server.
finops:
- name: Emailoctopus Finops
  service_category: Marketing and Communications
  slug: emailoctopus-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/emailoctopus.png
layout: provider
modified: '2026-08-13'
name: EmailOctopus
nav: Providers
network: true
overview: 'EmailOctopus publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Automation API, Campaign API, Contact API, and 3 more. Tagged areas include Email, Email Marketing, Newsletters, Campaigns, and Automation.


  The EmailOctopus catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EmailOctopus'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Emailoctopus Plans Pricing
  plan_count: 3
  slug: emailoctopus-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Emailoctopus Rate Limits
  slug: emailoctopus-rate-limits
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 65.6
    developer_ergonomics: 54.2
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/emailoctopus/refs/heads/main/screenshots/emailoctopus-2026-07-25T213222.png
security:
- kind: authentication
  name: Emailoctopus Authentication
  slug: emailoctopus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Emailoctopus Domain Security
  slug: emailoctopus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: emailoctopus
tags:
- Email
- Email Marketing
- Newsletters
- Campaigns
- Automation
- Contacts
- List
- Marketing
- Webhook
- Transactional Email
- Subscriber Management
- Reporting
website: https://emailoctopus.com
---
