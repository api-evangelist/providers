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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://recess.gg/
- group: start
  title: ''
  type: SignUp
  url: https://recess.gg/school/apply
- group: start
  title: ''
  type: Login
  url: https://recess.gg/login
- group: commercial
  title: ''
  type: Pricing
  url: https://recess.gg/school/tuition
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/recess-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/recess-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recess-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/recess-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://recess.gg/.well-known/security.txt
created: '2026-07-17'
description: Recess (Recess Academy, recess.gg) is an online school for gifted and neurodivergent students, including learners with ADHD, dyslexia, autism spectrum, and anxiety. It combines core academics, interest-led classes, small-group coworking sessions with an AI tutor, and a daily community hour, with personalized pacing and world-class mentors. Recess is backed by Bloomberg Beta. As of this enrichment pass the company operates a consumer education web application and publishes no public API, developer portal, SDKs, or OpenAPI surface; the only machine-discoverable surface found is a valid RFC 9116 security.txt with a security contact.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recess.png
layout: provider
modified: '2026-07-21'
name: Recess
nav: Providers
network: true
overview: 'Recess is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online School, and Neurodivergent Learning.


  Recess'' developer surface includes signup flow, pricing, and 7 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recess/refs/heads/main/screenshots/recess-2026-09-02T153046.png
security:
- kind: domain-security
  name: Recess Domain Security
  slug: recess-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Recess Vulnerability Disclosure
  slug: recess-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: recess
tags:
- Company
- Education
- EdTech
- Online School
- Neurodivergent Learning
- Gifted Education
- Consumer
website: https://recess.gg/
---
