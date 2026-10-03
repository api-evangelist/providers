---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gatiflow Agentic Access
  operation_count: 7
  slug: gatiflow-agentic-access
  summary_line: 7 operations
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
artifact_total: 20
asyncapis:
- description: ''
  name: Gatiflow Webhooks
  slug: gatiflow-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/asyncapi/gatiflow-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/gatiflow-webhooks.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://gatiflow.io/api-docs#versioning
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/well-known/gatiflow-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/gatiflow-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/well-known/gatiflow-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gatiflow-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/security/gatiflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gatiflow-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/hosts/gatiflow-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gatiflow-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/vendors/gatiflow-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gatiflow-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/agentic-access/gatiflow-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gatiflow-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/rate-limits/gatiflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gatiflow-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/plans/gatiflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gatiflow-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/rules/gatiflow-rules.yml
  title: ''
  type: Spectral
  url: rules/gatiflow-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/json-ld/gatiflow-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gatiflow-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/vocabulary/gatiflow-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gatiflow-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/data-model/gatiflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gatiflow-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/changelog/gatiflow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gatiflow-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/conventions/gatiflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gatiflow-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://gatiflow.io/compliance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/security/gatiflow-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/gatiflow-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/security/gatiflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gatiflow-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/authentication/gatiflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gatiflow-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/9fR5IzLq0q
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/lifecycle/gatiflow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gatiflow-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/errors/gatiflow-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/gatiflow-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/errors/gatiflow-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gatiflow-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/conformance/gatiflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gatiflow-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/llms/gatiflow-llms.txt
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
  href: https://raw.githubusercontent.com/api-evangelist/gatiflow/refs/heads/main/finops/gatiflow-finops.yml
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
- name: Gatiflow Finops
  service_category: Analytics
  slug: gatiflow-finops
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
- class_count: 2
  name: Gatiflow Context
  property_count: 6
  slug: gatiflow-context
layout: provider
modified: '2026-09-27'
name: GatiFlow
nav: Providers
network: true
overview: 'GatiFlow publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Intelligence API, Public API, Usage API, and 1 more. Tagged areas include Market Intelligence, Developer Signals, Trends, Hiring, and Open Source.


  The GatiFlow catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  GatiFlow''s developer surface includes changelog, authentication, getting-started guide, pricing, support, engineering blog, code examples, and 50 more developer resources.'
plans:
- name: Gatiflow Plans Pricing
  plan_count: 4
  slug: gatiflow-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 8
  name: Gatiflow Rate Limits
  slug: gatiflow-rate-limits
rules:
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: GatiFlow API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: gatiflow-rules
score:
  band: exemplar
  composite: 74.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 83.8
    catalog_earned_first_party: 24.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.2
  facets:
    access_clarity: 100.0
    contract_governance: 22.0
    contract_quality: 33.3
    developer_ergonomics: 70.8
    discoverability: 91.1
    operational_transparency: 94.7
  previous_composite: 68.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 69.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
