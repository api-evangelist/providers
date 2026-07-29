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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Topaz Agentic Access
  operation_count: 15
  slug: topaz-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 5
apis:
- description: Policy-driven decisions - is, decisiontree, and query - evaluated by the OPA engine.
  name: Topaz Authorizer API
  slug: topaz-authorizer-api
- description: Graph-based check and graph-expansion queries over the directory.
  name: Topaz Directory Checks API
  slug: topaz-directory-checks-api
- description: Objects in the Zanzibar-style directory - users, groups, resources, and other entities.
  name: Topaz Directory Objects API
  slug: topaz-directory-objects-api
- description: Relations (tuples) connecting subjects to objects in the directory graph.
  name: Topaz Directory Relations API
  slug: topaz-directory-relations-api
- description: OPA policy modules loaded into the authorizer.
  name: Topaz Policies API
  slug: topaz-policies-api
artifact_total: 10
collections:
- collection_type: open
  name: Topaz Authorizer and Directory API
  slug: open-topaz
common:
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
overview: 'Topaz publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authorizer API, Directory Checks API, Directory Objects API, and 2 more. Tagged areas include Access Control, Authorization, Fine-Grained Authorization, Open Source, and RBAC.


  Topaz''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Topaz Plans Pricing
  plan_count: 2
  slug: topaz-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Topaz Rate Limits
  slug: topaz-rate-limits
score:
  band: thin
  composite: 33.2
  delta: -2.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 57.6
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
slug: topaz
tags:
- Access Control
- Authorization
- Fine-Grained Authorization
- Open Source
- RBAC
- ReBAC
- Zanzibar
- OPA
- Policy as Code
website: https://www.topaz.sh/
---
