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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Snyk Container Agentic Access
  operation_count: 10
  slug: snyk-container-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.snyk.io/rest
  baseurl_source: spec
  description: Manage Snyk Container scanning projects
  name: Snyk Container Container Projects API
  slug: snyk-container-container-projects-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: spec
  description: Retrieve container vulnerability issues
  name: Snyk Container Issues API
  slug: snyk-container-issues-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: spec
  description: Manage scan targets (images, registries)
  name: Snyk Container Targets API
  slug: snyk-container-targets-api
artifact_total: 27
collections:
- collection_type: postman
  name: Snyk Container Container Projects API
  slug: postman-snyk-container-container-projects-api
- collection_type: postman
  name: Snyk Container Container Projects Issues API
  slug: postman-snyk-container-issues-api
- collection_type: postman
  name: Snyk Container Container Projects Targets API
  slug: postman-snyk-container-targets-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Snyk Container Container Projects API
  slug: open-snyk-container-container-projects-api
- collection_type: open
  name: Snyk Container Container Projects Issues API
  slug: open-snyk-container-issues-api
- collection_type: open
  name: Snyk Container Container Projects Targets API
  slug: open-snyk-container-targets-api
- collection_type: open
  name: Snyk Container API
  slug: open-snyk-container
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/snyk-container/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/snyk-container-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/snyk-container-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/snyk-container-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/snyk-container-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/snyk-container-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://snyk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snyk.io/scan-using-snyk/snyk-container
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snyk.io/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snyk
- group: company
  title: ''
  type: Blog
  url: https://snyk.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://snyk.io/plans/
- group: start
  title: ''
  type: Signup
  url: https://app.snyk.io/signup
- group: other
  title: ''
  type: REST API
  url: https://apidocs.snyk.io/
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.snyk.io/snyk-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.snyk.io/snyk-api/changelog
- group: build
  title: ''
  type: SDKs
  url: https://github.com/snyk/snyk-sdk-java
- group: build
  title: ''
  type: CLI
  url: https://github.com/snyk/cli
- group: other
  title: ''
  type: Kubernetes Operator
  url: https://github.com/snyk/kubernetes-monitor
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/snyk-container-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/snyk-container-list-projects-example.json
- group: build
  title: ''
  type: Examples
  url: examples/snyk-container-list-issues-example.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.snyk.io/llms.txt
created: '2026-03-26'
description: Snyk Container helps developers find and fix vulnerabilities in container images and Kubernetes workloads. It integrates into existing development workflows to provide continuous security monitoring throughout the container lifecycle, scanning Docker images, Kubernetes manifests, and Helm charts for known CVEs and misconfigurations.
examples:
- key_count: 4
  name: Snyk Container List Issues Example
  slug: snyk-container-list-issues-example
- key_count: 4
  name: Snyk Container List Projects Example
  slug: snyk-container-list-projects-example
finops:
- name: Snyk Container Finops
  service_category: API
  slug: snyk-container-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snyk-container.png
json_schemas:
- name: Snyk Container Issue
  property_count: 3
  slug: snyk-container-issue
- name: Snyk Container Project
  property_count: 3
  slug: snyk-container-project
json_structures:
- name: Snyk Container Project Structure
  property_count: 0
  slug: snyk-container-project-structure
jsonld:
- class_count: 26
  name: Snyk Container Context
  property_count: 2
  slug: snyk-container-context
layout: provider
modified: '2026-05-19'
name: Snyk Container
nav: Providers
network: true
overview: 'Snyk Container publishes 3 APIs on the [APIs.io](https://apis.io/) network: Container Projects API, Issues API, and Targets API. Tagged areas include Container Images, Containers, Kubernetes, Security, and Vulnerability Management.


  The Snyk Container catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Snyk Container''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, signup flow, changelog, and 16 more developer resources.'
plans:
- name: Snyk Container Plans Pricing
  plan_count: 3
  slug: snyk-container-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Snyk Container Rate Limits
  slug: snyk-container-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Snyk Container API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: snyk-container-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Snyk Container API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 3
  slug: snyk-container-rules
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 18
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 71.2
    developer_ergonomics: 61.9
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 53.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/snyk-container/refs/heads/main/screenshots/snyk-container-2026-06-20T194116.png
security:
- kind: authentication
  name: Snyk Container Authentication
  slug: snyk-container-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Snyk Container Domain Security
  slug: snyk-container-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snyk Container Vulnerability Disclosure
  slug: snyk-container-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Snyk Container Trust Center
  slug: snyk-container-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: snyk-container
tags:
- Container Images
- Containers
- Kubernetes
- Security
- Vulnerability Management
- DevSecOps
- Open-Source
website: https://snyk.io/
---
