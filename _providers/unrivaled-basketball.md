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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.sportradar.com/unrivaled
  baseurl_source: declared
  description: The Games API from Unrivaled Basketball — 5 operation(s) for games.
  name: Unrivaled Basketball Games API
  slug: unrivaled-basketball-games-api
- baseURL: https://api.sportradar.com/unrivaled
  baseurl_source: declared
  description: The League API from Unrivaled Basketball — 7 operation(s) for league.
  name: Unrivaled Basketball League API
  slug: unrivaled-basketball-league-api
- baseURL: https://api.sportradar.com/unrivaled
  baseurl_source: declared
  description: The Players API from Unrivaled Basketball — 1 operation(s) for players.
  name: Unrivaled Basketball Players API
  slug: unrivaled-basketball-players-api
- baseURL: https://api.sportradar.com/unrivaled
  baseurl_source: declared
  description: The Seasons API from Unrivaled Basketball — 4 operation(s) for seasons.
  name: Unrivaled Basketball Seasons API
  slug: unrivaled-basketball-seasons-api
- baseURL: https://api.sportradar.com/unrivaled
  baseurl_source: declared
  description: The Series API from Unrivaled Basketball — 2 operation(s) for series.
  name: Unrivaled Basketball Series API
  slug: unrivaled-basketball-series-api
- baseURL: https://api.sportradar.com/unrivaled
  baseurl_source: declared
  description: The Teams API from Unrivaled Basketball — 1 operation(s) for teams.
  name: Unrivaled Basketball Teams API
  slug: unrivaled-basketball-teams-api
- baseURL: https://api.sportradar.com/unrivaled
  baseurl_source: declared
  description: The Tournaments API from Unrivaled Basketball — 3 operation(s) for tournaments.
  name: Unrivaled Basketball Tournaments API
  slug: unrivaled-basketball-tournaments-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unrivaled Games API
  slug: open-unrivaled-basketball-games-api
- collection_type: open
  name: Unrivaled Games League API
  slug: open-unrivaled-basketball-league-api
- collection_type: open
  name: Unrivaled Games Players API
  slug: open-unrivaled-basketball-players-api
- collection_type: open
  name: Unrivaled Games Seasons API
  slug: open-unrivaled-basketball-seasons-api
- collection_type: open
  name: Unrivaled Games Series API
  slug: open-unrivaled-basketball-series-api
- collection_type: open
  name: Unrivaled Games Teams API
  slug: open-unrivaled-basketball-teams-api
- collection_type: open
  name: Unrivaled Games Tournaments API
  slug: open-unrivaled-basketball-tournaments-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unrivaled-basketball-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unrivaled-basketball-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.unrivaled.basketball/
- group: company
  title: ''
  type: Blog
  url: https://www.unrivaled.basketball/news
- group: operate
  title: ''
  type: Support
  url: https://www.unrivaled.basketball/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unrivaled.basketball/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unrivaled.basketball/legal/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sportradar.com/basketball/reference/unrivaled-overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sportradar.com/basketball/reference/unrivaled-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sportradar.com/basketball/docs/unrivaled-ig-api-basics
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/17203961-e11f651d-fb09-4326-a96b-71a4c41d655d?action=collection%2Ffork&collection-url=entityId%3D17203961-e11f651d-fb09-4326-a96b-71a4c41d655d%26entityType%3Dcollection%26workspaceId%3Da6193b92-ee53-4979-bbfe-7ffdc589c3fc
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unrivaled-basketball-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unrivaled-basketball-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unrivaled-basketball-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unrivaled-basketball-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unrivaled-basketball-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unrivaled-basketball-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/unrivaled-basketball-unrivaled-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/unrivaled-basketball-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unrivaled-basketball-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unrivaled-basketball-well-known.yml
created: '2026-07-17'
description: Unrivaled is a U.S. professional women's 3x3 basketball league co-founded by Napheesa Collier and Breanna Stewart, playing a condensed winter season with six clubs and a midseason 1-on-1 tournament. The league's official real-time data API — the Unrivaled API v8 — is operated by Sportradar as the league's Official Data Provider, delivering schedules, standings, rosters, live scores, play-by-play (including the Elam Ending and weighted free throws), injuries, transfers, and season statistics in JSON or XML.
image: https://www.unrivaled.basketball/images/icon-mask.png
layout: provider
modified: '2026-07-21'
name: Unrivaled Basketball
nav: Providers
network: true
overview: 'Unrivaled Basketball publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Games API, League API, Players API, and 4 more. Tagged areas include Company, Consumer, Basketball, Sports, and Womens Sports.


  Unrivaled Basketball''s developer surface includes authentication, engineering blog, support, documentation, API reference, getting-started guide, changelog, and 15 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 53.4
    developer_ergonomics: 61.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 39.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unrivaled-basketball/refs/heads/main/screenshots/unrivaled-basketball-2026-08-17T082632.png
security:
- kind: authentication
  name: Unrivaled Basketball Authentication
  slug: unrivaled-basketball-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Unrivaled Basketball Domain Security
  slug: unrivaled-basketball-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unrivaled-basketball
tags:
- Company
- Consumer
- Basketball
- Sports
- Womens Sports
- Sports Data
- Media
- League
website: https://www.unrivaled.basketball/
---
