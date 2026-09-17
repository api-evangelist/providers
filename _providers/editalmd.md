---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Alertas API from EditalMD — 3 operation(s) for alertas.
  name: EditalMD Alertas API
  slug: editalmd-alertas-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Apis.json API from EditalMD — 1 operation(s) for apis.json.
  name: EditalMD Apis.json API
  slug: editalmd-apis-json-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Busca API from EditalMD — 1 operation(s) for busca.
  name: EditalMD Busca API
  slug: editalmd-busca-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Cnaes API from EditalMD — 1 operation(s) for cnaes.
  name: EditalMD Cnaes API
  slug: editalmd-cnaes-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Compra API from EditalMD — 1 operation(s) for compra.
  name: EditalMD Compra API
  slug: editalmd-compra-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Credito API from EditalMD — 1 operation(s) for credito.
  name: EditalMD Credito API
  slug: editalmd-credito-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Documento API from EditalMD — 2 operation(s) for documento.
  name: EditalMD Documento API
  slug: editalmd-documento-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Dono API from EditalMD — 3 operation(s) for dono.
  name: EditalMD Dono API
  slug: editalmd-dono-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Editalmd API from EditalMD — 1 operation(s) for editalmd.
  name: EditalMD Editalmd API
  slug: editalmd-editalmd-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Feed.json API from EditalMD — 1 operation(s) for feed.json.
  name: EditalMD Feed.json API
  slug: editalmd-feed-json-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Feed.xml API from EditalMD — 1 operation(s) for feed.xml.
  name: EditalMD Feed.xml API
  slug: editalmd-feed-xml-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Health API from EditalMD — 1 operation(s) for health.
  name: EditalMD Health API
  slug: editalmd-health-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Mcp API from EditalMD — 1 operation(s) for mcp.
  name: EditalMD MCP API
  slug: editalmd-mcp-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Metrics API from EditalMD — 1 operation(s) for metrics.
  name: EditalMD Metrics API
  slug: editalmd-metrics-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Okf API from EditalMD — 1 operation(s) for okf.
  name: EditalMD Okf API
  slug: editalmd-okf-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Recibo API from EditalMD — 1 operation(s) for recibo.
  name: EditalMD Recibo API
  slug: editalmd-recibo-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Vigias API from EditalMD — 3 operation(s) for vigias.
  name: EditalMD Vigias API
  slug: editalmd-vigias-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The Visit API from EditalMD — 1 operation(s) for visit.
  name: EditalMD Visit API
  slug: editalmd-visit-api
- baseURL: https://editalmd.com/api/
  baseurl_source: declared
  description: The .well Known API from EditalMD — 1 operation(s) for .well known.
  name: EditalMD .well Known API
  slug: editalmd-well-known-api
artifact_total: 27
asyncapis:
- description: ''
  name: Editalmd Webhooks
  slug: editalmd-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://editalmd.com/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/editalmd/refs/heads/main/mcp/editalmd-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/editalmd-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/editalmd/refs/heads/main/overlays/editalmd-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/editalmd-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/editalmd/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://editalmd.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/editalmd/refs/heads/main/security/editalmd-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/editalmd-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/editalmd/refs/heads/main/security/editalmd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/editalmd-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/editalmd/refs/heads/main/security/editalmd-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/editalmd-vulnerability-disclosure.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/editalmd/refs/heads/main/well-known/editalmd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/editalmd-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/editalmd/refs/heads/main/well-known/editalmd-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/editalmd-security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://editalmd.com/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://editalmd.com/privacidade
- group: commercial
  title: ''
  type: Pricing
  url: https://editalmd.com/#precos
created: '2026-09-05'
description: Agent-native data API over Brazil's public-procurement portal PNCP (Portal Nacional de Contratações Públicas). Provides full-text tender search, proposal and challenge deadlines, editais rendered as markdown with provenance and SHA-256 hashes, new-tender alerts by keyword or CNPJ, tender change-watchers, and extracted eligibility (habilitação) checklists. Search is free; other routes are paid per request (x402) or via prepaid credit with no signup.
image: https://editalmd.com/icon.svg
layout: provider
mcp_servers:
- description: ''
  name: EditalMD MCP Server
  slug: editalmd-mcp-server
- description: 'Hosted first-party MCP server (Streamable HTTP, JSON-RPC 2.0) dispatched by the same Cloudflare Worker as the REST API. Exposes 19 tools covering the whole product: free PNCP tender search, tender she'
  name: EditalMD MCP Server
  slug: editalmd-mcp-server-2
modified: '2026-09-05'
name: EditalMD
nav: Providers
network: true
overview: 'EditalMD publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Alertas API, Apis.json API, Busca API, and 16 more. Tagged areas include GovTech, Public Procurement, Brazil, PNCP, and Legal & Compliance.


  The EditalMD catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  EditalMD''s developer surface includes pricing and 12 more developer resources.'
plans:
- name: Editalmd Plans Pricing
  plan_count: 0
  slug: editalmd-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Editalmd Rate Limits
  slug: editalmd-rate-limits
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 57.8
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 39.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 43.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Editalmd Authentication
  slug: editalmd-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Editalmd Domain Security
  slug: editalmd-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Editalmd Vulnerability Disclosure
  slug: editalmd-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: editalmd
tags:
- GovTech
- Public Procurement
- Brazil
- PNCP
- Legal & Compliance
- Business Intelligence
- Company Data
- CNPJ
- CNAE
- SICAF
- Document Extraction
- agent-native
- MCP
- x402
- Machine-Payable
website: https://editalmd.com
---
