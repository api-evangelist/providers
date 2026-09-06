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
- description: OLM extends Kubernetes with CRDs for operator lifecycle management including ClusterServiceVersion for describing operator capabilities and requirements, Subscription for tracking update channels, Ins
  name: Operator Lifecycle Manager API
  slug: olm-api
- description: The Operator SDK provides tools for building Kubernetes operators. It includes scaffolding commands, code generation for CRD types and controllers, integration testing harness, scorecard for validatin
  name: Operator SDK
  slug: operator-sdk
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/operator-framework-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://operatorframework.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/operator-framework
created: '2026-03-16'
description: The Operator Framework is a CNCF incubating toolkit for building and managing Kubernetes Operators. It includes the Operator SDK for scaffolding and building operators using Go, Ansible, or Helm, the Operator Lifecycle Manager (OLM) for installing and managing operators on clusters, and OperatorHub for discovering and sharing operators. The framework codifies operational knowledge into software.
finops:
- name: Operator Framework Finops
  service_category: API
  slug: operator-framework-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/operator-framework.png
layout: provider
modified: '2026-04-28'
name: Operator Framework
nav: Providers
network: true
overview: 'Operator Framework publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Cloud-Native, Incubating, Kubernetes, and Lifecycle Management.


  Operator Framework''s developer surface includes documentation and 2 more developer resources.'
plans:
- name: Operator Framework Plans Pricing
  plan_count: 3
  slug: operator-framework-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Operator Framework Rate Limits
  slug: operator-framework-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 9.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 13.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/operator-framework/refs/heads/main/screenshots/operator-framework-2026-06-20T191058.png
security:
- kind: domain-security
  name: Operator Framework Domain Security
  slug: operator-framework-domain-security
  summary_line: TLSv1.3 · HSTS
slug: operator-framework
tags:
- Automation
- Cloud-Native
- Incubating
- Kubernetes
- Lifecycle Management
- Operators
website: https://operatorframework.io
---
