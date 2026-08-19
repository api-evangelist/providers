---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Qr Code Crafter Agentic Access
  operation_count: 19
  slug: qr-code-crafter-agentic-access
  summary_line: 19 operations · 13 acting
api_count: 1
apis:
- description: REST API for generating static and bulk QR codes and managing dynamic URL redirects/vaults with aggregate analytics. Includes an OpenAPI 3.0.1 contract, WebMCP browser-agent context, ai-plugin.json, l
  name: QRCodeCrafter API
  slug: qrcodecrafter-api
artifact_total: 7
collections:
- collection_type: open
  name: QRCodeCrafter API
  slug: open-qr-code-crafter-openapi-original
common:
- group: company
  title: ''
  type: Website
  url: https://qrcodecrafter.com
- group: docs
  title: ''
  type: Documentation
  url: https://qrcodecrafter.com/qr-code-api
- group: docs
  title: ''
  type: APIReference
  url: https://qrcodecrafter.com/openapi.yaml
- group: commercial
  title: ''
  type: Pricing
  url: https://qrcodecrafter.com/qr-code-api-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qrcodecrafter.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qrcodecrafter.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@qrcodecrafter.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://qrcodecrafter.com/faq
- group: agent
  title: ''
  type: LLMsTxt
  url: https://qrcodecrafter.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qr-code-crafter-llms.txt
- group: agent
  title: ''
  type: WebMCP
  url: mcp/qr-code-crafter-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qr-code-crafter-agentic-access.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qr-code-crafter-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qr-code-crafter-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qr-code-crafter-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/qr-code-crafter-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qr-code-crafter-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qr-code-crafter-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qr-code-crafter-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qr-code-crafter-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qr-code-crafter-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://qrcodecrafter.com/feeds/agent-updates.xml
- group: design
  title: ''
  type: Conformance
  url: conformance/qr-code-crafter-conformance.yml
- group: build
  title: ''
  type: Examples
  url: examples/qr-code-crafter-agent-recipes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/qr-code-crafter-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/qr-code-crafter-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qr-code-crafter-domain-security.yml
- group: other
  title: ''
  type: APIsJSON
  url: https://qrcodecrafter.com/apis.json
created: '2026-07-24'
description: 'Public QR code generation API by Brand Aspect Ltd (England & Wales, company 05105266) supporting 27 payload types — URL, GS1 Digital Link, Wi-Fi, vCard, event, location, crypto and fifteen payment schemes including PIX, UPI, PromptPay, VietQR, Swiss QR-bill and SEPA/GiroCode — exported as SVG, PNG, JPG, WebP, PDF or EPS at up to 4096px. Adds bounded bulk ZIP generation (50 rows with a manifest), a generate-and-verify endpoint that decodes the finished asset and returns an evidence receipt, and capability-managed dynamic URL redirects and vaults with privacy-preserving aggregate counts and no accounts or visitor tracking. Unusually agent-native for its size: it self-publishes an APIs.json index, OpenAPI 3.0.1 in both JSON and YAML, an ai-plugin manifest, a WebMCP browser-agent context with eight tool schemas, llms.txt, ai.txt, an Atom change feed for agents, and Markdown variants of every public page.'
image: https://qrcodecrafter.com/icons/icon-512x512.png
layout: provider
modified: '2026-08-11'
name: QR Code Crafter
nav: Providers
network: true
overview: 'QR Code Crafter publishes 1 API on the [APIs.io](https://apis.io/) network: QRCodeCrafter API. Tagged areas include QR code, QR code generation, static QR, dynamic QR, and dynamic redirects.


  QR Code Crafter''s developer surface includes documentation, API reference, pricing, support, authentication, changelog, code examples, and 22 more developer resources.'
plans:
- name: Qr Code Crafter Plans Pricing
  plan_count: 1
  slug: qr-code-crafter-plans-pricing
random_paper: 130
rate_limits:
- limit_count: 4
  name: Qr Code Crafter Rate Limits
  slug: qr-code-crafter-rate-limits
score:
  band: developing
  composite: 45.7
  delta: 2.2
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 43.7
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 47.4
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qr-code-crafter/refs/heads/main/screenshots/qr-code-crafter-2026-08-17T081420.png
security:
- kind: authentication
  name: Qr Code Crafter Authentication
  slug: qr-code-crafter-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Qr Code Crafter Domain Security
  slug: qr-code-crafter-domain-security
  summary_line: TLSv1.3 · HSTS
slug: qr-code-crafter
tags:
- QR code
- QR code generation
- static QR
- dynamic QR
- dynamic redirects
- image export
- bulk generation
- developer tools
- OpenAPI
- WebMCP
- browser agents
- payments (QR)
- agent readiness
- llms.txt
- capability tokens
website: https://qrcodecrafter.com
---
