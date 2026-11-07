---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentpay Agentic Access
  operation_count: 1
  slug: agentpay-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Pay-per-call web extraction, DNS/WHOIS lookup and document processing tools for AI agents.
  name: AgentPay API
  slug: agentpay-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/agentpay/agentic-access/agentpay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentpay-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentpay/rules/agentpay-rules.yml
  title: ''
  type: Spectral
  url: rules/agentpay-rules.yml
- group: design
  href: https://artifacts.apis.io/agentpay/conformance/agentpay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentpay-conformance.yml
- group: other
  href: https://artifacts.apis.io/agentpay/hosts/agentpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentpay-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentpay/vendors/agentpay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentpay-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agentpay/security/agentpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentpay.agentpay-apis.workers.dev
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/noah-silver/agentpay
created: '2026-10-02'
description: AgentPay provides pay‑per‑call web extraction, DNS/network intelligence, and document processing tools for AI agents. It offers REST APIs and MCP servers for extracting web pages to markdown, performing DNS and WHOIS lookups, parsing PDFs, RSS/Atom feeds, and generating site sitemaps, all billed per request via x402 on Base or Algorand. No signup required, with free trial credits and transparent pricing.
layout: provider
modified: '2026-10-02'
name: AgentPay
nav: Providers
network: true
overview: 'AgentPay is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Extraction, Lookup, and Tools.


  The AgentPay catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentPay''s developer surface includes documentation and 7 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: AgentPay API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agentpay-rules
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 9.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/agentpay/agentpay-2026-10-11T093054.png
security:
- kind: domain-security
  name: Agentpay Domain Security
  slug: agentpay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentpay
tags:
- Company
- Artificial Intelligence
- Extraction
- Lookup
- Tools
website: https://agentpay.agentpay-apis.workers.dev
---
