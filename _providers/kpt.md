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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: kpt package-centric toolchain for Kubernetes configuration management and delivery.
  name: Kpt
  slug: kpt
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kpt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kpt.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://kpt.dev/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleContainerTools/kpt
created: '2025-01-01'
description: kpt is a package-centric toolchain that enables a configuration authoring, automation, and delivery experience, which simplifies managing Kubernetes platforms and KRM-driven infrastructure at scale by utilizing resource configuration as the artifact of record.
finops:
- name: Kpt Finops
  service_category: API
  slug: kpt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kpt.png
layout: provider
modified: '2026-04-28'
name: Kpt
nav: Providers
network: true
overview: 'Kpt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Configuration Management, GitOps, Infrastructure as Code, and Kubernetes.


  Kpt''s developer surface includes documentation and 3 more developer resources.'
plans:
- name: Kpt Plans Pricing
  plan_count: 3
  slug: kpt-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Kpt Rate Limits
  slug: kpt-rate-limits
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kpt/refs/heads/main/screenshots/kpt-2026-06-20T184145.png
security:
- kind: domain-security
  name: Kpt Domain Security
  slug: kpt-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kpt
tags:
- Configuration Management
- GitOps
- Infrastructure as Code
- Kubernetes
website: https://kpt.dev/
---
