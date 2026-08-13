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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Finout Agentic Access
  operation_count: 15
  slug: finout-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 6
apis:
- description: Query and analyze costs using Finout Views
  name: Finout Cost API
  slug: finout-cost-api
- description: Retrieve CostGuard scans and recommendations
  name: Finout CostGuard API
  slug: finout-costguard-api
- description: Query and create notification endpoints
  name: Finout Endpoints API
  slug: finout-endpoints-api
- description: Query MegaBill keys, values, and metadata for building filters
  name: Finout Query Language API
  slug: finout-query-language-api
- description: Manage metadata for virtual tags
  name: Finout Virtual Tag Metadata API
  slug: finout-virtual-tag-metadata-api
- description: Create, retrieve, update, and delete Virtual Tag configurations
  name: Finout Virtual Tags API
  slug: finout-virtual-tags-api
artifact_total: 28
collections:
- collection_type: postman
  name: Finout Cost API
  slug: postman-finout-cost-api
- collection_type: postman
  name: Finout Cost CostGuard API
  slug: postman-finout-costguard-api
- collection_type: postman
  name: Finout Cost Endpoints API
  slug: postman-finout-endpoints-api
- collection_type: postman
  name: Finout Cost Query Language API
  slug: postman-finout-query-language-api
- collection_type: postman
  name: Finout Cost Virtual Tag Metadata API
  slug: postman-finout-virtual-tag-metadata-api
- collection_type: postman
  name: Finout Cost Virtual Tags API
  slug: postman-finout-virtual-tags-api
- collection_type: open
  name: Finout API
  slug: open-finout-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/finout/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finout-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/finout-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finout-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/finout-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finout-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finout-io
- group: company
  title: ''
  type: Website
  url: https://www.finout.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.finout.io/pricing
- group: other
  title: ''
  type: Customers
  url: https://www.finout.io/customer-stories
- group: company
  title: ''
  type: Blog
  url: https://www.finout.io/blog
- group: other
  title: ''
  type: Events
  url: https://www.finout.io/events-and-webinars
- group: other
  title: ''
  type: WhitePapers
  url: https://www.finout.io/hubfs/White%20Papers/Whitepaper%20_%20website25_02.pdf
- group: company
  title: ''
  type: About
  url: https://www.finout.io/about/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finout.io/
- group: auth
  title: ''
  type: Compliance
  url: https://www.finout.io/compliance
- group: learn
  title: ''
  type: Webinars
  url: https://www.finout.io/events-and-webinars
- group: agent
  title: ''
  type: MCPServer
  url: https://www.finout.io/blog/introducing-finouts-mcp-integration
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.finout.io/llms.txt
created: '2026-01-02'
description: Finout is an enterprise-grade FinOps solution that helps companies easily allocate, manage and reduce their cloud spending across their entire infrastructure. We make costs easy to understand across any cloud infrastructure and scalefrom AI cost to Kubernetes. From Startups to enterprises, we turn cloud chaos into clarity.
finops:
- name: Finout Finops
  service_category: API
  slug: finout-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finout.png
json_schemas:
- name: Finout CostGuard Scan
  property_count: 4
  slug: cost-guard-scan
- name: Finout Cost Query
  property_count: 3
  slug: cost-query
- name: Finout Endpoint
  property_count: 4
  slug: endpoint
- name: Finout Scan Recommendation
  property_count: 7
  slug: scan-recommendation
- name: Finout Virtual Tag
  property_count: 4
  slug: virtual-tag
jsonld:
- class_count: 2
  name: Finout Context
  property_count: 19
  slug: finout-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Finout
nav: Providers
network: true
overview: 'Finout publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cost API, CostGuard API, Endpoints API, and 3 more. Tagged areas include Budgets, Costs, and FinOps.


  The Finout catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Finout''s developer surface includes authentication, pricing, engineering blog, documentation, and 15 more developer resources.'
plans:
- name: Finout Plans Pricing
  plan_count: 3
  slug: finout-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 5
  name: Finout Rate Limits
  slug: finout-rate-limits
rules:
- name: Finout API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: finout-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 76.1
    developer_ergonomics: 34.8
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finout/refs/heads/main/screenshots/finout-2026-06-20T181223.png
security:
- kind: authentication
  name: Finout Authentication
  slug: finout-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Finout Domain Security
  slug: finout-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Finout Trust Center
  slug: finout-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: finout
tags:
- Budgets
- Costs
- FinOps
website: https://www.finout.io/
---
