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
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Health AI Clarity Market API provides search listings, get listing, outcomes, price tape, evidence check, and checkout operations.
  name: Clarity Market
  slug: clarity-market
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/healthai-com/llms/healthai-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/healthai-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/healthai-com/mcp/healthai-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/healthai-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/healthai-com/hosts/healthai-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/healthai-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/healthai-com/vendors/healthai-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/healthai-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.healthai.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.healthai.com/privacy.html
- group: auth
  href: https://artifacts.apis.io/healthai-com/security/healthai-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/healthai-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://healthai.com/
created: '2026-10-30'
description: Health AI builds sourced evidence tools for AI agents, offering Clarity for product checks, Constat for FDA-device research, and an evidence platform that aggregates data to help developers and regulators assess health‑related AI products. The company provides open‑source resources, whitepapers, and a public API that enables integration of its evidence services into applications. Its mission is to bring transparency and rigor to AI‑driven health solutions, supporting compliance, safety, and informed decision‑making.
image: https://healthai.com/favicon-192.png
layout: provider
mcp_servers:
- description: Remote MCP server at app.healthai.com.
  name: healthai-com MCP Server
  slug: healthai-com-mcp-yml
modified: '2026-10-30'
name: healthai-com
nav: Providers
network: true
overview: healthai-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Artificial Intelligence, Evidence, and Tools.
random_paper: 20
scopes:
- name: Healthai Com Scopes
  scope_count: 0
  slug: healthai-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/healthai-com/healthai-com-2026-11-03T133316.png
security:
- kind: authentication
  name: Healthai Com Authentication
  slug: healthai-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Healthai Com Domain Security
  slug: healthai-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: healthai-com
tags:
- Company
- Health
- Artificial Intelligence
- Evidence
- Tools
website: https://healthai.com/
---
