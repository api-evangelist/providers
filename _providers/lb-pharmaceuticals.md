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
  url: security/lb-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lbpharma.us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lbpharma.us/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://lbpharma.us/contact/
coverage:
  checked: '2026-08-23'
  detail: LB Pharmaceuticals is a clinical-stage drug developer whose entire web presence is a WordPress marketing and investor-relations site; the only machine-readable surface is the stock WordPress core REST API at lbpharma.us/wp-json/ (222 routes, every namespace a CMS plugin such as contact-form-7, redirection and wp-smush), with no product API, no developer or docs subdomain (api./docs./developer.lbpharma.us all NXDOMAIN), no GitHub organization and no published client library.
  evidence:
  - status: 200
    url: https://lbpharma.us/wp-json/
  - status: 404
    url: https://lbpharma.us/openapi.json
  - status: 404
    url: https://lbpharma.us/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/lbpharma
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'LB Pharmaceuticals Inc (Nasdaq: LBRX) is a clinical-stage biopharmaceutical company headquartered at One Pennsylvania Plaza, New York, developing novel therapies for neuropsychiatric diseases including schizophrenia and bipolar depression. Its lead asset, LB-102, is an oral small-molecule benzamide antipsychotic with potent D2, D3 and 5HT7 antagonism, positioned to become the first benzamide antipsychotic approved for neuropsychiatric disorders in the United States. The company reported positive Phase 2 schizophrenia results from its NOVA1 trial in January 2025 and initiated the ILLUMINATE-1 Phase 2 bipolar depression trial in January 2026. LB Pharmaceuticals is a drug developer, not a software vendor: it publishes no public API, developer portal, SDK or machine-readable contract, and its web presence is a WordPress corporate and investor-relations site.'
image: https://lbpharma.us/wp-content/uploads/2026/03/LBlogo-color_final-opt.png
layout: provider
modified: '2026-08-23'
name: LB Pharmaceuticals
nav: Providers
network: true
overview: 'LB Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Health.


  LB Pharmaceuticals'' developer surface includes support and 3 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.1
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Lb Pharmaceuticals Domain Security
  slug: lb-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lb-pharmaceuticals
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Health
- Clinical Trials
- Neuroscience
- Drug Development
website: https://lbpharma.us/
---
