---
access_model:
  confidence: high
  label: Paid per card · Self-serve signup · Unbilled test mode
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Handwrite Io Agentic Access
  operation_count: 4
  slug: handwrite-io-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: Available handwriting styles
  name: Handwrite IO Handwriting API
  slug: handwrite-io-handwriting-api
- description: Order tracking and status
  name: Handwrite IO Orders API
  slug: handwrite-io-orders-api
- description: Send handwritten notes
  name: Handwrite IO Send API
  slug: handwrite-io-send-api
- description: Available stationery and cards
  name: Handwrite IO Stationery API
  slug: handwrite-io-stationery-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Handwrite IO Handwriting API
  slug: open-handwrite-io-handwriting-api
- collection_type: open
  name: Handwrite IO Handwriting Orders API
  slug: open-handwrite-io-orders-api
- collection_type: open
  name: Handwrite IO Handwriting Send API
  slug: open-handwrite-io-send-api
- collection_type: open
  name: Handwrite IO Handwriting Stationery API
  slug: open-handwrite-io-stationery-api
- collection_type: open
  name: Handwrite IO API
  slug: open-handwrite-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/handwrite-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/handwrite-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/handwrite-io-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/handwrite-io-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/handwrite-io-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/handwrite-io-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/handwrite-io-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/handwrite-io-finops.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/handwrite-io-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/handwrite-io-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/handwrite-io-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/handwrite-io-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/handwrite-io-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/handwrite-io-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.handwrite.io/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.handwrite.io/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.handwrite.io/#endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.handwrite.io/#getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/handwriteio
- group: operate
  title: ''
  type: Support
  url: https://www.handwrite.io/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.handwrite.io/faq
- group: company
  title: ''
  type: Blog
  url: https://www.handwrite.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.handwrite.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.handwrite.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.handwrite.io/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/handwrite
- group: company
  title: ''
  type: Website
  url: https://handwrite.io/
created: '2024-11-14'
description: 'Handwrite is a South Carolina based direct-mail service that writes and mails real handwritten cards on demand, and exposes that fulfillment as a small REST API at https://api.handwrite.io/v1. Four operations cover the whole surface: list the handwriting styles on the account, list the stationery and card options, send a card to between one and ten US recipients (or up to 1,000 orders in a single batch request), and fetch an order to follow it from processing through written to complete and retrieve proof images of the finished card and envelope. Authentication is a single static API key sent raw in the Authorization header, prefixed test_hw for unbilled test-mode calls or live_hw for calls that actually mail and bill. Pricing is per mailed card rather than per API call, from $2.99 down to $2.45 by volume, with the card, envelope, handwriting and postage included. The API is rate limited to 60 requests per minute per key. Handwrite also ships a Zapier integration for teams
  that do not want to write code.'
finops:
- name: Handwrite Io Finops
  service_category: API
  slug: handwrite-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/handwrite-io.png
layout: provider
modified: '2026-08-13'
name: Handwrite IO
nav: Providers
network: true
overview: 'Handwrite IO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Handwriting API, Orders API, Send API, and 1 more. Tagged areas include Direct Mail, Handwritten, Handwritten Notes, Cards, and Marketing.


  The Handwrite IO catalog on APIs.io includes 1 Spectral governance ruleset.


  Handwrite IO''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Handwrite Io Plans Pricing
  plan_count: 5
  slug: handwrite-io-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Handwrite Io Rate Limits
  slug: handwrite-io-rate-limits
rules:
- effective_rule_count: 41
  extends:
  - spectral:oas
  name: Handwrite IO API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: handwrite-io-rules
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 33.3
    contract_quality: 55.8
    developer_ergonomics: 55.4
    discoverability: 68.5
    governance: 33.3
    operational_transparency: 23.7
  previous_composite: 50.7
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/handwrite-io/refs/heads/main/screenshots/handwrite-io-2026-06-20T182501.png
security:
- kind: authentication
  name: Handwrite Io Authentication
  slug: handwrite-io-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Handwrite Io Domain Security
  slug: handwrite-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: handwrite-io
tags:
- Direct Mail
- Handwritten
- Handwritten Notes
- Cards
- Marketing
- Notes
- Print
- Fulfillment
- Customer Engagement
website: https://handwrite.io/
---
