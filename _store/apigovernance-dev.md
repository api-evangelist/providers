---
aid: apigovernance-dev
url: https://raw.githubusercontent.com/api-evangelist/apigovernance-dev/refs/heads/main/apis.yml
name: APIGovernance.Dev
description: APIGovernance.Dev is an AI-powered API governance platform that enforces API best practices through automated reviews trained on 10,000 public APIs. It provides the API Governance Top-10 list of best practices, automated CI/CD integration, and tools to help organizations deliver consistent, industry-standard APIs. Powered by PerfAI, Inc.
tags:
  - API Design
  - API Governance
  - Best Practices
  - Compliance
  - Guidelines
  - Standards
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-19'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: apigovernance-dev:apigovernance-dev
    name: APIGovernance.Dev
    tags:
      - API Governance
      - Best Practices
      - Compliance
    humanURL: https://apigovernance.dev/
    properties:
      - url: https://apigovernance.dev/
        type: Documentation
      - url: https://apigovernance.dev/pricing
        type: Pricing
      - url: json-schema/apigovernance-guideline-schema.json
        type: JSONSchema
      - url: json-schema/apigovernance-policy-schema.json
        type: JSONSchema
      - url: json-schema/apigovernance-review-schema.json
        type: JSONSchema
      - url: json-ld/apigovernance-context.jsonld
        type: JSON-LD
    description: APIGovernance.Dev provides automated API governance reviews using AI trained on 10,000 public APIs. It offers the API Governance Top-10 best practices list, CI/CD integration, and enterprise governance tools.
common:
  - url: https://apigovernance.dev/
    type: Website
  - url: https://apigovernance.dev/pricing
    type: Pricing
  - type: Features
    data:
      - name: AI-Powered API Reviews
        description: Automated API governance reviews trained on patterns from 10,000 public APIs.
      - name: API Governance Top-10
        description: Curated list of the top 10 API governance best practices across security, design, and documentation.
      - name: CI/CD Integration
        description: GitHub Actions and CI/CD pipeline integration for automated governance checks.
      - name: API Gateway Integration
        description: Integration with popular API gateways for runtime governance enforcement.
      - name: Issue Tracking Integration
        description: Jira and GitHub Issues integration for governance violation tracking.
  - type: UseCases
    data:
      - name: Automated API Review
        description: Automatically review API specifications against governance guidelines before release.
      - name: Team Standards Enforcement
        description: Enforce consistent API standards across multiple development teams.
      - name: API Design Guidance
        description: Provide developers with actionable best practice guidance during API design.
      - name: Compliance Auditing
        description: Audit existing APIs for compliance with organizational governance policies.
  - type: Integrations
    data:
      - name: GitHub Actions
        description: CI/CD integration for automated governance checks on API specification changes.
      - name: Jira
        description: Create Jira issues for governance violations found during reviews.
      - name: GitHub Issues
        description: Create GitHub issues for governance violations.
      - name: API Gateways
        description: Integration with API gateway platforms for runtime policy enforcement.
  - type: Solutions
    data:
      - name: Free Plan
        description: Basic API governance reviews with the API Governance Top-10 checks.
      - name: Growth Plan
        description: $199/month with advanced governance automation and CI/CD integration.
      - name: Enterprise Plan
        description: Custom pricing with full governance suite, SSO, and dedicated support.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
