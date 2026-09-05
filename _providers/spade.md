---
access_model:
  confidence: high
  label: Contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.spade.com/pricing
  - https://docs.spade.com/reference/integrate-with-spades-api
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.7
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Spade Agentic Access
  operation_count: 73
  slug: spade-agentic-access
  summary_line: 73 operations · 51 acting
api_count: 1
apis:
- baseURL: https://east.api.spade.com
  baseurl_source: declared
  description: Enrich card transactions
  name: Spade Card Enrichment API
  slug: spade-card-enrichment-api
- baseURL: https://east.api.spade.com
  baseurl_source: declared
  description: Register category action triggers and receive triggered actions in enrichment responses
  name: Spade Category Action Triggers API
  slug: spade-category-action-triggers-api
- baseURL: https://east.api.spade.com
  baseurl_source: declared
  description: Create custom categories and personalize enrichments
  name: Spade Category Personalization API
  slug: spade-category-personalization-api
- baseURL: https://east.api.spade.com
  baseurl_source: declared
  description: Provide feedback on card events or report enrichment errors
  name: Spade Feedback and Reporting API
  slug: spade-feedback-and-reporting-api
- baseURL: https://east.api.spade.com
  baseurl_source: declared
  description: Register merchant action triggers and receive triggered actions in enrichment responses
  name: Spade Merchant Action Triggers API
  slug: spade-merchant-action-triggers-api
- baseURL: https://east.api.spade.com
  baseurl_source: declared
  description: Search for Spade merchants
  name: Spade Merchant Search API
  slug: spade-merchant-search-api
- baseURL: https://east.api.spade.com
  baseurl_source: declared
  description: Enrich transfers
  name: Spade Transfer Enrichment API
  slug: spade-transfer-enrichment-api
- baseURL: https://east.api.spade.com
  baseurl_source: declared
  description: The Universal Enrichment API from Spade — 3 operation(s) for universal enrichment.
  name: Spade Universal Enrichment API
  slug: spade-universal-enrichment-api
artifact_total: 25
asyncapis:
- description: ''
  name: Spade Webhooks
  slug: spade-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spade Card Enrichment API
  slug: open-spade-card-enrichment-api
- collection_type: open
  name: Spade Card Enrichment Category Action Triggers API
  slug: open-spade-category-action-triggers-api
- collection_type: open
  name: Spade Card Enrichment Category Personalization API
  slug: open-spade-category-personalization-api
- collection_type: open
  name: Spade Card Enrichment Feedback and Reporting API
  slug: open-spade-feedback-and-reporting-api
- collection_type: open
  name: Spade Card Enrichment Merchant Action Triggers API
  slug: open-spade-merchant-action-triggers-api
- collection_type: open
  name: Spade Card Enrichment Merchant Search API
  slug: open-spade-merchant-search-api
- collection_type: open
  name: Spade Card Enrichment Transfer Enrichment API
  slug: open-spade-transfer-enrichment-api
- collection_type: open
  name: Spade Card Enrichment Universal Enrichment API
  slug: open-spade-universal-enrichment-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/spade-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spade.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spade.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.spade.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spade.com/reference/integrate-with-spades-api
- group: operate
  title: ''
  type: Support
  url: https://www.spade.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spade.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spade.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spade.com/privacy
- group: operate
  title: ''
  type: SLA
  url: https://www.spade.com/sla
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.spade.com/changelog/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spade-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spade-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spade-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/spade-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spade-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spade-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spade-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spade-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/spade-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spade-webhooks.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spade-agentic-access.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spade-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.spade.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/spade-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spade-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.spade.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spade-domain-security.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spadeapi.com
- group: company
  title: ''
  type: Blog
  url: https://blog.spade.com
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/45578594-3ac97973-91ba-4d95-ad07-c058a347bddc
- group: agent
  title: ''
  type: WellKnown
  url: well-known/spade-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/spade-api-catalog.json
- group: other
  title: ''
  type: AgentCard
  url: a2a/spade-a2a.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spade-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/spade-plans-pricing.yml
created: '2026-07-17'
description: Spade is a real-time transaction enrichment and merchant intelligence platform for financial services. Its API transforms raw, messy card, transfer, and universal transaction records into clean, structured, verified merchant, location, and category data with sub-50ms latency. Fintechs, banks, and card issuers use Spade for authorization decisions, rewards attribution, recurring-payment detection, risk and fraud signals, spend analytics, and category personalization, plus merchant search and account/program/user/card-scoped action triggers. Spade operates east and west US sandbox and production environments and is SOC 2 Type II certified.
image: https://spadewp.wpenginepowered.com/wp-content/uploads/2025/07/OpenGraph.webp
layout: provider
modified: '2026-08-14'
name: Spade
nav: Providers
network: true
overview: 'Spade publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Card Enrichment API, Category Action Triggers API, Category Personalization API, and 5 more. Tagged areas include Company, Financial-Services, Transaction Enrichment, Merchant Intelligence, and Payments.


  The Spade catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spade''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, authentication, and 30 more developer resources.'
plans:
- name: Spade Plans Pricing
  plan_count: 3
  slug: spade-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Spade Rate Limits
  slug: spade-rate-limits
score:
  band: exemplar
  composite: 69.7
  coverage:
    artifact_dirs: 24
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 64.7
    developer_ergonomics: 69.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 69.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spade/refs/heads/main/screenshots/spade-2026-08-17T080423.png
security:
- kind: authentication
  name: Spade Authentication
  slug: spade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spade Domain Security
  slug: spade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spade Vulnerability Disclosure
  slug: spade-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Spade Trust Center
  slug: spade-trust-center
  summary_line: SOC 2 Type II
slug: spade
tags:
- Company
- Financial-Services
- Transaction Enrichment
- Merchant Intelligence
- Payments
- Data Enrichment
- Fraud and Risk
- Fintech
website: https://docs.spade.com
---
