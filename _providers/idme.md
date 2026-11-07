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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: ID.me's OpenID Connect and OAuth 2.0 identity provider. Supports the authorization code flow (with PKCE), refresh tokens, encrypted ID tokens and userinfo, and returns verified identity attributes and
  name: ID.me OpenID Connect & OAuth 2.0 API
  slug: id-me-openid-connect-oauth-2-0-api
- description: 'ID.me''s REST Services API for orchestrating identity verification: create and manage verifications, verify phone possession and identity via telecom endpoints, and verify identity documents (driver''s '
  name: ID.me Services API
  slug: id-me-services-api
- baseURL: https://services.idmelabs.com
  baseurl_source: declared
  description: 'ID.me applications API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: ID.me applications API
  slug: applications-api
- baseURL: https://api.id.me
  baseurl_source: declared
  description: 'ID.me core API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: ID.me core API
  slug: core-api
- baseURL: https://api.id.me
  baseurl_source: declared
  description: 'ID.me document passback API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: ID.me document passback API
  slug: document-passback-api
- baseURL: https://services.idmelabs.com
  baseurl_source: declared
  description: 'ID.me services API as documented publicly: 14 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: ID.me services API
  slug: services-api
artifact_total: 33
asyncapis:
- description: ''
  name: Idme Services Webhooks
  slug: idme-services-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/idme/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/idme/rules/idme-rules.yml
  title: ''
  type: Spectral
  url: rules/idme-rules.yml
- group: design
  href: https://artifacts.apis.io/idme/json-ld/idme-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/idme-context.jsonld
- group: design
  href: https://artifacts.apis.io/idme/vocabulary/idme-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/idme-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/idme/data-model/idme-data-model.yml
  title: ''
  type: DataModel
  url: data-model/idme-data-model.yml
- group: auth
  href: https://artifacts.apis.io/idme/security/idme-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/idme-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/idme/hosts/idme-hosts.yml
  title: ''
  type: Hosts
  url: hosts/idme-hosts.yml
- group: build
  href: https://artifacts.apis.io/idme/integrations/idme-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/idme-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/idme/vendors/idme-vendors.yml
  title: ''
  type: Vendors
  url: vendors/idme-vendors.yml
- group: auth
  href: https://artifacts.apis.io/idme/security/idme-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/idme-trust-center.yml
- group: company
  title: ''
  type: Blog
  url: https://network.id.me/insights-home/
- group: company
  title: ''
  type: BlogRSS
  url: https://network.id.me/feed/
- group: company
  title: ''
  type: Website
  url: https://www.id.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.id.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.id.me
- group: docs
  title: ''
  type: APIReference
  url: https://docs.id.me/services-api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.id.me/home
- group: operate
  title: ''
  type: Support
  url: https://docs.id.me/integrations/deploy-and-monitor/help
- group: operate
  title: ''
  type: StatusPage
  url: https://status.id.me
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IDme
- group: start
  title: ''
  type: SignUp
  url: https://developers.id.me
- group: agent
  href: https://artifacts.apis.io/idme/llms/idme-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/idme-llms.txt
- group: agent
  href: https://artifacts.apis.io/idme/well-known/idme-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/idme-well-known.yml
- group: auth
  href: https://artifacts.apis.io/idme/well-known/idme-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/idme-security.txt
- group: other
  href: https://artifacts.apis.io/idme/well-known/idme-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/idme-openid-configuration.json
- group: auth
  href: https://artifacts.apis.io/idme/authentication/idme-authentication.yml
  title: ''
  type: Authentication
  url: authentication/idme-authentication.yml
- group: auth
  href: https://artifacts.apis.io/idme/scopes/idme-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/idme-scopes.yml
- group: agent
  href: https://artifacts.apis.io/idme/mcp/idme-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/idme-mcp.yml
- group: design
  href: https://artifacts.apis.io/idme/errors/idme-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/idme-problem-types.yml
- group: design
  href: https://artifacts.apis.io/idme/lifecycle/idme-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/idme-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/idme/conventions/idme-conventions.yml
  title: ''
  type: Conventions
  url: conventions/idme-conventions.yml
- group: design
  href: https://artifacts.apis.io/idme/conformance/idme-conformance.yml
  title: ''
  type: Conformance
  url: conformance/idme-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.id.me/guides/learn-more/digital-wallet/nist-ial-2
- group: start
  href: https://artifacts.apis.io/idme/sandbox/idme-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/idme-sandbox.yml
- group: build
  href: https://artifacts.apis.io/idme/packages/idme-packages.yml
  title: ''
  type: Packages
  url: packages/idme-packages.yml
- group: build
  href: https://artifacts.apis.io/idme/packages/idme-packages.yml
  title: ''
  type: SDKs
  url: packages/idme-packages.yml
- group: design
  href: https://artifacts.apis.io/idme/components/idme-components.yml
  title: ''
  type: Components
  url: components/idme-components.yml
