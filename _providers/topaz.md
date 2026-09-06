---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Topaz Agentic Access
  operation_count: 15
  slug: topaz-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 1
apis:
- baseURL: https://localhost:8383
  baseurl_source: declared
  description: Policy-driven decisions - is, decisiontree, and query - evaluated by the OPA engine.
  name: Topaz Authorizer API
  slug: topaz-authorizer-api
- baseURL: https://localhost:8383
  baseurl_source: declared
  description: Graph-based check and graph-expansion queries over the directory.
  name: Topaz Directory Checks API
  slug: topaz-directory-checks-api
- baseURL: https://localhost:8383
  baseurl_source: declared
  description: Objects in the Zanzibar-style directory - users, groups, resources, and other entities.
  name: Topaz Directory Objects API
  slug: topaz-directory-objects-api
- baseURL: https://localhost:8383
  baseurl_source: declared
  description: Relations (tuples) connecting subjects to objects in the directory graph.
  name: Topaz Directory Relations API
  slug: topaz-directory-relations-api
- baseURL: https://localhost:8383
  baseurl_source: declared
  description: OPA policy modules loaded into the authorizer.
  name: Topaz Policies API
  slug: topaz-policies-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Topaz and Directory Authorizer API
  slug: open-topaz-authorizer-api
- collection_type: open
  name: Topaz and Directory Authorizer Directory Checks API
  slug: open-topaz-directory-checks-api
- collection_type: open
  name: Topaz and Directory Authorizer Directory Objects API
  slug: open-topaz-directory-objects-api
- collection_type: open
  name: Topaz and Directory Authorizer Directory Relations API
  slug: open-topaz-directory-relations-api
- collection_type: open
  name: Topaz and Directory Authorizer Policies API
  slug: open-topaz-policies-api
- collection_type: open
  name: Topaz Authorizer and Directory API
  slug: open-topaz
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/aserto-dev/topaz/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/aserto-dev/topaz/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/aserto-dev/topaz/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/aserto-dev/topaz/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/aserto-dev/topaz/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/aserto-dev/topaz/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/topaz-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aserto-dev/topaz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aserto
- group: company
  title: ''
  type: Website
  url: https://www.topaz.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://www.topaz.sh/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/topaz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/topaz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/topaz-finops.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/aserto-dev/topaz
created: '2026-07-11'
description: Topaz is an open-source (Apache-2.0) authorizer for fine-grained, policy-based, real-time access control for applications and APIs, maintained by Aserto (github.com/aserto-dev/topaz). It combines the Open Policy Agent (OPA) decision engine with a built-in Zanzibar-style relationship directory, so you can express authorization as policy-as-code and model RBAC, ReBAC, and ABAC over an object graph of users, groups, resources, and relations. Topaz is self-hosted - you run the authorizer yourself (Docker or binary) and it exposes gRPC plus REST (gRPC-gateway) APIs from your own instance. The Authorizer API answers decisions (is, decisiontree, query); the Directory API reads and writes objects, relations, and permission checks; and a local web Console ships alongside. Aserto is the commercial hosted control plane built on Topaz for centrally managing policies, data, and decision logs across many deployed authorizers.
finops:
- name: Topaz Finops
  service_category: Identity and Access Management
  slug: topaz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/topaz.png
layout: provider
modified: '2026-07-11'
name: Topaz
nav: Providers
network: true
overview: 'Topaz publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authorizer API, Directory Checks API, Directory Objects API, and 2 more. Tagged areas include Access Control, Authorization, Fine-Grained Authorization, Open-Source, and RBAC.


  Topaz''s developer surface includes documentation and 14 more developer resources.'
plans:
- name: Topaz Plans Pricing
  plan_count: 2
  slug: topaz-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Topaz Rate Limits
  slug: topaz-rate-limits
score:
  band: developing
  composite: 39.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.7
    developer_ergonomics: 17.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 60.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/topaz/refs/heads/main/screenshots/topaz-2026-09-02T163918.png
slug: topaz
tags:
- Access Control
- Authorization
- Fine-Grained Authorization
- Open-Source
- RBAC
- ReBAC
- Zanzibar
- OPA
- Policy as Code
website: https://www.topaz.sh/
---
