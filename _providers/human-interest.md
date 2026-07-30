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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Partner GraphQL API for onboarding 401(k)/403(b) retirement plans, OpenID Connect single sign-on, and webhook event subscriptions.
  name: Human Interest GraphQL API
  slug: human-interest-graphql-api
artifact_total: 6
asyncapis:
- description: ''
  name: Human Interest Webhooks
  slug: human-interest-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://humaninterest.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.humaninterest.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.humaninterest.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://humaninterest.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://humaninterest.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.humaninterest.com
- group: operate
  title: ''
  type: Support
  url: https://humaninterest.com/support
- group: company
  title: ''
  type: Blog
  url: https://humaninterest.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://humaninterest.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://humaninterest.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/human-interest-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/human-interest-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/human-interest-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.humaninterest.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/human-interest-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/human-interest-webhooks.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/human-interest-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/human-interest-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/human-interest-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/human-interest-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/human-interest-llms.txt
created: '2026-07-17'
description: Human Interest is a fintech company providing affordable, full-service 401(k), 403(b), and IRA retirement plans built for small and medium-sized businesses. Founded to close the retirement savings gap, it combines automated plan administration, 600+ payroll integrations, and low-cost index-fund investing. For platforms and partners it publishes a GraphQL API (https://api.humaninterest.com/v1/graphql) that lets them onboard retirement plans end to end, integrate OpenID Connect single sign-on, and subscribe to webhook events, all documented at docs.humaninterest.com. Human Interest maintains a SafeBase trust center with SOC 1, SOC 2 Type 1 & 2, GLBA, and CCPA attestations plus a responsible-disclosure program.
image: https://cdn.builder.io/api/v1/image/assets%2Fe2719c23b0574124be5a7ea31e5b5e3b%2Fc050d2c9eb53497bb95bab1b377daf4a
layout: provider
modified: '2026-07-19'
name: Human Interest
nav: Providers
network: true
overview: 'Human Interest publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Retirement, 401(k), and Employee Benefits.


  The Human Interest catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Human Interest''s developer surface includes documentation, pricing, signup flow, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 66
score:
  band: developing
  composite: 43.4
  delta: 7.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 34.8
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 18.4
  previous_composite: 36.4
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/human-interest/refs/heads/main/screenshots/human-interest-2026-07-25T221647.png
security:
- kind: authentication
  name: Human Interest Authentication
  slug: human-interest-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Human Interest Domain Security
  slug: human-interest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Human Interest Vulnerability Disclosure
  slug: human-interest-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Human Interest Trust Center
  slug: human-interest-trust-center
  summary_line: SOC 1, SOC 2 Type 1, SOC 2 Type 2
slug: human-interest
tags:
- Company
- Fintech
- Retirement
- 401(k)
- Employee Benefits
- Payroll
- GraphQL
- API
website: https://humaninterest.com
---
