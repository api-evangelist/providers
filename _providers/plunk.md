---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Plunk Agentic Access
  operation_count: 14
  slug: plunk-agentic-access
  summary_line: 14 operations · 11 acting
api_count: 2
apis:
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Create and send marketing campaigns.
  name: Plunk Campaigns API
  slug: plunk-campaigns-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Manage contacts and their subscription state.
  name: Plunk Contacts API
  slug: plunk-contacts-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Track contact events that drive automations.
  name: Plunk Events API
  slug: plunk-events-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Send transactional email.
  name: Plunk Transactional API
  slug: plunk-transactional-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Public API endpoints for sending emails and tracking events
  name: Plunk Public API
  slug: plunk-public-api-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Audience segmentation
  name: Plunk Segments API
  slug: plunk-segments-api
- baseURL: https://api.useplunk.com/v1
  baseurl_source: declared
  description: Email template management
  name: Plunk Templates API
  slug: plunk-templates-api
artifact_total: 20
asyncapis:
- description: ''
  name: Plunk Webhooks
  slug: plunk-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Plunk Campaigns API
  slug: open-plunk-campaigns-api
- collection_type: open
  name: Plunk Campaigns Contacts API
  slug: open-plunk-contacts-api
- collection_type: open
  name: Plunk Campaigns Events API
  slug: open-plunk-events-api
- collection_type: open
  name: Plunk Campaigns Transactional API
  slug: open-plunk-transactional-api
- collection_type: open
  name: Plunk API
  slug: open-plunk
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/useplunk/plunk/blob/next/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plunk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plunk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plunk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useplunk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/useplunk
- group: company
  title: ''
  type: Website
  url: https://www.useplunk.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useplunk.com
- group: commercial
  title: ''
  type: Plans
  url: plans/plunk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plunk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/plunk-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/plunk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/plunk-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plunk-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/plunk-api-overlay.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/plunk-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/plunk-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plunk-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plunk-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.useplunk.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plunk-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plunk-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/plunk-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plunk-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.useplunk.com/dpa
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.useplunk.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useplunk.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.useplunk.com
- group: operate
  title: ''
  type: Support
  url: https://www.useplunk.com/discord
- group: commercial
  title: ''
  type: Pricing
  url: https://www.useplunk.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://next-app.useplunk.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://next-app.useplunk.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.useplunk.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.useplunk.com/privacy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/useplunk/plunk
created: '2026-06-20'
description: Plunk is an open-source (AGPL-3.0) email platform for developers that unifies transactional email, marketing campaigns, contact segmentation and event-driven workflow automation behind a single REST API. It publishes its own OpenAPI 3.1.0 at docs.useplunk.com/openapi.json, declaring next-api.useplunk.com as the production base URL, and authenticates with a two-class Bearer API key where the prefix decides capability — sk_ for every endpoint and pk_ for the client-safe /v1/track tracking call. The API supports Idempotency-Key on both public write endpoints, cursor pagination, a structured error envelope carrying machine codes plus remediation hints, and a documented webhook event catalogue delivered as workflow steps. Every documentation page is also served as Markdown. The entire stack self-hosts with Docker Compose for full data ownership and no per-email costs.
finops:
- name: Plunk Finops
  service_category: Email and Messaging
  slug: plunk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plunk.png
layout: provider
modified: '2026-08-13'
name: Plunk
nav: Providers
network: true
overview: 'Plunk publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contacts API, Events API, and 4 more. Tagged areas include Email, Transactional Email, Marketing, Automation, and Open-Source.


  The Plunk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Plunk''s developer surface includes authentication, documentation, changelog, API reference, getting-started guide, support, pricing, and 29 more developer resources.'
plans:
- name: Plunk Plans Pricing
  plan_count: 3
  slug: plunk-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Plunk Rate Limits
  slug: plunk-rate-limits
score:
  band: exemplar
  composite: 68.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 69.5
    developer_ergonomics: 64.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 73.7
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plunk/refs/heads/main/screenshots/plunk-2026-06-20T191814.png
security:
- kind: authentication
  name: Plunk Authentication
  slug: plunk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plunk Domain Security
  slug: plunk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: plunk
tags:
- Email
- Transactional Email
- Marketing
- Automation
- Open-Source
- Software-as-a-Service
- Email API
- Webhook
- Segmentation
- Workflow-Automation
- Self-Hosted
- Developer Tools
website: https://www.useplunk.com
---
