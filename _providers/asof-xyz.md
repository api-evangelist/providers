---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for retrieving wallet holdings reports and related billing information.
  name: AsOf API
  slug: asof-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/asof-xyz/plans/asof-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asof-xyz-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/asof-xyz/llms/asof-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asof-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/asof-xyz/mcp/asof-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asof-xyz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/asof-xyz/well-known/asof-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asof-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/asof-xyz/hosts/asof-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asof-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/asof-xyz/vendors/asof-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asof-xyz-vendors.yml
- group: auth
  href: https://artifacts.apis.io/asof-xyz/security/asof-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asof-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asof.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://asof.xyz/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://asof.xyz/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asof.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asof.xyz/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://asof.xyz/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://asof.xyz/mcp
coverage:
  checked: '2026-10-30'
  detail: Documentation is rendered via JavaScript and provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://asof.xyz/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: AsOf provides a web‑based platform that generates wallet holdings reports by connecting to users’ preferred large language models (LLMs). Users can view balances, values, and download clear reports. The service offers a free demo, subscription pricing, and integrates with Supabase for data storage. It emphasizes privacy, acceptable use, and provides developer resources via its MCP at /mcp.
image: https://asof.xyz/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.asof.xyz.
  name: asof-xyz MCP Server
  slug: asof-xyz-mcp-yml
modified: '2026-10-29'
name: asof-xyz
nav: Providers
network: true
overview: 'asof-xyz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Crypto, Wallet, and Analytics.


  asof-xyz''s developer surface includes documentation, pricing, getting-started guide, and 11 more developer resources.'
plans:
- name: Asof Xyz Plans Pricing
  plan_count: 8
  slug: asof-xyz-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Asof Xyz Rate Limits
  slug: asof-xyz-rate-limits
scopes:
- name: Asof Xyz Scopes
  scope_count: 0
  slug: asof-xyz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Asof Xyz Authentication
  slug: asof-xyz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Asof Xyz Domain Security
  slug: asof-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asof-xyz
tags:
- Company
- Finance
- Crypto
- Wallet
- Analytics
- API
website: https://asof.xyz/
---
