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
- acting_count: 23
  human_in_the_loop: 1
  name: Apigen Agentic Access
  operation_count: 39
  slug: apigen-agentic-access
  summary_line: 39 operations · 23 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: Configure connections to external data sources.
  name: APIGen Connectors API
  slug: apigen-connectors-api
- description: Deploy APIs to target environments.
  name: APIGen Deployments API
  slug: apigen-deployments-api
- description: Define and manage API endpoints.
  name: APIGen Endpoints API
  slug: apigen-endpoints-api
- description: Manage API generation projects.
  name: APIGen Projects API
  slug: apigen-projects-api
- description: Define data schemas for APIs.
  name: APIGen Schemas API
  slug: apigen-schemas-api
- description: Create and run automated API tests.
  name: APIGen Tests API
  slug: apigen-tests-api
- description: Manage API authentication tokens.
  name: APIGen Tokens API
  slug: apigen-tokens-api
- description: Manage user profiles.
  name: APIGen Users API
  slug: apigen-users-api
artifact_total: 42
collections:
- collection_type: open
  name: APIGen API
  slug: open-apigen-apigen
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apigen-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apigen-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apigen-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apigen
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ApiGen/ApiGen
- group: build
  title: ''
  type: SDKs
  url: https://packagist.org/packages/apigen/apigen
- group: other
  title: ''
  type: Docker
  url: https://hub.docker.com/r/apigen/apigen
created: '2025-01-08'
description: ApiGen is an open source PHP API documentation generator that automatically produces smart and simple documentation from PHP source code. It supports PHP 7.1+ including all PHP 8.3 features like enums, union types, readonly classes, and intersection types. ApiGen is maintained by the ApiGen GitHub organization and can be installed via Docker, Phar binary, or Composer.
examples:
- key_count: 4
  name: Apigen Api Example
  slug: apigen-api-example
- key_count: 5
  name: Apigen Deployment Example
  slug: apigen-deployment-example
- key_count: 5
  name: Apigen Endpoint Example
  slug: apigen-endpoint-example
- key_count: 4
  name: Apigen Project Example
  slug: apigen-project-example
features:
- description: Automatically generates API documentation from PHP source code with phpDoc support.
  name: PHP Documentation Generation
- description: Full support for PHP 7.1+ including typed properties, enums, union types, readonly classes, and PHP 8.3 features.
  name: Modern PHP Support
- description: Supports intersection types, disjunctive normal form types, constructor property promotion, and all PHPStan-supported types.
  name: Advanced Type Systems
- description: Available via Docker, Phar binary, or Composer for flexible integration into any PHP project workflow.
  name: Flexible Installation
- description: Uses Latte templating for customizable documentation output with built-in CommonMark support.
  name: Template-Based Output
finops:
- name: Apigen Finops
  service_category: API
  slug: apigen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apigen.png
integrations:
- description: Available as a Composer package for easy installation in PHP projects.
  name: Composer
- description: Official Docker image for containerized documentation generation.
  name: Docker
- description: Can be integrated into GitHub Actions workflows for automated documentation.
  name: GitHub Actions
- description: Built on phpstan/phpdoc-parser for comprehensive type system support.
  name: PHPStan
json_schemas:
- name: APIGen API
  property_count: 14
  slug: apigen-api
- name: APIGen Deployment
  property_count: 13
  slug: apigen-deployment
- name: APIGen Endpoint
  property_count: 13
  slug: apigen-endpoint
- name: APIGen Project
  property_count: 9
  slug: apigen-project
json_structures:
- name: Apigen Api Structure
  property_count: 14
  slug: apigen-api-structure
- name: Apigen Deployment Structure
  property_count: 13
  slug: apigen-deployment-structure
- name: Apigen Endpoint Structure
  property_count: 13
  slug: apigen-endpoint-structure
- name: Apigen Project Structure
  property_count: 9
  slug: apigen-project-structure
jsonld:
- class_count: 29
  name: Apigen Context
  property_count: 10
  slug: apigen-context
layout: provider
modified: '2026-05-19'
name: APIGen
nav: Providers
network: true
overview: 'APIGen publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Connectors API, Deployments API, Endpoints API, and 5 more. Tagged areas include Code, Documentation, Generation, Open Source, and PHP.


  The APIGen catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  APIGen''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Apigen Plans Pricing
  plan_count: 3
  slug: apigen-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 5
  name: Apigen Rate Limits
  slug: apigen-rate-limits
rules:
- name: APIGen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apigen-jsonschema-spectral-rules
- name: APIGen API Rules
  rule_count: 17
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 12
  slug: apigen-spectral-rules
score:
  band: developing
  composite: 50.5
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 79.7
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apigen/refs/heads/main/screenshots/apigen-2026-06-20T172236.png
security:
- kind: authentication
  name: Apigen Authentication
  slug: apigen-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Apigen Domain Security
  slug: apigen-domain-security
  summary_line: TLSv1.3
slug: apigen
tags:
- Code
- Documentation
- Generation
- Open Source
- PHP
use_cases:
- description: Generate comprehensive API reference documentation for PHP libraries and packages.
  name: PHP Library Documentation
- description: Automate API documentation generation as part of continuous integration workflows.
  name: CI/CD Documentation Pipeline
- description: Create and maintain documentation for open source PHP projects.
  name: Open Source Project Docs
---
