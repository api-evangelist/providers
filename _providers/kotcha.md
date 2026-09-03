---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kotcha-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kotcha.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@kotcha.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kotcha.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kotcha.com/en/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.kotcha.com/en/our-story
- group: company
  title: ''
  type: Partners
  url: https://www.kotcha.com/en/partnership
- group: company
  title: ''
  type: Press
  url: https://drive.google.com/drive/folders/1_Dc4bCirc8qc6YDSHdYUAtXXvk1evLI8
- group: other
  title: ''
  type: Downloads
  url: https://kotcha.go.link/1VEPz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kotcha-running
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/kotcha.run/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/people/Kotcha/61580625827349/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kotcha-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/kotcha-plans-pricing.yml
coverage:
  checked: '2026-08-17'
  detail: Kotcha is a consumer iOS/Android running-coach subscription from PACEUP SAS with no developer program at all — the marketing site has no /docs, /developers or /api route, api.kotcha.com and developer.kotcha.com are NXDOMAIN, and its Terms & Conditions section 6 explicitly prohibit "accessing services through unauthorized means or automated methods".
  evidence:
  - status: 404
    url: https://www.kotcha.com/openapi.json
  - status: 404
    url: https://www.kotcha.com/.well-known/agent-card.json
  - status: 200
    url: https://www.kotcha.com/en/terms-and-conditions
  reason: no-developer-program
  state: none
created: '2026-08-17'
description: Kotcha is a consumer running-coaching mobile application operated by PACEUP SAS, a French company based in Paris, and co-founded with marathon world-record holder Eliud Kipchoge and the NN Running Team. The app generates personalized, adaptive training plans for 5K, 10K, half-marathon and marathon distances, delivered through a conversational AI coach that adapts to completed workouts, and it imports activity and health data from Strava, Garmin Connect, Apple, Coros and Huawei wearables. Kotcha raised EUR 3.5M in October 2025 in a round led by Racine2, operated by Serena and makesense. Kotcha is a consumer subscription product distributed through the Apple App Store and Google Play; it publishes no developer portal, no API documentation and no machine-readable API contract, and its terms of service explicitly prohibit automated access to the service. This profile records that absence rather than an API surface.
image: https://www.kotcha.com/favicon.png
layout: provider
modified: '2026-08-17'
name: Kotcha
nav: Providers
network: true
overview: 'Kotcha is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Sporttech, Running, Fitness, and Health.


  Kotcha''s developer surface includes support and 13 more developer resources.'
plans:
- name: Kotcha Plans Pricing
  plan_count: 0
  slug: kotcha-plans-pricing
random_paper: 4
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kotcha/refs/heads/main/screenshots/kotcha-2026-09-02T150142.png
security:
- kind: domain-security
  name: Kotcha Domain Security
  slug: kotcha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kotcha
tags:
- Company
- Sporttech
- Running
- Fitness
- Health
- Coaching
- Artificial Intelligence
- Mobile Application
- Wearables
- Consumer
website: https://www.kotcha.com/
---
