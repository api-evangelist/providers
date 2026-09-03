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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 2.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Flow Engineering exposes a GraphQL API for programmatic access to the Systems Graph (requirements, design artifacts, test cases, and integrations). The single GraphQL endpoint is served from api.flowe
  name: Flow GraphQL API
  slug: flow-graphql-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://flowengineering.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.flowengineering.com/sign-in
- group: start
  title: ''
  type: Login
  url: https://app.flowengineering.com/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://flowengineering.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://flowengineering.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flowengineering.com/privacy-and-cookie-policy
- group: auth
  title: ''
  type: Compliance
  url: https://flowengineering.com/security
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flow-engineering-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flow-engineering-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flow-engineering-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flow-engineering-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/flow-engineering-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flow-engineering-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flow-engineering-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flow-engineering-llms.txt
created: '2026-07-17'
description: Flow Engineering builds a requirements-management and AI-agent platform for hardware engineering teams. Its Systems Graph connects requirements, CAD, simulation, code, and test into a single system of record, and its AI agents continuously run impact analysis, check test coverage, verify compliance, and track mass, cost, and power budgets as designs change. Flow integrates with CAD, PLM, simulation, and developer tools (Onshape, GitHub, GitLab, Jira, Linear, Confluence, and more) and is used by hardware teams at companies such as Rivian, Joby, Skydio, and Isar Aerospace. The platform is backed by a GraphQL API at api.flowengineering.com secured with AWS Cognito OAuth2/OIDC, with API access included on paid plans. Flow Engineering is a portfolio company of EQT Ventures.
image: https://images.ctfassets.net/c2mtbunjxyfe/2QGR6p0asAXpvpfMUqWciO/0f4467ec22711446d218284b2aa4a5e3/open-graph.png
layout: provider
modified: '2026-07-19'
name: Flow Engineering
nav: Providers
network: true
overview: 'Flow Engineering publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software Development, Hardware Engineering, Requirements Management, and Systems Engineering.


  Flow Engineering''s developer surface includes signup flow, pricing, engineering blog, authentication, and 11 more developer resources.'
random_paper: 10
scopes:
- name: Flow Engineering Scopes
  scope_count: 4
  slug: flow-engineering-scopes
  summary_line: 4 scopes · authorizationCode/implicit
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.6
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flow-engineering/refs/heads/main/screenshots/flow-engineering-2026-07-25T214832.png
security:
- kind: authentication
  name: Flow Engineering Authentication
  slug: flow-engineering-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Flow Engineering Domain Security
  slug: flow-engineering-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Flow Engineering Trust Center
  slug: flow-engineering-trust-center
  summary_line: SOC 2 Type II, NIST 800-171, ITAR / EAR aligned, GDPR
slug: flow-engineering
tags:
- Company
- Software Development
- Hardware Engineering
- Requirements Management
- Systems Engineering
- MBSE
- AI Agents
- CAD
- Product Lifecycle Management
- GraphQL
website: https://flowengineering.com/
---
