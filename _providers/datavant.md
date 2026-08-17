---
access_model:
  confidence: high
  label: Enterprise · Partner onboarding
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - review
  - https://developer.datavant.com/openapi.json
  - https://aws.amazon.com/marketplace/pp/prodview-eolcfagze2ihw
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 63.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 28
  human_in_the_loop: 2
  name: Datavant Agentic Access
  operation_count: 54
  slug: datavant-agentic-access
  summary_line: 54 operations · 28 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: Datavant's REST API for identified patient medical record retrieval - the programmable side of Datavant Connect Retrieval (the ex-Ciox release-of-information business). Resource-oriented, JSON-encoded
  name: Datavant REST API
  slug: datavant-rest-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datavant-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/datavant-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datavant-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datavant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datavant.com/
- group: company
  title: ''
  type: Blog
  url: https://www.datavant.com/blog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.datavant.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datavant.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datavant.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datavant
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datavant
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datavant-llms.txt
- group: other
  title: ''
  type: ProductPage
  url: https://www.datavant.com/products/connect-linkage
- group: other
  title: ''
  type: ProductPage
  url: https://www.datavant.com/products/connect-privacy
- group: other
  title: ''
  type: ProductPage
  url: https://www.datavant.com/products/connect-retrieval
- group: other
  title: ''
  type: ProductPage
  url: https://www.datavant.com/products/insights-and-evidence-generation
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.datavant.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://developer.datavant.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.datavant.com/docs
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/datavant-rest-api-openapi.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@datavant.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datavant.com/terms-of-use
- group: start
  title: ''
  type: Login
  url: https://portal.datavant.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/datavant-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/datavant-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/datavant-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/datavant-rest-api-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datavant-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/datavant-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/datavant-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.datavant.com/about/privacy-compliance
- group: agent
  title: ''
  type: WellKnown
  url: well-known/datavant-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://auth.datavant.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/datavant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.datavant.com/report-vulnerabilities
- group: auth
  title: ''
  type: TrustCenter
  url: security/datavant-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/datavant-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/datavant-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/datavant-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-eolcfagze2ihw
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/datavant-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/datavant-mcp.yml
created: '2026-07-24'
description: 'Datavant is a United States health-data logistics company, formed from the 2021 merger of Datavant and Ciox Health, that connects and de-identifies healthcare data across a "network of networks" spanning 350+ real-world data partners, 80,000+ hospitals and clinics, and a majority of the largest US health systems. Its core capabilities are privacy-preserving record linkage using Datavant tokens, HIPAA Expert Determination and de-identification, medical record retrieval / release of information, and real-world evidence generation for life sciences, payers, providers, and government. Datavant publishes a real machine-readable contract for the retrieval side of that business: an OpenAPI 3.1.0 document for the Datavant REST API (36 paths, 54 operations, OAuth 2.0 client credentials, base https://api.datavant.io/v2) is served anonymously at https://developer.datavant.com/openapi.json, even though that host''s root returns HTTP 404. Access is still enterprise and contract-gated -
  there is no self-serve sign-up, no published pricing beyond a single AWS Marketplace listing, no published scopes or rate limits, and no FHIR CapabilityStatement. Home market is the United States.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: datavant-mcp.yml
  slug: datavant-mcpyml
modified: '2026-08-14'
name: Datavant
nav: Providers
network: true
overview: 'Datavant publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Healthcare, United States, Interoperability, Health Data, and De-Identification.


  Datavant''s developer surface includes authentication, engineering blog, documentation, API reference, support, changelog, CLI, and 36 more developer resources.'
plans:
- name: Datavant Plans Pricing
  plan_count: 1
  slug: datavant-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 0
  name: Datavant Rate Limits
  slug: datavant-rate-limits
scopes:
- name: Datavant Scopes
  scope_count: 0
  slug: datavant-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.0
  delta: 45.5
  facets:
    commercial_clarity: 81.6
    contract_quality: 50.1
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 13.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 66.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/datavant/refs/heads/main/screenshots/datavant-2026-07-25T211401.png
security:
- kind: authentication
  name: Datavant Authentication
  slug: datavant-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Datavant Domain Security
  slug: datavant-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Datavant Vulnerability Disclosure
  slug: datavant-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Datavant Trust Center
  slug: datavant-trust-center
  summary_line: FedRAMP Moderate, SOC 2 Type 2, HIPAA, FIPS 140-2
slug: datavant
tags:
- Healthcare
- United States
- Interoperability
- Health Data
- De-Identification
- Tokenization
- Real-World Data
- Record Retrieval
- Data Connectivity
- Life Sciences
- HIPAA
- Medical Records
- Release of Information
- Privacy
- OAuth 2.0
- Health Information Exchange
website: https://www.datavant.com/
---
