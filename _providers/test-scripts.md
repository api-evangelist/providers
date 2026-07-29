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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Test Scripts Agentic Access
  operation_count: 7
  slug: test-scripts-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 11
apis:
- description: Newman is the command-line companion for Postman, enabling Postman collections and test scripts to be run directly from the terminal or integrated into CI/CD pipelines such as GitHub Actions, Jenkins,
  name: Newman CLI
  slug: newman-cli
- description: Karate is an open-source framework that combines API test automation, mocks, performance testing, and UI automation into a single framework. Test scripts are written in plain-text Gherkin syntax, maki
  name: Karate API Testing Framework
  slug: karate-api-testing-framework
- description: REST Assured is a Java-based DSL for simplifying testing of REST services. It integrates with JUnit and TestNG, and supports BDD-style test scripting with a fluent API for validating HTTP responses, h
  name: REST Assured
  slug: rest-assured
- description: 'Dredd is an open-source language-agnostic command-line tool for validating API documentation written in OpenAPI or API Blueprint against its backend implementation. It reads test scripts derived from '
  name: Dredd API Testing Framework
  slug: dredd-api-testing-framework
- description: Playwright is a cross-browser end-to-end testing framework from Microsoft that supports writing test scripts in JavaScript, TypeScript, Python, Java, and .NET. It is widely used for API testing, brows
  name: Playwright Test
  slug: playwright-test
- description: Schemathesis is a property-based testing tool for web APIs. It reads OpenAPI or GraphQL schemas and automatically generates test scripts to discover edge cases, crashes, and specification violations t
  name: Schemathesis
  slug: schemathesis
- description: The Collections API from Test Scripts — 2 operation(s) for collections.
  name: Test Scripts Collections API
  slug: test-scripts-collections-api
- description: The Environments API from Test Scripts — 1 operation(s) for environments.
  name: Test Scripts Environments API
  slug: test-scripts-environments-api
- description: The Mocks API from Test Scripts — 1 operation(s) for mocks.
  name: Test Scripts Mocks API
  slug: test-scripts-mocks-api
- description: The Monitors API from Test Scripts — 1 operation(s) for monitors.
  name: Test Scripts Monitors API
  slug: test-scripts-monitors-api
- description: 'Cypress is a JavaScript end-to-end testing framework designed for modern web applications. Its test scripting API supports both API testing and browser automation, with real-time test runner feedback '
  name: Cypress
  slug: cypress
artifact_total: 27
collections:
- collection_type: open
  name: Postman API (Test Scripts)
  slug: open-test-scripts
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/test-scripts-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/test-scripts-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/test-scripts-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/test-scripts-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/test-scripts-authentication.yml
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/api-evangelist/test-scripts
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/test-scripts/main/json-schema/test-scripts-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/test-scripts/main/json-structure/test-scripts-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/test-scripts/main/json-ld/test-scripts-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/test-scripts/main/vocabulary/test-scripts-vocabulary.yml
created: '2025'
description: Automated scripts used to verify software functionality, validate code behavior, and ensure quality through repeatable testing procedures. Test scripts encode testing logic in executable form, enabling continuous integration pipelines to run validation automatically on every code change. They support unit testing, integration testing, end-to-end testing, contract testing, performance testing, and security scanning across REST, GraphQL, SOAP, and gRPC APIs.
examples:
- key_count: 13
  name: Test Script Api Contract Example
  slug: test-script-api-contract-example
- key_count: 13
  name: Test Script Performance Example
  slug: test-script-performance-example
finops:
- name: Test Scripts Finops
  service_category: API
  slug: test-scripts-finops
graphqls:
- description: ''
  name: Test Scripts GraphQL API
  slug: test-scripts-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/test-scripts.png
json_schemas:
- name: Test Script
  property_count: 13
  slug: test-scripts
json_structures:
- name: Test Scripts Structure
  property_count: 0
  slug: test-scripts-structure
jsonld:
- class_count: 22
  name: Test Scripts Context
  property_count: 9
  slug: test-scripts-context
layout: provider
modified: '2026-07-25'
name: Test Scripts
nav: Providers
network: true
overview: 'Test Scripts publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Environments API, Mocks API, and 1 more. Tagged areas include Automation, CI/CD, Contract Testing, Quality Assurance, and Software Development.


  The Test Scripts catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Test Scripts'' developer surface includes authentication and 9 more developer resources.'
plans:
- name: Test Scripts Plans Pricing
  plan_count: 3
  slug: test-scripts-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Test Scripts Rate Limits
  slug: test-scripts-rate-limits
rules:
- name: Test Scripts API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: test-scripts-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.3
  delta: -3.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 60.2
    developer_ergonomics: 10.9
    discoverability: 75.9
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/test-scripts/refs/heads/main/screenshots/test-scripts-2026-06-20T195157.png
security:
- kind: authentication
  name: Test Scripts Authentication
  slug: test-scripts-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Test Scripts Domain Security
  slug: test-scripts-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Test Scripts Vulnerability Disclosure
  slug: test-scripts-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Test Scripts Trust Center
  slug: test-scripts-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, HIPAA, GDPR, CSA STAR
slug: test-scripts
tags:
- Automation
- CI/CD
- Contract Testing
- Quality Assurance
- Software Development
- Testing
website: https://en.wikipedia.org/wiki/Test_automation
---
