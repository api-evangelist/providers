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
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: DiDi Enterprise Services (DDES) Open API for corporate employee travel management — approval, bills, budget/cost centers, city info, company entities, single sign-on, users, orders, ranks, regulations
  name: DiDi Enterprise (DDES) Open API
  slug: didi-enterprise-ddes-open-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.didiglobal.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://opendocs.xiaojukeji.com/version2024
- group: docs
  title: ''
  type: Documentation
  url: https://opendocs.xiaojukeji.com/version2024
- group: start
  title: ''
  type: GettingStarted
  url: https://opendocs.xiaojukeji.com/version2024/10957
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/didi
- group: auth
  title: ''
  type: Authentication
  url: authentication/didi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/didi-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/didi-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/didi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/didi-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/didi-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/didi-llms.txt
created: '2026-07-17'
description: DiDi Global is a mobility technology platform best known for ride-hailing, taxi-hailing, and enterprise employee travel across China and international markets. DiDi exposes a public developer surface through DiDi Enterprise Services (DDES) — an Open API for corporate travel management covering approval workflows, bills, budget/cost centers, orders, single sign-on, users, roles, and company entities. The DDES API (base URL https://api.es.xiaojukeji.com) is documented at opendocs.xiaojukeji.com/version2024, secured with OAuth 2.0 client_credentials plus per-request signing, and shipped with official Java and Go SDKs under the github.com/didi organization. DiDi is backed by Hillhouse and the SoftBank Vision Fund.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/didi.png
layout: provider
modified: '2026-07-18'
name: Didi
nav: Providers
network: true
overview: 'Didi publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Ride Hailing, Transportation, and Enterprise Travel.


  Didi''s developer surface includes documentation, getting-started guide, authentication, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 19.9
  provenance:
    conformance: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/didi/refs/heads/main/screenshots/didi-2026-07-25T211941.png
security:
- kind: authentication
  name: Didi Authentication
  slug: didi-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Didi Domain Security
  slug: didi-domain-security
  summary_line: TLSv1.2 · DMARC
slug: didi
tags:
- Company
- Mobility
- Ride Hailing
- Transportation
- Enterprise Travel
- Expense Management
- Authentication
website: https://www.didiglobal.com
---
