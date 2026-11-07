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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://alderinvoices.com
  baseurl_source: declared
  description: The Drafts API from Alder — 1 operation(s) for drafts.
  name: Alder Drafts API
  slug: alderinvoices-com-drafts-api
- baseURL: https://alderinvoices.com
  baseurl_source: declared
  description: The Pdf API from Alder — 1 operation(s) for pdf.
  name: Alder PDF API
  slug: alderinvoices-com-pdf-api
- baseURL: https://alderinvoices.com
  baseurl_source: declared
  description: The Template Drafts API from Alder — 1 operation(s) for template drafts.
  name: Alder Template Drafts API
  slug: alderinvoices-com-template-drafts-api
- baseURL: https://alderinvoices.com
  baseurl_source: declared
  description: The Templates API from Alder — 1 operation(s) for templates.
  name: Alder Templates API
  slug: alderinvoices-com-templates-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/alderinvoices-com/data-model/alderinvoices-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alderinvoices-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/alderinvoices-com/errors/alderinvoices-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alderinvoices-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/alderinvoices-com/llms/alderinvoices-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alderinvoices-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/alderinvoices-com/mcp/alderinvoices-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alderinvoices-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/alderinvoices-com/hosts/alderinvoices-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alderinvoices-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/alderinvoices-com/vendors/alderinvoices-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alderinvoices-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/alderinvoices-com/security/alderinvoices-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alderinvoices-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alderinvoices.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://alderinvoices.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://alderinvoices.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://alderinvoices.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://alderinvoices.com/developers
- group: operate
  title: ''
  type: Support
  url: https://alderinvoices.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alderinvoices.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alderinvoices.com/privacy
created: '2026-11-01'
description: Alder provides a free, web‑based invoice generator that lets users create professional PDF invoices without an account. The service includes a REST API and a Machine‑Control‑Protocol (MCP) for AI agents, enabling programmatic invoice creation, customization of logos, line items, taxes, discounts, and PDF download. Alder’s platform is open, requires no sign‑up, and offers unlimited invoice generation for individuals and businesses.
image: https://alderinvoices.com/alder-logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at alderinvoices.com.
  name: Alder MCP Server
  slug: alderinvoices-com-mcp-yml
modified: '2026-11-01'
name: Alder
nav: Providers
network: true
overview: 'Alder publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Drafts API, PDF API, Template Drafts API, and 1 more. Tagged areas include Invoices, Finance, PDF, Free, and MCP.


  Alder''s developer surface includes documentation, API reference, getting-started guide, support, and 11 more developer resources.'
random_paper: 20
scopes:
- name: Alderinvoices Com Scopes
  scope_count: 0
  slug: alderinvoices-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 44.4
    developer_ergonomics: 21.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 31.7
  provenance:
    conformance: unknown
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alderinvoices Com Authentication
  slug: alderinvoices-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alderinvoices Com Domain Security
  slug: alderinvoices-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alderinvoices-com
tags:
- Invoices
- Finance
- PDF
- Free
- MCP
website: https://alderinvoices.com/
---
