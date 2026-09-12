---
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
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: 'The AdvicePay REST API (v1.0.1) exposes the fee-for-service billing platform to integrators: admins, advisors, agreements, clients, custom attributes, deliverables, engagements, invoices, notification'
  name: AdvicePay API
  slug: advicepay-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/advicepay-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advicepay-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/advicepay-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://advicepay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.advicepay.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.advicepay.com/#introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.advicepay.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.advicepay.com/#introduction
- group: operate
  title: ''
  type: Support
  url: https://advicepay.com/contact-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://advicepay.helpscoutdocs.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.advicepay.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://advicepay.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.advicepay.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.advicepay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://advicepay.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://advicepay.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.advicepay.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://advicepay.com/changelog
- group: auth
  title: ''
  type: Security
  url: https://advicepay.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://advicepay.com/security/
- group: commercial
  title: ''
  type: Plans
  url: plans/advicepay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/advicepay-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/advicepay-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/advicepay-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/advicepay-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/advicepay-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/advicepay-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/advicepay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/advicepay-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/advicepay-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/advicepay-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/advicepay-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/advicepay-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/advicepay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advicepay-llms.txt
created: '2026-09-09'
description: AdvicePay is a fee-for-service billing, payment processing and engagement-management platform built for financial advisors, RIAs and broker-dealers. Founded by Michael Kitces and Alan Moore, it lets firms invoice clients for financial planning advice, collect card and ACH payments, run recurring subscriptions, capture eSignatures, track engagement workflows and deliverables, and enforce compliance oversight over advisor billing. AdvicePay publishes a public REST API (v1.0.1) at app.advicepay.com/api/public/v1 covering admins, advisors, agreements, clients, custom attributes, deliverables, engagements, invoices, notifications, offices, subscriptions and transfers, secured with OAuth 2.0 (authorization code and client credentials, with client_secret_post, client_secret_jwt and private_key_jwt authentication methods) plus SAML 2.0 single sign-on. API access is an Enterprise-plan capability.
image: https://advicepay.com/hubfs/AdvicePay%20Logos/PNG%20AdvicePay%20Logos%20(Email)/Website%20Favicon.png
layout: provider
modified: '2026-09-09'
name: AdvicePay
nav: Providers
network: true
overview: 'AdvicePay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Services, Payments, Billing, Invoicing, and Financial Planning.


  AdvicePay''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Advicepay Plans Pricing
  plan_count: 3
  slug: advicepay-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Advicepay Rate Limits
  slug: advicepay-rate-limits
scopes:
- name: Advicepay Scopes
  scope_count: 1
  slug: advicepay-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: developing
  composite: 53.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 53.6
    discoverability: 68.5
    operational_transparency: 71.1
  previous_composite: 53.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Advicepay Authentication
  slug: advicepay-authentication
  summary_line: oauth2/apiKey/saml2 · 3 schemes
- kind: domain-security
  name: Advicepay Domain Security
  slug: advicepay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Advicepay Vulnerability Disclosure
  slug: advicepay-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Advicepay Trust Center
  slug: advicepay-trust-center
  summary_line: SOC 2 Type II, PCI SAQ A
slug: advicepay
tags:
- Financial Services
- Payments
- Billing
- Invoicing
- Financial Planning
- Wealth Management
- Subscriptions
- eSignature
- Compliance
- FinTech
website: https://advicepay.com/
---
