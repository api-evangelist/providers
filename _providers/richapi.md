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
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: RichAPI Backend API providing data enrichment and MCP endpoints.
  name: RichAPI Backend API
  slug: richapi-backend-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/plans/richapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/richapi-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://richapi.ai/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/authentication/richapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/richapi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/conformance/richapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/richapi-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/llms/richapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/richapi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/mcp/richapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/richapi-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/well-known/richapi-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/richapi-vercel-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/well-known/richapi-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/richapi-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/well-known/richapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/richapi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/hosts/richapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/richapi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/vendors/richapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/richapi-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/packages/richapi-packages.yml
  title: ''
  type: SDKs
  url: packages/richapi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/packages/richapi-packages.yml
  title: ''
  type: Packages
  url: packages/richapi-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.richapi.ai
- group: auth
  title: ''
  type: Security
  url: https://richapi.ai/security
- group: start
  title: ''
  type: Login
  url: https://app.richapi.ai/auth/sign-in
- group: docs
  title: ''
  type: APIReference
  url: https://richapi.ai/developers
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/security/richapi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/richapi-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/richapi/refs/heads/main/security/richapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/richapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://richapi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://app.richapi.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.richapi.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://richapi.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://richapi.ai/blog
created: '2026-10-02'
description: RichAPI provides a B2B data enrichment platform and Managed Customer Platform (MCP) that aggregates over 65 GTM data endpoints across categories such as company enrichment, contact finding, social signals, and webscraping. With a single API key and credit pool, developers can integrate live contact, company, and signal data into applications, CRMs, and AI assistants. The service offers a free tier with 25 credits, flexible pricing, and extensive documentation for quick onboarding.
image: https://richapi.ai/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: RichAPI MCP Server
  slug: richapi-mcp-server
modified: '2026-10-02'
name: RichAPI
nav: Providers
network: true
overview: 'RichAPI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Enrichment, B2B, and MCP.


  RichAPI''s developer surface includes authentication, API reference, documentation, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Richapi Plans Pricing
  plan_count: 5
  slug: richapi-plans-pricing
random_paper: 10
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 66.7
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Richapi Authentication
  slug: richapi-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Richapi Domain Security
  slug: richapi-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Richapi Trust Center
  slug: richapi-trust-center
  summary_line: SOC 2, GDPR
slug: richapi
tags:
- Company
- Data Enrichment
- B2B
- MCP
website: https://richapi.ai/
---
