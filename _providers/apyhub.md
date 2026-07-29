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
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Apyhub Agentic Access
  operation_count: 5
  slug: apyhub-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 4
apis:
- description: Document conversion utilities
  name: ApyHub Convert API
  slug: apyhub-convert-api
- description: Currency conversion utilities
  name: ApyHub Currency API
  slug: apyhub-currency-api
- description: Data extraction utilities
  name: ApyHub Extract API
  slug: apyhub-extract-api
- description: Document generation utilities
  name: ApyHub Generate API
  slug: apyhub-generate-api
artifact_total: 16
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apyhub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apyhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apyhub-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apyhub
- group: company
  title: ''
  type: Website
  url: https://apyhub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://apyhub.com/docs
- group: company
  title: ''
  type: Blog
  url: https://apyhub.com/blog
- group: start
  title: ''
  type: Signup
  url: https://apyhub.com/register
- group: start
  title: ''
  type: Login
  url: https://apyhub.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apyhub
- group: agent
  title: ''
  type: LlmsText
  url: https://apyhub.com/llms.txt
created: '2025-01-08'
description: ApyHub is an API platform that provides a collection of utility APIs for common development tasks such as document conversion, data processing, image manipulation, currency exchange, and more. It simplifies API development by offering pre-built, ready-to-use API utilities that developers can integrate into their applications quickly.
examples:
- key_count: 7
  name: Conversion Request Example
  slug: conversion-request-example
finops:
- name: Apyhub Finops
  service_category: API
  slug: apyhub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apyhub.png
json_schemas:
- name: ConversionRequest
  property_count: 7
  slug: conversion-request
json_structures:
- name: Conversion Request Structure
  property_count: 0
  slug: conversion-request-structure
jsonld:
- class_count: 12
  name: Apyhub Context
  property_count: 0
  slug: apyhub-context
layout: provider
modified: '2026-04-19'
name: ApyHub
nav: Providers
network: true
overview: 'ApyHub publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Convert API, Currency API, Extract API, and 1 more. Tagged areas include API Platform, Data Processing, Document Conversion, and Utility APIs.


  The ApyHub catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  ApyHub''s developer surface includes authentication, documentation, engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Apyhub Plans Pricing
  plan_count: 3
  slug: apyhub-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Apyhub Rate Limits
  slug: apyhub-rate-limits
rules:
- name: ApyHub API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: apyhub-jsonschema-spectral-rules
- name: ApyHub API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 13
  slug: apyhub-spectral-rules
score:
  band: developing
  composite: 51.1
  delta: -3.5
  facets:
    commercial_clarity: 52.6
    contract_quality: 75.4
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.6
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
screenshot: https://raw.githubusercontent.com/api-evangelist/apyhub/refs/heads/main/screenshots/apyhub-2026-06-20T172345.png
security:
- kind: authentication
  name: Apyhub Authentication
  slug: apyhub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Apyhub Domain Security
  slug: apyhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apyhub
tags:
- API Platform
- Data Processing
- Document Conversion
- Utility APIs
website: https://apyhub.com/
---
