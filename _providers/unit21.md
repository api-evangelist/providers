---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for ingesting entities, instruments, and transaction events into the Unit21 risk and compliance platform. Enables creation and management of alerts, cases, rules, and suspicious activity repo
  name: Unit21 API
  slug: unit21-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/unit21-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unit21-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unit21-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unit21.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unit21.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/u21
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unit21/
- group: company
  title: ''
  type: Blog
  url: https://www.unit21.ai/resources/risk-compliance-blog
- group: other
  title: ''
  type: X
  url: https://twitter.com/unit21inc
- group: operate
  title: ''
  type: Support
  url: https://support.unit21.ai/hc/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.unit21.ai/security
- group: commercial
  title: ''
  type: Plans
  url: plans/unit21-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unit21-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unit21-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unit21.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unit21.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unit21-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/unit21-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unit21-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unit21-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unit21-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unit21-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unit21-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/unit21-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unit21-data-model.yml
coverage:
  checked: '2026-08-27'
  detail: Every path on docs.unit21.ai -- the API reference, the release notes, and even nonexistent paths -- now returns the same 7,947-byte "Sign in | Unit21" page asking you to email for an access link, and status.unit21.ai redirects into that same login, so the entire Unit21 developer and operational surface is readable only by existing customers.
  evidence:
  - status: 200
    url: https://docs.unit21.ai/reference/api-reference
  - status: 200
    url: https://docs.unit21.ai/page/release-notes
  - status: 200
    url: https://docs.unit21.ai/docs/nonexistent-zzz-control
  - status: 200
    url: http://status.unit21.ai/
  - status: 401
    url: https://sandbox1-api.unit21.com/v1/entities/list
  - status: 200
    url: https://www.unit21.ai/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-06-13'
description: Unit21 is an agentic AI platform for fraud and AML (Anti-Money Laundering) detection and compliance operations. It provides a REST API for ingesting transaction data, managing detection rules, reviewing alerts, and filing suspicious activity reports (SARs). The platform supports real-time transaction monitoring, case management, entity and instrument tracking, and automated regulatory filing including SARs, STRs, CTRs, and goAML reports.
finops:
- name: Unit21 Finops
  service_category: ''
  slug: unit21-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unit21.png
jsonld:
- class_count: 0
  name: Unit21 Context
  property_count: 0
  slug: unit21-context
layout: provider
modified: '2026-08-27'
name: Unit21
nav: Providers
network: true
overview: 'Unit21 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fraud Detection, AML, Anti-Money Laundering, Compliance, and Fintech.


  The Unit21 catalog on APIs.io includes 1 JSON-LD context.


  Unit21''s developer surface includes documentation, engineering blog, support, authentication, and 21 more developer resources.'
plans:
- name: Unit21 Plans Pricing
  plan_count: 1
  slug: unit21-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Unit21 Rate Limits
  slug: unit21-rate-limits
score:
  band: thin
  composite: 27.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.0
    catalog_earned_first_party: 8.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 17.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 27.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unit21/refs/heads/main/screenshots/unit21-2026-06-20T200036.png
security:
- kind: authentication
  name: Unit21 Authentication
  slug: unit21-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Unit21 Domain Security
  slug: unit21-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unit21 Vulnerability Disclosure
  slug: unit21-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Unit21 Trust Center
  slug: unit21-trust-center
  summary_line: SOC 2, GDPR
slug: unit21
tags:
- Fraud Detection
- AML
- Anti-Money Laundering
- Compliance
- Fintech
- Transaction Monitoring
- Risk
- SAR
- Financial Crime
- Suspicious Activity Reports
website: https://www.unit21.ai/
---
