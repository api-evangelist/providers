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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nuvig-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nuvigtx.com/
- group: company
  title: ''
  type: About
  url: https://nuvigtx.com/science/
- group: other
  title: ''
  type: Science
  url: https://nuvigtx.com/science/
- group: other
  title: ''
  type: Pipeline
  url: https://nuvigtx.com/pipeline/
- group: other
  title: ''
  type: Team
  url: https://nuvigtx.com/team/
- group: company
  title: ''
  type: News
  url: https://nuvigtx.com/news/
- group: company
  title: ''
  type: Blog
  url: https://nuvigtx.com/news/
- group: company
  title: ''
  type: BlogFeeds
  url: https://nuvigtx.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://nuvigtx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://nuvigtx.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nuvigtx.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nuvigtx.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://nuvigtx.com/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nuvig-therapeutics-inc
- group: company
  title: ''
  type: Twitter
  url: https://x.com/nuvigtx
- group: company
  title: ''
  type: Investors
  url: https://www.hiive.com/securities/nuvig-therapeutics-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nuvig-therapeutics-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Nuvig is a clinical-stage biotech whose product is a drug candidate (NVG-2089), not software — nuvigtx.com is a five-page corporate WordPress site with no /developers, /api or /docs path, no GitHub organization, and no package on any registry.
  evidence:
  - status: 404
    url: https://nuvigtx.com/developers
  - status: 404
    url: https://nuvigtx.com/openapi.json
  - status: 404
    url: https://nuvigtx.com/.well-known/agent-card.json
  - status: 200
    url: https://nuvigtx.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'Nuvig Therapeutics, Inc. is a privately held, clinical-stage biotechnology company headquartered at 3450 Hillview Avenue, Palo Alto, California, developing next-generation immunomodulators for chronic autoimmune and inflammatory disease. Its lead investigational candidate, NVG-2089, is an engineered Fc fragment designed to selectively engage type II Fc receptors and harness an endogenous regulatory mechanism that resolves autoimmune dysregulation while preserving normal immune function; the first patient was dosed in a Phase 2 trial in chronic inflammatory demyelinating polyneuropathy (CIDP) in May 2025. The company announced a $161 million Series B financing in December 2024. Nuvig is a therapeutics developer, not a software vendor: as of August 2026 it publishes no developer portal, API reference, SDK, GitHub organization, or machine-readable API contract of any kind. Its public web surface is a corporate WordPress site covering science, pipeline, team, news and careers,
  from which the only machine-readable artifact published is a Yoast-generated llms.txt.'
image: https://nuvigtx.com/wp-content/uploads/2022/04/bg-logo-nuvig.svg
layout: provider
modified: '2026-08-04'
name: Nuvig Therapeutics
nav: Providers
network: true
overview: 'Nuvig Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Immunology, and Autoimmune Disease.


  Nuvig Therapeutics'' developer surface includes product news, engineering blog, and 16 more developer resources.'
random_paper: 107
score:
  band: minimal
  composite: 11.5
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nuvig-therapeutics/refs/heads/main/screenshots/nuvig-therapeutics-2026-08-07T185808.png
security:
- kind: domain-security
  name: Nuvig Therapeutics Domain Security
  slug: nuvig-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nuvig-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Immunology
- Autoimmune Disease
- Therapeutics
- Clinical Trials
- Life Sciences
- United States
website: https://nuvigtx.com/
---
