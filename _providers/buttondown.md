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
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 71
  human_in_the_loop: 0
  name: Buttondown Agentic Access
  operation_count: 133
  slug: buttondown-agentic-access
  summary_line: 133 operations · 71 acting
api_count: 1
apis:
- description: The Accounts API from Buttondown — 1 operation(s) covering the authenticated account and its plan/feature state.
  name: Buttondown Accounts API
  slug: buttondown-accounts-api
- description: The Advertising Units API from Buttondown — 6 operation(s) covering newsletter sponsorship inventory — advertising units and the slots sold against them.
  name: Buttondown Advertising Units API
  slug: buttondown-advertising-units-api
- description: The API Requests API from Buttondown — 2 operation(s) covering the account's own API request log, including retained response bodies for idempotent requests.
  name: Buttondown API Requests API
  slug: buttondown-api-requests-api
- description: The Attachments API from Buttondown — 4 operation(s) covering files attached to emails and inbox replies.
  name: Buttondown Attachments API
  slug: buttondown-attachments-api
- description: The Automations API from Buttondown — 7 operation(s) covering triggered and scheduled email sequences, their actions, timing and analytics.
  name: Buttondown Automations API
  slug: buttondown-automations-api
- description: The Books API from Buttondown — 5 operation(s) covering the Bookshop.org book catalog embedded in newsletters.
  name: Buttondown Books API
  slug: buttondown-books-api
- description: The Bulk Actions API from Buttondown — 2 operation(s) covering asynchronous mass operations over existing records.
  name: Buttondown Bulk Actions API
  slug: buttondown-bulk-actions-api
- description: The Comments API from Buttondown — 5 operation(s) covering subscriber comments on emails, and their moderation state.
  name: Buttondown Comments API
  slug: buttondown-comments-api
- description: The Coupons API from Buttondown — 1 operation(s) covering Stripe coupons available to a paid newsletter.
  name: Buttondown Coupons API
  slug: buttondown-coupons-api
- description: The Emails API from Buttondown — 11 operation(s) covering drafting, scheduling, publishing, rendering and analyzing newsletter emails.
  name: Buttondown Emails API
  slug: buttondown-emails-api
- description: The Events API from Buttondown — 2 operation(s) covering the unified event store that also powers webhooks.
  name: Buttondown Events API
  slug: buttondown-events-api
- description: The Exports API from Buttondown — 3 operation(s) covering data exports of subscribers, emails and events.
  name: Buttondown Exports API
  slug: buttondown-exports-api
- description: The External Feeds API from Buttondown — 7 operation(s) covering RSS-to-email feeds, their polling cadence and the items they produce.
  name: Buttondown External Feeds API
  slug: buttondown-external-feeds-api
- description: The Forms API from Buttondown — 5 operation(s) covering hosted and embeddable subscription forms.
  name: Buttondown Forms API
  slug: buttondown-forms-api
- description: The Images API from Buttondown — 4 operation(s) covering images hosted for use in emails and archives.
  name: Buttondown Images API
  slug: buttondown-images-api
- description: The Imports API from Buttondown — 5 operation(s) covering bulk subscriber imports — the supported path for adding subscribers at volume.
  name: Buttondown Imports API
  slug: buttondown-imports-api
- description: The Newsletters API from Buttondown — 7 operation(s) covering newsletter settings, branding, locale, and custom sending/hosting domain verification.
  name: Buttondown Newsletters API
  slug: buttondown-newsletters-api
- description: The Notes API from Buttondown — 3 operation(s) covering internal notes attached to subscribers and team members.
  name: Buttondown Notes API
  slug: buttondown-notes-api
- description: The Ping API from Buttondown — 1 operation(s) covering a connectivity and credential health check.
  name: Buttondown Ping API
  slug: buttondown-ping-api
- description: The Prices API from Buttondown — 3 operation(s) covering paid-subscription pricing and products.
  name: Buttondown Prices API
  slug: buttondown-prices-api
- description: The Public API from Buttondown — 1 operation(s) covering the unauthenticated public archive search.
  name: Buttondown Public API
  slug: buttondown-public-api
- description: The Segments API from Buttondown — 5 operation(s) covering saved, reusable audiences built from tag and metadata filters.
  name: Buttondown Segments API
  slug: buttondown-segments-api
