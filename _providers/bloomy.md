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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bloomylearning.com/
- group: start
  title: ''
  type: Login
  url: https://www.bloomylearning.com/login
- group: start
  title: ''
  type: SignUp
  url: https://app.bloomylearning.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bloomylearning.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bloomylearning.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@bloomylearning.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bloomy-llms.txt
created: '2026-07-17'
description: Bloomy (bloomylearning.com) is an AI-powered adaptive learning platform for K-12 students, founded by Alex Southmayd and backed by Y Combinator (Summer 2026 batch). The product diagnoses each student's knowledge gaps, builds a personalized standards-aligned learning path across English Language Arts, Math, and Writing, and delivers Socratic AI tutoring plus mastery-based practice, requiring 90%+ mastery before a student advances. It integrates third-party diagnostic/assessment data (i-Ready, NWEA MAP) and provides a real-time teacher dashboard. Bloomy serves traditional districts, charter schools, homeschools, and microschools, and sells to families via monthly or annual subscriptions (with ESA/EFA fund eligibility in some states). As of this profile Bloomy publishes no public API, developer portal, SDKs, or developer documentation; this record captures its verified public identity and legal/account surface only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomy.png
layout: provider
modified: '2026-07-18'
name: Bloomy
nav: Providers
network: true
overview: 'Bloomy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Artificial Intelligence, and Adaptive Learning.


  Bloomy''s developer surface includes signup flow, support, and 6 more developer resources.'
random_paper: 7
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
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomy/refs/heads/main/screenshots/bloomy-2026-07-25T203416.png
security:
- kind: domain-security
  name: Bloomy Domain Security
  slug: bloomy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bloomy
tags:
- Company
- Education
- EdTech
- Artificial Intelligence
- Adaptive Learning
- K-12
- E-Learning
- Personalization
- AI Tutor
website: https://bloomylearning.com/
---
