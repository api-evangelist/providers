---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Xpay Sh Agentic Access
  operation_count: 6
  slug: xpay-sh-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- baseURL: https://api.xpay.sh/hub
  baseurl_source: declared
  description: The Rda API from xpay-sh — 2 operation(s) for rda.
  name: xpay-sh Rda API
  slug: xpay-sh-rda-api
- baseURL: https://api.xpay.sh/hub
  baseurl_source: declared
  description: The Rdas API from xpay-sh — 1 operation(s) for rdas.
  name: xpay-sh Rdas API
  slug: xpay-sh-rdas-api
- baseURL: https://api.xpay.sh/hub
  baseurl_source: declared
  description: The Run API from xpay-sh — 1 operation(s) for run.
  name: xpay-sh Run API
  slug: xpay-sh-run-api
- baseURL: https://api.xpay.sh/hub
  baseurl_source: declared
  description: The Wallet API from xpay-sh — 2 operation(s) for wallet.
  name: xpay-sh Wallet API
  slug: xpay-sh-wallet-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/xpay-sh/agentic-access/xpay-sh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xpay-sh-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/xpay-sh/plans/xpay-sh-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xpay-sh-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/xpay-sh/rules/xpay-sh-rules.yml
  title: ''
  type: Spectral
  url: rules/xpay-sh-rules.yml
- group: design
  href: https://artifacts.apis.io/xpay-sh/json-ld/xpay-sh-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/xpay-sh-context.jsonld
- group: design
  href: https://artifacts.apis.io/xpay-sh/vocabulary/xpay-sh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xpay-sh-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/xpay-sh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/xpay-sh/data-model/xpay-sh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xpay-sh-data-model.yml
- group: auth
  href: https://artifacts.apis.io/xpay-sh/authentication/xpay-sh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xpay-sh-authentication.yml
- group: design
  href: https://artifacts.apis.io/xpay-sh/errors/xpay-sh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xpay-sh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xpay-sh/conformance/xpay-sh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xpay-sh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xpay-sh/llms/xpay-sh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xpay-sh-llms.txt
- group: agent
  href: https://artifacts.apis.io/xpay-sh/well-known/xpay-sh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xpay-sh-well-known.yml
- group: other
  href: https://artifacts.apis.io/xpay-sh/hosts/xpay-sh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xpay-sh-hosts.yml
- group: other
  href: https://artifacts.apis.io/xpay-sh/vendors/xpay-sh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xpay-sh-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xpay.sh/legal/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://www.xpay.sh/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xpay.sh/legal/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.xpay.sh/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://www.xpay.sh/publishers/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xpaysh
- group: company
  title: ''
  type: Blog
  url: https://www.xpay.sh/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.xpay.sh/en/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xpay.sh/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.xpay.sh/llms.txt
- group: auth
  href: https://artifacts.apis.io/xpay-sh/security/xpay-sh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xpay-sh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://xpay.sh/
created: '2026-10-30'
description: xpay✦ is an agent‑readiness stack for commerce, enabling storefronts, content, and APIs to be discoverable, transactable, and monetizable by AI agents such as ChatGPT, Claude, Gemini, and autonomous shoppers. It offers catalog, content, checkout, and order handling, providing a SaaS platform for merchants, publishers, and AI‑driven commerce.
json_schemas:
- name: CreateRdaRequest
  property_count: 12
  slug: xpay-sh-create-rda-request
- name: RdaDetail
  property_count: 25
  slug: xpay-sh-rda-detail
- name: RdaSummary
  property_count: 16
  slug: xpay-sh-rda-summary
- name: RunResult
  property_count: 7
  slug: xpay-sh-run-result
- name: Wallet
  property_count: 8
  slug: xpay-sh-wallet
jsonld:
- class_count: 8
  name: Xpay Sh Context
  property_count: 55
  slug: xpay-sh-context
layout: provider
modified: '2026-10-30'
name: xpay-sh
nav: Providers
network: true
overview: 'xpay-sh publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Rda API, Rdas API, Run API, and 1 more. Tagged areas include Company, Commerce, Artificial Intelligence, Software-as-a-Service, and Agent Readiness.


  The xpay-sh catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  xpay-sh''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, API reference, and 19 more developer resources.'
plans:
- name: Xpay Sh Plans Pricing
  plan_count: 2
  slug: xpay-sh-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: xpay-sh API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: xpay-sh-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.0
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 63.7
    developer_ergonomics: 31.5
    discoverability: 70.5
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/xpay-sh/xpay-sh-2026-11-03T150307.png
security:
- kind: authentication
  name: Xpay Sh Authentication
  slug: xpay-sh-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Xpay Sh Domain Security
  slug: xpay-sh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: xpay-sh-hub
  slug: xpay-sh-hub
- name: xpay-sh-manage-rda
  slug: xpay-sh-manage-rda
- name: xpay-sh-payment
  slug: xpay-sh-payment
slug: xpay-sh
tags:
- Company
- Commerce
- Artificial Intelligence
- Software-as-a-Service
- Agent Readiness
website: https://xpay.sh/
---
