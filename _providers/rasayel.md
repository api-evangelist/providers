---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Rasayel Agentic Access
  operation_count: 22
  slug: rasayel-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.rasayel.io/v1/
  baseurl_source: declared
  description: The Channels API from Rasayel — 1 operation(s) for channels.
  name: Rasayel Channels API
  slug: rasayel-channels-api
- baseURL: https://api.rasayel.io/v1/
  baseurl_source: declared
  description: The Contacts API from Rasayel — 5 operation(s) for contacts.
  name: Rasayel Contacts API
  slug: rasayel-contacts-api
- baseURL: https://api.rasayel.io/v1/
  baseurl_source: declared
  description: The Conversations API from Rasayel — 2 operation(s) for conversations.
  name: Rasayel Conversations API
  slug: rasayel-conversations-api
- baseURL: https://api.rasayel.io/v1/
  baseurl_source: declared
  description: The Messages API from Rasayel — 1 operation(s) for messages.
  name: Rasayel Messages API
  slug: rasayel-messages-api
- baseURL: https://api.rasayel.io/v1/
  baseurl_source: declared
  description: The Properties API from Rasayel — 2 operation(s) for properties.
  name: Rasayel Properties API
  slug: rasayel-properties-api
- baseURL: https://api.rasayel.io/v1/
  baseurl_source: declared
  description: The Tags API from Rasayel — 1 operation(s) for tags.
  name: Rasayel Tags API
  slug: rasayel-tags-api
- baseURL: https://api.rasayel.io/v1/
  baseurl_source: declared
  description: The Templates API from Rasayel — 2 operation(s) for templates.
  name: Rasayel Templates API
  slug: rasayel-templates-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rasayel REST Channels API
  slug: open-rasayel-channels-api
- collection_type: open
  name: Rasayel REST Channels Contacts API
  slug: open-rasayel-contacts-api
- collection_type: open
  name: Rasayel REST Channels Conversations API
  slug: open-rasayel-conversations-api
- collection_type: open
  name: Rasayel REST Channels Messages API
  slug: open-rasayel-messages-api
- collection_type: open
  name: Rasayel REST Channels Properties API
  slug: open-rasayel-properties-api
- collection_type: open
  name: Rasayel REST Channels Tags API
  slug: open-rasayel-tags-api
- collection_type: open
  name: Rasayel REST Channels Templates API
  slug: open-rasayel-templates-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/rasayel-rest-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rasayel-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rasayel-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rasayel-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rasayel-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rasayel-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rasayel.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rasayel-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rasayel-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rasayel-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rasayel-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rasayel-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rasayel-rest-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rasayel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rasayel-domain-security.yml
- group: build
  title: ''
  type: Postman
  url: https://rest.developers.rasayel.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.rasayel.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rasayel.io/
- group: docs
  title: ''
  type: APIReference
  url: https://rest.developers.rasayel.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rasayel.io/en/introduction
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.rasayel.io/
- group: company
  title: ''
  type: Blog
  url: https://learn.rasayel.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rasayel
- group: commercial
  title: ''
  type: Pricing
  url: https://rasayel.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.rasayel.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.rasayel.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.rasayel.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.rasayel.io/privacy
- group: company
  title: ''
  type: Website
  url: https://rasayel.io
created: '2026-07-17'
description: Rasayel is a WhatsApp platform for B2B sales teams. It combines a shared team inbox, workflow automation and lead qualification, chatbots and AI, WhatsApp message templates and Flows (forms), and campaign broadcasting, alongside CRM integrations (HubSpot, Pipedrive, Salesforce, Zoho) and Zapier. Its public REST API (api.rasayel.io/v1) and GraphQL API let developers manage contacts, message templates, conversations, tags, channels, and custom properties, and send WhatsApp messages programmatically using API-key authentication with Read and Read/Write scopes.
image: https://github.com/rasayel.png
layout: provider
modified: '2026-07-20'
name: Rasayel
nav: Providers
network: true
overview: 'Rasayel publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Channels API, Contacts API, Conversations API, and 4 more. Tagged areas include Company, WhatsApp, Messaging, Business Messaging, and Sales.


  Rasayel''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 23 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 1
  name: Rasayel Rate Limits
  slug: rasayel-rate-limits
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 15.5
    developer_ergonomics: 57.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rasayel/refs/heads/main/screenshots/rasayel-2026-08-17T081447.png
security:
- kind: authentication
  name: Rasayel Authentication
  slug: rasayel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rasayel Domain Security
  slug: rasayel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rasayel
tags:
- Company
- WhatsApp
- Messaging
- Business Messaging
- Sales
- CRM
- Customer Communication
- Conversational Commerce
website: https://rasayel.io
---
