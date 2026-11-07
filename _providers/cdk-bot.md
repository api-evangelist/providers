---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cdk Bot Agentic Access
  operation_count: 13
  slug: cdk-bot-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.cdk.bot
  baseurl_source: declared
  description: The Games API from CDK Bot — 3 operation(s) for games.
  name: CDK Bot Games API
  slug: cdk-bot-games-api
- baseURL: https://api.cdk.bot
  baseurl_source: declared
  description: The Meta API from CDK Bot — 5 operation(s) for meta.
  name: CDK Bot Meta API
  slug: cdk-bot-meta-api
- baseURL: https://api.cdk.bot
  baseurl_source: declared
  description: The Orders API from CDK Bot — 2 operation(s) for orders.
  name: CDK Bot Orders API
  slug: cdk-bot-orders-api
- baseURL: https://api.cdk.bot
  baseurl_source: declared
  description: The Purchase API from CDK Bot — 1 operation(s) for purchase.
  name: CDK Bot Purchase API
  slug: cdk-bot-purchase-api
- baseURL: https://api.cdk.bot
  baseurl_source: declared
  description: The Refunds API from CDK Bot — 1 operation(s) for refunds.
  name: CDK Bot Refunds API
  slug: cdk-bot-refunds-api
- baseURL: https://api.cdk.bot
  baseurl_source: declared
  description: The Status API from CDK Bot — 1 operation(s) for status.
  name: CDK Bot Status API
  slug: cdk-bot-status-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/cdk-bot/agentic-access/cdk-bot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cdk-bot-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cdk-bot/rules/cdk-bot-rules.yml
  title: ''
  type: Spectral
  url: rules/cdk-bot-rules.yml
- group: design
  href: https://artifacts.apis.io/cdk-bot/vocabulary/cdk-bot-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cdk-bot-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cdk-bot/errors/cdk-bot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cdk-bot-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cdk-bot/conformance/cdk-bot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cdk-bot-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cdk-bot/llms/cdk-bot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cdk-bot-llms.txt
- group: other
  href: https://artifacts.apis.io/cdk-bot/a2a/cdk-bot-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cdk-bot-a2a.yml
- group: other
  href: https://artifacts.apis.io/cdk-bot/hosts/cdk-bot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cdk-bot-hosts.yml
- group: other
  href: https://artifacts.apis.io/cdk-bot/vendors/cdk-bot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cdk-bot-vendors.yml
- group: build
  href: https://artifacts.apis.io/cdk-bot/packages/cdk-bot-packages.yml
  title: ''
  type: SDKs
  url: packages/cdk-bot-packages.yml
- group: build
  href: https://artifacts.apis.io/cdk-bot/packages/cdk-bot-packages.yml
  title: ''
  type: Packages
  url: packages/cdk-bot-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdk.bot/terms
- group: company
  title: ''
  type: Blog
  url: https://cdk.bot/blog
- group: docs
  title: ''
  type: APIReference
  url: https://api.cdk.bot/docs
- group: auth
  href: https://artifacts.apis.io/cdk-bot/security/cdk-bot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cdk-bot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cdk.bot/
created: '2026-11-04'
description: CDK Bot provides an agent‑native REST API for purchasing digital products such as game keys, gift cards, and subscriptions using USDC on the Base blockchain. The platform offers instant delivery, zero registration, and on‑chain verification, with a public OpenAPI 3.1 specification, interactive Swagger docs, and a discovery manifest for autonomous AI agents. It supports browsing over 40,000 products, includes health checks, rate‑limit information, and dedicated support via email.
image: https://cdk.bot/og-image.png
layout: provider
modified: '2026-11-04'
name: CDK Bot
nav: Providers
network: true
overview: 'CDK Bot publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Games API, Meta API, Orders API, and 3 more. Tagged areas include Digital Products, Crypto Payments, and Autonomous Agents.


  The CDK Bot catalog on APIs.io includes 1 Spectral governance ruleset.


  CDK Bot''s developer surface includes engineering blog, API reference, and 14 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: CDK Bot API Rules
  rule_count: 45
  severity_counts:
    error: 41
    hint: 0
    info: 3
    warn: 1
  slug: cdk-bot-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 47.3
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 11.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cdk Bot Domain Security
  slug: cdk-bot-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cdk-bot
tags:
- Digital Products
- Crypto Payments
- Autonomous Agents
website: https://cdk.bot/
---
