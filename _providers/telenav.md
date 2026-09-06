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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 22.7
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Location-based semantic search for the connected car - onebox search with category, brand, corridor, polygon, and bounding-box filters, reverse geocoding, EV charge-station search, auto-suggest and wo
  name: Telenav Entity Service REST API
  slug: telenav-entity-service-rest-api
artifact_total: 4
asyncapis:
- description: ''
  name: Telenav Webhooks
  slug: telenav-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.telenav.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.telenav.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telenav.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.telenav.com/api-references/sdk/entity/current/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.telenav.com/entity-android/install-sdk.html
- group: company
  title: ''
  type: Blog
  url: https://www.telenav.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.telenav.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telenav.com/legal/policies-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telenav.com/legal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Telenav
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telenav-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/telenav-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telenav-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telenav-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telenav-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/telenav-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/telenav-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/telenav-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/telenav-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/telenav-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/telenav-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/telenav-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/telenav-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telenav-llms.txt
created: '2026-07-17'
description: Telenav is a connected-car and location-based services company that powers in-vehicle navigation (VIVID NAV), infotainment (VIVID IVI), and in-car commerce (VIVID COMMERCE) for automotive partners including Daimler, Ford, GM, Toyota, and Xpeng. Its developer surface centers on the Entity Service REST API for location-aware semantic search, auto-suggest predictions, entity detail lookup, and discovery including EV charge-station search, alongside partner-distributed navigation and driver-intelligence SDKs documented at docs.telenav.com and open-source Java tooling on Maven Central.
image: https://avatars.githubusercontent.com/u/3743554?v=4
layout: provider
modified: '2026-07-21'
name: Telenav
nav: Providers
network: true
overview: 'Telenav publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mapping, Navigation, Location, Search, and Automotive.


  The Telenav catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Telenav''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, changelog, and 17 more developer resources.'
random_paper: 16
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 41.7
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telenav/refs/heads/main/screenshots/telenav-2026-09-02T162734.png
security:
- kind: authentication
  name: Telenav Authentication
  slug: telenav-authentication
  summary_line: apiKey/requestSignature · 3 schemes
- kind: domain-security
  name: Telenav Domain Security
  slug: telenav-domain-security
  summary_line: HSTS · DMARC
slug: telenav
tags:
- Mapping
- Navigation
- Location
- Search
- Automotive
- Connected Cars
- EV Charging
- Points of Interest
website: https://www.telenav.com
---
