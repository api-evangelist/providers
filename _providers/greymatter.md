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
api_count: 3
apis:
- description: The Greymatter Platform API provides programmatic access to configure and manage the Greymatter zero trust networking platform. It enables automation of service mesh deployment, zero trust policy enfo
  name: Greymatter Platform API
  slug: greymatter-platform-api
- description: The Greymatter Service Connectivity layer provides APIs for connecting services across all environments including on-premises, multi-cloud, and edge deployments. It delivers real-time traffic control,
  name: Greymatter Service Connectivity API
  slug: greymatter-service-connectivity-api
- description: The Greymatter Analytics layer provides observability APIs that unify telemetry, audit trails, and zero trust visibility across all meshes and environments. It integrates with SIEMs and APMs, supports
  name: Greymatter Analytics API
  slug: greymatter-analytics-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greymatter-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greymatterio
- group: company
  title: ''
  type: Website
  url: https://greymatter.io/
- group: docs
  title: ''
  type: Documentation
  url: https://greymatter.io/documentation/
- group: operate
  title: ''
  type: Support
  url: https://greymatter.io/contact-support/
- group: company
  title: ''
  type: Blog
  url: https://greymatter.io/filtered/?_resource_type=blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://greymatter.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://greymatter.io/terms-of-use/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/greymatter-io
created: '2026-03-16'
description: Greymatter is a Kubernetes-native, zero trust networking platform that delivers secure, agentic, and scalable service connectivity across multi-cloud, hybrid, and edge environments. It provides a unified platform with five integrated layers covering service connectivity, zero trust security, orchestration, observability analytics, and enterprise integration for distributed microservices architectures.
finops:
- name: Greymatter Finops
  service_category: API
  slug: greymatter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greymatter.png
layout: provider
modified: '2026-04-28'
name: Greymatter
nav: Providers
network: true
overview: 'Greymatter publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise, Kubernetes, Networking, Service Mesh, and Zero Trust.


  Greymatter''s developer surface includes documentation, support, engineering blog, and 6 more developer resources.'
plans:
- name: Greymatter Plans Pricing
  plan_count: 3
  slug: greymatter-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Greymatter Rate Limits
  slug: greymatter-rate-limits
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 19.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/greymatter/refs/heads/main/screenshots/greymatter-2026-06-20T182404.png
security:
- kind: domain-security
  name: Greymatter Domain Security
  slug: greymatter-domain-security
  summary_line: TLSv1.3 · DMARC
slug: greymatter
tags:
- Enterprise
- Kubernetes
- Networking
- Service Mesh
- Zero Trust
website: https://greymatter.io/
---
