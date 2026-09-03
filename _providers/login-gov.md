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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Login Gov Agentic Access
  operation_count: 9
  slug: login-gov-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 2
apis:
- baseURL: https://secure.login.gov
  baseurl_source: declared
  description: SAML SSO request endpoint.
  name: Login.gov Authentication API
  slug: login-gov-authentication-api
- baseURL: https://secure.login.gov
  baseurl_source: declared
  description: OAuth 2.0 authorization endpoint where the user authenticates.
  name: Login.gov Authorization API
  slug: login-gov-authorization-api
- baseURL: https://secure.login.gov
  baseurl_source: declared
  description: OIDC discovery and public key endpoints.
  name: Login.gov Discovery API
  slug: login-gov-discovery-api
- baseURL: https://secure.login.gov
  baseurl_source: declared
  description: RP-initiated logout and session termination.
  name: Login.gov Logout API
  slug: login-gov-logout-api
- baseURL: https://secure.login.gov
  baseurl_source: declared
  description: SAML 2.0 IdP metadata.
  name: Login.gov Metadata API
  slug: login-gov-metadata-api
- baseURL: https://secure.login.gov
  baseurl_source: declared
  description: Token exchange using private_key_jwt or PKCE.
  name: Login.gov Token API
  slug: login-gov-token-api
- baseURL: https://secure.login.gov
  baseurl_source: declared
  description: User attribute retrieval with a bearer access token.
  name: Login.gov UserInfo API
  slug: login-gov-userinfo-api
artifact_total: 45
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Login.gov OpenID Connect Authentication API
  slug: open-login-gov-authentication-api
- collection_type: open
  name: Login.gov OpenID Connect Authentication Authorization API
  slug: open-login-gov-authorization-api
- collection_type: open
  name: Login.gov OpenID Connect Authentication Discovery API
  slug: open-login-gov-discovery-api
- collection_type: open
  name: Login.gov OpenID Connect Authentication Logout API
  slug: open-login-gov-logout-api
- collection_type: open
  name: Login.gov OpenID Connect Authentication Metadata API
  slug: open-login-gov-metadata-api
- collection_type: open
  name: Login.gov OpenID Connect API
  slug: open-login-gov-oidc
- collection_type: open
  name: Login.gov SAML 2.0 API
  slug: open-login-gov-saml
- collection_type: open
  name: Login.gov OpenID Connect Authentication Token API
  slug: open-login-gov-token-api
- collection_type: open
  name: Login.gov OpenID Connect Authentication UserInfo API
  slug: open-login-gov-userinfo-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/login-gov-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/18F/identity-idp/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/18F/identity-idp/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/18F/identity-idp/blob/main/docs/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/18F/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/18F/identity-idp/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/login-gov-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/login-gov-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/login-gov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/login-gov-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.login.gov
- group: start
  title: ''
  type: Portal
  url: https://www.login.gov/partners
- group: docs
  title: ''
  type: Documentation
  url: https://developers.login.gov
- group: start
  title: ''
  type: Signup
  url: https://www.login.gov/partners/get-started/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.login.gov/oidc/getting-started/
- group: start
  title: ''
  type: Sandbox
  url: https://portal.int.identitysandbox.gov
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/18F
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/18F/identity-idp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/18F/identity-oidc-sinatra
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/18F/identity-saml-sinatra
- group: operate
  title: ''
  type: StatusPage
  url: https://status.login.gov
- group: company
  title: ''
  type: Blog
  url: https://www.login.gov/about/news/
- group: operate
  title: ''
  type: Contact
  url: https://www.login.gov/contact/
- group: other
  title: ''
  type: BusinessInquiries
  url: https://www.login.gov/partners/business-inquiries/
- group: commercial
  title: ''
  type: Privacy
  url: https://www.login.gov/policy/
- group: other
  title: ''
  type: Accessibility
  url: https://www.login.gov/accessibility/
- group: commercial
  title: ''
  type: Plans
  url: plans/login-gov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/login-gov-rate-limits.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/login-gov-vocabulary.yml
created: '2026-05-25'
description: Login.gov is the U.S. federal government's secure single sign-on and identity verification service for the public, operated by the General Services Administration's Technology Transformation Services (GSA TTS). Relying parties — federal, and in some cases state and local — federate user authentication to Login.gov via OpenID Connect (iGov profile) or SAML 2.0, with support for IAL1 (auth-only) and IAL2 (identity-verified) assurance and AAL2 multi-factor authentication including phishing-resistant and PIV/CAC authenticators.
examples:
- key_count: 2
  name: Login Gov Token Exchange Example
  slug: login-gov-token-exchange-example
- key_count: 9
  name: Login Gov Userinfo Ial1 Example
  slug: login-gov-userinfo-ial1-example
- key_count: 16
  name: Login Gov Userinfo Ial2 Example
  slug: login-gov-userinfo-ial2-example
features:
- Single account for the public to access participating federal services
- OpenID Connect (iGov profile) and SAML 2.0 federation
- Authorization code flow with private_key_jwt or PKCE; implicit flow not supported
- IAL1 (authentication only) and IAL2 (identity-verified) assurance levels
- AAL2 with TOTP, SMS/voice, push, security keys, PIV/CAC, and platform passkeys
- Phishing-resistant AAL2 variant and HSPD-12 (PIV/CAC) AAL2 variant
- Identity proofing with optional facial-match step
- Self-service Partner Portal (sandbox and production) for client registration and scope/cert management
- JWKS endpoint with at-least-annual key rotation; SAML certs rotated yearly with year-versioned endpoints
- User attributes scoped per OIDC scope/SAML attribute: email, all_emails, name, address, birthdate, phone, SSN, verified_at, locale, x509 subject/issuer/presented
- Built and operated in the open: identity-idp (Ruby on Rails) and sample SP apps published under github.com/18F
- English, Spanish, and French locales
- Section 508 accessibility commitment; published privacy policy and PIA
- Cost-recoverable funding model via Interagency Agreement (IAA); no public rate card
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/login-gov.png
json_schemas:
- name: Login.gov ID Token Claims
  property_count: 11
  slug: login-gov-id-token
- name: Login.gov UserInfo
  property_count: 19
  slug: login-gov-userinfo
jsonld:
- class_count: 29
  name: Login Gov Context
  property_count: 4
  slug: login-gov-context
layout: provider
modified: '2026-05-25'
name: Login.gov
nav: Providers
network: true
overview: 'Login.gov publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Authorization API, Discovery API, and 4 more. Tagged areas include Government, Federal, GSA, Identity, and Authentication.


  The Login.gov catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Login.gov''s developer surface includes authentication, developer portal, documentation, signup flow, getting-started guide, sandbox, engineering blog, and 22 more developer resources.'
plans:
- name: Login Gov Plans Pricing
  plan_count: 2
  slug: login-gov-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Login Gov Rate Limits
  slug: login-gov-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Login.gov API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: login-gov-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Login.gov API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: login-gov-rules
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 42.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 28.8
    contract_quality: 64.7
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 65.0
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/login-gov/refs/heads/main/screenshots/login-gov-2026-06-20T184653.png
security:
- kind: authentication
  name: Login Gov Authentication
  slug: login-gov-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Login Gov Domain Security
  slug: login-gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Login Gov Vulnerability Disclosure
  slug: login-gov-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: login-gov
tags:
- Government
- Federal
- GSA
- Identity
- Authentication
- SSO
- OIDC
- SAML
- IAL2
- AAL2
website: https://www.login.gov
---
