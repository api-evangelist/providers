---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 63
  human_in_the_loop: 1
  name: Authlete Agentic Access
  operation_count: 86
  slug: authlete-agentic-access
  summary_line: 86 operations · 63 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing OAuth 2.0 Authorization Endpoint.
  name: Authlete Authorization Endpoint API
  slug: authlete-authorization-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing Client-Initiated Backchannel Authentication (CIBA).
  name: Authlete CIBA API
  slug: authlete-ciba-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for managing OAuth clients, including creation, update, and deletion of clients.
  name: Authlete Client Management API
  slug: authlete-client-management-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing OAuth 2.0 Device Flow
  name: Authlete Device Flow API
  slug: authlete-device-flow-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing OAuth 2.0 Dynamic Client Registration.
  name: Authlete Dynamic Client Registration API
  slug: authlete-dynamic-client-registration-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing OpenID Federation using Authlete.
  name: Authlete Federation Endpoint API
  slug: authlete-federation-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoint for implementing OAuth 2.0 grants, including grant management actions like updating and revoking grants.
  name: Authlete Grant Management Endpoint API
  slug: authlete-grant-management-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for managing hardware security keys (HSK).
  name: Authlete Hardware Security Key API
  slug: authlete-hardware-security-key-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing OAuth 2.0 Introspection Endpoint.
  name: Authlete Introspection Endpoint API
  slug: authlete-introspection-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for JOSE objects.
  name: Authlete Jose Object API
  slug: authlete-jose-object-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for to generate JSON Web Key Set (JWKS) for a service.
  name: Authlete JWK Set Endpoint API
  slug: authlete-jwk-set-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: The Lifecycle API from Authlete — 1 operation(s) for lifecycle.
  name: Authlete Lifecycle API
  slug: authlete-lifecycle-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for Native SSO
  name: Authlete Native SSO API
  slug: authlete-native-sso-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing OAuth 2.0 Pushed Authorization Requests (PAR).
  name: Authlete Pushed Authorization Endpoint API
  slug: authlete-pushed-authorization-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoint for implementing OAuth 2.0 Revocation Endpoint.
  name: Authlete Revocation Endpoint API
  slug: authlete-revocation-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for managing services, including creation, update, and deletion of services.
  name: Authlete Service Management API
  slug: authlete-service-management-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing OAuth 2.0 Token Endpoint.
  name: Authlete Token Endpoint API
  slug: authlete-token-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for various token related operations, including creating, revoking and deleting access_tokens with specified scopes.
  name: Authlete Token Operations API
  slug: authlete-token-operations-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing OpenID Connect UserInfo Endpoint.
  name: Authlete UserInfo Endpoint API
  slug: authlete-userinfo-endpoint-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for various utility operations.
  name: Authlete Utility Endpoints API
  slug: authlete-utility-endpoints-api
- baseURL: https://us.authlete.com
  baseurl_source: declared
  description: API endpoints for implementing and running a Verifiable Credential Issuer (VCI).
  name: Authlete Verifiable Credential Issuer API
  slug: authlete-verifiable-credential-issuer-api
artifact_total: 53
collections:
- collection_type: open
  name: Authlete Authorization Endpoint API
  slug: open-authlete-authorization-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint CIBA API
  slug: open-authlete-ciba-api
- collection_type: open
  name: Authlete Authorization Endpoint Client Management API
  slug: open-authlete-client-management-api
- collection_type: open
  name: Authlete Authorization Endpoint Device Flow API
  slug: open-authlete-device-flow-api
- collection_type: open
  name: Authlete Authorization Endpoint Dynamic Client Registration API
  slug: open-authlete-dynamic-client-registration-api
- collection_type: open
  name: Authlete Authorization Endpoint Federation Endpoint API
  slug: open-authlete-federation-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint Grant Management Endpoint API
  slug: open-authlete-grant-management-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint Hardware Security Key API
  slug: open-authlete-hardware-security-key-api
- collection_type: open
  name: Authlete Authorization Endpoint Introspection Endpoint API
  slug: open-authlete-introspection-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint Jose Object API
  slug: open-authlete-jose-object-api
- collection_type: open
  name: Authlete Authorization Endpoint JWK Set Endpoint API
  slug: open-authlete-jwk-set-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint Lifecycle API
  slug: open-authlete-lifecycle-api
- collection_type: open
  name: Authlete Authorization Endpoint Native SSO API
  slug: open-authlete-native-sso-api
- collection_type: open
  name: Authlete Authorization Endpoint Pushed Authorization Endpoint API
  slug: open-authlete-pushed-authorization-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint Revocation Endpoint API
  slug: open-authlete-revocation-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint Service Management API
  slug: open-authlete-service-management-api
- collection_type: open
  name: Authlete Authorization Endpoint Token Endpoint API
  slug: open-authlete-token-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint Token Operations API
  slug: open-authlete-token-operations-api
- collection_type: open
  name: Authlete Authorization Endpoint UserInfo Endpoint API
  slug: open-authlete-userinfo-endpoint-api
- collection_type: open
  name: Authlete Authorization Endpoint Utility Endpoints API
  slug: open-authlete-utility-endpoints-api
- collection_type: open
  name: Authlete Authorization Endpoint Verifiable Credential Issuer API
  slug: open-authlete-verifiable-credential-issuer-api
common:
- group: commercial
  href: https://artifacts.apis.io/authlete/plans/authlete-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/authlete-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/authlete/capabilities/authlete-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/authlete-capability-edges.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.authlete.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.authlete.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.authlete.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.authlete.com/developers/getting_started/
