---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Presto Foundation Agentic Access
  operation_count: 3
  slug: presto-foundation-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: The Presto Client REST API is the HTTP protocol used by Presto clients to submit SQL queries to a Presto coordinator and stream back results. It centers on POST /v1/statement to submit a query, GET on
  name: Presto Client REST API
  slug: presto-client-rest-api
- description: The Presto Coordinator REST API exposes resources for inspecting and managing a running Presto cluster, including Node, Query, Stage, Statement, and Task resources. These endpoints are served by the c
  name: Presto Coordinator REST API
  slug: presto-coordinator-rest-api
- description: Submit, page, and cancel SQL queries.
  name: Presto Foundation Statement API
  slug: presto-foundation-statement-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Presto Client REST Statement API
  slug: open-presto-foundation-statement-api
- collection_type: open
  name: Presto Client REST API
  slug: open-presto-foundation
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/prestodb/presto/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/presto-foundation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/presto-foundation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/presto-foundation-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/presto-foundation-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/presto-foundation
- group: start
  title: ''
  type: Portal
  url: https://prestodb.io/
- group: docs
  title: ''
  type: Documentation
  url: https://prestodb.io/docs/current/
- group: other
  title: ''
  type: Foundation
  url: https://prestodb.io/foundation/
- group: company
  title: ''
  type: Blog
  url: https://prestodb.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://prestodb.io/community/
- group: other
  title: ''
  type: Events
  url: https://prestodb.io/events/
- group: other
  title: ''
  type: Resources
  url: https://prestodb.io/resources/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prestodb
- group: operate
  title: ''
  type: Slack
  url: https://communityinviter.com/apps/prestodb/prestodb
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/prestodb
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/PrestoDB
- group: other
  title: ''
  type: Linux Foundation
  url: https://www.linuxfoundation.org/projects/case-studies/presto/
created: '2026-03-16'
description: The Presto Foundation is a Linux Foundation project supporting Presto, an open source distributed SQL query engine for big data analytics. Founded by Facebook (Meta), Uber, Twitter, and Alibaba, Presto enables interactive analytics across diverse data sources at massive scale, with a vendor-neutral governance model and an active ecosystem of contributors and integrations.
finops:
- name: Presto Foundation Finops
  service_category: API
  slug: presto-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/presto-foundation.png
layout: provider
modified: '2026-04-28'
name: Presto Foundation
nav: Providers
network: true
overview: 'Presto Foundation publishes 1 API on the [APIs.io](https://apis.io/) network: Statement API. Tagged areas include Analytics, Big Data, Distributed SQL, Linux Foundation, and Open-Source.


  Presto Foundation''s developer surface includes authentication, developer portal, documentation, engineering blog, YouTube channel, and 13 more developer resources.'
plans:
- name: Presto Foundation Plans Pricing
  plan_count: 3
  slug: presto-foundation-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Presto Foundation Rate Limits
  slug: presto-foundation-rate-limits
scopes:
- name: Presto Foundation Scopes
  scope_count: 0
  slug: presto-foundation-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.9
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.2
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 29.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/presto-foundation/refs/heads/main/screenshots/presto-foundation-2026-06-20T192054.png
security:
- kind: authentication
  name: Presto Foundation Authentication
  slug: presto-foundation-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Presto Foundation Domain Security
  slug: presto-foundation-domain-security
  summary_line: TLSv1.3 · DMARC
slug: presto-foundation
tags:
- Analytics
- Big Data
- Distributed SQL
- Linux Foundation
- Open-Source
- Query Engine
- SQL
website: https://prestodb.io/
---
