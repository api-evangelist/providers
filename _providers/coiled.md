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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: Token-authenticated REST API for submitting Coiled batch jobs (single job scripts) to run on cloud VMs and Dask clusters.
  name: Coiled Batch REST API
  slug: coiled-batch-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://coiled.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coiled.io/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coiled.io/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coiled.io/user_guide/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coiled.io/user_guide/setup/index.html
- group: company
  title: ''
  type: Blog
  url: https://docs.coiled.io/blog/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coiled.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.coiled.io/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.coiled.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coiled.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coiled.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.coiled.io/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coiled
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.coiled.io/user_guide/changelog.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coiled-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coiled-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coiled-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/coiled-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coiled-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/coiled-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coiled-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.coiled.io/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.coiled.io/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coiled-domain-security.yml
created: '2026-07-17'
description: Coiled is a lightweight cloud compute platform that lets Python developers scale their code to thousands of cloud machines without managing Kubernetes, Docker, or infrastructure. Built by the maintainers of Dask, Coiled provisions cloud VMs and Dask clusters in a user's own AWS, GCP, or Azure account, automatically replicates the local software environment, runs the work across large clusters, and tears the resources back down when finished. It powers Dask clusters, serverless functions, batch jobs, hosted Jupyter notebooks, and interactive CLI jobs, and exposes a first-party Python client, a `coiled` command-line interface, and a token-authenticated REST API. Coiled was surfaced as a portfolio company of Bessemer Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coiled.png
layout: provider
modified: '2026-07-18'
name: Coiled
nav: Providers
network: true
overview: 'Coiled publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Cloud Computing, Data Science, and Dask.


  Coiled''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 17 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 35.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coiled/refs/heads/main/screenshots/coiled-2026-07-25T210020.png
security:
- kind: authentication
  name: Coiled Authentication
  slug: coiled-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coiled Domain Security
  slug: coiled-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Coiled Trust Center
  slug: coiled-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: coiled
tags:
- Company
- Ai Ml
- Cloud Computing
- Data Science
- Dask
- Python
- Distributed Computing
- Machine-Learning
- Serverless
website: https://coiled.io
---
