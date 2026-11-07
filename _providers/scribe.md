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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Scribe Agentic Access
  operation_count: 4
  slug: scribe-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://public-api.scribehow.com
  baseurl_source: declared
  description: The Documents API from Scribe — 2 operation(s) for documents.
  name: Scribe Documents API
  slug: scribe-documents-api
- baseURL: https://public-api.scribehow.com
  baseurl_source: declared
  description: The Search API from Scribe — 1 operation(s) for search.
  name: Scribe Search API
  slug: scribe-search-api
- baseURL: https://public-api.scribehow.com
  baseurl_source: declared
  description: The Teams API from Scribe — 1 operation(s) for teams.
  name: Scribe Teams API
  slug: scribe-teams-api
artifact_total: 17
collections:
- collection_type: open
  name: Scribe Search & Retrieval Documents API
  slug: open-scribe-documents-api
- collection_type: open
  name: Scribe & Retrieval Documents Search API
  slug: open-scribe-search-api
- collection_type: open
  name: Scribe Search & Retrieval Documents Teams API
  slug: open-scribe-teams-api
common:
- group: commercial
  href: https://artifacts.apis.io/scribe/plans/scribe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scribe-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/scribe/capabilities/scribe-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/scribe-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/scribe/overlays/scribe-search-retrieval-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scribe-search-retrieval-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://scribe.com
- group: docs
  title: ''
  type: Documentation
  url: https://public-api.scribehow.com/schema/redoc/
- group: docs
  title: ''
  type: APIReference
  url: https://public-api.scribehow.com/schema/redoc/
- group: start
  title: ''
  type: GettingStarted
  url: https://scribehow.com/settings?tab=developerAccess
- group: operate
  title: ''
  type: Support
  url: https://support.scribehow.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://scribe.com/library
- group: commercial
  title: ''
  type: Pricing
  url: https://scribe.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://scribehow.com/signup?plan=free
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scribe.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scribe.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.scribe.com
- group: auth
  title: ''
  type: Compliance
  url: https://scribe.com/security
- group: auth
  href: https://artifacts.apis.io/scribe/security/scribe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/scribe-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/scribe/authentication/scribe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scribe-authentication.yml
- group: design
  href: https://artifacts.apis.io/scribe/conventions/scribe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scribe-conventions.yml
- group: design
  href: https://artifacts.apis.io/scribe/errors/scribe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scribe-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/scribe/rate-limits/scribe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scribe-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/scribe/lifecycle/scribe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scribe-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/scribe/conformance/scribe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scribe-conformance.yml
- group: design
  href: https://artifacts.apis.io/scribe/data-model/scribe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scribe-data-model.yml
- group: auth
  href: https://artifacts.apis.io/scribe/security/scribe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scribe-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/scribe/well-known/scribe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scribe-well-known.yml
- group: agent
  href: https://artifacts.apis.io/scribe/mcp/scribe-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/scribe-mcp.yml
- group: agent
  href: https://artifacts.apis.io/scribe/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/scribe/agentic-access/scribe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scribe-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/scribe/llms/scribe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scribe-llms.txt
created: '2026-07-17'
description: Scribe (scribehow) is an AI workflow-documentation platform founded in 2019 that automatically turns any process or software walkthrough into a step-by-step guide. Its products — Scribe Capture, the knowledge base, and the newer Scribe Optimize workflow-mapping platform — are used by more than five million people across a large share of the Fortune 500. For developers, Scribe publishes a read-only Search & Retrieval API (OpenAPI 3.1) that searches, lists, and retrieves an organization's Scribe Documents and Knowledge Pages for integration into custom applications and AI agents. Public API access is an Enterprise-plan feature authenticated with a static API key sent in the X-API-Key header. The company is backed by Amplify Partners, Redpoint Ventures, Tiger Global, StepStone, Morado Ventures, and New York Life Ventures, and reached a $1.3B valuation with its 2025 Series C.
finops:
- has_sources: true
  method: derived
  name: Scribe Finops
  primary_unit: seat
  service_category: ''
  slug: scribe-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scribe.png
layout: provider
modified: '2026-07-21'
name: Scribe
nav: Providers
network: true
overview: 'Scribe publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Documents API, Search API, and Teams API. Tagged areas include Company, Artificial Intelligence, Documentation, Knowledge Management, and Search.


  The Scribe catalog on APIs.io includes 1 Spectral governance ruleset.


  Scribe''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Scribe Plans Pricing
  plan_count: 4
  slug: scribe-plans-pricing
- name: Scribe Price Estimates
  plan_count: 0
  slug: scribe-price-estimates
random_paper: 8
rate_limits:
- limit_count: 2
  name: Scribe Rate Limits
  slug: scribe-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Scribe API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: scribe-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 52.7
    developer_ergonomics: 49.4
    discoverability: 73.2
    operational_transparency: 36.8
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ferpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/scribe/scribe-2026-08-17T081843.png
security:
- kind: authentication
  name: Scribe Authentication
  slug: scribe-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scribe Domain Security
  slug: scribe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Scribe Trust Center
  slug: scribe-trust-center
  summary_line: SOC 2 Type II, ISO 27001, HIPAA, FERPA, GDPR, US State Privacy Laws
skill_count: 2
skills:
- name: Search the Scribe knowledge base
  slug: scribe-search-knowledge-base
- name: Sync Scribe documents into an external system
  slug: scribe-sync-documents
slug: scribe
tags:
- Company
- Artificial Intelligence
- Documentation
- Knowledge Management
- Search
- Workflows
- Process Documentation
- Enterprise
website: https://scribe.com
---
