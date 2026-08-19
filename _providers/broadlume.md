---
access_model:
  confidence: medium
  label: Documented, key required
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://developer.broadlume.com/bms
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for Broadlume BMS, the flooring business management system formerly known as RollMaster. 256 documented operations across 28 resource groups covering orders, quotes, leads, customers, product
  name: Broadlume BMS API
  slug: bms
artifact_total: 7
collections:
- collection_type: open
  name: Broadlume BMS API
  slug: open-broadlume-bms
common:
- group: company
  title: ''
  type: Website
  url: https://broadlume.com/
- group: company
  title: ''
  type: Blog
  url: https://www.broadlume.com/resources/blog
- group: start
  title: ''
  type: Login
  url: https://www.broadlume.com/retailer-login
- group: start
  title: ''
  type: SignUp
  url: https://www.broadlume.com/schedule-a-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.broadlume.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.broadlume.com/terms-of-use
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.broadlume.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.broadlume.com/bms
- group: docs
  title: ''
  type: APIReference
  url: https://developer.broadlume.com/bms
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.broadlume.com/bms/authentication
- group: start
  title: ''
  type: Sandbox
  url: https://developer.broadlume.com/api-runner/broadlume/bms
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/broadlume-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/broadlume
- group: auth
  title: ''
  type: DomainSecurity
  url: security/broadlume-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/broadlume-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/broadlume-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/broadlume-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/broadlume-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/broadlume-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/broadlume-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/broadlume-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/broadlume-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/broadlume-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/broadlume-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/broadlume-bms-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/broadlume-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/broadlume-rate-limits.yml
created: '2026-07-17'
description: Broadlume is an all-in-one business platform for the flooring industry, serving more than 4,000 retailers and 300+ manufacturers. Its products span lead-generating websites, digital advertising, SEO and reputation management, product catalogs, and a suite of flooring business software covering accounting, inventory management, job costing, and lead management, plus a retail selling system with in-store visualization and e-commerce sample ordering. Broadlume publishes a public developer portal at developer.broadlume.com documenting the Broadlume BMS API — the REST interface to its flooring ERP, formerly known as RollMaster, which Broadlume acquired in November 2021 — covering orders, quotes, leads, customers, products, inventory, purchase orders, invoicing, accounts receivable, general ledger, installation scheduling and handheld barcode operations. Broadlume is owned by Cyncly.
image: https://optimise2.assets-servd.host/broadlume-platform/production/images/Notebooks.png?w=1200&h=630&q=82&auto=format&fit=crop&dm=1663075995&s=fbf90ba9ce3de4a4318d0dd612edb58a
layout: provider
mcp_servers:
- description: ''
  name: broadlume-mcp.yml
  slug: broadlume-mcpyml
modified: '2026-08-13'
name: Broadlume
nav: Providers
network: true
overview: 'Broadlume publishes 1 API on the [APIs.io](https://apis.io/) network: BMS API. Tagged areas include Company, Flooring, Retail, Marketing, and Websites.


  Broadlume''s developer surface includes engineering blog, signup flow, documentation, API reference, getting-started guide, sandbox, changelog, and 21 more developer resources.'
plans:
- name: Broadlume Plans Pricing
  plan_count: 0
  slug: broadlume-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 0
  name: Broadlume Rate Limits
  slug: broadlume-rate-limits
score:
  band: developing
  composite: 47.6
  delta: -2.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 55.9
    developer_ergonomics: 68.5
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/broadlume/refs/heads/main/screenshots/broadlume-2026-07-25T203941.png
security:
- kind: authentication
  name: Broadlume Authentication
  slug: broadlume-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Broadlume Domain Security
  slug: broadlume-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: broadlume
tags:
- Company
- Flooring
- Retail
- Marketing
- Websites
- Business Software
- Home Improvement
- ERP
- Inventory
- Point of Sale
- Accounting
- Order Management
website: https://broadlume.com/
---
