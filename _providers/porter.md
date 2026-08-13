---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Porter Agentic Access
  operation_count: 19
  slug: porter-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 7
apis:
- description: Extension interface for building and using mixins, which are the building blocks for authoring Porter bundles. Mixins provide pre-built integrations for interacting with tools and services such as Kub
  name: Porter Mixins API
  slug: porter-mixins-api
- description: Plugin interface that allows extending Porter's core functionality, such as storing installation data, credential sets, and parameter sets in external systems like cloud storage instead of the local f
  name: Porter Plugins API
  slug: porter-plugins-api
- description: Operations for searching, inspecting, and managing CNAB bundles published to OCI registries.
  name: Porter Bundles API
  slug: porter-bundles-api
- description: Operations for managing credential sets that supply secret values to bundle executions.
  name: Porter CredentialSets API
  slug: porter-credentialsets-api
- description: Operations for managing bundle installations, including install, upgrade, invoke, and uninstall lifecycle actions.
  name: Porter Installations API
  slug: porter-installations-api
- description: Operations for managing parameter sets that supply configuration values to bundle executions.
  name: Porter ParameterSets API
  slug: porter-parametersets-api
- description: Operations for querying the history of bundle action executions and their outputs.
  name: Porter Runs API
  slug: porter-runs-api
artifact_total: 17
collections:
- collection_type: open
  name: Porter Bundle API
  slug: open-porter-bundle
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/getporter/porter/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/porter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/porter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/porter-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/porterrun
- group: company
  title: ''
  type: Website
  url: https://porter.sh/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/porter-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/porter-manifest-schema.json
- group: docs
  title: ''
  type: Documentation
  url: https://porter.sh/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://porter.sh/docs/learn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getporter
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/getporter/porter
- group: operate
  title: ''
  type: Community
  url: https://porter.sh/community/
- group: company
  title: ''
  type: Blog
  url: https://porter.sh/blog/index.xml
created: '2025'
description: A package manager for Kubernetes that uses Cloud Native Application Bundles (CNAB) to package and deploy applications along with their dependencies and configuration.
finops:
- name: Porter Finops
  service_category: DevOps Tooling
  slug: porter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/porter.png
json_schemas:
- name: Porter Bundle Manifest
  property_count: 23
  slug: porter-manifest
jsonld:
- class_count: 0
  name: Porter Context
  property_count: 9
  slug: porter-context
layout: provider
modified: '2026-05-19'
name: Porter
nav: Providers
network: true
overview: 'Porter publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bundles API, CredentialSets API, Installations API, and 2 more. Tagged areas include Cloud Native, CNAB, DevOps, Kubernetes, and Package Manager.


  The Porter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Porter''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 10 more developer resources.'
plans:
- name: Porter Plans Pricing
  plan_count: 1
  slug: porter-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 1
  name: Porter Rate Limits
  slug: porter-rate-limits
rules:
- name: Porter API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: porter-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.1
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 64.9
    developer_ergonomics: 37.0
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/porter/refs/heads/main/screenshots/porter-2026-06-20T191932.png
security:
- kind: authentication
  name: Porter Authentication
  slug: porter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Porter Domain Security
  slug: porter-domain-security
  summary_line: TLSv1.3 · HSTS
slug: porter
tags:
- Cloud Native
- CNAB
- DevOps
- Kubernetes
- Package Manager
website: https://porter.sh/
---
