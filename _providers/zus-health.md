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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Zus FHIR R4 REST API plus Auth Service and Patient History APIs. Implements FHIR R4 (v4.0.1) across 128 resource types with instance-level CRUD, transaction Bundles, conditional create/update/delete b
  name: Zus FHIR & Platform API
  slug: zus-fhir-platform-api
- description: The Zus FHIR Query Service (FQS) is a read-only GraphQL API over the FHIR data model, exposed at a single endpoint. Supports UPID-scoped (one-human) and builder-scoped queries across resource types in
  name: Zus FHIR GraphQL API (FQS)
  slug: zus-fhir-graphql-api-fqs
artifact_total: 6
asyncapis:
- description: ''
  name: Zus Health Zushooks
  slug: zus-health-zushooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zushealth.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zushealth.com/docs/intro-to-zus
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zushealth.com/reference/general
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zushealth.com/docs/getting-started-with-the-zap
- group: operate
  title: ''
  type: Support
  url: https://docs.zushealth.com/contact-support
- group: company
  title: ''
  type: Blog
  url: https://zushealth.com/team/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zushealth
- group: start
  title: ''
  type: SignUp
  url: https://docs.zushealth.com/page/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.zushealth.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zushealth.com/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zushealth.com/website-privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zusapi.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zus-health/workspace/zus-health-workspace
- group: auth
  title: ''
  type: Compliance
  url: https://zushealth.com/platform/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zus-health-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zus-health-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zus-health-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zus-health-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zus-health-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/zus-health-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/zus-health-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zus-health-zushooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zus-health-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zus-health-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zus-health-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zus-health-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zus-health-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zus-health-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/zus-health-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Zus Health is a next-generation shared health data platform that brings information speed to healthcare. Its flagship Zus Aggregated Profile (ZAP) consolidates a patient's longitudinal medical record — encounters, conditions, medications, labs, and transitions of care sourced from EHR, pharmacy, ADT, and lab networks plus TEFCA — into a single, deduplicated, FHIR R4-native view accessible via a standalone app, embeddable UI, or API. Zus exposes a FHIR R4 REST API and a read-only FHIR GraphQL Query Service (FQS) over 128 FHIR resource types, an Auth Service for machine-to-machine and user authentication, Patient History APIs for network enrollment and querying, Zushooks event webhooks, and SQL-friendly relational data marts on Snowflake and Databricks. The platform is SOC 2 Type 2 compliant and HIPAA-compliant.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zus-health.png
layout: provider
mcp_servers:
- description: ''
  name: zus-health-mcp.yml
  slug: zus-health-mcpyml
modified: '2026-07-21'
name: Zus Health
nav: Providers
network: true
overview: 'Zus Health publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, FHIR, and Interoperability.


  The Zus Health catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zus Health''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 50.3
  delta: 1.6
  facets:
    commercial_clarity: 42.1
    contract_quality: 55.0
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 48.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Zus Health Authentication
  slug: zus-health-authentication
  summary_line: oauth2/openIdConnect/http · 4 schemes
- kind: domain-security
  name: Zus Health Domain Security
  slug: zus-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zus-health
tags:
- Company
- Health
- Healthcare
- FHIR
- Interoperability
- Health Data
- Patient Records
- EHR
- GraphQL
- Webhooks
website: https://docs.zushealth.com/docs
---
