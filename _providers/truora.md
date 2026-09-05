---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 4
  name: Truora Agentic Access
  operation_count: 12
  slug: truora-agentic-access
  summary_line: 12 operations · 6 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.checks.truora.com
  baseurl_source: declared
  description: API-key and web integration token management.
  name: Truora Account API
  slug: truora-account-api
- baseURL: https://api.checks.truora.com
  baseurl_source: declared
  description: Background checks on persons, vehicles, and companies across LatAm.
  name: Truora Checks API
  slug: truora-checks-api
- baseURL: https://api.checks.truora.com
  baseurl_source: declared
  description: Recurring re-checks of previously verified subjects.
  name: Truora Continuous Monitoring API
  slug: truora-continuous-monitoring-api
- baseURL: https://api.checks.truora.com
  baseurl_source: declared
  description: Web and WhatsApp identity verification processes.
  name: Truora Digital Identity API
  slug: truora-digital-identity-api
- baseURL: https://api.checks.truora.com
  baseurl_source: declared
  description: Document, facial, email, and phone validation (KYC).
  name: Truora Validators API
  slug: truora-validators-api
artifact_total: 26
asyncapis:
- description: ''
  name: Truora Webhooks
  slug: truora-webhooks
collections:
- collection_type: postman
  name: Truora Account API
  slug: postman-truora-account-api
- collection_type: postman
  name: Truora Account Checks API
  slug: postman-truora-checks-api
- collection_type: postman
  name: Truora Account Continuous Monitoring API
  slug: postman-truora-continuous-monitoring-api
- collection_type: postman
  name: Truora Account Digital Identity API
  slug: postman-truora-digital-identity-api
- collection_type: postman
  name: Truora Account Validators API
  slug: postman-truora-validators-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Truora Account API
  slug: open-truora-account-api
- collection_type: open
  name: Truora Account Checks API
  slug: open-truora-checks-api
- collection_type: open
  name: Truora Account Continuous Monitoring API
  slug: open-truora-continuous-monitoring-api
- collection_type: open
  name: Truora Account Digital Identity API
  slug: open-truora-digital-identity-api
- collection_type: open
  name: Truora Account Validators API
  slug: open-truora-validators-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/truora/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/truora-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/truora-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/truora-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truora-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/truora-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truora
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truora
- group: company
  title: ''
  type: Website
  url: https://www.truora.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.truora.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/truora-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truora-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truora-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.truora.com/en
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truora-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/truora-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/truora-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/truora-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truora-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truora-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truora-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truora-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.truora.com/en/iso-27001-certification
- group: design
  title: ''
  type: DataModel
  url: data-model/truora-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/truora-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/truora-overlay.yaml
- group: design
  title: ''
  type: Components
  url: components/truora-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/truora-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://www.truora.com/es/politica-de-seguridad
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.truora.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.truora.com/guides/api_integration_guide/
- group: docs
  title: ''
  type: APIReference
  url: https://dev.truora.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.truora.com/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://account.truora.com/account#/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truora.com/en/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truora.com/en/integral-privacy-notice
- group: operate
  title: ''
  type: Support
  url: https://www.truora.com/en/contact-sales
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/truora-api-docs/workspace/truora-api-docs
created: '2026-07-17'
description: Truora is a Latin American identity verification and fraud-prevention platform. Its REST APIs run background checks on people, vehicles, and companies across LatAm, validate documents/faces/email/phone for KYC, and orchestrate web and WhatsApp conversational onboarding flows. All requests authenticate with a Truora-API-Key header.
finops:
- name: Truora Finops
  service_category: Identity and Fraud Prevention
  slug: truora-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truora.png
layout: provider
modified: '2026-07-17'
name: Truora
nav: Providers
network: true
overview: 'Truora publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Checks API, Continuous Monitoring API, and 2 more. Tagged areas include Identity Verification, KYC, Background Checks, Fraud Prevention, and LatAm.


  The Truora catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Truora''s developer surface includes authentication, documentation, engineering blog, getting-started guide, API reference, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Truora Plans Pricing
  plan_count: 3
  slug: truora-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Truora Rate Limits
  slug: truora-rate-limits
scopes:
- name: Truora Scopes
  scope_count: 14
  slug: truora-scopes
  summary_line: 14 scopes · authorizationCode/ciba/refreshToken
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 62.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truora/refs/heads/main/screenshots/truora-2026-08-17T080431.png
security:
- kind: authentication
  name: Truora Authentication
  slug: truora-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Truora Domain Security
  slug: truora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Truora Vulnerability Disclosure
  slug: truora-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Truora Trust Center
  slug: truora-trust-center
  summary_line: ISO 27001, ISO 30107, GDPR
slug: truora
tags:
- Identity Verification
- KYC
- Background Checks
- Fraud Prevention
- LatAm
- WhatsApp
website: https://www.truora.com/
---
