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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peaxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peaxy.net/
- group: company
  title: ''
  type: Blog
  url: https://peaxy.net/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://peaxy.net/feed/
- group: operate
  title: ''
  type: Support
  url: https://peaxy.net/request-live-demo/
- group: start
  title: ''
  type: SignUp
  url: https://peaxy.net/request-live-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://peaxy.net/general-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://peaxy.net/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://peaxy.net/soc2certification/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peaxy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peaxy-inc-/
- group: design
  title: ''
  type: Conformance
  url: conformance/peaxy-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/peaxy-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/peaxy-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/peaxy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/peaxy-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/peaxy-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Peaxy markets "a range of open API's" on four product pages but publishes no developer portal, API reference or machine-readable contract anywhere — every route to the platform is the /request-live-demo/ form, and the only host that answers is the WordPress marketing site.
  evidence:
  - status: 200
    url: https://peaxy.net/build/
  - status: 404
    url: https://peaxy.net/developers
  - status: 404
    url: https://peaxy.net/api-reference
  - status: 404
    url: https://peaxy.net/openapi.json
  - status: 404
    url: https://peaxy.net/.well-known/agent-card.json
  - status: 302
    url: https://peaxy.com/
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: Peaxy, Inc. is a San Jose, California industrial AI and digital-twin software company founded in 2012, with offices in Stockholm, Sweden and Cagliari, Italy. Its Peaxy Lifecycle Intelligence (PLI) platform threads design, test, manufacturing, field and service data for mission-critical physical assets into a single cloud-based source of truth, then applies machine learning to predict failures, extend asset life and support warranty, quality and readiness decisions. Product lines cover battery and energy-storage analytics (R&D through manufacturing, deployment and second life), defense readiness and predictive maintenance for the U.S. Department of Defense and Department of Energy, critical infrastructure and airport/circuit-level AI, a battery LIMS, and EcoGrid for renewable energy communities. Peaxy markets "a range of open APIs" for platform integration, but publishes no public developer portal, API reference or machine-readable contract — access runs through a demo request
  and a customer engagement. The platform is SOC 2 Type II certified and aligned to NIST 800-171.
image: https://peaxy.net/wp-content/uploads/2021/10/logo.svg
layout: provider
modified: '2026-08-26'
name: Peaxy
nav: Providers
network: true
overview: 'Peaxy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial AI, Digital Twin, Battery Analytics, and Energy Storage.


  Peaxy''s developer surface includes engineering blog, support, signup flow, and 14 more developer resources.'
plans:
- name: Peaxy Plans Pricing
  plan_count: 0
  slug: peaxy-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Peaxy Rate Limits
  slug: peaxy-rate-limits
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 20.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 32.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peaxy/refs/heads/main/screenshots/peaxy-2026-09-02T150928.png
security:
- kind: domain-security
  name: Peaxy Domain Security
  slug: peaxy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: peaxy
tags:
- Company
- Industrial AI
- Digital Twin
- Battery Analytics
- Energy Storage
- Predictive Maintenance
- Asset Management
- Manufacturing
- Defense
- Analytics
- Data Management
- Machine-Learning
website: https://peaxy.net/
---
