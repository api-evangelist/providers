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
api_count: 1
apis:
- description: Kustomize is a Kubernetes-native configuration management tool that lets you customize untemplated YAML files for multiple purposes, leaving the original YAML intact and usable as-is, using a template
  name: Kustomize
  slug: kustomize
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kustomize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kustomize.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kubectl.docs.kubernetes.io/references/kustomize/
- group: start
  title: ''
  type: GettingStarted
  url: https://kubectl.docs.kubernetes.io/installation/kustomize/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kubernetes-sigs/kustomize
created: '2026-03-26'
description: Kustomize is a Kubernetes-native configuration management tool that lets you customize untemplated YAML files for multiple purposes, leaving the original YAML intact and usable as-is, using a template-free approach to configuration customization.
finops:
- name: Kustomize Finops
  service_category: API
  slug: kustomize-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kustomize.png
layout: provider
modified: '2026-04-28'
name: Kustomize
nav: Providers
network: true
overview: 'Kustomize publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Configuration Management, Containers, Infrastructure as Code, Kubernetes, and YAML.


  Kustomize''s developer surface includes documentation, getting-started guide, and 3 more developer resources.'
plans:
- name: Kustomize Plans Pricing
  plan_count: 3
  slug: kustomize-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Kustomize Rate Limits
  slug: kustomize-rate-limits
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kustomize/refs/heads/main/screenshots/kustomize-2026-06-20T184222.png
security:
- kind: domain-security
  name: Kustomize Domain Security
  slug: kustomize-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kustomize
tags:
- Configuration Management
- Containers
- Infrastructure as Code
- Kubernetes
- YAML
website: https://kustomize.io/
---
