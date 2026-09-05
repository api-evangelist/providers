---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/e-cross-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/e-cross-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/e-cross-llms.txt
- group: company
  title: ''
  type: Website
  url: https://e-cross.tech
created: '2026-07-17'
description: e-CROSS is a cross-border e-commerce platform that lets international brands sell into Latin America. Acting as a Merchant of Record, it handles payment processing, currency exchange, logistics and fulfillment intelligence, customs and legal compliance, and storefront localization so merchants can expand into the region with a simple integration into their existing e-commerce stack. e-CROSS is a 500 Global portfolio company. Its public site runs on Wix and exposes a hosted, unauthenticated Model Context Protocol (MCP) server plus an llms.txt for agentic AI access to public site content; e-CROSS does not currently publish a first-party developer API, OpenAPI, or SDK.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/e-cross.png
layout: provider
mcp_servers:
- description: ''
  name: e-CROSS Site MCP (Wix)
  slug: e-cross-site-mcp-wix
modified: '2026-07-18'
name: e-CROSS
nav: Providers
network: true
overview: e-CROSS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cross-Border Commerce, E-Commerce, Merchant of Record, and Payments.
random_paper: 7
score:
  band: minimal
  composite: 2.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/e-cross/refs/heads/main/screenshots/e-cross-2026-07-25T212618.png
security:
- kind: domain-security
  name: E Cross Domain Security
  slug: e-cross-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: e-cross
tags:
- Company
- Cross-Border Commerce
- E-Commerce
- Merchant of Record
- Payments
- Logistics
- Latin America
- MCP
website: https://e-cross.tech
---
