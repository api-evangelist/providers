---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/thundra/refs/heads/main/security/thundra-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thundra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thundra.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thundra-io
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/thundra/refs/heads/main/packages/thundra-packages.yml
  title: ''
  type: Packages
  url: packages/thundra-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/thundra/refs/heads/main/llms/thundra-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thundra-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/thundra/refs/heads/main/lifecycle/thundra-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thundra-lifecycle.yml
created: '2026-07-17'
description: Thundra was an application observability and security platform for serverless, container, and VM workloads, best known for AWS Lambda monitoring and debugging. Its products included Thundra APM (distributed tracing), Sidekick (remote debugging), and Foresight (CI pipeline test observability). Founded in 2018 out of OpsGenie and backed by Battery Ventures, its assets were acquired by Catchpoint in April 2023 and the service has been discontinued — thundra.io now redirects to Catchpoint's acquisition announcement and the GitHub organization states "Thundra is no longer in service." Its open-source agents and plugins remain published on npm, PyPI, Maven Central, NuGet, and pkg.go.dev.
image: https://avatars.githubusercontent.com/u/36259632
layout: provider
modified: '2026-07-21'
name: Thundra
nav: Providers
network: true
overview: Thundra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Serverless, APM, and Monitoring.
random_paper: 10
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/thundra/refs/heads/main/screenshots/thundra-2026-09-02T163647.png
security:
- kind: domain-security
  name: Thundra Domain Security
  slug: thundra-domain-security
  summary_line: no transport/DNS hardening detected
slug: thundra
tags:
- Company
- Observability
- Serverless
- APM
- Monitoring
- Debugging
- AWS Lambda
- Defunct
- Developer Tools
website: https://www.thundra.io
---
