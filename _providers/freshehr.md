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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://freshehr.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://freshehr.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freshehr
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/10361651/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/freshehr
- group: build
  title: ''
  type: Packages
  url: packages/freshehr-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freshehr-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshehr-domain-security.yml
coverage:
  checked: '2026-09-02'
  detail: freshEHR is an openEHR/HL7 FHIR consultancy that sells modelling, training and implementation expertise rather than software — freshehr.com is a five-section brochure site whose only technical link is a training page, and every contract and /.well-known path probed on freshehr.com and freshehr.github.io returned 404 while api./docs./training./app.freshehr.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://freshehr.com/
  - status: 404
    url: https://freshehr.com/openapi.json
  - status: 404
    url: https://freshehr.com/.well-known/api-catalog
  - status: 404
    url: https://freshehr.com/.well-known/agent-card.json
  - status: 404
    url: https://freshehr.github.io/openapi.json
  - status: <no DNS>
    url: https://api.freshehr.com/
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: 'freshEHR Clinical Informatics Ltd is a UK open-standards health and social care informatics consultancy, founded in 2014 by Dr Ian McNicoll and registered in England as company 08989238. It provides openEHR and HL7 FHIR expertise rather than a software product: openEHR strategy, analysis, design and governance of clinical models (archetypes and templates), curation, terminology and data mapping across SNOMED CT, dm+d and ICD, data exchange work across HL7 V2, HL7 CDA and HL7 FHIR, plus specialist training and mentoring in clinical modelling. Its work spans NHS England, NHS Education for Scotland, Digital Health and Care Wales, HSE Ireland, One London, CatSalut in Catalonia, the Jamaican Ministry of Health and Wellness, and Karolinska University Hospital. freshEHR operates no API of its own — no developer portal, no public API reference, and no machine-readable contract on any host it controls, verified 2026-09-02.'
image: https://freshehr.com/assets/img/freshehr-logo-2.png
layout: provider
modified: '2026-09-02'
name: freshEHR
nav: Providers
network: true
overview: freshEHR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Health, Healthcare, and Clinical Informatics.
random_paper: 15
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: domain-security
  name: Freshehr Domain Security
  slug: freshehr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: freshehr
tags:
- Company
- Consulting
- Health
- Healthcare
- Clinical Informatics
- Electronic Health Records
- openEHR
- HL7 FHIR
- SNOMED CT
- Interoperability
- Standards
- Training
- United Kingdom
website: https://freshehr.com/
---
