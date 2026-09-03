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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upstream-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upstreambio.com/
- group: company
  title: ''
  type: About
  url: https://upstreambio.com/about/
- group: company
  title: ''
  type: Blog
  url: https://investors.upstreambio.com/news-events/news-releases
- group: company
  title: ''
  type: BlogRSS
  url: https://upstreambio.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://investors.upstreambio.com/shareholder-services/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upstreambio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upstreambio.com/terms/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upstreambio
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.upstreambio.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upstream-bio-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Upstream Bio is a Nasdaq-listed clinical-stage drug developer whose product is a single therapeutic program (verekitug, an anti-TSLP-receptor antibody in Phase 2/3); upstreambio.com is a fourteen-page WordPress marketing site with no /developers, /docs or /api path at all, the investor material lives on a hosted IR subdomain, and the only machine-readable endpoints on either host are the CMS defaults — an RSS feed, a Yoast sitemap, and WordPress core's undocumented, noindexed /wp-json/ route index — rather than any published product API.
  evidence:
  - status: 200
    url: https://upstreambio.com/
  - status: 404
    url: https://upstreambio.com/openapi.json
  - status: 404
    url: https://upstreambio.com/swagger.json
  - status: 404
    url: https://upstreambio.com/graphql
  - status: 404
    url: https://upstreambio.com/llms.txt
  - status: 404
    url: https://upstreambio.com/.well-known/api-catalog
  - status: 404
    url: https://upstreambio.com/.well-known/agent-card.json
  - status: 404
    url: https://upstreambio.com/.well-known/agent.json
  - status: 404
    url: https://investors.upstreambio.com/llms.txt
  - status: 404
    url: https://investors.upstreambio.com/.well-known/api-catalog
  - status: 200
    url: https://upstreambio.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: 'Upstream Bio is a clinical-stage biotechnology company headquartered at 460 Totten Pond Road in Waltham, Massachusetts, founded in 2021 and listed on Nasdaq as UPB since its October 2024 IPO. The company develops treatments for inflammatory disease with an initial focus on severe respiratory disorders, and its strategy is built around a single lead asset: verekitug (UPB-101), described by the company as the only known antagonist in clinical development that targets the receptor for thymic stromal lymphopoietin (TSLP). Verekitug has been advanced into Phase 2 studies in severe asthma, chronic rhinosinusitis with nasal polyps (CRSwNP) and chronic obstructive pulmonary disease (COPD), with a Phase 3 development strategy announced in 2026. Upstream Bio is a therapeutics developer rather than a software vendor: upstreambio.com is a fourteen-page WordPress marketing site, investor material is served from a hosted Q4-style investor-relations subdomain, and the company publishes no
  developer program, no public API, no SDK and no machine-readable API contract.'
image: https://upstreambio.com/wp-content/uploads/2026/08/upstream-bio-social-image.jpg
layout: provider
modified: '2026-09-02'
name: Upstream Bio
nav: Providers
network: true
overview: 'Upstream Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Healthcare.


  Upstream Bio''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Upstream Bio Domain Security
  slug: upstream-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: upstream-bio
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Healthcare
- Immunology
- Respiratory
- Clinical Trials
- Drug Development
- Nasdaq
website: https://upstreambio.com/
---
