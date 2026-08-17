---
access_model:
  confidence: medium
  label: Enterprise, contact sales
  onboarding: approval
  pricing: enterprise
  public: false
  source:
  - https://www.validity.com/pricing/
  - https://developer.everest.validity.com/
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'The Everest API by Validity — the Return Path platform''s surviving programmable surface. Two live major versions behind one host: /api/2.0 is current and covers inbox placement testing and seed lists,'
  name: Everest API
  slug: everest-api
artifact_total: 8
asyncapis:
- description: ''
  name: Return Path Webhooks
  slug: return-path-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.returnpath.com/
- group: other
  title: ''
  type: Product
  url: https://www.validity.com/capabilities/engage-inbox-placement-and-deliverability/
- group: company
  title: ''
  type: Blog
  url: https://www.validity.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://knowledge.validity.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://knowledge.validity.com/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://mycommunity.validity.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.validity.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.validity.com/legal/terms-of-service/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.everest.validity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.everest.validity.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.everest.validity.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/two50okay/workspace/everest-by-validity-s-public-workspace/overview
- group: start
  title: ''
  type: Login
  url: https://everest.validity.com/login
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.validity.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.validity.com/
- group: auth
  title: ''
  type: Security
  url: https://trust.validity.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/return-path-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/return-path-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/return-path-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/return-path-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/return-path-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/return-path-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/return-path-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/return-path-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/return-path-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/return-path-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/return-path-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/return-path-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/return-path-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/return-path-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/return-path-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/return-path-llms.txt
created: '2026-07-17'
description: Return Path is an email-deliverability and inbox-intelligence brand that pioneered sender reputation, inbox-placement monitoring, and email fraud protection for marketers and email senders. Founded in 1999 and backed by Sapphire Ventures and Union Square Ventures, Return Path was acquired by Validity in 2019 and now ships as the Validity Everest email-success platform; returnpath.com 301-redirects to validity.com. The platform draws on signals from billions of global mailboxes to measure inbox placement, sender reputation, and deliverability across major mailbox providers. The Return Path product line's surviving API surface is the Everest API at api.everest.validity.com — 170 published operations across inbox placement, sender reputation and Sender Score, blocklist and spam-trap monitoring, DMARC infrastructure reporting, engagement analytics, list validation and certification. Validity publishes no OpenAPI, but it does publish a complete public Postman collection at developer.everest.validity.com,
  which is the machine-readable contract this profile is built from.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/return-path.png
layout: provider
modified: '2026-08-13'
name: Return Path
nav: Providers
network: true
overview: 'Return Path publishes 1 API on the [APIs.io](https://apis.io/) network: Everest API. Tagged areas include Company, Martech, Email, Email Deliverability, and Email Marketing.


  The Return Path catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Return Path''s developer surface includes engineering blog, support, documentation, API reference, authentication, and 28 more developer resources.'
plans:
- name: Return Path Plans Pricing
  plan_count: 0
  slug: return-path-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 1
  name: Return Path Rate Limits
  slug: return-path-rate-limits
score:
  band: developing
  composite: 52.2
  delta: 39.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.1
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 12.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Return Path Authentication
  slug: return-path-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Return Path Domain Security
  slug: return-path-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Return Path Vulnerability Disclosure
  slug: return-path-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Return Path Trust Center
  slug: return-path-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27701, GDPR, CCPA, EU-US Data Privacy Framework, Microsoft SSPA, Standard Contractual Clauses
slug: return-path
tags:
- Company
- Martech
- Email
- Email Deliverability
- Email Marketing
- Sender Reputation
- Inbox Placement
- Deliverability
- DMARC
- Email Authentication
- Email Validation
- Analytics
website: https://www.returnpath.com/
---
