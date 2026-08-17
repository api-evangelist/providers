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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Odoo Agentic Access
  operation_count: 3
  slug: odoo-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 4
apis:
- description: Odoo's external API for integrating with the platform using JSON-RPC and XML-RPC protocols for accessing all business modules.
  name: Odoo External API
  slug: odoo-external-api
- description: Unauthenticated XML-RPC endpoint for version + authentication
  name: Odoo Common API
  slug: odoo-common-api
- description: JSON-RPC transport for the same operations
  name: Odoo JSON-RPC API
  slug: odoo-json-rpc-api
- description: Authenticated XML-RPC endpoint for model operations
  name: Odoo Object API
  slug: odoo-object-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Odoo External Common API
  slug: open-odoo-common-api
- collection_type: open
  name: Odoo External Common JSON-RPC API
  slug: open-odoo-json-rpc-api
- collection_type: open
  name: Odoo External Common Object API
  slug: open-odoo-object-api
- collection_type: open
  name: Odoo External API
  slug: open-odoo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/odoo-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/odoo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/odoo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/odoo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/odoo
- group: company
  title: ''
  type: Website
  url: https://www.odoo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.odoo.com/documentation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/odoo
- group: company
  title: ''
  type: Blog
  url: https://www.odoo.com/blog
created: '2026-03-16'
description: Odoo is an open-source suite of business applications covering ERP, CRM, eCommerce, accounting, inventory, and more. Odoo provides external APIs for integrating with the Odoo platform using JSON-RPC and XML-RPC protocols.
finops:
- name: Odoo Finops
  service_category: API
  slug: odoo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/odoo.png
layout: provider
modified: '2026-04-28'
name: Odoo
nav: Providers
network: true
overview: 'Odoo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Common API, JSON-RPC API, and Object API. Tagged areas include Business Applications, CRM, ERP, and Open Source.


  Odoo''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Odoo Plans Pricing
  plan_count: 3
  slug: odoo-plans-pricing
random_paper: 135
rate_limits:
- limit_count: 5
  name: Odoo Rate Limits
  slug: odoo-rate-limits
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 54.5
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 28.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/odoo/refs/heads/main/screenshots/odoo-2026-06-20T190621.png
security:
- kind: authentication
  name: Odoo Authentication
  slug: odoo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Odoo Domain Security
  slug: odoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Odoo Vulnerability Disclosure
  slug: odoo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: odoo
tags:
- Business Applications
- CRM
- ERP
- Open Source
website: https://www.odoo.com/
---
