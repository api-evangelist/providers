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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boston-scientific-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bos-sci
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boston-scientific
- group: company
  title: ''
  type: Website
  url: https://www.bostonscientific.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.bostonscientific.com/
- group: company
  title: ''
  type: Careers
  url: https://www.bostonscientific.com/en-US/careers.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.bostonscientific.com/content/dam/elabeling/crm/pr/359483-012_LATITUDE_CM_en_S.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.bostonscientific.com/en-US/customer-service.html
- group: company
  title: ''
  type: Blog
  url: https://news.bostonscientific.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.bostonscientific.com/en-US/account/registration.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bostonscientific.com/en-US/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bostonscientific.com/en-US/privacy-policy.html
- group: auth
  title: ''
  type: Security
  url: security/boston-scientific-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/boston-scientific-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/boston-scientific-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boston-scientific-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/boston-scientific-packages.yml
- group: design
  title: ''
  type: Components
  url: components/boston-scientific-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/boston-scientific-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boston-scientific-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/boston-scientific-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/boston-scientific-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boston-scientific-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boston-scientific-llms.txt
coverage:
  checked: '2026-09-04'
  detail: Boston Scientific's only published integration contract — the LATITUDE Integration IDCO and HL7 Specifications, which pins HL7 v2.6 / IHE PCD-09 / ISO-IEEE 11073-10103:2014 by name — ships exclusively as a 7 MB PDF on the eLabeling CDN, with no OpenAPI, AsyncAPI or schema anywhere alongside it.
  evidence:
  - status: 200
    url: https://www.bostonscientific.com/content/dam/elabeling/crm/pr/359483-012_LATITUDE_CM_en_S.pdf
  - status: 404
    url: https://www.bostonscientific.com/openapi.json
  - status: 200
    url: https://cdx.bostonscientific.com/openapi.json
  - status: 404
    url: https://www.bostonscientific.com/.well-known/api-catalog
  reason: pdf-only-docs
  state: unreadable
created: '2026-03-21'
description: Boston Scientific is a global medical device manufacturer that develops, manufactures, and markets devices used in interventional medical specialties including interventional cardiology, cardiac rhythm management, electrophysiology, urology, pelvic health, endoscopy, neuromodulation, and peripheral interventions. The company advances science for life by transforming patient lives through innovative medical solutions.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boston-scientific.png
layout: provider
modified: '2026-09-04'
name: Boston Scientific
nav: Providers
network: true
overview: 'Boston Scientific is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Digital Health, Cardiology, Urology, and Endoscopy.


  Boston Scientific''s developer surface includes documentation, support, engineering blog, signup flow, changelog, and 19 more developer resources.'
plans:
- name: Boston Scientific Plans Pricing
  plan_count: 0
  slug: boston-scientific-plans-pricing
press:
- date: '2026-05-25'
  title: Boston Scientific uses AI in medical tech for 9 years
  url: https://www.linkedin.com/posts/henson-sy-5295232_paid-program-how-ai-is-transforming-health-activity-7325902716625399808-Nhps
- date: '2026-05-25'
  title: How is AI Transforming Healthcare?
  url: https://news.bostonscientific.com/warren-wang-how-is-ai-transforming-healthcare
- date: '2026-05-25'
  title: Buy Boston Scientific Stock. It's a Way to Diversify From AI?
  url: https://www.barrons.com/articles/buy-boston-scientific-stock-price-pick-0001482400
- date: '2026-05-25'
  title: 'Boston Scientific''s AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/boston-scientific-ai-strategy-analysis-of-dominance-in-medical-technologies/
- date: '2026-05-25'
  title: Using AI to predict and prevent cardiac emergencies
  url: https://news.bostonscientific.com/ai-diagnostic-heart-failure-symptoms-arrythmia
random_paper: 20
rate_limits:
- limit_count: 0
  name: Boston Scientific Rate Limits
  slug: boston-scientific-rate-limits
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 25.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boston-scientific/refs/heads/main/screenshots/boston-scientific-2026-06-20T173616.png
security:
- kind: domain-security
  name: Boston Scientific Domain Security
  slug: boston-scientific-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boston Scientific Vulnerability Disclosure
  slug: boston-scientific-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Boston Scientific Trust Center
  slug: boston-scientific-trust-center
  summary_line: trust center published
slug: boston-scientific
tags:
- Medical Devices
- Digital Health
- Cardiology
- Urology
- Endoscopy
- Neuromodulation
- Fortune 500
website: https://www.bostonscientific.com
---
