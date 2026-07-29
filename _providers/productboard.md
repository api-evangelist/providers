---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for managing features, components, products, notes (customer feedback), users, companies, objectives, releases, and webhooks within Productboard. Supports both v1 and v2 endpoints. Authentica
  name: Productboard Public API
  slug: public-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/productboard-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/productboard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/productboard-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/productboard
- group: company
  title: ''
  type: Website
  url: https://www.productboard.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.productboard.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.productboard.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.productboard.com/trial/
- group: operate
  title: ''
  type: Support
  url: https://support.productboard.com
- group: company
  title: ''
  type: Blog
  url: https://www.productboard.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.productboard.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/productboard/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.productboard.com/llms.txt
created: '2026-05-11'
description: Productboard is a product management platform that helps product teams capture user feedback, prioritize features, build product roadmaps, and align engineering, design, and go-to-market stakeholders around what to build next. The Productboard Public REST API (v1 and v2) provides programmatic access to features, components, products, notes, users, companies, objectives, releases, and webhooks at https://api.productboard.com, with authentication via a Public API Access token (Bearer) or OAuth2.
graphqls:
- description: This document describes a conceptual GraphQL schema for the Productboard product management platform. Productboard provides a Public REST API at https://api.productboard.com (v1 and v2), and this sche
  name: Productboard GraphQL Schema
  slug: productboard-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/productboard.png
layout: provider
modified: '2026-05-11'
name: Productboard
nav: Providers
network: true
overview: 'Productboard publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Product Management, Roadmapping, Customer Feedback, Prioritization, and Product Operations.


  Productboard''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 29.9
  delta: 11.2
  facets:
    commercial_clarity: 18.4
    contract_quality: 54.3
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 18.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/productboard/refs/heads/main/screenshots/productboard-2026-06-20T192139.png
security:
- kind: domain-security
  name: Productboard Domain Security
  slug: productboard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Productboard Vulnerability Disclosure
  slug: productboard-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Productboard Trust Center
  slug: productboard-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
slug: productboard
tags:
- Product Management
- Roadmapping
- Customer Feedback
- Prioritization
- Product Operations
website: https://www.productboard.com
---
