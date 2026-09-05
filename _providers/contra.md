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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://contra.com/public-api
  baseurl_source: declared
  description: The Public Api API from Contra — 3 operation(s) for public api.
  name: Contra Public Api API
  slug: contra-public-api-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Contra Public Public Api API
  slug: open-contra-public-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/contra-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://contra.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/contra/contra-sdk
- group: company
  title: ''
  type: Blog
  url: https://contra.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://contra.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://contra.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contra.com/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contra.com/policies/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contra
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contra.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/contra-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contra-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/contra-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/contra-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/contra-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/contra-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/contra-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/contra-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/contra-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/contra-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/contra-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contra-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/contra-llms.txt
created: '2026-07-17'
description: Contra is an independent-first, commission-free freelance marketplace and professional network for the jobs and skills of the future, founded in 2019 by Ben Huffman and Gajus Kuizinas and backed by Cowboy Ventures, Unusual Ventures, and NEA. Independents build a portfolio, get discovered, and manage work from inquiry to contract to payment without platform commissions. For developers, Contra exposes a read-only Public API (programs, filters, and expert profiles under https://contra.com/public-api/, authenticated with an X-API-Key header), an attribute-driven Webflow SDK, a React UI-kit, and a hosted, OAuth 2.1-protected Model Context Protocol (MCP) server at https://contra.com/mcp (scope mcp:tools).
image: https://contra.com/static/opengraph-assets/v2/fallbacks/contra-fallback-open-graph-image.png
layout: provider
mcp_servers:
- description: ''
  name: Contra MCP
  slug: contra-mcp
modified: '2026-07-18'
name: Contra
nav: Providers
network: true
overview: 'Contra publishes 1 API on the [APIs.io](https://apis.io/) network: Public Api API. Tagged areas include Company, Future Of Work, Freelance Marketplace, Talent, and Hiring.


  Contra''s developer surface includes documentation, engineering blog, pricing, signup flow, authentication, and 19 more developer resources.'
random_paper: 17
scopes:
- name: Contra Scopes
  scope_count: 1
  slug: contra-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 39.5
    developer_ergonomics: 32.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 37.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contra/refs/heads/main/screenshots/contra-2026-07-25T210337.png
security:
- kind: authentication
  name: Contra Authentication
  slug: contra-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Contra Domain Security
  slug: contra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contra
tags:
- Company
- Future Of Work
- Freelance Marketplace
- Talent
- Hiring
- Professional Network
- MCP
- Developer API
website: https://contra.com
---
