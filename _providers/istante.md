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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/istante-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://istante.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://istante.ai/privacy-policy.html
- group: operate
  title: ''
  type: Support
  url: https://istante.ai/faq.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/istante-llms.txt
created: '2026-07-17'
description: Istante is an Italian technology company (VAT IT03635230547, based in the Perugia area) that develops and operates Athena, a business-process-automation platform built around a team of specialized AI assistants. Athena covers assistants for communication routing and email classification, credit management and collections, a 24/7 voice/phone assistant, quote and order processing, automated tender monitoring and scoring, outbound lead engagement, contract and legal analysis, and HR and onboarding. It is positioned to collaborate with staff rather than replace them, keeping critical decisions under human oversight, and is offered on a fixed-cost "Digital Working Units" (DWU) pricing model rather than variable token pricing. The platform integrates across email, Microsoft Teams, WhatsApp, SMS, and phone, and is presented as GDPR and EU AI Act compliant. Istante was surfaced as a portfolio company of Canaan Partners and added to the API Evangelist network for enrichment.
image: https://istante.ai/logo.svg
layout: provider
modified: '2026-07-19'
name: Istante
nav: Providers
network: true
overview: 'Istante is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Business Process Automation, and Automation.


  Istante''s developer surface includes support and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 8.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/istante/refs/heads/main/screenshots/istante-2026-07-25T222950.png
security:
- kind: domain-security
  name: Istante Domain Security
  slug: istante-domain-security
  summary_line: TLSv1.3
slug: istante
tags:
- Company
- Artificial Intelligence
- AI Agents
- Business Process Automation
- Automation
- Compliance
- Italy
website: https://istante.ai
---
