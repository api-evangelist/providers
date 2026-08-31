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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'The WordPress core REST API served from the company''s marketing site. It is live, anonymous for published content, and self-describing: the discovery document at /wp-json/ lists 472 routes across 19 n'
  name: Droplet Biosciences WordPress REST API
  slug: droplet-biosciences-wordpress-rest-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://dropletbiosci.com/
- group: company
  title: ''
  type: About
  url: https://dropletbiosci.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://dropletbiosci.com/contact/
- group: other
  title: ''
  type: Team
  url: https://dropletbiosci.com/about/
- group: company
  title: ''
  type: Careers
  url: https://dropletbiosci.com/careers/
- group: company
  title: ''
  type: Press
  url: https://dropletbiosci.com/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://dropletbiosci.com/press-releases/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dropletbiosci.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dropletbiosci.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://dropletbiosci.com/certificates-licenses/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/droplet-biosciences-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/droplet-biosciences-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/droplet-biosciences-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/droplet-biosciences-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/droplet-biosciences-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/droplet-biosciences-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/droplet-biosciences-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/droplet-biosciences-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/droplet-biosciences-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/droplet-biosciences-llms.txt
created: '2026-08-12'
description: 'Droplet Biosciences is a Cambridge, Massachusetts clinical-stage molecular diagnostics company, founded in 2021 by physician scientists and backed by The Engine Ventures, that has pioneered a lymph liquid biopsy platform for detecting molecular residual disease after cancer surgery. Rather than sampling blood, Droplet stabilizes and extracts lymphatic fluid from routine post-surgical drain material through a proprietary isolation process, yielding an analyte source in which circulating tumor DNA is present at substantially higher levels than in matched plasma. Its lead test, LymphDetect, is an ultra-sensitive tumor-informed ctDNA assay initially targeting HPV-independent head and neck squamous cell carcinoma, run out of the company''s own CLIA-licensed laboratory. Droplet is a laboratory and assay company, not a software vendor: it publishes no developer program, no documentation, no SDK and no OpenAPI. The machine-readable endpoints catalogued here are not a product API —
  they are the WordPress REST API, an OAuth 2.0 authorization server and three Model Context Protocol endpoints emitted by plugins on the company''s marketing site, all found live and callable on dropletbiosci.com during contract discovery on 2026-08-12.'
image: https://dropletbiosci.com/wp-content/uploads/2022/10/cropped-Droplet-Favicon-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: Droplet Biosciences MCP Server
  slug: droplet-biosciences-mcp-server
modified: '2026-08-12'
name: Droplet Biosciences
nav: Providers
network: true
overview: 'Droplet Biosciences publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Diagnostics, and Oncology.


  Droplet Biosciences'' developer surface includes authentication and 19 more developer resources.'
plans:
- name: Droplet Biosciences Plans Pricing
  plan_count: 0
  slug: droplet-biosciences-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Droplet Biosciences Rate Limits
  slug: droplet-biosciences-rate-limits
scopes:
- name: Droplet Biosciences Scopes
  scope_count: 1
  slug: droplet-biosciences-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Droplet Biosciences Authentication
  slug: droplet-biosciences-authentication
  summary_line: none/oauth2/http · 3 schemes
- kind: domain-security
  name: Droplet Biosciences Domain Security
  slug: droplet-biosciences-domain-security
  summary_line: TLSv1.3 · DMARC
slug: droplet-biosciences
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Oncology
- Genomics
- Liquid Biopsy
- Life Sciences
- Biotechnology
- Clinical Laboratory
website: https://dropletbiosci.com/
---
