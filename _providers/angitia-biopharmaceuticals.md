---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: true
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
  score: 2.2
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.angitiabio.com/
- group: company
  title: ''
  type: About
  url: https://www.angitiabio.com/aboutus
- group: company
  title: ''
  type: News
  url: https://www.angitiabio.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.angitiabio.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.angitiabio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.angitiabio.com/privacypolicy
- group: other
  title: ''
  type: ContentSignal
  url: well-known/angitia-biopharmaceuticals-robots.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/angitia-biopharmaceuticals-domain-security.yml
coverage:
  checked: '2026-08-06'
  detail: Angitia is a clinical-stage drug developer whose product is a bispecific antibody, not software; angitiabio.com is a seven-page corporate brochure site and every API discovery path on it returns 404, with api., developer., docs. and portal.angitiabio.com all NXDOMAIN.
  evidence:
  - status: 404
    url: https://www.angitiabio.com/openapi.json
  - status: 404
    url: https://www.angitiabio.com/.well-known/agent-card.json
  - status: 404
    url: https://www.angitiabio.com/developers
  - status: 200
    url: https://www.angitiabio.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Angitia Biopharmaceuticals is a clinical-stage biopharmaceutical company founded in 2018, headquartered at 3027 Townsgate Road, Westlake Village, California, with research and development operations in Guangzhou, China. It discovers and develops biologic therapeutics for serious musculoskeletal diseases, including osteoporosis, osteogenesis imperfecta, bone metastasis, osteoarthritis and muscle disorders. Its clinical pipeline is led by AGA2118 and AGA2115, bispecific antibodies targeting sclerostin and DKK1, alongside AGA111 in lumbar interbody fusion. The company closed a $120 million Series C financing in December 2024 led by Bain Capital Life Sciences. Angitia is a drug developer, not a software vendor: it publishes no API, developer portal, SDK, machine-readable specification, or technology platform of any kind. Its only machine-readable public surface is an XML sitemap and a robots.txt carrying Cloudflare-managed Content-Signal directives that reserve AI training rights.'
image: https://www.angitiabio.com/home/img/logo.png
layout: provider
modified: '2026-08-06'
name: Angitia Biopharmaceuticals
nav: Providers
network: true
overview: 'Angitia Biopharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, biopharmaceuticals, Pharmaceuticals, and Life Sciences.


  Angitia Biopharmaceuticals'' developer surface includes product news, support, and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 10.0
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/angitia-biopharmaceuticals/refs/heads/main/screenshots/angitia-biopharmaceuticals-2026-08-07T161410.png
security:
- kind: domain-security
  name: Angitia Biopharmaceuticals Domain Security
  slug: angitia-biopharmaceuticals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: angitia-biopharmaceuticals
tags:
- Company
- Biotechnology
- biopharmaceuticals
- Pharmaceuticals
- Life Sciences
- Drug Development
- Clinical Trials
- Healthcare
- Musculoskeletal
- Therapeutics
website: https://www.angitiabio.com/
---
