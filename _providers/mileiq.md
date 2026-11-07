---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mileiq Agentic Access
  operation_count: 6
  slug: mileiq-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://external-api.mileiq.com
  baseurl_source: declared
  description: The groups API from MileIQ — 3 operation(s) for groups.
  name: MileIQ Groups API
  slug: mileiq-groups-api
- baseURL: https://external-api.mileiq.com
  baseurl_source: declared
  description: The users API from MileIQ — 3 operation(s) for users.
  name: MileIQ Users API
  slug: mileiq-users-api
artifact_total: 12
collections:
- collection_type: open
  name: MileIQ External groups API
  slug: open-mileiq-groups-api
- collection_type: open
  name: MileIQ External groups users API
  slug: open-mileiq-users-api
common:
- group: other
  href: https://artifacts.apis.io/mileiq/overlays/mileiq-external-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mileiq-external-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/mileiq/security/mileiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mileiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mileiq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mileiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mileiq.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.mileiq.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mileiq.com/api-reference/getting-started
- group: company
  title: ''
  type: Blog
  url: https://mileiq.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.mileiq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mileiq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mileiq.com/en-ca/for-business/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mileiq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mileiq.com/privacy
- group: auth
  href: https://artifacts.apis.io/mileiq/authentication/mileiq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mileiq-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mileiq/scopes/mileiq-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mileiq-scopes.yml
- group: design
  href: https://artifacts.apis.io/mileiq/conventions/mileiq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mileiq-conventions.yml
- group: design
  href: https://artifacts.apis.io/mileiq/errors/mileiq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mileiq-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/mileiq/rate-limits/mileiq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/mileiq-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/mileiq/lifecycle/mileiq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mileiq-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/mileiq/changelog/mileiq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mileiq-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.mileiq.com/api-reference/changelog
- group: design
  href: https://artifacts.apis.io/mileiq/conformance/mileiq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mileiq-conformance.yml
- group: design
  href: https://artifacts.apis.io/mileiq/data-model/mileiq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mileiq-data-model.yml
- group: agent
  href: https://artifacts.apis.io/mileiq/well-known/mileiq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mileiq-well-known.yml
- group: agent
  href: https://artifacts.apis.io/mileiq/mcp/mileiq-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mileiq-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mileiq/llms/mileiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mileiq-llms.txt
- group: agent
  href: https://artifacts.apis.io/mileiq/agentic-access/mileiq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mileiq-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/mileiq/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: MileIQ is an automatic mileage-tracking service for individuals and teams that logs every drive in the background, classifies each trip as business or personal, and calculates the deductible mileage value for tax and expense reporting. Its read-only OAuth 2.1 External API (external-api.mileiq.com) exposes authenticated user profiles, drive/trip records with start and end geolocation, distance, and monetary value, plus administrator access to group (team) rosters and member-reported drives — letting accounting, expense, and reimbursement platforms sync MileIQ mileage data. Originally built by Mobile Data Labs and later part of Microsoft, MileIQ now operates as an independent product. The API is currently available on a request basis.
image: https://www.mileiq.com/images/mileiq.7b54ead1.svg
layout: provider
modified: '2026-07-20'
name: MileIQ
nav: Providers
network: true
overview: 'MileIQ publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Groups API and Users API. Tagged areas include Company, Consumer, Mileage Tracking, Expense Management, and Transportation.


  The MileIQ catalog on APIs.io includes 1 Spectral governance ruleset.


  MileIQ''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Mileiq Rate Limits
  slug: mileiq-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: MileIQ API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: mileiq-rules
scopes:
- name: Mileiq Scopes
  scope_count: 7
  slug: mileiq-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 55.3
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 15.8
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mileiq/mileiq-2026-08-07T172909.png
security:
- kind: authentication
  name: Mileiq Authentication
  slug: mileiq-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Mileiq Domain Security
  slug: mileiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Retrieve a user's MileIQ drives
  slug: mileiq-retrieve-user-drives
- name: Review a MileIQ group's reported drives
  slug: mileiq-review-group-reported-drives
slug: mileiq
tags:
- Company
- Consumer
- Mileage Tracking
- Expense Management
- Transportation
- Tax
- Accounting
- Location
- Fleet Management
website: https://www.mileiq.com/
---
