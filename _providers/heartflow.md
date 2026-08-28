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
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Production REST API behind the Heartflow One platform, observed live at https://api.heartflow.net. Every probed route answers with the Django REST Framework challenge {"detail":"Authentication credent
  name: Heartflow One Platform API
  slug: heartflow-one-platform-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/heartflow-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heartflow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.heartflow.com/
- group: operate
  title: ''
  type: Support
  url: https://www.heartflow.com/heartflow-one/support/
- group: company
  title: ''
  type: Blog
  url: https://www.heartflow.com/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HeartFlow
- group: start
  title: ''
  type: Login
  url: https://app.heartflow.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.heartflow.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.heartflow.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: conformance/heartflow-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/heartflow-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/heartflow-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heartflow-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/heartflow-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heartflow-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/heartflow-lifecycle.yml
coverage:
  checked: '2026-08-22'
  detail: Heartflow runs a live Django REST Framework API at api.heartflow.net whose every route, including the mounted /swagger/ and /redoc/ reference pages, answers 403 "Authentication credentials were not provided.", and its documentation host docs.heartflow.net is a CloudFront distribution gated by signed cookies that returns 403 MissingKey on every path, so the contract exists but is issued only to contracted institutional customers.
  evidence:
  - status: 403
    url: https://api.heartflow.net/api/v1/
  - status: 403
    url: https://api.heartflow.net/swagger/
  - status: 403
    url: https://docs.heartflow.net/openapi.json
  - status: 404
    url: https://api.heartflow.net/openapi.json
  - status: 404
    url: https://www.heartflow.com/llms.txt
  reason: customer-only-docs
  state: gated
created: '2026-08-22'
description: 'Heartflow, Inc. (Nasdaq: HTFL) is a healthcare technology company founded in 2010 and headquartered in San Francisco, California. Its Heartflow One platform applies AI to coronary computed tomography angiography (CCTA) to non-invasively diagnose and manage coronary artery disease, bundling Roadmap Analysis, FFRct Analysis, Plaque Analysis, Plaque Staging and the PCI Navigator, and delivering results back into hospital PACS and EMR systems. More than 650,000 patients have been analyzed across 1,800+ institutions. Heartflow runs a production REST API at api.heartflow.net and customer documentation at docs.heartflow.net, but both are authenticated: there is no public developer program, no published OpenAPI, and no self-serve signup.'
image: https://www.heartflow.com/wp-content/uploads/2025/01/heartflow_logo_white.svg
layout: provider
modified: '2026-08-22'
name: HeartFlow
nav: Providers
network: true
overview: 'HeartFlow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Imaging, Artificial Intelligence, and Cardiology.


  HeartFlow''s developer surface includes support, engineering blog, and 14 more developer resources.'
plans:
- name: Heartflow Plans Pricing
  plan_count: 0
  slug: heartflow-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Heartflow Rate Limits
  slug: heartflow-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 21.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Heartflow Authentication
  slug: heartflow-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Heartflow Domain Security
  slug: heartflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Heartflow Trust Center
  slug: heartflow-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO 13485:2016, HITRUST, HIPAA, GDPR, CCPA
slug: heartflow
tags:
- Company
- Healthcare
- Medical Imaging
- Artificial Intelligence
- Cardiology
- Diagnostics
- Medical Devices
- Radiology
- Clinical Decision Support
- Machine Learning
website: https://www.heartflow.com/
---
