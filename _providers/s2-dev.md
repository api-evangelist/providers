---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: S2 Dev Agentic Access
  operation_count: 24
  slug: s2-dev-agentic-access
  summary_line: 24 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://a.s2.dev/v1
  baseurl_source: declared
  description: Manage access tokens
  name: S2 Dev Access Tokens API
  slug: s2-dev-access-tokens-api
- baseURL: https://a.s2.dev/v1
  baseurl_source: declared
  description: Manage basins
  name: S2 Dev Basins API
  slug: s2-dev-basins-api
- baseURL: https://a.s2.dev/v1
  baseurl_source: declared
  description: Manage locations
  name: S2 Dev Locations API
  slug: s2-dev-locations-api
- baseURL: https://a.s2.dev/v1
  baseurl_source: declared
  description: Usage metrics and data.
  name: S2 Dev Metrics API
  slug: s2-dev-metrics-api
- baseURL: https://a.s2.dev/v1
  baseurl_source: declared
  description: Manage records
  name: S2 Dev Records API
  slug: s2-dev-records-api
- baseURL: https://a.s2.dev/v1
  baseurl_source: declared
  description: Manage streams
  name: S2 Dev Streams API
  slug: s2-dev-streams-api
artifact_total: 25
collections:
- collection_type: open
  name: S2, the durable streams access-tokens API
  slug: open-s2-dev-access-tokens-api
- collection_type: open
  name: S2, the durable streams access-tokens basins API
  slug: open-s2-dev-basins-api
- collection_type: open
  name: S2, the durable streams access-tokens locations API
  slug: open-s2-dev-locations-api
- collection_type: open
  name: S2, the durable streams access-tokens metrics API
  slug: open-s2-dev-metrics-api
- collection_type: open
  name: S2, the durable streams access-tokens records API
  slug: open-s2-dev-records-api
- collection_type: open
  name: S2, the durable access-tokens streams API
  slug: open-s2-dev-streams-api
common:
- group: other
  href: https://artifacts.apis.io/s2-dev/capabilities/s2-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/s2-dev-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/s2-dev/plans/s2-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/s2-dev-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/s2-dev/overview
- group: company
  title: ''
  type: BlogRSS
  url: https://s2.dev/blog/feed.xml
- group: company
  title: ''
  type: Website
  url: https://www.s2.dev/
- group: auth
  href: https://artifacts.apis.io/s2-dev/security/s2-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/s2-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/s2-dev/security/s2-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/s2-dev-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/s2-dev/agentic-access/s2-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/s2-dev-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/s2-dev/authentication/s2-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/s2-dev-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://s2.dev/docs/platform/security
- group: auth
  href: https://artifacts.apis.io/s2-dev/security/s2-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/s2-dev-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://s2.dev/docs/platform/security
- group: start
  title: ''
  type: DeveloperPortal
  url: https://s2.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://s2.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://s2.dev/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://s2.dev/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:hi@s2.dev
- group: company
  title: ''
  type: Blog
  url: https://s2.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/s2-streamstore
- group: commercial
  title: ''
  type: Pricing
  url: https://s2.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://s2.dev/dashboard
- group: commercial
  title: ''
  type: TermsOfService
  url: https://s2.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://s2.dev/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.s2.dev
- group: build
  href: https://artifacts.apis.io/s2-dev/packages/s2-dev-packages.yml
  title: ''
  type: Packages
  url: packages/s2-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/s2-dev/packages/s2-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/s2-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/s2-dev/cli/s2-dev-cli.yml
  title: ''
  type: CLI
  url: cli/s2-dev-cli.yml
- group: start
  href: https://artifacts.apis.io/s2-dev/sandbox/s2-dev-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/s2-dev-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/s2-dev/changelog/s2-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/s2-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/s2-dev/lifecycle/s2-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/s2-dev-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/s2-dev/rate-limits/s2-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/s2-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/s2-dev/conventions/s2-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/s2-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/s2-dev/conventions/s2-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/s2-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/s2-dev/errors/s2-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/s2-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/s2-dev/data-model/s2-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/s2-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/s2-dev/conformance/s2-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/s2-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/s2-dev/well-known/s2-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/s2-dev-well-known.yml
- group: auth
  href: https://artifacts.apis.io/s2-dev/well-known/s2-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/s2-dev-security.txt
- group: other
  href: https://artifacts.apis.io/s2-dev/well-known/s2-dev-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/s2-dev-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/s2-dev/llms/s2-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/s2-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/s2-dev/overlays/s2-dev-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/s2-dev-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/s2-dev/mcp/s2-dev-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/s2-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/s2-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: S2 ("Stream Store") is the API for unlimited, durable, real-time streams. Where object storage deals with blobs, S2 provides append-able, ordered record streams that can be tailed in real time and replayed from any retained point. Core data-plane operations are append, read, and check-tail; the control plane manages accounts, basins (stream namespaces), streams, scoped access tokens, locations, and metrics. It targets agent session logs, live views and build logs, event sourcing and sync, data feeds, resumable LLM token streaming, and observability. Access is over a REST/JSON + Protobuf HTTP API, an S2S binary protocol over HTTP/2, SSE tailing, first-party TypeScript, Python, Go, and Rust SDKs, a CLI, and a Terraform provider. S2 is a Y Combinator-backed company.
finops:
- has_sources: true
  method: derived
  name: S2 Dev Finops
  primary_unit: gib
  service_category: ''
  slug: s2-dev-finops
  template: false
image: https://avatars.githubusercontent.com/u/136030139?v=4
layout: provider
modified: '2026-10-06'
name: S2 Dev
nav: Providers
network: true
overview: 'S2 Dev publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Tokens API, Basins API, Locations API, and 3 more. Tagged areas include Company, Streaming, Real-Time, Event Streaming, and Durable Storage.


  The S2 Dev catalog on APIs.io includes 1 Spectral governance ruleset.


  S2 Dev''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 36 more developer resources.'
plans:
- name: S2 Dev Plans Pricing
  plan_count: 11
  slug: s2-dev-plans-pricing
- name: S2 Dev Price Estimates
  plan_count: 0
  slug: s2-dev-price-estimates
random_paper: 1
rate_limits:
- limit_count: 5
  name: S2 Dev Rate Limits
  slug: s2-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: S2 Dev API Rules
  rule_count: 63
  severity_counts:
    error: 55
    hint: 0
    info: 2
    warn: 6
  slug: s2-dev-rules
score:
  band: exemplar
  composite: 71.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 55.4
    developer_ergonomics: 81.5
    discoverability: 73.2
    operational_transparency: 76.3
  previous_composite: 70.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/s2-dev/s2-dev-2026-08-17T081704.png
security:
- kind: authentication
  name: S2 Dev Authentication
  slug: s2-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: S2 Dev Domain Security
  slug: s2-dev-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: S2 Dev Vulnerability Disclosure
  slug: s2-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: S2 Dev Trust Center
  slug: s2-dev-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 3
skills:
- name: Append records and tail a stream on S2
  slug: s2-dev-append-and-tail-records
- name: Create a basin and stream on S2
  slug: s2-dev-create-basin-and-stream
- name: Issue a scoped S2 access token
  slug: s2-dev-issue-scoped-token
slug: s2-dev
tags:
- Company
- Streaming
- Real-Time
- Event Streaming
- Durable Storage
- Message Streaming
- Data Feed
- Observability
- Developer Tools
- Infrastructure
website: https://www.s2.dev/
---
