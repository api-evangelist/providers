---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The AccountVerifications API from CertifID — 4 operation(s) for accountverifications.
  name: CertifID Account Verifications API
  slug: certifid-accountverifications-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The BankLookup API from CertifID — 2 operation(s) for banklookup.
  name: CertifID Bank Lookup API
  slug: certifid-banklookup-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The CollectRequest API from CertifID — 3 operation(s) for collectrequest.
  name: CertifID Collect Request API
  slug: certifid-collectrequest-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The ConfirmRequest API from CertifID — 3 operation(s) for confirmrequest.
  name: CertifID Confirm Request API
  slug: certifid-confirmrequest-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The Disbursements API from CertifID — 10 operation(s) for disbursements.
  name: CertifID Disbursements API
  slug: certifid-disbursements-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The IdentityRequest API from CertifID — 4 operation(s) for identityrequest.
  name: CertifID Identity Request API
  slug: certifid-identityrequest-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The Integration API from CertifID — 12 operation(s) for integration.
  name: CertifID Integration API
  slug: certifid-integration-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The Lenders API from CertifID — 2 operation(s) for lenders.
  name: CertifID Lenders API
  slug: certifid-lenders-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The Location API from CertifID — 2 operation(s) for location.
  name: CertifID Location API
  slug: certifid-location-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The PayoffOrdering API from CertifID — 6 operation(s) for payoffordering.
  name: CertifID Payoff Ordering API
  slug: certifid-payoffordering-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The SendRequest API from CertifID — 3 operation(s) for sendrequest.
  name: CertifID Send Request API
  slug: certifid-sendrequest-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The Test API from CertifID — 3 operation(s) for test.
  name: CertifID Test API
  slug: certifid-test-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The Underwriter API from CertifID — 1 operation(s) for underwriter.
  name: CertifID Underwriter API
  slug: certifid-underwriter-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The Users API from CertifID — 1 operation(s) for users.
  name: CertifID Users API
  slug: certifid-users-api
- baseURL: https://api.certifid.com
  baseurl_source: declared
  description: The WiringInstructions API from CertifID — 1 operation(s) for wiringinstructions.
  name: CertifID Wiring Instructions API
  slug: certifid-wiringinstructions-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CertifID V2 Account Verifications API
  slug: open-certifid-accountverifications-api
- collection_type: open
  name: CertifID V2 Bank Lookup API
  slug: open-certifid-banklookup-api
- collection_type: open
  name: CertifID V2 Collect Request API
  slug: open-certifid-collectrequest-api
- collection_type: open
  name: CertifID V2 Confirm Request API
  slug: open-certifid-confirmrequest-api
- collection_type: open
  name: CertifID V2 Disbursements API
  slug: open-certifid-disbursements-api
- collection_type: open
  name: CertifID V2 Identity Request API
  slug: open-certifid-identityrequest-api
- collection_type: open
  name: CertifID V2 Integration API
  slug: open-certifid-integration-api
- collection_type: open
  name: CertifID V2 Lenders API
  slug: open-certifid-lenders-api
- collection_type: open
  name: CertifID V2 Location API
  slug: open-certifid-location-api
- collection_type: open
  name: CertifID V2 Payoff Ordering API
  slug: open-certifid-payoffordering-api
- collection_type: open
  name: CertifID V2 Send Request API
  slug: open-certifid-sendrequest-api
- collection_type: open
  name: CertifID V2 Test API
  slug: open-certifid-test-api
- collection_type: open
  name: CertifID V2 Underwriter API
  slug: open-certifid-underwriter-api
- collection_type: open
  name: CertifID V2 Users API
  slug: open-certifid-users-api
- collection_type: open
  name: CertifID V2 APIs
  slug: open-certifid-v2-apis
- collection_type: open
  name: CertifID V2 Wiring Instructions API
  slug: open-certifid-wiringinstructions-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/certifid-capability-edges.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/certifid-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.certifid.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.certifid.com/swagger/index.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/certifid-v2-apis-openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/certifid-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/certifid-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/certifid-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/certifid-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/certifid-openid-configuration.json
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/certifid-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/certifid-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/certifid-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/certifid-certifid-v2-apis-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/certifid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/certifid-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.certifid.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/certifid-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.certifid.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/certifid-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/certifid-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CertifID
- group: start
  title: ''
  type: Login
  url: https://portal.certifid.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.certifid.com/request-a-demo
- group: operate
  title: ''
  type: Support
  url: https://www.certifid.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.certifid.com/resources/articles
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.certifid.com/company/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.certifid.com/company/privacy-policy
created: '2026-08-09'
description: CertifID is a wire fraud prevention, identity verification and funds protection platform for the real estate closing process, serving title agents, law firms, real estate agents, lenders and home buyers and sellers. Its products verify the identities of transaction participants, verify business and bank account ownership, securely share and confirm wiring instructions, order and verify mortgage payoffs, collect earnest money and cash-to-close payments, provide secure eSigning, and insure wires against fraud loss. CertifID exposes a public "CertifID V2 APIs" REST surface at api.certifid.com for third-party integrations, documented with a live OpenAPI 3.0.1 definition served from Swagger UI and secured with Auth0-backed OAuth 2.0.
image: https://cdn.prod.website-files.com/60a41ae959fbb36bd6808d6e/688ce259fd22b6b6905c812d_thumbnail-homepage.png
layout: provider
mcp_servers:
- description: CertifID operates NO Model Context Protocol server. This artifact is a CANDIDATE tool list that API Evangelist derived from the 57 operations in the live CertifID V2 APIs OpenAPI definition. It is a d
  name: CertifID MCP Server
  slug: certifid-mcp-server
modified: '2026-08-09'
name: CertifID
nav: Providers
network: true
overview: 'CertifID publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Account Verifications API, Bank Lookup API, Collect Request API, and 12 more. Tagged areas include Company, Wire Fraud Prevention, Real-Estate, Title Insurance, and Identity Verification.


  CertifID''s developer surface includes API reference, authentication, changelog, signup flow, support, engineering blog, and 23 more developer resources.'
random_paper: 2
scopes:
- name: Certifid Scopes
  scope_count: 12
  slug: certifid-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 44.8
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 42.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/certifid/refs/heads/main/screenshots/certifid-2026-08-17T080816.png
security:
- kind: authentication
  name: Certifid Authentication
  slug: certifid-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Certifid Domain Security
  slug: certifid-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: certifid
tags:
- Company
- Wire Fraud Prevention
- Real-Estate
- Title Insurance
- Identity Verification
- Business Verification
- Payments
- Fraud Prevention
- Escrow and Settlement
- Financial-Services
- Security
website: https://www.certifid.com/
---
