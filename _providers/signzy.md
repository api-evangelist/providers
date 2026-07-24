---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 76.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Signzy Agentic Access
  operation_count: 6
  slug: signzy-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 4
apis:
- description: The Authentication API from Signzy — 2 operation(s) for authentication.
  name: Signzy Authentication API
  slug: signzy-authentication-api
- description: The Banking API from Signzy — 1 operation(s) for banking.
  name: Signzy Banking API
  slug: signzy-banking-api
- description: The Identity (India) API from Signzy — 2 operation(s) for identity (india).
  name: Signzy Identity (India) API
  slug: signzy-identity-india-api
- description: The Identity (US) API from Signzy — 1 operation(s) for identity (us).
  name: Signzy Identity (US) API
  slug: signzy-identity-us-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signzy-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/signzy-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/signzy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signzy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signzy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signzy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signzy
- group: company
  title: ''
  type: Website
  url: https://www.signzy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.signzy.com
- group: commercial
  title: ''
  type: Plans
  url: plans/signzy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/signzy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/signzy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.signzy.com/blogs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signzy-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/signzy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/signzy-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/signzy-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/signzy-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/signzy-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/signzy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/signzy-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/signzy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/signzy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signzy.com
- group: design
  title: ''
  type: Conventions
  url: conventions/signzy-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/signzy-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/signzy-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.signzy.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.signzy.com/us/verification-api-marketplace/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.signzy.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.signzy.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.signzy.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.signzy.com/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://www.signzy.com/contact
- group: build
  title: ''
  type: Postman
  url: collections/signzy.postman_collection.json
created: '2026-07-17'
description: Signzy is a global identity verification, KYC, KYB and AML compliance platform founded in Bengaluru, India in 2015. Its API marketplace exposes 240+ bespoke verification building blocks - document OCR, liveness and face match, deepfake detection, Aadhaar/PAN and other India checks, US ID and business verification, AML/sanctions/PEP screening, bank verification, Video KYC and Aadhaar eSign - behind a single token-authenticated REST API across India, the US, the Middle East and APAC.
finops:
- name: Signzy Finops
  service_category: Identity and Compliance
  slug: signzy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signzy.png
layout: provider
mcp_servers:
- description: ''
  name: signzy-mcp.yml
  slug: signzy-mcpyml
modified: '2026-07-17'
name: Signzy
nav: Providers
network: true
overview: 'Signzy publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Banking API, Identity (India) API, and 1 more. Tagged areas include Identity Verification, KYC, KYB, AML, and Onboarding.


  Signzy''s developer surface includes authentication, documentation, engineering blog, sandbox, API reference, getting-started guide, support, and 29 more developer resources.'
plans:
- name: Signzy Plans Pricing
  plan_count: 2
  slug: signzy-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Signzy Rate Limits
  slug: signzy-rate-limits
score:
  band: strong
  composite: 63.9
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 57.1
    developer_ergonomics: 84.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 63.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Signzy Authentication
  slug: signzy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Signzy Domain Security
  slug: signzy-domain-security
  summary_line: HSTS
- kind: vulnerability-disclosure
  name: Signzy Vulnerability Disclosure
  slug: signzy-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Signzy Trust Center
  slug: signzy-trust-center
  summary_line: ISO 27001, SOC 2, GDPR, FATF-aligned
slug: signzy
tags:
- Identity Verification
- KYC
- KYB
- AML
- Onboarding
- Compliance
- RegTech
website: https://www.signzy.com/
---
