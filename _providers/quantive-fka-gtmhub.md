---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://quantive.com/'', ''status'': 302, ''note'': ''declared website redirects to https://www.workboard.com/ — a different registrable domain (quantive.com -> workboard.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://quantive.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Gtmhub
- group: build
  title: ''
  type: Packages
  url: packages/quantive-fka-gtmhub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/quantive-fka-gtmhub-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/quantive-fka-gtmhub-cli.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantive-fka-gtmhub-domain-security.yml
created: '2026-07-17'
description: 'Quantive (formerly Gtmhub) is a strategy-execution and OKR (Objectives and Key Results) SaaS platform, historically backed by Insight Partners. The company and its "Quantive Results" product have since been acquired and folded into WorkBoard — quantive.com now redirects to workboard.com and the developer portal (developer.quantive.com) has been decommissioned. The public REST API and OpenAPI reference are no longer reachable, but first-party developer tooling remains published on public registries: the @gtmhub/sdk extensibility SDK on npm (for building marketplace plugins and insights) and the gtmhub-cli command-line client (distributed via Homebrew, Chocolatey, and GitHub releases). This profile captures the surviving developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantive-fka-gtmhub.png
layout: provider
modified: '2026-07-20'
name: Quantive (fka Gtmhub)
nav: Providers
network: true
overview: 'Quantive (fka Gtmhub) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OKR, Strategy Execution, Goal Management, and Performance Management.


  Quantive (fka Gtmhub)''s developer surface includes CLI and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quantive-fka-gtmhub/refs/heads/main/screenshots/quantive-fka-gtmhub-2026-09-02T152613.png
security:
- kind: domain-security
  name: Quantive Fka Gtmhub Domain Security
  slug: quantive-fka-gtmhub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: quantive-fka-gtmhub
tags:
- Company
- OKR
- Strategy Execution
- Goal Management
- Performance Management
- Software-as-a-Service
- Extensibility SDK
- CLI
website: https://quantive.com/
---
