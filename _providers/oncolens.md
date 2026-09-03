---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 17.6
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/oncolens-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oncolens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oncolens.com/
- group: company
  title: ''
  type: Blog
  url: https://www.oncolens.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.oncolens.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oncolens.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://signin.oncolens.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OncoLens
- group: auth
  title: ''
  type: Compliance
  url: conformance/oncolens-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oncolens-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oncolens-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oncolens-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oncolens-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oncolens-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/oncolens-login-openid-configuration.json
- group: commercial
  title: ''
  type: Plans
  url: plans/oncolens-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oncolens-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oncolens-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/oncolens-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oncolens-conventions.yml
created: '2026-08-26'
description: OncoLens is an Atlanta, Georgia based AI-enabled digital healthcare platform for oncology, delivering workflow and analytics software to cancer programs and life science organizations. The platform extracts structured insight from unstructured clinical, pathology and laboratory data in the EMR to power multidisciplinary tumor board and case conference workflow, cancer registry abstraction and casefinding automation, accreditation and quality-metric reporting (CoC, NAPBC, NAPRC, ASCO QOPI), biomarker and precision-medicine tracking, real-world data analytics, and AI-assisted clinical trial matching and patient identification. Through the OncoLens Research Network it connects cancer centers with pharmaceutical and biotech sponsors for real-world data, quality improvement and industry-sponsored trial initiatives. OncoLens reports 220+ cancer centers, 45,000+ multidisciplinary physicians and 5M+ oncology patients under care on the platform. The product is delivered as a customer-facing
  SaaS application behind an Auth0-backed single sign-on; OncoLens publishes no public developer portal, API reference, or machine-readable API contract.
image: https://www.oncolens.com/wp-content/uploads/2022/10/ocl-logo-tm.svg
layout: provider
modified: '2026-08-26'
name: OncoLens
nav: Providers
network: true
overview: 'OncoLens is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Oncology, Cancer Care, and Clinical Trials.


  OncoLens'' developer surface includes engineering blog, support, authentication, and 17 more developer resources.'
plans:
- name: Oncolens Plans Pricing
  plan_count: 0
  slug: oncolens-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Oncolens Rate Limits
  slug: oncolens-rate-limits
scopes:
- name: Oncolens Scopes
  scope_count: 0
  slug: oncolens-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 22.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 61.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oncolens/refs/heads/main/screenshots/oncolens-2026-09-02T150840.png
security:
- kind: authentication
  name: Oncolens Authentication
  slug: oncolens-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Oncolens Domain Security
  slug: oncolens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Oncolens Trust Center
  slug: oncolens-trust-center
  summary_line: SOC 2, HIPAA, SOC 3, ISO 27001, HITRUST, PCI DSS, FedRAMP
slug: oncolens
tags:
- Company
- Healthcare
- Oncology
- Cancer Care
- Clinical Trials
- Health Data
- Real-World Data
- Artificial Intelligence
- Analytics
- Clinical Workflow
- Cancer Registry
- Life Sciences
- Software-as-a-Service
website: https://www.oncolens.com/
---
