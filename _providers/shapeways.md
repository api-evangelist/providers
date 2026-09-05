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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Shapeways Agentic Access
  operation_count: 10
  slug: shapeways-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.shapeways.com
  baseurl_source: declared
  description: Shipping options for a destination.
  name: Shapeways Cart API
  slug: shapeways-cart-api
- baseURL: https://api.shapeways.com
  baseurl_source: declared
  description: The Shapeways material catalog (40+ materials).
  name: Shapeways Materials API
  slug: shapeways-materials-api
- baseURL: https://api.shapeways.com
  baseurl_source: declared
  description: Upload, list, retrieve, and delete 3D models.
  name: Shapeways Models API
  slug: shapeways-models-api
- baseURL: https://api.shapeways.com
  baseurl_source: declared
  description: Place and track manufacturing orders.
  name: Shapeways Orders API
  slug: shapeways-orders-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shapeways Cart API
  slug: open-shapeways-cart-api
- collection_type: open
  name: Shapeways Cart Materials API
  slug: open-shapeways-materials-api
- collection_type: open
  name: Shapeways Cart Models API
  slug: open-shapeways-models-api
- collection_type: open
  name: Shapeways Cart Orders API
  slug: open-shapeways-orders-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/shapeways-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.shapeways.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shapeways.com/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.shapeways.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.shapeways.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.shapeways.com/
- group: company
  title: ''
  type: Blog
  url: https://www.shapeways.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Shapeways
- group: start
  title: ''
  type: SignUp
  url: https://auth.shapeways.com/register
- group: start
  title: ''
  type: Login
  url: https://auth.shapeways.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shapeways.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shapeways.com/privacy-statement
- group: auth
  title: ''
  type: Authentication
  url: authentication/shapeways-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shapeways-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shapeways-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shapeways-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/shapeways-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/shapeways-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shapeways-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shapeways-problem-types.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/shapeways-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shapeways-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shapeways-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shapeways-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shapeways-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.shapeways.com
created: '2026-07-17'
description: Shapeways is an on-demand 3D printing and additive-manufacturing platform that turns digital 3D models into physical parts across 12 additive technologies and 40+ materials, serving over one million customers in 180+ countries as a turnkey manufacturing partner for prototyping, production, and lifecycle support. Its OAuth 2.0 REST API (base URL https://api.shapeways.com) lets applications browse the material catalog, upload and manage 3D models, retrieve shipping options, and place and track manufacturing orders. Endpoints are versioned with a trailing /v1 path segment; official client libraries are published for PHP, Python, JavaScript, Go, and C++.
image: http://www.shapeways.com/wp-content/uploads/2021/03/SW-Thumbnail-Horizontal-1.jpg
layout: provider
modified: '2026-07-21'
name: Shapeways
nav: Providers
network: true
overview: 'Shapeways publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Cart API, Materials API, Models API, and 1 more. Tagged areas include Company, 3D Printing, Additive Manufacturing, Manufacturing, and Prototyping.


  Shapeways'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 15
scopes:
- name: Shapeways Scopes
  scope_count: 0
  slug: shapeways-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 12.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 31.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shapeways/refs/heads/main/screenshots/shapeways-2026-09-02T155109.png
security:
- kind: authentication
  name: Shapeways Authentication
  slug: shapeways-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Shapeways Domain Security
  slug: shapeways-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shapeways
tags:
- Company
- 3D Printing
- Additive Manufacturing
- Manufacturing
- Prototyping
- Hardware
- Fulfillment
- E-Commerce
website: https://www.shapeways.com
---
