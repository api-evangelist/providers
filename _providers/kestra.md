---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Kestra Agentic Access
  operation_count: 19
  slug: kestra-agentic-access
  summary_line: 19 operations · 7 acting
api_count: 1
apis:
- description: The Kestra Enterprise API extends the open-source API with additional endpoints for enterprise features including authentication, RBAC, audit logging, multi-tenancy, SSO, and advanced governance capab
  name: Kestra Enterprise API
  slug: enterprise-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Trigger and inspect workflow executions.
  name: Kestra Executions API
  slug: kestra-executions-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Manage namespace files.
  name: Kestra Files API
  slug: kestra-files-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Manage flow definitions.
  name: Kestra Flows API
  slug: kestra-flows-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Manage namespace-scoped key-value pairs.
  name: Kestra KVStore API
  slug: kestra-kvstore-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Manage namespaces.
  name: Kestra Namespaces API
  slug: kestra-namespaces-api
- baseURL: http://localhost:8080
  baseurl_source: spec
  description: Manage and test triggers.
  name: Kestra Triggers API
  slug: kestra-triggers-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kestra Open Source REST Executions API
  slug: open-kestra-executions-api
- collection_type: open
  name: Kestra Open Source REST Executions Files API
  slug: open-kestra-files-api
- collection_type: open
  name: Kestra Open Source REST Executions Flows API
  slug: open-kestra-flows-api
- collection_type: open
  name: Kestra Open Source REST Executions KVStore API
  slug: open-kestra-kvstore-api
- collection_type: open
  name: Kestra Open Source REST Executions Namespaces API
  slug: open-kestra-namespaces-api
- collection_type: open
  name: Kestra Open Source REST Executions Triggers API
  slug: open-kestra-triggers-api
- collection_type: open
  name: Kestra Open Source REST API
  slug: open-kestra
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kestra-io/kestra/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/kestra-io/kestra/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/kestra-io/kestra/blob/develop/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kestra-io/kestra/blob/develop/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kestra-io/kestra/blob/develop/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/kestra-io/kestra/blob/develop/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kestra-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/kestra-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kestra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kestra-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kestra
- group: start
  title: ''
  type: Portal
  url: https://kestra.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kestra.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://kestra.io/docs/quickstart
- group: learn
  title: ''
  type: Tutorials
  url: https://kestra.io/docs/tutorial
- group: docs
  title: ''
  type: APIReference
  url: https://kestra.io/docs/api-reference
- group: docs
  title: ''
  type: APIReference
  url: https://kestra.io/docs/api-reference/open-source
- group: auth
  title: ''
  type: Authentication
  url: https://kestra.io/docs/enterprise/auth/api
- group: build
  title: ''
  type: SDKs
  url: https://kestra.io/docs/api-reference/kestra-sdk
- group: company
  title: ''
  type: Blog
  url: https://kestra.io/blogs
- group: operate
  title: ''
  type: ChangeLog
  url: https://kestra.io/docs/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://kestra.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.kestra.io/hc/en-us
- group: operate
  title: ''
  type: Community
  url: https://kestra.io/community
- group: operate
  title: ''
  type: FAQ
  url: https://kestra.io/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kestra-io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kestra-io/kestra
- group: other
  title: ''
  type: Terraform
  url: https://kestra.io/docs/terraform
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kestra.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kestra.io/terms-and-services
- group: operate
  title: ''
  type: Contact
  url: https://kestra.io/contact-us
- group: agent
  title: ''
  type: LlmsText
  url: https://kestra.io/llms.txt
created: '2026-03-03'
description: Kestra is a declarative workflow orchestration platform where pipelines are defined in YAML, combining visual and code-first approaches.
finops:
- name: Kestra Finops
  service_category: API
  slug: kestra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kestra.png
layout: provider
modified: '2026-04-28'
name: Kestra
nav: Providers
network: true
overview: 'Kestra publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Executions API, Files API, Flows API, and 3 more. Tagged areas include Automation, Data Pipeline, Event-Driven, Orchestration, and Workflows.


  Kestra''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, engineering blog, changelog, and 25 more developer resources.'
plans:
- name: Kestra Plans Pricing
  plan_count: 3
  slug: kestra-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Kestra Rate Limits
  slug: kestra-rate-limits
score:
  band: developing
  composite: 51.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 61.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 51.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kestra/refs/heads/main/screenshots/kestra-2026-06-20T184000.png
security:
- kind: authentication
  name: Kestra Authentication
  slug: kestra-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kestra Domain Security
  slug: kestra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Kestra Trust Center
  slug: kestra-trust-center
  summary_line: SOC 2, ISO 27001
slug: kestra
tags:
- Automation
- Data Pipeline
- Event-Driven
- Orchestration
- Workflows
website: https://kestra.io/
---