- group: design
  href: https://artifacts.apis.io/idme/asyncapi/idme-services-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/idme-services-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/idme/security/idme-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/idme-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/idme/security/idme-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/idme-vulnerability-disclosure.yml
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://docs.id.me/mcp
  - status: 200
    url: https://www.id.me
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: ID.me is a digital identity network that provides NIST 800-63-3 IAL2/AAL2 identity verification, single sign-on, and group affiliation (community) verification for government agencies, healthcare, and commercial partners. For developers, ID.me exposes an OpenID Connect and OAuth 2.0 identity provider (authorization code flow with PKCE, plus SAML 2.0 federation), a REST Services API for telecom and document verification, an Applications API, a Document Passback API, and a Shared Signals Framework (SSF) event stream for fraud and verification signals. Native iOS and Android SDKs, a button widget, conversion tracking, and multi-language sample code round out the developer surface, letting relying parties add strong identity proofing and attribute exchange to any application or IAM platform (Okta, Keycloak, Entra, PingOne, AWS Cognito).
image: https://avatars.githubusercontent.com/u/295660?v=4
json_schemas:
- name: GetApiPublicV3AttributesJsonResponse
  property_count: 3
  slug: idme-get-api-public-v3-attributes-json-response
- name: GetApiV2DocumentPasscardVerifyResponse
  property_count: 4
  slug: idme-get-api-v2-document-passcard-verify-response
- name: GetApiV2DocumentPassportVerifyResponse
  property_count: 4
  slug: idme-get-api-v2-document-passport-verify-response
- name: GetApiV2ProductTransactionidResponse
  property_count: 4
  slug: idme-get-api-v2-product-transactionid-response
- name: GetV1DomainsDomainResponse
  property_count: 8
  slug: idme-get-v1-domains-domain-response
- name: GetV1SectorsIdStructuresResponse
  property_count: 5
  slug: idme-get-v1-sectors-id-structures-response
- name: PatchV1OrganizationsUuidRequest
  property_count: 8
  slug: idme-patch-v1-organizations-uuid-request
- name: PatchV1OrganizationsUuidResponse
  property_count: 5
  slug: idme-patch-v1-organizations-uuid-response
- name: PostApiAuthV1CredentialsUuidCheckResponse
  property_count: 1
  slug: idme-post-api-auth-v1-credentials-uuid-check-response
- name: PostApiPublicV3DocumentsDocumenttokenResponse
  property_count: 1
  slug: idme-post-api-public-v3-documents-documenttoken-response
- name: PostApiPublicV3DocumentsRefreshDocumenttokenResponse
  property_count: 1
  slug: idme-post-api-public-v3-documents-refresh-documenttoken-response
- name: PostApiV2TelecomIdentityRequest
  property_count: 5
  slug: idme-post-api-v2-telecom-identity-request
- name: PostApiV2TelecomPossessionSmsConfirmRequest
  property_count: 3
  slug: idme-post-api-v2-telecom-possession-sms-confirm-request
- name: PostApiV2TelecomPossessionSmsSendRequest
  property_count: 4
  slug: idme-post-api-v2-telecom-possession-sms-send-request
- name: PostV1DomainsResponse
  property_count: 6
  slug: idme-post-v1-domains-response
- name: PostV1OrganizationsOrganizationuuidApplicationsRequest
  property_count: 11
  slug: idme-post-v1-organizations-organizationuuid-applications-request
jsonld:
- class_count: 36
  name: Idme Context
  property_count: 54
  slug: idme-context
layout: provider
mcp_servers:
- description: Official hosted MCP server for the ID.me developer documentation, advertised in docs.id.me/llms.txt for AI client integration (Claude Code, Cursor, etc.). Surfaces the ID.me integration docs — OIDC/OA
  name: ID.me Developer Docs
  slug: id-me-developer-docs
modified: '2026-10-06'
name: ID.me
nav: Providers
network: true
overview: 'ID.me is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including applications API, core API, document passback API, and 3 more. Tagged areas include Company, Identity, Identity Verification, Authentication, and OpenID Connect.


  The ID.me catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  ID.me''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, authentication, and 33 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ID.me API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: idme-rules
scopes:
- name: Idme Scopes
  scope_count: 11
  slug: idme-scopes
  summary_line: 11 scopes · authorizationCode
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 33.5
    developer_ergonomics: 73.2
    discoverability: 80.0
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 48.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 37.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/idme/idme-2026-08-17T123853.png
security:
- kind: authentication
  name: Idme Authentication
  slug: idme-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Idme Domain Security
  slug: idme-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Idme Vulnerability Disclosure
  slug: idme-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Idme Trust Center
  slug: idme-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR, FIPS 140
skill_count: 2
skills:
- name: idme-document-verification
  slug: idme-document-verification
- name: idme-telecom-phone-verification
  slug: idme-telecom-phone-verification
slug: idme
tags:
- Company
- Identity
- Identity Verification
- Authentication
- OpenID Connect
- OAuth
- SAML
- SSO
- Digital Identity
- KYC
- Fraud Prevention
- Government
- Identity Federation
website: https://www.id.me
---
