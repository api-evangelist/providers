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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 9.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'Multi-tenant REST API for the Cogniac computer-vision platform (CloudCore): manage tenants, applications, subjects, media, detections, EdgeFlow/CloudFlow appliances, network cameras, deployment groups'
  name: Cogniac Public API
  slug: cogniac-public-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://cogniac.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.cogniac.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cogniac.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cogniac.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Cogniac/cogniac-sdk-py
- group: start
  title: ''
  type: Login
  url: https://cogniac.io/app/login
- group: operate
  title: ''
  type: Support
  url: https://cogniac.ai/contact/
- group: company
  title: ''
  type: Blog
  url: https://cogniac.ai/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cogniac
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cogniac.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cogniac.ai/privacy/
- group: build
  title: ''
  type: Packages
  url: packages/cogniac-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cogniac-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cogniac-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cogniac-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cogniac-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cogniac-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cogniac-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cogniac-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cogniac.ai/news/cogniac-confirmed-as-soc2-compliant/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cogniac-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cogniac-llms.txt
created: '2026-07-17'
description: Cogniac is a low-code enterprise AI computer-vision platform that turns visual data from cameras and image/video streams into automated visual inspection and defect detection across manufacturing, transportation, logistics, and government operations. Its cloud platform (CloudCore) exposes a multi-tenant public REST API at api.cogniac.io covering tenants, applications (classification, box/point detection, http_input, camera_capture, and integration types), subjects, media, detections, on-premise EdgeFlow GPU appliances, cloud-hosted CloudFlow, network cameras, deployment groups, and workflows. Cogniac ships an official Python SDK and CLI (plus an archived C# SDK) and a provider-published agent skill, and is SOC 2 compliant.
image: https://github.com/Cogniac.png
layout: provider
modified: '2026-07-18'
name: Cogniac
nav: Providers
network: true
overview: 'Cogniac publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Computer-Vision, Artificial Intelligence, Machine-Learning, and Visual Inspection.


  Cogniac''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 16 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 26.1
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cogniac/refs/heads/main/screenshots/cogniac-2026-07-25T210000.png
security:
- kind: authentication
  name: Cogniac Authentication
  slug: cogniac-authentication
  summary_line: apiKey/http/browserLogin · 4 schemes
- kind: domain-security
  name: Cogniac Domain Security
  slug: cogniac-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cogniac
tags:
- Company
- Computer-Vision
- Artificial Intelligence
- Machine-Learning
- Visual Inspection
- Defect Detection
- Edge AI
- Manufacturing
- Industrial IoT
- MLOps
website: https://cogniac.ai/
---
