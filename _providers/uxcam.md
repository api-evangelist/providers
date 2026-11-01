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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.uxcam.com/v2
  baseurl_source: declared
  description: Custom and automatic events logged during sessions
  name: UXCam Events API
  slug: uxcam-events-api
- baseURL: https://api.uxcam.com/v2
  baseurl_source: declared
  description: Recorded usage sessions (qualitative list + quantitative analytics)
  name: UXCam Sessions API
  slug: uxcam-sessions-api
- baseURL: https://api.uxcam.com/v2
  baseurl_source: declared
  description: App users tracked by the UXCam SDK
  name: UXCam Users API
  slug: uxcam-users-api
artifact_total: 13
collections:
- collection_type: open
  name: UXCam Data Access Events API
  slug: open-uxcam-events-api
- collection_type: open
  name: UXCam Data Access Events Sessions API
  slug: open-uxcam-sessions-api
- collection_type: open
  name: UXCam Data Access Events Users API
  slug: open-uxcam-users-api
common:
- group: other
  href: https://artifacts.apis.io/uxcam/overlays/uxcam-data-access-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/uxcam-data-access-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://uxcam.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uxcam.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uxcam.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.uxcam.com/docs/data-access-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uxcam.com/docs/what-is-uxcam
- group: operate
  title: ''
  type: Support
  url: https://help.uxcam.com
- group: company
  title: ''
  type: Blog
  url: https://uxcam.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uxcam
- group: commercial
  title: ''
  type: Pricing
  url: https://uxcam.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.uxcam.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.uxcam.com/en/articles/10222767-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uxcam.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uxcam.com
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/9127779/2s935it5r2
- group: build
  href: https://artifacts.apis.io/uxcam/postman/uxcam-data-access-v2-postman.json
  title: ''
  type: PostmanCollection
  url: postman/uxcam-data-access-v2-postman.json
- group: operate
  href: https://artifacts.apis.io/uxcam/changelog/uxcam-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/uxcam-changelog.yml
- group: agent
  href: https://artifacts.apis.io/uxcam/mcp/uxcam-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/uxcam-mcp.yml
- group: agent
  href: https://artifacts.apis.io/uxcam/llms/uxcam-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uxcam-llms.txt
- group: build
  href: https://artifacts.apis.io/uxcam/packages/uxcam-packages.yml
  title: ''
  type: Packages
  url: packages/uxcam-packages.yml
- group: build
  href: https://artifacts.apis.io/uxcam/packages/uxcam-packages.yml
  title: ''
  type: SDKs
  url: packages/uxcam-packages.yml
- group: agent
  href: https://artifacts.apis.io/uxcam/well-known/uxcam-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/uxcam-well-known.yml
- group: auth
  href: https://artifacts.apis.io/uxcam/well-known/uxcam-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/uxcam-security.txt
- group: auth
  href: https://artifacts.apis.io/uxcam/authentication/uxcam-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uxcam-authentication.yml
- group: design
  href: https://artifacts.apis.io/uxcam/conventions/uxcam-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uxcam-conventions.yml
- group: design
  href: https://artifacts.apis.io/uxcam/errors/uxcam-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uxcam-problem-types.yml
- group: design
  href: https://artifacts.apis.io/uxcam/lifecycle/uxcam-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uxcam-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/uxcam/conformance/uxcam-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uxcam-conformance.yml
- group: design
  href: https://artifacts.apis.io/uxcam/data-model/uxcam-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uxcam-data-model.yml
- group: auth
  href: https://artifacts.apis.io/uxcam/security/uxcam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uxcam-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/uxcam/security/uxcam-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/uxcam-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://uxcam.com/bug-bounty
- group: agent
  href: https://artifacts.apis.io/uxcam/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: UXCam is a mobile-first product analytics and session replay platform that helps product, UX, and engineering teams understand how people actually use their apps. SDKs for Android, iOS, React Native, Flutter, Cordova, Xamarin/MAUI, NativeScript, and the web capture session recordings, heatmaps, gestures, crashes, and custom events with built-in PII occlusion, while the Data Access API exposes session, user, and event analytics programmatically and an official MCP server guides agent-driven SDK integration.
image: https://github.com/uxcam.png
layout: provider
mcp_servers:
- description: Remote MCP server at integration.mcp.uxcam.com over streamable HTTP; 3 tools listed.
  name: UXCam MCP Server
  slug: uxcam-integration
modified: '2026-07-21'
name: UXCam
nav: Providers
network: true
overview: 'UXCam publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Events API, Sessions API, and Users API. Tagged areas include Company, Product Analytics, Session Replay, Mobile Analytics, and Heatmaps.


  UXCam''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 42.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 14.3
    developer_ergonomics: 70.8
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 42.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/uxcam/uxcam-2026-08-17T082703.png
security:
- kind: authentication
  name: Uxcam Authentication
  slug: uxcam-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Uxcam Domain Security
  slug: uxcam-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Uxcam Vulnerability Disclosure
  slug: uxcam-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: Analyze user cohorts in UXCam
  slug: uxcam-analyze-user-cohorts
- name: Export event analytics from UXCam
  slug: uxcam-export-event-analytics
- name: Triage problem sessions in UXCam
  slug: uxcam-triage-problem-sessions
slug: uxcam
tags:
- Company
- Product Analytics
- Session Replay
- Mobile Analytics
- Heatmaps
- User Experience
- Crash Reporting
website: https://uxcam.com
---
