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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 14.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The Interac Hub is an HTTP API that simplifies digital identity verification. Relying parties obtain verified identity data through financial-institution authentication (Interac Verification Service, '
  name: Interac Hub Verification API
  slug: interac-hub-verification-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/interac-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.interac.ca/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://innovation.interac.ca/
- group: docs
  title: ''
  type: Documentation
  url: https://documents.hub-verify.innovation.interac.ca/docs/welcome
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Interac
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/interac-corp/
- group: company
  title: ''
  type: Blog
  url: https://www.interac.ca/en/content-category/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.interac.ca/en/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.interac.ca/en/legal/
- group: start
  title: ''
  type: GettingStarted
  url: https://documents.hub-verify.innovation.interac.ca/docs/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://innovation.interac.ca/support/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/interac-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/interac-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/interac-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/interac-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/interac-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/interac-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/interac-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/interac-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/interac-llms.txt
created: '2026-07-23'
description: Interac Corp. is Canada's domestic payments and digital verification network, founded in 1984 as the Interac Association and reorganized as a for-profit corporation in 2018 (through the merger of Interac Association and Acxsys). Headquartered in Toronto and owned by a consortium of Canadian financial institutions and payment processors, Interac is shared national payment infrastructure rather than a chartered bank — it has no Schedule I / Schedule II banking charter. It operates the Interac Debit domestic debit network, Interac e-Transfer (used by roughly 88% of Canadians), and Interac verification / digital identity services, connecting 300+ financial institutions and processing on the order of 18.6 million transactions a day. As one of the core Canadian rails alongside Payments Canada, Interac runs the Interac Innovation Hub developer program. Its most openly documented public API surface is the Interac Hub Verification Service, an HTTP identity-verification API built on OAuth
  2.0 and OpenID Connect (Authorization Code Grant with Pushed Authorization Requests); a self-serve sandbox is available through the Hub Verification developer portal, while full production access and other products (Business Request Money, Interac Direct) are partner-gated behind a commercial relationship with an issuing financial institution.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Interac
nav: Providers
network: true
overview: 'Interac publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Payments, Canada, Interac, and Digital Identity.


  Interac''s developer surface includes documentation, engineering blog, getting-started guide, support, authentication, sandbox, and 15 more developer resources.'
random_paper: 7
scopes:
- name: Interac Scopes
  scope_count: 3
  slug: interac-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.1
  provenance:
    conformance: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interac/refs/heads/main/screenshots/interac-2026-07-25T222655.png
security:
- kind: authentication
  name: Interac Authentication
  slug: interac-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Interac Domain Security
  slug: interac-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: interac
tags:
- Financial-Services
- Payments
- Canada
- Interac
- Digital Identity
- Verification
- Open Banking
- Consumer-Driven Banking
- Infrastructure
website: https://www.interac.ca/
---
