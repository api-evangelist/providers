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
  url: security/eos-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.helloeos.ai/
- group: start
  title: ''
  type: Login
  url: https://my.helloeos.ai/login
- group: start
  title: ''
  type: Demo
  url: https://calendly.com/arya-helloeos/30min
created: '2026-07-17'
description: 'Eos AI is a San Francisco healthcare technology company building an autonomous operating system for healthcare that helps clinics and hospitals identify eligible patients and enable early care interventions. The platform connects to fragmented clinical systems (EHRs, imaging archives, labs, scheduling, and billing), resolves patient identities across sites and encounters, and links records into a continuous longitudinal history that can be searched and analyzed as one distributed database. Two harmonization products anchor the stack: VERA standardizes medical imaging across scanners, sites, and protocols to improve model performance and shorten deployment, and LUCIA structures EHR free text, ICD, SNOMED, and clinical signals into a unified representation for downstream analytics. On top of the harmonized data, Eos runs predictive models over full patient trajectories and drives automations into hospital workflows, reporting roughly 3x administrative productivity and 37% revenue
  recovery in early deployments. Founded in 2025 by Arya Khokhar and backed by Y Combinator (Winter 2026 batch). Its application is gated at my.helloeos.ai; no public developer API, OpenAPI, or developer portal has been published to date, so this profile captures the company identity and the security posture of its public web surface.'
image: https://www.helloeos.ai/static/images/favicon.png
layout: provider
modified: '2026-07-19'
name: Eos AI
nav: Providers
network: true
overview: Eos AI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Artificial Intelligence, and Machine-Learning.
random_paper: 7
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eos-ai/refs/heads/main/screenshots/eos-ai-2026-07-25T213503.png
security:
- kind: domain-security
  name: Eos Ai Domain Security
  slug: eos-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: eos-ai
tags:
- Company
- Health
- Healthcare
- Artificial Intelligence
- Machine-Learning
- Clinical Data
- Data Harmonization
- Medical Imaging
- Predictive Analytics
- Hospital Operations
website: https://www.helloeos.ai/
---
