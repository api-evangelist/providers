---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
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
  description: Identity and discovery endpoints
  name: Doximity OpenID Connect API
  slug: doximity-openid-connect-api
- baseURL: https://auth.doximity.com
  baseurl_source: declared
  description: OAuth 2.0 authorization and token endpoints
  name: Doximity O Auth API
  slug: doximity-oauth-api
artifact_total: 14
collections:
- collection_type: open
  name: Doximity 2.0 & OpenID Connect OAuth API
  slug: open-doximity-oauth-api
- collection_type: open
  name: Doximity 2.0 & OAuth OpenID Connect API
  slug: open-doximity-openid-connect-api
common:
- group: company
  title: ''
  type: Blog
  url: https://blog.doximity.com/updates
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.doximity.com/feed
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
  href: https://artifacts.apis.io/doximity/openapi/_original/doximity-oauth-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/doximity-oauth-openapi.yml
- group: auth
  href: https://artifacts.apis.io/doximity/authentication/doximity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doximity-authentication.yml
- group: auth
  href: https://artifacts.apis.io/doximity/scopes/doximity-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/doximity-scopes.yml
- group: agent
  href: https://artifacts.apis.io/doximity/well-known/doximity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doximity-well-known.yml
- group: auth
  href: https://artifacts.apis.io/doximity/well-known/doximity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doximity-security.txt
- group: build
  href: https://artifacts.apis.io/doximity/packages/doximity-packages.yml
  title: ''
  type: Packages
  url: packages/doximity-packages.yml
- group: build
  href: https://artifacts.apis.io/doximity/packages/doximity-packages.yml
  title: ''
  type: SDKs
  url: packages/doximity-packages.yml
- group: agent
  href: https://artifacts.apis.io/doximity/mcp/doximity-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/doximity-mcp.yml
- group: agent
  href: https://artifacts.apis.io/doximity/llms/doximity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doximity-llms.txt
- group: other
  href: https://artifacts.apis.io/doximity/overlays/doximity-oauth-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doximity-oauth-overlay.yaml
- group: design
  href: https://artifacts.apis.io/doximity/conformance/doximity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doximity-conformance.yml
- group: design
  href: https://artifacts.apis.io/doximity/errors/doximity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/doximity-problem-types.yml
- group: design
  href: https://artifacts.apis.io/doximity/lifecycle/doximity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/doximity-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/doximity/conventions/doximity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/doximity-conventions.yml
- group: design
  href: https://artifacts.apis.io/doximity/data-model/doximity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/doximity-data-model.yml
- group: operate
  href: https://artifacts.apis.io/doximity/rate-limits/doximity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/doximity-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/doximity/security/doximity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doximity-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/doximity/security/doximity-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/doximity-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/doximity/security/doximity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doximity-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/doximity/agentic-access/doximity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/doximity-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/doximity/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Doximity is the leading digital platform for U.S. medical professionals, used by the majority of physicians and a large share of nurse practitioners and physician assistants. Its public developer surface is an OAuth 2.0 and OpenID Connect identity API hosted at auth.doximity.com that lets third-party applications verify and identify Doximity members against the Doximity medical database, request a curated set of profile claims (name, credentials, specialty, email, office, and more), and reduce registration friction. Doximity also ships the Doximity Dialer SDKs for iOS and Android so partner apps can place HIPAA-secure calls that mask the caller's personal number, plus a Share Button and Registration integration. Authentication uses the Authorization Code grant with mandatory PKCE, refresh tokens, and device_code, and the platform is SOC 2 Type 2 and HIPAA/HITECH certified. This profile was enriched by the API Evangelist pipeline from Doximity's public developer documentation
  and OpenID Connect discovery metadata.
image: https://www.doximity.com/img/logos/doximity-logo.png
layout: provider
modified: '2026-10-06'
name: Doximity
nav: Providers
network: true
overview: 'Doximity publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: OpenID Connect API and O Auth API. Tagged areas include Company, Health Tech, Identity, OAuth, and OpenID Connect.


  The Doximity catalog on APIs.io includes 1 Spectral governance ruleset.


  Doximity''s developer surface includes engineering blog, documentation, getting-started guide, signup flow, support, authentication, and 28 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 1
  name: Doximity Rate Limits
  slug: doximity-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Doximity API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: doximity-rules
scopes:
- name: Doximity Scopes
  scope_count: 21
  slug: doximity-scopes
  summary_line: 21 scopes · authorizationCode
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 42.2
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 34.2
  previous_composite: 52.2
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
    score: 45.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/doximity/doximity-2026-07-25T212328.png
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
skill_count: 2
skills:
- name: Refresh and revoke a Doximity session
  slug: doximity-refresh-and-revoke
- name: Verify and identify a Doximity member
  slug: doximity-verify-member
slug: doximity
tags:
- Company
- Health Tech
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
