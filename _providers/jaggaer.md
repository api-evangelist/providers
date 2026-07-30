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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Jaggaer Agentic Access
  operation_count: 50
  slug: jaggaer-agentic-access
  summary_line: 50 operations · 20 acting
api_count: 16
apis:
- description: Asynchronous process status operations
  name: JAGGAER Async API
  slug: jaggaer-async-api
- description: Event attribute management
  name: JAGGAER Attributes API
  slug: jaggaer-attributes-api
- description: Award scenario retrieval
  name: JAGGAER Awards API
  slug: jaggaer-awards-api
- description: Bid submission retrieval
  name: JAGGAER Bids API
  slug: jaggaer-bids-api
- description: Event contact management
  name: JAGGAER Contacts API
  slug: jaggaer-contacts-api
- description: Customer host management operations
  name: JAGGAER Customer Hosts API
  slug: jaggaer-customer-hosts-api
- description: Sourcing event operations
  name: JAGGAER Events API
  slug: jaggaer-events-api
- description: Event item management
  name: JAGGAER Items API
  slug: jaggaer-items-api
- description: Optimization job management operations
  name: JAGGAER Jobs API
  slug: jaggaer-jobs-api
- description: Location and rate structure operations
  name: JAGGAER Locations API
  slug: jaggaer-locations-api
- description: Event rate retrieval
  name: JAGGAER Rates API
  slug: jaggaer-rates-api
- description: Event scenario retrieval
  name: JAGGAER Scenarios API
  slug: jaggaer-scenarios-api
- description: Event supplier management
  name: JAGGAER Suppliers API
  slug: jaggaer-suppliers-api
- description: Template management operations
  name: JAGGAER Templates API
  slug: jaggaer-templates-api
- description: Entity upload URL generation
  name: JAGGAER Uploads API
  slug: jaggaer-uploads-api
- description: User administration operations
  name: JAGGAER Users API
  slug: jaggaer-users-api
artifact_total: 32
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jaggaer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jaggaer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jaggaer-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.jaggaer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asodocs.jaggaer.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Jaggaer-Direct
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jaggaer/
- group: company
  title: ''
  type: Blog
  url: https://www.jaggaer.com/blog
- group: other
  title: ''
  type: X
  url: https://x.com/jaggaerpro
- group: operate
  title: ''
  type: Support
  url: https://www.jaggaer.com/support
- group: commercial
  title: ''
  type: Plans
  url: plans/jaggaer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/jaggaer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/jaggaer-finops.yml
created: '2026-06-13'
description: JAGGAER is an AI-powered procurement and supplier management platform serving 1,400+ enterprises worldwide, managing $2.9 trillion in annual spend and connecting 13 million suppliers globally. The platform provides REST APIs for sourcing optimization, contract management, supplier information management, purchasing, and spend analytics. JAGGAER's Advanced Sourcing Optimizer (ASO) APIs enable system-to-system integration using OAuth 2.0 bearer tokens and API keys to automate procurement workflows across source-to-pay and procure-to-pay use cases. The platform integrates with 40+ ERP systems including SAP, Oracle, Workday, and Microsoft Dynamics, supporting bidirectional communications for enterprise procurement automation.
examples:
- key_count: 2
  name: Jaggaer Async Status Response
  slug: jaggaer-async-status-response
- key_count: 2
  name: Jaggaer Create Event Request
  slug: jaggaer-create-event-request
- key_count: 16
  name: Jaggaer Job Response
  slug: jaggaer-job-response
- key_count: 5
  name: Jaggaer Submit Job Request
  slug: jaggaer-submit-job-request
- key_count: 1
  name: Jaggaer Submit Job Response
  slug: jaggaer-submit-job-response
finops:
- name: Jaggaer Finops
  service_category: ''
  slug: jaggaer-finops
graphqls:
- description: JAGGAER is a direct and indirect spend management platform covering procurement, sourcing, contract management, supplier management, and accounts payable. The API covers RFx events, PO lifecycle, supp
  name: JAGGAER GraphQL API
  slug: jaggaer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jaggaer.png
json_schemas:
- name: JAGGAER Quay Optimization Job
  property_count: 18
  slug: jaggaer-optimization-job
- name: JAGGAER Sourcing Event
  property_count: 10
  slug: jaggaer-sourcing-event
jsonld:
- class_count: 0
  name: Jaggaer Context
  property_count: 63
  slug: jaggaer-context
layout: provider
modified: '2026-06-13'
name: JAGGAER
nav: Providers
network: true
overview: 'JAGGAER publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Async API, Attributes API, Awards API, and 13 more. Tagged areas include Procurement, Sourcing, Supplier Management, Contracts, and Spend Analytics.


  The JAGGAER catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JAGGAER''s developer surface includes authentication, documentation, engineering blog, support, and 9 more developer resources.'
plans:
- name: Jaggaer Plans Pricing
  plan_count: 4
  slug: jaggaer-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 0
  name: Jaggaer Rate Limits
  slug: jaggaer-rate-limits
rules:
- name: JAGGAER API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: jaggaer-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.4
  delta: -3.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.8
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jaggaer/refs/heads/main/screenshots/jaggaer-2026-06-20T183653.png
security:
- kind: authentication
  name: Jaggaer Authentication
  slug: jaggaer-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Jaggaer Domain Security
  slug: jaggaer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jaggaer
tags:
- Procurement
- Sourcing
- Supplier Management
- Contracts
- Spend Analytics
- eProcurement
- Source-to-Pay
- Procure-to-Pay
website: https://www.jaggaer.com/
---
