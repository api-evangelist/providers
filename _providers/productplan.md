---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Productplan Agentic Access
  operation_count: 64
  slug: productplan-agentic-access
  summary_line: 64 operations · 32 acting
api_count: 8
apis:
- description: Manage bars (features/items) within roadmaps
  name: ProductPlan Bars API
  slug: productplan-bars-api
- description: Manage ideas, opportunities, customers, and idea forms
  name: ProductPlan Discovery API
  slug: productplan-discovery-api
- description: Manage launches, checklist sections, and tasks
  name: ProductPlan Launches API
  slug: productplan-launches-api
- description: Manage roadmaps, lanes, milestones, bars, and comments
  name: ProductPlan Roadmaps API
  slug: productplan-roadmaps-api
- description: Application status
  name: ProductPlan Status API
  slug: productplan-status-api
- description: Manage OKR objectives and key results
  name: ProductPlan Strategy API
  slug: productplan-strategy-api
- description: List teams
  name: ProductPlan Teams API
  slug: productplan-teams-api
- description: List account users
  name: ProductPlan Users API
  slug: productplan-users-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ProductPlan REST Bars API
  slug: open-productplan-bars-api
- collection_type: open
  name: ProductPlan REST Bars Discovery API
  slug: open-productplan-discovery-api
- collection_type: open
  name: ProductPlan REST Bars Launches API
  slug: open-productplan-launches-api
- collection_type: open
  name: ProductPlan REST Bars Roadmaps API
  slug: open-productplan-roadmaps-api
- collection_type: open
  name: ProductPlan REST Bars Status API
  slug: open-productplan-status-api
- collection_type: open
  name: ProductPlan REST Bars Strategy API
  slug: open-productplan-strategy-api
- collection_type: open
  name: ProductPlan REST Bars Teams API
  slug: open-productplan-teams-api
- collection_type: open
  name: ProductPlan REST Bars Users API
  slug: open-productplan-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/productplan-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/productplan-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/productplan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/productplan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/productplan-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.productplan.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.productplan.com/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ProductPlan
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/productplan
- group: company
  title: ''
  type: Blog
  url: https://www.productplan.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.productplan.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.productplan.com
- group: other
  title: ''
  type: X
  url: https://x.com/ProductPlan
- group: commercial
  title: ''
  type: Plans
  url: plans/productplan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/productplan-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/productplan-finops.yml
created: '2026-06-13'
description: ProductPlan is a road mapping software platform providing a REST API for creating and managing roadmaps, features, goals, OKRs, launches, and discovery. It integrates with tools like Jira, GitHub, Slack, and Trello, enabling teams to plan, align, and share product strategies with stakeholders.
examples:
- key_count: 12
  name: Bar Create
  slug: bar-create
- key_count: 1
  name: Bar Response
  slug: bar-response
- key_count: 3
  name: Idea Create
  slug: idea-create
- key_count: 1
  name: Key Result Update
  slug: key-result-update
- key_count: 2
  name: Objective Create
  slug: objective-create
- key_count: 2
  name: Roadmap List Response
  slug: roadmap-list-response
finops:
- name: Productplan Finops
  service_category: ''
  slug: productplan-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/productplan.png
json_schemas:
- name: Bar
  property_count: 19
  slug: bar
- name: Idea
  property_count: 6
  slug: idea
- name: KeyResult
  property_count: 7
  slug: key-result
- name: Launch
  property_count: 6
  slug: launch
- name: Objective
  property_count: 5
  slug: objective
- name: Roadmap
  property_count: 5
  slug: roadmap
jsonld:
- class_count: 46
  name: Productplan Context
  property_count: 16
  slug: productplan-context
layout: provider
modified: '2026-06-13'
name: ProductPlan
nav: Providers
network: true
overview: 'ProductPlan publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bars API, Discovery API, Launches API, and 5 more. Tagged areas include Roadmapping, Product Management, OKR, Roadmaps, and Features.


  The ProductPlan catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ProductPlan''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Productplan Plans Pricing
  plan_count: 1
  slug: productplan-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Productplan Rate Limits
  slug: productplan-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ProductPlan API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: productplan-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.5
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 63.5
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/productplan/refs/heads/main/screenshots/productplan-2026-06-20T192137.png
security:
- kind: authentication
  name: Productplan Authentication
  slug: productplan-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Productplan Domain Security
  slug: productplan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Productplan Vulnerability Disclosure
  slug: productplan-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Productplan Trust Center
  slug: productplan-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: productplan
tags:
- Roadmapping
- Product Management
- OKR
- Roadmaps
- Features
- Product Strategy
- Launches
- Discovery
- Integration
website: https://www.productplan.com
---
