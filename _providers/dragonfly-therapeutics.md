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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 13.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Model Context Protocol endpoint served from the Dragonfly Therapeutics website host. This is a platform-provided surface automatically provisioned by Wix for every site it builds — not a first-party D
  name: Dragonfly Therapeutics Site MCP
  slug: dragonfly-therapeutics-site-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.dragonflytx.com/
- group: company
  title: ''
  type: Blog
  url: https://www.dragonflytx.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.dragonflytx.com/blog-feed.xml
- group: company
  title: ''
  type: News
  url: https://www.dragonflytx.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dragonflytx.com/_files/ugd/cb0357_e5861f3f611f4e3091162162753c2083.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dragonfly-therapeutics-inc.
- group: other
  title: ''
  type: Profile
  url: https://www.hiive.com/securities/dragonfly-therapeutics-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dragonfly-therapeutics-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dragonfly-therapeutics-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dragonfly-therapeutics-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dragonfly-therapeutics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dragonfly-therapeutics-domain-security.yml
coverage:
  checked: '2026-08-12'
  detail: Dragonfly Therapeutics is a clinical-stage NK-cell immunotherapy developer whose product is a drug pipeline, not software; the whole site is ten Wix pages with no developer, API or docs route, and the only machine-readable surfaces (llms.txt and a /_api/mcp endpoint) are boilerplate auto-provisioned by Wix rather than anything the company authored.
  evidence:
  - status: 404
    url: https://www.dragonflytx.com/developers
  - status: 404
    url: https://www.dragonflytx.com/api-docs
  - status: 400
    url: https://www.dragonflytx.com/openapi.json
  - status: 400
    url: https://www.dragonflytx.com/.well-known/agent-card.json
  - status: 200
    url: https://www.dragonflytx.com/llms.txt
  - status: 200
    url: https://www.dragonflytx.com/_api/mcp
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: 'Dragonfly Therapeutics is a clinical-stage biotechnology company based in Waltham, Massachusetts, founded in 2016 by Tyler Jacks, Bill Haney and David Raulet to develop natural killer (NK) cell-based immunotherapies. Its proprietary TriNKET (Tri-specific NK cell Engager Therapy) and cytokine engager platforms produce molecules that bind both a tumor or disease antigen and an NK cell activating receptor, recruiting innate and adaptive immunity against cancer, autoimmune disease, fibrosis and neuro-inflammation. Lead clinical candidate DF1001 targets HER2 in advanced solid tumors, and the platform is licensed under multi-target collaborations with AbbVie, Bristol Myers Squibb, Merck and Gilead. Dragonfly is a therapeutics developer rather than a software company: it publishes no developer program, no public API, no SDKs and no machine-readable API contract. The only agent-readable surfaces on its own host are the llms.txt and Model Context Protocol endpoint automatically provisioned
  by its Wix website platform.'
layout: provider
mcp_servers:
- description: ''
  name: Dragonfly Therapeutics MCP Server
  slug: dragonfly-therapeutics-mcp-server
modified: '2026-08-12'
name: Dragonfly Therapeutics
nav: Providers
network: true
overview: 'Dragonfly Therapeutics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Immunotherapy, and Oncology.


  Dragonfly Therapeutics'' developer surface includes engineering blog, product news, authentication, and 9 more developer resources.'
plans:
- name: Dragonfly Therapeutics Plans Pricing
  plan_count: 0
  slug: dragonfly-therapeutics-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Dragonfly Therapeutics Rate Limits
  slug: dragonfly-therapeutics-rate-limits
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.5
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 26.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Dragonfly Therapeutics Authentication
  slug: dragonfly-therapeutics-authentication
  summary_line: none/bearer-visitor-token · 2 schemes
- kind: domain-security
  name: Dragonfly Therapeutics Domain Security
  slug: dragonfly-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dragonfly-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Immunotherapy
- Oncology
- Life Sciences
- Clinical Stage
- Drug Discovery
- Healthcare
website: https://www.dragonflytx.com/
---
