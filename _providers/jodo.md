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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://ext.jodo.in
  baseurl_source: declared
  description: Event delivery surface for the Jodo platform. Jodo POSTs 36 documented events across student master data, manual payments, Flex subscriptions/mandates/instalments, Pay collections and Cred education l
  name: Jodo Webhooks
  slug: jodo-webhooks
- baseURL: https://ext.jodo.in
  baseurl_source: declared
  description: Institute reference data (branches, grades, fee components, discounts) and webhook subscriptions.
  name: Jodo Configuration API
  slug: jodo-configuration-api
- baseURL: https://ext.jodo.in
  baseurl_source: declared
  description: Flexible instalment plans backed by an auto-debit mandate.
  name: Jodo Flex API
  slug: jodo-flex-api
- baseURL: https://ext.jodo.in
  baseurl_source: declared
  description: Checkout orders and shareable hosted payment links.
  name: Jodo Pay API
  slug: jodo-pay-api
- baseURL: https://ext.jodo.in
  baseurl_source: declared
  description: Student master data, fee structures and manual payment reconciliation.
  name: Jodo Students API
  slug: jodo-students-api
- baseURL: https://ext.jodo.in
  baseurl_source: declared
  description: Register ERP/institute users and mint short-lived tokens for Jodo-hosted flows.
  name: Jodo Users API
  slug: jodo-users-api
artifact_total: 11
asyncapis:
- description: Jodo delivers state changes for students, manual payments, Flex instalment plans, Pay collections and Cred education loans as HTTP POST webhooks to a URL the institute registers per event_code. PROVEN
  name: Jodo Webhooks
  slug: jodo-webhooks-asyncapi
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/jodo-integrations-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.jodo.in/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.jodo.in/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jodo.in/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.jodo.in/getting-started/api-structure/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.jodo.in/getting-started/introduction/
- group: auth
  title: ''
  type: Authentication
  url: authentication/jodo-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/jodo-sandbox.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jodo.in/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/jodo-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jodo-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jodo-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/jodo-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jodo-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jodo-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jodo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jodo-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/jodo-packages.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/jodo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jodo-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jodo-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.jodo.in/
- group: company
  title: ''
  type: Blog
  url: https://www.jodo.in/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jodohq
- group: operate
  title: ''
  type: Support
  url: https://www.jodo.in/contact-us/
- group: start
  title: ''
  type: Login
  url: https://app.jodo.in/institute/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jodo.in/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jodo.in/privacy-policy/
created: '2026-08-23'
description: 'Jodo is a Bengaluru-based fintech that automates fee collection for Indian educational institutes — schools, colleges, universities, coaching centres and skilling institutes. Founded in 2020 by Atulya Bhat, Raghav Nagarajan and Koustav Dey, the company says it serves 5,000+ institutes across 90+ cities and has processed over INR 30,000 crore in fees for 25 lakh+ students. Jodo ships three products on one platform: Flex (structured fees paid in instalments through an auto-debit mandate), Pay (student-linked collections, hosted checkout orders and shareable payment links) and Cred (education loans originated with NBFC lending partners). Its public ERP Integrations API lets an institute''s ERP, finance or student-information system register users and students, sync fee structures and discounts, reconcile manual payments, configure instalment schedules, create checkout orders and payment links, and manage webhook subscriptions. Jodo publishes a substantial developer reference at
  docs.jodo.in covering 25 REST operations and 36 webhook events, with documented UAT and production environments, Basic Auth, an error code registry, a retry and idempotency policy, HMAC SHA-256 webhook signatures and published source IP ranges — but no machine-readable OpenAPI or AsyncAPI document, and no public pricing.'
image: https://www.jodo.in/assets/images/icons/favicon.png
layout: provider
modified: '2026-08-23'
name: Jodo
nav: Providers
network: true
overview: 'Jodo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Configuration API, Flex API, and 3 more. Tagged areas include Company, Payments, Education, Fintech, and Fee Collection.


  The Jodo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Jodo''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, support, and 22 more developer resources.'
plans:
- name: Jodo Plans Pricing
  plan_count: 0
  slug: jodo-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Jodo Rate Limits
  slug: jodo-rate-limits
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 4.5
    contract_quality: 24.7
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 40.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jodo/refs/heads/main/screenshots/jodo-2026-09-02T145951.png
security:
- kind: authentication
  name: Jodo Authentication
  slug: jodo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jodo Domain Security
  slug: jodo-domain-security
  summary_line: TLSv1.3
slug: jodo
tags:
- Company
- Payments
- Education
- Fintech
- Fee Collection
- Lending
- India
- Webhook
- ERP Integration
- Financial-Services
website: https://www.jodo.in/
---
