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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: The Apiary API provides programmatic access to manage API projects, documentation, and team collaboration. It allows creating and updating API Blueprint and Swagger/OpenAPI documents, managing team me
  name: Apiary API
  slug: apiary-api
- description: API Blueprint is a high-level API design language created by Apiary for designing and documenting web APIs. It uses a Markdown-based syntax that is human-readable and machine-parseable, enabling teams
  name: API Blueprint
  slug: api-blueprint
artifact_total: 19
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apiaryio/api-blueprint/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apiaryio/api-blueprint/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/apiaryio/api-blueprint/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apiary-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apiary-io
- group: company
  title: ''
  type: Website
  url: https://apiary.io
- group: docs
  title: ''
  type: Documentation
  url: https://help.apiary.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apiaryio
- group: company
  title: ''
  type: Blog
  url: https://blog.apiary.io
- group: commercial
  title: ''
  type: Pricing
  url: https://apiary.io/plans
- group: start
  title: ''
  type: Login
  url: https://login.apiary.io
- group: start
  title: ''
  type: Signup
  url: https://login.apiary.io/register
- group: operate
  title: ''
  type: Support
  url: https://help.apiary.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
created: '2026-03-25'
description: Apiary is an API design and documentation platform, now part of Oracle Cloud Infrastructure. With 486,000+ users and 591,000+ APIs managed, it uses API Blueprint and Swagger/OpenAPI specifications to produce interactive API documentation, mock servers, automated testing, and collaborative API design workflows. Apiary enables teams to design APIs before writing code, generate documentation automatically, and validate implementations against specifications.
features:
- description: Native support for API Blueprint, a high-level Markdown-based API description language for collaborative design.
  name: API Blueprint Support
- description: Import and work with Swagger and OpenAPI specifications alongside API Blueprint documents.
  name: OpenAPI/Swagger Support
- description: Auto-generate interactive documentation from API specs with a built-in API console for live testing.
  name: Interactive API Documentation
- description: Instant mock servers generated from API specs allowing frontend development before backend is ready.
  name: Mock Servers
- description: Run automated tests against API implementations using Dredd, the open-source API testing framework.
  name: Automated API Testing
- description: Team-based API design with version history, commenting, and shared workspaces.
  name: Collaborative Workflows
- description: Apiary CLI for integrating API design and testing workflows into CI/CD pipelines.
  name: CLI Integration
- description: Maintains Dredd (testing), Gavel (validation), and API Blueprint as open-source projects.
  name: Open Source Tooling
finops:
- name: Apiary Finops
  service_category: API
  slug: apiary-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apiary.png
layout: provider
modified: '2026-04-19'
name: Apiary
nav: Providers
network: true
overview: 'Apiary publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Blueprint, API Design, API Testing, Collaboration, and Design-First.


  Apiary''s developer surface includes documentation, engineering blog, pricing, signup flow, support, and 10 more developer resources.'
plans:
- name: Apiary Plans Pricing
  plan_count: 3
  slug: apiary-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Apiary Rate Limits
  slug: apiary-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 25.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apiary/refs/heads/main/screenshots/apiary-2026-06-20T172227.png
security:
- kind: domain-security
  name: Apiary Domain Security
  slug: apiary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apiary
tags:
- API Blueprint
- API Design
- API Testing
- Collaboration
- Design-First
- Documentation
- Mock Servers
- Oracle
use_cases:
- description: Design APIs in API Blueprint or OpenAPI before writing code, enabling parallel frontend and backend development.
  name: Design-First API Development
- description: Automatically generate interactive API documentation from API specifications for developer consumption.
  name: API Documentation Generation
- description: Generate instant mock servers from specs to enable frontend development without a live backend.
  name: Mock Server Prototyping
- description: Validate API implementations against their specifications using Dredd to catch regressions.
  name: Contract Testing
- description: Collaborate on API design standards and review API changes in a shared workspace.
  name: Team API Governance
website: https://apiary.io
---
