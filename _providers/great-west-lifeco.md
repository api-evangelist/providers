---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.4
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: Listed in the public API catalog of the Empower developer portal, operated by Great-West Lifeco's U.S. retirement subsidiary Empower. Marked "production" and categorized "financial", it returns partic
  name: Empower Balance API
  slug: empower-balance-api
- description: The authorization API for Empower's API suite, listed as "production" in the public Empower developer portal catalog. It generates bearer access tokens used to authorize calls to the other Empower API
  name: Empower OAuth 2.0 API
  slug: empower-oauth-2-0-api
- description: The production API gateway of Canada Life, Great-West Lifeco's Canadian operating brand, at api.canadalife.com. It publishes no documentation, but it does serve a real OpenID Connect discovery documen
  name: Canada Life API Gateway (OAuth 2.0 / OpenID Connect)
  slug: canada-life-api-gateway
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/great-west-lifeco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.greatwestlifeco.com/
- group: company
  title: ''
  type: About
  url: https://www.greatwestlifeco.com/who-we-are/about-us.html
- group: company
  title: ''
  type: News
  url: https://www.greatwestlifeco.com/news-and-events/news.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.empower.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.empower.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.empower.com/docs/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.empower.com/api-catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.empower.com/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://developer.empower.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.empower.com/docs/status-and-maintenance
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.empower.com/DevTerms
- group: start
  title: ''
  type: SignUp
  url: https://developer.empower.com/hybridauth-connect/authenticate/cognito
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greatwestlifeco.com/privacy-policy.html
- group: operate
  title: ''
  type: Roadmap
  url: https://www.empower.com/financial-professionals/experience/apis
- group: auth
  title: ''
  type: Compliance
  url: https://www.empower.com/financial-professionals/about-empower/cybersecurity
- group: auth
  title: ''
  type: TrustCenter
  url: security/great-west-lifeco-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/great-west-lifeco-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/great-west-lifeco-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/great-west-lifeco-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/great-west-lifeco-openid-configuration.json
- group: design
  title: ''
  type: Conventions
  url: conventions/great-west-lifeco-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/great-west-lifeco-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/great-west-lifeco-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/great-west-lifeco-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/great-west-lifeco-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/great-west-lifeco-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/great-west-lifeco-llms.txt
created: '2026-07-25'
description: 'Great-West Lifeco Inc. is a Winnipeg-headquartered international financial services holding company and a member of the Power Corporation group, and one of the largest life insurers in North America. It operates through Canada Life in Canada, the United Kingdom, the Isle of Man and Germany, through Irish Life in Ireland, and through Empower in the United States, spanning individual and group life, health and dental, disability and critical illness insurance, annuities and payout products, segregated funds and wealth management, employer-sponsored retirement recordkeeping, and life reinsurance. Its home market is Canada, where it is federally supervised by OSFI for prudential matters while market conduct is regulated province by province, and where no open-insurance mandate exists (Consumer-Driven Banking excludes insurance outright). Its API posture reflects that absence of a forcing function: the Great-West Lifeco corporate site and the Canadian consumer site canadalife.com
  publish no developer portal and no API documentation, and probes of developer/docs subdomains and /developers, /api, /developer, /partners and /integrations paths return no such surface. Two production API surfaces nevertheless exist inside the group, both partner-gated and unrelated to each other. Canada Life runs an Apigee gateway at api.canadalife.com that serves a real OpenID Connect discovery document anonymously - issuer, JWKS, token, revocation and userinfo endpoints, with the authorization endpoint deliberately published as "authorize-NOT-SUPPORTED" and an empty scopes_supported array - and whose error envelopes point to https://apimarketplace.canadalife.com, a digitalML-hosted API marketplace that does not resolve publicly. The U.S. retirement subsidiary Empower runs a genuine developer portal that lists two production APIs publicly while naming eight API products plus three coming soon on its marketing site, places every piece of reference documentation behind login, documents
  an x-api-key header with OAuth 2.0 client_credentials and private_key_jwt in support of FAPI, publishes release notes, a maintenance window and a mock-data sandbox, and issues credentials only after a reviewed access request. There is no downloadable OpenAPI anywhere, no public Postman collection, no SDK, no MCP server, no webhook or event catalog, and no ACORD, AL3 or IVANS reference on any public property in the group.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Great-West Lifeco
nav: Providers
network: true
overview: 'Great-West Lifeco publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Canada, Life Insurance, Health Insurance, and Employee Benefits.


  Great-West Lifeco''s developer surface includes product news, developer portal, documentation, API reference, getting-started guide, support, signup flow, and 21 more developer resources.'
random_paper: 18
scopes:
- name: Great West Lifeco Scopes
  scope_count: 0
  slug: great-west-lifeco-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 43.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 71.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/great-west-lifeco/refs/heads/main/screenshots/great-west-lifeco-2026-07-25T220257.png
security:
- kind: authentication
  name: Great West Lifeco Authentication
  slug: great-west-lifeco-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Great West Lifeco Domain Security
  slug: great-west-lifeco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Great West Lifeco Trust Center
  slug: great-west-lifeco-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, NIST 800-53, NIST CSF, OWASP
slug: great-west-lifeco
tags:
- Insurance
- Canada
- Life Insurance
- Health Insurance
- Employee Benefits
- Retirement
- Wealth Management
- Reinsurance
- Annuities
- Partner Gated
website: https://www.greatwestlifeco.com/
---
