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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 34.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Doximity Agentic Access
  operation_count: 10
  slug: doximity-agentic-access
  summary_line: 10 operations · 3 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://auth.doximity.com
  baseurl_source: declared
  description: OAuth 2.0 authorization and token endpoints
  name: Doximity OAuth API
  slug: doximity-oauth-api
- baseURL: https://auth.doximity.com
  baseurl_source: declared
  description: Identity and discovery endpoints
  name: Doximity OpenID Connect API
  slug: doximity-openid-connect-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Doximity 2.0 & OpenID Connect OAuth API
  slug: open-doximity-oauth-api
- collection_type: open
  name: Doximity 2.0 & OAuth OpenID Connect API
  slug: open-doximity-openid-connect-api
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
  url: openapi/_original/doximity-oauth-openapi.yml
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
  name: Doximity MCP Server
  slug: doximity-mcp-server
modified: '2026-07-18'
name: Doximity
nav: Providers
network: true
overview: 'Doximity publishes 2 APIs on the [APIs.io](https://apis.io/) network: OAuth API and OpenID Connect API. Tagged areas include Company, Health Tech, Identity, Authentication, and OpenID Connect.


  Doximity''s developer surface includes documentation, getting-started guide, signup flow, support, authentication, and 27 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 1
  name: Doximity Rate Limits
  slug: doximity-rate-limits
scopes:
- name: Doximity Scopes
  scope_count: 21
  slug: doximity-scopes
  summary_line: 21 scopes · authorizationCode
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 46.9
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 55.3
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Health Tech
- Identity
- Authentication
- OpenID Connect
- Physician Network
- Healthcare
- SSO
- Verification
website: https://www.doximity.com
---
