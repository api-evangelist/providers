---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Botx402 Io Agentic Access
  operation_count: 3
  slug: botx402-io-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Pay‑per‑use bot API providing paid lookups and one‑shot reports to AI agents and users.
  name: BotX402 API
  slug: botx402-api
- baseURL: https://botx402.io
  baseurl_source: declared
  description: The Agent API from BotX402 — 1 operation(s) for agent.
  name: BotX402 Agent API
  slug: botx402-io-agent-api
- baseURL: https://botx402.io
  baseurl_source: declared
  description: The Base Address Balance API from BotX402 — 1 operation(s) for base address balance.
  name: BotX402 Base Address Balance API
  slug: botx402-io-base-address-balance-api
- baseURL: https://botx402.io
  baseurl_source: declared
  description: The .well Known API from BotX402 — 1 operation(s) for .well known.
  name: BotX402 .well Known API
  slug: botx402-io-well-known-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/botx402-io/agentic-access/botx402-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/botx402-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/botx402-io/plans/botx402-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/botx402-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/botx402-io/rules/botx402-io-rules.yml
  title: ''
  type: Spectral
  url: rules/botx402-io-rules.yml
- group: design
  href: https://artifacts.apis.io/botx402-io/vocabulary/botx402-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/botx402-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/botx402-io/errors/botx402-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/botx402-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/botx402-io/conformance/botx402-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/botx402-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/botx402-io/llms/botx402-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/botx402-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/botx402-io/well-known/botx402-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/botx402-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/botx402-io/hosts/botx402-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/botx402-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/botx402-io/vendors/botx402-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/botx402-io-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.botx402.io/
- group: auth
  href: https://artifacts.apis.io/botx402-io/security/botx402-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/botx402-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://botx402.io/
- group: docs
  title: ''
  type: Documentation
  url: https://botx402.io/about
- group: commercial
  title: ''
  type: Pricing
  url: https://botx402.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://botx402.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://botx402.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://botx402.io/status
created: '2026-11-02'
description: BotX402 provides pay‑per‑use bots that perform one‑off business jobs such as audits, compliance reports, and analyses. Small businesses can submit data, pay per run, and receive a PDF report without creating an account or subscription. The service emphasizes simplicity, low cost, and defencible outputs, targeting occasional needs rather than ongoing SaaS solutions.
layout: provider
modified: '2026-11-02'
name: BotX402
nav: Providers
network: true
overview: 'BotX402 publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, Base Address Balance API, .well Known API, and 1 more. Tagged areas include Company, Pay-Per-Use, Bots, Business, and Automation.


  The BotX402 catalog on APIs.io includes 1 Spectral governance ruleset.


  BotX402''s developer surface includes documentation, pricing, and 16 more developer resources.'
plans:
- name: Botx402 Io Plans Pricing
  plan_count: 1
  slug: botx402-io-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: BotX402 API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: botx402-io-rules
score:
  band: thin
  composite: 31.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 48.8
    catalog_earned_first_party: 8.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 43.1
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Botx402 Io Domain Security
  slug: botx402-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: botx402-io
tags:
- Company
- Pay-Per-Use
- Bots
- Business
- Automation
- SaaS-alternative
website: https://botx402.io/
---
