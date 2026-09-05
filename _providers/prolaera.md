---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://prolaera.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.lcvista.com/prolaera — a different registrable domain (prolaera.com -> lcvista.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://prolaera.com
- group: start
  title: ''
  type: SignUp
  url: https://app.prolaera.com/
- group: start
  title: ''
  type: Login
  url: https://app.prolaera.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lcvista.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.lcvista.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lcvista.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lcvista.com/terms-of-use
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prolaera-domain-security.yml
created: '2026-07-17'
description: Prolaera is a learning and compliance platform built for modern CPAs and accounting firms, combining automated CPE (Continuing Professional Education) tracking, a learning management system (LMS), and a built-in course library so firms can administer training, monitor license and compliance requirements, and manage professional development in one place. Prolaera merged with LCvista and now operates as "Prolaera by LCvista"; the product is delivered as a hosted SaaS application at app.prolaera.com with SSO/SAML 2.0 identity support and SCORM/AICC/xAPI content compatibility. It is a portfolio company of 500 Global. Prolaera does not currently publish a public developer API, developer portal, or machine-readable API specifications.
image: https://www.lcvista.com/hubfs/lcvista-symbol-round-color.png
layout: provider
modified: '2026-07-20'
name: Prolaera
nav: Providers
network: true
overview: 'Prolaera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Continuing Professional Education, CPE, Compliance, and Learning Management System.


  Prolaera''s developer surface includes signup flow, engineering blog, support, and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prolaera/refs/heads/main/screenshots/prolaera-2026-09-02T152133.png
security:
- kind: domain-security
  name: Prolaera Domain Security
  slug: prolaera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prolaera
tags:
- Company
- Continuing Professional Education
- CPE
- Compliance
- Learning Management System
- Accounting
- Professional Development
- Software-as-a-Service
website: https://prolaera.com
---
