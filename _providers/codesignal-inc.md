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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'CodeSignal''s primary programmatic surface: a GraphQL API for reading assessments and company test sessions and running mutations, authenticated with a Bearer API key. Read operations live under RootQu'
  name: CodeSignal GraphQL API
  slug: codesignal-graphql-api
artifact_total: 6
asyncapis:
- description: ''
  name: Codesignal Inc Webhooks
  slug: codesignal-inc-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://codesignal.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.codesignal.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.codesignal.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.codesignal.com/graphql
- group: commercial
  title: ''
  type: Pricing
  url: https://codesignal.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://identity.codesignal.com/auth/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://codesignal.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://codesignal.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://codesignal.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.codesignal.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codesignal.com/
- group: auth
  title: ''
  type: Compliance
  url: https://codesignal.com/compliance-trust/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.codesignal.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/codesignal-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codesignal-inc-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codesignal-inc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codesignal-inc-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/codesignal-inc-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/codesignal-inc-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/codesignal-inc-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codesignal-inc-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codesignal-inc-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codesignal-inc-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://codesignal.com/security/disclosure-policy
created: '2026-07-17'
description: CodeSignal is a technical skills assessment and interview platform used by employers to evaluate, hire, and develop engineering talent through skills assessments, an AI Interviewer, live technical interviews, and skills development and intelligence products. For programmatic integration CodeSignal publishes a developer surface at developer.codesignal.com built around a GraphQL API (https://app.codesignal.com/graphql) authenticated with a Bearer API key, a Webhook API that delivers HMAC-SHA256-signed JSON event notifications for assessments, test sessions, and live interviews, and a Learn API. The platform integrates with major ATS, LMS, HCM, and SSO/identity providers and maintains SOC 2 Type II and ISO 27001 compliance.
image: https://codesignal.com/wp-content/uploads/2023/01/codesignal-logo.png
layout: provider
modified: '2026-07-18'
name: CodeSignal, Inc.
nav: Providers
network: true
overview: 'CodeSignal, Inc. publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Business Applications, Technical Assessment, Developer Hiring, and Skills Assessment.


  The CodeSignal, Inc. catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CodeSignal, Inc.''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, support, authentication, and 17 more developer resources.'
random_paper: 65
score:
  band: developing
  composite: 47.9
  delta: 8.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 41.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 34.2
  previous_composite: 39.7
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/codesignal-inc/refs/heads/main/screenshots/codesignal-inc-2026-07-25T205939.png
security:
- kind: authentication
  name: Codesignal Inc Authentication
  slug: codesignal-inc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Codesignal Inc Domain Security
  slug: codesignal-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Codesignal Inc Vulnerability Disclosure
  slug: codesignal-inc-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Codesignal Inc Trust Center
  slug: codesignal-inc-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: codesignal-inc
tags:
- Company
- Business Applications
- Technical Assessment
- Developer Hiring
- Skills Assessment
- Technical Interviews
- GraphQL
- Webhooks
- Talent
website: https://codesignal.com/
---
