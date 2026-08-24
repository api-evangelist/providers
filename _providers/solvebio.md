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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API for querying biomedical and genomic datasets (now the QuartzBio EDP REST API). Served per-customer on instance hosts; requires authentication.
  name: SolveBio API
  slug: solvebio-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solvebio-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/solvebio
- group: build
  title: ''
  type: Packages
  url: packages/solvebio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/solvebio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/solvebio-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/solvebio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/solvebio-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/solvebio-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/solvebio-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/solvebio-llms.txt
created: '2026-07-17'
description: 'SolveBio is a platform for biomedical and genomic datasets that lets developers query, harmonize, and automate bioinformatics workflows over curated reference data through a REST API and first-party client libraries (Python, JavaScript, Ruby, and R). SolveBio has been rebranded to QuartzBio, a Precision for Medicine company: the solvebio.com website now redirects to quartz.bio, the legacy API is served as the QuartzBio EDP REST API on per-customer instance hosts, and the SolveBio SDKs are being deprecated in favor of the quartzbio packages (Python client end of maintenance 2026-03-31). Surfaced as a portfolio company of a16z and enriched from its public GitHub organization and package registries.'
image: https://avatars.githubusercontent.com/u/3717969?s=200&v=4
layout: provider
modified: '2026-07-21'
name: SolveBio
nav: Providers
network: true
overview: 'SolveBio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Genomics, Bioinformatics, Life Sciences, and Precision Medicine.


  SolveBio''s developer surface includes CLI, authentication, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 13.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 13.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Solvebio Authentication
  slug: solvebio-authentication
  summary_line: oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Solvebio Domain Security
  slug: solvebio-domain-security
  summary_line: TLSv1.3
slug: solvebio
tags:
- Company
- Genomics
- Bioinformatics
- Life Sciences
- Precision Medicine
- Biomedical Data
- Datasets
- SDK
---
