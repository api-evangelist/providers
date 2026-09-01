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
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Porter Agentic Access
  operation_count: 19
  slug: porter-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 1
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
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Porter Bundle API
  slug: open-porter-bundle
- collection_type: open
  name: Porter Bundle Bundles API
  slug: open-porter-bundles-api
- collection_type: open
  name: Porter Bundle Bundles CredentialSets API
  slug: open-porter-credentialsets-api
- collection_type: open
  name: Porter Bundle Bundles Installations API
  slug: open-porter-installations-api
- collection_type: open
  name: Porter Bundle Bundles ParameterSets API
  slug: open-porter-parametersets-api
- collection_type: open
  name: Porter Bundle Bundles Runs API
  slug: open-porter-runs-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/getporter/porter/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/getporter/porter/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/getporter/porter/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/getporter/porter/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/getporter/porter/blob/main/CONTRIBUTING.md
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
overview: 'Porter publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bundles API, CredentialSets API, Installations API, and 2 more. Tagged areas include Cloud-Native, CNAB, DevOps, Kubernetes, and Package Manager.


  The Porter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Porter''s developer surface includes authentication, documentation, getting-started guide, engineering blog, and 15 more developer resources.'
plans:
- name: Porter Plans Pricing
  plan_count: 1
  slug: porter-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Porter Rate Limits
  slug: porter-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Porter API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: porter-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 63.4
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Cloud-Native
- CNAB
- DevOps
- Kubernetes
- Package Manager
website: https://porter.sh/
---
