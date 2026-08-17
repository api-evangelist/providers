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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 8
apis:
- description: Redocly Realm is the comprehensive API lifecycle management platform that unifies Redoc, Revel, and Reef into a single integrated product. Realm includes API documentation, mock servers, linting, cata
  name: Redocly Realm
  slug: redocly-realm
- description: Redocly Reunite is the Git-connected collaboration and deployment surface for Realm. It prepares, deploys, and hosts documentation projects and mock servers and ships a content editor, pull requests a
  name: Redocly Reunite
  slug: redocly-reunite
- description: Redocly Revel is the external developer hub product. It renders Markdown, Markdoc, and React pages with multi-product and localization capabilities, enabling organizations to create polished developer
  name: Redocly Revel
  slug: redocly-revel
- description: 'Redocly Reef is the internal API platform — a service catalog and governance product that organizes, aids discovery, and monitors APIs throughout their lifecycle. Reef includes Catalog for organizing '
  name: Redocly Reef
  slug: redocly-reef
- description: 'Redoc is the open-source engine that renders API reference documentation from OpenAPI definitions with a three-panel layout known for clarity and usability. Supports OpenAPI 3.2, 3.1, 3.0 and OpenAPI '
  name: Redocly Redoc
  slug: redocly-redoc
- description: Redocly CLI is an open-source command-line tool for working with OpenAPI descriptions, developer portals, and other API lifecycle operations. Supports linting, validation, bundling, splitting, and dec
  name: Redocly CLI
  slug: redocly-cli
- description: Respect Monitoring is Redocly's continuous, API-aware monitoring product powered by OpenAPI Arazzo workflows. Rather than uptime checking, it validates that API responses conform to specifications — e
  name: Redocly Respect Monitoring
  slug: redocly-respect
- description: Arazzo is the OpenAPI Initiative's specification for describing multi-step API workflows; Redocly is a primary tooling vendor with first-class Arazzo support across Redocly CLI (lint, validate, genera
  name: Arazzo Specification (Redocly Tooling)
  slug: redocly-arazzo
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/redocly-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://redocly.com/docs
- group: other
  title: ''
  type: Customers
  url: https://redocly.com/customers
- group: commercial
  title: ''
  type: Pricing
  url: https://redocly.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://redocly.com/blog
- group: learn
  title: ''
  type: Webinars
  url: https://redocly.com/webinars
- group: auth
  title: ''
  type: Security
  url: https://redocly.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redocly.com/
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://redocly.com/sla
- group: build
  title: ''
  type: CLI
  url: https://redocly.com/redocly-cli
- group: company
  title: ''
  type: About
  url: https://redocly.com/about
- group: operate
  title: ''
  type: Support
  url: https://redocly.com/contact-us
- group: other
  title: ''
  type: Products
  url: https://redocly.com/products
- group: start
  title: ''
  type: Login
  url: https://auth.cloud.redocly.com/login
- group: start
  title: ''
  type: Signup
  url: https://redocly.com/billing/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redocly.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redocly.com/subscription-agreement
- group: company
  title: ''
  type: Careers
  url: https://redocly.com/careers
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Redocly
- group: other
  title: ''
  type: X
  url: https://twitter.com/Redocly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redocly
- group: other
  title: ''
  type: Governance
  url: https://redocly.com/api-governance
- group: operate
  title: ''
  type: ChangeLog
  url: https://redocly.com/docs/realm/changelog
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://redocly.com/vulnerability-disclosure-policy
- group: other
  title: ''
  type: DataProcessingAddendum
  url: https://redocly.com/dpa
- group: commercial
  title: ''
  type: Pricing
  url: https://redocly.com/startup-discount
- group: docs
  title: ''
  type: Reference
  url: https://redocly.com/reference
- group: commercial
  title: ''
  type: Plans
  url: plans/redocly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/redocly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/redocly-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://redocly.com/llms.txt
created: '2026-01-05'
description: Redocly is a company that specializes in API documentation and governance tooling. Their platform helps organizations create, manage, and publish API documentation through Realm (the integrated lifecycle platform that unifies Redoc, Revel, and Reef), Reunite (Git-connected collaboration and deployment for docs/APIs), Revel (developer portal), Reef (internal API catalog and scorecard), and Redoc (open-source OpenAPI renderer). The Redocly CLI provides linting, bundling, splitting, decoration, and documentation generation for OpenAPI, AsyncAPI, and Arazzo specifications. Respect Monitoring adds continuous, Arazzo-powered API monitoring, and the Enterprise tier exposes MCP Servers and AI search for Realm portals — positioning Redocly's catalog as an AI substrate for agentic software.
examples:
- key_count: 2
  name: Redocly Cli Commands Example
  slug: redocly-cli-commands-example
- key_count: 3
  name: Redocly Config Example
  slug: redocly-config-example
- key_count: 3
  name: Redocly Lint Result Example
  slug: redocly-lint-result-example
finops:
- name: Redocly Finops
  service_category: API
  slug: redocly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/redocly.png
json_schemas:
- name: Redocly Configuration
  property_count: 7
  slug: redocly-config
- name: Redocly Lint Result
  property_count: 3
  slug: redocly-lint-result
json_structures:
- name: Redocly Config Structure
  property_count: 0
  slug: redocly-config-structure
- name: Redocly Lint Result Structure
  property_count: 0
  slug: redocly-lint-result-structure
jsonld:
- class_count: 0
  name: Redocly Context
  property_count: 4
  slug: redocly-context
layout: provider
modified: '2026-05-22'
name: Redocly
nav: Providers
network: true
overview: 'Redocly publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, API Catalog, API Documentation, Arazzo, and Developer Portal.


  The Redocly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Redocly''s developer surface includes documentation, pricing, engineering blog, CLI, support, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Redocly Plans Pricing
  plan_count: 13
  slug: redocly-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 7
  name: Redocly Rate Limits
  slug: redocly-rate-limits
rules:
- name: Redocly API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: redocly-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 24.2
    developer_ergonomics: 28.3
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 55.3
  previous_composite: 45.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/redocly/refs/heads/main/screenshots/redocly-2026-06-20T192731.png
security:
- kind: domain-security
  name: Redocly Domain Security
  slug: redocly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: redocly
tags:
- AI
- API Catalog
- API Documentation
- Arazzo
- Developer Portal
- Governance
- Linting
- MCP
- Monitoring
- OpenAPI
---
