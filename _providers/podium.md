---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for managing customer communications including messaging, reviews, payments, webchat, contacts, automations, and webhooks for local businesses. Base URL is https://api.podium.com/v4/ and uses
  name: Podium API
  slug: podium-api
artifact_total: 21
asyncapis:
- description: ''
  name: Podium Webhooks
  slug: podium-webhooks
collections:
- collection_type: open
  name: Accounts
  slug: open-podium-accounts
- collection_type: open
  name: Appointments
  slug: open-podium-appointments
- collection_type: open
  name: Campaigns
  slug: open-podium-campaigns
- collection_type: open
  name: Contacts
  slug: open-podium-contacts
- collection_type: open
  name: Conversations
  slug: open-podium-conversations
- collection_type: open
  name: Feedback (Surveys)
  slug: open-podium-feedback-surveys
- collection_type: open
  name: Messenger
  slug: open-podium-messenger
- collection_type: open
  name: Payments
  slug: open-podium-payments
- collection_type: open
  name: Phones
  slug: open-podium-phones
- collection_type: open
  name: Products
  slug: open-podium-products
- collection_type: open
  name: Webhooks
  slug: open-podium-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.podium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.podium.com/reference/introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.podium.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/podium
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podiumhq/
- group: company
  title: ''
  type: Blog
  url: https://www.podium.com/resource-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.podium.com/getpricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.podium.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/podiumhq/
- group: commercial
  title: ''
  type: Plans
  url: plans/podium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/podium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/podium-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/podium-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/podium-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/podium-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/podium-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/podium-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/podium-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/podium-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/podium-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.podium.com
- group: start
  title: ''
  type: Sandbox
  url: sandbox/podium-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/podium-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/podium-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/podium-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/podium-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/podium-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://docs.podium.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.podium.com/docs/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/podium
- group: operate
  title: ''
  type: Support
  url: https://www.podium.com/knowledgebase/s
- group: start
  title: ''
  type: Login
  url: https://auth.podium.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.podium.com/#termsofservice-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.podium.com/#privacypolicy-us
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/podiumhq/podium-s-api-workspace
created: '2026-06-13'
description: Podium is a customer communication platform providing a REST API for local businesses to manage text-based conversations, reviews, payment requests, lead capture forms, webchat, and AI-driven lead conversion. The API is organized around REST with predictable resource-oriented URLs, JSON-encoded responses, and OAuth 2.0 authentication.
finops:
- name: Podium Finops
  service_category: ''
  slug: podium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podium.png
jsonld:
- class_count: 18
  name: Podium Context
  property_count: 3
  slug: podium-context
layout: provider
modified: '2026-08-14'
name: Podium
nav: Providers
network: true
overview: 'Podium publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Communication, Reviews, Messaging, Payments, and Webchat.


  The Podium catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Podium''s developer surface includes documentation, engineering blog, pricing, authentication, changelog, sandbox, API reference, and 30 more developer resources.'
plans:
- name: Podium Plans Pricing
  plan_count: 0
  slug: podium-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 1
  name: Podium Rate Limits
  slug: podium-rate-limits
scopes:
- name: Podium Scopes
  scope_count: 25
  slug: podium-scopes
  summary_line: 25 scopes · authorizationCode
score:
  band: strong
  composite: 57.5
  delta: -5.9
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 65.2
    developer_ergonomics: 43.5
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 43.4
  previous_composite: 63.4
  provenance:
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 65.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/podium/refs/heads/main/screenshots/podium-2026-06-20T191840.png
security:
- kind: authentication
  name: Podium Authentication
  slug: podium-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Podium Domain Security
  slug: podium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Podium Trust Center
  slug: podium-trust-center
  summary_line: trust center published
slug: podium
tags:
- Customer Communication
- Reviews
- Messaging
- Payments
- Webchat
- Local Business
- SMS
- Lead Generation
website: https://www.podium.com/
---
