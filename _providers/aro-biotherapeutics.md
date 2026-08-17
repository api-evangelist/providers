---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: A live, anonymously reachable Model Context Protocol endpoint served from Aro Biotherapeutics' own host and advertised in the site's llms.txt. It is provided by the Wix platform, not built by Aro — it
  name: Aro Biotherapeutics Site MCP
  slug: site-mcp
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.arobiotx.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/aro-biotherapeutics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aro-biotherapeutics-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/aro-biotherapeutics-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aro-biotherapeutics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aro-biotherapeutics-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.arobiotx.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.arobiotx.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arobiotx.com/legal-notices
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arobiotx.com/privacy-policy
created: '2026-08-06'
description: Aro Biotherapeutics is a Philadelphia-based biotechnology company developing tissue-targeted genetic medicines built on Centyrins, a proprietary engineered human protein scaffold that is small, stable and highly soluble. Aro conjugates Centyrins to oligonucleotide payloads (Centyrin-siRNA conjugates) to deliver RNA- and DNA-based therapeutics precisely to cells and tissues outside the liver, including muscle and immune cells. Its lead program, ABX1100, is a CD71-targeted Centyrin-siRNA conjugate for Pompe disease that has received FDA orphan drug designation. The company is privately held, raised a $41.5M Series B led by Cowen Healthcare Investments with participation from Johnson & Johnson Innovation, and is headquartered at 601 Walnut Street, Philadelphia, PA. Aro publishes no developer program, API reference or SDK; the only machine-readable surface on its domain is the Wix-platform llms.txt and Site MCP endpoint.
image: https://static.wixstatic.com/media/55e8e9_a8e1814d42074178825df49af5a75963~mv2.jpg/v1/fill/w_1851,h_930,al_c/55e8e9_a8e1814d42074178825df49af5a75963~mv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: aro-biotherapeutics-mcp.yml
  slug: aro-biotherapeutics-mcpyml
modified: '2026-08-06'
name: Aro Biotherapeutics
nav: Providers
network: true
overview: 'Aro Biotherapeutics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Genetic Medicine, and Life Sciences.


  Aro Biotherapeutics'' developer surface includes authentication, engineering blog, support, and 7 more developer resources.'
random_paper: 41
score:
  band: emerging
  composite: 20.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 26.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 20.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aro-biotherapeutics/refs/heads/main/screenshots/aro-biotherapeutics-2026-08-07T161732.png
security:
- kind: authentication
  name: Aro Biotherapeutics Authentication
  slug: aro-biotherapeutics-authentication
  summary_line: none/session-token · 2 schemes
- kind: domain-security
  name: Aro Biotherapeutics Domain Security
  slug: aro-biotherapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aro-biotherapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Genetic Medicine
- Life Sciences
- Pharmaceuticals
- Model Context Protocol
website: https://www.arobiotx.com/
---
