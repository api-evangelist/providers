---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Live, versioned HTTP event-ingest API behind the Black Crow AI JavaScript tag. POST /v1/events/{event_name} accepts a JSON body identified by siteName, pageId and visitorId and carries the visit, purc
  name: Black Crow AI Events API
  slug: black-crow-ai-events-api
- description: Client-side JavaScript API exposed by the Black Crow AI tag as window.blackcrow. Brands push a binding ({app_name 'audience', bind 'scores_update', callback}) to receive Black Crow's real-time visitor
  name: Black Crow AI Global API
  slug: black-crow-ai-global-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/black-crow-ai-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/black-crow-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.blackcrow.ai/legal/security-policy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/black-crow-ai-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/black-crow-ai-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/black-crow-ai-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/black-crow-ai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/black-crow-ai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/black-crow-ai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/black-crow-ai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/black-crow-ai-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/black-crow-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/black-crow-ai-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/black-crow-ai-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/black-crow-ai-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/black-crow-ai-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/black-crow-ai-plans-pricing.yml
- group: docs
  title: ''
  type: Documentation
  url: https://blackcrow.zendesk.com/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://blackcrow.zendesk.com/hc/en-us/articles/46541281990043-Getting-Started-with-Black-Crow-Storefronts-Onboarding
- group: company
  title: ''
  type: Blog
  url: https://www.blackcrow.ai/resources
- group: operate
  title: ''
  type: Support
  url: https://blackcrow.zendesk.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://www.blackcrow.ai/demo
- group: start
  title: ''
  type: Login
  url: https://app.blackcrow.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.blackcrow.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackcrow.ai/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/october8ai
- group: company
  title: ''
  type: Website
  url: https://www.blackcrow.ai/
created: '2026-07-17'
description: Black Crow AI is an ecommerce AI company that turns paid advertising traffic into predictable revenue using AI-generated post-click Storefronts. Storefronts are shopping experiences built specifically for paid ad traffic, kept aligned with ad creative and audience intent, generated in minutes through a no-code workflow, and optimized through structured split-test experimentation and continuous learning. Black Crow also exposes a script-based "Global API" callback that surfaces its real-time visitor prediction scores (delivered in under 20 milliseconds) so brands can ingest scores into any target platform. Surfaced as a portfolio company of Bloomberg Beta and enriched into the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/black-crow-ai.png
layout: provider
modified: '2026-08-12'
name: Black Crow AI
nav: Providers
network: true
overview: 'Black Crow AI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Artificial Intelligence, Machine-Learning, and Marketing.


  Black Crow AI''s developer surface includes authentication, sandbox, documentation, getting-started guide, engineering blog, support, signup flow, and 20 more developer resources.'
plans:
- name: Black Crow Ai Plans Pricing
  plan_count: 0
  slug: black-crow-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Black Crow Ai Rate Limits
  slug: black-crow-ai-rate-limits
score:
  band: thin
  composite: 30.4
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 30.4
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/black-crow-ai/refs/heads/main/screenshots/black-crow-ai-2026-07-25T203228.png
security:
- kind: authentication
  name: Black Crow Ai Authentication
  slug: black-crow-ai-authentication
  summary_line: none/session · 3 schemes
- kind: domain-security
  name: Black Crow Ai Domain Security
  slug: black-crow-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Black Crow Ai Vulnerability Disclosure
  slug: black-crow-ai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: black-crow-ai
tags:
- Company
- E-Commerce
- Artificial Intelligence
- Machine-Learning
- Marketing
- Advertising
- Personalization
- Conversion Optimization
- Analytics
- Event Ingest
- Tag Management
- Shopify
website: https://www.blackcrow.ai/
---
