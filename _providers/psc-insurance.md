---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 5
asyncapis:
- description: 'PSC Insurance publishes no event surface of its own: there is no webhook catalogue, no event reference, no AsyncAPI document and no streaming product on any pscinsurance.com.au host. One real, anonymo'
  name: PSC Insurance Content Lake — real-time listen stream
  slug: psc-insurance-content-lake-asyncapi
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/psc-insurance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/psc-insurance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pscinsurance.com.au/
- group: company
  title: ''
  type: Website
  url: https://www.pscbroking.co.nz/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/psc-insurance-brokers/
- group: company
  title: ''
  type: Blog
  url: https://www.pscinsurance.com.au/insights/
- group: operate
  title: ''
  type: Support
  url: https://www.pscinsurance.com.au/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pscinsurance.com.au/terms-of-use-statement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pscinsurance.com.au/privacy-statement/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.pscinsurance.com.au/.well-known/security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.pscinsurance.com.au/.well-known/security.txt
- group: auth
  title: ''
  type: Compliance
  url: https://www.pscinsurance.com.au/industry-memberships/
- group: other
  title: ''
  type: OpenIDConnectDiscovery
  url: https://login.pscinsurance.com.au/.well-known/openid-configuration
- group: agent
  title: ''
  type: WellKnown
  url: well-known/psc-insurance-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/psc-insurance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/psc-insurance-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/psc-insurance-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/psc-insurance-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/psc-insurance-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/psc-insurance-content-lake-asyncapi.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/psc-insurance-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/psc-insurance-llms.txt
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-25'
description: PSC Insurance is an Australian insurance broking and intermediary group operating as PSC Insurance Brokers across every Australian state and territory, with a New Zealand arm trading as PSC Broking. It places commercial and SME risk — business packages, construction and civil contracting, public liability, cyber, professional indemnity, directors and officers, management liability, commercial property and industrial special risks, strata, motor and fleet, agribusiness and livestock, workers compensation, financial lines and trade credit, and medical and allied health cover — advising clients rather than carrying underwriting risk itself. Formerly the ASX-listed PSC Insurance Group, the business now sits inside The Ardonagh Group's Australian distribution platform; its former corporate domain pscinsurancegroup.com.au 301-redirects to envest.com.au, and the broking site's security.txt names an @envest.com.au contact. Its API posture is honestly assessed as none. There is no public
  developer portal, no self-serve API, no published OpenAPI or Swagger definition, no GraphQL surface, no Postman collection, no SDK, no webhook catalog, and no ACORD, AL3, IVANS or agency-download reference anywhere on its public estate. Two machine-facing surfaces are confirmed live and neither is documented by PSC — an Auth0-hosted OpenID Connect identity endpoint at login.pscinsurance.com.au fronting a client/broker login wall, and the Sanity Content Lake dataset behind the marketing site, whose GROQ query, document, export and real-time listen endpoints all answer anonymously. Both are vendor infrastructure under PSC tenancy, not developer products. This matches the Australian market seam — the Consumer Data Right that opened banking and energy was designated for general insurance and then deferred, so no forcing function ever reached brokers, and integration here remains partner-gated and broker-platform mediated.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: PSC Insurance
nav: Providers
network: true
overview: 'PSC Insurance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, Broker, Insurance Brokerage, and Property and Casualty.


  The PSC Insurance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PSC Insurance''s developer surface includes engineering blog, support, authentication, and 20 more developer resources.'
random_paper: 147
scopes:
- name: Psc Insurance Scopes
  scope_count: 14
  slug: psc-insurance-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: thin
  composite: 38.5
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 39.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 80.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Psc Insurance Authentication
  slug: psc-insurance-authentication
  summary_line: openIdConnect/oauth2/http · 3 schemes
- kind: domain-security
  name: Psc Insurance Domain Security
  slug: psc-insurance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Psc Insurance Vulnerability Disclosure
  slug: psc-insurance-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: psc-insurance
tags:
- Insurance
- Australia
- Broker
- Insurance Brokerage
- Property and Casualty
- Commercial Insurance
- Cyber Insurance
- Intermediary
- Partner Gated
- No Public API
website: https://www.pscinsurance.com.au/
---
