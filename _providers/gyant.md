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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gyant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gyant.com/
- group: company
  title: ''
  type: Blog
  url: https://www.fabrichealth.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fabrichealth.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fabrichealth.com/terms-conditions
- group: auth
  title: ''
  type: Compliance
  url: https://www.fabrichealth.com/security-compliance
created: '2026-07-17'
description: Gyant was a San Francisco-based digital health company that built an AI-powered conversational virtual assistant for health systems, guiding patients through symptom checking, care navigation, and triage across web and messaging channels. In 2022 Gyant was acquired by Fabric (fabrichealth.com), and gyant.com now redirects to Fabric's healthcare care-access platform, which combines conversational AI with physician-built clinical protocols for virtual care, patient engagement, and clinical automation. Gyant does not publish a public API, developer portal, or SDKs; this profile captures the company's identity, published legal/compliance surface, and domain security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gyant.png
layout: provider
modified: '2026-07-19'
name: Gyant
nav: Providers
network: true
overview: 'Gyant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Virtual Assistant, and Conversational AI.


  Gyant''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gyant/refs/heads/main/screenshots/gyant-2026-07-25T220448.png
security:
- kind: domain-security
  name: Gyant Domain Security
  slug: gyant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gyant
tags:
- Company
- Healthcare
- Artificial Intelligence
- Virtual Assistant
- Conversational AI
- Patient Engagement
- Digital Health
- Care Navigation
website: https://gyant.com/
---
