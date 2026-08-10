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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kyverno Agentic Access
  operation_count: 13
  slug: kyverno-agentic-access
  summary_line: 13 operations
api_count: 9
apis:
- description: Kyverno is a Kubernetes-native policy engine that runs as a dynamic admission controller to validate, mutate, and generate Kubernetes resources using policies written as Kubernetes resources. It suppo
  name: Kyverno
  slug: kyverno
- description: The Kyverno CLI provides a command-line interface for applying and testing Kyverno policies against Kubernetes resources outside of a cluster. It can be used in CI/CD pipelines to validate resources b
  name: Kyverno CLI
  slug: kyverno-cli
- description: Cluster-scoped policy report endpoints
  name: Kyverno ClusterPolicyReports API
  slug: kyverno-clusterpolicyreports-api
- description: Health and readiness endpoints
  name: Kyverno Health API
  slug: kyverno-health-api
- description: Namespace listing endpoints
  name: Kyverno Namespaces API
  slug: kyverno-namespaces-api
- description: Policy listing and detail endpoints
  name: Kyverno Policies API
  slug: kyverno-policies-api
- description: Namespaced policy report endpoints
  name: Kyverno PolicyReports API
  slug: kyverno-policyreports-api
- description: Policy result query endpoints
  name: Kyverno Results API
  slug: kyverno-results-api
- description: Policy source listing endpoints
  name: Kyverno Sources API
  slug: kyverno-sources-api
artifact_total: 18
collections:
- collection_type: open
  name: Kyverno Policy Reporter API
  slug: open-kyverno-policy-reporter
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kyverno-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyverno-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nirmata
- group: company
  title: ''
  type: Website
  url: https://kyverno.io/
- group: docs
  title: ''
  type: Documentation
  url: https://kyverno.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://kyverno.io/docs/installation/
- group: operate
  title: ''
  type: ChangeLog
  url: https://kyverno.io/docs/releases/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kyverno
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kyverno/kyverno
- group: company
  title: ''
  type: Blog
  url: https://kyverno.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://kyverno.io/community/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/kyverno-policy-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kyverno-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://kyverno.io/llms.txt
created: '2025-01-01'
description: Kyverno is a Kubernetes native policy management engine for security, automation, and governance. It uses Kubernetes admission controllers to validate, mutate, and generate configurations using policies written as Kubernetes resources.
finops:
- name: Kyverno Finops
  service_category: API
  slug: kyverno-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kyverno.png
json_schemas:
- name: Kyverno Policy
  property_count: 5
  slug: kyverno-policy
jsonld:
- class_count: 11
  name: Kyverno Context
  property_count: 47
  slug: kyverno-context
layout: provider
modified: '2026-05-19'
name: Kyverno
nav: Providers
network: true
overview: 'Kyverno publishes 7 APIs on the [APIs.io](https://apis.io/) network, including ClusterPolicyReports API, Health API, Namespaces API, and 4 more. Tagged areas include Cloud Native, Governance, Kubernetes, Policy Management, and Security.


  The Kyverno catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Kyverno''s developer surface includes documentation, getting-started guide, changelog, engineering blog, and 10 more developer resources.'
plans:
- name: Kyverno Plans Pricing
  plan_count: 3
  slug: kyverno-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 5
  name: Kyverno Rate Limits
  slug: kyverno-rate-limits
rules:
- name: Kyverno API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: kyverno-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.5
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyverno/refs/heads/main/screenshots/kyverno-2026-06-20T184228.png
security:
- kind: domain-security
  name: Kyverno Domain Security
  slug: kyverno-domain-security
  summary_line: TLSv1.3 · HSTS
slug: kyverno
tags:
- Cloud Native
- Governance
- Kubernetes
- Policy Management
- Security
website: https://kyverno.io/
---
