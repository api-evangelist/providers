---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 4
  name: Bewary Agentic Access
  operation_count: 47
  slug: bewary-agentic-access
  summary_line: 47 operations · 18 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Account API from Bewary — 1 operation(s) for account.
  name: Bewary Account API
  slug: bewary-account-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The App API from Bewary — 1 operation(s) for app.
  name: Bewary App API
  slug: bewary-app-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Assess API from Bewary — 1 operation(s) for assess.
  name: Bewary Assess API
  slug: bewary-assess-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Backtest API from Bewary — 2 operation(s) for backtest.
  name: Bewary Backtest API
  slug: bewary-backtest-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Batch API from Bewary — 1 operation(s) for batch.
  name: Bewary Batch API
  slug: bewary-batch-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Billing API from Bewary — 4 operation(s) for billing.
  name: Bewary Billing API
  slug: bewary-billing-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Bulk API from Bewary — 3 operation(s) for bulk.
  name: Bewary Bulk API
  slug: bewary-bulk-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Calibration API from Bewary — 1 operation(s) for calibration.
  name: Bewary Calibration API
  slug: bewary-calibration-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Datasets API from Bewary — 1 operation(s) for datasets.
  name: Bewary Datasets API
  slug: bewary-datasets-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Directory API from Bewary — 4 operation(s) for directory.
  name: Bewary Directory API
  slug: bewary-directory-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Domain API from Bewary — 2 operation(s) for domain.
  name: Bewary Domain API
  slug: bewary-domain-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Email API from Bewary — 1 operation(s) for email.
  name: Bewary Email API
  slug: bewary-email-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Events API from Bewary — 1 operation(s) for events.
  name: Bewary Events API
  slug: bewary-events-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Iban API from Bewary — 1 operation(s) for iban.
  name: Bewary Iban API
  slug: bewary-iban-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Ip API from Bewary — 1 operation(s) for ip.
  name: Bewary Ip API
  slug: bewary-ip-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Keys API from Bewary — 2 operation(s) for keys.
  name: Bewary Keys API
  slug: bewary-keys-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Payment Handle API from Bewary — 1 operation(s) for payment handle.
  name: Bewary Payment Handle API
  slug: bewary-payment-handle-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Phone API from Bewary — 1 operation(s) for phone.
  name: Bewary Phone API
  slug: bewary-phone-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Shortcode API from Bewary — 1 operation(s) for shortcode.
  name: Bewary Shortcode API
  slug: bewary-shortcode-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Url API from Bewary — 1 operation(s) for url.
  name: Bewary URL API
  slug: bewary-url-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Wallet API from Bewary — 1 operation(s) for wallet.
  name: Bewary Wallet API
  slug: bewary-wallet-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Watches API from Bewary — 2 operation(s) for watches.
  name: Bewary Watches API
  slug: bewary-watches-api
- baseURL: https://api.bewary.app
  baseurl_source: declared
  description: The Webhooks API from Bewary — 4 operation(s) for webhooks.
  name: Bewary Webhooks API
  slug: bewary-webhooks-api
artifact_total: 37
asyncapis:
- description: ''
  name: Bewary Webhooks
  slug: bewary-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/bewary/agentic-access/bewary-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bewary-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bewary/plans/bewary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bewary-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bewary/rules/bewary-rules.yml
  title: ''
  type: Spectral
  url: rules/bewary-rules.yml
- group: design
  href: https://artifacts.apis.io/bewary/json-ld/bewary-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bewary-context.jsonld
- group: design
  href: https://artifacts.apis.io/bewary/vocabulary/bewary-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bewary-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bewary/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bewary/asyncapi/bewary-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bewary-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bewary/data-model/bewary-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bewary-data-model.yml
- group: build
  href: https://artifacts.apis.io/bewary/cli/bewary-cli.yml
  title: ''
  type: CLI
  url: cli/bewary-cli.yml
