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
api_count: 1
apis:
- description: Schemathesis is a property-based API testing tool that automatically generates test cases from OpenAPI and GraphQL schemas to find bugs and spec violations. It detects server crashes, schema violation
  name: Schemathesis
  slug: schemathesis
artifact_total: 11
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/schemathesis/schemathesis/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/schemathesis/schemathesis/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/schemathesis/schemathesis/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/schemathesis/schemathesis/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/schemathesis/schemathesis/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/schemathesis-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/schemathesis-io
- group: company
  title: ''
  type: Website
  url: https://schemathesis.io
- group: docs
  title: ''
  type: Documentation
  url: https://schemathesis.readthedocs.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/schemathesis
- group: build
  title: ''
  type: PyPI Package
  url: https://pypi.org/project/schemathesis/
- group: other
  title: ''
  type: Docker Image
  url: https://hub.docker.com/r/schemathesis/schemathesis
- group: company
  title: ''
  type: Blog
  url: https://schemathesis.io/blog
- group: other
  title: ''
  type: Research
  url: https://dl.acm.org/doi/10.1145/3510003.3510097
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/vocabulary/schemathesis-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/examples/schemathesis-cli-test-example.json
created: '2026-03-25'
description: Schemathesis is a property-based API testing tool that automatically generates test cases from OpenAPI and GraphQL schemas to find bugs and specification violations. It uses the Hypothesis property-based testing framework to generate diverse, edge-case-covering test inputs from schema constraints, detecting server crashes, response schema violations, validation bypasses, and stateful bugs in multi-step workflows. Used by Netflix, SAP, Red Hat, IBM, and JetBrains.
examples:
- key_count: 7
  name: Schemathesis Cli Test Example
  slug: schemathesis-cli-test-example
finops:
- name: Schemathesis Finops
  service_category: API
  slug: schemathesis-finops
graphqls:
- description: Schemathesis is a property-based API testing tool that automatically generates test cases from OpenAPI and GraphQL schemas to find bugs and spec violations. It detects server crashes, schema violation
  name: Schemathesis GraphQL API
  slug: schemathesis-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/schemathesis.png
json_schemas:
- name: Schemathesis Configuration
  property_count: 14
  slug: schemathesis-config
json_structures:
- name: Schemathesis Config Structure
  property_count: 0
  slug: schemathesis-config-structure
jsonld:
- class_count: 23
  name: Schemathesis Context
  property_count: 2
  slug: schemathesis-context
layout: provider
modified: '2026-05-02'
name: Schemathesis
nav: Providers
network: true
overview: 'Schemathesis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, Contract Testing, Developer Tools, Fuzzing, and OpenAPI.


  The Schemathesis catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Schemathesis'' developer surface includes documentation, engineering blog, code examples, and 13 more developer resources.'
plans:
- name: Schemathesis Plans Pricing
  plan_count: 3
  slug: schemathesis-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Schemathesis Rate Limits
  slug: schemathesis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Schemathesis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: schemathesis-jsonschema-spectral-rules
screenshot: https://raw.githubusercontent.com/api-evangelist/schemathesis/refs/heads/main/screenshots/schemathesis-2026-06-20T193520.png
security:
- kind: domain-security
  name: Schemathesis Domain Security
  slug: schemathesis-domain-security
  summary_line: TLSv1.3 · DMARC
slug: schemathesis
tags:
- API Testing
- Contract Testing
- Developer Tools
- Fuzzing
- OpenAPI
- Property-Based Testing
- Schemathesis
website: https://schemathesis.io
---
