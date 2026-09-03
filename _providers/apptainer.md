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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Apptainer Agentic Access
  operation_count: 5
  slug: apptainer-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.apptainer.org/v1
  baseurl_source: spec
  description: Container image management
  name: Apptainer Images API
  slug: apptainer-images-api
- baseURL: https://api.apptainer.org/v1
  baseurl_source: spec
  description: Running container instance management
  name: Apptainer Instances API
  slug: apptainer-instances-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apptainer Container Runtime Images API
  slug: open-apptainer-images-api
- collection_type: open
  name: Apptainer Container Runtime Images Instances API
  slug: open-apptainer-instances-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apptainer/apptainer/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apptainer/apptainer/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apptainer/apptainer/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apptainer/apptainer/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apptainer/apptainer/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apptainer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apptainer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apptainer-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://apptainer.org/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/apptainer
created: '2026-03-16'
description: Apptainer, formerly Singularity, is a Linux Foundation project providing a high-performance container runtime optimized for high-performance computing and scientific workloads. It enables reproducible, portable scientific computing with support for existing Docker/OCI containers and integration with HPC schedulers.
examples:
- key_count: 8
  name: Container Image Example
  slug: container-image-example
finops:
- name: Apptainer Finops
  service_category: API
  slug: apptainer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apptainer.png
json_schemas:
- name: ContainerImage
  property_count: 8
  slug: container-image
json_structures:
- name: Container Image Structure
  property_count: 0
  slug: container-image-structure
jsonld:
- class_count: 12
  name: Apptainer Context
  property_count: 0
  slug: apptainer-context
layout: provider
modified: '2026-05-19'
name: Apptainer
nav: Providers
network: true
overview: 'Apptainer publishes 2 APIs on the [APIs.io](https://apis.io/) network: Images API and Instances API. Tagged areas include Containers, HPC, Scientific Computing, Open-Source, and Linux Foundation.


  The Apptainer catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apptainer''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Apptainer Plans Pricing
  plan_count: 3
  slug: apptainer-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Apptainer Rate Limits
  slug: apptainer-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apptainer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apptainer-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Apptainer API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 13
  slug: apptainer-spectral-rules
score:
  band: developing
  composite: 44.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 67.3
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apptainer/refs/heads/main/screenshots/apptainer-2026-06-20T172331.png
security:
- kind: authentication
  name: Apptainer Authentication
  slug: apptainer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apptainer Domain Security
  slug: apptainer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apptainer
tags:
- Containers
- HPC
- Scientific Computing
- Open-Source
- Linux Foundation
---
