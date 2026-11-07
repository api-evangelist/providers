---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 66.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 65
  human_in_the_loop: 6
  name: Logbrew Agentic Access
  operation_count: 141
  slug: logbrew-agentic-access
  summary_line: 141 operations · 65 acting · 6 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Your account, sign-in tokens, usage, and pending invitations.
  name: LogBrew Account API
  slug: logbrew-account-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Product actions that people and agents take in your app.
  name: LogBrew Actions API
  slug: logbrew-actions-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Alert rules, webhooks, push devices, and alert preferences.
  name: LogBrew Alerts API
  slug: logbrew-alerts-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Plans, checkout, and the billing portal.
  name: LogBrew Billing API
  slug: logbrew-billing-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: AI clients you connected to the LogBrew MCP server.
  name: LogBrew Connected clients API
  slug: logbrew-connected-clients-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Debug files and release artifacts that symbolicate native and web crashes.
  name: LogBrew Debug files API
  slug: logbrew-debug-files-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Send telemetry from your own code when no LogBrew SDK fits.
  name: LogBrew Ingestion API
  slug: logbrew-ingestion-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: 'Grouped errors: list, read, triage, assign, own, and investigate.'
  name: LogBrew Issues API
  slug: logbrew-issues-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: A live stream of new telemetry.
  name: LogBrew Live feed API
  slug: logbrew-live-feed-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Logs and their investigations.
  name: LogBrew Logs API
  slug: logbrew-logs-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Metric samples, series, and investigations.
  name: LogBrew Metrics API
  slug: logbrew-metrics-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Organizations, members, invitations, teams, and project roles.
  name: LogBrew Organizations API
  slug: logbrew-organizations-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: 'Product analytics: overview, properties, funnels, paths, retention, and more.'
  name: LogBrew Product analytics API
  slug: logbrew-product-analytics-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Projects, project keys, setup checks, and repository components.
  name: LogBrew Projects API
  slug: logbrew-projects-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Releases, deployments, and release investigations.
  name: LogBrew Releases API
  slug: logbrew-releases-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Support tickets.
  name: LogBrew Support API
  slug: logbrew-support-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Traces, spans, and their investigations.
  name: LogBrew Traces API
  slug: logbrew-traces-api
- baseURL: https://api.logbrew.co
  baseurl_source: declared
  description: Signal counts over time.
  name: LogBrew Volume API
  slug: logbrew-volume-api
artifact_total: 34
common:
- group: agent
  href: https://artifacts.apis.io/logbrew/agentic-access/logbrew-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/logbrew-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/logbrew/plans/logbrew-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/logbrew-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/logbrew/rules/logbrew-rules.yml
  title: ''
  type: Spectral
  url: rules/logbrew-rules.yml
- group: design
  href: https://artifacts.apis.io/logbrew/json-ld/logbrew-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/logbrew-context.jsonld
- group: design
  href: https://artifacts.apis.io/logbrew/vocabulary/logbrew-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/logbrew-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/logbrew/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/logbrew/data-model/logbrew-data-model.yml
  title: ''
  type: DataModel
  url: data-model/logbrew-data-model.yml
- group: build
  href: https://artifacts.apis.io/logbrew/cli/logbrew-cli.yml
  title: ''
  type: CLI
  url: cli/logbrew-cli.yml
- group: operate
  href: https://artifacts.apis.io/logbrew/changelog/logbrew-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/logbrew-changelog.yml
- group: design
  href: https://artifacts.apis.io/logbrew/errors/logbrew-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/logbrew-problem-types.yml
- group: design
  href: https://artifacts.apis.io/logbrew/conformance/logbrew-conformance.yml
  title: ''
  type: Conformance
  url: conformance/logbrew-conformance.yml
- group: agent
  href: https://artifacts.apis.io/logbrew/llms/logbrew-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/logbrew-llms.txt
- group: other
  href: https://artifacts.apis.io/logbrew/a2a/logbrew-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/logbrew-a2a.yml
