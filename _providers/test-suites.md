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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Test Suites Agentic Access
  operation_count: 7
  slug: test-suites-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- description: JUnit 5 is the Java testing framework used to organize test cases into test suites. The @Suite annotation enables test class grouping, tag-based filtering, and hierarchical suite composition, making i
  name: JUnit 5
  slug: junit-5
- description: pytest is the Python testing framework supporting test suite organization through test classes, directories, markers, and fixtures. Its plugin architecture enables test suite reporting, parallel execu
  name: pytest
  slug: pytest
- description: Jasmine is a behavior-driven JavaScript testing framework that organizes test cases into describe/it suite blocks. It is commonly used for organizing API client test suites in Node.js environments and
  name: Jasmine
  slug: jasmine
- description: Mocha is a flexible JavaScript test suite framework supporting both synchronous and asynchronous API tests. It provides describe/it nesting for suite organization, rich reporting, and integration with
  name: Mocha
  slug: mocha
- description: Jest is a zero-configuration JavaScript testing framework with built-in test suite runner, mocking, coverage reporting, and snapshot testing. Widely used for React applications and Node.js API service
  name: Jest
  slug: jest
- description: Bruno is an open-source API client and test suite manager that stores API collections as plain files alongside application code. It enables version- controlled test suites in a format designed for git
  name: Bruno
  slug: bruno
- description: 'Hurl is a command-line tool that runs HTTP requests defined in a simple plain-text format, enabling lightweight API test suites that can be committed to source control and executed in CI/CD pipelines '
  name: Hurl
  slug: hurl
- description: TestNG is a Java testing framework inspired by JUnit and NUnit that provides advanced test suite configuration including grouping, prioritization, parameterized tests, and parallel execution. It is wi
  name: TestNG
  slug: testng
- description: The Collections API from Test Suites — 2 operation(s) for collections.
  name: Test Suites Collections API
  slug: test-suites-collections-api
- description: The Workspaces API from Test Suites — 2 operation(s) for workspaces.
  name: Test Suites Workspaces API
  slug: test-suites-workspaces-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Postman API (Test Suites) Collections API
  slug: open-test-suites-collections-api
- collection_type: open
  name: Postman API (Test Suites) Collections Workspaces API
  slug: open-test-suites-workspaces-api
- collection_type: open
  name: Postman Collections API (Test Suites)
  slug: open-test-suites
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/test-suites-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/test-suites-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/test-suites-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/test-suites-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/test-suites-authentication.yml
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/api-evangelist/test-suites
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/test-suites/main/json-schema/test-suites-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/test-suites/main/json-structure/test-suites-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/test-suites/main/json-ld/test-suites-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/test-suites/main/vocabulary/test-suites-vocabulary.yml
created: '2025'
description: A collection of organized test cases designed to validate specific functionality or features of software applications and APIs. Test suites group related test cases into logical units that can be executed together, providing comprehensive coverage of a system's behavior. They are widely used by developers to build, maintain, and scale software testing across functional testing, regression testing, contract testing, and compliance validation. Test suites range from unit test collections in JUnit and pytest to API test collection suites in Postman, Bruno, and Karate.
examples:
- key_count: 12
  name: Test Suite Api Integration Example
  slug: test-suite-api-integration-example
finops:
- name: Test Suites Finops
  service_category: API
  slug: test-suites-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/test-suites.png
json_schemas:
- name: Test Suite
  property_count: 13
  slug: test-suites
json_structures:
- name: Test Suites Structure
  property_count: 0
  slug: test-suites-structure
jsonld:
- class_count: 14
  name: Test Suites Context
  property_count: 8
  slug: test-suites-context
layout: provider
modified: '2026-05-03'
name: Test Suites
nav: Providers
network: true
overview: 'Test Suites publishes 2 APIs on the [APIs.io](https://apis.io/) network: Collections API and Workspaces API. Tagged areas include API Testing, Collection, Quality Assurance, Software Development, and Test Management.


  The Test Suites catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Test Suites'' developer surface includes authentication and 9 more developer resources.'
plans:
- name: Test Suites Plans Pricing
  plan_count: 3
  slug: test-suites-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Test Suites Rate Limits
  slug: test-suites-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Test Suites API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: test-suites-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.6
  coverage:
    artifact_dirs: 15
    catalog_gap: 55.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 25.0
    contract_quality: 59.2
    developer_ergonomics: 21.4
    discoverability: 70.4
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/test-suites/refs/heads/main/screenshots/test-suites-2026-06-20T195156.png
security:
- kind: authentication
  name: Test Suites Authentication
  slug: test-suites-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Test Suites Domain Security
  slug: test-suites-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Test Suites Vulnerability Disclosure
  slug: test-suites-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Test Suites Trust Center
  slug: test-suites-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, HIPAA, GDPR, CSA STAR
slug: test-suites
tags:
- API Testing
- Collection
- Quality Assurance
- Software Development
- Test Management
- Testing
website: https://en.wikipedia.org/wiki/Test_suite
---
