---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: REST API hosted on api.anaconda.org that provides read access to conda-forge package metadata including package details, version lists, platform availability, download counts, licensing, and distribut
  name: Anaconda.org Package API
  slug: anacondaorg-package-api
- description: Static JSON index files served over HTTPS from conda.anaconda.org for each supported platform subdirectory (linux-64, osx-64, win-64, etc.). repodata.json and repodata.json.zst enumerate every availab
  name: conda-forge Channel Repodata API
  slug: conda-forge-channel-repodata-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/conda-forge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conda-forge-domain-security.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://conda-forge.org/docs/user/introduction/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/conda-forge
- group: operate
  title: ''
  type: Status
  url: https://conda-forge.org/status/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anaconda.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anaconda.com/terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://conda-forge.org/news/
- group: operate
  title: ''
  type: Forums
  url: https://github.com/conda-forge/conda-forge.github.io/discussions
- group: other
  title: ''
  type: Chat
  url: https://conda-forge.zulipchat.com/
- group: operate
  title: ''
  type: Support
  url: https://github.com/conda-forge/conda-forge.github.io/issues
created: '2026-06-13'
description: conda-forge is a community-led conda package channel providing over 33,000 open-source packages for scientific computing, data science, and general Python development. The project offers programmatic access through the Anaconda.org REST API for querying package metadata, searching packages by name, retrieving version histories, and accessing distribution file details. Additionally, the conda repository format exposes repodata and channeldata JSON indices that enumerate all packages, versions, platforms, and dependency metadata across every supported architecture.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://conda-forge.org/assets/img/anvil_white.png
layout: provider
modified: '2026-06-13'
name: conda-forge
nav: Providers
network: true
overview: 'conda-forge publishes 1 API on the [APIs.io](https://apis.io/) network: Anaconda.org Package API. Tagged areas include Conda, Packages, Scientific Computing, Python, and Open-Source.


  conda-forge''s developer surface includes getting-started guide, GitHub presence, status page, engineering blog, support, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 1
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 28.4
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conda-forge/refs/heads/main/screenshots/conda-forge-2026-06-20T174843.png
security:
- kind: domain-security
  name: Conda Forge Domain Security
  slug: conda-forge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Conda Forge Vulnerability Disclosure
  slug: conda-forge-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: conda-forge
tags:
- Conda
- Packages
- Scientific Computing
- Python
- Open-Source
---