- description: The Snippets API from Buttondown — 5 operation(s) covering reusable content snippets referenced from emails.
  name: Buttondown Snippets API
  slug: buttondown-snippets-api
- description: The Subscribers API from Buttondown — 12 operation(s) covering subscriber lifecycle — creation, updates, tags, referrals, automations and Stripe subscriptions.
  name: Buttondown Subscribers API
  slug: buttondown-subscribers-api
- description: The Survey Responses API from Buttondown — 3 operation(s) covering responses collected from newsletter surveys.
  name: Buttondown Survey Responses API
  slug: buttondown-survey-responses-api
- description: The Surveys API from Buttondown — 5 operation(s) covering surveys embedded in emails and on the archive.
  name: Buttondown Surveys API
  slug: buttondown-surveys-api
- description: The Tags API from Buttondown — 6 operation(s) covering subscriber tags and their analytics.
  name: Buttondown Tags API
  slug: buttondown-tags-api
- description: The Users API from Buttondown — 5 operation(s) covering team members on the account and their permissions.
  name: Buttondown Users API
  slug: buttondown-users-api
- description: The Webhooks API from Buttondown — 7 operation(s) covering webhook registration, delivery attempts, and test fires.
  name: Buttondown Webhooks API
  slug: buttondown-webhooks-api
- description: The Buttondown hosted newsletter platform provides a markdown-based composition experience, subscriber management, delivery infrastructure, analytics, monetization via paid subscriptions, team collabo
  name: Buttondown Newsletter Platform
  slug: newsletter-platform
- description: The Buttondown Webhooks API API from Buttondown — 0 operation(s) for buttondown webhooks api.
  name: Buttondown Buttondown Webhooks API
  slug: buttondown-buttondown-webhooks-api-api
artifact_total: 71
asyncapis:
- description: ''
  name: Buttondown Webhooks
  slug: buttondown-webhooks
collections:
- collection_type: open
  name: Buttondown Accounts API
  slug: open-buttondown-accounts-api
- collection_type: open
  name: Buttondown Advertising Units API
  slug: open-buttondown-advertising-units-api
- collection_type: open
  name: Buttondown API Requests API
  slug: open-buttondown-api-requests-api
- collection_type: open
  name: Buttondown Attachments API
  slug: open-buttondown-attachments-api
- collection_type: open
  name: Buttondown Automations API
  slug: open-buttondown-automations-api
- collection_type: open
  name: Buttondown Books API
  slug: open-buttondown-books-api
- collection_type: open
  name: Buttondown Bulk Actions API
  slug: open-buttondown-bulk-actions-api
- collection_type: open
  name: Buttondown Comments API
  slug: open-buttondown-comments-api
- collection_type: open
  name: Buttondown Coupons API
  slug: open-buttondown-coupons-api
- collection_type: open
  name: Buttondown Emails API
  slug: open-buttondown-emails-api
- collection_type: open
  name: Buttondown Events API
  slug: open-buttondown-events-api
- collection_type: open
  name: Buttondown Exports API
  slug: open-buttondown-exports-api
- collection_type: open
  name: Buttondown External Feeds API
  slug: open-buttondown-external-feeds-api
- collection_type: open
  name: Buttondown Forms API
  slug: open-buttondown-forms-api
- collection_type: open
  name: Buttondown Images API
  slug: open-buttondown-images-api
- collection_type: open
  name: Buttondown Imports API
  slug: open-buttondown-imports-api
- collection_type: open
  name: Buttondown Newsletters API
  slug: open-buttondown-newsletters-api
- collection_type: open
  name: Buttondown Notes API
  slug: open-buttondown-notes-api
- collection_type: open
  name: Buttondown Ping API
  slug: open-buttondown-ping-api
- collection_type: open
  name: Buttondown Prices API
  slug: open-buttondown-prices-api
- collection_type: open
  name: Buttondown public API
  slug: open-buttondown-public-api
- collection_type: open
  name: Buttondown Segments API
  slug: open-buttondown-segments-api
- collection_type: open
  name: Buttondown Snippets API
  slug: open-buttondown-snippets-api
- collection_type: open
  name: Buttondown Subscribers API
  slug: open-buttondown-subscribers-api
- collection_type: open
  name: Buttondown Survey Responses API
  slug: open-buttondown-survey-responses-api
