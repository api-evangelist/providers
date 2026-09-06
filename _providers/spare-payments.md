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
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
asyncapis:
- description: ''
  name: Spare Payments Webhooks
  slug: spare-payments-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://paywithspare.com
- group: start
  title: ''
  type: Login
  url: https://app.paywithspare.com
- group: docs
  title: ''
  type: Documentation
  url: https://sparepayments.notion.site
- group: docs
  title: ''
  type: APIReference
  url: https://sparepayments.notion.site/API-Documentation-22eb891ffdf84651aacebc3a6459b686
- group: operate
  title: ''
  type: Support
  url: https://paywithspare.com/school-support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://paywithspare.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://paywithspare.com/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sparepayments
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/spare-payments-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/spare-payments-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spare-payments-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/spare-payments-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spare-payments-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spare-payments-llms.txt
created: '2026-07-17'
description: Spare (Spare L.L.C., paywithspare.com) is a school management and cashless-payments platform that digitizes payments and automates internal school processes using contactless technology — wristbands, phones, student ID cards, and QR codes. It serves schools, parents, and vendors through a centralized admin dashboard with permission controls, parent spending limits and dietary/allergen monitoring, vendor inventory tools, and attendance tracking. Spare exposes a REST API (JSON over HTTPS, standard HTTP verbs and status codes) that has not yet been opened to the public; its webhook surface is publicly documented so external inventory and attendance systems can react to Spare events in near real time. Backed by 500 Global.
image: https://avatars.githubusercontent.com/u/227619477?v=4
layout: provider
modified: '2026-07-21'
name: Spare Payments
nav: Providers
network: true
overview: 'Spare Payments is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Education, Schools, and Cashless Payments.


  The Spare Payments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Spare Payments'' developer surface includes documentation, API reference, support, changelog, and 10 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 13.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spare-payments/refs/heads/main/screenshots/spare-payments-2026-09-02T160319.png
security:
- kind: domain-security
  name: Spare Payments Domain Security
  slug: spare-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spare-payments
tags:
- Company
- Payments
- Education
- Schools
- Cashless Payments
- EdTech
- Attendance
- Webhook
website: https://paywithspare.com
---
