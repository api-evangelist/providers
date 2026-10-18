---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Visible.vc providing access to portfolio data, metrics, contacts, and notes.
  name: Visible API
  slug: visible-api
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/plans/visible-vc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/visible-vc-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://visible.vc/security/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/llms/visible-vc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/visible-vc-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/mcp/visible-vc-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/visible-vc-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/well-known/visible-vc-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/visible-vc-status-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/well-known/visible-vc-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/visible-vc-help-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/well-known/visible-vc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/visible-vc-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/hosts/visible-vc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/visible-vc-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/vendors/visible-vc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/visible-vc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://visible.vc/terms
- group: operate
  title: ''
  type: Support
  url: https://help.visible.vc/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.visible.vc/
- group: auth
  title: ''
  type: Security
  url: https://visible.vc/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://visible.vc/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://visible.vc/pricing/
- group: company
  title: ''
  type: Blog
  url: https://visible.vc/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.visible.vc/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/security/visible-vc-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/visible-vc-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/visible-vc/refs/heads/main/security/visible-vc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/visible-vc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://visible.vc
coverage:
  checked: '2026-10-14'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract found at the API host.
  evidence:
  - status: 404
    url: https://api.visible.vc/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Visible.vc provides a platform for investors and founders to monitor portfolios, collect and verify data, and generate real-time reports. It offers an open API and MCP server to integrate private market data into workflows, supporting AI‑driven insights, secure data rooms, fundraising pipelines, and investor updates. Over 950 VC funds and 7,000 founders use Visible.vc to streamline capital raising and portfolio management.
image: https://visible.vc/_astro/open-graph-main.DNUHFpej.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at docs.visible.vc.
  name: Visible.vc MCP Server
  slug: visible-vc-mcp-yml
modified: '2026-10-14'
name: Visible.vc
nav: Providers
network: true
overview: 'Visible.vc is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Venture Capital, Portfolio Management, and Data Analytics.


  Visible.vc''s developer surface includes support, pricing, engineering blog, documentation, and 16 more developer resources.'
plans:
- name: Visible Vc Plans Pricing
  plan_count: 4
  slug: visible-vc-plans-pricing
random_paper: 0
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.0
    operational_transparency: 26.3
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Visible Vc Domain Security
  slug: visible-vc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Visible Vc Trust Center
  slug: visible-vc-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: visible-vc
tags:
- Company
- Fintech
- Venture Capital
- Portfolio Management
- Data Analytics
website: https://visible.vc
---
