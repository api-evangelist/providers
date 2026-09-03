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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognoa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cognoa.com/
- group: start
  title: ''
  type: Portal
  url: https://app.cognoa.com/
- group: start
  title: ''
  type: Login
  url: https://app.cognoa.com/sign_in
- group: operate
  title: ''
  type: Support
  url: https://cognoa.com/support/
- group: company
  title: ''
  type: Blog
  url: https://cognoa.com/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://cognoa.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cognoa
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cognoa.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.cognoa.com/link/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://cognoa.com/wp-content/uploads/2023/06/CA-Cognoa-Comprehensive-Compliance-Program.pdf
coverage:
  checked: '2026-08-09'
  detail: Cognoa ships Canvas Dx only as an end-user medical device — a caregiver iOS/Android app and a prescriber web portal at app.cognoa.com — with no developer portal, no published spec and no SDK; the portal is a Rails app that answers every /.well-known/*, /openapi.json, /graphql and /mcp probe with its "Oops! We couldn't locate your page!" not-found shell (HTML 200 or JSON 404), so none of those 200s is a real discovery document.
  evidence:
  - status: 404
    url: https://cognoa.com/openapi.json
  - status: 404
    url: https://app.cognoa.com/openapi.json
  - status: 200
    url: https://app.cognoa.com/.well-known/agent-card.json
  - status: 404
    url: https://cognoa.com/.well-known/security.txt
  - status: 200
    url: https://github.com/cognoa
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: Cognoa is a pediatric behavioral health company in Palo Alto, California building digital diagnostics and therapeutics for early childhood development, starting with autism. Its flagship product, Canvas Dx, is an FDA-authorized Software as a Medical Device that aids clinicians in diagnosing or ruling out autism spectrum disorder in children aged 18 to 72 months, combining a caregiver questionnaire, short home videos scored by credentialed human video analysts, and a healthcare-provider questionnaire into a machine-learning classifier that returns Positive, Negative, or Indeterminate. Canvas Dx is delivered as an iOS/Android caregiver app plus a prescriber web portal at app.cognoa.com; Cognoa ships no public developer API, SDK, or webhook surface.
image: https://cognoa.com/wp-content/uploads/cropped-Cognoa-C-192x192.png
layout: provider
modified: '2026-08-09'
name: Cognoa
nav: Providers
network: true
overview: 'Cognoa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Healthcare, and Autism.


  Cognoa''s developer surface includes developer portal, support, engineering blog, and 8 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 16.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cognoa/refs/heads/main/screenshots/cognoa-2026-09-02T145120.png
security:
- kind: domain-security
  name: Cognoa Domain Security
  slug: cognoa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cognoa
tags:
- Company
- Health
- Digital Health
- Healthcare
- Autism
- Pediatrics
- Diagnostics
- Artificial Intelligence
- Machine-Learning
- Software as a Medical Device
- Behavioral Health
website: https://cognoa.com/
---
