---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-05'
api_count: 6
apis:
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The administrative REST API for a Strivacity instance — accounts and identity stores, applications and clients, adaptive access and MFA policies, journeys, branding, consents, claims and dialects, gro
  name: Strivacity Admin API
  slug: strivacity-admin-api
- baseURL: https://{tenant}.strivacity.com/myaccount/api/v1
  baseurl_source: declared
  description: The end-customer self-service REST API behind the Strivacity My Account portal — authenticator (MFA) management, consent opt-in and opt-out, personal-data export and account deletion, and self-managem
  name: Strivacity MyAccount API
  slug: strivacity-myaccount-api
- baseURL: https://{tenant}.strivacity.com/flow/api
  baseurl_source: declared
  description: The Native Journey (Journey Flow) API used by native and single-page applications to render Strivacity login, registration, MFA, passkey, password-reset and account-activation journeys in their own UI
  name: Strivacity Journey Flow API
  slug: strivacity-journey-flow-api
artifact_total: 11
asyncapis:
- description: ''
  name: Strivacity Events
  slug: strivacity-events
common:
- group: company
  title: ''
  type: Website
  url: https://www.strivacity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.strivacity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strivacity.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.strivacity.com/reference/getting-started-with-the-admin-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.strivacity.com/reference/getting-started-1
- group: operate
  title: ''
  type: Support
  url: https://support.strivacity.com/
- group: company
  title: ''
  type: Blog
  url: https://www.strivacity.com/learn-support/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strivacity
- group: commercial
  title: ''
  type: Pricing
  url: https://www.strivacity.com/products/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.strivacity.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.strivacity.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.strivacity.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.strivacity.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.strivacity.com/docs/release-support-matrix
- group: auth
  title: ''
  type: Security
  url: https://www.strivacity.com/report-a-security-issue
- group: auth
  title: ''
  type: Compliance
  url: https://security.strivacity.com
- group: auth
  title: ''
  type: TrustCenter
  url: security/strivacity-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/strivacity-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/strivacity-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/strivacity-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.strivacity.com/.well-known/api-catalog
- group: build
  title: ''
  type: Packages
  url: packages/strivacity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/strivacity-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/strivacity-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/strivacity-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/strivacity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/strivacity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/strivacity-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/strivacity-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/strivacity-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strivacity-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/strivacity-vulnerability-disclosure.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/strivacity-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/strivacity-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/strivacity-events.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/strivacity-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/strivacity-plans-pricing.yml
created: '2026-08-29'
description: 'Strivacity is a customer identity and access management (CIAM) vendor that runs a single-tenant, dedicated-cloud identity platform for consumer, partner, B2B and — since its Agentic AI release — AI-agent identities. The product covers registration and self-service, adaptive multi-factor authentication, passkeys and FIDO2, social and enterprise federation, consent management, identity verification, fraud detection, delegated administration and identity orchestration, and it exposes all of it through published REST APIs: an Admin API for configuring and operating an instance, an Admin Management API for the admin plane itself, a MyAccount API for end-customer self-service, a Journey Flow (Native Journey) API for rendering login and registration natively, and a Simple Authentication API. Strivacity also acts as the OAuth 2.1 authorization server in front of a customer''s own MCP servers and APIs, issuing audience-restricted, consent-gated tokens to AI agents.'
image: https://cdn.prod.website-files.com/64259842d8e30c2ec61617ab/642b123a6f2bf0db754b0ab3_webclip.png
layout: provider
modified: '2026-08-29'
name: Strivacity
nav: Providers
network: true
overview: 'Strivacity publishes 3 APIs on the [APIs.io](https://apis.io/) network: Admin API, MyAccount API, and Journey Flow API. Tagged areas include Identity, customer-identity-and-access-management, CIAM, Authentication, and Authorization.


  The Strivacity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Strivacity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Strivacity Plans Pricing
  plan_count: 1
  slug: strivacity-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 9
  name: Strivacity Rate Limits
  slug: strivacity-rate-limits
scopes:
- name: Strivacity Scopes
  scope_count: 0
  slug: strivacity-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 66.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 65.2
    developer_ergonomics: 54.2
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 88.2
  previous_composite: 66.4
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/strivacity/refs/heads/main/screenshots/strivacity-2026-09-02T161018.png
security:
- kind: authentication
  name: Strivacity Authentication
  slug: strivacity-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Strivacity Domain Security
  slug: strivacity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Strivacity Vulnerability Disclosure
  slug: strivacity-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Strivacity Trust Center
  slug: strivacity-trust-center
  summary_line: SOC 2 Type II, SOC 3, PCI DSS, GDPR, CCPA, FIPS 140-2, VPAT, FIDO Certification
slug: strivacity
tags:
- Identity
- customer-identity-and-access-management
- CIAM
- Authentication
- Authorization
- OpenID Connect
- Consent Management
- Multi-Factor Authentication
- Identity Verification
- Fraud Detection
- Agentic Identity
- Security
website: https://www.strivacity.com/
---
