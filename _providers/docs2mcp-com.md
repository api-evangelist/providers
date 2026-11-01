---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 8.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Hosted MCP server that stores uploaded documents and provides searchable AI-powered access via a streamable HTTP endpoint.
  name: docs2mcp MCP API
  slug: docs2mcp-mcp-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/docs2mcp-com/plans/docs2mcp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docs2mcp-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/docs2mcp-com/authentication/docs2mcp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/docs2mcp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/docs2mcp-com/conformance/docs2mcp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docs2mcp-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/docs2mcp-com/hosts/docs2mcp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docs2mcp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/docs2mcp-com/vendors/docs2mcp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docs2mcp-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs2mcp.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://app.docs2mcp.com/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs2mcp.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs2mcp.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.docs2mcp.com/login/
- group: docs
  title: ''
  type: Documentation
  url: https://docs2mcp.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/docs2mcp
- group: auth
  href: https://artifacts.apis.io/docs2mcp-com/security/docs2mcp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docs2mcp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs2mcp.com/
coverage:
  checked: '2026-10-30'
  detail: Public documentation is available but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be retrieved.
  evidence:
  - status: 403
    url: https://api.docs2mcp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: docs2mcp provides a custom deployment that turns your documents into a Model Context Protocol (MCP) server, enabling AI assistants such as Claude, ChatGPT, Perplexity, Gemini, Cursor, and Copilot Studio to query your own PDFs, Word files, spreadsheets, presentations, CSVs and images. It offers full source attribution by linking each AI answer back to the exact sentence, table row, or figure in the original document. Users can upload documents once and reuse them across unlimited sessions, with no file limits, and benefit from automatic indexing, chunking and embedding for searchable knowledge bases.
image: https://docs2mcp.com/logo.svg
layout: provider
modified: '2026-10-30'
name: docs2mcp-com
nav: Providers
network: true
overview: 'docs2mcp-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Document Management, MCP, Integration, and Cloud.


  docs2mcp-com''s developer surface includes authentication, support, pricing, documentation, and 10 more developer resources.'
plans:
- name: Docs2Mcp Com Plans Pricing
  plan_count: 5
  slug: docs2mcp-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Docs2Mcp Com Rate Limits
  slug: docs2mcp-com-rate-limits
scopes:
- name: Docs2Mcp Com Scopes
  scope_count: 0
  slug: docs2mcp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Docs2Mcp Com Authentication
  slug: docs2mcp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Docs2Mcp Com Domain Security
  slug: docs2mcp-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: docs2mcp-com
tags:
- AI
- Document Management
- MCP
- Integration
- Cloud
website: https://docs2mcp.com/
---
