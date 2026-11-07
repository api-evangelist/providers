---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'The Qubole Data Service (QDS) REST API for submitting and managing data commands (Hive, Presto, Spark, Hadoop, Pig, shell, DB import/export, notebook), managing compute clusters, scheduling recurring '
  name: Qubole Data Service REST API
  slug: qubole-data-service-rest-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/qubole/plans/qubole-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qubole-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/qubole/security/qubole-trust-center.yml
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
  href: https://artifacts.apis.io/qubole/packages/qubole-packages.yml
  title: ''
  type: Packages
  url: packages/qubole-packages.yml
- group: build
  href: https://artifacts.apis.io/qubole/packages/qubole-packages.yml
  title: ''
  type: SDKs
  url: packages/qubole-packages.yml
- group: build
  href: https://artifacts.apis.io/qubole/cli/qubole-cli.yml
  title: ''
  type: CLI
  url: cli/qubole-cli.yml
- group: auth
  href: https://artifacts.apis.io/qubole/authentication/qubole-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qubole-authentication.yml
- group: design
  href: https://artifacts.apis.io/qubole/conventions/qubole-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qubole-conventions.yml
- group: design
  href: https://artifacts.apis.io/qubole/data-model/qubole-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qubole-data-model.yml
- group: design
  href: https://artifacts.apis.io/qubole/lifecycle/qubole-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qubole-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/qubole/conformance/qubole-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qubole-conformance.yml
- group: agent
  href: https://artifacts.apis.io/qubole/well-known/qubole-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qubole-well-known.yml
- group: agent
  href: https://artifacts.apis.io/qubole/mcp/qubole-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/qubole-mcp.yml
- group: agent
  href: https://artifacts.apis.io/qubole/llms/qubole-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qubole-llms.txt
- group: auth
  href: https://artifacts.apis.io/qubole/security/qubole-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qubole-domain-security.yml
created: '2026-07-17'
description: Qubole is a cloud-native data lake platform (now part of Idera) that lets teams run multiple open-source data-processing engines - Apache Spark, Presto, Hive, Hadoop, and Airflow - together in a single, cost-optimized, self-managing environment across AWS, Microsoft Azure, Google Cloud Platform, and Oracle Cloud Infrastructure. The Qubole Data Service (QDS) automates cluster provisioning, autoscaling, and spot/preemptible instance management to reduce data-lake costs, and exposes a comprehensive REST API for submitting Hive/Presto/Spark/Hadoop commands, managing clusters, scheduling jobs, running notebooks and dashboards, and administering accounts, users, groups, and roles. First-party SDKs (Python qds-sdk, Java, and Ruby), the qds.py command-line tool, and the afctl Airflow CLI wrap the API. This profile was surfaced as a VC-portfolio lead and enriched by the API Evangelist pipeline against Qubole's live public documentation and package registries.
finops:
- has_sources: true
  method: derived
  name: Qubole Finops
  primary_unit: qcu per hour
  service_category: ''
  slug: qubole-finops
  template: false
image: https://www.qubole.com/wp-content/themes/qubole/assets/images/logo.svg
layout: provider
modified: '2026-07-20'
name: Qubole
nav: Providers
network: true
overview: 'Qubole is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Data Lake, Big Data, and Analytics.


  Qubole''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 21 more developer resources.'
plans:
- name: Qubole Plans Pricing
  plan_count: 3
  slug: qubole-plans-pricing
random_paper: 0
score:
  band: developing
  composite: 46.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 73.2
    operational_transparency: 18.4
  previous_composite: 46.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/qubole/qubole-2026-09-02T152637.png
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
