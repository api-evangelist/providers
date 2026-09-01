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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST Assured is a Java DSL library for testing and validating RESTful APIs using a fluent, BDD-style syntax with given-when-then patterns. It supports HTTP methods, JSON/XML validation, authentication
  name: REST Assured
  slug: rest-assured
artifact_total: 12
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/rest-assured/rest-assured/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/rest-assured/rest-assured/blob/master/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/rest-assured/rest-assured/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rest-assured-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rest-assured.io
- group: docs
  title: ''
  type: Documentation
  url: https://rest-assured.io/#docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rest-assured
- group: operate
  title: ''
  type: Support
  url: http://groups.google.com/group/rest-assured
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/rest-assured/refs/heads/main/vocabulary/rest-assured-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/rest-assured/refs/heads/main/json-ld/rest-assured-context.jsonld
created: '2026-03-25'
description: REST Assured is a Java library for simplifying the testing and validation of RESTful APIs. It provides a fluent domain-specific language (DSL) built on the given-when-then BDD pattern, making it easy to write readable and maintainable API tests. REST Assured supports HTTP methods GET, POST, PUT, DELETE, OPTIONS, PATCH, and HEAD, along with JSON and XML response validation, JSONPath and XmlPath parsing, multiple authentication schemes, Spring MockMvc integration, and full request/response logging. Version 6.0.0 requires Java 17+ and integrates with Groovy 5, Spring 7, and Jackson 3. The library is distributed via Maven Central under the io.rest-assured group ID and is used by tens of thousands of development teams for API automation testing.
examples:
- key_count: 7
  name: Rest Assured Get User Example
  slug: rest-assured-get-user-example
- key_count: 7
  name: Rest Assured Post User Example
  slug: rest-assured-post-user-example
finops:
- name: Rest Assured Finops
  service_category: API
  slug: rest-assured-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rest-assured.png
json_schemas:
- name: REST Assured Request Specification
  property_count: 12
  slug: rest-assured-request
- name: REST Assured Response Specification
  property_count: 6
  slug: rest-assured-response
json_structures:
- name: Rest Assured Request Structure
  property_count: 0
  slug: rest-assured-request-structure
jsonld:
- class_count: 9
  name: Rest Assured Context
  property_count: 16
  slug: rest-assured-context
layout: provider
modified: '2026-05-02'
name: REST Assured
nav: Providers
network: true
overview: 'REST Assured publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Functional Testing, Testing, Java, API Testing, and Automation.


  The REST Assured catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  REST Assured''s developer surface includes documentation, support, and 8 more developer resources.'
plans:
- name: Rest Assured Plans Pricing
  plan_count: 3
  slug: rest-assured-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Rest Assured Rate Limits
  slug: rest-assured-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: REST Assured API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rest-assured-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 44.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 34.7
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 35.0
  previous_composite: 30.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rest-assured/refs/heads/main/screenshots/rest-assured-2026-06-20T192958.png
security:
- kind: domain-security
  name: Rest Assured Domain Security
  slug: rest-assured-domain-security
  summary_line: TLSv1.3
slug: rest-assured
tags:
- Functional Testing
- Testing
- Java
- API Testing
- Automation
website: https://rest-assured.io
---
