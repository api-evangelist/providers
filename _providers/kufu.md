---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://app.smarthr.jp/api/v1
  baseurl_source: declared
  description: カスタム家族項目テンプレートを操作します
  name: KUFU カスタム家族項目テンプレート API
  slug: kufu-default-api
- baseURL: https://app.smarthr.jp/api/v1
  baseurl_source: declared
  description: Webhook を操作します
  name: KUFU Webhook API
  slug: kufu-webhook-api
artifact_total: 10
asyncapis:
- description: ''
  name: Kufu Smarthr Webhooks
  slug: kufu-smarthr-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SmartHR カスタム家族項目テンプレート API
  slug: open-kufu-default-api
- collection_type: open
  name: SmartHR カスタム家族項目テンプレート Webhook API
  slug: open-kufu-webhook-api
common:
- group: company
  title: ''
  type: Website
  url: https://smarthr.co.jp
- group: start
  title: ''
  type: Portal
  url: https://smarthr.jp
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.smarthr.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.smarthr.jp/api
- group: docs
  title: ''
  type: APIReference
  url: https://developer.smarthr.jp/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.smarthr.jp/api/about_api
- group: operate
  title: ''
  type: Support
  url: https://support.smarthr.jp/ja/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.smarthr.jp/ja/
- group: company
  title: ''
  type: Blog
  url: https://tech.smarthr.jp/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kufu
- group: commercial
  title: ''
  type: Pricing
  url: https://smarthr.jp/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.smarthr.jp/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smarthr.jp/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smarthr.co.jp/privacy/
- group: other
  title: ''
  type: DesignSystem
  url: https://smarthr.design/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/kufu-smarthr-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/kufu-smarthr-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kufu-smarthr-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/kufu-packages.yml
- group: design
  title: ''
  type: Components
  url: components/kufu-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kufu-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/kufu-security.txt
- group: auth
  title: ''
  type: Security
  url: security/kufu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kufu-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kufu-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/kufu-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kufu-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kufu-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kufu-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kufu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kufu-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kufu-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kufu-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kufu-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kufu-changelog.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/kufu-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kufu-llms.txt
created: '2026-07-17'
description: KUFU, Inc. is the founding name of SmartHR, Inc., the Japanese cloud HR platform, and remains the company's GitHub organization identity. SmartHR is a system of record for employee data across Japanese back-office HR — hiring and onboarding, social insurance and labour paperwork, family and dependent records, organizational structure, payslips, and withholding tax slips. The SmartHR API is a tenant-scoped REST API on a per-customer subdomain, described by a live Swagger 2.0 document covering 60 paths and 120 operations, and is offered free to existing SmartHR customers. It ships a webhook event surface, an application-gated sandbox on a separate domain, and an open-source React component library, but no official client SDK.
image: https://smarthr.jp/_astro/ogp_a-1.BA0NIxgO.jpg
layout: provider
modified: '2026-07-19'
name: KUFU
nav: Providers
network: true
overview: 'KUFU publishes 2 APIs on the [APIs.io](https://apis.io/) network: カスタム家族項目テンプレート API and Webhook API. Tagged areas include Company, Human Resources, HR Tech, Payroll, and Employee Data.


  The KUFU catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KUFU''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
random_paper: 2
score:
  band: strong
  composite: 57.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 55.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 57.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 62.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kufu/refs/heads/main/screenshots/kufu-2026-07-25T224324.png
security:
- kind: authentication
  name: Kufu Authentication
  slug: kufu-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kufu Domain Security
  slug: kufu-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kufu Vulnerability Disclosure
  slug: kufu-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Kufu Trust Center
  slug: kufu-trust-center
  summary_line: ISO/IEC 27001, SOC 2
slug: kufu
tags:
- Company
- Human Resources
- HR Tech
- Payroll
- Employee Data
- Software-as-a-Service
- Japan
- Onboarding
- Social Insurance
- Webhook
website: https://smarthr.co.jp
---
