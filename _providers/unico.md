---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 33.5
  scored_at: '2026-09-03'
api_count: 3
apis:
- baseURL: https://api.id.unico.app
  baseurl_source: declared
  description: The API contract (internally TCA / Check.Integration) — used when the integrator's own application owns the biometric capture and sends the image directly in the request. The verification result retur
  name: Unico IDCloud API
  slug: idcloud-api
- baseURL: https://api.idcloud.unico.app
  baseurl_source: declared
  description: The Web & SDK contract — used when Unico hosts the verification journey. The process is created before capture; the response carries a userRedirectUrl the end user is sent to by iFrame or redirect, pl
  name: Unico IDCloud Web & SDK API
  slug: idcloud-web-sdk
- baseURL: https://identity.acesso.io
  baseurl_source: declared
  description: 'The OAuth2 token service every IDCloud contract authenticates against. Implements the RFC 7523 JWT-bearer grant with an RS256-signed assertion exchanged for a one-hour access token, and serves a live '
  name: Unico Identity OAuth2
  slug: identity-oauth2
artifact_total: 14
asyncapis:
- description: ''
  name: Unico Webhooks
  slug: unico-webhooks
collections:
- collection_type: postman
  name: To Share
  slug: postman-unico-api-integration
- collection_type: postman
  name: unico - Authentication - Oauth2
  slug: postman-unico-oauth2
- collection_type: postman
  name: Plataforma Unico
  slug: postman-unico-web-sdk-integration
common:
- group: company
  title: ''
  type: Website
  url: https://www.unico.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.unico.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.unico.io/developers/api-reference/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.unico.io/developers/api-reference/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.unico.io/developers/api-reference/authentication
- group: operate
  title: ''
  type: Support
  url: https://www.unico.io/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.unico.io/resources/faq
- group: company
  title: ''
  type: Blog
  url: https://www.unico.io/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unico-id
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unico.io
- group: start
  title: ''
  type: Login
  url: https://business.unico.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://devcenter.unico.io/privacy/usa/policies/website-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://devcenter.unico.io/privacy/usa/policies/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://developer.unico.io/developers/api-reference/postman
- group: auth
  title: ''
  type: Security
  url: security/unico-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unico-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/unico-security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/unico-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/unico-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unico-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unico-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unico-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unico-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unico-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unico-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unico-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unico-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unico-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/unico-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unico-packages.yml
- group: design
  title: ''
  type: Components
  url: components/unico-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unico-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unico-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/unico-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/unico-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unico-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unico-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unico-domain-security.yml
created: '2026-09-02'
description: 'Unico (unico IDtech) is a Brazilian identity-technology company whose IDCloud platform performs facial-biometric identity verification, liveness detection, document capture and OCR, and fraud-risk decisioning for customer onboarding, step-up authentication and card-not-present payment verification. Founded out of Acesso Digital and headquartered in Sao Paulo with offices in Mexico City, Londrina and Menlo Park, it has raised roughly $338M across four rounds and states it processes 150M+ transactions per month on Google Cloud. Its public developer surface is two REST contracts — an API contract where the integrator owns the camera and sends the selfie in the request, and a Web & SDK contract where Unico hosts the whole verification journey — plus an outbound webhook, four native capture SDKs, and three published Postman collections. It publishes no OpenAPI: the developer portal''s own OpenAPI page reads "Placeholder OpenAPI specification."'
image: https://developer.unico.io/img/unico-favicon.png
layout: provider
modified: '2026-09-02'
name: Unico
nav: Providers
network: true
overview: 'Unico publishes 3 APIs on the [APIs.io](https://apis.io/) network: IDCloud API, IDCloud Web & SDK API, and Identity OAuth2. Tagged areas include Identity Verification, Biometrics, Facial Recognition, Liveness Detection, and KYC.


  The Unico catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Unico''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, changelog, and 31 more developer resources.'
plans:
- name: Unico Plans Pricing
  plan_count: 0
  slug: unico-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Unico Rate Limits
  slug: unico-rate-limits
scopes:
- name: Unico Scopes
  scope_count: 0
  slug: unico-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 76.2
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 55.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Unico Authentication
  slug: unico-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Unico Domain Security
  slug: unico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unico Vulnerability Disclosure
  slug: unico-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Unico Trust Center
  slug: unico-trust-center
  summary_line: SOC 2 Type 2, GDPR, ISO/IEC 42001, iBeta Level 1 (Presentation Attack Detection), iBeta Level 2 (Presentation Attack Detection), BixeLab Level 1 (Presentation Attack Detection), BixeLab Level 2 (Presentation Attack Detection), BixeLab Level 3 (Presentation Attack Detection), BixeLab Injection Attack Detection, Tested by NIST (face recognition)
slug: unico
tags:
- Identity Verification
- Biometrics
- Facial Recognition
- Liveness Detection
- KYC
- Fraud Prevention
- Onboarding
- Authentication
- AML
- Age Verification
- Document Verification
- Identity
- Brazil
- Latin America
website: https://www.unico.io
---
