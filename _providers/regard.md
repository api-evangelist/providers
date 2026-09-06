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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://regard.com
- group: company
  title: ''
  type: Blog
  url: https://regard.com/resources/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://regard.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://regard.com/onc-certification
- group: auth
  title: ''
  type: TrustCenter
  url: security/regard-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/regard-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/regard-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/regard-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/regard-plans-pricing.yml
coverage:
  checked: '2026-08-15'
  detail: Regard sells an EHR-embedded clinical AI platform that CALLS hospital Epic, Cerner and generic FHIR servers as a client; it ships no developer API of its own — regard.com/openapi.json, /swagger.json, /api-docs and /docs all 404, api.regard.com and docs.regard.com do not resolve in DNS, and its ONC Health IT Module certification omits the sec. 170.315(g)(10) standardized-API criterion.
  evidence:
  - status: 404
    url: https://regard.com/openapi.json
  - status: 404
    url: https://regard.com/api-docs
  - status: 404
    url: https://regard.com/.well-known/agent-card.json
  - status: 200
    url: https://regard.com/llms.txt
  - status: 200
    url: https://regard.com/technology
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Regard is an AI-powered clinical diagnosis and documentation platform for hospitals and health systems. It reviews 100% of a patient's electronic health record (EHR) to surface and recommend evidence-supported diagnoses, then generates clinical documentation at the point of care. Regard positions itself around "earning revenue through better care, not queries," spanning clinical notes, mid-revenue-cycle denial prevention and revenue capture, HCC risk-adjustment capture, and screening for care gaps. The company reports 12.9M+ recommended diagnoses accepted by clinicians and $50M+ in revenue generated for health systems. Regard integrates directly with EHRs rather than exposing a public developer API; its Health IT Module is ONC 2015 Cures Update certified. Backed by Foundry Group and Techstars. This profile is maintained in the API Evangelist network.
image: https://cdn.prod.website-files.com/6a0437304c683d2c1726ea92/6a5561f29575eedbb1a4052e_regard_open_graph_1200_630.png
layout: provider
modified: '2026-08-15'
name: Regard
nav: Providers
network: true
overview: 'Regard is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare AI, Clinical Documentation, Clinical Decision Support, and Electronic Health Records.


  Regard''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Regard Plans Pricing
  plan_count: 0
  slug: regard-plans-pricing
random_paper: 20
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 14.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/regard/refs/heads/main/screenshots/regard-2026-09-02T153245.png
security:
- kind: domain-security
  name: Regard Domain Security
  slug: regard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Regard Trust Center
  slug: regard-trust-center
  summary_line: ONC 2015 Cures Update (Health IT Module), ISO 9001
slug: regard
tags:
- Company
- Healthcare AI
- Clinical Documentation
- Clinical Decision Support
- Electronic Health Records
- Revenue Cycle Management
- Health IT
- Diagnosis
website: https://regard.com
---
