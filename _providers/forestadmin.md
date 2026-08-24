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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The Forest Admin Admin Backend is a REST API deployed on the customer's own infrastructure. It translates UI calls from the Forest Admin browser interface into database queries covering CRUD operation
  name: Forest Admin REST API (Admin Backend)
  slug: admin-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forestadmin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.forestadmin.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.forestadmin.com/documentation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ForestAdmin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forestadmin
- group: company
  title: ''
  type: Blog
  url: https://www.forestadmin.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.forestadmin.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.forestadmin.com
- group: operate
  title: ''
  type: Community
  url: https://community.forestadmin.com
- group: commercial
  title: ''
  type: Plans
  url: plans/forestadmin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forestadmin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/forestadmin-finops.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/forestadmin-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/forestadmin-context.jsonld
created: 2026-06-12
description: Forest Admin is an ops orchestration platform and internal tool builder that enables operations and compliance teams to manage data, workflows, and business processes through a customizable admin panel. It uses an agent-based architecture where developers deploy a REST API agent (Admin Backend) on their own infrastructure, keeping data entirely within client-controlled servers. The platform supports Node.js, Ruby on Rails, Python (Django/Flask), and PHP (Laravel/Symfony) agents that introspect data models and expose CRUD, filtering, pagination, and sorting capabilities through a generated Admin API. Forest Admin includes role-based access control (RBAC), JWT-based dual authentication, AI-assisted workflows, MCP server integration, SOC 2 compliance, and human-AI collaboration features for regulated industries such as fintech, KYC/AML, and payments operations.
finops:
- name: Forestadmin Finops
  service_category: ''
  slug: forestadmin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forestadmin.png
jsonld:
- class_count: 12
  name: Forestadmin Context
  property_count: 20
  slug: forestadmin-context
layout: provider
modified: 2026-06-12
name: Forest Admin
nav: Providers
network: true
overview: 'Forest Admin publishes 1 API on the [APIs.io](https://apis.io/) network: REST API (Admin Backend). Tagged areas include Admin Panel, Internal Tools, RBAC, Workflow-Automation, and CRUD.


  The Forest Admin catalog on APIs.io includes 1 JSON-LD context.


  Forest Admin''s developer surface includes documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Forestadmin Plans Pricing
  plan_count: 3
  slug: forestadmin-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 4
  name: Forestadmin Rate Limits
  slug: forestadmin-rate-limits
score:
  band: thin
  composite: 35.0
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 43.7
    developer_ergonomics: 4.8
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 34.2
  previous_composite: 35.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forestadmin/refs/heads/main/screenshots/forestadmin-2026-06-20T181423.png
security:
- kind: domain-security
  name: Forestadmin Domain Security
  slug: forestadmin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: forestadmin
tags:
- Admin Panel
- Internal Tools
- RBAC
- Workflow-Automation
- CRUD
- Fintech
- Compliance
- Low-Code
- AI Agents
website: https://www.forestadmin.com
---
