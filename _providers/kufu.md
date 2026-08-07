---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: カスタム家族項目テンプレートを操作します
  name: KUFU カスタム家族項目テンプレート API
  slug: kufu-default-api
- description: Webhook を操作します
  name: KUFU Webhook API
  slug: kufu-webhook-api
artifact_total: 8
asyncapis:
- description: ''
  name: Kufu Smarthr Webhooks
  slug: kufu-smarthr-webhooks
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
  url: openapi/kufu-smarthr-openapi.json
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: kufu-mcp.yml
  slug: kufu-mcpyml
modified: '2026-07-19'
name: KUFU
nav: Providers
network: true
overview: 'KUFU publishes 2 APIs on the [APIs.io](https://apis.io/) network: カスタム家族項目テンプレート API and Webhook API. Tagged areas include Company, Human Resources, HR Tech, Payroll, and Employee Data.


  The KUFU catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  KUFU''s developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
random_paper: 104
score:
  band: developing
  composite: 53.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 55.0
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 53.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
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
- SaaS
- Japan
- Onboarding
- Social Insurance
- Webhooks
website: https://smarthr.co.jp
---
