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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: APIGovernance.Dev provides automated API governance reviews using AI trained on 10,000 public APIs. It offers the API Governance Top-10 best practices list, CI/CD integration, and enterprise governanc
  name: APIGovernance.Dev
  slug: apigovernance-dev
artifact_total: 32
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apigovernance-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apigovernance.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://apigovernance.dev/pricing
created: '2025-01-08'
description: APIGovernance.Dev is an AI-powered API governance platform that enforces API best practices through automated reviews trained on 10,000 public APIs. It provides the API Governance Top-10 list of best practices, automated CI/CD integration, and tools to help organizations deliver consistent, industry-standard APIs. Powered by PerfAI, Inc.
examples:
- key_count: 6
  name: Apigovernance Guideline Example
  slug: apigovernance-guideline-example
- key_count: 5
  name: Apigovernance Policy Example
  slug: apigovernance-policy-example
- key_count: 6
  name: Apigovernance Review Example
  slug: apigovernance-review-example
features:
- description: Automated API governance reviews trained on patterns from 10,000 public APIs.
  name: AI-Powered API Reviews
- description: Curated list of the top 10 API governance best practices across security, design, and documentation.
  name: API Governance Top-10
- description: GitHub Actions and CI/CD pipeline integration for automated governance checks.
  name: CI/CD Integration
- description: Integration with popular API gateways for runtime governance enforcement.
  name: API Gateway Integration
- description: Jira and GitHub Issues integration for governance violation tracking.
  name: Issue Tracking Integration
finops:
- name: Apigovernance Dev Finops
  service_category: API
  slug: apigovernance-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apigovernance-dev.png
integrations:
- description: CI/CD integration for automated governance checks on API specification changes.
  name: GitHub Actions
- description: Create Jira issues for governance violations found during reviews.
  name: Jira
- description: Create GitHub issues for governance violations.
  name: GitHub Issues
- description: Integration with API gateway platforms for runtime policy enforcement.
  name: API Gateways
json_schemas:
- name: Guideline
  property_count: 6
  slug: apigovernance-guideline
- name: Policy
  property_count: 5
  slug: apigovernance-policy
- name: Review
  property_count: 6
  slug: apigovernance-review
json_structures:
- name: Apigovernance Guideline Structure
  property_count: 6
  slug: apigovernance-guideline-structure
- name: Apigovernance Policy Structure
  property_count: 5
  slug: apigovernance-policy-structure
- name: Apigovernance Review Structure
  property_count: 6
  slug: apigovernance-review-structure
jsonld:
- class_count: 5
  name: Apigovernance Context
  property_count: 7
  slug: apigovernance-context
layout: provider
modified: '2026-04-19'
name: APIGovernance.Dev
nav: Providers
network: true
overview: 'APIGovernance.Dev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Design, API Governance, Best Practices, Compliance, and Guidelines.


  The APIGovernance.Dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIGovernance.Dev''s developer surface includes pricing and 2 more developer resources.'
plans:
- name: Apigovernance Dev Plans Pricing
  plan_count: 3
  slug: apigovernance-dev-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 5
  name: Apigovernance Dev Rate Limits
  slug: apigovernance-dev-rate-limits
rules:
- name: APIGovernance.Dev API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apigovernance-dev-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 34.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 39.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apigovernance-dev/refs/heads/main/screenshots/apigovernance-dev-2026-06-20T172239.png
security:
- kind: domain-security
  name: Apigovernance Dev Domain Security
  slug: apigovernance-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apigovernance-dev
solutions:
- description: Basic API governance reviews with the API Governance Top-10 checks.
  name: Free Plan
- description: $199/month with advanced governance automation and CI/CD integration.
  name: Growth Plan
- description: Custom pricing with full governance suite, SSO, and dedicated support.
  name: Enterprise Plan
tags:
- API Design
- API Governance
- Best Practices
- Compliance
- Guidelines
- Standards
use_cases:
- description: Automatically review API specifications against governance guidelines before release.
  name: Automated API Review
- description: Enforce consistent API standards across multiple development teams.
  name: Team Standards Enforcement
- description: Provide developers with actionable best practice guidance during API design.
  name: API Design Guidance
- description: Audit existing APIs for compliance with organizational governance policies.
  name: Compliance Auditing
website: https://apigovernance.dev/
---
