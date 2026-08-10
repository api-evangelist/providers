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
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rivus-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rivuspharma.com/
- group: company
  title: ''
  type: About
  url: https://www.rivuspharma.com/about/
- group: company
  title: ''
  type: News
  url: https://www.rivuspharma.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.rivuspharma.com/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rivuspharma.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rivuspharma.com/terms/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rivus-pharmaceuticals
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/rivus-pharmaceuticals_stock/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rivus-pharmaceuticals-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rivus-pharmaceuticals-llms.txt
coverage:
  checked: '2026-08-05'
  detail: Rivus Pharmaceuticals is a clinical-stage biopharmaceutical company whose product is a drug (HU6) rather than software — the public site carries only About, Focus, Pipeline, News and Careers, no api./developer./docs./portal./app./status. host resolves for rivuspharma.com, no Rivus GitHub organisation exists under any plausible name, and every spec-discovery and /.well-known/ path returns a genuine 404 on both the apex and www hosts (the site root returns 200 and a deliberate control path also returns 404, so these are real absences, not a soft-404 catch-all).
  evidence:
  - status: 404
    url: https://www.rivuspharma.com/openapi.json
  - status: 404
    url: https://www.rivuspharma.com/.well-known/agent-card.json
  - status: 404
    url: https://www.rivuspharma.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/rivuspharma
  - status: 200
    url: https://www.rivuspharma.com/
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Rivus Pharmaceuticals is a privately held clinical-stage biopharmaceutical company founded in 2019, with corporate offices in South San Francisco, California and research operations in Charlottesville, Virginia. Grounded in mitochondrial biology, it develops oral small-molecule controlled metabolic accelerators for obesity and associated cardio-metabolic disease. Lead candidate HU6 is in Phase 2 development for metabolic dysfunction-associated steatohepatitis (MASH) and has reported Phase 2a data in obesity-related heart failure with preserved ejection fraction (HFpEF); RV-8451, an oral non-peptide GLP-1 receptor agonist for obesity, is in IND-enabling studies. Rivus is a therapeutics developer, not a software or technology vendor: it publishes no developer program, public API, SDK or machine-readable specification of any kind.'
image: https://www.rivuspharma.com/themes/default/images/logo.svg
layout: provider
modified: '2026-08-05'
name: Rivus Pharmaceuticals
nav: Providers
network: true
overview: 'Rivus Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  Rivus Pharmaceuticals'' developer surface includes product news and 10 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 12.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Rivus Pharmaceuticals Domain Security
  slug: rivus-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rivus-pharmaceuticals
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Healthcare
- Drug Development
- Metabolic Health
website: https://www.rivuspharma.com/
---
