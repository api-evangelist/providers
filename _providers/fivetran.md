---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Fivetran Agentic Access
  operation_count: 36
  slug: fivetran-agentic-access
  summary_line: 36 operations · 23 acting
api_count: 1
apis:
- description: The Fivetran REST API allows programmatic management of all platform resources including users, roles, teams, groups, destinations, connections, webhooks, transformations, transformation projects, cer
  name: Fivetran REST API
  slug: fivetran-rest-api
- baseURL: https://api.fivetran.com/v1
  baseurl_source: declared
  description: The Connections API from Fivetran — 7 operation(s) for connections.
  name: Fivetran Connections API
  slug: fivetran-connections-api
- baseURL: https://api.fivetran.com/v1
  baseurl_source: declared
  description: The Destinations API from Fivetran — 2 operation(s) for destinations.
  name: Fivetran Destinations API
  slug: fivetran-destinations-api
- baseURL: https://api.fivetran.com/v1
  baseurl_source: declared
  description: The Groups API from Fivetran — 2 operation(s) for groups.
  name: Fivetran Groups API
  slug: fivetran-groups-api
- baseURL: https://api.fivetran.com/v1
  baseurl_source: declared
  description: The Metadata API from Fivetran — 1 operation(s) for metadata.
  name: Fivetran Metadata API
  slug: fivetran-metadata-api
- baseURL: https://api.fivetran.com/v1
  baseurl_source: declared
  description: The Roles API from Fivetran — 1 operation(s) for roles.
  name: Fivetran Roles API
  slug: fivetran-roles-api
- baseURL: https://api.fivetran.com/v1
  baseurl_source: declared
  description: The Teams API from Fivetran — 1 operation(s) for teams.
  name: Fivetran Teams API
  slug: fivetran-teams-api
- baseURL: https://api.fivetran.com/v1
  baseurl_source: declared
  description: The Users API from Fivetran — 2 operation(s) for users.
  name: Fivetran Users API
  slug: fivetran-users-api
- baseURL: https://api.fivetran.com/v1
  baseurl_source: declared
  description: The Webhooks API from Fivetran — 5 operation(s) for webhooks.
  name: Fivetran Webhooks API
  slug: fivetran-webhooks-api
artifact_total: 47
collections:
- collection_type: open
  name: Fivetran REST Connections API
  slug: open-fivetran-connections-api
- collection_type: open
  name: Fivetran REST Connections Destinations API
  slug: open-fivetran-destinations-api
- collection_type: open
  name: Fivetran REST Connections Groups API
  slug: open-fivetran-groups-api
- collection_type: open
  name: Fivetran REST Connections Metadata API
  slug: open-fivetran-metadata-api
- collection_type: open
  name: Fivetran REST Connections Roles API
  slug: open-fivetran-roles-api
- collection_type: open
  name: Fivetran REST Connections Teams API
  slug: open-fivetran-teams-api
- collection_type: open
  name: Fivetran REST Connections Users API
  slug: open-fivetran-users-api
- collection_type: open
  name: Fivetran REST Connections Webhooks API
  slug: open-fivetran-webhooks-api
- collection_type: open
  name: Fivetran REST API
  slug: open-fivetran
common:
- group: commercial
  href: https://artifacts.apis.io/fivetran/plans/fivetran-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fivetran-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fivetran/rate-limits/fivetran-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fivetran-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fivetran/finops/fivetran-finops.yml
  title: ''
  type: FinOps
  url: finops/fivetran-finops.yml
- group: agent
  href: https://artifacts.apis.io/fivetran/agentic-access/fivetran-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fivetran-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fivetran/security/fivetran-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fivetran-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fivetran/security/fivetran-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fivetran-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fivetran/authentication/fivetran-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fivetran-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fivetran
- group: company
  title: ''
  type: Website
  url: https://www.fivetran.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fivetran.com/docs
- group: docs
  title: ''
  type: REST API Documentation
  url: https://fivetran.com/docs/rest-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fivetran
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/fivetran/fivetran-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/fivetran/claude-sap-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://fivetran.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.fivetran.com/blog/rss.xml
created: '2026-03-27'
description: Fivetran is an automated data integration platform providing pre-built connectors for syncing data from SaaS applications, databases, and APIs into cloud data warehouses. The Fivetran REST API exposes management of users, groups, teams, roles, destinations, connections, transformations, webhooks, certificates, and connector metadata.
features:
- 'Free: low-volume usage included'
- 'Paid Connections: $5 base for 1M MAR, tiered declining above'
- 'Transformations: free under 5K runs, $0.01 above, declining at scale'
- 'Enterprise: PrivateLink, Hybrid, HIPAA, BAA, audit logs'
- Annual contracts save up to 22%
- 500+ pre-built connectors (SaaS, DBs, files, events)
- 'Destinations: Snowflake, BigQuery, Redshift, Databricks, Postgres, etc.'
- 'Management API: 600 req/min/account'
- Sync frequency from 24/day (Free) to 1-minute (Paid)
- dbt Core integration for transformations
- Quickstart Data Models
- Custom connectors via Connector SDK
- Webhooks for sync events
- OAuth 2.0 + service accounts
- PrivateLink, Hybrid Deployment (Enterprise)
- Customer-managed encryption keys (Enterprise)
finops:
- has_sources: true
  method: generated
  name: Fivetran Finops
  primary_unit: ''
  service_category: Data Integration
  slug: fivetran-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fivetran.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Fivetran
nav: Providers
network: true
overview: 'Fivetran publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Connections API, Destinations API, Groups API, and 6 more. Tagged areas include Connectors, Data Integration, Data Pipeline, ETL, and Software-as-a-Service.


  The Fivetran catalog on APIs.io includes 1 Spectral governance ruleset.


  Fivetran''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Fivetran Plans Pricing
  plan_count: 4
  slug: fivetran-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 3
  name: Fivetran Rate Limits
  slug: fivetran-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Fivetran API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: fivetran-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 18.2
    contract_quality: 48.7
    developer_ergonomics: 37.5
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fivetran/fivetran-2026-06-20T181255.png
security:
- kind: authentication
  name: Fivetran Authentication
  slug: fivetran-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fivetran Domain Security
  slug: fivetran-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fivetran Trust Center
  slug: fivetran-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
skill_count: 4
skills:
- name: fivetran-create-and-sync-connection
  slug: fivetran-create-and-sync-connection
- name: fivetran-create-and-test-webhook
  slug: fivetran-create-and-test-webhook
- name: fivetran-create-retrieve-group
  slug: fivetran-create-retrieve-group
- name: fivetran-manage-destination
  slug: fivetran-manage-destination
slug: fivetran
tags:
- Connectors
- Data Integration
- Data Pipeline
- ETL
- Software-as-a-Service
- Unified API
website: https://www.fivetran.com/
---
