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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.keyper.io/access
  baseurl_source: declared
  description: Retrieve the permission whitelist / blacklist for an Access Control System.
  name: Keyper Permissions API
  slug: keyper-permissions-api
- baseURL: https://api.keyper.io/access
  baseurl_source: declared
  description: Send access / entry transactions to keyper.
  name: Keyper Transactions API
  slug: keyper-transactions-api
artifact_total: 8
collections:
- collection_type: open
  name: keyper Access Permissions API
  slug: open-keyper-permissions-api
- collection_type: open
  name: keyper Access Permissions Transactions API
  slug: open-keyper-transactions-api
common:
- group: agent
  href: https://artifacts.apis.io/keyper/mcp/keyper-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/keyper-mcp.yml
- group: other
  href: https://artifacts.apis.io/keyper/overlays/keyper-access-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/keyper-access-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.keyper.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.keyper.com
- group: docs
  title: ''
  type: APIReference
  url: https://developers.keyper.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.keyper.com
- group: operate
  title: ''
  type: Support
  url: https://support.keyper.com/developers/
- group: company
  title: ''
  type: Blog
  url: https://www.keyper.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keyper
- group: start
  title: ''
  type: Login
  url: https://app.keyper.io/business/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.keyper.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.keyper.com/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.keyper.com
- group: build
  href: https://artifacts.apis.io/keyper/packages/keyper-packages.yml
  title: ''
  type: Packages
  url: packages/keyper-packages.yml
- group: build
  href: https://artifacts.apis.io/keyper/packages/keyper-packages.yml
  title: ''
  type: SDKs
  url: packages/keyper-packages.yml
- group: design
  href: https://artifacts.apis.io/keyper/components/keyper-components.yml
  title: ''
  type: Components
  url: components/keyper-components.yml
- group: start
  href: https://artifacts.apis.io/keyper/sandbox/keyper-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/keyper-sandbox.yml
- group: design
  href: https://artifacts.apis.io/keyper/lifecycle/keyper-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/keyper-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/keyper/llms/keyper-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keyper-llms.txt
- group: agent
  href: https://artifacts.apis.io/keyper/well-known/keyper-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/keyper-well-known.yml
- group: agent
  href: https://artifacts.apis.io/keyper/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/keyper/security/keyper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keyper-domain-security.yml
created: '2026-07-17'
description: keyper is an Austrian technology company providing connected ticketing and digital access solutions. Its developer platform lets ticketing systems, resellers and access control systems (ACS) deliver e-tickets and exchange access data through the keyper Access API, Connect Provider / Reseller APIs, Ticket Delivery API, native Android and iOS SDKs, and embeddable web components (seatmaps and checkout). The Access API sends entry transactions for keys (ticket barcodes) and their permissions (events), and returns the Grant / Block permission whitelist an access control system enforces at the gate. keyper serves sports, arts and culture organisations across Austria and Central Europe and is backed by Speedinvest.
image: https://www.keyper.com/wp-content/uploads/keyper-logo.png
layout: provider
modified: '2026-07-19'
name: Keyper
nav: Providers
network: true
overview: 'Keyper publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Permissions API and Transactions API. Tagged areas include Company, Ticketing, Access Control, Event, and Developer Platform.


  Keyper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, sandbox, and 16 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 14.5
    developer_ergonomics: 73.2
    discoverability: 66.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 34.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/keyper/keyper-2026-07-25T223658.png
security:
- kind: authentication
  name: Keyper Authentication
  slug: keyper-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Keyper Domain Security
  slug: keyper-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: Report gate entry transactions to keyper
  slug: keyper-send-transactions
- name: Sync the keyper permission whitelist to an access control system
  slug: keyper-sync-permissions
slug: keyper
tags:
- Company
- Ticketing
- Access Control
- Event
- Developer Platform
- SDK
- Sports
- Arts and Culture
- Austria
website: https://www.keyper.com
---
