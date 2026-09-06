---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Mostly Ai Agentic Access
  operation_count: 48
  slug: mostly-ai-agentic-access
  summary_line: 48 operations · 23 acting
api_count: 1
apis:
- description: REST API for the hosted MOSTLY AI Platform. Lets you manage connectors, generators, synthetic datasets, and runs. API keys are issued from the user profile menu in the web application.
  name: MOSTLY AI REST API
  slug: rest-api
- description: Open-source Python SDK (mostlyai, Apache 2.0) for training generators and producing synthetic data. Runs in LOCAL mode on user compute or CLIENT mode against the MOSTLY AI Platform. Powered by the Tab
  name: MOSTLY AI Synthetic Data SDK
  slug: python-sdk
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The About API from MOSTLY AI — 1 operation(s) for about.
  name: MOSTLY AI About API
  slug: mostly-ai-about-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Computes API from MOSTLY AI — 2 operation(s) for computes.
  name: MOSTLY AI Computes API
  slug: mostly-ai-computes-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Connectors API from MOSTLY AI — 7 operation(s) for connectors.
  name: MOSTLY AI Connectors API
  slug: mostly-ai-connectors-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Datasets API from MOSTLY AI — 2 operation(s) for datasets.
  name: MOSTLY AI Datasets API
  slug: mostly-ai-datasets-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Generators API from MOSTLY AI — 10 operation(s) for generators.
  name: MOSTLY AI Generators API
  slug: mostly-ai-generators-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Models API from MOSTLY AI — 1 operation(s) for models.
  name: MOSTLY AI Models API
  slug: mostly-ai-models-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Organizations API from MOSTLY AI — 3 operation(s) for organizations.
  name: MOSTLY AI Organizations API
  slug: mostly-ai-organizations-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Synthetic Datasets API from MOSTLY AI — 5 operation(s) for synthetic datasets.
  name: MOSTLY AI Synthetic Datasets API
  slug: mostly-ai-synthetic-datasets-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Synthetic Probes API from MOSTLY AI — 1 operation(s) for synthetic probes.
  name: MOSTLY AI Synthetic Probes API
  slug: mostly-ai-synthetic-probes-api
- baseURL: https://app.mostly.ai
  baseurl_source: declared
  description: The Users API from MOSTLY AI — 4 operation(s) for users.
  name: MOSTLY AI Users API
  slug: mostly-ai-users-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MOSTLY AI Platform REST About API
  slug: open-mostly-ai-about-api
- collection_type: open
  name: MOSTLY AI Platform REST About Computes API
  slug: open-mostly-ai-computes-api
- collection_type: open
  name: MOSTLY AI Platform REST About Connectors API
  slug: open-mostly-ai-connectors-api
- collection_type: open
  name: MOSTLY AI Platform REST About Datasets API
  slug: open-mostly-ai-datasets-api
- collection_type: open
  name: MOSTLY AI Platform REST About Generators API
  slug: open-mostly-ai-generators-api
- collection_type: open
  name: MOSTLY AI Platform REST About Models API
  slug: open-mostly-ai-models-api
- collection_type: open
  name: MOSTLY AI Platform REST About Organizations API
  slug: open-mostly-ai-organizations-api
- collection_type: open
  name: MOSTLY AI Platform REST About Synthetic Datasets API
  slug: open-mostly-ai-synthetic-datasets-api
- collection_type: open
  name: MOSTLY AI Platform REST About Synthetic Probes API
  slug: open-mostly-ai-synthetic-probes-api
- collection_type: open
  name: MOSTLY AI Platform REST About Users API
  slug: open-mostly-ai-users-api
- collection_type: open
  name: MOSTLY AI Platform REST API
  slug: open-mostly-ai
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/mostly-ai/mostlyai/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/mostly-ai/mostlyai/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/mostly-ai/mostlyai/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/mostly-ai/mostlyai/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mostly-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mostly-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mostly-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://mostly.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://mostly.ai/docs
- group: docs
  title: ''
  type: APIDocs
  url: https://api-docs.mostly.ai/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mostly-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mostly-ai
- group: commercial
  title: ''
  type: Plans
  url: plans/mostly-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mostly-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mostly-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://mostly.ai/blog
created: '2026-05-23'
description: MOSTLY AI provides a synthetic data platform for high-fidelity, privacy-safe tabular data. It ships an open-source Python SDK (mostlyai, Apache 2.0) that runs in LOCAL mode for on-prem training or CLIENT mode against the hosted MOSTLY AI Platform, plus a REST API used by both the SDK and the web app. The SDK is powered by the TabularARGN model architecture and supports differential privacy.
finops:
- name: Mostly Ai Finops
  service_category: API
  slug: mostly-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mostly-ai.png
layout: provider
modified: '2026-05-23'
name: MOSTLY AI
nav: Providers
network: true
overview: 'MOSTLY AI publishes 10 APIs on the [APIs.io](https://apis.io/) network, including About API, Computes API, Connectors API, and 7 more. Tagged areas include Synthetic Data, Privacy, Tabular, Differential Privacy, and Python SDK.


  MOSTLY AI''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 12 more developer resources.'
plans:
- name: Mostly Ai Plans Pricing
  plan_count: 1
  slug: mostly-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Mostly Ai Rate Limits
  slug: mostly-ai-rate-limits
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 56.0
    catalog_earned_first_party: 0.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 50.0
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mostly-ai/refs/heads/main/screenshots/mostly-ai-2026-06-20T185821.png
security:
- kind: authentication
  name: Mostly Ai Authentication
  slug: mostly-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mostly Ai Domain Security
  slug: mostly-ai-domain-security
  summary_line: TLSv1.3
slug: mostly-ai
tags:
- Synthetic Data
- Privacy
- Tabular
- Differential Privacy
- Python SDK
- REST
- Apache 2.0
website: https://mostly.ai/
---
