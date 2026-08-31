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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secretome-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://secretometherapeutics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://secretometherapeutics.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secretometherapeutics.com/privacy-policy
- group: company
  title: ''
  type: News
  url: https://secretometherapeutics.com/news-publications
- group: operate
  title: ''
  type: PressReleases
  url: https://secretometherapeutics.com/press-releases
- group: other
  title: ''
  type: Team
  url: https://secretometherapeutics.com/team
- group: operate
  title: ''
  type: Contact
  url: https://secretometherapeutics.com/contact
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/secretome-therapeutics_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/secretome-therapeutics-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Secretome Therapeutics is a clinical-stage cell-therapy developer whose only web property is a VendorGroup/Kscope investor-relations site with seven marketing pages and no developer section; that platform answers HTTP 200 with the homepage HTML for every unknown path, so /openapi.json, /graphql, /llms.txt and all seven /.well-known/ probes returned soft-404 HTML shells rather than documents, and no GitHub organisation, npm or PyPI package exists under the company name.
  evidence:
  - status: 200
    url: https://secretometherapeutics.com/openapi.json
  - status: 200
    url: https://secretometherapeutics.com/.well-known/agent-card.json
  - status: 200
    url: https://secretometherapeutics.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/secretome-therapeutics
  - status: 200
    url: https://secretometherapeutics.com/our-science
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Secretome Therapeutics is a clinical-stage biotechnology company (formerly NeoProgen, founded 2018) developing allogeneic, off-the-shelf regenerative therapies derived from neonatal cardiac progenitor cells (nCPCs). Its lead candidate STM-01, and the cell-free secretome STM-2, target heart failure with preserved ejection fraction (HFpEF), dilated cardiomyopathy (DCM) and Duchenne muscular dystrophy associated cardiomyopathy, and are in Phase 1 clinical study. The company publishes a corporate and investor-relations website covering its science, pipeline, team, patient/expanded-access policy and press releases; it publishes no developer program, API, SDK or machine-readable contract of any kind.
image: https://storage.googleapis.com/vendorgroup-assets/site/c26b1537-b667-48ad-bd88-c03a4a03b51d/2026/03/20/69bc8e242fbd420ce21e43d1/secretome-social.jpg
layout: provider
modified: '2026-08-26'
name: Secretome Therapeutics
nav: Providers
network: true
overview: 'Secretome Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Regenerative Medicine, and Cell Therapy.


  Secretome Therapeutics'' developer surface includes product news and 9 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.0
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
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
  name: Secretome Therapeutics Domain Security
  slug: secretome-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS
slug: secretome-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Regenerative Medicine
- Cell Therapy
- Cardiology
- Clinical Stage
- Life Sciences
- Healthcare
website: https://secretometherapeutics.com/
---
