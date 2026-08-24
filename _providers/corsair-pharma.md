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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corsair-pharma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.corsairpharma.com/
- group: company
  title: ''
  type: Blog
  url: https://www.corsairpharma.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.corsairpharma.com/blog-feed.xml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corsairpharma.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corsairpharma.com/terms-of-use
coverage:
  checked: '2026-08-11'
  detail: Corsair Pharma is a clinical-stage drug developer whose entire web presence is a five-page Wix marketing site (home, news, team, privacy-policy, terms-of-use) with no developer, API, docs or partner section; the live host additionally answers every path with a SiteGround "Robot Challenge Screen" (HTTP 202), so the page inventory and the absence of any /.well-known document were confirmed from Wayback Machine captures instead.
  evidence:
  - status: 202
    url: https://www.corsairpharma.com/
  - status: 202
    url: https://www.corsairpharma.com/openapi.json
  - status: 404
    url: http://web.archive.org/web/2025id_/https://www.corsairpharma.com/developers
  - status: 404
    url: https://web.archive.org/web/20240405094716/https://www.corsairpharma.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/corsairpharma
  - status: 404
    url: https://pypi.org/pypi/corsair-pharma/json
  reason: not-a-software-company
  state: none
created: '2026-08-11'
description: 'Corsair Pharma, Inc. is a privately held clinical-stage biopharmaceutical company developing proprietary prodrugs of treprostinil for the treatment of pulmonary arterial hypertension (PAH). Its lead program, the TRX-248 transdermal system, is an investigational once-daily patch that delivers an inactive treprostinil prodrug across the skin for conversion to active drug in the liver, aiming to combine the efficacy and titration profile of parenteral prostacyclin therapy with non-invasive once-daily dosing. The company completed its preclinical program, announced positive Phase 1 results for TRX-248 in June 2026, closed a $23M Series B led by New Rhein Healthcare Investors, and has entered a strategic collaboration with United Therapeutics to advance novel treprostinil prodrugs. Corsair Pharma is a drug developer, not a software vendor: its public web presence is a five-page marketing and investor-news site with no developer program, API, SDK, or machine-readable specification
  of any kind.'
image: https://static.wixstatic.com/media/eb8f76_be22d65dbdb84f7dbd3bae3f30cf754e~mv2.png
layout: provider
modified: '2026-08-11'
name: Corsair Pharma
nav: Providers
network: true
overview: 'Corsair Pharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Drug Development.


  Corsair Pharma''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 3.3
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: domain-security
  name: Corsair Pharma Domain Security
  slug: corsair-pharma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: corsair-pharma
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Drug Development
- Clinical Trials
- Pulmonary Arterial Hypertension
- Transdermal Delivery
website: https://www.corsairpharma.com/
---
