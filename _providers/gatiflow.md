---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 56.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.gatiflow.io
  baseurl_source: declared
  description: The intelligence operations of the GatiFlow Intelligence API — the current intelligence report (content scales with plan), snapshot history, one archived report by snapshot id, and a CSV/PDF export of
  name: GatiFlow Intelligence API
  phrasing_intents:
  - id: report_api_v1_intelligence_report_get
    intent: Generate a fresh intelligence report
    question: How do I generate a current intelligence report for my organization in Gatiflow?
  - id: report_history_list_api_v1_intelligence_report_history_get
    intent: List retained report snapshots
    question: Which past report snapshots are still retained for my organization?
  - id: report_at_snapshot_api_v1_intelligence_report_at__snapshot_id__get
    intent: Retrieve an archived report snapshot
    question: Can I open the intelligence report exactly as it was collected on an earlier date?
  - id: export_report_api_v1_intelligence_report_export_get
    intent: Export the intelligence report as a file
    question: Can I download the intelligence report as a CSV or PDF file instead of JSON?
  phrasing_ops: 4
  slug: gatiflow-intelligence-api
- baseURL: https://api.gatiflow.io
  baseurl_source: declared
  description: The public operations of the GatiFlow Intelligence API — the Daily Insights payload (web-app session auth, not an API key; an API key receives 401 there) and the latest Saturday Deep Dive preview (tit
  name: GatiFlow Public API
  phrasing_intents:
  - id: get_latest_deep_dive_api_v1_public_deep_dive_get
    intent: Preview the latest Deep Dive article
    question: What is the topic of the most recent Gatiflow Deep Dive article?
  - id: weekly_report_api_v1_public_weekly_report_get
    intent: Get the Daily Insights report
    question: How do I read today's Daily Insights report that backs the Insights page?
  phrasing_ops: 2
  slug: gatiflow-public-api
- baseURL: https://api.gatiflow.io
  baseurl_source: declared
  description: The usage operation of the GatiFlow Intelligence API — recent calls made with the API key used on the request (limit up to 500), so a scheduled job can audit its own traffic without a second log.
  name: GatiFlow Usage API
  phrasing_intents:
  - id: get_my_usage_api_v1_usage_get
    intent: List recent calls made with my API key
    question: Which endpoints has my Gatiflow API key called recently, and with what status codes?
  phrasing_ops: 1
  slug: gatiflow-usage-api
- baseURL: https://api.gatiflow.io
  baseurl_source: declared
  description: The intelligence:alert webhook GatiFlow pushes to HTTPS endpoints registered by Pro and Business organizations — spike, emerging and new_hirer alerts matching the watchlist, signed with HMAC-SHA256 (X
  name: GatiFlow Webhooks API
  slug: gatiflow-webhooks-api
- baseURL: https://api.gatiflow.io
  baseurl_source: declared
  description: 'Topic signals for AI agents, paid per call in USDC over x402: no account, no API key. The first request returns 402 with the price; the retried, paid request returns the signals.'
  name: GatiFlow Agent API
  slug: gatiflow-agent-api
artifact_total: 22
asyncapis:
- description: ''
  name: Gatiflow Webhooks
  slug: gatiflow-webhooks
common:
- group: design
  href: https://artifacts.apis.io/gatiflow/rules/gatiflow-rules.yml
  title: ''
  type: Spectral
  url: rules/gatiflow-rules.yml
- group: design
  href: https://artifacts.apis.io/gatiflow/json-ld/gatiflow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gatiflow-context.jsonld
- group: other
  href: https://artifacts.apis.io/gatiflow/capabilities/gatiflow-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gatiflow-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/gatiflow/asyncapi/gatiflow-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gatiflow-webhooks.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://gatiflow.io/api-docs#versioning
- group: auth
  href: https://artifacts.apis.io/gatiflow/well-known/gatiflow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gatiflow-security.txt
- group: agent
  href: https://artifacts.apis.io/gatiflow/well-known/gatiflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gatiflow-well-known.yml
- group: auth
  href: https://artifacts.apis.io/gatiflow/security/gatiflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gatiflow-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/gatiflow/hosts/gatiflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gatiflow-hosts.yml
- group: other
  href: https://artifacts.apis.io/gatiflow/vendors/gatiflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gatiflow-vendors.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: https://gatiflow.io/agentic-access.json
- group: operate
  href: https://artifacts.apis.io/gatiflow/rate-limits/gatiflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gatiflow-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/gatiflow/plans/gatiflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gatiflow-plans-pricing.yml
- group: design
  title: ''
  type: Spectral
  url: https://gatiflow.io/spectral.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://gatiflow.io/context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://gatiflow.io/vocabulary.json
- group: agent
  title: ''
  type: AgentSkill
  url: https://gatiflow.io/.well-known/agent-skills/gatiflow-intelligence/SKILL.md
- group: other
  title: ''
  type: Overlay
  url: https://gatiflow.io/overlays/api-key-client.json
- group: design
  href: https://artifacts.apis.io/gatiflow/data-model/gatiflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gatiflow-data-model.yml
- group: operate
  href: https://artifacts.apis.io/gatiflow/changelog/gatiflow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gatiflow-changelog.yml
- group: design
  href: https://artifacts.apis.io/gatiflow/conventions/gatiflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gatiflow-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://gatiflow.io/compliance
- group: auth
  href: https://artifacts.apis.io/gatiflow/security/gatiflow-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gatiflow-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/gatiflow/security/gatiflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gatiflow-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/gatiflow/authentication/gatiflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gatiflow-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/9fR5IzLq0q
- group: design
  href: https://artifacts.apis.io/gatiflow/lifecycle/gatiflow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gatiflow-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/gatiflow/errors/gatiflow-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/gatiflow-error-codes.yml
- group: design
  href: https://artifacts.apis.io/gatiflow/errors/gatiflow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gatiflow-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: https://gatiflow.io/conformance.json
- group: agent
  href: https://artifacts.apis.io/gatiflow/llms/gatiflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gatiflow-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://gatiflow.io/changelog
- group: company
  title: ''
  type: Website
  url: https://gatiflow.io
- group: start
  title: ''
  type: Login
  url: https://gatiflow.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gatiflow.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gatiflow.io/privacy
- group: other
  title: ''
  type: AITransparency
  url: https://gatiflow.io/compliance
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://gatiflow.io/opt-out
- group: other
  title: ''
  type: APIsJSON
  url: https://gatiflow.io/apis.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://gatiflow.io/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://gatiflow.io/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://gatiflow.io/#pricing
- group: auth
  title: ''
  type: Security
  url: https://gatiflow.io/aup
- group: operate
  title: ''
  type: Support
  url: mailto:support@gatiflow.io
- group: company
  title: ''
  type: Blog
  url: https://gatiflow.io/academy
- group: design
  title: ''
  type: Webhooks
  url: https://gatiflow.io/api-docs/webhooks
- group: operate
  title: ''
  type: Roadmap
  url: https://gatiflow.io/roadmap
- group: build
  title: ''
  type: PostmanCollection
  url: https://gatiflow.io/postman_collection.json
- group: other
  title: ''
  type: SBOM
  url: https://api.gatiflow.io/sbom.cdx.json
- group: operate
  title: ''
  type: SupportLifetime
  url: https://gatiflow.io/api-docs#versioning
- group: build
  title: ''
  type: CodeExamples
  url: https://gatiflow.io/api-docs/examples
- group: other
  title: ''
  type: APICatalog
  url: https://gatiflow.io/.well-known/api-catalog
- group: other
  title: ''
  type: ContentSignal
  url: https://gatiflow.io/robots.txt
- group: start
  title: ''
  type: Console
  url: https://api.gatiflow.io/docs
- group: commercial
  href: https://artifacts.apis.io/gatiflow/finops/gatiflow-finops.yml
  title: ''
  type: FinOps
  url: finops/gatiflow-finops.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://gatiflow.io/privacy#processors
- group: other
  title: ''
  type: DataResidency
  url: https://gatiflow.io/privacy#data-residency
- group: operate
  title: ''
  type: IncidentNotification
  url: https://gatiflow.io/privacy#incident-notification
- group: commercial
  title: ''
  type: GlobalPrivacyControl
  url: https://gatiflow.io/privacy#global-privacy-control
- group: learn
  title: ''
  type: TrainingDataSummary
  url: https://gatiflow.io/compliance#training-data
- group: other
  title: ''
  type: ExitAssistance
  url: https://gatiflow.io/terms#effect-of-termination
created: '2026-09-21'
description: GatiFlow is a market, talent and hiring intelligence product that turns public developer activity into structured signals and serves them as a read-only JSON API. Thirteen public sources — GitHub, StackOverflow, HackerNews, Dev.to, arXiv, OpenReview, npm, PyPI, HuggingFace, Adzuna, Remotive, job boards (Greenhouse and Lever public postings) and SEC EDGAR — are polled on a six-hour cycle; a trend-category signal is published only once two independent sources confirm it or one source repeats it across two collection cycles, confidence is computed from source authority, diversity and persistence rather than raw mention count, and every signal carries its evidence and week-over-week movement. The public GatiFlow Intelligence API exposes seven read-only operations (the current report, snapshot history, a point-in-time snapshot, a CSV/PDF export, the daily insights payload, the latest Deep Dive preview, and per-key usage), authenticated with a gf_-prefixed API key in the X-API-Key
  header, priced across Free, Starter ($49/mo), Pro ($149/mo) and Business ($499/mo) plans.
finops:
- has_sources: true
  method: authored
  name: Gatiflow Finops
  primary_unit: subscription
  service_category: Analytics
  slug: gatiflow-finops
  template: false
image: https://gatiflow.io/favicon.svg
json_schemas:
- name: DailyInsights
  property_count: 9
  slug: gatiflow-daily-insights
- name: DeepDivePreview
  property_count: 10
  slug: gatiflow-deep-dive-preview
- name: IntelligenceReport
  property_count: 11
  slug: gatiflow-intelligence-report
- name: ReportHistory
  property_count: 4
  slug: gatiflow-report-history
- name: UsageLog
  property_count: 3
  slug: gatiflow-usage-log
jsonld:
- class_count: 12
  name: Gatiflow Context
  property_count: 22
  slug: gatiflow-context
layout: provider
modified: '2026-10-12'
name: GatiFlow
nav: Providers
network: true
overview: 'GatiFlow publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Intelligence API, Public API, Usage API, and 2 more. Tagged areas include Market Intelligence, Developer Signals, Trends, Hiring, and Open Source.


  The GatiFlow catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  GatiFlow''s developer surface includes changelog, authentication, getting-started guide, pricing, support, engineering blog, code examples, and 54 more developer resources.'
plans:
- name: Gatiflow Plans Pricing
  plan_count: 4
  slug: gatiflow-plans-pricing
- name: Gatiflow Price Estimates
  plan_count: 0
  slug: gatiflow-price-estimates
random_paper: 21
rate_limits:
- limit_count: 8
  name: Gatiflow Rate Limits
  slug: gatiflow-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: GatiFlow API Rules
  rule_count: 29
  severity_counts:
    error: 18
    hint: 0
    info: 3
    warn: 8
  slug: gatiflow-rules
score:
  band: exemplar
  composite: 80.1
  coverage:
    artifact_dirs: 35
    catalog_earned: 108.3
    catalog_earned_first_party: 42.0
    catalog_gap: 6.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -14.8
  facets:
    access_clarity: 73.7
    contract_governance: 89.8
    contract_quality: 84.5
    developer_ergonomics: 46.1
    discoverability: 91.1
    operational_transparency: 63.2
  previous_composite: 94.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 60.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/gatiflow/gatiflow-2026-10-11T104741.png
security:
- kind: authentication
  name: Gatiflow Authentication
  slug: gatiflow-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Gatiflow Domain Security
  slug: gatiflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gatiflow Vulnerability Disclosure
  slug: gatiflow-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gatiflow Trust Center
  slug: gatiflow-trust-center
  summary_line: trust center published
skill_count: 1
skills:
- name: gatiflow-intelligence
  slug: gatiflow-intelligence
slug: gatiflow
tags:
- Market Intelligence
- Developer Signals
- Trends
- Hiring
- Open Source
- Research
- B2B SaaS
- Artificial Intelligence
website: https://gatiflow.io
---
