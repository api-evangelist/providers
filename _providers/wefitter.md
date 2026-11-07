---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Wefitter Agentic Access
  operation_count: 77
  slug: wefitter-agentic-access
  summary_line: 77 operations · 34 acting
api_count: 1
apis:
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: The app API from WeFitter — 1 operation(s) for app.
  name: WeFitter App API
  slug: wefitter-app-api
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: WeFitter API’s challenge engine will bring endless engagement to your platform. For more information about the possibilities in challenges please go to https://www.wefitter.com/en-us/features/gamifica
  name: WeFitter Challenge API
  slug: wefitter-challenge-api
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: Connections are the links between profiles and their wearables.
  name: WeFitter Connection API
  slug: wefitter-connection-api
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: The insights API from WeFitter — 1 operation(s) for insights.
  name: WeFitter Insights API
  slug: wefitter-insights-api
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: The loyalty API from WeFitter — 2 operation(s) for loyalty.
  name: WeFitter Loyalty API
  slug: wefitter-loyalty-api
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: 'Send a notification to all devices for the specified profiles The data will be sent to the client in the following format: ``` { "app": <app public id>, "title": <title>, "body": <body>, "link": <opti'
  name: WeFitter Notification API
  slug: wefitter-notification-api
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: 'Profiles are containers for wearables data. The profiles can be seen as an extension of users in a different system. Profiles are anonymous objects which can participate in teams and challenges. Keep '
  name: WeFitter Profile API
  slug: wefitter-profile-api
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: The team API from WeFitter — 5 operation(s) for team.
  name: WeFitter Team API
  slug: wefitter-team-api
- baseURL: https://api.wefitter.com/api/v1.3
  baseurl_source: declared
  description: <p> Before any calls can be made to wefitter, BasicAuth is needed to verify the identity of the requesting party. This call will result into a Bearer token which has administrator privileges and is va
  name: WeFitter Token API
  slug: wefitter-token-api
artifact_total: 26
asyncapis:
- description: ''
  name: Wefitter Webhooks
  slug: wefitter-webhooks
collections:
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
- group: other
  href: https://artifacts.apis.io/wefitter/capabilities/wefitter-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/wefitter-capability-edges.yml
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
  href: https://artifacts.apis.io/wefitter/openapi/_original/wefitter-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/wefitter-openapi-original.json
- group: other
  href: https://artifacts.apis.io/wefitter/overlays/wefitter-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wefitter-openapi-overlay.yaml
- group: build
  href: https://artifacts.apis.io/wefitter/packages/wefitter-packages.yml
  title: ''
  type: Packages
  url: packages/wefitter-packages.yml
- group: build
  href: https://artifacts.apis.io/wefitter/packages/wefitter-packages.yml
  title: ''
  type: SDKs
  url: packages/wefitter-packages.yml
- group: agent
  href: https://artifacts.apis.io/wefitter/mcp/wefitter-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/wefitter-mcp.yml
- group: agent
  href: https://artifacts.apis.io/wefitter/llms/wefitter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wefitter-llms.txt
- group: design
  href: https://artifacts.apis.io/wefitter/conformance/wefitter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wefitter-conformance.yml
- group: design
  href: https://artifacts.apis.io/wefitter/errors/wefitter-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wefitter-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wefitter/lifecycle/wefitter-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wefitter-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/wefitter/changelog/wefitter-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wefitter-changelog.yml
- group: design
  href: https://artifacts.apis.io/wefitter/conventions/wefitter-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wefitter-conventions.yml
- group: design
  href: https://artifacts.apis.io/wefitter/data-model/wefitter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wefitter-data-model.yml
- group: design
  href: https://artifacts.apis.io/wefitter/asyncapi/wefitter-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wefitter-webhooks.yml
- group: design
  href: https://artifacts.apis.io/wefitter/components/wefitter-components.yml
  title: ''
  type: Components
  url: components/wefitter-components.yml
- group: agent
  href: https://artifacts.apis.io/wefitter/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/wefitter/security/wefitter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wefitter-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/wefitter/agentic-access/wefitter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wefitter-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/wefitter/authentication/wefitter-authentication.yml
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
modified: '2026-07-21'
name: WeFitter
nav: Providers
network: true
overview: 'WeFitter publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including App API, Challenge API, Connection API, and 6 more. Tagged areas include Company, Health, Fitness, Wearables, and Health Data.


  The WeFitter catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  WeFitter''s developer surface includes documentation, getting-started guide, API reference, support, engineering blog, changelog, signup flow, and 25 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: WeFitter API Rules
  rule_count: 64
  severity_counts:
    error: 58
    hint: 0
    info: 2
    warn: 4
  slug: wefitter-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
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
    score: 19.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wefitter/wefitter-2026-08-17T082909.png
security:
- kind: authentication
  name: Wefitter Authentication
  slug: wefitter-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Wefitter Domain Security
  slug: wefitter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Onboard a profile and connect a wearable
  slug: wefitter-onboard-profile-and-connect-wearable
- name: Retrieve a profile's health data
  slug: wefitter-retrieve-health-data
- name: Create and run a gamification challenge
  slug: wefitter-run-a-challenge
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
