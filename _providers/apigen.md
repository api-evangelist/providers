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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
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
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: APIGen API
  slug: open-apigen-apigen
- collection_type: open
  name: APIGen Connectors API
  slug: open-apigen-connectors-api
- collection_type: open
  name: APIGen Connectors Deployments API
  slug: open-apigen-deployments-api
- collection_type: open
  name: APIGen Connectors Endpoints API
  slug: open-apigen-endpoints-api
- collection_type: open
  name: APIGen Connectors Projects API
  slug: open-apigen-projects-api
- collection_type: open
  name: APIGen Connectors Schemas API
  slug: open-apigen-schemas-api
- collection_type: open
  name: APIGen Connectors Tests API
  slug: open-apigen-tests-api
- collection_type: open
  name: APIGen Connectors Tokens API
  slug: open-apigen-tokens-api
- collection_type: open
  name: APIGen Connectors Users API
  slug: open-apigen-users-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ApiGen/ApiGen/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ApiGen/ApiGen/releases
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


  APIGen''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Apigen Plans Pricing
  plan_count: 3
  slug: apigen-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Apigen Rate Limits
  slug: apigen-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: APIGen API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apigen-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: APIGen API Rules
  rule_count: 17
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 12
  slug: apigen-spectral-rules
score:
  band: thin
  composite: 38.7
  delta: -5.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 77.4
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 28.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
