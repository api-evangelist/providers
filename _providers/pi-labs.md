---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'OpenAPI-compatible REST API for scoring, calibrating, and optimizing LLM outputs against rubrics of natural-language questions. Authenticated with an API key (WITHPI_API_KEY) sent as an Authorization '
  name: Pi Scoring API
  slug: pi-scoring-api
artifact_total: 2
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/microsoft/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://withpi.ai
- group: docs
  title: ''
  type: Documentation
  url: https://code.withpi.ai
- group: docs
  title: ''
  type: APIReference
  url: https://code.withpi.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://code.withpi.ai/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withpi
- group: operate
  title: ''
  type: ChangeLog
  url: https://withpi.ai/release-notes
- group: build
  title: ''
  type: Packages
  url: packages/pi-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pi-labs-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pi-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pi-labs-conventions.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pi-labs-llms.txt
created: '2026-07-17'
description: Pi Labs (withpi.ai) is an applied-AI company, backed by Accel and later acquired by Microsoft, that builds tooling to evaluate and enhance AI applications. Its core product, Pi Scorer, is a deterministic, roughly 200ms foundation model that scores any text against a rubric of natural-language questions — reported to be about 500x more efficient than using an LLM as a judge. Teams use it to calibrate rubrics, gate and rank LLM outputs, and close the loop across training, inference, and feedback. The scoring engine is exposed as an OpenAPI-compatible REST API at api.withpi.ai with official Python and TypeScript SDKs (both published as "withpi"), a copilot for building scoring specs, and a Promptfoo integration (Pi Scorer).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pi-labs.png
layout: provider
modified: '2026-07-20'
name: Pi Labs
nav: Providers
network: true
overview: 'Pi Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Evaluation, LLM, and Scoring.


  Pi Labs'' developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 8 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.9
  provenance:
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Pi Labs Authentication
  slug: pi-labs-authentication
  summary_line: apiKey · 1 scheme
slug: pi-labs
tags:
- Company
- Artificial Intelligence
- Evaluation
- LLM
- Scoring
- Machine-Learning
- Developer Tools
website: https://withpi.ai
---
