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
  url: security/surge-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://surgetx.com/
- group: company
  title: ''
  type: About
  url: https://surgetx.com/science/
- group: other
  title: ''
  type: Team
  url: https://surgetx.com/team/
- group: company
  title: ''
  type: News
  url: https://surgetx.com/news/
- group: operate
  title: ''
  type: Contact
  url: https://surgetx.com/contacts/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/surge-therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/surge-therapeutics_stock/
coverage:
  checked: '2026-08-05'
  detail: SURGE Therapeutics is a clinical-stage oncology drug developer whose entire web presence is a five-page WordPress marketing site (home, science, news, team, contacts); the only machine-readable endpoint on surgetx.com is WordPress core's default /wp-json CMS route index, and api./developer./docs./portal.surgetx.com are all NXDOMAIN.
  evidence:
  - status: 404
    url: https://surgetx.com/openapi.json
  - status: 404
    url: https://surgetx.com/.well-known/agent-card.json
  - status: 404
    url: https://surgetx.com/.well-known/security.txt
  - status: 404
    url: https://surgetx.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/surgetx
  - status: 200
    url: https://surgetx.com/wp-json
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: SURGE Therapeutics is a clinical-stage biotechnology company based in Cambridge, Massachusetts, developing intraoperative cancer immunotherapy. Founded on research from Dr. Michael Goldberg's laboratory at Harvard Medical School, the company's SURGERx platform is an injectable, biodegradable hydrogel placed directly at the site of surgical tumor resection to provide extended, localized release of immunotherapy — addressing the surgery-induced inflammation that suppresses the immune system and allows residual disease to reawaken. Its lead program, SRG-514, completed Phase 1 dose escalation in breast cancer patients undergoing surgery and is being prepared for a registrational trial, with an additional IND cleared for a Phase 1/2a study in bladder cancer. SURGE has raised a $26M Series A and a $32M Series B. It is a therapeutics developer, not a software company, and publishes no developer program, API, or machine-readable interface.
image: https://surgetx.com/wp-content/uploads/2021/06/SURGE_No-Slogan-COLOUR-1024x279.png
layout: provider
modified: '2026-08-05'
name: SURGE Therapeutics
nav: Providers
network: true
overview: 'SURGE Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Immunotherapy.


  SURGE Therapeutics'' developer surface includes product news and 7 more developer resources.'
random_paper: 2
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Surge Therapeutics Domain Security
  slug: surge-therapeutics-domain-security
  summary_line: TLSv1.2
slug: surge-therapeutics
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Immunotherapy
- Drug Delivery
- Clinical Stage
- Health
- Life Sciences
website: https://surgetx.com/
---
