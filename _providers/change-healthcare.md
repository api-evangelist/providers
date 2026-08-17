---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://developer.optum.com/eligibilityandclaims/docs/create-a-sandbox-account
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: JSON-over-REST front end to the HIPAA X12 EDI transaction set — 270/271 eligibility, 276/277 claim status, 837P/837I claim submission and validation, 835/277 claims responses and reports, 278 prior au
  name: Change Healthcare Medical Network API
  slug: change-healthcare-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.changehealthcare.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.optum.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.changehealthcare.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optum.com/en/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optum.com/en/privacy-policy.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/change-healthcare-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/change-healthcare-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/change-healthcare-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/change-healthcare-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/change-healthcare-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/change-healthcare
coverage:
  checked: '2026-08-15'
  detail: Change Healthcare no longer operates a developer surface of its own — UnitedHealth Group absorbed it into Optum, www.changehealthcare.com 301s to business.optum.com, developers.changehealthcare.com 301s to developer.optum.com, and Optum's own documentation tells integrators "Do not use the https://apis.changehealthcare.com as it is an old domain and no longer supported"; the surviving Medical Network API contracts are served from apigw.optum.com and are catalogued under all/optum rather than duplicated here.
  evidence:
  - status: 301
    url: https://www.changehealthcare.com/
  - status: 301
    url: https://developers.changehealthcare.com/
  - status: 400
    url: https://apis.changehealthcare.com/openapi.json
  - status: 0
    url: https://api.changehealthcare.com/
  - status: 200
    url: https://developer.optum.com/eligibilityandclaims/docs/api-urls
  reason: defunct
  state: none
created: '2026-04-19'
description: 'Change Healthcare was one of the largest healthcare technology and clearinghouse companies in the United States, moving eligibility, claim, remittance and prior-authorization transactions between providers and payers over X12 EDI. UnitedHealth Group acquired it in October 2022 and folded it into Optum, and the brand has since been retired: www.changehealthcare.com redirects to business.optum.com, developers.changehealthcare.com redirects path-for-path to developer.optum.com, and the apis.changehealthcare.com API gateway is decommissioned and documented by Optum as "an old domain and no longer supported". The Change Healthcare Medical Network APIs — Eligibility v3, Professional Claims v3, Institutional Claims v1, Claim Status v2, Claims Responses and Reports v2, Attachments, PayerList v1 and Prior Authorization v1 — are still operated and documented, but on Optum infrastructure and under Optum hosts.'
finops:
- name: Change Healthcare Finops
  service_category: Healthcare / Data Exchange
  slug: change-healthcare-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/change-healthcare.png
layout: provider
modified: '2026-08-15'
name: Change Healthcare
nav: Providers
network: true
overview: 'Change Healthcare publishes 1 API on the [APIs.io](https://apis.io/) network: Medical Network API. Tagged areas include Healthcare, Technology, Analytics, EDI, and Claims.'
plans:
- name: Change Healthcare Plans Pricing
  plan_count: 0
  slug: change-healthcare-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 0
  name: Change Healthcare Rate Limits
  slug: change-healthcare-rate-limits
score:
  band: emerging
  composite: 20.2
  delta: 1.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 18.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/change-healthcare/refs/heads/main/screenshots/change-healthcare-2026-06-20T174215.png
security:
- kind: domain-security
  name: Change Healthcare Domain Security
  slug: change-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: change-healthcare
tags:
- Healthcare
- Technology
- Analytics
- EDI
- Claims
- Eligibility
- Clearinghouse
- Revenue Cycle Management
- Prior Authorization
website: https://www.changehealthcare.com
---
