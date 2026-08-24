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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.5
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Plunk Agentic Access
  operation_count: 14
  slug: plunk-agentic-access
  summary_line: 14 operations · 11 acting
api_count: 5
apis:
- description: Plunk's own published OpenAPI 3.1.0, served at https://docs.useplunk.com/openapi.json and declaring https://next-api.useplunk.com as the production base URL. Covers the public API (transactional send,
  name: Plunk API
  slug: plunk-api
- description: Create and send marketing campaigns.
  name: Plunk Campaigns API
  slug: plunk-campaigns-api
- description: Manage contacts and their subscription state.
  name: Plunk Contacts API
  slug: plunk-contacts-api
- description: Track contact events that drive automations.
  name: Plunk Events API
  slug: plunk-events-api
- description: Send transactional email.
  name: Plunk Transactional API
  slug: plunk-transactional-api
artifact_total: 18
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
overview: 'Plunk publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contacts API, and 3 more. Tagged areas include Email, Transactional Email, Marketing, Automation, and Open-Source.


  The Plunk catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Plunk''s developer surface includes authentication, documentation, changelog, API reference, getting-started guide, support, pricing, and 28 more developer resources.'
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
  composite: 71.1
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 30.3
    contract_quality: 74.2
    developer_ergonomics: 63.7
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 73.7
  previous_composite: 71.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
