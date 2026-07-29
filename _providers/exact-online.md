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
- acting_count: 13
  human_in_the_loop: 0
  name: Exact Online Agentic Access
  operation_count: 26
  slug: exact-online-agentic-access
  summary_line: 26 operations · 13 acting
api_count: 7
apis:
- description: REST and OData API (v1) for Exact Online covering financials, sales, purchasing, inventory, HRM, CRM, project management, and master data. Authentication is OAuth 2.0; applications register in the Exa
  name: Exact Online REST / OData API
  slug: rest-api
- description: The CRM API from Exact Online — 4 operation(s) for crm.
  name: Exact Online CRM API
  slug: exact-online-crm-api
- description: The Financial API from Exact Online — 1 operation(s) for financial.
  name: Exact Online Financial API
  slug: exact-online-financial-api
- description: The Logistics API from Exact Online — 1 operation(s) for logistics.
  name: Exact Online Logistics API
  slug: exact-online-logistics-api
- description: The Purchase API from Exact Online — 1 operation(s) for purchase.
  name: Exact Online Purchase API
  slug: exact-online-purchase-api
- description: The Sales API from Exact Online — 3 operation(s) for sales.
  name: Exact Online Sales API
  slug: exact-online-sales-api
- description: The System API from Exact Online — 3 operation(s) for system.
  name: Exact Online System API
  slug: exact-online-system-api
artifact_total: 14
collections:
- collection_type: open
  name: Exact Online REST / OData API
  slug: open-exact-online
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exact-online-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/exact-online-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/exact-online-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exact-online-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exact-online-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/exact-online-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/exact
- group: company
  title: ''
  type: Website
  url: https://www.exact.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.exactonline.com/community/s/knowledge-base
- group: docs
  title: ''
  type: API Documentation
  url: https://start.exactonline.nl/docs/HlpRestAPIResources.aspx
- group: commercial
  title: ''
  type: Pricing
  url: https://www.exact.com/nl/software/prijs
- group: start
  title: ''
  type: Signup
  url: https://www.exact.com/nl/probeer-gratis
- group: other
  title: ''
  type: App Center
  url: https://apps.exactonline.com
- group: company
  title: ''
  type: Blog
  url: https://www.exact.com/nl/blog?format=feed&type=rss
created: '2026-05-11'
description: Exact Online is a Dutch cloud business software suite from Exact (Delft, NL) serving SMEs and accountants with accounting, ERP, invoicing, CRM, project management, and AI-driven automation, used by more than 675,000 companies. The platform exposes a comprehensive REST and OData API covering financial, HRM, logistics, CRM, and project data across regional deployments (start.exactonline.nl, .co.uk, .be, .de, .fr, .es, .com). Authentication is via OAuth 2.0 with regional authorization and token endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/exact-online.png
layout: provider
modified: '2026-05-11'
name: Exact Online
nav: Providers
network: true
overview: 'Exact Online publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CRM API, Financial API, Logistics API, and 3 more. Tagged areas include Accounting, ERP, Invoicing, Business Software, and CRM.


  Exact Online''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 8
scopes:
- name: Exact Online Scopes
  scope_count: 0
  slug: exact-online-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.1
  delta: -2.1
  facets:
    commercial_clarity: 18.4
    contract_quality: 53.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exact-online/refs/heads/main/screenshots/exact-online-2026-06-20T180917.png
security:
- kind: authentication
  name: Exact Online Authentication
  slug: exact-online-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Exact Online Domain Security
  slug: exact-online-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Exact Online Vulnerability Disclosure
  slug: exact-online-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Exact Online Trust Center
  slug: exact-online-trust-center
  summary_line: GDPR
slug: exact-online
tags:
- Accounting
- ERP
- Invoicing
- Business Software
- CRM
- Financial Software
- SME
website: https://www.exact.com
---
