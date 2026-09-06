---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://intuscare.com/
- group: company
  title: ''
  type: About
  url: https://intuscare.com/about-intuscare/
- group: company
  title: ''
  type: Blog
  url: https://intuscare.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://intuscare.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://intuscare.com/contact-us/
- group: start
  title: ''
  type: Login
  url: https://carehub.intus.care/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://intuscare.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IntusCare
- group: other
  title: ''
  type: CaseStudies
  url: https://intuscare.com/case-studies/
- group: company
  title: ''
  type: Careers
  url: https://intuscare.com/careers/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/intus-care
- group: company
  title: ''
  type: Twitter
  url: https://x.com/intus_care
- group: design
  title: ''
  type: Conformance
  url: conformance/intus-care-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/intus-care-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intus-care-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/intus-care-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/intus-care-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intus-care-llms.txt
coverage:
  checked: '2026-08-23'
  detail: IntusCare sells CareHub, IRIS and its population-health suite as authenticated SaaS to PACE organizations and delivers TPA integrations itself, so it ships no developer portal, API reference or machine-readable contract — carehub.intus.care, the one product origin that returns honest status codes, 404s on /openapi.json, /fhir/R4/metadata and every /.well-known/ path, and no api./developer./docs. subdomain resolves on either intuscare.com or intus.care.
  evidence:
  - status: 404
    url: https://carehub.intus.care/openapi.json
  - status: 404
    url: https://carehub.intus.care/fhir/R4/metadata
  - status: 404
    url: https://carehub.intus.care/.well-known/agent-card.json
  - status: 200
    url: https://intus.care/robots.txt
  - status: 202
    url: https://intuscare.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-23'
description: IntusCare (Intus Care, Inc.) is a Providence, Rhode Island health technology company building an end-to-end software and services ecosystem for PACE — Programs of All-Inclusive Care for the Elderly. Founded in 2019 by Brown University students Robbie Felton, Evan Jackson and Alex Rothberg, it launched population health analytics at PACE of Rhode Island in 2020 and now serves 70+ PACE organizations. Its products are CareHub, a PACE-native ONC-certified EMR and care-management platform; IRIS, a risk-adjustment and coding system for PACE and value-based care organizations; and a Population Health & Utilization Management suite delivered with fractionally-staffed Integrated Care Services clinicians. IntusCare markets interoperability and out-of-the-box third-party administrator (TPA) integrations, but as of this profile it publishes no public developer program, API reference, or machine-readable contract — customer-facing surfaces are the authenticated CareHub and analytics applications.
image: https://intuscare.com/wp-content/uploads/2025/05/logo-intuscare-Favicon.png
layout: provider
modified: '2026-08-23'
name: Intus Care
nav: Providers
network: true
overview: 'Intus Care is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Electronic Health Records, Population Health, Risk Adjustment, and Senior Care.


  Intus Care''s developer surface includes engineering blog, support, and 16 more developer resources.'
plans:
- name: Intus Care Plans Pricing
  plan_count: 0
  slug: intus-care-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Intus Care Rate Limits
  slug: intus-care-rate-limits
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 14.5
    commercial_clarity: 14.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 11.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intus-care/refs/heads/main/screenshots/intus-care-2026-09-02T145915.png
security:
- kind: domain-security
  name: Intus Care Domain Security
  slug: intus-care-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: intus-care
tags:
- Healthcare
- Electronic Health Records
- Population Health
- Risk Adjustment
- Senior Care
- Value-Based Care
- Analytics
- Compliance
- Utilization Management
- PACE
website: https://intuscare.com/
---
