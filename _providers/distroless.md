---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Distroless images by Google contain only the application and its runtime dependencies, stripping out package managers, shells, and other OS-level utilities to minimize attack surface and image size.
  name: Distroless
  slug: distroless
artifact_total: 4
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/distroless/refs/heads/main/plans/distroless-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/distroless-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/distroless/refs/heads/main/rate-limits/distroless-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/distroless-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/distroless/refs/heads/main/finops/distroless-finops.yml
  title: ''
  type: FinOps
  url: finops/distroless-finops.yml
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/GoogleContainerTools/distroless/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/GoogleContainerTools/distroless/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/GoogleContainerTools/distroless/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://github.com/GoogleContainerTools/distroless
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleContainerTools
- group: start
  title: ''
  type: Container Registry
  url: https://gcr.io/distroless
- group: operate
  title: ''
  type: Issues
  url: https://github.com/GoogleContainerTools/distroless/issues
created: '2026-03-26'
description: Distroless images by Google contain only the application and its runtime dependencies, stripping out package managers, shells, and other OS-level utilities to minimize attack surface and image size. The smallest variant (gcr.io/distroless/static-debian12) is roughly 2 MB. Distroless ships base images for static binaries, glibc-based binaries, C/C++, Java (17, 21, 25), Node.js (22, 24), and Python 3, with multi-architecture support including amd64, arm64, arm, s390x, ppc64le, and riscv64. Adopters include Kubernetes, Knative, Tekton, and Teleport.
finops:
- has_sources: false
  method: generated
  name: Distroless Finops
  primary_unit: ''
  service_category: API
  slug: distroless-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/distroless.png
layout: provider
modified: '2026-04-28'
name: Distroless
nav: Providers
network: true
overview: Distroless is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Container Images, Containers, Google, and Security.
plans:
- name: Distroless Plans Pricing
  plan_count: 3
  slug: distroless-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Distroless Rate Limits
  slug: distroless-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 60.0
  previous_composite: 18.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/distroless/refs/heads/main/screenshots/distroless-2026-06-20T180057.png
slug: distroless
tags:
- Cloud-Native
- Container Images
- Containers
- Google
- Security
---
