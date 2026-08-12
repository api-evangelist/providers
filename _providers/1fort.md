---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 241
  human_in_the_loop: 2
  name: 1Fort Agentic Access
  operation_count: 574
  slug: 1fort-agentic-access
  summary_line: 574 operations · 241 acting · 2 human-in-the-loop
api_count: 89
apis:
- description: '**Access:** requires a JWT access token.'
  name: 1Fort agent_runtime (v2) API
  slug: 1fort-agent-runtime-v2-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Analytics API
  slug: 1fort-analytics-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort application: applications API'
  slug: 1fort-application-applications-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort application: clients API'
  slug: 1fort-application-clients-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort application (v2): applications API'
  slug: 1fort-application-v2-applications-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort application (v2): coverages API'
  slug: 1fort-application-v2-coverages-api
- description: '**Deprecated.** Legacy Ascend billing/payments; use the Billing (v2) endpoints instead. **Access:** mixed; some endpoints are public, others require JWT or an API key (per endpoint).'
  name: 1Fort Ascend API
  slug: 1fort-ascend-api
- description: '**Deprecated.** Legacy Ascend billing/payments; use the Billing (v2) endpoints instead. **Access:** requires a JWT access token.'
  name: 1Fort ascend (v2) API
  slug: 1fort-ascend-v2-api
- description: Sign in / sign up via Google or Office365 OAuth and refresh JWT access tokens. **Access:** mixed; some endpoints are public, others require JWT (per endpoint).
  name: 1Fort Auth API
  slug: 1fort-auth-api
- description: One-time-password (OTP) authentication. **Access:** public; no authentication required.
  name: 1Fort Authentication API
  slug: 1fort-authentication-api
- description: Billing and payments. Replaces the deprecated Ascend payment endpoints. **Access:** requires a JWT access token.
  name: 1Fort billing (v2) API
  slug: 1fort-billing-v2-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker: ai-customization-types API'
  slug: 1fort-broker-ai-customization-types-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker: ai-customizations API'
  slug: 1fort-broker-ai-customizations-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Broker Ams Integration API
  slug: 1fort-broker-ams-integration-api
- description: '**Access:** mixed; some endpoints are public, others require JWT (per endpoint).'
  name: 1Fort Broker API
  slug: 1fort-broker-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker: clients API'
  slug: 1fort-broker-clients-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker: email_preferences API'
  slug: 1fort-broker-email-preferences-api
- description: '**Access:** public; no authentication required.'
  name: 1Fort Broker Google API
  slug: 1fort-broker-google-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Broker Groups API
  slug: 1fort-broker-groups-api
- description: '**Access:** public; no authentication required.'
  name: 1Fort Broker Office365 API
  slug: 1fort-broker-office365-api
- description: '**Access:** public; no authentication required.'
  name: 1Fort Broker Office365 Individual API
  slug: 1fort-broker-office365-individual-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker: proposal-preferences API'
  slug: 1fort-broker-proposal-preferences-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Broker Settings API
  slug: 1fort-broker-settings-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker: take-rates API'
  slug: 1fort-broker-take-rates-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker: user-ai-customizations API'
  slug: 1fort-broker-user-ai-customizations-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker: users API'
  slug: 1fort-broker-users-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker (v2): applications API'
  slug: 1fort-broker-v2-applications-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker (v2): clients API'
  slug: 1fort-broker-v2-clients-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker (v2): coverages API'
  slug: 1fort-broker-v2-coverages-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker (v2): email-templates API'
  slug: 1fort-broker-v2-email-templates-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker (v2): quote-policies API'
  slug: 1fort-broker-v2-quote-policies-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker (v2): quotes API'
  slug: 1fort-broker-v2-quotes-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker (v2): storefront API'
  slug: 1fort-broker-v2-storefront-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort broker (v2): team-users API'
  slug: 1fort-broker-v2-team-users-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Business Admin API
  slug: 1fort-business-admin-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Business API
  slug: 1fort-business-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Business Broker Users API
  slug: 1fort-business-broker-users-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Business User API
  slug: 1fort-business-user-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Carrier API
  slug: 1fort-carrier-api
