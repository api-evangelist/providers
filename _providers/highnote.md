---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
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
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Highnote Agentic Access
  operation_count: 1
  slug: highnote-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://api.us.highnote.com/graphql
  baseurl_source: declared
  description: Single GraphQL endpoint for all Highnote operations.
  name: Highnote Graph QL API
  phrasing_intents:
  - id: postGraphql
    intent: Run a GraphQL query or mutation on Highnote
    question: How do I send a GraphQL query or mutation to the Highnote platform?
  phrasing_ops: 1
  slug: highnote-graph-ql-api
artifact_total: 18
asyncapis:
- description: Highnote delivers event notifications to registered HTTPS webhook notification targets (addWebhookNotificationTarget) via outbound POST. Subscribe a target to event types with addSubscriptionsToNotifi
  name: Highnote Event Notifications
  slug: highnote-events-asyncapi
collections:
- collection_type: postman
  name: Highnote GraphQL API
  slug: postman-highnote-graphql-api
- collection_type: open
  name: Highnote GraphQL API
  slug: open-highnote-graphql-api
- collection_type: open
  name: Highnote GraphQL API
  slug: open-highnote
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://highnote.com/blog/rss.xml
- group: agent
  href: https://artifacts.apis.io/highnote/skills/highnote-accept-a-payment.md
  title: ''
  type: AgentSkill
  url: skills/highnote-accept-a-payment.md
- group: docs
  title: ''
  type: APIReference
  url: https://docs.highnote.com/docs/tags/api
- group: build
  title: ''
  type: SDKs
  url: https://docs.highnote.com/docs/developers/sdks/about-sdks
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/highnote/overview
- group: agent
  href: https://artifacts.apis.io/highnote/agentic-access/highnote-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/highnote-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/highnote/security/highnote-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/highnote-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/highnote/authentication/highnote-authentication.yml
  title: ''
  type: Authentication
  url: authentication/highnote-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://highnote.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.highnote.com/docs/developers/about-developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.highnote.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Highnote-Platform
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/highnote-platform
- group: company
  title: ''
  type: Blog
  url: https://highnote.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://highnote.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://highnote.com/agreements/terms/01-05-22
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://highnote.com/agreements/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.highnote.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.highnote.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.highnote.com/docs/get-started/about-highnote
- group: start
  title: ''
  type: Signup
  url: https://dashboard.highnote.com
- group: commercial
  href: https://artifacts.apis.io/highnote/plans/highnote-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/highnote-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/highnote/rate-limits/highnote-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/highnote-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/highnote/finops/highnote-finops.yml
  title: ''
  type: FinOps
  url: finops/highnote-finops.yml
- group: build
  href: https://artifacts.apis.io/highnote/packages/highnote-packages.yml
  title: ''
  type: Packages
  url: packages/highnote-packages.yml
- group: build
  href: https://artifacts.apis.io/highnote/packages/highnote-packages.yml
  title: ''
  type: SDKs
  url: packages/highnote-packages.yml
- group: agent
  href: https://artifacts.apis.io/highnote/mcp/highnote-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/highnote-mcp.yml
- group: build
  href: https://artifacts.apis.io/highnote/mcp/highnote-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/highnote-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/highnote/llms/highnote-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/highnote-llms.txt
- group: agent
  href: https://artifacts.apis.io/highnote/well-known/highnote-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/highnote-well-known.yml
- group: other
  href: https://artifacts.apis.io/highnote/overlays/highnote-graphql-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/highnote-graphql-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/highnote/conformance/highnote-conformance.yml
  title: ''
  type: Conformance
  url: conformance/highnote-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.highnote.com/docs/get-started/introduction/pci-dss-compliance
- group: design
  href: https://artifacts.apis.io/highnote/errors/highnote-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/highnote-problem-types.yml
- group: build
  href: https://artifacts.apis.io/highnote/errors/highnote-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/highnote-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/highnote/lifecycle/highnote-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/highnote-lifecycle.yml
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://docs.highnote.com/docs/developers/api/status-changes
- group: design
  href: https://artifacts.apis.io/highnote/conventions/highnote-conventions.yml
  title: ''
  type: Conventions
  url: conventions/highnote-conventions.yml
