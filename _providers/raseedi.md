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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://raseediapp.com
- group: company
  title: ''
  type: Blog
  url: https://www.raseediapp.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.raseediapp.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/raseedi-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/raseedi-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raseedi-domain-security.yml
created: '2026-07-17'
description: Raseedi is an Egyptian financial technology platform that helps underbanked users manage their spending and save money. Through its mobile app it offers free and discounted calls, mobile top-ups and bill payments, cash loans, and a smart dialer, building a community for financial control and savings. Surfaced as a portfolio company of 500 Global and added to the API Evangelist network, Raseedi runs a Wix-hosted marketing site with no first-party developer API; its only machine-readable surface is a published llms.txt and the generic Wix Site MCP endpoint.
image: https://raseediapp.com/favicon.ico
layout: provider
mcp_servers:
- description: 'Raseedi''s marketing site (raseediapp.com) is hosted on Wix and exposes the generic Wix Site MCP endpoint. This is platform-provided infrastructure, NOT a first-party Raseedi product API. It answers a '
  name: Raseedi Site MCP
  slug: raseedi-site-mcp
modified: '2026-07-20'
name: Raseedi
nav: Providers
network: true
overview: 'Raseedi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial-Services, Mobile Payments, and Egypt.


  Raseedi''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 13.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/raseedi/refs/heads/main/screenshots/raseedi-2026-09-02T152905.png
security:
- kind: domain-security
  name: Raseedi Domain Security
  slug: raseedi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: raseedi
tags:
- Company
- Fintech
- Financial-Services
- Mobile Payments
- Egypt
- Lending
- Telecom
- Financial Inclusion
website: https://raseediapp.com
---
