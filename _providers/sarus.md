---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Sarus Gateway is the server component of the Sarus privacy layer. It is deployed inside the customer's own environment (Docker or Kubernetes, on-premises or in AWS/Azure/GCP) and is reached by the
  name: Sarus Gateway API
  slug: sarus-gateway
- description: Qrlew is Sarus's open-source (Apache 2.0) SQL manipulation and differential-privacy engine, written in Rust and published under github.com/Qrlew. The Qrlew server wraps it in a small RESTful API — POS
  name: Qrlew Server API
  slug: qrlew-server
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.sarus.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sarus.tech/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sarus-tech
- group: company
  title: ''
  type: Blog
  url: https://www.sarus.tech/blog
- group: operate
  title: ''
  type: Support
  url: https://www.sarus.tech/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sarus.tech/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/sarus-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sarus-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/sarus-schema.proto
- group: build
  title: ''
  type: Examples
  url: examples/qrlew-server-example.http
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sarus-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sarus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sarus-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sarus-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sarus-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sarus-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sarus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sarus-rate-limits.yml
created: '2026-08-17'
description: Sarus Technologies is a Paris-based privacy-engineering company (Y Combinator W22, founded 2020 by the team behind AlephD) that builds a privacy layer sitting between sensitive data and the analysts, data scientists and LLMs that need it. The Sarus platform deploys inside the customer's own infrastructure — Docker or Kubernetes, on-premises or on AWS, Azure and GCP — and applies differential privacy, DP-trained synthetic data and on-the-fly SQL and Python query rewriting so practitioners can run analytics, machine learning and LLM fine-tuning on data they never see. Developers reach the platform through the first-party 'sarus' Python client for the Sarus Gateway, a BI connector, and Qrlew, Sarus's open-source Rust SQL-rewriting engine. Because the product is customer-deployed, Sarus publishes no hosted, multi-tenant API base URL and no OpenAPI; its public machine-readable surface is the Sarus Data Spec protobuf schema and the Qrlew server's published request examples.
image: https://cdn.prod.website-files.com/61bc58893bfe8290fd9fa12a/61bc58893bfe827a089fa131_logotype-dark.svg
layout: provider
modified: '2026-08-17'
name: Sarus
nav: Providers
network: true
overview: 'Sarus publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Privacy, Differential Privacy, and Synthetic Data.


  Sarus'' developer surface includes documentation, engineering blog, support, code examples, authentication, changelog, and 12 more developer resources.'
random_paper: 111
score:
  band: thin
  composite: 26.6
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 29.6
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  schema_version: 0.12.0
  scored_at: '2026-08-19'
slug: sarus
tags:
- Company
- Ai Data
- Privacy
- Differential Privacy
- Synthetic Data
- Analytics
- Machine Learning
- Data Governance
- SQL
- Open Source
website: https://www.sarus.tech/
---
