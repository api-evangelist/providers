---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 13
  name: Justt Agentic Access
  operation_count: 23
  slug: justt-agentic-access
  summary_line: 23 operations · 13 acting · 13 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Chargebacks API from Justt — 4 operation(s) for chargebacks.
  name: Justt Chargebacks API
  slug: justt-chargebacks-api
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Data Subjects API from Justt — 1 operation(s) for data subjects.
  name: Justt Data Subjects API
  slug: justt-data-subjects-api
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Evidence API from Justt — 2 operation(s) for evidence.
  name: Justt Evidence API
  slug: justt-evidence-api
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Files API from Justt — 1 operation(s) for files.
  name: Justt Files API
  slug: justt-files-api
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Integrations API from Justt — 2 operation(s) for integrations.
  name: Justt Integrations API
  slug: justt-integrations-api
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Merchants API from Justt — 2 operation(s) for merchants.
  name: Justt Merchants API
  slug: justt-merchants-api
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Pre-chargeback Alerts API from Justt — 3 operation(s) for pre-chargeback alerts.
  name: Justt Pre-chargeback Alerts API
  slug: justt-pre-chargeback-alerts-api
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Sandbox API from Justt — 1 operation(s) for sandbox.
  name: Justt Sandbox API
  slug: justt-sandbox-api
- baseURL: https://api.justt.ai/v1
  baseurl_source: declared
  description: The Transactions API from Justt — 1 operation(s) for transactions.
  name: Justt Transactions API
  slug: justt-transactions-api
arazzos:
- description: 'Pull pre-chargeback alerts from Ethoca / Verifi, read one, and report its outcome back to Justt using the alert networks'' own outcome vocabulary. Note the read operations and the write operation live '
  name: Work a Justt pre-chargeback alert to a reported outcome
  slug: justt-alert-to-outcome
- description: Create a test chargeback from raw Stripe dispute data in the sandbox, advance it to under_review, then resolve it as won — firing a webhook at each transition so an integration can be validated end to
  name: Drive a chargeback through its lifecycle in the Justt sandbox
  slug: justt-sandbox-lifecycle
- description: Read an open chargeback, upload an evidence file, submit it to the PSP, and poll the asynchronous submission to a terminal state.
  name: Submit evidence for a Justt chargeback
  slug: justt-submit-evidence
- description: 'List open chargebacks, enrich one with additional merchant data, and override whether Justt should represent it. Acceptance is deliberately NOT part of this workflow — it is irreversible and requires '
  name: Triage Justt chargebacks and set the representment decision
  slug: justt-triage-and-decide
artifact_total: 27
asyncapis:
- description: ''
  name: Justt Webhook Events
  slug: justt-webhook-events
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://justt.ai/feed/
- group: other
  href: https://artifacts.apis.io/justt/capabilities/justt-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/justt-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/justt/agentic-access/justt-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/justt-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/justt/security/justt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/justt-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/justt/authentication/justt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/justt-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://justt.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.justt.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.justt.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.justt.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.justt.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developers.justt.ai/docs/contact-us
- group: company
  title: ''
  type: Blog
  url: https://justt.ai/blog/
- group: start
  title: ''
  type: Login
  url: https://app.justt.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://justt.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://justt.ai/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.justt.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.justt.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.justt.ai/
- group: other
  href: https://artifacts.apis.io/justt/well-known/justt-well-known.yml
  title: ''
  type: APICatalog
  url: well-known/justt-well-known.yml
- group: agent
  href: https://artifacts.apis.io/justt/well-known/justt-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/justt-well-known.yml
- group: agent
  href: https://artifacts.apis.io/justt/mcp/justt-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/justt-mcp.yml
- group: build
  href: https://artifacts.apis.io/justt/mcp/justt-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/justt-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/justt/llms/justt-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/justt-llms.txt
