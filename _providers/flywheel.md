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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 13.5
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Full REST API for the Flywheel platform, covering the container hierarchy (groups, projects, subjects, sessions, acquisitions, files, analyses), gears and jobs, users and permissions, and search. Docu
  name: Flywheel Core API
  slug: flywheel-core-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flywheel.io/Developer_Guides/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flywheel.io/Developer_Guides/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.flywheel.io/latest/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.flywheel.io/latest/tags/16.19.2/python/getting_started_new.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/flywheel-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/flywheel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flywheel-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/flywheel-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flywheel-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flywheel-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flywheel-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/flywheel-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flywheel-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flywheel-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://flywheel.io/compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/flywheel-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flywheel-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flywheel-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flywheel-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://forum.flywheel.io
- group: company
  title: ''
  type: Blog
  url: https://flywheel.io/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flywheel-io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flywheel.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flywheel.io/terms/
- group: company
  title: ''
  type: Website
  url: https://flywheel.io
created: '2026-07-17'
description: Flywheel is a medical imaging data management and AI development platform for biomedical research, clinical trials, and medical device R&D. It securely ingests, organizes, de-identifies, processes, and analyzes imaging data (DICOM, NIfTI, and more) in a strict container hierarchy (Group, Project, Subject, Session, Acquisition, File, Analysis) and automates workflows with reusable plug-in applications called Gears. Developers integrate through a per-instance REST API documented with Swagger, an official Python SDK, a command line interface, and an open-source Developer Toolkit (fw-client, fw-file, fw-gear, fw-curation, fw-classification). Flywheel is HIPAA, SOC 2/SOC 3, GDPR, and 21 CFR Part 11 compliant. Surfaced as an 8vc portfolio company and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flywheel.png
layout: provider
modified: '2026-07-19'
name: Flywheel
nav: Providers
network: true
overview: 'Flywheel publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Imaging, Healthcare, Data Management, and Machine Learning.


  Flywheel''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, support, and 18 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 38.2
  delta: 4.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 33.4
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Flywheel Authentication
  slug: flywheel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Flywheel Domain Security
  slug: flywheel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Flywheel Trust Center
  slug: flywheel-trust-center
  summary_line: HIPAA, SOC 2, SOC 3, GDPR, 21 CFR Part 11, IRB
slug: flywheel
tags:
- Company
- Medical Imaging
- Healthcare
- Data Management
- Machine Learning
- Research
- DICOM
- Life Sciences
website: https://flywheel.io
---
