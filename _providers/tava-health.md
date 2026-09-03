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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tava-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tavahealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tavahealth.com/
- group: operate
  title: ''
  type: Support
  url: https://www.tavahealth.com/get-help
- group: company
  title: ''
  type: Blog
  url: https://www.tavahealth.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tava-health
- group: start
  title: ''
  type: SignUp
  url: https://care.tavahealth.com/signup
- group: start
  title: ''
  type: Login
  url: https://care.tavahealth.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tavahealth.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tavahealth.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://tavahealth.statuspage.io/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tava-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tava-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/tava-health-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/tava-health-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tava-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tava-health-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tava-health-llms.txt
coverage:
  checked: '2026-08-29'
  detail: Tava Health's only developer documentation is the ReadMe.io hub titled "DirectCare by Tava Health" at docs.tavahealth.com, which is protected by a project-level password issued to contracted partners — every path, including /reference, /changelog and /sitemap.xml, returns 302 to /password?redirect=<path>, and a control probe of a path that does not exist returned the identical 302, confirming the gate is universal rather than a missing page.
  evidence:
  - status: 302
    url: https://docs.tavahealth.com/reference
  - status: 302
    url: https://docs.tavahealth.com/openapi.json
  - status: 302
    url: https://docs.tavahealth.com/zzz-does-not-exist-9182
  - status: 404
    url: https://www.tavahealth.com/openapi.json
  - status: 404
    url: https://www.tavahealth.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-29'
description: 'Tava Health, Inc. is a Utah-founded (2019) digital behavioral-health company that sells mental health care as an employer and health-plan benefit. Employers, health plans and provider groups contract with Tava; covered members are matched to a licensed therapist — typically within about twelve hours — and receive care over secure video or in person through a nationwide clinical network. Care is delivered by Tava Professionals, a set of state-level professional entities that act as the HIPAA covered entity, while Tava Health, Inc. operates the technology platform as their business associate. The platform runs as two portals: a client portal at care.tavahealth.com for members and a provider/administrative portal at app.tavahealth.com for therapists and plan administrators. Tava also runs DirectCare, a partner-facing product with its own developer hub at docs.tavahealth.com; that hub is a ReadMe.io site and is password-protected, so no public API reference, OpenAPI definition
  or other machine-readable contract is available at this time.'
image: https://cdn.prod.website-files.com/69b16eaa32e6453c489312a1/69b16eaa32e6453c489312ea_649c6f80719c67b8516a71ee_webclip.webp
layout: provider
modified: '2026-08-29'
name: Tava Health
nav: Providers
network: true
overview: 'Tava Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Mental Health, Behavioral Health, and Telehealth.


  Tava Health''s developer surface includes support, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Tava Health Plans Pricing
  plan_count: 0
  slug: tava-health-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Tava Health Rate Limits
  slug: tava-health-rate-limits
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 17.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tava-health/refs/heads/main/screenshots/tava-health-2026-09-02T162617.png
security:
- kind: domain-security
  name: Tava Health Domain Security
  slug: tava-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tava-health
tags:
- Company
- Healthcare
- Mental Health
- Behavioral Health
- Telehealth
- Employee Benefits
- Health Plans
- HIPAA
- Digital Health
- Care Delivery
website: https://www.tavahealth.com/
---
