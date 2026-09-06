---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
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
    well_known_catalog: true
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: REST API for the Bakuraku (バクラク) back-office suite. Publicly documented capabilities are retrieval and list-search of applications/requests (申請), download of attached files, creation of applications f
  name: Bakuraku API
  slug: bakuraku-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://layerx.co.jp/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bakuraku.jp/workflow/function/api/
- group: docs
  title: ''
  type: Documentation
  url: https://bakuraku.jp/workflow/function/api/
- group: docs
  title: ''
  type: APIReference
  url: https://api.bakuraku.layerx.jp/rest/docs/
- group: operate
  title: ''
  type: Support
  url: https://bakuraku-login.layerx.jp/hc/ja
- group: company
  title: ''
  type: Blog
  url: https://tech.layerx.co.jp/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LayerXcom
- group: commercial
  title: ''
  type: Pricing
  url: https://bakuraku.jp/expense/price/
- group: start
  title: ''
  type: SignUp
  url: https://id.layerx.jp/auth/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bakuraku.jp/terms/api-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://layerx.co.jp/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://bakuraku-status.jp/
- group: auth
  title: ''
  type: Security
  url: https://layerx.co.jp/security_policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://bakuraku.jp/security/
- group: auth
  title: ''
  type: Compliance
  url: conformance/layerx-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/layerx-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/layerx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/layerx-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/layerx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/layerx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/layerx-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/layerx-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/layerx-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/layerx-plans-pricing.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/layerx-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/layerx-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/layerx-llms.txt
coverage:
  checked: '2026-08-23'
  detail: 'The Bakuraku REST API is live and reachable at https://api.bakuraku.layerx.jp/rest — it answers anonymous calls with its own JSON error envelope and an x-layerx-request-id header — but its reference at /rest/docs/ sits behind HTTP Basic auth at the AWS load balancer (401, WWW-Authenticate: Basic), issued only to companies LayerX has approved as an "API契約者" on top of an existing Bakuraku subscription, and the API terms state the specification document is supplied separately to those customers, so no OpenAPI exists at any public URL.'
  evidence:
  - status: 401
    url: https://api.bakuraku.layerx.jp/rest/docs/
  - status: 400
    url: https://api.bakuraku.layerx.jp/rest/v1/tenant/users
  - status: 404
    url: https://api.bakuraku.layerx.jp/openapi.json
  - status: 200
    url: https://bakuraku.jp/terms/api-terms/
  reason: customer-only-docs
  state: gated
created: '2026-08-23'
description: 'LayerX Inc. (株式会社LayerX) is a Tokyo-based enterprise software company founded 1 August 2018, operating as a compound startup across four business lines: Bakuraku (バクラク), an AI back-office suite covering expense reimbursement, invoice receipt and issuance, workflow and approvals, electronic bookkeeping, attendance, payroll and a corporate card; Ai Workforce, an enterprise LLM document-processing platform; a Fintech business run through the Mitsui-X / Mitsui & Co. Digital Asset Management joint venture; and a Security business added through the April 2026 acquisition of AgenticSec Inc. Its developer surface is the Bakuraku API — a REST API at api.bakuraku.layerx.jp built on an internal unified GraphQL gateway and tsoa, exposing application/approval retrieval and creation, attachment download, and tenant user, group and position directories. API access is granted by application to existing Bakuraku customers, who are issued a scoped API key from the Bakuraku admin console; the
  API reference at /rest/docs/ is HTTP Basic protected and no OpenAPI definition is published publicly.'
image: https://layerx.co.jp/wp-content/uploads/2023/10/cropped-Icon_Square-300x300.png
layout: provider
modified: '2026-08-23'
name: LayerX
nav: Providers
network: true
overview: 'LayerX publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Japan, Back Office, Expense Management, and Invoicing.


  LayerX''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 20 more developer resources.'
plans:
- name: Layerx Plans Pricing
  plan_count: 0
  slug: layerx-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Layerx Rate Limits
  slug: layerx-rate-limits
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 41.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 37.0
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/layerx/refs/heads/main/screenshots/layerx-2026-09-02T150224.png
security:
- kind: authentication
  name: Layerx Authentication
  slug: layerx-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Layerx Domain Security
  slug: layerx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Layerx Vulnerability Disclosure
  slug: layerx-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Layerx Trust Center
  slug: layerx-trust-center
  summary_line: ISO/IEC 27001 (ISMS), SOC 1 Type 2, JIIMA 電帳法スキャナ保存ソフト法的要件認証, JIIMA 電帳法電子取引ソフト法的要件認証
slug: layerx
tags:
- Company
- Japan
- Back Office
- Expense Management
- Invoicing
- Accounts Payable
- Workflows
- Approvals
- Accounting
- Payroll
- Attendance
- Corporate Cards
- Artificial Intelligence
- AI Agents
- Document Processing
- Software-as-a-Service
- Enterprise Software
- Fintech
website: https://layerx.co.jp/
---
