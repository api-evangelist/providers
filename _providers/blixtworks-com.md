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
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Vision toolbox paid per-call via x402 (USDC on Base) offering zero-shot categorization, captioning, OCR, and CLIP embeddings.
  name: img-categorize
  slug: img-categorize
- baseURL: https://www.blixtworks.com
  baseurl_source: declared
  description: 'Vision toolbox paid per-call via x402 (USDC on Base): zero-shot categorization, captioning, OCR, CLIP embeddings. No accounts or API keys.'
  name: img-categorize Api API
  slug: img-categorize-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/blixtworks-com/rules/blixtworks-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blixtworks-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blixtworks-com/errors/blixtworks-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blixtworks-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/blixtworks-com/conformance/blixtworks-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blixtworks-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blixtworks-com/llms/blixtworks-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blixtworks-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/blixtworks-com/mcp/blixtworks-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/blixtworks-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/blixtworks-com/hosts/blixtworks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blixtworks-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blixtworks-com/vendors/blixtworks-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blixtworks-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/blixtworks-com/security/blixtworks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blixtworks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blixtworks.com/
created: '2026-11-02'
description: Blixtworks provides vision tools for agents and applications, offering image categorization, captioning, OCR, and embedding services. Payments are handled via x402 (USDC on Base) with a pay-per-call model. No account or API key is required to access the endpoints.
layout: provider
mcp_servers:
- description: Remote MCP server at www.blixtworks.com.
  name: Blixtworks MCP Server
  slug: blixtworks-com-mcp-yml
modified: '2026-11-02'
name: Blixtworks
nav: Providers
network: true
overview: 'Blixtworks publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including img-categorize Api API, and 1 more. Tagged areas include Vision, OCR, and Embeddings.


  The Blixtworks catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: Blixtworks API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: blixtworks-com-rules
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 36.7
    developer_ergonomics: 0.0
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blixtworks Com Domain Security
  slug: blixtworks-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blixtworks-com
tags:
- Vision
- OCR
- Embeddings
website: https://blixtworks.com/
---
