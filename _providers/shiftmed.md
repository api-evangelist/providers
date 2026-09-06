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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: ShiftMed markets an API that lets a hospital, health system or post-acute facility tap its network of credentialed CNAs, LPNs and RNs and fill open shifts on demand from within its existing scheduling
  name: ShiftMed Workforce API
  slug: shiftmed-workforce-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shiftmed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shiftmed.com/
- group: operate
  title: ''
  type: Support
  url: https://help.shiftmed.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.shiftmed.com/professionals/blog/
- group: start
  title: ''
  type: Login
  url: https://portal.shiftmed.com/login
- group: start
  title: ''
  type: SignUp
  url: https://apply.shiftmed.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shiftmed.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shiftmed.com/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://www.shiftmed.com/about/contact/
- group: company
  title: ''
  type: Press
  url: https://www.shiftmed.com/about/press-releases/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.shiftmed.com/insights/knowledge-center/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shiftmed
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC38kDGvSQpGqEf4a-gGPWUg
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/shiftmed_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shiftmed-llms.txt
coverage:
  checked: '2026-08-05'
  detail: ShiftMed publicly markets "a public API" that "can be embedded in health system platforms", but ships no developer host at all — developer.shiftmed.com and docs.shiftmed.com do not resolve, and the only documented route to the API is the "Book a Workforce Consultation" form on the partners page.
  evidence:
  - status: 200
    url: https://www.shiftmed.com/about/partners/
  - status: 200
    url: https://api.shiftmed.com/v1/health
  - status: 200
    url: https://api.shiftmed.com/openapi.json
  - status: 404
    url: https://www.shiftmed.com/.well-known/security.txt
  - status: 404
    url: https://www.shiftmed.com/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: ShiftMed is a McLean, Virginia healthcare workforce technology company operating an on-demand clinician marketplace and AI-powered open shift management platform for hospitals, health systems, skilled nursing facilities and post-acute providers. It matches credentialed W-2 CNAs, LPNs and RNs to open shifts, and markets an API that lets a facility tap that clinician network directly from its own scheduling stack. The API surface reaches customers through workforce-management partner integrations — UKG Pro Workforce Management (formerly UKG Dimensions), symplr Smart Square, QGenda, Smartlinx and Attendance on Demand — alongside file-based SFTP feeds. ShiftMed publishes no public developer portal, documentation, specification or SDK; API access is arranged through a workforce consultation.
image: https://images.ctfassets.net/5ghoewqh73wu/1g43njpFzYtQFmeTGNhdcN/b98de6dbb6af4fafc7c41b2a714307f8/Home_Hero_HighRes.webp
layout: provider
modified: '2026-08-05'
name: ShiftMed
nav: Providers
network: true
overview: 'ShiftMed publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Staffing, Workforce Management, and Scheduling.


  ShiftMed''s developer surface includes support, engineering blog, signup flow, YouTube channel, and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shiftmed/refs/heads/main/screenshots/shiftmed-2026-09-02T155203.png
security:
- kind: domain-security
  name: Shiftmed Domain Security
  slug: shiftmed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shiftmed
tags:
- Company
- Healthcare
- Staffing
- Workforce Management
- Scheduling
- Marketplace
- Nursing
- Human Resources
- Health Systems
website: https://www.shiftmed.com/
---
