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
  url: security/pinetree-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pinetreetx.com/
- group: company
  title: ''
  type: News
  url: https://www.pinetreetx.com/en/news/news.php
- group: other
  title: ''
  type: Team
  url: https://www.pinetreetx.com/en/team/leadership.php
- group: company
  title: ''
  type: Careers
  url: https://www.pinetreetx.com/en/careers/job.php
- group: company
  title: ''
  type: Investors
  url: https://www.pinetreetx.com/en/investors/investors.php
- group: operate
  title: ''
  type: Contact
  url: https://www.pinetreetx.com/en/communication/contact.php
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/pinetree-therapeutics_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pinetree-therapeutics
coverage:
  checked: '2026-08-05'
  detail: Pinetree Therapeutics is a preclinical-stage oncology drug developer whose product is a protein-degrader therapeutic, not software — its entire public site is seven brochure pages (team, science, news, careers, investors, contact) served from PHP with no /developers, /api, api./docs./developer. subdomain, sitemap, llms.txt or any /.well-known/ document.
  evidence:
  - status: 200
    url: https://www.pinetreetx.com/
  - status: 404
    url: https://www.pinetreetx.com/developers
  - status: 404
    url: https://www.pinetreetx.com/api
  - status: 404
    url: https://www.pinetreetx.com/openapi.json
  - status: 404
    url: https://www.pinetreetx.com/llms.txt
  - status: 404
    url: https://www.pinetreetx.com/.well-known/agent-card.json
  - status: 404
    url: https://www.pinetreetx.com/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Pinetree Therapeutics, Inc. is a preclinical-stage biotechnology company headquartered at West Cambridge Scientific Park, 767C Concord Ave, Cambridge, Massachusetts, developing next-generation targeted protein degraders (TPDs) built on its proprietary AbReptor platform. AbReptor degrades membrane-bound and extracellular proteins through target co-engagement, induced endocytosis, endolysosome formation and lysosomal degradation, aiming to overcome drug resistance and tumor recurrence in oncology, with additional application in inflammation and immunology. The company is advancing trispecific degraders and ADC-integrated programs, closed a $17M Series A in July 2024, and has entered a licensing partnership with AstraZeneca. It is a therapeutics developer rather than a software vendor: it publishes no public API, developer portal, SDK or machine-readable specification.'
image: https://www.pinetreetx.com/images/common/logo.png
layout: provider
modified: '2026-08-05'
name: PineTree Therapeutics
nav: Providers
network: true
overview: 'PineTree Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Oncology.


  PineTree Therapeutics'' developer surface includes product news and 8 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Pinetree Therapeutics Domain Security
  slug: pinetree-therapeutics-domain-security
  summary_line: TLSv1.2
slug: pinetree-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Oncology
- Drug Discovery
- Targeted Protein Degradation
- Preclinical
website: https://www.pinetreetx.com/
---
