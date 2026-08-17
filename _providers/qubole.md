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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'The Qubole Data Service (QDS) REST API for submitting and managing data commands (Hive, Presto, Spark, Hadoop, Pig, shell, DB import/export, notebook), managing compute clusters, scheduling recurring '
  name: Qubole Data Service REST API
  slug: qubole-data-service-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/qubole-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.qubole.com/products/trust
- group: company
  title: ''
  type: Website
  url: https://www.qubole.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qubole.com/en/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qubole.com/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qubole.com/en/latest/rest-api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qubole.com/en/latest/quick-start-guide/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.qubole.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qubole.com/qubole-pricing
- group: start
  title: ''
  type: SignUp
  url: https://us.qubole.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: https://www.qubole.com/company/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.qubole.com/TOS.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qubole.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qubole
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qubole.com/
- group: build
  title: ''
  type: Packages
  url: packages/qubole-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qubole-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/qubole-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qubole-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qubole-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qubole-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qubole-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qubole-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qubole-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qubole-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qubole-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qubole-domain-security.yml
created: '2026-07-17'
description: Qubole is a cloud-native data lake platform (now part of Idera) that lets teams run multiple open-source data-processing engines - Apache Spark, Presto, Hive, Hadoop, and Airflow - together in a single, cost-optimized, self-managing environment across AWS, Microsoft Azure, Google Cloud Platform, and Oracle Cloud Infrastructure. The Qubole Data Service (QDS) automates cluster provisioning, autoscaling, and spot/preemptible instance management to reduce data-lake costs, and exposes a comprehensive REST API for submitting Hive/Presto/Spark/Hadoop commands, managing clusters, scheduling jobs, running notebooks and dashboards, and administering accounts, users, groups, and roles. First-party SDKs (Python qds-sdk, Java, and Ruby), the qds.py command-line tool, and the afctl Airflow CLI wrap the API. This profile was surfaced as a VC-portfolio lead and enriched by the API Evangelist pipeline against Qubole's live public documentation and package registries.
image: https://www.qubole.com/wp-content/themes/qubole/assets/images/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: qubole-mcp.yml
  slug: qubole-mcpyml
modified: '2026-07-20'
name: Qubole
nav: Providers
network: true
overview: 'Qubole publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Data Lake, Big Data, and Analytics.


  Qubole''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 20 more developer resources.'
random_paper: 52
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 21.1
  previous_composite: 36.3
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Qubole Authentication
  slug: qubole-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qubole Domain Security
  slug: qubole-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Qubole Trust Center
  slug: qubole-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: qubole
tags:
- Company
- Data
- Data Lake
- Big Data
- Analytics
- Spark
- Presto
- Hive
- Airflow
- Machine Learning
- Cloud
- Data Engineering
website: https://www.qubole.com/
---