- collection_type: open
  name: Buttondown Surveys API
  slug: open-buttondown-surveys-api
- collection_type: open
  name: Buttondown Tags API
  slug: open-buttondown-tags-api
- collection_type: open
  name: Buttondown Users API
  slug: open-buttondown-users-api
- collection_type: open
  name: Buttondown Webhooks API
  slug: open-buttondown-webhooks-api
- collection_type: open
  name: Buttondown API
  slug: open-buttondown
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/buttondown-openapi.json
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/buttondown-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/buttondown-authentication.yml
- group: auth
  title: ''
  type: API Keys
  url: https://buttondown.com/keys
- group: design
  title: ''
  type: Conventions
  url: conventions/buttondown-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/buttondown-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/buttondown-error-codes.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/buttondown-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buttondown-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/buttondown-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/buttondown-finops.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/buttondown-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/buttondown-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/buttondown-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.buttondown.com/api-versioning
- group: design
  title: ''
  type: Versioning
  url: https://docs.buttondown.com/api-versioning
- group: operate
  title: ''
  type: StatusPage
  url: https://status.buttondown.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/buttondown-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/buttondown-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/buttondown-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/buttondown-sandbox.yml
- group: build
  title: ''
  type: Examples
  url: examples/buttondown-fixtures.json
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/buttondown-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/buttondown-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/buttondown-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/buttondown-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://buttondown.com/blog/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buttondown-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/buttondown-llms.txt
- group: company
  title: ''
  type: Website
  url: https://buttondown.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.buttondown.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.buttondown.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.buttondown.com/api-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.buttondown.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://buttondown.com/support
- group: company
  title: ''
  type: Blog
  url: https://buttondown.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/buttondown
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/buttondown/openapi
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buttondown
- group: commercial
  title: ''
  type: Pricing
  url: https://buttondown.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://buttondown.com/register
- group: start
  title: ''
  type: Login
  url: https://buttondown.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buttondown.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buttondown.com/legal/privacy
created: '2026-04-23'
description: Buttondown is an independent, bootstrapped email newsletter platform for writers, creators and developers, offering a Markdown and rich-text editor, subscriber management with tags, segments and metadata, automations, RSS-to-email, surveys, comments, paid subscriptions via Stripe with no revenue share, custom sending and hosting domains, and hosted archives. Its public REST API covers 133 operations across 29 resource areas — subscribers, emails, tags, segments, automations, webhooks, imports, exports, surveys, forms, images, snippets, prices and more — described by a live OpenAPI 3.1 document, backed by an 82-event webhook catalog, a date-based version train, idempotency keys, and a first-party CLI for syncing newsletter content to a local folder.
examples:
- key_count: 48
  name: Buttondown Enums
  slug: buttondown-enums
- key_count: 51
  name: Buttondown Fixtures
  slug: buttondown-fixtures
finops:
- name: Buttondown Finops
  service_category: API
  slug: buttondown-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buttondown.png
layout: provider
modified: '2026-08-13'
name: Buttondown
nav: Providers
network: true
overview: 'Buttondown publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Advertising Units API, API Requests API, and 27 more. Tagged areas include Analytics, Automations, Email, Markdown, and Newsletters.


  The Buttondown catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Buttondown''s developer surface includes authentication, changelog, CLI, sandbox, code examples, documentation, API reference, and 38 more developer resources.'
plans:
- name: Buttondown Plans Pricing
  plan_count: 2
  slug: buttondown-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Buttondown Rate Limits
  slug: buttondown-rate-limits
score:
  band: exemplar
  composite: 68.2
  coverage:
    artifact_dirs: 26
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 4.5
    contract_quality: 70.5
    developer_ergonomics: 73.2
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 92.1
  previous_composite: 68.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/buttondown/refs/heads/main/screenshots/buttondown-2026-06-20T173820.png
security:
- kind: authentication
  name: Buttondown Authentication
  slug: buttondown-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Buttondown Domain Security
  slug: buttondown-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Buttondown Vulnerability Disclosure
  slug: buttondown-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: buttondown
tags:
- Analytics
- Automations
- Email
- Markdown
- Newsletters
- Paid Subscriptions
- Software-as-a-Service
- Subscribers
- Webhook
- Segmentation
- Developer Tools
- Marketing
website: https://buttondown.com/
---