- group: operate
  href: https://artifacts.apis.io/bewary/changelog/bewary-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bewary-changelog.yml
- group: design
  href: https://artifacts.apis.io/bewary/conventions/bewary-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bewary-conventions.yml
- group: auth
  href: https://artifacts.apis.io/bewary/authentication/bewary-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bewary-authentication.yml
- group: design
  href: https://artifacts.apis.io/bewary/errors/bewary-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bewary-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bewary/conformance/bewary-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bewary-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bewary/llms/bewary-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bewary-llms.txt
- group: other
  href: https://artifacts.apis.io/bewary/a2a/bewary-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bewary-a2a.yml
- group: agent
  href: https://artifacts.apis.io/bewary/well-known/bewary-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bewary-well-known.yml
- group: other
  href: https://artifacts.apis.io/bewary/hosts/bewary-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bewary-hosts.yml
- group: build
  href: https://artifacts.apis.io/bewary/packages/bewary-packages.yml
  title: ''
  type: SDKs
  url: packages/bewary-packages.yml
- group: build
  href: https://artifacts.apis.io/bewary/packages/bewary-packages.yml
  title: ''
  type: Packages
  url: packages/bewary-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bewary.app/terms
- group: operate
  title: ''
  type: Support
  url: https://bewary.app/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bewary.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bewary.app/pricing
- group: start
  title: ''
  type: Login
  url: https://bewary.app/login
- group: start
  title: ''
  type: GettingStarted
  url: https://bewary.app/docs/related
- group: docs
  title: ''
  type: APIReference
  url: https://bewary.app/docs/changelog
- group: auth
  href: https://artifacts.apis.io/bewary/security/bewary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bewary-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bewary.app
- group: docs
  title: ''
  type: Documentation
  url: https://bewary.app/docs
created: '2026-11-02'
description: Bewary provides a scam detection API and MCP server for apps and AI agents. It checks links, domains, phone numbers, emails, wallets, IBANs, apps and payment handles for scams. A free key offers 1,000 credits per month, with prepaid credit packs available. The service offers real‑time verdicts (scam, suspicious, safe, unknown) and detailed reason codes, supporting developers, security teams and AI integrations. Operated by Reply200 Inc., Bewary aims to help prevent fraud across digital channels.
image: https://bewary.app/og/default.png?v=9ed86ef4
json_schemas:
- name: Envelope
  property_count: 18
  slug: bewary-envelope
- name: RelatedResponse
  property_count: 15
  slug: bewary-related-response
- name: WatchCreated
  property_count: 11
  slug: bewary-watch-created
- name: WatchDetail
  property_count: 12
  slug: bewary-watch-detail
- name: WebhookCreated
  property_count: 10
  slug: bewary-webhook-created
- name: WebhookDetail
  property_count: 10
  slug: bewary-webhook-detail
jsonld:
- class_count: 119
  name: Bewary Context
  property_count: 352
  slug: bewary-context
layout: provider
modified: '2026-11-02'
name: Bewary
nav: Providers
network: true
overview: 'Bewary publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, App API, Assess API, and 20 more. Tagged areas include Company, Security, Fraud Prevention, and MCP.


  The Bewary catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bewary''s developer surface includes CLI, changelog, authentication, support, pricing, getting-started guide, API reference, and 23 more developer resources.'
plans:
- name: Bewary Plans Pricing
  plan_count: 5
  slug: bewary-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Bewary API Rules
  rule_count: 51
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 7
  slug: bewary-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 70.8
    developer_ergonomics: 44.6
    discoverability: 57.1
    operational_transparency: 23.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bewary Authentication
  slug: bewary-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Bewary Domain Security
  slug: bewary-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: bewary-lookup-domain-and-related
  slug: bewary-lookup-domain-and-related
slug: bewary
tags:
- Company
- Security
- Fraud Prevention
- MCP
website: https://bewary.app
---
