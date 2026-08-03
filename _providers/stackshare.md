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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 12.2
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'The StackShare GraphQL API provides programmatic access to StackShare''s database of developer tools and company tech stacks. It exposes four primary capability areas: Leads (find companies using speci'
  name: StackShare GraphQL API
  slug: stackshare-graphql-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackshare-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackshare
- group: company
  title: ''
  type: Website
  url: https://stackshare.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackshare.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackshare.io/reference/getting-started
- group: start
  title: ''
  type: Signup
  url: https://stackshare.io/api
- group: commercial
  title: ''
  type: Pricing
  url: https://stackshare.io/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://stackshare.io/enterprise
- group: auth
  title: ''
  type: Authentication
  url: https://docs.stackshare.io/reference/authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackshare.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stackshare.io/privacy
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@stackshareio
- group: other
  title: ''
  type: X
  url: https://twitter.com/stackshare
- group: build
  title: ''
  type: GitHub
  url: https://github.com/stackshare
created: '2026-03-24'
description: StackShare is a platform where developers and companies share information about the technologies and tools they use to build software. The StackShare GraphQL API provides programmatic access to StackShare's database of developer tools and company tech stacks, exposing Leads (find companies using specific tools), Enrichment (retrieve the full tech stack for a domain), Tools (query metadata about technologies), and Search capabilities.
examples:
- key_count: 4
  name: Stackshare Enrichment Example
  slug: stackshare-enrichment-example
finops:
- name: Stackshare Finops
  service_category: API
  slug: stackshare-finops
graphqls:
- description: 'The StackShare GraphQL API provides programmatic access to StackShare''s database of developer tools and company tech stacks. It exposes four primary capability areas: Leads (find companies using speci'
  name: StackShare GraphQL API
  slug: stackshare-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackshare.png
json_schemas:
- name: StackShare Company
  property_count: 4
  slug: stackshare-company
- name: StackShare Tool
  property_count: 8
  slug: stackshare-tool
json_structures:
- name: Stackshare Tool Structure
  property_count: 0
  slug: stackshare-tool-structure
jsonld:
- class_count: 11
  name: Stackshare Context
  property_count: 2
  slug: stackshare-context
layout: provider
modified: '2026-05-02'
name: StackShare
nav: Providers
network: true
overview: 'StackShare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Software Discovery, and Tech Stacks.


  The StackShare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  StackShare''s developer surface includes documentation, getting-started guide, signup flow, pricing, authentication, engineering blog, GitHub presence, and 7 more developer resources.'
plans:
- name: Stackshare Plans Pricing
  plan_count: 3
  slug: stackshare-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Stackshare Rate Limits
  slug: stackshare-rate-limits
rules:
- name: StackShare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: stackshare-jsonschema-spectral-rules
score:
  band: thin
  composite: 41.7
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 12.9
    developer_ergonomics: 32.6
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 41.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Stackshare Domain Security
  slug: stackshare-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stackshare
tags:
- Developer Tools
- Software Discovery
- Tech Stacks
website: https://stackshare.io/
---
