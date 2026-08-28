---
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The Satispay GBusiness API is the merchant-facing payments API. It creates and updates payments across the MATCH_CODE, MATCH_USER, REFUND, PRE_AUTHORIZED, FUND_LOCK, PRE_AUTHORIZED_FUND_LOCK and HOTP_
  name: Satispay GBusiness API
  slug: satispay-gbusiness-api
- description: The production-environment definition Satispay publishes alongside the payments API, covering consumer lookup, daily closure retrieval, shop profile, pre-authorized payment tokens, MQTT certificates f
  name: Satispay GBusiness API (production surface)
  slug: satispay-gbusiness-production
- description: 'The staging/sandbox definition Satispay publishes for verifying an RSA-signed request before going live. It exposes the authentication test endpoint used to confirm the Digest, Message, Signature and '
  name: Satispay GBusiness API (sandbox)
  slug: satispay-gbusiness-sandbox
artifact_total: 10
asyncapis:
- description: ''
  name: Satispay Webhooks
  slug: satispay-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/satispay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/satispay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/satispay-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.satispay.com/it-it/business
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.satispay.com/docs/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://developers.satispay.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developers.satispay.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.satispay.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.satispay.com/en/business
- group: company
  title: ''
  type: Blog
  url: https://www.satispay.com/it-it/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/satispay
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.satispay.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.satispay.com/it-it/business/costi/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.satispay.com/it-it/legal-hub/condizioni-generali/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.satispay.com/it-it/legal-hub/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.satispay.com/changelog
- group: build
  title: ''
  type: Packages
  url: packages/satispay-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/satispay-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/satispay-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/satispay-security.txt
- group: auth
  title: ''
  type: Security
  url: security/satispay-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/satispay-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/satispay-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/satispay-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/satispay-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/satispay-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/satispay-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/satispay-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/satispay-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/satispay-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/satispay-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/satispay-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/satispay-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/satispay-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/satispay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/satispay-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/satispay-gbusiness-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/satispay-production-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/satispay-sandbox-overlay.yaml
created: '2026-08-26'
description: Satispay is an Italian mobile payment network and e-money institution, founded in 2013 and headquartered in Milan, that lets consumers pay merchants directly from a bank account without card rails. For developers it publishes the Satispay GBusiness API — an HTTPS/JSON payments API served from authservices.satispay.com with a staging twin at staging.authservices.satispay.com — covering one-off payments (QR match-code, phone match-user, HOTP), automatic/pre-authorized recurring payments, funds lock, refunds, consumer lookup, shop profile, MQTT certificates for in-store devices, checkout sessions, daily closures and transaction reports. Authentication is RSA request signing following the "Signing HTTP Messages" (Cavage) draft rather than OAuth, POSTs accept an Idempotency-Key header, and payment status changes are delivered to a merchant callback_url. Satispay also ships first-party e-commerce plugins (Shopify, Shopware, WooCommerce, PrestaShop, Magento 2), a PHP SDK, and in-store
  Java and Swift SDKs.
image: https://www.satispay.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Satispay MCP Server
  slug: satispay-mcp-server
modified: '2026-08-26'
name: Satispay
nav: Providers
network: true
overview: 'Satispay publishes 3 APIs on the [APIs.io](https://apis.io/) network: GBusiness API, GBusiness API (production surface), and GBusiness API (sandbox). Tagged areas include Payments, Mobile Payments, Fintech, E-Money, and E-Commerce.


  The Satispay catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Satispay''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 33 more developer resources.'
plans:
- name: Satispay Plans Pricing
  plan_count: 2
  slug: satispay-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Satispay Rate Limits
  slug: satispay-rate-limits
score:
  band: strong
  composite: 54.6
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 57.8
    developer_ergonomics: 54.2
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 57.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Satispay Authentication
  slug: satispay-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Satispay Domain Security
  slug: satispay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Satispay Vulnerability Disclosure
  slug: satispay-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: satispay
tags:
- Payments
- Mobile Payments
- Fintech
- E-Money
- E-Commerce
- Italy
- Europe
- Merchant Services
- Recurring Payments
- Refunds
- Meal Vouchers
- Company
website: https://www.satispay.com/it-it/business
---
