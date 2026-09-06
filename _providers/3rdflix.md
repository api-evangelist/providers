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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Wriety's "Agentic APIs" are marketed as 100+ AI capabilities that OEM manufacturers embed into interactive flat panel displays - freehand and math recognition in 194 languages, doodle/object interpret
  name: Wriety Agentic APIs
  slug: wriety-agentic-apis
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3rdflix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wriety.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wriety.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.wriety.com/web
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wriety.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wriety.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.wriety.com/contact-us
- group: commercial
  title: ''
  type: Plans
  url: plans/3rdflix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/3rdflix-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/3rdflix-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3rdflix-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Wriety (3rdFlix Visual Effects Private Limited) markets "100+ Agentic APIs" for OEM embedding into interactive flat panels, but the entire reference is a marketing PDF spec sheet listing 91 feature names with no base URL, endpoint, method, parameter or auth scheme, and the only access path on the AI API page is "GET WRIETY TODAY" with info@wriety.com and +91 87126 91769.
  evidence:
  - status: 200
    url: https://www.wriety.com/aiapi
  - status: 200
    url: https://www.wriety.com/static/media/AI%20APIs%20Spec%20Sheet.5573c503d2fc81e7e73f.pdf
  - status: 404
    url: https://api.wriety.com/openapi.json
  - status: 404
    url: https://api.wriety.com/v3/api-docs
  - status: 502
    url: https://www.practically.com/openapi.json
  reason: sales-gate
  state: gated
created: '2026-09-05'
description: Practically is the experiential-learning brand of 3rdFlix Visual Effects Private Limited, a Hyderabad, India edtech company founded in 2018 by Subbarao Siddabattula, Charu Noheria and Ilangovel Thulasimani. The original Practically app delivered 3D, AR and simulation-based STEM learning for classes 6-12 and raised roughly USD 14M. The company's live product is now Wriety, an interactive-whiteboard and classroom-collaboration platform for interactive flat panels (IFPs) that is marketed alongside a set of "Agentic APIs" - a catalogue of 100+ AI features (handwriting and math recognition, transcription, lesson and assessment generation, image analysis) offered to OEM panel makers. As of this pass no machine-readable API contract, developer portal or API reference is published anywhere on the estate; the only API collateral is a marketing PDF spec sheet, and access runs through a sales contact.
image: https://www.wriety.com/favicon.svg
layout: provider
modified: '2026-09-05'
name: Practically
nav: Providers
network: true
overview: 'Practically publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Artificial Intelligence, and Collaboration.


  Practically''s developer surface includes pricing, signup flow, support, and 8 more developer resources.'
plans:
- name: 3Rdflix Plans Pricing
  plan_count: 3
  slug: 3rdflix-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 3Rdflix Rate Limits
  slug: 3rdflix-rate-limits
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 3Rdflix Domain Security
  slug: 3rdflix-domain-security
  summary_line: no transport/DNS hardening detected
slug: 3rdflix
tags:
- Company
- Education
- EdTech
- Artificial Intelligence
- Collaboration
- Interactive Whiteboard
- India
website: https://www.wriety.com/
---
