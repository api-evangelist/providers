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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Fitbark Agentic Access
  operation_count: 18
  slug: fitbark-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 1
apis:
- baseURL: https://app.fitbark.com/api/v2
  baseurl_source: declared
  description: Historical activity series, totals and time breakdowns
  name: FitBark Activity API
  slug: fitbark-activity-api
- baseURL: https://app.fitbark.com/api/v2
  baseurl_source: declared
  description: Dog profile, relationships and pictures
  name: FitBark Dog API
  slug: fitbark-dog-api
- baseURL: https://app.fitbark.com/api/v2
  baseurl_source: declared
  description: Daily goal management
  name: FitBark Goals API
  slug: fitbark-goals-api
- baseURL: https://app.fitbark.com/api/v2
  baseurl_source: declared
  description: OAuth 2.0 authorization and token endpoints
  name: FitBark OAuth API
  slug: fitbark-oauth-api
- baseURL: https://app.fitbark.com/api/v2
  baseurl_source: declared
  description: Authenticated user profile and relationships
  name: FitBark User API
  slug: fitbark-user-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FitBark Activity API
  slug: open-fitbark-activity-api
- collection_type: open
  name: FitBark Activity Dog API
  slug: open-fitbark-dog-api
- collection_type: open
  name: FitBark Activity Goals API
  slug: open-fitbark-goals-api
- collection_type: open
  name: FitBark Activity OAuth API
  slug: open-fitbark-oauth-api
- collection_type: open
  name: FitBark Activity User API
  slug: open-fitbark-user-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fitbark-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fitbark-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fitbark-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fitbark-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fitbark-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fitbark-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/fitbark-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fitbark-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fitbark-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fitbark.com/dev/
- group: docs
  title: ''
  type: Documentation
  url: https://documenter.getpostman.com/view/238826/2s8ZDbW1Gf
- group: docs
  title: ''
  type: APIReference
  url: https://documenter.getpostman.com/view/238826/2s8ZDbW1Gf
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/238826/2s8ZDbW1Gf
- group: operate
  title: ''
  type: Support
  url: https://help.fitbark.com/en/collections/3873135
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.fitbark.com/en/articles/6490193
- group: start
  title: ''
  type: SignUp
  url: https://forms.gle/tPAsmmEv9718a2ss7
- group: company
  title: ''
  type: Website
  url: https://fitbark.com/
created: '2026-07-17'
description: FitBark makes GPS and health-monitoring wearables for dogs and offers the FitBark Public API (v2), an OAuth 2.0 REST API that lets developers integrate FitBark activity and health data into third-party mobile and web applications. The API exposes a dog's activity series and totals, time-at-activity-level breakdowns, daily activity-point goals, similar-dog statistics, related users and dogs, and Base64/JPEG profile pictures. Approved developers receive a client_id and client_secret and authenticate with the OAuth 2.0 authorization_code and client_credentials grants (base host https://app.fitbark.com). FitBark was a Techstars portfolio company; this profile was enriched by API Evangelist from FitBark's official published developer documentation and Postman collection.
image: https://www.fitbark.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: FitBark MCP Server
  slug: fitbark-mcp-server
modified: '2026-07-19'
name: FitBark
nav: Providers
network: true
overview: 'FitBark publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Dog API, Goals API, and 2 more. Tagged areas include Company, Dogs, Pets, Wearables, and Activity Tracking.


  FitBark''s developer surface includes authentication, documentation, API reference, support, signup flow, and 13 more developer resources.'
random_paper: 4
scopes:
- name: Fitbark Scopes
  scope_count: 1
  slug: fitbark-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 54.0
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fitbark/refs/heads/main/screenshots/fitbark-2026-07-25T214628.png
security:
- kind: authentication
  name: Fitbark Authentication
  slug: fitbark-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Fitbark Domain Security
  slug: fitbark-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fitbark
tags:
- Company
- Dogs
- Pets
- Wearables
- Activity Tracking
- Health
- IoT
- Fitness
website: https://fitbark.com/
---
