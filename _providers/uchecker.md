---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.1
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: Вход, регистрация, управление JWT-токенами и API ключами, привязка Telegram
  name: uChecker Аутентификация API
  slug: uchecker-default-api
- description: Проверка email-адресов, управление задачами валидации, получение и скачивание результатов
  name: uChecker Валидация Email API
  slug: uchecker-email-api
- description: 'Программный интерфейс для ESP-провайдеров: расчёт стоимости и автоматическое создание аккаунтов с зачислением кредитов'
  name: uChecker ESP Провайдеры API
  slug: uchecker-esp-api
artifact_total: 10
asyncapis:
- description: ''
  name: Uchecker Webhooks
  slug: uchecker-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uchecker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uchecker-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://api.uchecker.net/mcp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uchecker-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/uchecker-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uchecker-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/uchecker-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/uchecker-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uchecker-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uchecker-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uchecker-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uchecker-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uchecker-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uchecker-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uchecker-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/uchecker-packages.yml
- group: start
  title: ''
  type: Console
  url: https://api.uchecker.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.uchecker.net/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.uchecker.net/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://uchecker.net/en#tariffs
- group: start
  title: ''
  type: SignUp
  url: https://app.uchecker.net
- group: operate
  title: ''
  type: Support
  url: https://t.me/goodsam911
- group: company
  title: ''
  type: Blog
  url: https://uchecker.net/blog-en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uchecker.net/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uchecker.net/privacy-policy
created: '2026-08-16'
description: Russian-language email-validation platform offering bulk and single email verification (SMTP mailbox existence, MX/DNS, catch-all, disposable, role-based, spam-trap/blacklist checks) plus free DNS/email tools. Access via REST API, a hosted MCP server, web dashboard, and Telegram bot.
image: https://uchecker.net/images/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: uChecker MCP Server
  slug: uchecker-mcp-server
- description: 'First-party hosted MCP server for uChecker email validation. Streamable HTTP transport, authenticated with the same uChecker API key used by the REST API (x-api-key header, or Authorization: Bearer <k'
  name: uChecker MCP Server
  slug: uchecker-mcp-server-2
modified: '2026-08-16'
name: uChecker
nav: Providers
network: true
overview: 'uChecker publishes 3 APIs on the [APIs.io](https://apis.io/) network: Аутентификация API, Валидация Email API, and ESP Провайдеры API. Tagged areas include Email Verification, Email, SMTP, DNS, and Deliverability.


  The uChecker catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  uChecker''s developer surface includes authentication, developer console, API reference, documentation, pricing, signup flow, support, and 19 more developer resources.'
plans:
- name: Uchecker Plans Pricing
  plan_count: 11
  slug: uchecker-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Uchecker Rate Limits
  slug: uchecker-rate-limits
score:
  band: developing
  composite: 48.4
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 16.7
    contract_quality: 62.6
    developer_ergonomics: 44.6
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 7.9
  previous_composite: 48.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uchecker/refs/heads/main/screenshots/uchecker-2026-08-17T082530.png
security:
- kind: authentication
  name: Uchecker Authentication
  slug: uchecker-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Uchecker Domain Security
  slug: uchecker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uchecker
tags:
- Email Verification
- Email
- SMTP
- DNS
- Deliverability
- mx
- SPF
- DKIM
- DMARC
- MCP
- agent-native
- Data Quality
---
