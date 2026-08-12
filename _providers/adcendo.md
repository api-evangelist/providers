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
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adcendo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adcendo.com/
- group: company
  title: ''
  type: About
  url: https://adcendo.com/adcendo/about/about-adcendo/
- group: other
  title: ''
  type: Pipeline
  url: https://adcendo.com/adcendo/our-science/pipeline/
- group: other
  title: ''
  type: Publications
  url: https://adcendo.com/adcendo/our-science/key-publications/
- group: operate
  title: ''
  type: PressReleases
  url: https://adcendo.com/adcendo/investors/press-releases/
- group: company
  title: ''
  type: BlogRSS
  url: https://adcendo.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://adcendo.com/adcendo/your-careers-and-our-values/
- group: operate
  title: ''
  type: Contact
  url: https://adcendo.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adcendo.com/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://adcendo.com/cookie-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adcendo-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Adcendo is a clinical-stage biopharmaceutical company developing antibody-drug conjugates; its only machine-readable endpoint is the stock WordPress REST API of its marketing CMS at /wp-json/ (LiteSpeed, Wordfence, Divi and Google Site Kit plugin routes), and every OpenAPI, GraphQL, MCP and A2A discovery path on adcendo.com returns 404.
  evidence:
  - status: 404
    url: https://adcendo.com/openapi.json
  - status: 404
    url: https://adcendo.com/graphql
  - status: 404
    url: https://adcendo.com/.well-known/agent-card.json
  - status: 404
    url: https://adcendo.com/.well-known/security.txt
  - status: 200
    url: https://adcendo.com/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: Adcendo ApS is a clinical-stage biopharmaceutical company headquartered in Copenhagen, Denmark, with US operations in Boston, Massachusetts, developing a new generation of antibody-drug conjugates (ADCs) for cancers with high unmet medical need. Founded in 2017 out of research by Lars Henning Engelholm and Niels Behrendt, the company advances a clinical and pre-clinical pipeline that includes ADCE-T02 (targeting Tissue Factor, in the Phase 1b Tiffany-01 study across advanced solid tumors), ADCE-D01 (targeting uPARAP, granted FDA Fast Track designation for soft tissue sarcoma), and the pre-clinical ADCE-B05. Adcendo is a privately held, venture-backed therapeutics developer; it publishes a corporate website, pipeline and publications pages, and investor press releases, but it operates no developer program, public API, or machine-readable API contract.
image: https://adcendo.com/wp-content/uploads/adcendo-logo.png
layout: provider
modified: '2026-08-06'
name: Adcendo
nav: Providers
network: true
overview: Adcendo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Life Sciences.
random_paper: 22
score:
  band: minimal
  composite: 8.5
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adcendo/refs/heads/main/screenshots/adcendo-2026-08-07T160906.png
security:
- kind: domain-security
  name: Adcendo Domain Security
  slug: adcendo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adcendo
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Life Sciences
- Antibody-Drug Conjugates
- Clinical Stage
- Denmark
website: https://adcendo.com/
---
