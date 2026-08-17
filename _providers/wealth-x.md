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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-17'
api_count: 7
apis:
- description: Retrieve individual and company wealth-intelligence dossiers.
  name: Wealth-X Dossiers API
  slug: wealth-x-dossiers-api
- description: Reference / lookup data used to build searches.
  name: Wealth-X Reference API
  slug: wealth-x-reference-api
- description: Advanced search across the Wealth-X database.
  name: Wealth-X Search API
  slug: wealth-x-search-api
- description: 'GraphQL search and enrichment across Altrata person and organization profiles, including the wealth dataset that Wealth-X contributes — net worth, wealth tier, wealth assets, charitable and political '
  name: Altrata Profile API
  slug: altrata-profile-api
- description: 'GraphQL API returning ranked relationship paths from the authenticated user to a target person or organization (1st and 2nd degree), plus the full first-degree network of any person. The successor to '
  name: Altrata Relationship API
  slug: altrata-relationship-api
- description: GraphQL API for leadership and organizational events — primarily executive role announcements — queried by person or organization altrataId and sorted by effective date, newest first. A polled query A
  name: Altrata Events API
  slug: altrata-events-api
- description: 'Asynchronous bulk matching of a customer dataset against the Altrata dataset. Submit a personsMatch or organizations mutation, receive a requestId, poll until matched, then page the results as unique '
  name: Altrata Matching API
  slug: altrata-matching-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wealth-X Connect Dossiers API
  slug: open-wealth-x-dossiers-api
- collection_type: open
  name: Wealth-X Connect Dossiers Reference API
  slug: open-wealth-x-reference-api
- collection_type: open
  name: Wealth-X Connect Dossiers Search API
  slug: open-wealth-x-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/wealth-x-connect-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wealthx.com/api/main.html
- group: docs
  title: ''
  type: Documentation
  url: https://developers.wealthx.com/docs/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://developers.wealthx.com/docs/api/index.html
- group: start
  title: ''
  type: Portal
  url: https://wealthx.com/products/api
- group: operate
  title: ''
  type: Support
  url: https://wealthx.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wealthx.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wealthx.com/terms-of-use
- group: build
  title: ''
  type: Postman
  url: https://developers.wealthx.com/api/Wealth-X%20API%20Samples.postman_collection.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wealth-x-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wealth-x-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wealth-x-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wealth-x-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wealth-x-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wealth-x-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wealth-x-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wealth-x-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wealth-x-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/wealth-x-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wealth-x-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wealth-x-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wealth-x-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wealth-x-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wealth-x-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/wealth-x-trust-center.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wealth-x-well-known.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/wealth-x-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wealth-x-llms-published.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.altrata.com/service-user-credentials
- group: start
  title: ''
  type: Login
  url: https://app.altrata.com/login
- group: company
  title: ''
  type: Blog
  url: https://altrata.com/resources/types/articles
created: '2026-07-17'
description: Wealth-X, an Altrata company founded in 2010, provides curated wealth intelligence on ultra-high-net-worth (UHNW) and very-high-net-worth (VHNW) individuals and their privately held companies. Its Connect API delivers Wealth-X dossiers — net worth, careers, interests, philanthropy and relationship networks — plus advanced prospect search and bulk/incremental sync directly into a subscriber's CRM or data platform. Wealth-X serves financial services, luxury, nonprofit and education clients for prospect qualification, relationship intelligence and compliance. Altrata's developer documentation names Wealth-X as a legacy product migrating to the unified Altrata GraphQL platform (Profile, Relationship, Events and Matching APIs), which also fronts a live OAuth-protected remote MCP server.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wealth-x.png
layout: provider
mcp_servers:
- description: ''
  name: wealth-x-mcp.yml
  slug: wealth-x-mcpyml
modified: '2026-08-14'
name: Wealth-X
nav: Providers
network: true
overview: 'Wealth-X publishes 3 APIs on the [APIs.io](https://apis.io/) network: Dossiers API, Reference API, and Search API. Tagged areas include Company, Wealth Intelligence, Data, UHNW, and Prospecting.


  Wealth-X''s developer surface includes documentation, API reference, developer portal, support, authentication, changelog, getting-started guide, and 25 more developer resources.'
plans:
- name: Wealth X Plans Pricing
  plan_count: 5
  slug: wealth-x-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Wealth X Rate Limits
  slug: wealth-x-rate-limits
scopes:
- name: Wealth X Scopes
  scope_count: 0
  slug: wealth-x-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  delta: 23.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 15.3
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 27.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Wealth X Authentication
  slug: wealth-x-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Wealth X Domain Security
  slug: wealth-x-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wealth X Trust Center
  slug: wealth-x-trust-center
  summary_line: SOC 2, CCPA Validation
slug: wealth-x
tags:
- Company
- Wealth Intelligence
- Data
- UHNW
- Prospecting
- Financial Services
- CRM
- People Data
- Altrata
- GraphQL
- MCP
- Wealth Screening
website: https://developers.wealthx.com/api/main.html
---