- group: design
  href: https://artifacts.apis.io/highnote/conventions/highnote-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/highnote-conventions.yml
- group: operate
  href: https://artifacts.apis.io/highnote/changelog/highnote-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/highnote-changelog.yml
- group: start
  href: https://artifacts.apis.io/highnote/sandbox/highnote-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/highnote-sandbox.yml
- group: design
  href: https://artifacts.apis.io/highnote/components/highnote-components.yml
  title: ''
  type: Components
  url: components/highnote-components.yml
- group: design
  href: https://artifacts.apis.io/highnote/data-model/highnote-data-model.yml
  title: ''
  type: DataModel
  url: data-model/highnote-data-model.yml
- group: docs
  href: https://artifacts.apis.io/highnote/asyncapi/highnote-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/highnote-events-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/highnote/asyncapi/highnote-events-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/highnote-events-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/highnote/skills/_index.yml
  title: ''
  type: AgentSkills
  url: skills/_index.yml
created: '2026-06-20'
description: Highnote is a modern, unified embedded-finance and banking-as-a-service platform for card issuing, card acquiring, credit, and real-time money movement, with a built-in real-time programmable ledger and full program management. The entire platform is driven by a single GraphQL API at https://api.us.highnote.com/graphql (test https://api.us.test.highnote.com/graphql), authenticated with a base64-encoded API key over HTTP Basic auth. One endpoint covers card products, US person and business account holders (KYC/KYB onboarding), financial accounts and credit lines, virtual/physical/tokenized payment cards, transaction authorization and clearing, disputes, spend and velocity rules, collaborative authorization, multi-rail money movement (ACH, wire, RTP, push-to-card), and outbound webhook event notifications. Highnote is a US-based platform serving digital-first businesses embedding financial products; access is enterprise, contract-gated, with self-serve dashboard signup and a test
  environment.
finops:
- has_sources: true
  method: derived
  name: Highnote Finops
  primary_unit: transaction
  service_category: ''
  slug: highnote-finops
  template: false
graphqls:
- description: The [Highnote](https://highnote.com/) embedded-finance platform exposes a **single GraphQL
  name: Highnote GraphQL API
  slug: highnote-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/highnote.png
layout: provider
modified: '2026-10-06'
name: Highnote
nav: Providers
network: true
overview: 'Highnote publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Card Issuing, Card Acquiring, Embedded Finance, Banking as a Service, and Fintech.


  The Highnote catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Highnote''s developer surface includes API reference, authentication, documentation, engineering blog, pricing, support, getting-started guide, and 39 more developer resources.'
plans:
- name: Highnote Plans Pricing
  plan_count: 3
  slug: highnote-plans-pricing
- name: Highnote Price Estimates
  plan_count: 0
  slug: highnote-price-estimates
random_paper: 14
rate_limits:
- limit_count: 2
  name: Highnote Rate Limits
  slug: highnote-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Highnote API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: highnote-rules
score:
  band: exemplar
  composite: 69.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 58.5
    catalog_earned_first_party: 12.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 31.8
    contract_quality: 62.1
    developer_ergonomics: 74.4
    discoverability: 73.2
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 69.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/highnote/highnote-2026-06-20T182732.png
security:
- kind: authentication
  name: Highnote Authentication
  slug: highnote-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Highnote Domain Security
  slug: highnote-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: Accept and capture an acquiring card payment
  slug: highnote-accept-a-payment
- name: Onboard an account holder and issue a payment card
  slug: highnote-issue-a-card
- name: Move funds across rails
  slug: highnote-move-money
- name: Register a webhook target and subscribe to events
  slug: highnote-subscribe-to-events
slug: highnote
tags:
- Card Issuing
- Card Acquiring
- Embedded Finance
- Banking as a Service
- Fintech
- Payments
- GraphQL
- Ledger
- Credit
- Money Movement
- ACH
- KYC
- United States
website: https://highnote.com
---
