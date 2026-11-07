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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Peerbound Agentic Access
  operation_count: 10
  slug: peerbound-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: /api/public/v1
  baseurl_source: spec
  description: The Activities API from Peerbound — 2 operation(s) for activities.
  name: Peerbound Activities API
  slug: peerbound-activities-api
- baseURL: /api/public/v1
  baseurl_source: spec
  description: The Moments API from Peerbound — 2 operation(s) for moments.
  name: Peerbound Moments API
  slug: peerbound-moments-api
- baseURL: /api/public/v1
  baseurl_source: spec
  description: The Notes API from Peerbound — 2 operation(s) for notes.
  name: Peerbound Notes API
  slug: peerbound-notes-api
- baseURL: /api/public/v1
  baseurl_source: spec
  description: The Reviews API from Peerbound — 2 operation(s) for reviews.
  name: Peerbound Reviews API
  slug: peerbound-reviews-api
- baseURL: /api/public/v1
  baseurl_source: spec
  description: The Stories API from Peerbound — 2 operation(s) for stories.
  name: Peerbound Stories API
  slug: peerbound-stories-api
artifact_total: 20
common:
- group: auth
  href: https://artifacts.apis.io/peerbound/well-known/peerbound-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/peerbound-status-security.txt
- group: other
  href: https://artifacts.apis.io/peerbound/vendors/peerbound-vendors.yml
  title: ''
  type: Vendors
  url: vendors/peerbound-vendors.yml
- group: agent
  href: https://artifacts.apis.io/peerbound/agentic-access/peerbound-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/peerbound-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/peerbound/rules/peerbound-rules.yml
  title: ''
  type: Spectral
  url: rules/peerbound-rules.yml
- group: design
  href: https://artifacts.apis.io/peerbound/json-ld/peerbound-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/peerbound-context.jsonld
- group: design
  href: https://artifacts.apis.io/peerbound/vocabulary/peerbound-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/peerbound-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/peerbound/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/peerbound/data-model/peerbound-data-model.yml
  title: ''
  type: DataModel
  url: data-model/peerbound-data-model.yml
- group: design
  href: https://artifacts.apis.io/peerbound/conventions/peerbound-conventions.yml
  title: ''
  type: Conventions
  url: conventions/peerbound-conventions.yml
- group: auth
  href: https://artifacts.apis.io/peerbound/authentication/peerbound-authentication.yml
  title: ''
  type: Authentication
  url: authentication/peerbound-authentication.yml
- group: design
  href: https://artifacts.apis.io/peerbound/errors/peerbound-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/peerbound-problem-types.yml
- group: design
  href: https://artifacts.apis.io/peerbound/conformance/peerbound-conformance.yml
  title: ''
  type: Conformance
  url: conformance/peerbound-conformance.yml
- group: agent
  href: https://artifacts.apis.io/peerbound/llms/peerbound-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/peerbound-llms.txt
- group: agent
  href: https://artifacts.apis.io/peerbound/well-known/peerbound-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/peerbound-well-known.yml
- group: other
  href: https://artifacts.apis.io/peerbound/hosts/peerbound-hosts.yml
  title: ''
  type: Hosts
  url: hosts/peerbound-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.peerbound.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.peerbound.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.peerbound.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.peerbound.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.peerbound.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.peerbound.com/articles/3144479554-peerbound-onboarding-guide
- group: docs
  title: ''
  type: Documentation
  url: https://help.peerbound.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/peerbound
- group: auth
  href: https://artifacts.apis.io/peerbound/security/peerbound-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peerbound-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.peerbound.com/
created: '2026-10-29'
description: Peerbound provides a platform to centralize customer proof, uncover advocates and insights, and empower sales teams to win deals. Trusted by companies such as Canva, Gong, and Lattice, it helps turn customer testimonials into revenue-driving assets. The service aggregates case studies, reviews, and success stories, offering analytics and integration with CRM tools to streamline sales enablement.
image: https://framerusercontent.com/assets/LUuLhKnV3Hemd6HrgHfUf2fGDY.png
json_schemas:
- name: Activity
  property_count: 10
  slug: peerbound-activity
- name: ListResponse[Activity]
  property_count: 2
  slug: peerbound-list-response-activity
- name: ListResponse[Moment]
  property_count: 2
  slug: peerbound-list-response-moment
- name: ListResponse[Note]
  property_count: 2
  slug: peerbound-list-response-note
- name: ListResponse[Review]
  property_count: 2
  slug: peerbound-list-response-review
- name: ListResponse[Story]
  property_count: 2
  slug: peerbound-list-response-story
- name: Moment
  property_count: 11
  slug: peerbound-moment
- name: Note
  property_count: 10
  slug: peerbound-note
- name: Review
  property_count: 12
  slug: peerbound-review
- name: Story
  property_count: 9
  slug: peerbound-story
jsonld:
- class_count: 22
  name: Peerbound Context
  property_count: 51
  slug: peerbound-context
layout: provider
modified: '2026-10-29'
name: Peerbound
nav: Providers
network: true
overview: 'Peerbound publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Moments API, Notes API, and 2 more. Tagged areas include Company, Software-as-a-Service, Sales Enablement, Customer Proof, and Analytics.


  The Peerbound catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Peerbound''s developer surface includes authentication, engineering blog, getting-started guide, documentation, and 21 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Peerbound API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: peerbound-rules
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 47.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 39.3
    contract_governance: 22.0
    contract_quality: 57.1
    developer_ergonomics: 30.2
    discoverability: 55.4
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/peerbound/peerbound-2026-11-03T141105.png
security:
- kind: authentication
  name: Peerbound Authentication
  slug: peerbound-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Peerbound Domain Security
  slug: peerbound-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peerbound
tags:
- Company
- Software-as-a-Service
- Sales Enablement
- Customer Proof
- Analytics
website: https://www.peerbound.com/
---
