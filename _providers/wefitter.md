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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Wefitter Agentic Access
  operation_count: 77
  slug: wefitter-agentic-access
  summary_line: 77 operations · 34 acting
api_count: 1
apis:
- description: The app API from WeFitter — 1 operation(s) for app.
  name: WeFitter app API
  slug: wefitter-app-api
- description: WeFitter API’s challenge engine will bring endless engagement to your platform. For more information about the possibilities in challenges please go to https://www.wefitter.com/en-us/features/gamifica
  name: WeFitter challenge API
  slug: wefitter-challenge-api
- description: Connections are the links between profiles and their wearables.
  name: WeFitter connection API
  slug: wefitter-connection-api
- description: The insights API from WeFitter — 1 operation(s) for insights.
  name: WeFitter insights API
  slug: wefitter-insights-api
- description: The loyalty API from WeFitter — 2 operation(s) for loyalty.
  name: WeFitter loyalty API
  slug: wefitter-loyalty-api
- description: 'Send a notification to all devices for the specified profiles The data will be sent to the client in the following format: ``` { "app": <app public id>, "title": <title>, "body": <body>, "link": <opti'
  name: WeFitter notification API
  slug: wefitter-notification-api
- description: 'Profiles are containers for wearables data. The profiles can be seen as an extension of users in a different system. Profiles are anonymous objects which can participate in teams and challenges. Keep '
  name: WeFitter profile API
  slug: wefitter-profile-api
- description: The team API from WeFitter — 5 operation(s) for team.
  name: WeFitter team API
  slug: wefitter-team-api
- description: <p> Before any calls can be made to wefitter, BasicAuth is needed to verify the identity of the requesting party. This call will result into a Bearer token which has administrator privileges and is va
  name: WeFitter token API
  slug: wefitter-token-api
artifact_total: 24
asyncapis:
- description: ''
  name: Wefitter Webhooks
  slug: wefitter-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WeFitter app API
  slug: open-wefitter-app-api
- collection_type: open
  name: WeFitter app challenge API
  slug: open-wefitter-challenge-api
- collection_type: open
  name: WeFitter app connection API
  slug: open-wefitter-connection-api
- collection_type: open
  name: WeFitter app insights API
  slug: open-wefitter-insights-api
- collection_type: open
  name: WeFitter app loyalty API
  slug: open-wefitter-loyalty-api
- collection_type: open
  name: WeFitter app notification API
  slug: open-wefitter-notification-api
- collection_type: open
  name: WeFitter app profile API
  slug: open-wefitter-profile-api
- collection_type: open
  name: WeFitter app team API
  slug: open-wefitter-team-api
- collection_type: open
  name: WeFitter app token API
  slug: open-wefitter-token-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.wefitter.com/en-us/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wefitter.com/en-us/developers/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wefitter.com/en-us/developers/getting-started/
- group: docs
  title: ''
  type: APIReference
  url: https://api.wefitter.com/api/v1.3/redoc/
- group: docs
  title: ''
  type: Guides
  url: https://www.wefitter.com/en-us/developers/guides/
- group: operate
  title: ''
  type: Support
  url: https://developers.wefitter.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.wefitter.com/en-us/resources/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.wefitter.com/en-us/developers/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wefitter
- group: start
  title: ''
  type: SignUp
  url: https://api.wefitter.com/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wefitter.com/en-us/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wefitter.com/en-us/privacy-policy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/wefitter-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/wefitter-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/wefitter-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wefitter-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wefitter-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wefitter-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/wefitter-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wefitter-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wefitter-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/wefitter-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wefitter-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wefitter-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wefitter-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/wefitter-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wefitter-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wefitter-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wefitter-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wefitter.com
created: '2026-07-17'
description: WeFitter is a health and fitness data platform ("one API to access wearable data, gamification and AI") operated by Thunderbyte.AI in Groningen, Netherlands. Its REST API aggregates health and activity data from 300+ wearables and fitness apps — Fitbit, Garmin, Google Fit, Apple Health, Withings, Polar, Oura, Whoop, Samsung Health, Huawei and more — into a single unified, deduplicated data model, and layers gamification (challenges, leaderboards, teams, points) and AI insights (biological age, recommendations) on top. Organizations use it to build corporate wellbeing, digital fitness, e-health and insurance solutions. WeFitter also ships mobile SDK bridges for Apple Health, Samsung Health and Android Health Connect.
image: https://www.wefitter.com/static/frontend/img/website/wefitter.png
layout: provider
mcp_servers:
- description: ''
  name: WeFitter MCP Server
  slug: wefitter-mcp-server
modified: '2026-07-21'
name: WeFitter
nav: Providers
network: true
overview: 'WeFitter publishes 9 APIs on the [APIs.io](https://apis.io/) network, including app API, challenge API, connection API, and 6 more. Tagged areas include Company, Health, Fitness, Wearables, and Health Data.


  The WeFitter catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  WeFitter''s developer surface includes documentation, getting-started guide, API reference, support, engineering blog, changelog, signup flow, and 24 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 59.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wefitter/refs/heads/main/screenshots/wefitter-2026-08-17T082909.png
security:
- kind: authentication
  name: Wefitter Authentication
  slug: wefitter-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wefitter Domain Security
  slug: wefitter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: wefitter
tags:
- Company
- Health
- Fitness
- Wearables
- Health Data
- Wellbeing
- Gamification
- Digital Health
- Insurance
- Activity Tracking
website: https://wefitter.com
---
