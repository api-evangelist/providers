---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://veesion.io/en/
- group: company
  title: ''
  type: Blog
  url: https://veesion.io/en/blog-veesion/
- group: operate
  title: ''
  type: Support
  url: https://veesion.io/en/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veesion.io/en/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veesion.io/en/legal/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/veesion-io
- group: start
  title: ''
  type: CustomerPortal
  url: https://portal.veesion.io/
- group: auth
  title: ''
  type: Compliance
  url: conformance/veesion-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/veesion-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: 'Veesion ships AI shoplifting detection as an installed end-user product for store staff — a mobile alert app plus an on-site appliance — and publishes no developer surface at all: the word "API" does not appear in the copy of any of the 157 pages in its own sitemap, and every contract-discovery probe (OpenAPI, Swagger, GraphQL, WSDL, MCP tools/list, A2A agent card) missed on veesion.io, www.veesion.io, portal.veesion.io, veesion.pro and demo.veesion.io.'
  evidence:
  - status: 404
    url: https://veesion.io/llms.txt
  - status: 404
    url: https://veesion.io/openapi.json
  - status: 404
    url: https://veesion.io/.well-known/agent-card.json
  - status: 404
    url: https://veesion.io/.well-known/security.txt
  - status: 404
    url: https://veesion.io/en/pricing/
  - status: 401
    url: https://veesion.io/wp-json/
  - status: 404
    url: https://veesion.pro/openapi.json
  - status: 200
    url: https://veesion.io/page-sitemap1.xml
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: Veesion is a French computer-vision company that sells AI-powered shoplifting detection to retailers. Its gesture-recognition models run against a store's existing CCTV cameras — either on a compact on-site server or through a serverless integration — and analyse body movement and concealment behaviour rather than faces, so no biometric identification is performed. When a pattern associated with theft is recognised, the store team receives a short video alert in a mobile app for review. Founded in 2018 and headquartered in Bordeaux, France (Veesion SAS, RCS Nanterre 838 664 274), the company operates across supermarkets, hypermarkets, pharmacies and independent retail stores in more than 25 countries, and raised a EUR 38M Series B to expand its AI-powered loss-prevention platform. Veesion is sold as an end-user product through a direct and partner sales motion; it publishes no public developer program, API reference, SDK or machine-readable contract.
image: https://veesion.io/wp-content/uploads/2023/06/veesion_gradiente.png
layout: provider
modified: '2026-09-02'
name: Veesion
nav: Providers
network: true
overview: 'Veesion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Computer Vision, Video Surveillance, and Retail.


  Veesion''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Veesion Plans Pricing
  plan_count: 0
  slug: veesion-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Veesion Rate Limits
  slug: veesion-rate-limits
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 15.1
  provenance:
    conformance: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Veesion Domain Security
  slug: veesion-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: veesion
tags:
- Company
- Artificial Intelligence
- Computer Vision
- Video Surveillance
- Retail
- Loss Prevention
- Physical Security
- Gesture Recognition
- France
website: https://veesion.io/en/
---
