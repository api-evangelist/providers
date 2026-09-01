---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
- acting_count: 17
  human_in_the_loop: 0
  name: Crossplane Agentic Access
  operation_count: 31
  slug: crossplane-agentic-access
  summary_line: 31 operations · 17 acting
api_count: 1
apis:
- description: 'CompositeResourceDefinitions (XRDs) extend the Kubernetes API with new custom resource types. An XRD defines the schema and API surface for a composite resource and an optional namespace-scoped claim '
  name: Crossplane CompositeResourceDefinitions API
  slug: crossplane-compositeresourcedefinitions-api
- description: Compositions define how to compose a set of managed resources or Composition Functions into a higher-level composite resource. A Composition acts as a template that maps fields from a composite resour
  name: Crossplane Compositions API
  slug: crossplane-compositions-api
- description: Configurations are Crossplane packages that bundle Compositions and CompositeResourceDefinitions together into a distributable unit that can be installed into a Crossplane control plane.
  name: Crossplane Configurations API
  slug: crossplane-configurations-api
- description: DeploymentRuntimeConfigs customize the runtime behavior of Provider and Function deployments, including replica counts, resource limits, service account annotations, and pod template overrides.
  name: Crossplane DeploymentRuntimeConfigs API
  slug: crossplane-deploymentruntimeconfigs-api
- description: EnvironmentConfigs provide shared configuration data that can be referenced by Compositions via environment patches, enabling reusable configuration across multiple Compositions.
  name: Crossplane EnvironmentConfigs API
  slug: crossplane-environmentconfigs-api
- description: Functions are Crossplane packages that contain Composition Functions, which are OCI container images invoked during composition to perform advanced resource templating and transformation logic.
  name: Crossplane Functions API
  slug: crossplane-functions-api
- description: Providers are Crossplane packages that install controllers and CRDs for managing resources on a specific infrastructure platform such as AWS, GCP, or Azure.
  name: Crossplane Providers API
  slug: crossplane-providers-api
artifact_total: 35
collections:
- collection_type: postman
  name: Crossplane Kubernetes CompositeResourceDefinitions API
  slug: postman-crossplane-compositeresourcedefinitions-api
- collection_type: postman
  name: Crossplane Kubernetes CompositeResourceDefinitions Compositions API
  slug: postman-crossplane-compositions-api
- collection_type: postman
  name: Crossplane Kubernetes CompositeResourceDefinitions Configurations API
  slug: postman-crossplane-configurations-api
- collection_type: postman
  name: Crossplane Kubernetes CompositeResourceDefinitions DeploymentRuntimeConfigs API
  slug: postman-crossplane-deploymentruntimeconfigs-api
- collection_type: postman
  name: Crossplane Kubernetes CompositeResourceDefinitions EnvironmentConfigs API
  slug: postman-crossplane-environmentconfigs-api
- collection_type: postman
  name: Crossplane Kubernetes CompositeResourceDefinitions Functions API
  slug: postman-crossplane-functions-api
- collection_type: postman
  name: Crossplane Kubernetes CompositeResourceDefinitions Providers API
  slug: postman-crossplane-providers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crossplane Kubernetes CompositeResourceDefinitions API
  slug: open-crossplane-compositeresourcedefinitions-api
- collection_type: open
  name: Crossplane Kubernetes CompositeResourceDefinitions Compositions API
  slug: open-crossplane-compositions-api
- collection_type: open
  name: Crossplane Kubernetes CompositeResourceDefinitions Configurations API
  slug: open-crossplane-configurations-api
- collection_type: open
  name: Crossplane Kubernetes CompositeResourceDefinitions DeploymentRuntimeConfigs API
  slug: open-crossplane-deploymentruntimeconfigs-api
- collection_type: open
  name: Crossplane Kubernetes CompositeResourceDefinitions EnvironmentConfigs API
  slug: open-crossplane-environmentconfigs-api
