---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Bubbles Agentic Access
  operation_count: 8
  slug: bubbles-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 1
apis:
- description: 'The Bubble Data API allows external services to read, create, update, and delete data stored in Bubble apps via REST endpoints. The API supports authentication via API keys and exposes app data types '
  name: Bubble Data API
  slug: bubble-data-api
- description: The Bubble Workflow API enables external systems to trigger backend workflows in a Bubble app via HTTP requests. Workflows can receive data, execute business logic, and return results, supporting inte
  name: Bubble Workflow API
  slug: bubble-workflow-api
- baseURL: https://{app-name}.bubbleapps.io/api/1.1
  baseurl_source: declared
  description: Generic CRUD operations against your Bubble application data types.
  name: Bubble Data API
  slug: bubbles-data-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bubble Data API
  slug: open-bubbles-data-api
- collection_type: open
  name: Bubble Data API
  slug: open-bubbles
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bubbles-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bubbles-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bubbles-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bubbles-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bubble-hq
- group: company
  title: ''
  type: Website
  url: https://bubble.io
- group: start
  title: ''
  type: Portal
  url: https://manual.bubble.io/core-resources/api
- group: docs
  title: ''
  type: Documentation
  url: https://manual.bubble.io
- group: start
  title: ''
  type: GettingStarted
  url: https://manual.bubble.io/core-resources/api
- group: commercial
  title: ''
  type: Pricing
  url: https://bubble.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bubble.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bubble.io/privacy
- group: start
  title: ''
  type: Signup
  url: https://bubble.io/signup
- group: start
  title: ''
  type: Login
  url: https://bubble.io/login
- group: operate
  title: ''
  type: Forums
  url: https://forum.bubble.io
- group: company
  title: ''
  type: Blog
  url: https://bubble.io/blog
created: '2024-11-13'
description: Bubble is an AI-powered no-code development platform that enables individuals and teams to design and launch scalable web applications without writing code. Bubble provides a visual programming environment for building database-backed applications, marketplaces, SaaS tools, and enterprise applications. The platform includes API connector capabilities for integrating with external services via REST APIs, webhooks, and data APIs to expose app data programmatically.
finops:
- name: Bubbles Finops
  service_category: API
  slug: bubbles-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bubbles.png
layout: provider
modified: '2026-04-21'
name: Bubble
nav: Providers
network: true
overview: 'Bubble publishes 1 API on the [APIs.io](https://apis.io/) network: Data API. Tagged areas include Application, Low-Code, No-Code, Visual Programming, and Webhook.


  Bubble''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Bubbles Plans Pricing
  plan_count: 3
  slug: bubbles-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Bubbles Rate Limits
  slug: bubbles-rate-limits
score:
  band: developing
  composite: 40.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bubbles/refs/heads/main/screenshots/bubbles-2026-06-20T173737.png
security:
- kind: authentication
  name: Bubbles Authentication
  slug: bubbles-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bubbles Domain Security
  slug: bubbles-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Bubbles Trust Center
  slug: bubbles-trust-center
  summary_line: SOC 2, GDPR
slug: bubbles
tags:
- Application
- Low-Code
- No-Code
- Visual Programming
- Webhook
- Web App
website: https://bubble.io
---
