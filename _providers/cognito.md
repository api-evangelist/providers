---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-09-17'
api_count: 1
apis:
- description: REST API for identity verification, KYC, and AML watchlist/PEP screening. JSON:API media type (application/vnd.api+json), date-based versioning via the Cognito-Version header, and HTTP request-signatu
  name: Cognito Identity Verification API
  slug: cognito-identity-verification-api
artifact_total: 5
asyncapis:
- description: ''
  name: Cognito Flow Webhooks
  slug: cognito-flow-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.cognitohq.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/plaid/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cognitohq.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cognitohq.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cognitohq.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://cognitohq.com/docs/identity/id-verification-api-quickstart
- group: company
  title: ''
  type: Blog
  url: https://cognitohq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://plaid.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.plaid.com/signup/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cognitohq.com/privacy-statement
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cognitohq.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://cognitohq.com/docs/guides/api-changelog
- group: operate
  title: ''
  type: Deprecation
  url: https://cognitohq.com/docs/guides/breaking-changes
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/asyncapi/cognito-flow-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cognito-flow-webhooks.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/authentication/cognito-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cognito-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/conventions/cognito-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cognito-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/conformance/cognito-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cognito-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/lifecycle/cognito-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cognito-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/changelog/cognito-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cognito-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/packages/cognito-packages.yml
  title: ''
  type: Packages
  url: packages/cognito-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/sandbox/cognito-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cognito-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/errors/cognito-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cognito-problem-types.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/security/cognito-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cognito-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cognitohq.com/docs/guides/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/security/cognito-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cognito-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/mcp/cognito-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cognito-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/llms/cognito-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cognito-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/components/cognito-components.yml
  title: ''
  type: Components
  url: components/cognito-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/data-model/cognito-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cognito-data-model.yml
created: '2026-07-17'
description: 'Cognito (cognitohq.com, operated by BlockScore, Inc.) is an identity verification, KYC, and AML compliance API provider that was backed by Y Combinator and Battery Ventures and acquired by Plaid in 2020. Its API turns a phone number, name, or ID document into a verified identity in under a minute, covering 209 countries and thousands of document types. Three developer products sit on one REST API: Identity (phone-first, frictionless verification), Flow (an all-in-one hosted / embeddable verification experience integrated in minutes with document and selfie checks), and Screening (watchlist, sanctions, and politically-exposed-person AML screening with daily re-scans across 20+ lists). The API is JSON:API (application/vnd.api+json), date-versioned via a Cognito-Version header, and authenticated with HTTP request signatures (HMAC-SHA256 over a digest of the body). It ships a sandbox host, signed webhooks, and client SDKs for seven languages.'
image: https://cognitohq.com/wp-content/themes/cognito/images/cognito-share.jpg
layout: provider
modified: '2026-07-18'
name: Cognito
nav: Providers
network: true
overview: 'Cognito publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Identity, Identity Verification, KYC, and AML.


  The Cognito catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cognito''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 22 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 59.5
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 43.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/cognito/refs/heads/main/screenshots/cognito-2026-07-25T210011.png
security:
- kind: authentication
  name: Cognito Authentication
  slug: cognito-authentication
  summary_line: httpSignature · 1 scheme
- kind: domain-security
  name: Cognito Domain Security
  slug: cognito-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cognito Vulnerability Disclosure
  slug: cognito-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: cognito
tags:
- Company
- Identity
- Identity Verification
- KYC
- AML
- Compliance
- Fraud Prevention
- Onboarding
- Watchlist Screening
website: https://www.cognitohq.com/
---
