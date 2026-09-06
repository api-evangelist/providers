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
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The CNCF Cloud Native Interactive Landscape is the canonical map of the cloud-native ecosystem. The landscape is generated daily from landscape.yml and enriched with data from Crunchbase and GitHub. T
  name: CNCF Cloud Native Interactive Landscape
  slug: cncf-landscape
- description: CNCF stewards an open-source project portfolio whose APIs underpin much of modern cloud infrastructure - Kubernetes API, OpenTelemetry, CloudEvents, gRPC, CNI, CSI, OCI image and runtime specs, Promet
  name: CNCF Hosted Projects (Standards Steward)
  slug: cncf-projects
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cncf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cncf.io/
- group: other
  title: ''
  type: Landscape
  url: https://landscape.cncf.io/
- group: other
  title: ''
  type: Catalog
  url: https://www.cncf.io/projects/
- group: company
  title: ''
  type: Blog
  url: https://www.cncf.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cncf
- group: company
  title: ''
  type: About
  url: https://www.cncf.io/all-cncf/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy/
- group: other
  title: ''
  type: X
  url: https://twitter.com/CloudNativeFdn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloud-native-computing-foundation/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/cloudnativefdn
created: '2025-01-01'
description: The Cloud Native Computing Foundation (CNCF) is part of the Linux Foundation and hosts critical components of the global cloud-native technology infrastructure - including Kubernetes, Prometheus, Envoy, etcd, OpenTelemetry, CloudEvents, gRPC, and CNI. CNCF stewards open-source project governance and publishes the Cloud Native Interactive Landscape, a community-curated dataset (landscape.yml) of cloud-native projects and products with metadata such as GitHub stars, contributor counts, funding, and headquarters location.
finops:
- name: Cncf Finops
  service_category: API
  slug: cncf-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cncf.png
layout: provider
modified: '2026-04-23'
name: CNCF
nav: Providers
network: true
overview: 'CNCF publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Containers, Kubernetes, Open-Source, and Standards.


  CNCF''s developer surface includes engineering blog, YouTube channel, and 9 more developer resources.'
plans:
- name: Cncf Plans Pricing
  plan_count: 3
  slug: cncf-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Cncf Rate Limits
  slug: cncf-rate-limits
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 15.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cncf/refs/heads/main/screenshots/cncf-2026-06-20T174634.png
security:
- kind: domain-security
  name: Cncf Domain Security
  slug: cncf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cncf
tags:
- Cloud-Native
- Containers
- Kubernetes
- Open-Source
- Standards
website: https://www.cncf.io/
---
