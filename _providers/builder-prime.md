---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Builder Prime's REST "Open API" — the tenant-scoped integration surface used to create leads and clients, and to read clients, employees, projects, appointments, appointment types and appointment resu
  name: Builder Prime Open API
  slug: builder-prime-open-api
artifact_total: 4
asyncapis:
- description: ''
  name: Builder Prime Webhooks
  slug: builder-prime-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/builder-prime-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.builderprime.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.builderprime.com/blog/open-api-documentation
- group: operate
  title: ''
  type: Support
  url: https://help.builderprime.com/bp-knowledgebase
- group: company
  title: ''
  type: Blog
  url: https://www.builderprime.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.builderprime.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.builderprime.com/register
- group: start
  title: ''
  type: Login
  url: https://app.builderprime.com/admin/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.builderprime.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.builderprime.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Builder-Prime
- group: operate
  title: ''
  type: StatusPage
  url: https://builderprime.statuspage.io/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/builder-prime-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/builder-prime-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/builder-prime-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/builder-prime-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/builder-prime-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/builder-prime-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/builder-prime-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/builder-prime-llms.txt
created: '2026-08-08'
description: Builder Prime is an all-in-one CRM and business management platform built for home improvement contractors and remodelers. It combines lead and client management, appointment setting, estimating and price books, proposals and e-signature contracts, project and production scheduling, invoicing and payments, SMS and email communication, marketing automation, and sales reporting in a single multi-tenant web and mobile application. Each customer works from its own subdomain, and Builder Prime exposes a REST "Open API" plus webhooks and a Zapier app so contractors can push leads and pull client, employee, project and appointment data between Builder Prime and lead aggregators, call centers, financing partners, measurement tools and accounting systems.
image: https://cdn.prod.website-files.com/66dacc76fb28939d860bf57c/671740708dbd70842afe1db7_builder-prime-logo.webp
layout: provider
modified: '2026-08-08'
name: Builder Prime
nav: Providers
network: true
overview: 'Builder Prime publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Home Improvement, Construction, and Contractors.


  The Builder Prime catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Builder Prime''s developer surface includes documentation, support, engineering blog, pricing, signup flow, authentication, and 14 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 41.6
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 35.9
  provenance:
    conformance: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/builder-prime/refs/heads/main/screenshots/builder-prime-2026-09-02T144954.png
security:
- kind: authentication
  name: Builder Prime Authentication
  slug: builder-prime-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Builder Prime Domain Security
  slug: builder-prime-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: builder-prime
tags:
- Company
- CRM
- Home Improvement
- Construction
- Contractors
- Remodeling
- Sales
- Estimating
- Project Management
- Lead Management
- Field Service
- Software-as-a-Service
website: https://www.builderprime.com/
---
