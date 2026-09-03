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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.alkimiya.eu/
- group: company
  title: ''
  type: About
  url: https://www.alkimiya.eu/chi-siamo/67/
- group: operate
  title: ''
  type: Support
  url: https://www.alkimiya.eu/contatti/
- group: company
  title: ''
  type: Blog
  url: https://www.alkimiya.eu/articoli/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alkimiya.eu/privacy/
- group: start
  title: ''
  type: Login
  url: https://www.alkimiya.eu/login/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alkimiya
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alkimiya-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alkimiya-llms.txt
coverage:
  checked: '2026-09-02'
  detail: Alkimiya's SmartCare product page markets an integration API in prose but the company publishes no developer portal, reference or spec anywhere — every contract-discovery path on www.alkimiya.eu 404s, certificate transparency shows no api/dev/docs subdomain exists, and the only published route to the API is the contact form at /contatti/ and info@alkimiya.eu.
  evidence:
  - status: 200
    url: https://www.alkimiya.eu/soluzioni/smartcare/427/
  - status: 404
    url: https://www.alkimiya.eu/openapi.json
  - status: 404
    url: https://www.alkimiya.eu/docs/
  - status: 200
    url: https://www.alkimiya.eu/contatti/
  reason: sales-gate
  state: gated
created: '2026-09-02'
description: Alkimiya SRL is an Italian digital-health startup headquartered in Rome that builds and distributes clinical decision support systems grounded in Evidence Based Medicine. It is the exclusive Italian distributor of EBMEDS, a third-generation CDSS owned by Duodecim Publication Company of Finland carrying more than 1,000 clinical algorithms for drug interaction, contraindication, dosage and medication-reconciliation checking. Alkimiya is also developing SmartCare, its own Digital Clinical Decision Pathway platform for the proactive support of post-discharge and chronic patients, combining an evidence-based knowledge base, a rules engine and an integration API meant to make telemedicine systems and electronic health records act on clinical guidance. Continuum of Care packages the same pathway engine as cloud SaaS with patient-facing mobile apps. The company markets the SmartCare API but publishes no developer portal, reference or machine-readable contract.
image: https://www.alkimiya.eu/assets/images/logo.jpg
layout: provider
modified: '2026-09-02'
name: Alkimiya
nav: Providers
network: true
overview: 'Alkimiya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Clinical Decision Support, and Evidence Based Medicine.


  Alkimiya''s developer surface includes support, engineering blog, and 7 more developer resources.'
plans:
- name: Alkimiya Plans Pricing
  plan_count: 0
  slug: alkimiya-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Alkimiya Rate Limits
  slug: alkimiya-rate-limits
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Alkimiya Domain Security
  slug: alkimiya-domain-security
  summary_line: TLSv1.3
slug: alkimiya
tags:
- Company
- Health
- Healthcare
- Clinical Decision Support
- Evidence Based Medicine
- Digital Health
- Telemedicine
- Chronic Care
- Italy
website: https://www.alkimiya.eu/
---
