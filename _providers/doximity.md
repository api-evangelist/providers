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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Doximity Agentic Access
  operation_count: 10
  slug: doximity-agentic-access
  summary_line: 10 operations · 3 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: OAuth 2.0 authorization and token endpoints
  name: Doximity OAuth API
  slug: doximity-oauth-api
- description: Identity and discovery endpoints
  name: Doximity OpenID Connect API
  slug: doximity-openid-connect-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.doximity.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.doximity.com/developers/home
- group: docs
  title: ''
  type: Documentation
  url: https://www.doximity.com/developers/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.doximity.com/developers/documentation
- group: start
  title: ''
  type: SignUp
  url: https://www.doximity.com/developers/api_signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doximity
- group: operate
  title: ''
  type: Support
  url: https://support.doximity.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doximity.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doximity.com/clinicians/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.doximity.com/about/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.doximity.com/about/security
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/doximity-oauth-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doximity-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/doximity-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/doximity-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/doximity-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/doximity-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/doximity-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/doximity-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doximity-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/doximity-oauth-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/doximity-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/doximity-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/doximity-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/doximity-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/doximity-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doximity-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doximity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/doximity-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doximity-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doximity-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Doximity is the leading digital platform for U.S. medical professionals, used by the majority of physicians and a large share of nurse practitioners and physician assistants. Its public developer surface is an OAuth 2.0 and OpenID Connect identity API hosted at auth.doximity.com that lets third-party applications verify and identify Doximity members against the Doximity medical database, request a curated set of profile claims (name, credentials, specialty, email, office, and more), and reduce registration friction. Doximity also ships the Doximity Dialer SDKs for iOS and Android so partner apps can place HIPAA-secure calls that mask the caller's personal number, plus a Share Button and Registration integration. Authentication uses the Authorization Code grant with mandatory PKCE, refresh tokens, and device_code, and the platform is SOC 2 Type 2 and HIPAA/HITECH certified. This profile was enriched by the API Evangelist pipeline from Doximity's public developer documentation
  and OpenID Connect discovery metadata.
image: https://www.doximity.com/img/logos/doximity-logo.png
layout: provider
mcp_servers:
- description: ''
  name: doximity-mcp.yml
  slug: doximity-mcpyml
modified: '2026-07-18'
name: Doximity
nav: Providers
network: true
overview: 'Doximity publishes 2 APIs on the [APIs.io](https://apis.io/) network: OAuth API and OpenID Connect API. Tagged areas include Company, Healthtech, Identity, OAuth, and OpenID Connect.


  Doximity''s developer surface includes documentation, getting-started guide, signup flow, support, authentication, and 27 more developer resources.'
random_paper: 40
rate_limits:
- limit_count: 0
  name: Doximity Rate Limits
  slug: doximity-rate-limits
scopes:
- name: Doximity Scopes
  scope_count: 21
  slug: doximity-scopes
  summary_line: 21 scopes · authorizationCode
score:
  band: developing
  composite: 50.2
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 49.2
    developer_ergonomics: 53.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 15.8
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 72.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doximity/refs/heads/main/screenshots/doximity-2026-07-25T212328.png
security:
- kind: authentication
  name: Doximity Authentication
  slug: doximity-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Doximity Domain Security
  slug: doximity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Doximity Vulnerability Disclosure
  slug: doximity-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Doximity Trust Center
  slug: doximity-trust-center
  summary_line: SOC 2 Type 2, SOC 3, HIPAA, HITECH
slug: doximity
tags:
- Company
- Healthtech
- Identity
- OAuth
- OpenID Connect
- Authentication
- Physician Network
- Healthcare
- SSO
- Verification
website: https://www.doximity.com
---
