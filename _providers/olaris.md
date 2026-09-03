---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Unauthenticated remote Model Context Protocol endpoint served from Olaris' own host at https://www.myolaris.com/_api/mcp. It is the Wix platform Site MCP — provisioned by the website platform, not a f
  name: Olaris Site MCP
  slug: olaris-site-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.myolaris.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/olaris-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/olaris-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/olaris-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.myolaris.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/olarisbor
- group: auth
  title: ''
  type: DomainSecurity
  url: security/olaris-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/olaris-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/olaris-rate-limits.yml
created: '2026-08-26'
description: Olaris, Inc. is a precision-medicine diagnostics company in Framingham, Massachusetts, founded in 2014 by Elizabeth O'Day, that combines mass-spectrometry and NMR metabolomics with machine learning to turn metabolite signatures into clinical biomarkers of response. Its lead product, myOLARIS-KTdx, is a non-invasive urine test for surveillance of kidney graft injury in transplant recipients — including borderline, subclinical and clinical rejection and polyomavirus-associated nephropathy — run in the company's own CLIA-certified laboratory and distributed through a commercial collaboration with Labcorp. Olaris also sells biomarker discovery services to biopharma and is advancing a diagnostics pipeline across oncology, solid-organ transplant and neurodegeneration. Olaris publishes no public developer program, API reference or machine-readable API contract; its only machine-readable surfaces are the platform-generated llms.txt and Wix Site MCP endpoint served from its own marketing
  host.
image: https://static.wixstatic.com/media/e0d525_f21b71a783bf417e951f6808527da944~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: Olaris Site MCP
  slug: olaris-site-mcp
modified: '2026-08-26'
name: Olaris
nav: Providers
network: true
overview: 'Olaris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, Precision Medicine, and Metabolomics.


  Olaris'' developer surface includes authentication, support, and 7 more developer resources.'
plans:
- name: Olaris Plans Pricing
  plan_count: 0
  slug: olaris-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Olaris Rate Limits
  slug: olaris-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/olaris/refs/heads/main/screenshots/olaris-2026-09-02T150837.png
security:
- kind: authentication
  name: Olaris Authentication
  slug: olaris-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Olaris Domain Security
  slug: olaris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: olaris
tags:
- Company
- Healthcare
- Diagnostics
- Precision Medicine
- Metabolomics
- Machine-Learning
- Biomarkers
- Laboratory
- Transplant
- Life Sciences
website: https://www.myolaris.com/
---
