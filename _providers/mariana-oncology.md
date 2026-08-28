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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mariana-oncology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marianaoncology.com/
- group: company
  title: ''
  type: Blog
  url: https://marianaoncology.com/news/
- group: operate
  title: ''
  type: Contact
  url: https://marianaoncology.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marianaoncology.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://marianaoncology.com/privacy-statement/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marianaoncology
- group: other
  title: ''
  type: ParentCompany
  url: https://www.novartis.com/
- group: other
  title: ''
  type: ParentCompanyProfile
  url: https://github.com/api-evangelist/novartis
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://marianaoncology.com/news/mariana-oncology-to-be-acquired-by-novartis-to-advance-precision-radiopharmaceuticals-to-treat-cancer/
coverage:
  checked: '2026-08-25'
  detail: Mariana Oncology, a Novartis company, is a preclinical-stage radioligand-therapy developer whose entire web presence is a 23-URL Gatsby marketing site (sitemap-0.xml) with no developer, docs or API section; api./developer./docs./portal.marianaoncology.com are NXDOMAIN, there is no GitHub organization under any spelling of the name, and every contract-discovery path on the one live host returns the site's 404 shell.
  evidence:
  - status: 404
    url: https://marianaoncology.com/openapi.json
  - status: 404
    url: https://marianaoncology.com/.well-known/agent-card.json
  - status: 404
    url: https://marianaoncology.com/graphql
  - status: 200
    url: https://marianaoncology.com/sitemap-0.xml
  - status: 404
    url: https://api.github.com/orgs/mariana-oncology
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: 'Mariana Oncology, a Novartis company, is a Watertown, Massachusetts biotechnology company developing precision radioligand therapies (RLTs) — targeted radiopharmaceuticals that deliver alpha- and beta-emitting radioisotopes selectively to tumor cells while sparing healthy tissue. Its pipeline pursues solid-tumor targets including DLL3-expressing small cell lung cancer (MC-339), alongside breast and prostate programs, and it operates a Radioligand Therapy Innovation Center of Excellence for radiochemistry, isotope handling and clinical supply. Founded in 2020 and acquired by Novartis in May 2024, Mariana Oncology is a therapeutics developer, not a software vendor: it publishes no developer program, no public API, and no machine-readable interface of any kind.'
image: https://marianaoncology.com/mariana-og-image.png
layout: provider
modified: '2026-08-25'
name: Mariana Oncology
nav: Providers
network: true
overview: 'Mariana Oncology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Oncology, and Radiopharmaceuticals.


  Mariana Oncology''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.5
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: domain-security
  name: Mariana Oncology Domain Security
  slug: mariana-oncology-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mariana-oncology
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Oncology
- Radiopharmaceuticals
- Radioligand Therapy
- Life Sciences
- Healthcare
- Clinical Research
website: https://marianaoncology.com/
---
