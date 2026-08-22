---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cour-pharmaceuticals-development-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://courpharma.com/
- group: company
  title: ''
  type: About
  url: https://courpharma.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://courpharma.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://courpharma.com/feed/
- group: company
  title: ''
  type: Partners
  url: https://courpharma.com/partnerships/
- group: company
  title: ''
  type: Careers
  url: https://courpharma.com/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://courpharma.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://courpharma.com/terms-of-use/
- group: other
  title: ''
  type: Accessibility
  url: https://courpharma.com/accessibility/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cour-pharmaceuticals-development_stock/
coverage:
  checked: '2026-08-11'
  detail: COUR Pharma is a clinical-stage biotech developing CNP nanoparticle immune-tolerance therapies; its entire public site is a WordPress marketing/investor site with no developer section, api./developer./docs.courpharma.com do not resolve in DNS, and every contract and /.well-known/ probe returned the site's HTML 404 — the only machine-readable endpoint on the host is stock WordPress /wp-json/ CMS plumbing (Elementor, Astra, Forminator), not a product API.
  evidence:
  - status: 404
    url: https://courpharma.com/openapi.json
  - status: 404
    url: https://courpharma.com/.well-known/agent-card.json
  - status: 404
    url: https://courpharma.com/.well-known/security.txt
  - status: 404
    url: https://courpharma.com/llms.txt
  - status: 404
    url: https://courpharma.com/graphql
  - status: 0
    url: https://api.courpharma.com/
  reason: not-a-software-company
  state: none
created: '2026-08-11'
description: 'COUR Pharmaceuticals Development Co., Inc. (COUR Pharma) is a privately held, clinical-stage biotechnology company founded in 2012 and headquartered in the Chicago area (Northbrook/Skokie, Illinois), spun out of research at Northwestern University. COUR develops antigen-specific immune tolerance therapies built on its proprietary COUR Nanoparticle (CNP) platform: biodegradable polymer nanoparticles of roughly 500 nm carrying about 1% disease-specific antigen, which mimic apoptotic bodies so that antigen-presenting cells in the liver and spleen re-recognize the antigen as self, deleting pathogenic T cells and expanding regulatory T cells. Active clinical programs include CNP-103 for Type 1 Diabetes and CNP-106 for Myasthenia Gravis, with earlier work in Primary Biliary Cholangitis and Celiac Disease. COUR is a therapeutics developer, not a software or platform company: it publishes no developer program, no public API, and no machine-readable API contract of any kind.'
image: https://courpharma.com/wp-content/uploads/2025/06/Cour-OG.png
layout: provider
modified: '2026-08-11'
name: Cour Pharmaceuticals Development
nav: Providers
network: true
overview: 'Cour Pharmaceuticals Development is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Immunology.


  Cour Pharmaceuticals Development''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.5
  delta: -1.3
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Cour Pharmaceuticals Development Domain Security
  slug: cour-pharmaceuticals-development-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cour-pharmaceuticals-development
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Immunology
- Autoimmune Disease
- Clinical Trials
- Nanotechnology
- Drug Development
- Healthcare
website: https://courpharma.com/
---