- description: Checkout and payment session endpoints. **Access:** public; no authentication required.
  name: 1Fort Checkout API
  slug: 1fort-checkout-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Email AI Agent API
  slug: 1fort-email-ai-agent-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Email AI Agent - Attachments API
  slug: 1fort-email-ai-agent-attachments-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Email AI Agent - Businesses API
  slug: 1fort-email-ai-agent-businesses-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Email AI Agent - Entities API
  slug: 1fort-email-ai-agent-entities-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Email AI Agent - Markets API
  slug: 1fort-email-ai-agent-markets-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Email AI Agent - Profiles API
  slug: 1fort-email-ai-agent-profiles-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Email AI Agent - Reference Data API
  slug: 1fort-email-ai-agent-reference-data-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Email AI API
  slug: 1fort-email-ai-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort email_ai (v2): attachments API'
  slug: 1fort-email-ai-v2-attachments-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort email_ai (v2): carriers API'
  slug: 1fort-email-ai-v2-carriers-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort email_ai (v2): coverage-types API'
  slug: 1fort-email-ai-v2-coverage-types-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort email_ai (v2): emails API'
  slug: 1fort-email-ai-v2-emails-api
- description: '**Access:** public; no authentication required.'
  name: '1Fort email_ai (v2): gmail API'
  slug: 1fort-email-ai-v2-gmail-api
- description: '**Access:** public; no authentication required.'
  name: '1Fort email_ai (v2): office365 API'
  slug: 1fort-email-ai-v2-office365-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort email_ai (v2): profiles API'
  slug: 1fort-email-ai-v2-profiles-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort email_ai (v2): wholesalers API'
  slug: 1fort-email-ai-v2-wholesalers-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort google_workspace (v2) API
  slug: 1fort-google-workspace-v2-api
- description: '**Access:** mixed; some endpoints are public, others require JWT or an API key (per endpoint).'
  name: 1Fort herald (v2) API
  slug: 1fort-herald-v2-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort indications (v2) API
  slug: 1fort-indications-v2-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort insurance (v2) API
  slug: 1fort-insurance-v2-api
- description: Invitations for broker and business users. **Access:** mixed; some endpoints are public, others require JWT (per endpoint).
  name: 1Fort Invite API
  slug: 1fort-invite-api
- description: Legal documents and agreements. **Access:** requires a JWT access token.
  name: 1Fort Legal API
  slug: 1fort-legal-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort market (v2) API
  slug: 1fort-market-v2-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Markets API
  slug: 1fort-markets-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Markets - Business API
  slug: 1fort-markets-business-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort office365 (v2) API
  slug: 1fort-office365-v2-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort premium_finance (v2) API
  slug: 1fort-premium-finance-v2-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort quote_ai (v2) API
  slug: 1fort-quote-ai-v2-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote: applications API'
  slug: 1fort-quote-applications-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote: clients API'
  slug: 1fort-quote-clients-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote: quotes API'
  slug: 1fort-quote-quotes-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote (v2): application API'
  slug: 1fort-quote-v2-application-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote (v2): binders API'
  slug: 1fort-quote-v2-binders-api
- description: '**Access:** public; no authentication required.'
  name: '1Fort quote (v2): checkout API'
  slug: 1fort-quote-v2-checkout-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote (v2): cios API'
  slug: 1fort-quote-v2-cios-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote (v2): coverages API'
  slug: 1fort-quote-v2-coverages-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote (v2): quote-policies API'
  slug: 1fort-quote-v2-quote-policies-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote (v2): quotes API'
  slug: 1fort-quote-v2-quotes-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort quote (v2): tasks API'
  slug: 1fort-quote-v2-tasks-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Reports API
  slug: 1fort-reports-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Reward API
  slug: 1fort-reward-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Risk Manager API
  slug: 1fort-risk-manager-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort Sanity Check AI API
  slug: 1fort-sanity-check-ai-api
- description: Insured-facing storefront endpoints. Access is scoped by storefront identity (public links, API key, or storefront permission) rather than a user JWT. **Access:** mixed; some endpoints are public, oth
  name: 1Fort storefront (v2) API
  slug: 1fort-storefront-v2-api
