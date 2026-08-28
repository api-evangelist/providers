---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Kustomer Agentic Access
  operation_count: 2
  slug: kustomer-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 2
apis:
- description: Conversation threads with customers
  name: Kustomer Conversations API
  slug: kustomer-conversations-api
- description: Customer records in Kustomer
  name: Kustomer Customers API
  slug: kustomer-customers-api
artifact_total: 15
asyncapis:
- description: Kustomer's outbound webhook surface delivers event notifications when resources in a Kustomer organization are created or updated. Apps subscribe to a configured array of event names in their app defi
  name: Kustomer Outbound Webhook Events
  slug: kustomer-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kustomer REST Conversations API
  slug: open-kustomer-conversations-api
- collection_type: open
  name: Kustomer REST Conversations Customers API
  slug: open-kustomer-customers-api
- collection_type: open
  name: Kustomer REST API
  slug: open-kustomer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kustomer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kustomer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kustomer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kustomer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kustomer
- group: company
  title: ''
  type: Website
  url: https://www.kustomer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kustomer.com/kustomer-api-docs/reference
- group: commercial
  title: ''
  type: Plans
  url: plans/kustomer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kustomer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kustomer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.kustomer.com/resources/blog/
created: '2026-05-08'
description: Kustomer is an AI-powered customer service CRM that unifies conversations, customer data, automation, and reporting across channels.
finops:
- name: Kustomer Finops
  service_category: Customer Support
  slug: kustomer-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Kustomer AI-native CRM and customer service platform. Kustomer exposes a REST API at `https://api.kustomerapp.com` but this schema capture
  name: Kustomer GraphQL Schema
  slug: kustomer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kustomer.png
layout: provider
modified: '2026-05-30'
name: Kustomer
nav: Providers
network: true
overview: 'Kustomer publishes 2 APIs on the [APIs.io](https://apis.io/) network: Conversations API and Customers API. Tagged areas include Customer Service, CRM, Help Desk, Messaging, and Artificial Intelligence.


  The Kustomer catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Kustomer''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Kustomer Plans Pricing
  plan_count: 1
  slug: kustomer-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Kustomer Rate Limits
  slug: kustomer-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Kustomer API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: kustomer-asyncapi-spectral-rules
score:
  band: thin
  composite: 31.2
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 69.3
    developer_ergonomics: 13.1
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 31.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kustomer/refs/heads/main/screenshots/kustomer-2026-06-20T184221.png
security:
- kind: authentication
  name: Kustomer Authentication
  slug: kustomer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kustomer Domain Security
  slug: kustomer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kustomer
tags:
- Customer Service
- CRM
- Help Desk
- Messaging
- Artificial Intelligence
website: https://www.kustomer.com/
---
