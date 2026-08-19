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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
api_count: 4
apis:
- description: The backend half of the Truecaller OAuth SDK flow. After the mobile SDK returns an authorization code, partners exchange it at POST /v1/token (authorization_code grant with PKCE code_verifier; refresh
  name: Truecaller OAuth User Verification API
  slug: truecaller-oauth-api
- description: Server-side validation for the drop-call / IM-OTP verification flow that covers users without the Truecaller app. GET /v1/otp/client/installation/phoneNumberDetail/{accessToken} (clientId header) retu
  name: Truecaller Non-Truecaller User Verification API
  slug: truecaller-otp-verification-api
- description: Profile retrieval for the mobile-web (deep link) verification flow. After a user consents in the Truecaller app, Truecaller POSTs the accessToken and requestId to the partner's callback URL together w
  name: Truecaller Web SDK Profile API
  slug: truecaller-web-sdk-profile-api
- description: REST APIs for Truecaller's Verified Business Caller ID platform. Partners exchange a Key ID + Secret API Key for a 60-minute bearer token (POST /clients/{clientAccountId}/token), then push dynamic cal
  name: Truecaller for Business API
  slug: truecaller-for-business-api
artifact_total: 9
asyncapis:
- description: ''
  name: Truecaller Webhooks
  slug: truecaller-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/truecaller-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.truecaller.com/responsible-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truecaller-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/truecaller-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/truecaller-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/truecaller-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/truecaller-security.txt
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/truecaller-openid-configuration.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truecaller-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truecaller-business-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/truecaller-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/truecaller-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truecaller-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/truecaller-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truecaller-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.truecaller.com/truecaller-for-business/verified-business-api-documentation/deprecated-apis
- group: design
  title: ''
  type: Conformance
  url: conformance/truecaller-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/truecaller-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/truecaller-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/truecaller-webhooks.yml
- group: company
  title: ''
  type: Website
  url: https://www.truecaller.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.truecaller.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.truecaller.com/truecaller-sdk
- group: docs
  title: ''
  type: APIReference
  url: https://docs.truecaller.com/truecaller-for-business/verified-business-api-documentation/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.truecaller.com/truecaller-sdk/getting-started
- group: operate
  title: ''
  type: Support
  url: https://developer.truecaller.com/support
- group: company
  title: ''
  type: Blog
  url: https://developer.truecaller.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/truecaller
- group: start
  title: ''
  type: SignUp
  url: https://sdk-console-noneu.truecaller.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truecaller.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truecaller.com/privacy-policy
created: '2026-07-17'
description: 'Truecaller is the Stockholm-based caller identification and spam-blocking platform (atomico and balderton-capital portfolio) used by hundreds of millions of people to know who is calling. For developers it publishes the Truecaller SDK for Android, iOS, mobile web, Flutter, React Native and Shopify - one-tap phone-number verification built on OAuth 2.0 with PKCE (authorization code + refresh token, OIDC-style userinfo) plus a drop-call / IM-OTP flow for non-Truecaller users. Truecaller for Business adds REST APIs on enterprise-portal-noneu.truecaller.com for verified business caller ID: call personalisation (dynamic caller ID), number management, verified campaigns, and Call Me Back / User Feedback webhooks.'
image: https://www.truecaller.com/open-graph.jpg
layout: provider
modified: '2026-07-21'
name: Truecaller
nav: Providers
network: true
overview: 'Truecaller publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Caller ID, Phone Verification, and Identity.


  The Truecaller catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Truecaller''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 24 more developer resources.'
random_paper: 32
scopes:
- name: Truecaller Scopes
  scope_count: 6
  slug: truecaller-scopes
  summary_line: 6 scopes · authorizationCode/refreshToken
score:
  band: developing
  composite: 48.6
  delta: 0.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 64.3
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 47.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 48.4
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truecaller/refs/heads/main/screenshots/truecaller-2026-08-17T082447.png
security:
- kind: authentication
  name: Truecaller Authentication
  slug: truecaller-authentication
  summary_line: oauth2/http bearer/apiKey · 5 schemes
- kind: domain-security
  name: Truecaller Domain Security
  slug: truecaller-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Truecaller Vulnerability Disclosure
  slug: truecaller-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: truecaller
tags:
- Company
- Consumer
- Caller ID
- Phone Verification
- Identity
- OAuth
- Spam Detection
- Communications
- Mobile SDK
website: https://www.truecaller.com
---
