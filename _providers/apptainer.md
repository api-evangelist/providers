---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
