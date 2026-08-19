---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: true
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
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 48
  human_in_the_loop: 3
  name: Widen Agentic Access
  operation_count: 90
  slug: widen-agentic-access
  summary_line: 90 operations · 48 acting · 3 human-in-the-loop
api_count: 17
apis:
- description: Create, list, retrieve, edit, ping, and delete DAM asset webhooks.
  name: Widen Acquia-DAM-Webhooks API
  slug: widen-acquia-dam-webhooks-api
- description: Asset download, share, and view analytics endpoints.
  name: Widen Analytics API
  slug: widen-analytics-api
- description: Create, retrieve, update, delete, and search digital assets.
  name: Widen Assets API
  slug: widen-assets-api
- description: List product attributes and controlled vocabulary values.
  name: Widen Attributes API
  slug: widen-attributes-api
- description: Manage asset categories and category trees.
  name: Widen Categories API
  slug: widen-categories-api
- description: List product channels.
  name: Widen Channels API
  slug: widen-channels-api
- description: Create and list asset collections.
  name: Widen Collections API
  slug: widen-collections-api
- description: List recognized file formats.
  name: Widen File-Formats API
  slug: widen-file-formats-api
- description: Register and remove integration links on assets.
  name: Widen Integration-Links API
  slug: widen-integration-links-api
- description: Manage metadata fields and controlled vocabulary values.
  name: Widen Metadata API
  slug: widen-metadata-api
- description: Create and manage asset orders and conversions.
  name: Widen Orders API
  slug: widen-orders-api
- description: Create, retrieve, update, and search products (Acquia Entries).
  name: Widen Products API
  slug: widen-products-api
- description: Instant Search Connector integration URL.
  name: Widen Search-Connector API
  slug: widen-search-connector-api
- description: API usage summary.
  name: Widen Usage API
  slug: widen-usage-api
- description: Retrieve user and contact information.
  name: Widen Users API
  slug: widen-users-api
- description: Manage workflow projects and deliverables.
  name: Widen Workflow-App-Projects API
  slug: widen-workflow-app-projects-api
- description: Create, list, and delete workflow webhooks.
  name: Widen Workflow-Webhooks API
  slug: widen-workflow-webhooks-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks API
  slug: open-widen-acquia-dam-webhooks-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Analytics API
  slug: open-widen-analytics-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Assets API
  slug: open-widen-assets-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Attributes API
  slug: open-widen-attributes-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Categories API
  slug: open-widen-categories-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Channels API
  slug: open-widen-channels-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Collections API
  slug: open-widen-collections-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks File-Formats API
  slug: open-widen-file-formats-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Integration-Links API
  slug: open-widen-integration-links-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Metadata API
  slug: open-widen-metadata-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Orders API
  slug: open-widen-orders-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Products API
  slug: open-widen-products-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Search-Connector API
  slug: open-widen-search-connector-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Usage API
  slug: open-widen-usage-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Users API
  slug: open-widen-users-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Workflow-App-Projects API
  slug: open-widen-workflow-app-projects-api
- collection_type: open
  name: Acquia DAM (Widen) Acquia-DAM-Webhooks Workflow-Webhooks API
  slug: open-widen-workflow-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/widen-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/widen-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/widen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/widen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/widen-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.acquia.com/products/acquia-dam
- group: docs
  title: ''
  type: Documentation
  url: https://docs.acquia.com/acquia-dam
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/widen
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/widen-enterprises
- group: company
  title: ''
  type: Blog
  url: https://www.acquia.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acquia.com/products/acquia-dam
- group: operate
  title: ''
  type: StatusPage
  url: https://status.acquia.com/
- group: other
  title: ''
  type: X
  url: https://x.com/widencollective
- group: commercial
  title: ''
  type: Plans
  url: plans/widen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/widen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/widen-finops.yml
created: '2026-06-13'
description: Acquia Digital Asset Management (formerly Widen Collective) provides a REST API for managing digital assets, metadata, collections, embed codes, and asset distribution workflows. The API supports asset search and discovery, metadata management, analytics, orders, products, webhooks, and workflow automation across both v1 and v2 endpoints.
finops:
- name: Widen Finops
  service_category: ''
  slug: widen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/widen.png
layout: provider
modified: '2026-06-13'
name: Widen
nav: Providers
network: true
overview: 'Widen publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Acquia-DAM-Webhooks API, Analytics API, Assets API, and 14 more. Tagged areas include Digital Asset Management, DAM, Media, Assets, and Metadata.


  Widen''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Widen Plans Pricing
  plan_count: 3
  slug: widen-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 3
  name: Widen Rate Limits
  slug: widen-rate-limits
score:
  band: developing
  composite: 43.6
  delta: -0.1
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/widen/refs/heads/main/screenshots/widen-2026-06-20T201453.png
security:
- kind: authentication
  name: Widen Authentication
  slug: widen-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Widen Domain Security
  slug: widen-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Widen Vulnerability Disclosure
  slug: widen-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Widen Trust Center
  slug: widen-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: widen
tags:
- Digital Asset Management
- DAM
- Media
- Assets
- Metadata
- Collections
- Workflows
- Acquia
website: https://www.acquia.com/products/acquia-dam
---
