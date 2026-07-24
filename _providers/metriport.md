---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 13
  human_in_the_loop: 1
  name: Metriport Agentic Access
  operation_count: 30
  slug: metriport-agentic-access
  summary_line: 30 operations · 13 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Medical API consolidated FHIR data.
  name: Metriport Consolidated API
  slug: metriport-consolidated-api
- description: Devices API normalized health data.
  name: Metriport Devices Data API
  slug: metriport-devices-data-api
- description: Medical API clinical document query and retrieval.
  name: Metriport Document API
  slug: metriport-document-api
- description: Medical API facility management.
  name: Metriport Facility API
  slug: metriport-facility-api
- description: Medical API patient management.
  name: Metriport Patient API
  slug: metriport-patient-api
- description: Account settings and webhooks.
  name: Metriport Settings API
  slug: metriport-settings-api
- description: Devices API user and connect management.
  name: Metriport User API
  slug: metriport-user-api
arazzos:
- description: Register a patient, start a consolidated FHIR R4 query for the requested resources, poll until conversion completes, then count the consolidated data.
  name: Metriport Consolidated FHIR Query
  slug: metriport-consolidated-fhir-query-workflow
- description: Register a patient, trigger an IHE document query across the networks, poll until retrieval completes, list the resulting documents, and obtain a signed download URL.
  name: Metriport Patient Document Retrieval
  slug: metriport-patient-document-retrieval-workflow
- description: Create a facility, register a patient under it, then run an MPI demographic match to resolve an existing patient record.
  name: Metriport Patient Matching
  slug: metriport-patient-matching-workflow
- description: Create a devices user, mint a Connect Widget session token, then pull the user's activity and biometrics data from connected wearables.
  name: Metriport Wearables Connect
  slug: metriport-wearables-connect-workflow
artifact_total: 18
collections:
- collection_type: open
  name: Metriport API
  slug: open-metriport
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metriport-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metriport-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metriport-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metriport
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metriport
- group: company
  title: ''
  type: Website
  url: https://www.metriport.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.metriport.com
- group: commercial
  title: ''
  type: Plans
  url: plans/metriport-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metriport-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/metriport-finops.yml
- group: design
  title: ''
  type: ArazzoWorkflows
  url: ''
- group: company
  title: ''
  type: Blog
  url: https://www.metriport.com/blog
created: '2026-06-21'
description: Metriport is an open-source, universal API for healthcare data. The Medical API exchanges patient medical records across the CommonWell and Carequality networks and returns consolidated FHIR R4 data, while the Devices API hydrates activity, biometrics, nutrition, and sleep data from consumer wearables and mHealth apps. Companies can use the hosted Metriport cloud or self-host the open-source code to avoid vendor lock-in.
finops:
- name: Metriport Finops
  service_category: Healthcare and Life Sciences
  slug: metriport-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metriport.png
layout: provider
modified: '2026-06-21'
name: Metriport
nav: Providers
network: true
overview: 'Metriport publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Consolidated API, Devices Data API, Document API, and 4 more. Tagged areas include Healthcare, Medical Records, FHIR, Health Data, and Wearables.


  Metriport''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Metriport Plans Pricing
  plan_count: 4
  slug: metriport-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Metriport Rate Limits
  slug: metriport-rate-limits
score:
  band: thin
  composite: 35.3
  delta: -1.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.6
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.9
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Metriport Authentication
  slug: metriport-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metriport Domain Security
  slug: metriport-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metriport
tags:
- Healthcare
- Medical Records
- FHIR
- Health Data
- Wearables
- Open Source
website: https://www.metriport.com
---
