---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Holded Agentic Access
  operation_count: 42
  slug: holded-agentic-access
  summary_line: 42 operations · 20 acting
api_count: 1
apis:
- description: REST API for managing invoicing, contacts, products, accounting, projects, employees, and CRM records inside the Holded business management platform. Authentication uses an API key passed via the `key
  name: Holded REST API
  slug: rest-api
- description: The Accounting API from Holded — 1 operation(s) for accounting.
  name: Holded Accounting API
  slug: holded-accounting-api
- description: The Crm API from Holded — 2 operation(s) for crm.
  name: Holded Crm API
  slug: holded-crm-api
- description: The Invoicing API from Holded — 15 operation(s) for invoicing.
  name: Holded Invoicing API
  slug: holded-invoicing-api
- description: The Projects API from Holded — 2 operation(s) for projects.
  name: Holded Projects API
  slug: holded-projects-api
- description: The Team API from Holded — 2 operation(s) for team.
  name: Holded Team API
  slug: holded-team-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Holded REST Accounting API
  slug: open-holded-accounting-api
- collection_type: open
  name: Holded REST Accounting Crm API
  slug: open-holded-crm-api
- collection_type: open
  name: Holded REST Accounting Invoicing API
  slug: open-holded-invoicing-api
- collection_type: open
  name: Holded REST Accounting Projects API
  slug: open-holded-projects-api
- collection_type: open
  name: Holded REST Accounting Team API
  slug: open-holded-team-api
- collection_type: open
  name: Holded REST API
  slug: open-holded
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/holded-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/holded-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/holded-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/holdedhub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/holded
- group: company
  title: ''
  type: Website
  url: https://www.holded.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.holded.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.holded.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.holded.com/register
- group: agent
  title: ''
  type: LlmsText
  url: https://api.holded.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.holded.com/en/blog
created: '2026-05-11'
description: Holded is a cloud-based all-in-one business management platform from Spain (now part of Visma) that combines ERP, CRM, accounting, invoicing, inventory, project management, HR, and team collaboration features for small and medium-sized businesses. The Holded REST API provides programmatic access to invoicing, contacts, products, accounting, projects, employees, and CRM data using a simple API key authentication scheme over JSON.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/holded.png
layout: provider
modified: '2026-05-11'
name: Holded
nav: Providers
network: true
overview: 'Holded publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Crm API, Invoicing API, and 2 more. Tagged areas include ERP, CRM, Accounting, Invoicing, and Business Management.


  Holded''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 52.7
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/holded/refs/heads/main/screenshots/holded-2026-06-20T182811.png
security:
- kind: authentication
  name: Holded Authentication
  slug: holded-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Holded Domain Security
  slug: holded-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: holded
tags:
- ERP
- CRM
- Accounting
- Invoicing
- Business Management
- SMB
- Spain
website: https://www.holded.com
---
