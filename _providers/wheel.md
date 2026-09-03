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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.wheel.com/
- group: company
  title: ''
  type: Blog
  url: https://www.wheel.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://wheelhealth.statuspage.io/
- group: auth
  title: ''
  type: Compliance
  url: https://www.wheel.com/security-compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/wheel-trust-center.yml
- group: operate
  title: ''
  type: Support
  url: https://www.wheel.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wheel.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wheel.com/terms-of-use
- group: commercial
  title: ''
  type: Legal
  url: https://www.wheel.com/api-terms-of-use
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wheel-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wheel-lifecycle.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wheel.com/
- group: start
  title: ''
  type: Login
  url: https://clinicians.wheel.health
- group: design
  title: ''
  type: Conformance
  url: conformance/wheel-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/wheel-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wheel-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wheel-llms.txt
coverage:
  checked: '2026-08-15'
  detail: Wheel's developer portal at developers.wheel.com is a Netlify site behind site-wide password protection that answers HTTP 401 "Password Protection" to every path — including /openapi.json, /llms.txt and /.well-known/* — and its API Terms of Use §3 require an approved organizational agreement before Access Credentials are issued, so the contract is unreadable without a signed customer relationship.
  evidence:
  - status: 401
    url: https://developers.wheel.com/
  - status: 401
    url: https://developers.wheel.com/openapi.json
  - status: 404
    url: https://api.wheel.health/openapi.json
  - status: 404
    url: https://www.wheel.com/.well-known/api-catalog
  - status: 200
    url: https://wheelhealth.statuspage.io/api/v2/summary.json
  reason: customer-only-docs
  state: gated
created: '2026-07-17'
description: Wheel is a healthcare technology company providing the infrastructure for modern telehealth. Its Wheel Horizon platform is a modular care-enablement system that combines a nationwide clinician network, evidence-based virtual care programs, and integrated clinical operations so digital health companies, health plans, retailers and pharmacies, and life-sciences organizations can launch and scale virtual care. Wheel also operates WheelX, an enterprise AI health exchange, and Connected Services for integration. Wheel exposes a partner API, governed by an API Terms of Use and gated behind an approval process; the platform is HIPAA compliant and maintains SOC 2 controls. Public API reference documentation, SDKs, and a developer portal are not published. Wheel was surfaced as a portfolio company of CRV.
image: https://www.wheel.com/apple-touch-icon.png
layout: provider
modified: '2026-08-15'
name: Wheel
nav: Providers
network: true
overview: 'Wheel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Virtual Care, and Digital Health.


  Wheel''s developer surface includes engineering blog, support, legal docs, and 14 more developer resources.'
plans:
- name: Wheel Plans Pricing
  plan_count: 0
  slug: wheel-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Wheel Rate Limits
  slug: wheel-rate-limits
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 23.7
  provenance:
    conformance: first-party
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wheel/refs/heads/main/screenshots/wheel-2026-09-02T170651.png
security:
- kind: domain-security
  name: Wheel Domain Security
  slug: wheel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wheel Trust Center
  slug: wheel-trust-center
  summary_line: SOC 2, HIPAA
slug: wheel
tags:
- Company
- Healthcare
- Telehealth
- Virtual Care
- Digital Health
- Clinician Network
- Care Enablement
- HIPAA
website: https://www.wheel.com/
---
