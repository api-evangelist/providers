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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meetash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.poweredbyash.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ashwellness.io
- group: company
  title: ''
  type: Blog
  url: https://www.poweredbyash.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.poweredbyash.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.poweredbyash.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.poweredbyash.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.poweredbyash.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.poweredbyash.com
- group: design
  title: ''
  type: Conformance
  url: conformance/meetash-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meetash-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ashwellness.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meetash-llms.txt
coverage:
  checked: '2026-08-15'
  detail: 'Ash markets a "developer-friendly REST API" on its FAQ and platform pages, but its entire developer surface — docs.ashwellness.io, a ReadMe hub — is in password-protected mode: every path 302s to /password?redirect=<path> and the host''s robots.txt is "User-agent: * / Disallow: /", so no reference, no OpenAPI, no auth page and no rate-limit or pricing detail is publicly readable and the only way in is the contact-sales form.'
  evidence:
  - status: 302
    url: https://docs.ashwellness.io/
  - status: 302
    url: https://docs.ashwellness.io/reference
  - status: 200
    url: https://docs.ashwellness.io/robots.txt
  - status: 200
    url: https://www.poweredbyash.com/frequently-asked-questions
  reason: partner-login
  state: gated
created: '2026-07-17'
description: Ash (MeetAsh / Ash Wellness) is a New York-based health technology company, founded in 2019, that powers white-label at-home health testing programs for health plans, digital health companies, and public health organizations. Through a single, developer-friendly REST API integration, partners can trigger test kits, manage shipping logistics, and securely transmit results back into an EHR or patient portal across a national network of CLIA- and CAP-certified laboratories. Ash offers 120+ at-home diagnostic panels (hormone, cancer, allergy, STI, chronic condition, and infectious-disease testing with self-collected blood, stool, urine, saliva, and swab samples), care-gap-closure programs for HEDIS measures, kitting and fulfillment, physician-of-record services, and real-time reporting dashboards. The platform is fully HIPAA compliant and SOC 2 Type II certified, with enterprise-grade encryption protecting PHI. Surfaced as a 500 Global portfolio company and enriched into the API
  Evangelist network; the developer documentation is partner-gated (password protected).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meetash.png
layout: provider
modified: '2026-08-15'
name: MeetAsh
nav: Providers
network: true
overview: 'MeetAsh is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Diagnostics, and At-Home Testing.


  MeetAsh''s developer surface includes documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Meetash Plans Pricing
  plan_count: 0
  slug: meetash-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Meetash Rate Limits
  slug: meetash-rate-limits
score:
  band: emerging
  composite: 20.7
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 20.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meetash/refs/heads/main/screenshots/meetash-2026-08-07T172422.png
security:
- kind: domain-security
  name: Meetash Domain Security
  slug: meetash-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Meetash Trust Center
  slug: meetash-trust-center
  summary_line: HIPAA, SOC 2 Type II, CLIA, CAP
slug: meetash
tags:
- Company
- Health
- Healthcare
- Diagnostics
- At-Home Testing
- Lab Testing
- Digital Health
- Telehealth
- HIPAA
website: https://www.poweredbyash.com
---