- group: other
  href: https://artifacts.apis.io/justt/overlays/justt-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/justt-rest-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/justt/conformance/justt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/justt-conformance.yml
- group: design
  href: https://artifacts.apis.io/justt/errors/justt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/justt-problem-types.yml
- group: design
  href: https://artifacts.apis.io/justt/lifecycle/justt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/justt-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.justt.ai/docs/legacy-api-to-rest-api-migration-guide
- group: auth
  href: https://artifacts.apis.io/justt/scopes/justt-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/justt-scopes.yml
- group: start
  href: https://artifacts.apis.io/justt/sandbox/justt-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/justt-sandbox.yml
- group: design
  href: https://artifacts.apis.io/justt/conventions/justt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/justt-conventions.yml
- group: design
  href: https://artifacts.apis.io/justt/data-model/justt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/justt-data-model.yml
- group: design
  href: https://artifacts.apis.io/justt/asyncapi/justt-webhook-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/justt-webhook-events.yml
- group: agent
  href: https://artifacts.apis.io/justt/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/justt/plans/justt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/justt-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/justt/rate-limits/justt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/justt-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/justt/arazzo/_index.yml
  title: ''
  type: Arazzo
  url: arazzo/_index.yml
created: '2026-08-23'
description: Justt is an AI-native chargeback management and dispute-representment platform for high-volume merchants. Its Dynamic Arguments engine assembles evidence-backed representment packages for card disputes across 30+ payment service providers (Stripe, Adyen, PayPal, Braintree, Checkout.com, Worldpay, Chase Paymentech, Nuvei and others), and it also handles pre-chargeback alerts from Ethoca, Verifi CDRN and RDR. Justt publishes a public developer portal at developers.justt.ai with three OpenAPI definitions — a REST API for chargebacks, transactions, evidence, files, merchants and integrations; a Pre-Chargeback Alerts API; and an OpenAPI 3.1 webhook-events specification covering eleven signed event types — plus an RFC 9727 /.well-known/api-catalog, an llms.txt documentation index, a sandbox environment, and a Vanta-hosted trust center.
finops:
- has_sources: true
  method: derived
  name: Justt Finops
  primary_unit: ''
  service_category: ''
  slug: justt-finops
  template: true
image: https://justt.ai/wp-content/uploads/2025/03/blog-7-1.jpg
layout: provider
modified: '2026-10-06'
name: Justt
nav: Providers
network: true
overview: 'Justt publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Chargebacks API, Data Subjects API, Evidence API, and 6 more. Tagged areas include Company, Payments, Chargebacks, Disputes, and Fraud Prevention.


  The Justt catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Justt''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 30 more developer resources.'
plans:
- name: Justt Plans Pricing
  plan_count: 0
  slug: justt-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Justt Rate Limits
  slug: justt-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Justt API Rules
  rule_count: 57
  severity_counts:
    error: 46
    hint: 0
    info: 3
    warn: 8
  slug: justt-rules
scopes:
- name: Justt Scopes
  scope_count: 1
  slug: justt-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 56.4
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: site-plugin
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/justt/justt-2026-09-02T150010.png
security:
- kind: authentication
  name: Justt Authentication
  slug: justt-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Justt Domain Security
  slug: justt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Justt Trust Center
  slug: justt-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 27017, ISO 27018
skill_count: 4
skills:
- name: Receive and verify Justt webhooks
  slug: justt-handle-webhooks
- name: Submit evidence for a Justt chargeback
  slug: justt-submit-evidence
- name: Triage Justt chargebacks and set the fight/accept decision
  slug: justt-triage-and-decide-disputes
- name: Work Justt pre-chargeback alerts
  slug: justt-work-pre-chargeback-alerts
slug: justt
tags:
- Company
- Payments
- Chargebacks
- Disputes
- Fraud Prevention
- Risk Management
- Financial Services
- E-Commerce
- Artificial Intelligence
- Webhook
website: https://justt.ai/
---
