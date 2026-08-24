---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
api_count: 2
apis:
- description: 'Partner integration API for exchanging supply-chain and procurement data (purchase quotations, orders, catalog) between customer and supplier ERP systems and the Bionexo marketplace. Documented via a '
  name: Bionexo Integration API
  slug: bionexo-integration-api
- description: Integration-environment API that receives supply-chain data pushed from partner and supplier systems into the Bionexo platform. Documented via a hosted Swagger UI; the OpenAPI definition is served beh
  name: Bionexo Data Receiving API
  slug: bionexo-data-receiving-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://bionexo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://integration-api.bionexo.com/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://integration-api.bionexo.com/index.html
- group: company
  title: ''
  type: Blog
  url: https://bionexo.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://bionexo.com/suporte-tecnico/
- group: start
  title: ''
  type: Login
  url: https://login.bionexo.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bionexo.com/aviso-privacidade/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bionexo.com/termos-e-condicoes/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bionexo.com/
- group: design
  title: ''
  type: Lifecycle
  url: https://raw.githubusercontent.com/api-evangelist/bionexo/refs/heads/main/lifecycle/bionexo-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: https://raw.githubusercontent.com/api-evangelist/bionexo/refs/heads/main/security/bionexo-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://raw.githubusercontent.com/api-evangelist/bionexo/refs/heads/main/llms/bionexo-llms.txt
created: '2026-07-17'
description: Bionexo is Latin America's largest B2B healthcare supply-chain technology platform, founded in 2000 in Sao Paulo, Brazil. It connects hospitals, clinics, laboratories, health-plan operators, distributors, suppliers and industry through an integrated cloud suite spanning e-procurement and marketplace, the Tasy hospital ERP, Clinica nas Nuvens clinic management, and the Brasindice drug-price reference, covering supply-chain, clinical and financial operations end to end. The platform serves more than 11,000 clients and roughly 90 million patients a year across Brazil, Argentina, Colombia and Mexico, running the largest healthcare B2B marketplace in the region. For system-to-system integration Bionexo exposes a partner Integration API documented via Swagger/OpenAPI and a Data Receiving API for EDI-style exchange of purchase quotations and supply-chain data between customer and supplier ERP systems and the Bionexo marketplace.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bionexo.png
layout: provider
modified: '2026-07-18'
name: Bionexo
nav: Providers
network: true
overview: 'Bionexo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Supply Chain, Procurement, and Marketplace.


  Bionexo''s developer surface includes documentation, API reference, engineering blog, support, and 8 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 19.7
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 19.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bionexo/refs/heads/main/screenshots/bionexo-2026-07-25T203048.png
security:
- kind: domain-security
  name: Bionexo Domain Security
  slug: bionexo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bionexo
tags:
- Company
- Healthcare
- Supply Chain
- Procurement
- Marketplace
- eProcurement
- Hospitals
- ERP
- Latin America
- Brazil
website: https://bionexo.com/
---
