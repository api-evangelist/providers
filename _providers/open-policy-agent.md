---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Open Policy Agent Agentic Access
  operation_count: 18
  slug: open-policy-agent-agentic-access
  summary_line: 18 operations · 10 acting
api_count: 8
apis:
- description: The Compile API from Open Policy Agent — 1 operation(s) for compile.
  name: Open Policy Agent Compile API
  slug: open-policy-agent-compile-api
- description: The Config API from Open Policy Agent — 1 operation(s) for config.
  name: Open Policy Agent Config API
  slug: open-policy-agent-config-api
- description: The Data API from Open Policy Agent — 2 operation(s) for data.
  name: Open Policy Agent Data API
  slug: open-policy-agent-data-api
- description: The Health API from Open Policy Agent — 2 operation(s) for health.
  name: Open Policy Agent Health API
  slug: open-policy-agent-health-api
- description: The Policies API from Open Policy Agent — 2 operation(s) for policies.
  name: Open Policy Agent Policies API
  slug: open-policy-agent-policies-api
- description: The Query API API from Open Policy Agent — 1 operation(s) for query api.
  name: Open Policy Agent Query API API
  slug: open-policy-agent-query-api-api
- description: The Query API from Open Policy Agent — 1 operation(s) for query.
  name: Open Policy Agent Query API
  slug: open-policy-agent-query-api
- description: The Status API from Open Policy Agent — 1 operation(s) for status.
  name: Open Policy Agent Status API
  slug: open-policy-agent-status-api
artifact_total: 24
collections:
- collection_type: open
  name: Compile API
  slug: open-compile-api
- collection_type: open
  name: Config API
  slug: open-config-api
- collection_type: open
  name: Data API
  slug: open-data-api
- collection_type: open
  name: Health API
  slug: open-health-api
- collection_type: open
  name: Policy API
  slug: open-policy-api
- collection_type: open
  name: Query API
  slug: open-query-api
- collection_type: open
  name: Status API
  slug: open-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-policy-agent-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-policy-agent-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-policy-agent-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/open-policy-agent
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/opa-policy-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/opa-context.jsonld
- group: company
  title: ''
  type: Website
  url: https://www.openpolicyagent.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openpolicyagent.org/docs/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openpolicyagent.org/docs/latest/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.openpolicyagent.org/docs/latest/#running-opa
- group: auth
  title: ''
  type: Authentication
  url: https://www.openpolicyagent.org/docs/latest/rest-api/#authentication
- group: design
  title: ''
  type: ErrorCodes
  url: https://www.openpolicyagent.org/docs/latest/rest-api/#errors
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-policy-agent
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/open-policy-agent/opa
- group: company
  title: ''
  type: Blog
  url: https://blog.openpolicyagent.org/
- group: operate
  title: ''
  type: Community
  url: https://www.openpolicyagent.org/community/
- group: operate
  title: ''
  type: Slack
  url: https://slack.openpolicyagent.org/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/open-policy-agent/opa/blob/main/CHANGELOG.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/open-policy-agent/opa/security/policy
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/open-policy-agent
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/api-evangelist/open-policy-agent/overview
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/api-search/open-policy-agent
created: '2024-11-18'
description: Open Policy Agent (OPA) is an open-source project that provides a flexible and powerful policy engine for cloud-native environments. OPA enables users to define and enforce policies across their infrastructure, applications, and services through a declarative language called Rego. OPA integrates seamlessly with popular tools and frameworks like Kubernetes, Istio, and Envoy, making it easy to implement fine-grained access control, security, and compliance policies.
finops:
- name: Open Policy Agent Finops
  service_category: Identity / Authorization
  slug: open-policy-agent-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-policy-agent.png
json_schemas:
- name: Open Policy Agent Resources
  property_count: 0
  slug: opa-policy
jsonld:
- class_count: 0
  name: Opa Context
  property_count: 12
  slug: opa-context
layout: provider
modified: '2026-05-19'
name: Open Policy Agent
nav: Providers
network: true
overview: 'Open Policy Agent publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Compile API, Config API, Data API, and 5 more. Tagged areas include Policies and Standards.


  The Open Policy Agent catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Open Policy Agent''s developer surface includes documentation, getting-started guide, authentication, engineering blog, changelog, Stack Overflow tag, and 16 more developer resources.'
plans:
- name: Open Policy Agent Plans Pricing
  plan_count: 1
  slug: open-policy-agent-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Open Policy Agent Rate Limits
  slug: open-policy-agent-rate-limits
rules:
- name: Open Policy Agent API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: open-policy-agent-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 57.8
    developer_ergonomics: 41.3
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-policy-agent/refs/heads/main/screenshots/open-policy-agent-2026-06-20T190852.png
security:
- kind: domain-security
  name: Open Policy Agent Domain Security
  slug: open-policy-agent-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Open Policy Agent Vulnerability Disclosure
  slug: open-policy-agent-vulnerability-disclosure
  summary_line: disclosure policy published
slug: open-policy-agent
tags:
- Policies
- Standards
website: https://www.openpolicyagent.org/
---
