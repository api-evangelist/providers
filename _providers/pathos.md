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
  url: https://www.pathos.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pathos.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.pathos.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pathos.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pathos-inc
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pathos-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: well-known/pathos-content-signal.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pathos-domain-security.yml
coverage:
  checked: '2026-08-04'
  detail: Pathos AI is a clinical-stage oncology biotech whose PathOS platform is run by its own Sprint pods and licensed through pharma partnership deals, not exposed to third parties — the entire nine-page site (platform, pipeline, partners, partner-with-us) offers a contact form and no developer surface at all, and api./developer./docs.pathos.com do not resolve.
  evidence:
  - status: 404
    url: https://www.pathos.com/developers
  - status: 404
    url: https://www.pathos.com/openapi.json
  - status: 404
    url: https://www.pathos.com/.well-known/agent-card.json
  - status: 200
    url: https://www.pathos.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: Pathos (Pathos AI, Inc.) is an AI-enabled, clinical-stage biotechnology company founded in 2022 by Eric Lefkofsky and Ryan Fukushima that applies artificial intelligence and large-scale multimodal patient data to oncology drug development. Its PathOS platform is organized around three engines — Scout (AI asset selection that matches an investigational therapy to the patient subgroup most likely to respond), Sprint (small autonomous clinical-execution pods that design and run biomarker-driven trials), and Foundry (the oncology foundation model built in partnership with Tempus and AstraZeneca) — trained against a stated corpus of more than 200 petabytes of multimodal clinical, molecular and imaging data linked to patient outcomes. The company raised a $365M Series D in May 2025 at roughly a $1.6B valuation, completed the acquisition of Rain Oncology, and is advancing a precision-oncology pipeline that includes a CBP/p300 inhibitor and a brain-penetrant PRMT5 inhibitor. Pathos
  sells partnership and co-development to pharma and biotech; it publishes no public developer program, API, SDK or machine-readable specification.
image: https://lirp.cdn-website.com/8e545b68/dms3rep/multi/opt/pathos-open_graph-97b7336f-1920w.jpg
layout: provider
modified: '2026-08-04'
name: Pathos
nav: Providers
network: true
overview: 'Pathos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, Biotechnology, and Oncology.


  Pathos'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pathos/refs/heads/main/screenshots/pathos-2026-08-07T191548.png
security:
- kind: domain-security
  name: Pathos Domain Security
  slug: pathos-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pathos
tags:
- Company
- Artificial Intelligence
- Healthcare
- Biotechnology
- Oncology
- Drug Development
- Clinical Trials
- Precision Medicine
- Life Sciences
website: https://www.pathos.com/
---
