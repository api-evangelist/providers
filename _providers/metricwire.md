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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Production JSON API served from api.metricwire.com backing the Metricwire research data collection platform (studies, participants, schedules, survey responses, and passive/sensor data). No public Ope
  name: Metricwire API
  slug: metricwire-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metricwire-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metricwire.com/
- group: start
  title: ''
  type: Login
  url: https://app.metricwire.com/
- group: operate
  title: ''
  type: Support
  url: https://metricwire.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metricwire.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metricwire.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.metricwire.com/
- group: auth
  title: ''
  type: Compliance
  url: https://metricwire.com/data-privacy-security-summary/
- group: design
  title: ''
  type: Conformance
  url: conformance/metricwire-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metricwire-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metricwire-llms.txt
created: '2026-07-17'
description: Metricwire is a real-world data collection platform for ecological momentary assessment (EMA), experience sampling (ESM), and digital-health research. It helps organizations measure real-world experiences to inform treatments, service offerings, and policies. Researchers design studies, schedule time- and event-based prompts, collect participant self-reports alongside passive sensor and wearable data through native iOS and Android apps, and export the results for analysis. The platform is used across clinical trials, behavioral and public-health research, and patient-reported outcome programs, with an emphasis on data privacy and security (ISO 27001, GDPR). A production JSON API is served from api.metricwire.com and a participant/researcher application from app.metricwire.com, though Metricwire does not currently publish an open developer portal or machine-readable API specification.
image: https://metricwire.com/wp-content/uploads/2016/12/mw_icon_512x512_iTunesArtwork-270x270.png
layout: provider
modified: '2026-07-20'
name: Metricwire
nav: Providers
network: true
overview: 'Metricwire publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Research, Data Collection, Ecological Momentary Assessment, and Experience Sampling.


  Metricwire''s developer surface includes support and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 21.6
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 21.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metricwire/refs/heads/main/screenshots/metricwire-2026-08-07T172740.png
security:
- kind: domain-security
  name: Metricwire Domain Security
  slug: metricwire-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: metricwire
tags:
- Company
- Research
- Data Collection
- Ecological Momentary Assessment
- Experience Sampling
- Digital Health
- Clinical Trials
- Surveys
- Patient Reported Outcomes
- Mobile
website: https://metricwire.com/
---
