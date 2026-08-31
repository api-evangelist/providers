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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trexbio-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://trex.bio/
- group: company
  title: ''
  type: About
  url: https://trex.bio/about-trex-bio/
- group: other
  title: ''
  type: Platform
  url: https://trex.bio/deep-biology-platform/
- group: other
  title: ''
  type: Pipeline
  url: https://trex.bio/pipeline/
- group: company
  title: ''
  type: Blog
  url: https://trex.bio/news/
- group: company
  title: ''
  type: BlogFeeds
  url: https://trex.bio/feed/
- group: other
  title: ''
  type: Research
  url: https://trex.bio/news/
- group: company
  title: ''
  type: Careers
  url: https://trex.bio/careers/
- group: operate
  title: ''
  type: Contact
  url: https://trex.bio/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trex.bio/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trex.bio/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://trex.bio/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trexbio-inc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trexbio
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/trexbio_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trexbio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trexbio-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trexbio-domain-security.yml
coverage:
  checked: '2026-08-05'
  detail: 'TRexBio is a clinical-stage Treg biologics company with no developer program at all — trex.bio is a WordPress/WP Engine marketing site, and the only machine-readable things on it are stock CMS plumbing: the WordPress core REST API at /wp-json/ (342 routes, all of them WordPress and plugin routes), a Yoast-SEO-generated /llms.txt listing news posts and careers pages, and an undocumented WordPress MCP adapter at /wp-json/mcp/mcp-oauth-server that returns 401 mcp_unauthorized to anonymous tools/list — there is no product API, no /openapi.json, no docs host, and github.com/trexbio has zero public repositories.'
  evidence:
  - status: 404
    url: https://trex.bio/openapi.json
  - status: 404
    url: https://trex.bio/graphql
  - status: 404
    url: https://trex.bio/.well-known/agent-card.json
  - status: 401
    url: https://trex.bio/wp-json/mcp/mcp-oauth-server
  - status: 200
    url: https://trex.bio/llms.txt
  - status: 200
    url: https://api.github.com/orgs/trexbio/repos
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: TRexBio, Inc. is a clinical-stage biotechnology company headquartered at 681 Gateway Blvd in South San Francisco, California, founded in 2018 and seed funded by SV Health Investors, that discovers and develops immunoregulatory biologics based on tissue regulatory T cell (Treg) biology. Its Deep Biology Platform combines human tissue samples, computational biology and immunobiology expertise to map how tissue Tregs behave in disease and to identify and characterize novel targets for inflammatory, autoimmune and other immune-mediated conditions. Disclosed programs include TRB-061, the CD30 agonist TRB-071, TRB-081, and the Lilly-partnered TRB-051, with Phase 1 trials expected to initiate in 2027. The company announced an $84 million Series B in November 2024 and closed a further $50 million financing in January 2026; investors include Eli Lilly and Company, Pfizer Ventures, Johnson & Johnson, SV Health Investors and Polaris Partners. TRexBio publishes no developer program, API
  documentation, SDK or machine-readable API contract. trex.bio is a WordPress marketing site whose only machine-readable surfaces are the WordPress core REST API, a Yoast-generated llms.txt, and an OAuth-protected WordPress MCP adapter endpoint — CMS infrastructure rather than a product API.
image: https://trex.bio/wp-content/uploads/2025/10/cropped-Group-3.png
layout: provider
mcp_servers:
- description: ''
  name: TRexBio MCP Server
  slug: trexbio-mcp-server
modified: '2026-08-05'
name: TRexBio
nav: Providers
network: true
overview: 'TRexBio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Life Sciences, Pharmaceuticals, and Immunology.


  TRexBio''s developer surface includes engineering blog and 18 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 10.6
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Trexbio Domain Security
  slug: trexbio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trexbio
tags:
- Company
- Biotechnology
- Life Sciences
- Pharmaceuticals
- Immunology
- Drug Discovery
- Regulatory T Cells
- Clinical Stage
- Computational Biology
- Therapeutics
- South San Francisco
website: https://trex.bio/
---
