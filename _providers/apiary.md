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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://api.apiary.io
  baseurl_source: declared
  description: The Apiary API provides programmatic access to manage API projects, documentation, and team collaboration. It allows creating and updating API Blueprint and Swagger/OpenAPI documents, managing team me
  name: Apiary API
  slug: apiary-api
- description: API Blueprint is a high-level API design language created by Apiary for designing and documenting web APIs. It uses a Markdown-based syntax that is human-readable and machine-parseable, enabling teams
  name: API Blueprint
  slug: api-blueprint
artifact_total: 26
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/apiary-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/apiary-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/apiary-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/apiary-cli.yml
- group: design
  title: ''
  type: Components
  url: components/apiary-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/apiary-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/apiary-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/apiary-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/apiary-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/apiary-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/apiary-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/apiary-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/apiary-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/apiary-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apiary-llms.txt
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
  url: https://apiary.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiary.io/tos
- group: operate
  title: ''
  type: ChangeLogRSS
  url: https://apiary.docs.apiary.io/feed
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.apiary.io/feed.xml
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
json_schemas:
- name: Apiary Api List.Schema
  property_count: 1
  slug: apiary-api-list.schema
- name: Apiary Api Project Created.Schema
  property_count: 3
  slug: apiary-api-project-created.schema
- name: Apiary Error.Schema
  property_count: 1
  slug: apiary-error.schema
- name: Apiary Token List.Schema
  property_count: 1
  slug: apiary-token-list.schema
- name: Apiary Token.Schema
  property_count: 3
  slug: apiary-token.schema
- name: Apiary User.Schema
  property_count: 4
  slug: apiary-user.schema
layout: provider
modified: '2026-09-02'
name: Apiary
nav: Providers
network: true
overview: 'Apiary publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Blueprint, API Design, API Testing, Collaboration, and Design-First.


  Apiary''s developer surface includes authentication, CLI, changelog, sandbox, documentation, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Apiary Plans Pricing
  plan_count: 3
  slug: apiary-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Apiary Rate Limits
  slug: apiary-rate-limits
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 65.0
    catalog_earned_first_party: 20.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 4.5
    contract_quality: 21.9
    developer_ergonomics: 67.3
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 25.0
  previous_composite: 44.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apiary/refs/heads/main/screenshots/apiary-2026-06-20T172227.png
security:
- kind: authentication
  name: Apiary Authentication
  slug: apiary-authentication
  summary_line: apiKey/http · 3 schemes
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
