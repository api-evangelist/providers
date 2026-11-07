---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
  score: 3.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The hila REST APIs provide CRUD operations to deploy, manage, and monitor machine-learning models — drift detection, explainability, model performance, alerts, data profiling, inference tracking, pipe
  name: hila REST API
  slug: hila-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.vian.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vian.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vian.ai/5.0-r2/api-list.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vian.ai/5.0-r2/api-quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://www.vian.ai/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.vian.ai/whatsnew
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vianai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vian.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vian.ai/privacy
- group: auth
  href: https://artifacts.apis.io/vianai-systems/authentication/vianai-systems-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vianai-systems-authentication.yml
- group: build
  href: https://artifacts.apis.io/vianai-systems/cli/vianai-systems-cli.yml
  title: ''
  type: CLI
  url: cli/vianai-systems-cli.yml
- group: build
  href: https://artifacts.apis.io/vianai-systems/packages/vianai-systems-packages.yml
  title: ''
  type: Packages
  url: packages/vianai-systems-packages.yml
- group: build
  href: https://artifacts.apis.io/vianai-systems/packages/vianai-systems-packages.yml
  title: ''
  type: SDKs
  url: packages/vianai-systems-packages.yml
- group: design
  href: https://artifacts.apis.io/vianai-systems/conventions/vianai-systems-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vianai-systems-conventions.yml
- group: design
  href: https://artifacts.apis.io/vianai-systems/lifecycle/vianai-systems-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vianai-systems-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/vianai-systems/conformance/vianai-systems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vianai-systems-conformance.yml
- group: auth
  href: https://artifacts.apis.io/vianai-systems/conformance/vianai-systems-conformance.yml
  title: ''
  type: Compliance
  url: conformance/vianai-systems-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vianai-systems/mcp/vianai-systems-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vianai-systems-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vianai-systems/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/vianai-systems/security/vianai-systems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vianai-systems-domain-security.yml
created: '2026-07-17'
description: Vianai Systems is an enterprise AI company whose hila platform delivers GenAI-based conversational analytics ("talk to your data") alongside a machine-learning model monitoring, deployment, and observability platform. The hila REST APIs and Python client SDK (vianops-client) let teams deploy, manage, and monitor models — covering drift detection, explainability, model performance, alerts, data profiling, inference tracking, pipelines, and segments — driven from a vianctl command-line interface. hila is delivered as a customer-deployed platform (per-tenant *.vianai.site) and is available in Google Cloud Gemini Enterprise. The company is ISO 27001 and SOC 2 compliant.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vianai-systems.png
layout: provider
modified: '2026-07-21'
name: Vianai Systems
nav: Providers
network: true
overview: 'Vianai Systems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Artificial Intelligence, Machine Learning, and MLOps.


  Vianai Systems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, CLI, and 13 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.1
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 23.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vianai-systems/vianai-systems-2026-09-02T165839.png
security:
- kind: authentication
  name: Vianai Systems Authentication
  slug: vianai-systems-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Vianai Systems Domain Security
  slug: vianai-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Authenticate to hila and list projects
  slug: vianai-systems-authenticate-and-list-projects
- name: Register, deploy, and monitor a model
  slug: vianai-systems-deploy-and-monitor-model
slug: vianai-systems
tags:
- Company
- Enterprise
- Artificial Intelligence
- Machine Learning
- MLOps
- Model Monitoring
- Analytics
- Generative AI
- Observability
- Conversational Analytics
website: https://www.vian.ai
---
