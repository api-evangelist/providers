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
  url: security/ansun-biopharma-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ansun-biopharma-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ansunbiopharma.com/
- group: company
  title: ''
  type: Blog
  url: https://www.ansunbiopharma.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ansunbiopharma.com/feed/
- group: company
  title: ''
  type: About
  url: https://www.ansunbiopharma.com/about/who-we-are/
- group: operate
  title: ''
  type: Contact
  url: https://www.ansunbiopharma.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://www.ansunbiopharma.com/careers/career-opportunities/
- group: company
  title: ''
  type: Investors
  url: https://www.ansunbiopharma.com/investors/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/ansun-biopharma_stock/
coverage:
  checked: '2026-08-06'
  detail: Ansun Biopharma is a 25-person clinical-stage drug developer whose entire public site is a 24-page WordPress brochure about the DAS181 sialidase pipeline — there is no developer section, and every spec and .well-known path probed on ansunbiopharma.com returned 404 while api. and developer. subdomains do not resolve.
  evidence:
  - status: 404
    url: https://www.ansunbiopharma.com/developers
  - status: 404
    url: https://www.ansunbiopharma.com/openapi.json
  - status: 404
    url: https://www.ansunbiopharma.com/.well-known/agent-card.json
  - status: 200
    url: https://www.ansunbiopharma.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Ansun Biopharma is a privately held, clinical-stage biopharmaceutical company headquartered in the Sorrento Valley district of San Diego, California, founded in 2003 by virologists and molecular biologists and led by CEO Dr. Nancy Chang. Rather than targeting viruses directly, Ansun develops host-directed immuno-biologic therapies built on a recombinant sialidase platform. Its lead candidate, DAS181 (Ansun-181), is a multi-function sialidase fusion protein that removes the sialic acid receptors respiratory viruses use to enter host cells, and has been studied in parainfluenza virus (PIV), severe influenza, human metapneumovirus and COVID-19 in immunocompromised and hospitalized patients. The company also advances earlier-stage programs in oncology and autoimmune disease from the same sialidase platform. Ansun is a drug developer, not a software vendor: it publishes a corporate WordPress site covering its pipeline, research and technologies, publications, intellectual property,
  investors, news and careers, and exposes no public API, SDK, developer portal or machine-readable specification.'
image: https://www.ansunbiopharma.com/wp-content/uploads/2020/06/ansun-bio-logo-3.png
layout: provider
modified: '2026-08-06'
name: Ansun Biopharma
nav: Providers
network: true
overview: 'Ansun Biopharma is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Biopharmaceutical, Life Sciences, and Clinical Trials.


  Ansun Biopharma''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ansun-biopharma/refs/heads/main/screenshots/ansun-biopharma-2026-08-07T161422.png
security:
- kind: domain-security
  name: Ansun Biopharma Domain Security
  slug: ansun-biopharma-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ansun-biopharma
tags:
- Company
- Biotechnology
- Biopharmaceutical
- Life Sciences
- Clinical Trials
- Antivirals
- Health
- Drug Development
- San Diego
website: https://www.ansunbiopharma.com/
---
