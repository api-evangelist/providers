---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    auth_clarity: served
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Remote Model Context Protocol server (Streamable HTTP, JSON-RPC 2.0, no authentication) that lets AI assistants look up Denia Print products, options and exact prices, read shop information, request q
  name: Denia Print MCP Connector
  slug: denia-print-mcp-connector
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/deniaprint-es/conventions/deniaprint-es-conventions.yml
  title: ''
  type: Conventions
  url: conventions/deniaprint-es-conventions.yml
- group: auth
  href: https://artifacts.apis.io/deniaprint-es/authentication/deniaprint-es-authentication.yml
  title: ''
  type: Authentication
  url: authentication/deniaprint-es-authentication.yml
- group: agent
  href: https://artifacts.apis.io/deniaprint-es/llms/deniaprint-es-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deniaprint-es-llms.txt
- group: agent
  href: https://artifacts.apis.io/deniaprint-es/mcp/deniaprint-es-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/deniaprint-es-mcp.yml
- group: agent
  href: https://artifacts.apis.io/deniaprint-es/well-known/deniaprint-es-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deniaprint-es-well-known.yml
- group: other
  href: https://artifacts.apis.io/deniaprint-es/hosts/deniaprint-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deniaprint-es-hosts.yml
- group: build
  href: https://artifacts.apis.io/deniaprint-es/integrations/deniaprint-es-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/deniaprint-es-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/deniaprint-es/vendors/deniaprint-es-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deniaprint-es-vendors.yml
- group: auth
  href: https://artifacts.apis.io/deniaprint-es/security/deniaprint-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deniaprint-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deniaprint.es/
- group: docs
  title: Denia Print en tu asistente de IA (MCP connector guide)
  type: Documentation
  url: https://deniaprint.es/asistentes-ia
- group: start
  title: ''
  type: Login
  url: https://dashboard.deniaprint.es/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deniaprint.es/condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deniaprint.es/privacidad
- group: commercial
  title: ''
  type: LegalNotice
  url: https://deniaprint.es/aviso-legal
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/deniaprint
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/deniaprint/
created: '2026-11-05'
description: 'Denia Print is a local online print shop (imprenta) based in Dénia (Alicante, Spain) serving businesses across the Marina Alta: business cards, flyers, restaurant menus, banners, vinyl and signage with installation, textiles, merchandising, packaging and graphic design. Every product has an instant online price calculator and online design, with free file review and a digital proof before printing. Denia Print also publishes a remote MCP connector (https://deniaprint.es/mcp) so AI assistants such as Claude and ChatGPT can look up products, prices, options and lead times, request quotes and check order status without an account or key.'
image: https://deniaprint.es/brand/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at deniaprint.es; 8 tools listed.
  name: Denia Print MCP Server
  slug: denia-print
modified: '2026-11-05'
name: Denia Print
nav: Providers
network: true
overview: 'Denia Print is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Printing, Print on Demand, E-Commerce, and Signage.


  Denia Print''s developer surface includes authentication, documentation, and 15 more developer resources.'
plans:
- name: Deniaprint Es Plans Pricing
  plan_count: 0
  slug: deniaprint-es-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Deniaprint Es Rate Limits
  slug: deniaprint-es-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 71.7
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Deniaprint Es Authentication
  slug: deniaprint-es-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Deniaprint Es Domain Security
  slug: deniaprint-es-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deniaprint-es
tags:
- Company
- Printing
- Print on Demand
- E-Commerce
- Signage
- Graphic Design
- MCP
- Spain
website: https://deniaprint.es/
---