- description: '**Access:** mixed; some endpoints are public, others require JWT (per endpoint).'
  name: 1Fort Stripe API
  slug: 1fort-stripe-api
- description: '**Access:** requires a JWT access token or an API key.'
  name: 1Fort Suggestion AI API
  slug: 1fort-suggestion-ai-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort treasury (v2) API
  slug: 1fort-treasury-v2-api
- description: '**Access:** requires a JWT access token.'
  name: 1Fort User API
  slug: 1fort-user-api
- description: '**Access:** requires a JWT access token.'
  name: '1Fort user: default-access-role API'
  slug: 1fort-user-default-access-role-api
artifact_total: 97
asyncapis:
- description: ''
  name: 1Fort Webhooks
  slug: 1fort-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1fort-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/1fort-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1fort-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/1fort-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1fort-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1fort.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://api.1fort.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.1fort.com/api-docs
- group: operate
  title: ''
  type: Support
  url: https://help.1fort.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.1fort.com/en/
- group: company
  title: ''
  type: Blog
  url: https://1fort.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://1fort.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://1fort.ai/demo
- group: start
  title: ''
  type: Login
  url: https://app.1fort.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://1fort.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://1fort.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.1fort.com/
- group: auth
  title: ''
  type: Security
  url: https://1fort.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://security.1fort.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1fort-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1fort-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/1fort-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/1fort-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1fort-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/1fort-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1fort-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/1fort-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1fort-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1fort-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/1fort-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/1fort-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/1fort-webhooks.yml
- group: company
  title: ''
  type: Careers
  url: https://1fort.ai/careers
- group: company
  title: ''
  type: About
  url: https://1fort.ai/about
- group: company
  title: ''
  type: Partners
  url: https://1fort.ai/partners
created: '2026-08-05'
description: 1Fort is a New York City based insurtech platform that automates the commercial insurance workflow for brokers and agencies. Its AI "copilot" autofills submissions across 300+ coverages, quotes direct and wholesale markets, generates white-labeled proposals with side-by-side coverage comparisons and cross-sell recommendations, then processes binders, invoicing, premium finance, payments and payables through to ongoing policy servicing. Coverage lines span cyber, technology errors and omissions, professional liability, management liability, general liability and workers compensation. The platform runs on AWS, holds SOC 2 Type II, HIPAA and CCPA attestations, and exposes a large REST API at api.1fort.com whose Swagger 2.0 definition is published publicly at /api-docs — 574 operations across broker, application, quote, market, billing, checkout, storefront and Email AI Agent surfaces, plus inbound webhook receivers for Stripe, Ascend, Herald, Gmail and Office 365.
image: https://1fort.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: 1fort-mcp.yml
  slug: 1fort-mcpyml
modified: '2026-08-05'
name: 1Fort
nav: Providers
network: true
overview: '1Fort publishes 89 APIs on the [APIs.io](https://apis.io/) network, including agent_runtime (v2) API, Analytics API, application: applications API, and 86 more. Tagged areas include insurance, insurtech, commercial-insurance, cyber-insurance, and insurance-broker.


  The 1Fort catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  1Fort''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, authentication, and 29 more developer resources.'
random_paper: 28
rate_limits:
- limit_count: 4
  name: 1Fort Rate Limits
  slug: 1fort-rate-limits
score:
  band: developing
  composite: 51.1
  delta: -3.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.5
    developer_ergonomics: 36.4
    discoverability: 63.0
    governance: 20.8
    operational_transparency: 50.0
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 89
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/1fort/refs/heads/main/screenshots/1fort-2026-08-07T160647.png
security:
- kind: authentication
  name: 1Fort Authentication
  slug: 1fort-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 1Fort Domain Security
  slug: 1fort-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 1Fort Vulnerability Disclosure
  slug: 1fort-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: 1Fort Trust Center
  slug: 1fort-trust-center
  summary_line: SOC 2 Type II, HIPAA, CCPA
slug: 1fort
tags:
- insurance
- insurtech
- commercial-insurance
- cyber-insurance
- insurance-broker
- quoting
- policy-management
- premium-finance
- payments
- workflow-automation
- artificial-intelligence
- agentic-ai
website: https://1fort.ai/
---
