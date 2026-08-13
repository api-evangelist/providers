---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Persona Agentic Access
  operation_count: 28
  slug: persona-agentic-access
  summary_line: 28 operations · 18 acting
api_count: 7
apis:
- description: Manage end-user account records that group identity data and inquiries.
  name: Persona Accounts API
  slug: persona-accounts-api
- description: Create, manage, and review identity verification inquiries.
  name: Persona Inquiries API
  slug: persona-inquiries-api
- description: Manage allowlists, blocklists, and other reference lists.
  name: Persona Lists API
  slug: persona-lists-api
- description: Run database-driven reports such as watchlist or adverse media checks.
  name: Persona Reports API
  slug: persona-reports-api
- description: Track monitored transactions tied to an account.
  name: Persona Transactions API
  slug: persona-transactions-api
- description: Retrieve and manage individual verification checks within an inquiry.
  name: Persona Verifications API
  slug: persona-verifications-api
- description: Manage webhook subscriptions for asynchronous event delivery.
  name: Persona Webhooks API
  slug: persona-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: Persona Webhooks
  slug: open-persona-asyncapi
- collection_type: open
  name: Persona API
  slug: open-persona
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/persona-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/persona-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/persona-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/persona-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/persona-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withpersona
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/persona-identities
- group: start
  title: ''
  type: Portal
  url: https://withpersona.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withpersona.com/
- group: start
  title: ''
  type: Signup
  url: https://withpersona.com/dashboard/sign-up
- group: start
  title: ''
  type: Login
  url: https://withpersona.com/dashboard/login
- group: commercial
  title: ''
  type: Pricing
  url: https://withpersona.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withpersona.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withpersona.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withpersona.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.withpersona.com/docs/support
- group: company
  title: ''
  type: Blog
  url: https://withpersona.com/blog
- group: company
  title: ''
  type: Website
  url: https://withpersona.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.withpersona.com/llms.txt
created: '2026-03-16'
description: Persona provides identity verification and fraud prevention APIs. Their platform allows businesses to verify the identity of their users through document verification, selfie checks, database verifications, and more.
finops:
- name: Persona Finops
  service_category: API
  slug: persona-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/persona.png
layout: provider
modified: '2026-05-30'
name: Persona
nav: Providers
network: true
overview: 'Persona publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Inquiries API, Lists API, and 4 more. Tagged areas include Fraud Prevention, Identity Verification, and KYC.


  Persona''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, support, engineering blog, and 12 more developer resources.'
plans:
- name: Persona Plans Pricing
  plan_count: 3
  slug: persona-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Persona Rate Limits
  slug: persona-rate-limits
score:
  band: developing
  composite: 45.5
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 55.4
    developer_ergonomics: 34.8
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 87.5
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/persona/refs/heads/main/screenshots/persona-2026-06-20T191619.png
security:
- kind: authentication
  name: Persona Authentication
  slug: persona-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Persona Domain Security
  slug: persona-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Persona Vulnerability Disclosure
  slug: persona-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Persona Trust Center
  slug: persona-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: persona
tags:
- Fraud Prevention
- Identity Verification
- KYC
website: https://withpersona.com/
---
