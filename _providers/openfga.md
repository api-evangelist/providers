---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Openfga Agentic Access
  operation_count: 24
  slug: openfga-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 1
apis:
- description: The Assertions API from OpenFGA — 1 operation(s) for assertions.
  name: OpenFGA Assertions API
  slug: openfga-assertions-api
- description: The Authorization Models API from OpenFGA — 2 operation(s) for authorization models.
  name: OpenFGA Authorization Models API
  slug: openfga-authorization-models-api
- description: The AuthZenService API from OpenFGA — 6 operation(s) for authzenservice.
  name: OpenFGA AuthZenService API
  slug: openfga-authzenservice-api
- description: The Relationship Queries API from OpenFGA — 6 operation(s) for relationship queries.
  name: OpenFGA Relationship Queries API
  slug: openfga-relationship-queries-api
- description: The Relationship Tuples API from OpenFGA — 3 operation(s) for relationship tuples.
  name: OpenFGA Relationship Tuples API
  slug: openfga-relationship-tuples-api
- description: The Stores API from OpenFGA — 2 operation(s) for stores.
  name: OpenFGA Stores API
  slug: openfga-stores-api
artifact_total: 20
collections:
- collection_type: open
  name: OpenFGA Assertions API
  slug: open-openfga-assertions-api
- collection_type: open
  name: OpenFGA Assertions Authorization Models API
  slug: open-openfga-authorization-models-api
- collection_type: open
  name: OpenFGA Assertions AuthZenService API
  slug: open-openfga-authzenservice-api
- collection_type: open
  name: OpenFGA Assertions Relationship Queries API
  slug: open-openfga-relationship-queries-api
- collection_type: open
  name: OpenFGA Assertions Relationship Tuples API
  slug: open-openfga-relationship-tuples-api
- collection_type: open
  name: OpenFGA Assertions Stores API
  slug: open-openfga-stores-api
- collection_type: open
  name: OpenFGA
  slug: open-openfga
common:
- group: commercial
  href: https://artifacts.apis.io/openfga/plans/openfga-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openfga-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/openfga/rate-limits/openfga-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openfga-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/openfga/finops/openfga-finops.yml
  title: ''
  type: FinOps
  url: finops/openfga-finops.yml
- group: other
  href: https://artifacts.apis.io/openfga/capabilities/openfga-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openfga-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.openfga.dev/
- group: agent
  href: https://artifacts.apis.io/openfga/agentic-access/openfga-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openfga-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/openfga/security/openfga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openfga-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://openfga.dev/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openfga
- group: agent
  title: ''
  type: LlmsText
  url: https://openfga.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://openfga.dev/blog/rss.xml
created: '2026-03-16'
description: OpenFGA is a CNCF incubating high-performance authorization system implementing fine-grained access control based on the Zanzibar model. It provides a flexible relationship-based authorization engine that evaluates access decisions using a type system defined in a modeling language. OpenFGA supports authorization checks, relationship queries, and list operations through its API.
finops:
- has_sources: false
  method: generated
  name: Openfga Finops
  primary_unit: request
  service_category: API
  slug: openfga-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openfga.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.openfga.dev over HTTP; 2 tools listed.
  name: OpenFGA MCP Server
  slug: openfga
modified: '2026-05-19'
name: OpenFGA
nav: Providers
network: true
overview: 'OpenFGA publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assertions API, Authorization Models API, AuthZenService API, and 3 more. Tagged areas include Access Control, Authorization, Cloud-Native, Fine-Grained, and Incubating.


  The OpenFGA catalog on APIs.io includes 1 Spectral governance ruleset.


  OpenFGA''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Openfga Plans Pricing
  plan_count: 3
  slug: openfga-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Openfga Rate Limits
  slug: openfga-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: OpenFGA API Rules
  rule_count: 57
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 5
  slug: openfga-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 41.7
    developer_ergonomics: 11.9
    discoverability: 73.3
    operational_transparency: 13.2
  previous_composite: 25.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/openfga/openfga-2026-06-20T191007.png
security:
- kind: domain-security
  name: Openfga Domain Security
  slug: openfga-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openfga
tags:
- Access Control
- Authorization
- Cloud-Native
- Fine-Grained
- Incubating
- Zanzibar
website: https://www.openfga.dev/
---
