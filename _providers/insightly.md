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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Insightly Agentic Access
  operation_count: 12
  slug: insightly-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 8
apis:
- description: REST API for managing contacts, organizations, leads, opportunities, projects, tasks, events, products, price books, quotes, and custom objects in Insightly. Uses HTTP Basic authentication with a Base
  name: Insightly REST API v3.1
  slug: rest-api
- description: The Contacts API from Insightly — 3 operation(s) for contacts.
  name: Insightly Contacts API
  slug: insightly-contacts-api
- description: The Leads API from Insightly — 1 operation(s) for leads.
  name: Insightly Leads API
  slug: insightly-leads-api
- description: The Opportunities API from Insightly — 1 operation(s) for opportunities.
  name: Insightly Opportunities API
  slug: insightly-opportunities-api
- description: The Organisations API from Insightly — 1 operation(s) for organisations.
  name: Insightly Organisations API
  slug: insightly-organisations-api
- description: The Products API from Insightly — 1 operation(s) for products.
  name: Insightly Products API
  slug: insightly-products-api
- description: The Projects API from Insightly — 1 operation(s) for projects.
  name: Insightly Projects API
  slug: insightly-projects-api
- description: The Quotations API from Insightly — 1 operation(s) for quotations.
  name: Insightly Quotations API
  slug: insightly-quotations-api
artifact_total: 13
collections:
- collection_type: open
  name: Insightly CRM API
  slug: open-insightly
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/insightly-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/insightly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/insightly-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/insightly-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Insightly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/insightly
- group: company
  title: ''
  type: Website
  url: https://www.insightly.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.insightly.com/v3.1/Help
- group: operate
  title: ''
  type: Support
  url: https://support.insightly.com
- group: start
  title: ''
  type: Signup
  url: https://www.insightly.com/signup/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.insightly.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.insightly.com/blog
created: '2026-05-11'
description: Insightly is a CRM and project management platform for small and mid-sized businesses, combining contact and lead management, opportunity pipelines, project delivery, and marketing automation. The Insightly REST API provides programmatic access to contacts, organizations, leads, opportunities, projects, products, price books, quotes, and custom objects for CRM integrations and workflow automation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/insightly.png
layout: provider
modified: '2026-05-11'
name: Insightly
nav: Providers
network: true
overview: 'Insightly publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Leads API, Opportunities API, and 4 more. Tagged areas include CRM, Project Management, Lead Management, Opportunities, and Contacts.


  Insightly''s developer surface includes authentication, documentation, support, signup flow, pricing, engineering blog, and 6 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 28.8
  delta: -2.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 53.4
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/insightly/refs/heads/main/screenshots/insightly-2026-06-20T183401.png
security:
- kind: authentication
  name: Insightly Authentication
  slug: insightly-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Insightly Domain Security
  slug: insightly-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Insightly Vulnerability Disclosure
  slug: insightly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: insightly
tags:
- CRM
- Project Management
- Lead Management
- Opportunities
- Contacts
- SMB
website: https://www.insightly.com
---
