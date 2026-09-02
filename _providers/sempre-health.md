---
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sempre-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.semprehealth.com/
- group: operate
  title: ''
  type: Support
  url: https://www.semprehealth.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.semprehealth.com/press/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/semprehealth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.semprehealth.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.semprehealth.com/privacy/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/sempre-health-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sempre-health-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sempre-health-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sempre-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sempre-health-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sempre-health-trust-center.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sempre-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sempre-health-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Sempre Health markets no API at all - /developers, /developer, /api, /apis, /docs, /integrations and /partners are all HTTP 404 on the WordPress corporate site, its own health-plans page describes payer integration as the plan sharing a list of eligible members rather than as an API, and the one docs host that exists, docs.semprehealth.com, sits on Netlify and returned HTTP 429 with an empty body to every request from two separate networks while being indexed by no search engine.
  evidence:
  - status: 404
    url: https://www.semprehealth.com/developers
  - status: 404
    url: https://www.semprehealth.com/api
  - status: 404
    url: https://www.semprehealth.com/openapi.json
  - status: 429
    url: https://docs.semprehealth.com/
  - status: 200
    url: https://eligibility.semprehealth.com/.well-known/agent-card.json
  - status: 404
    url: https://pypi.org/pypi/semprehealth/json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Sempre Health is a San Francisco based digital health company, founded in 2015, that operates a behavior-based dynamic pricing platform for prescription medications. Working with health plans, pharmacy benefit managers and pharmaceutical manufacturers, it enrolls covered members and adjusts their copay at the point of fill through SMS outreach: the more consistently a member refills on time, the deeper the discount. The company reports more than 19 payer and PBM partners covering roughly 60% of commercially insured lives in the United States, availability at retail pharmacies in all 50 states, and HITRUST certification alongside a signed BAA with each plan. As of this profile Sempre Health publishes no public developer program, API reference, or machine-readable API contract; its own health-plans page describes payer integration as sharing a list of eligible members rather than as an API.'
image: https://www.semprehealth.com/wp-content/uploads/2022/01/cropped-SempreHealthFavicon-192x192-1.png
layout: provider
modified: '2026-08-26'
name: Sempre Health
nav: Providers
network: true
overview: 'Sempre Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Pharmacy.


  Sempre Health''s developer surface includes support, engineering blog, and 13 more developer resources.'
plans:
- name: Sempre Health Plans Pricing
  plan_count: 0
  slug: sempre-health-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Sempre Health Rate Limits
  slug: sempre-health-rate-limits
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 19.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Sempre Health Domain Security
  slug: sempre-health-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Sempre Health Vulnerability Disclosure
  slug: sempre-health-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Sempre Health Trust Center
  slug: sempre-health-trust-center
  summary_line: HITRUST, HIPAA Business Associate Agreement (BAA)
slug: sempre-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Pharmacy
- Pharmacy Benefits
- Prescriptions
- Medication Adherence
- Patient Engagement
- Health Plans
- SMS
website: https://www.semprehealth.com/
---
