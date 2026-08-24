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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 2
apis:
- description: 'StormForge Optimize Live is a Kubernetes resource rightsizing product that uses machine learning to automatically generate CPU and memory recommendations for container workloads. An agent deployed to '
  name: StormForge Optimize Live
  slug: optimize-live
- description: Command-line interface for interacting with the StormForge platform to manage clusters, workloads, and optimization recommendations. Supports authentication, resource inspection, recommendation genera
  name: StormForge CLI
  slug: stormforge-cli
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stormforge-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stormforge
- group: company
  title: ''
  type: Website
  url: https://www.stormforge.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stormforge.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stormforge.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.stormforge.io/blog/
- group: company
  title: ''
  type: About
  url: https://www.stormforge.io/about/
- group: operate
  title: ''
  type: Contact
  url: https://www.stormforge.io/contact/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stormforge.io/docs/get-started/
- group: start
  title: ''
  type: Signup
  url: https://app.stormforge.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/thestormforge
- group: start
  title: ''
  type: Sandbox
  url: https://docs.stormforge.io/docs/sandbox/
- group: commercial
  title: ''
  type: FinOps
  url: https://www.finops.org/members/stormforge/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.stormforge.io/llms.txt
created: '2026-03-27'
description: StormForge provides machine learning-based Kubernetes resource optimization (rightsizing) for reducing cloud infrastructure costs while maintaining application performance. The Optimize Live product deploys an agent to Kubernetes clusters that collects workload metrics, applies ML algorithms, and generates CPU and memory recommendations for containers. Recommendations can be applied automatically, on-demand, or exported as Kubernetes patches for GitOps workflows. StormForge supports Deployments, StatefulSets, DaemonSets, ReplicaSets, and custom workload types, and integrates with Karpenter, HPA, VPA, Argo CD, and APM tools.
finops:
- name: Stormforge Finops
  service_category: API
  slug: stormforge-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stormforge.png
json_schemas:
- name: StormForge Recommendation
  property_count: 11
  slug: stormforge-recommendation
json_structures:
- name: Stormforge Recommendation Structure
  property_count: 0
  slug: stormforge-recommendation-structure
jsonld:
- class_count: 0
  name: Stormforge Context
  property_count: 19
  slug: stormforge-context
layout: provider
modified: '2026-05-02'
name: StormForge
nav: Providers
network: true
overview: 'StormForge publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud Cost Optimization, DevOps, FinOps, Kubernetes, and Machine-Learning.


  The StormForge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  StormForge''s developer surface includes documentation, pricing, engineering blog, getting-started guide, signup flow, sandbox, and 8 more developer resources.'
plans:
- name: Stormforge Plans Pricing
  plan_count: 3
  slug: stormforge-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Stormforge Rate Limits
  slug: stormforge-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: StormForge API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: stormforge-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 11.3
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 23.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stormforge/refs/heads/main/screenshots/stormforge-2026-06-20T194605.png
security:
- kind: domain-security
  name: Stormforge Domain Security
  slug: stormforge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stormforge
tags:
- Cloud Cost Optimization
- DevOps
- FinOps
- Kubernetes
- Machine-Learning
- Resource Management
- Rightsizing
website: https://www.stormforge.io/
---