- group: auth
  href: https://artifacts.apis.io/logbrew/well-known/logbrew-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/logbrew-security.txt
- group: auth
  href: https://artifacts.apis.io/logbrew/well-known/logbrew-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/logbrew-api-security.txt
- group: agent
  href: https://artifacts.apis.io/logbrew/well-known/logbrew-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/logbrew-well-known.yml
- group: other
  href: https://artifacts.apis.io/logbrew/hosts/logbrew-hosts.yml
  title: ''
  type: Hosts
  url: hosts/logbrew-hosts.yml
- group: other
  href: https://artifacts.apis.io/logbrew/vendors/logbrew-vendors.yml
  title: ''
  type: Vendors
  url: vendors/logbrew-vendors.yml
- group: build
  href: https://artifacts.apis.io/logbrew/packages/logbrew-packages.yml
  title: ''
  type: SDKs
  url: packages/logbrew-packages.yml
- group: build
  href: https://artifacts.apis.io/logbrew/packages/logbrew-packages.yml
  title: ''
  type: Packages
  url: packages/logbrew-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://logbrew.co/en/security
- group: start
  title: ''
  type: Login
  url: https://logbrew.co/en/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://logbrew.co/en/changelog
- group: auth
  href: https://artifacts.apis.io/logbrew/security/logbrew-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/logbrew-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/logbrew/security/logbrew-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/logbrew-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://logbrew.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.logbrew.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://logbrew.co/en
- group: docs
  title: ''
  type: APIReference
  url: https://logbrew.co/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://logbrew.co/en/docs
- group: operate
  title: ''
  type: Support
  url: https://logbrew.co/en/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://logbrew.co/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://logbrew.co/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://logbrew.co/en/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LogBrewCo
created: '2026-11-02'
description: LogBrew provides agent‑first observability, offering error tracking, performance monitoring, crash reporting, log aggregation, tracing, and product analytics in a single platform. Developers can integrate via native SDKs or direct API calls, with a generous free tier and paid plans for teams. The service includes real‑time dashboards, alerting, and deep insights to help diagnose production issues quickly and improve product reliability.
image: https://logbrew.co/favicon-512x512.png
json_schemas:
- name: AccountUsageResponse
  property_count: 19
  slug: logbrew-account-usage-response
- name: IssueCorrectionVerificationResponse
  property_count: 19
  slug: logbrew-issue-correction-verification-response
- name: IssueInvestigationResponse
  property_count: 16
  slug: logbrew-issue-investigation-response
- name: MetricInvestigationResponse
  property_count: 15
  slug: logbrew-metric-investigation-response
- name: NativeIssueV5Response
  property_count: 25
  slug: logbrew-native-issue-v5-response
- name: SupportTicketResponse
  property_count: 24
  slug: logbrew-support-ticket-response
jsonld:
- class_count: 120
  name: Logbrew Context
  property_count: 283
  slug: logbrew-context
layout: provider
modified: '2026-11-02'
name: LogBrew
nav: Providers
network: true
overview: 'LogBrew publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Actions API, Alerts API, and 15 more. Tagged areas include Observability, Logging, Monitoring, Analytics, and Error Tracking.


  The LogBrew catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LogBrew''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, pricing, and 28 more developer resources.'
plans:
- name: Logbrew Plans Pricing
  plan_count: 4
  slug: logbrew-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: LogBrew API Rules
  rule_count: 71
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 11
  slug: logbrew-rules
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 68.8
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Logbrew Authentication
  slug: logbrew-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Logbrew Domain Security
  slug: logbrew-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Logbrew Vulnerability Disclosure
  slug: logbrew-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: create-checkout
  slug: create-checkout
- name: register-device
  slug: register-device
- name: sign-out
  slug: sign-out
slug: logbrew
tags:
- Observability
- Logging
- Monitoring
- Analytics
- Error Tracking
website: https://logbrew.co
---