- collection_type: open
  name: Crossplane Kubernetes CompositeResourceDefinitions Functions API
  slug: open-crossplane-functions-api
- collection_type: open
  name: Crossplane Kubernetes API
  slug: open-crossplane-kubernetes-api
- collection_type: open
  name: Crossplane Kubernetes CompositeResourceDefinitions Providers API
  slug: open-crossplane-providers-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/crossplane/crossplane/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/crossplane/crossplane/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/crossplane/crossplane/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/crossplane/crossplane/blob/main/CONTRIBUTING.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/crossplane/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crossplane-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crossplane-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crossplane-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crossplane
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/crossplane-composition-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/crossplane-xrd-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/crossplane-provider-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/crossplane-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/crossplane-vocabulary.yml
- group: company
  title: ''
  type: Website
  url: https://www.crossplane.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crossplane.io/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crossplane.io/latest/get-started/get-started-with-composition/
- group: docs
  title: ''
  type: Reference
  url: https://docs.crossplane.io/latest/api/
- group: company
  title: ''
  type: Blog
  url: https://blog.crossplane.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crossplane
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/crossplane/crossplane
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/crossplane/crossplane/releases
- group: operate
  title: ''
  type: Community
  url: https://docs.crossplane.io/latest/learn/
- group: other
  title: ''
  type: Contributing
  url: https://docs.crossplane.io/contribute/contribute/
- group: commercial
  title: ''
  type: License
  url: https://github.com/crossplane/crossplane/blob/main/LICENSE
- group: other
  title: ''
  type: CNCF
  url: https://www.cncf.io/projects/crossplane/
created: '2025-01-01'
description: Crossplane is a graduated CNCF open-source Kubernetes add-on that transforms a cluster into a universal control plane for cloud infrastructure, services, and applications. Crossplane introduces custom resources including CompositeResourceDefinitions (XRDs), Compositions, Claims, Providers, ProviderConfigs, Configurations, Functions, and EnvironmentConfigs, allowing platform teams to author self-service platform APIs that compose managed resources across AWS, GCP, Azure, and other providers using Kubernetes-style declarative configuration.
finops:
- name: Crossplane Finops
  service_category: API
  slug: crossplane-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crossplane.png
json_schemas:
- name: Crossplane Composition
  property_count: 4
  slug: crossplane-composition
- name: Crossplane Provider Configuration
  property_count: 0
  slug: crossplane-provider
- name: Crossplane CompositeResourceDefinition (XRD)
  property_count: 4
  slug: crossplane-xrd
jsonld:
- class_count: 6
  name: Crossplane Context
  property_count: 17
  slug: crossplane-context
layout: provider
modified: '2026-05-19'
name: Crossplane
nav: Providers
network: true
overview: 'Crossplane publishes 7 APIs on the [APIs.io](https://apis.io/) network, including CompositeResourceDefinitions API, Compositions API, Configurations API, and 4 more. Tagged areas include Apache 2.0, CNCF, Cloud-Native, Composition, and Control Plane.


  The Crossplane catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Crossplane''s developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, and 21 more developer resources.'
plans:
- name: Crossplane Plans Pricing
  plan_count: 3
  slug: crossplane-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Crossplane Rate Limits
  slug: crossplane-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Crossplane API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: crossplane-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Crossplane API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: crossplane-kubernetes-api-rules
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 72.9
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 50.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crossplane/refs/heads/main/screenshots/crossplane-2026-08-17T082555.png
security:
- kind: authentication
  name: Crossplane Authentication
  slug: crossplane-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crossplane Domain Security
  slug: crossplane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crossplane
tags:
- Apache 2.0
- CNCF
- Cloud-Native
- Composition
- Control Plane
- Custom Resource Definitions
- Graduated
- Infrastructure as Code
- Kubernetes
- Multi-Cloud
- Open-Source
- Platform Engineering
- Providers
website: https://www.crossplane.io/
---
