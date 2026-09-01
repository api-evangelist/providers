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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spark-neuro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sparkneuro.com/
- group: company
  title: ''
  type: About
  url: https://sparkneuro.com/about/
- group: operate
  title: ''
  type: Support
  url: https://sparkneuro.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sparkneuro.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sparkneuro.com/terms-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spark-neuro
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spark-neuro-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/spark-neuro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spark-neuro-rate-limits.yml
coverage:
  checked: '2026-08-28'
  detail: SPARK Neuro sells EEG-plus-AI diagnostics and neuro-analytics as a delivered enterprise product with no developer-facing side at all — sparkneuro.com is a nine-page WordPress site whose /developers, /api and /docs paths 404, sparkpredict.ai is a static landing page whose only interactive element is a Formspree demo form, and the one API-named host the company owns, api.sparkneuro.com, resolves in DNS but answers 502 Bad Gateway on every path.
  evidence:
  - status: 404
    url: https://sparkneuro.com/developers
  - status: 404
    url: https://sparkneuro.com/openapi.json
  - status: 502
    url: https://api.sparkneuro.com/
  - status: 404
    url: https://sparkpredict.ai/openapi.json
  - status: 404
    url: https://sparkneuro.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-28'
description: SPARK Neuro is a New York City neuroscience company that quantifies brain data with EEG and machine learning, for both clinical care and commercial audience measurement. Its clinical arm, SPARK Medical, pairs FDA-cleared EEG hardware with deep-learning models to produce objective biomarkers for Alzheimer's disease, traumatic brain injury and concussion, Parkinson's disease, ALS, and mental-health conditions, and ships a push-button test-and-report software platform aimed at clinicians, researchers and pharmaceutical trial operations. Its commercial arm, Spark MEDIA, applies the same biometric measurement to advertising and entertainment, reading emotional and attentional response to content. A third product, Spark Predict, is a conversational analytics interface over the company's healthcare claims intelligence engine, marketed to payers and providers. The company was founded by CEO Spencer Gerrol and has raised more than $35M. SPARK Neuro publishes no public developer program,
  API reference, or machine-readable contract; its software reaches customers as a delivered product rather than as an API.
image: https://sparkneuro.com/wp-content/uploads/2024/02/cropped-SPARKNEURO-RGB-Color-black-text.png
layout: provider
modified: '2026-08-28'
name: SPARK Neuro
nav: Providers
network: true
overview: 'SPARK Neuro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Neuroscience, Neurotechnology, Healthcare, and Medical Devices.


  SPARK Neuro''s developer surface includes support and 9 more developer resources.'
plans:
- name: Spark Neuro Plans Pricing
  plan_count: 0
  slug: spark-neuro-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Spark Neuro Rate Limits
  slug: spark-neuro-rate-limits
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 5
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Spark Neuro Domain Security
  slug: spark-neuro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spark-neuro
tags:
- Company
- Neuroscience
- Neurotechnology
- Healthcare
- Medical Devices
- EEG
- Artificial Intelligence
- Diagnostics
- Clinical Trials
- Advertising
website: https://sparkneuro.com/
---
