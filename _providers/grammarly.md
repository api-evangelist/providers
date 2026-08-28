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
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: Programmatic access to Grammarly usage and communication-performance analytics for integration into business-intelligence systems.
  name: Grammarly Analytics API
  slug: grammarly-analytics-api
- description: Allocate and reallocate Grammarly licenses from software asset management / IT-governance tooling.
  name: Grammarly License Management API
  slug: grammarly-license-management-api
- description: Score content on correctness, engagement, clarity, and delivery for organizational content governance (Beta).
  name: Grammarly Writing Score API
  slug: grammarly-writing-score-api
- description: Detect AI-generated content and help demonstrate original authorship (Beta).
  name: Grammarly AI Detection API
  slug: grammarly-ai-detection-api
- description: Detect plagiarism against published sources to help teams produce original work (Beta).
  name: Grammarly Plagiarism Detection API
  slug: grammarly-plagiarism-detection-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.grammarly.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.grammarly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.grammarly.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.grammarly.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.grammarly.com/your-first-api-request.html
- group: operate
  title: ''
  type: Support
  url: https://support.grammarly.com/
- group: company
  title: ''
  type: Blog
  url: https://www.grammarly.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grammarly
- group: commercial
  title: ''
  type: Pricing
  url: https://www.grammarly.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://www.grammarly.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.grammarly.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.grammarly.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.grammarly.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/grammarly-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.grammarly.com/security
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/grammarly
- group: auth
  title: ''
  type: Authentication
  url: authentication/grammarly-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/grammarly-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/grammarly-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/grammarly-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/grammarly-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/grammarly-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/grammarly-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/grammarly-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/grammarly-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/grammarly-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/grammarly-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grammarly-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/grammarly-vulnerability-disclosure.yml
created: '2026-07-17'
description: Grammarly is an AI writing-assistance company whose enterprise developer platform exposes a set of REST APIs that bring Grammarly's writing intelligence into an organization's own applications, business-intelligence systems, and IT tooling. The Grammarly APIs cover writing-quality scoring, AI generated-content detection, plagiarism detection, communication analytics, and license management, all secured with OAuth 2.0 client credentials and scoped permissions against the base URL https://api.grammarly.com/ecosystem/api/. Certified Readability Score and Tone Analysis APIs are announced as coming soon. Grammarly was surfaced as a portfolio company of IVP.
image: https://www.grammarly.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Grammarly
nav: Providers
network: true
overview: 'Grammarly publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Writing Assistance, Productivity, and Natural Language Processing.


  Grammarly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 6
scopes:
- name: Grammarly Scopes
  scope_count: 5
  slug: grammarly-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 39.1
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grammarly/refs/heads/main/screenshots/grammarly-2026-07-25T220215.png
security:
- kind: authentication
  name: Grammarly Authentication
  slug: grammarly-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Grammarly Domain Security
  slug: grammarly-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Grammarly Vulnerability Disclosure
  slug: grammarly-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Grammarly Trust Center
  slug: grammarly-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: grammarly
tags:
- Company
- Artificial Intelligence
- Writing Assistance
- Productivity
- Natural Language Processing
- Analytics
- Content
- Authentication
- Enterprise
website: https://www.grammarly.com
---
