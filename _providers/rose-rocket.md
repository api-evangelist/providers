---
access_model:
  confidence: high
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
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
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://network.roserocket.com/api/v2/platformModel
  baseurl_source: declared
  description: The Boards API from Rose Rocket — 1 operation(s) for boards.
  name: Rose Rocket Boards API
  slug: rose-rocket-boards-api
- baseURL: https://network.roserocket.com/api/v2/platformModel
  baseurl_source: declared
  description: The Events API from Rose Rocket — 1 operation(s) for events.
  name: Rose Rocket Events API
  slug: rose-rocket-events-api
- baseURL: https://network.roserocket.com/api/v2/platformModel
  baseurl_source: declared
  description: The Object Records API from Rose Rocket — 6 operation(s) for object records.
  name: Rose Rocket Object Records API
  slug: rose-rocket-object-records-api
- baseURL: https://network.roserocket.com/api/v2/platformModel
  baseurl_source: declared
  description: The User Groups API from Rose Rocket — 3 operation(s) for user groups.
  name: Rose Rocket User Groups API
  slug: rose-rocket-user-groups-api
artifact_total: 11
asyncapis:
- description: ''
  name: Rose Rocket Webhooks
  slug: rose-rocket-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/rose-rocket-platform-model-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.roserocket.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://roserocket.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://roserocket.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://roserocket.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://roserocket.readme.io/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.roserocket.com/
- group: company
  title: ''
  type: Blog
  url: https://www.roserocket.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.roserocket.com/pricing
- group: start
  title: ''
  type: Login
  url: https://roserocket.com/_/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.roserocket.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.roserocket.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.roserocket.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://roserocket.readme.io/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RoseRocketSDK
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rose-rocket-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rose-rocket-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rose-rocket-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rose-rocket-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rose-rocket-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/rose-rocket-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rose-rocket-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rose-rocket-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rose-rocket-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rose-rocket-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/rose-rocket-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rose-rocket-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rose-rocket-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/rose-rocket-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/rose-rocket-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rose-rocket-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rose-rocket-cli.yml
- group: design
  title: ''
  type: Components
  url: components/rose-rocket-components.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rose-rocket-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rose-rocket-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rose-rocket-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rose-rocket-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: 'Rose Rocket is a Toronto-based transportation management system (TMS) for freight brokers, carriers and 3PLs, sold as an AI-native, configurable operations platform rather than an off-the-shelf template. The product covers order intake, dispatch, tendering, tracking, documents, invoicing and billing, with no-code custom fields, boards and workflows, in-product AI agents (TED, Rosie, Rocky) and role-based access control down to the widget. Its developer surface is the Platform Model API, a single generic object-CRUD REST API served at network.roserocket.com/api/v2/platformModel that reads and writes every domain object — customer, order, task, stop, manifest, commodity, partner, quote, invoice, bill, asset, tag, contact, document — through one set of /objects operations keyed by objectKey, plus user groups, boards, events and webhook destinations. Authentication is OAuth 2.0 (authorization code or client-credentials service account) against an Auth0-hosted authorization server
  at a.roserocket.com. API access is not self-serve: credentials come from an account representative or the partnership team, and the pricing page lists "unlimited API access" as an Enterprise tier feature.'
image: https://framerusercontent.com/images/eevMW1fKr5iFYAXYwLYuO8Sp5PQ.jpg
layout: provider
modified: '2026-08-26'
name: Rose Rocket
nav: Providers
network: true
overview: 'Rose Rocket publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Boards API, Events API, Object Records API, and 1 more. Tagged areas include Transportation, Logistics, Freight, Trucking, and Transportation Management System.


  The Rose Rocket catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Rose Rocket''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 31 more developer resources.'
plans:
- name: Rose Rocket Plans Pricing
  plan_count: 2
  slug: rose-rocket-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Rose Rocket Rate Limits
  slug: rose-rocket-rate-limits
scopes:
- name: Rose Rocket Scopes
  scope_count: 0
  slug: rose-rocket-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 18.2
    contract_quality: 50.3
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 52.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rose-rocket/refs/heads/main/screenshots/rose-rocket-2026-09-02T154132.png
security:
- kind: authentication
  name: Rose Rocket Authentication
  slug: rose-rocket-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Rose Rocket Domain Security
  slug: rose-rocket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rose Rocket Vulnerability Disclosure
  slug: rose-rocket-vulnerability-disclosure
  summary_line: Hackerone
slug: rose-rocket
tags:
- Transportation
- Logistics
- Freight
- Trucking
- Transportation Management System
- Supply Chain
- Dispatch
- Webhook
- Authentication
- Canada
website: https://www.roserocket.com/
---
