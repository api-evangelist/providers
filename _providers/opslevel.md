---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Opslevel Agentic Access
  operation_count: 1
  slug: opslevel-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: 'The OpsLevel GraphQL API allows you to integrate OpsLevel with your other operational tools, enrich internal tickets, incidents, and other systems with service and team data pulled from OpsLevel. The '
  name: OpsLevel GraphQL API
  slug: graphql-api
- baseURL: https://api.opslevel.com
  baseurl_source: declared
  description: OpsLevel GraphQL endpoint.
  name: OpsLevel Graph QL API
  slug: opslevel-graph-ql-api
artifact_total: 15
collections:
- collection_type: open
  name: OpsLevel GraphQL API
  slug: open-opslevel-graphql-api
- collection_type: open
  name: OpsLevel GraphQL API
  slug: open-opslevel
common:
- group: commercial
  href: https://artifacts.apis.io/opslevel/plans/opslevel-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opslevel-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/opslevel/rate-limits/opslevel-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opslevel-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/opslevel/finops/opslevel-finops.yml
  title: ''
  type: FinOps
  url: finops/opslevel-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.opslevel.com/
- group: agent
  href: https://artifacts.apis.io/opslevel/agentic-access/opslevel-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opslevel-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/opslevel/security/opslevel-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/opslevel-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/opslevel/security/opslevel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opslevel-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/opslevel/authentication/opslevel-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opslevel-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.opslevel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opslevel.com/
- group: company
  title: ''
  type: Blog
  url: https://www.opslevel.com/resource/blog
- group: start
  title: ''
  type: Signup
  url: https://www.opslevel.com/request-a-demo
- group: start
  title: ''
  type: Login
  url: https://app.opslevel.com/users/sign_in
- group: commercial
  title: ''
  type: Pricing
  url: https://www.opslevel.com/pricing
- group: company
  title: ''
  type: About
  url: https://www.opslevel.com/about
- group: operate
  title: ''
  type: StatusPage
  url: https://opslevelstatus.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.opslevel.com/legal/t4-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.opslevel.com/legal/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.opslevel.com/legal/security
- group: operate
  title: ''
  type: Contact
  url: https://www.opslevel.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpsLevel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opslevel
- group: other
  title: ''
  type: Terraform Provider
  url: https://registry.terraform.io/providers/OpsLevel/opslevel/latest/docs
- group: other
  title: ''
  type: Customers
  url: https://www.opslevel.com/customers
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/OpsLevel/opslevel-mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.opslevel.com/llms.txt
created: '2026-03-03'
description: OpsLevel is a prescriptive internal developer portal for cataloging, measuring, and scaffolding services according to engineering best practices.
finops:
- has_sources: true
  method: derived
  name: Opslevel Finops
  primary_unit: ''
  service_category: ''
  slug: opslevel-finops
  template: true
graphqls:
- description: 'The OpsLevel GraphQL API allows you to integrate OpsLevel with your other operational tools, enrich internal tickets, incidents, and other systems with service and team data pulled from OpsLevel. The '
  name: OpsLevel GraphQL API
  slug: opslevel-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opslevel.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Remote MCP server at app.opslevel.com over HTTP.
  name: OpsLevel MCP Server
  slug: opslevel
modified: '2026-05-19'
name: OpsLevel
nav: Providers
network: true
overview: 'OpsLevel publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Graph QL API, and 1 more. Tagged areas include Developer Portal, Developer Tools, DevOps, Experience, and Internal Developer Portal.


  The OpsLevel catalog on APIs.io includes 1 Spectral governance ruleset.


  OpsLevel''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, pricing, and 20 more developer resources.'
plans:
- name: Opslevel Plans Pricing
  plan_count: 2
  slug: opslevel-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Opslevel Rate Limits
  slug: opslevel-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: OpsLevel API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: opslevel-rules
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 47.5
    catalog_earned_first_party: 8.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.1
  facets:
    access_clarity: 59.2
    contract_governance: 13.6
    contract_quality: 53.9
    developer_ergonomics: 39.3
    discoverability: 66.7
    operational_transparency: 36.8
  previous_composite: 45.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/opslevel/opslevel-2026-06-20T191105.png
security:
- kind: authentication
  name: Opslevel Authentication
  slug: opslevel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opslevel Domain Security
  slug: opslevel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Opslevel Vulnerability Disclosure
  slug: opslevel-vulnerability-disclosure
  summary_line: no policy recorded
slug: opslevel
tags:
- Developer Portal
- Developer Tools
- DevOps
- Experience
- Internal Developer Portal
- Microservices
- Platform Engineering
- Service Catalog
- Service Maturity
website: https://www.opslevel.com/
---
