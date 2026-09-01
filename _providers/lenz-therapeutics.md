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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lenz-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lenz-tx.com/
- group: company
  title: ''
  type: About
  url: https://lenz-tx.com/about/
- group: operate
  title: ''
  type: Contact
  url: https://lenz-tx.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://lenz-tx.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lenz-tx.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lenz-tx.com/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://ir.lenz-tx.com/news-events/press-releases
- group: company
  title: ''
  type: BlogRSS
  url: https://ir.lenz-tx.com/news-events/press-releases/rss
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.lenz-tx.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lenztx
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/lenz_tx
coverage:
  checked: '2026-08-25'
  detail: LENZ Therapeutics sells an FDA-approved eye drop, not software — its entire public estate is a ten-page WordPress marketing site (lenz-tx.com), a VIZZ product site and an investor-relations portal, with no /developers, /api or /docs page, no api./developer./docs. subdomain resolving in DNS, and no GitHub organization under any spelling of the name.
  evidence:
  - status: 404
    url: https://lenz-tx.com/developers
  - status: 404
    url: https://lenz-tx.com/openapi.json
  - status: 0
    url: https://api.lenz-tx.com/
  - status: 404
    url: https://api.github.com/orgs/lenz-tx
  - status: 200
    url: https://lenz-tx.com/page-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'LENZ Therapeutics, Inc. (Nasdaq: LENZ) is a commercial-stage ophthalmic pharmaceutical company headquartered in San Diego, California, focused on the commercialization of VIZZ (aceclidine ophthalmic solution) 1.44% — the first and only FDA-approved aceclidine-based eye drop for the treatment of presbyopia. LENZ commercializes VIZZ in the United States and establishes international licensing partnerships to provide access globally. The company publishes no developer program, public API, SDK, or machine-readable API description of any kind; its public surface is a ten-page WordPress marketing site, a VIZZ product site, and an investor-relations portal carrying SEC filings and a press-release RSS feed.'
image: https://lenz-tx.com/wp-content/uploads/2022/06/gb_home_1200x630.jpg
layout: provider
modified: '2026-08-25'
name: LENZ Therapeutics
nav: Providers
network: true
overview: 'LENZ Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Healthcare.


  LENZ Therapeutics'' developer surface includes engineering blog and 11 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.5
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Lenz Therapeutics Domain Security
  slug: lenz-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lenz-therapeutics
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Healthcare
- Ophthalmology
- Presbyopia
- Drug Development
- Public Company
website: https://lenz-tx.com/
---
