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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Apinity API enables organizations to manage their compliant API marketplace programmatically, including API registration, discovery, subscription management, and governance policy enforcement acro
  name: Apinity.io API
  slug: apinity-io
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apinity-io-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apinity-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apinity
- group: company
  title: ''
  type: Website
  url: https://apinity.io/
created: '2025-01-08'
description: Apinity empowers organisations to run their compliant API marketplace that simplifies integration, drives adoption, and secures governance. The platform provides tools for managing API lifecycle, enabling API discovery, enforcing compliance policies, and facilitating secure API-driven integrations across partner ecosystems.
examples:
- key_count: 9
  name: Apinity Marketplace Example
  slug: apinity-marketplace-example
features:
- description: Run a branded API marketplace that meets regulatory and compliance requirements for API sharing.
  name: Compliant API Marketplace
- description: Enable partners and teams to discover available APIs through a governed marketplace catalog.
  name: API Discovery
- description: Enforce governance policies across the API lifecycle from design through deprecation.
  name: API Governance
- description: Simplify partner integrations through standardized API access, documentation, and subscription management.
  name: Integration Simplification
- description: Track API adoption metrics and usage across marketplace subscribers.
  name: Adoption Tracking
finops:
- name: Apinity Io Finops
  service_category: API
  slug: apinity-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apinity-io.png
json_schemas:
- name: Apinity Marketplace API
  property_count: 9
  slug: apinity-marketplace
json_structures:
- name: Apinity Marketplace Structure
  property_count: 9
  slug: apinity-marketplace-structure
jsonld:
- class_count: 9
  name: Apinity Context
  property_count: 1
  slug: apinity-context
layout: provider
modified: '2026-04-19'
name: Apinity.io
nav: Providers
network: true
overview: 'Apinity.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Governance, API Marketplace, Compliance, Discovery, and Integration Platform.


  The Apinity.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Apinity Io Plans Pricing
  plan_count: 3
  slug: apinity-io-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 5
  name: Apinity Io Rate Limits
  slug: apinity-io-rate-limits
rules:
- name: Apinity.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apinity-io-jsonschema-spectral-rules
score:
  band: emerging
  composite: 24.4
  delta: -7.8
  facets:
    commercial_clarity: 15.8
    contract_quality: 22.6
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 32.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/screenshots/apinity-io-2026-06-20T172250.png
security:
- kind: domain-security
  name: Apinity Io Domain Security
  slug: apinity-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apinity-io
solutions:
- description: Full-featured compliant API marketplace for partner and customer-facing API distribution.
  name: API Marketplace
- description: Enterprise-grade API governance and compliance tooling for regulated industries.
  name: Enterprise Governance
tags:
- API Governance
- API Marketplace
- Compliance
- Discovery
- Integration Platform
use_cases:
- description: Build and manage a governed API marketplace for sharing APIs with external partners and customers.
  name: Partner API Ecosystem
- description: Ensure API access and usage complies with regulatory requirements through policy enforcement.
  name: Regulatory Compliance
- description: Provide an internal marketplace for discovering and subscribing to internal APIs across teams.
  name: Internal API Catalog
- description: Monetize APIs through marketplace subscriptions and usage-based billing.
  name: API Monetization
website: https://apinity.io/
---