- group: operate
  title: ''
  type: Support
  url: https://www.authlete.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.authlete.com/resources/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/authlete
- group: commercial
  title: ''
  type: Pricing
  url: https://www.authlete.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.authlete.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.authlete.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.authlete.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.authlete.com/service-status
- group: operate
  title: ''
  type: Deprecation
  url: https://www.authlete.com/developers/lts_policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.authlete.com/developers/relnotes/
- group: build
  href: https://artifacts.apis.io/authlete/packages/authlete-packages.yml
  title: ''
  type: Packages
  url: packages/authlete-packages.yml
- group: build
  href: https://artifacts.apis.io/authlete/packages/authlete-packages.yml
  title: ''
  type: SDKs
  url: packages/authlete-packages.yml
- group: build
  href: https://artifacts.apis.io/authlete/cli/authlete-cli.yml
  title: ''
  type: CLI
  url: cli/authlete-cli.yml
- group: design
  href: https://artifacts.apis.io/authlete/components/authlete-components.yml
  title: ''
  type: Components
  url: components/authlete-components.yml
- group: agent
  href: https://artifacts.apis.io/authlete/mcp/authlete-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/authlete-mcp.yml
- group: agent
  href: https://artifacts.apis.io/authlete/llms/authlete-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authlete-llms.txt
- group: other
  href: https://artifacts.apis.io/authlete/overlays/authlete-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/authlete-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/authlete/conformance/authlete-conformance.yml
  title: ''
  type: Conformance
  url: conformance/authlete-conformance.yml
- group: design
  href: https://artifacts.apis.io/authlete/errors/authlete-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/authlete-problem-types.yml
- group: design
  href: https://artifacts.apis.io/authlete/lifecycle/authlete-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/authlete-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/authlete/conventions/authlete-conventions.yml
  title: ''
  type: Conventions
  url: conventions/authlete-conventions.yml
- group: design
  href: https://artifacts.apis.io/authlete/data-model/authlete-data-model.yml
  title: ''
  type: DataModel
  url: data-model/authlete-data-model.yml
- group: agent
  href: https://artifacts.apis.io/authlete/well-known/authlete-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/authlete-well-known.yml
- group: auth
  href: https://artifacts.apis.io/authlete/well-known/authlete-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/authlete-security.txt
- group: agent
  href: https://artifacts.apis.io/authlete/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/authlete/agentic-access/authlete-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/authlete-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/authlete/authentication/authlete-authentication.yml
  title: ''
  type: Authentication
  url: authentication/authlete-authentication.yml
- group: auth
  href: https://artifacts.apis.io/authlete/security/authlete-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/authlete-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.authlete.com/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/authlete/security/authlete-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authlete-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://authlete.com
created: '2026-07-17'
description: Authlete is an API-first OAuth 2.0 and OpenID Connect backend service that provides a headless authorization-server engine. It handles the OAuth/OIDC protocol logic and token management so organizations can stand up standards-compliant authorization servers and verifiable-credential issuers without building the protocol layer themselves. Authlete separates the Management APIs (configure services and clients) from the Runtime APIs (power authorization, token, introspection, CIBA, device-flow, federation, and OID4VCI endpoints), and offers managed shared cloud, dedicated cloud, and self-managed deployment across US, Japan, Europe, and Brazil regional clusters. It supports advanced profiles including FAPI / FAPI 2.0, CIBA, PAR, Grant Management, OpenID Federation, Native SSO, and OpenID for Verifiable Credential Issuance, plus regional open-banking standards (Brazil Open Banking, Australia CDR). Backed by 500 Global.
finops:
- has_sources: true
  method: derived
  name: Authlete Finops
  primary_unit: subscription
  service_category: ''
  slug: authlete-finops
  template: false
image: https://avatars.githubusercontent.com/u/8684109?v=4
layout: provider
modified: '2026-07-18'
name: Authlete
nav: Providers
network: true
overview: 'Authlete publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authorization Endpoint API, CIBA API, Client Management API, and 18 more. Tagged areas include Company, OAuth, OpenID Connect, Authentication, and Authorization.


  The Authlete catalog on APIs.io includes 1 Spectral governance ruleset.


  Authlete''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
plans:
- name: Authlete Plans Pricing
  plan_count: 4
  slug: authlete-plans-pricing
- name: Authlete Price Estimates
  plan_count: 0
  slug: authlete-price-estimates
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Authlete API Rules
  rule_count: 66
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 17
  slug: authlete-rules
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 56.0
    developer_ergonomics: 68.5
    discoverability: 73.2
    operational_transparency: 52.6
  previous_composite: 58.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/authlete/authlete-2026-07-25T201804.png
security:
- kind: authentication
  name: Authlete Authentication
  slug: authlete-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Authlete Domain Security
  slug: authlete-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Authlete Vulnerability Disclosure
  slug: authlete-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Drive an authorization-code flow at the runtime endpoints
  slug: authlete-authorization-code-flow
- name: Issue a verifiable credential (OID4VCI)
  slug: authlete-issue-verifiable-credential
- name: Provision a service and register a client
  slug: authlete-provision-service-and-client
slug: authlete
tags:
- Company
- OAuth
- OpenID Connect
- Authentication
- Authorization
- Identity
- API Security
- FAPI
- Verifiable Credentials
- CIBA
website: https://authlete.com
---
