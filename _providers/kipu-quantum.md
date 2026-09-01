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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API and Python SDK for the Kipu Quantum Hub — submit quantum-classical workflows, run pre-built quantum services against 20+ backends, and manage jobs. Authenticated with API keys and OAuth2/OIDC
  name: Kipu Quantum Hub API
  slug: kipu-quantum-hub-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kipu-quantum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kipu-quantum.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.kipu-quantum.com
- group: docs
  title: ''
  type: Documentation
  url: https://kipu-quantum.com/platform
- group: commercial
  title: ''
  type: Pricing
  url: https://kipu-quantum.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://login.hub.kipu-quantum.com/realms/planqk/protocol/openid-connect/registrations
- group: start
  title: ''
  type: Login
  url: https://login.hub.kipu-quantum.com/realms/planqk/protocol/openid-connect/auth
- group: company
  title: ''
  type: Blog
  url: https://kipu-quantum.com/blog
- group: build
  title: ''
  type: SDKs
  url: packages/kipu-quantum-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/kipu-quantum-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kipu-quantum-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/kipu-quantum-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/kipu-quantum-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kipu-quantum-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kipu-quantum-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kipu-quantum-llms.txt
created: '2026-07-17'
description: 'Kipu Quantum GmbH is a Berlin-based deep-tech company building application-specific, hardware-efficient quantum algorithms and delivering them as a managed cloud platform. Its flagship product, the Kipu Quantum Hub (hub.kipu-quantum.com), is an end-to-end platform for industrial quantum computing: it provides unified access to 20+ quantum backends (IBM Quantum, IonQ, IQM, QuEra, Rigetti, Pasqal, Azure Quantum), a visual workflow designer for quantum-classical pipelines, an AI "matchmaker" (Tinkuq) that translates a business problem into a solver configuration, and a Quantum Service Store of pre-built solvers (Miray, Rimay, Iskay, HUK) targeting optimization, portfolio mix, network routing, and classification. Developers automate runs and integrate via a Python SDK, REST API, and CLI, authenticating with API keys and OAuth2/OIDC (Keycloak, PlanQK realm). Founded and led by Prof. Dr. Enrique Solano and Dr. Tobias Grab. Backed by HV Capital and surfaced into the API Evangelist
  network via VC-portfolio enrichment.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kipu-quantum.png
layout: provider
modified: '2026-07-19'
name: Kipu Quantum
nav: Providers
network: true
overview: 'Kipu Quantum publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Deep Tech, Quantum Computing, Quantum, and Artificial Intelligence.


  Kipu Quantum''s developer surface includes documentation, pricing, signup flow, engineering blog, authentication, and 11 more developer resources.'
random_paper: 5
scopes:
- name: Kipu Quantum Scopes
  scope_count: 12
  slug: kipu-quantum-scopes
  summary_line: 12 scopes · authorizationCode/clientCredentials
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    conformance: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kipu-quantum/refs/heads/main/screenshots/kipu-quantum-2026-07-25T223849.png
security:
- kind: authentication
  name: Kipu Quantum Authentication
  slug: kipu-quantum-authentication
  summary_line: apiKey/oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Kipu Quantum Domain Security
  slug: kipu-quantum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kipu-quantum
tags:
- Company
- Deep Tech
- Quantum Computing
- Quantum
- Artificial Intelligence
- Optimization
- Developer Platform
- SDK
- REST API
- Germany
website: https://kipu-quantum.com
---
