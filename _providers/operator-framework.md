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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
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
overview: 'Operator Framework publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automation, Cloud Native, Incubating, Kubernetes, and Lifecycle Management.


  Operator Framework''s developer surface includes documentation and 2 more developer resources.'
plans:
- name: Operator Framework Plans Pricing
  plan_count: 3
  slug: operator-framework-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 5
  name: Operator Framework Rate Limits
  slug: operator-framework-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: -1.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.4
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Cloud Native
- Incubating
- Kubernetes
- Lifecycle Management
- Operators
website: https://operatorframework.io
---
