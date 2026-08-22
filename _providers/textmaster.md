---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.2
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: OpenAPI 3.0.3-described REST API for ordering and managing translation, proofreading and copywriting work. 54 operations across Projects (create, quote, finalize, launch sync/async, pause, resume, can
  name: TextMaster API v1
  slug: textmaster-api-v1
artifact_total: 9
asyncapis:
- description: ''
  name: Textmaster Event Surface
  slug: textmaster-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://www.textmaster.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.textmaster.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.textmaster.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.textmaster.com/reference/abilities
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.textmaster.com/quick-start
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.textmaster.com/client
- group: operate
  title: ''
  type: Support
  url: mailto:support@textmaster.com
- group: start
  title: ''
  type: SignUp
  url: https://app.textmaster.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://app.textmaster.com/sign_in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/textmaster
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acolad.com/en/legal-notices/website-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.textmaster.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/textmaster-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/textmaster/bugbounty/blob/main/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/textmaster-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/textmaster-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.textmaster.com/client/policies/subprocessors
- group: design
  title: ''
  type: Conformance
  url: conformance/textmaster-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/textmaster-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/textmaster-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/textmaster-llms.txt
- group: other
  title: ''
  type: ContentSignal
  url: https://developer.textmaster.com/robots.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/textmaster-plans-pricing.yml
created: '2026-08-17'
description: TextMaster is a French professional translation, proofreading and copywriting platform that sells human-and-machine language work as an API-first service in 50+ languages. Clients create Projects, attach Documents (plain text or file URLs), request a quotation, launch against a prepaid credit wallet, and receive finished content back through status-change webhooks. The platform exposes a documented OpenAPI 3.0.3 REST API at api.textmaster.com covering projects, documents, glossaries, expertises, preferred authors, work/API templates, transactions, invoices and receipts, secured by OAuth 2.0 authorization-code apps with 22 granular scopes plus a legacy signature strategy. It ships first-party Akeneo, Magento 2, Salesforce Commerce Cloud and Hybris connectors and a PHP API client. TextMaster is now part of Acolad Group; the marketing site is a transition landing page pointing at Acolad's Lia platform, while the application, the API and the developer portal remain live and in service.
image: https://www.textmaster.com/assets/textmaster-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: textmaster-mcp.yml
  slug: textmaster-mcpyml
modified: '2026-08-17'
name: TextMaster
nav: Providers
network: true
overview: 'TextMaster publishes 1 API on the [APIs.io](https://apis.io/) network: API v1. Tagged areas include Company, Translation, Localization, Language Services, and Copywriting.


  The TextMaster catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TextMaster''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, and 19 more developer resources.'
plans:
- name: Textmaster Plans Pricing
  plan_count: 0
  slug: textmaster-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Textmaster Rate Limits
  slug: textmaster-rate-limits
scopes:
- name: Textmaster Scopes
  scope_count: 22
  slug: textmaster-scopes
  summary_line: 22 scopes · authorizationCode
score:
  band: developing
  composite: 41.8
  facets:
    access_clarity: 25.0
    commercial_clarity: 25.0
    contract_governance: 30.3
    contract_quality: 53.8
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 13.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
security:
- kind: authentication
  name: Textmaster Authentication
  slug: textmaster-authentication
  summary_line: oauth2/custom-signature · 2 schemes
- kind: domain-security
  name: Textmaster Domain Security
  slug: textmaster-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Textmaster Vulnerability Disclosure
  slug: textmaster-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: textmaster
tags:
- Company
- Translation
- Localization
- Language Services
- Copywriting
- Proofreading
- Machine Translation
- Content Production
- Translation Memory
- Glossary
- Ecommerce Localization
- Product Information Management
- Webhooks
- OAuth2
- SaaS
website: https://www.textmaster.com/
---
