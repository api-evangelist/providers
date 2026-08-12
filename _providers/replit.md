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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Replit Agentic Access
  operation_count: 12
  slug: replit-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 3
apis:
- description: The Deployments API from Replit — 2 operation(s) for deployments.
  name: Replit Deployments API
  slug: replit-deployments-api
- description: The Repls API from Replit — 4 operation(s) for repls.
  name: Replit Repls API
  slug: replit-repls-api
- description: The Users API from Replit — 3 operation(s) for users.
  name: Replit Users API
  slug: replit-users-api
artifact_total: 20
collections:
- collection_type: postman
  name: Replit Deployments API
  slug: postman-replit-deployments-api
- collection_type: postman
  name: Replit Deployments Repls API
  slug: postman-replit-repls-api
- collection_type: postman
  name: Replit Deployments Users API
  slug: postman-replit-users-api
- collection_type: open
  name: Replit
  slug: open-replit
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/replit/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/replit-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/replit-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/replit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/replit-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/repl-it
- group: company
  title: ''
  type: Website
  url: https://replit.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.replit.com
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.replit.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://replit.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.replit.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://replit.com/site/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://replit.com/site/privacy
- group: start
  title: ''
  type: Signup
  url: https://replit.com/signup
- group: start
  title: ''
  type: Login
  url: https://replit.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/replit
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/replit/replit-py
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/replit
- group: operate
  title: ''
  type: StatusPage
  url: https://status.replit.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.replit.com/llms.txt
created: '2026-01-02'
description: Replit is a cloud-based development platform that lets you create, run, and deploy software directly from your browser. It provides instant, containerized environments for many programming languages, real-time multiplayer collaboration, an integrated editor and terminal, built-in package management, version control, and AI coding assistance. Use the Replit API to manage Repls, deployments, and users programmatically.
examples:
- key_count: 4
  name: Replit Create Repl Example
  slug: replit-create-repl-example
finops:
- name: Replit Finops
  service_category: API
  slug: replit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/replit.png
json_schemas:
- name: Replit Repl
  property_count: 10
  slug: replit-repl
json_structures:
- name: Replit Repl Structure
  property_count: 0
  slug: replit-repl-structure
jsonld:
- class_count: 1
  name: Replit Context
  property_count: 19
  slug: replit-context
layout: provider
modified: '2026-05-19'
name: Replit
nav: Providers
network: true
overview: 'Replit publishes 3 APIs on the [APIs.io](https://apis.io/) network: Deployments API, Repls API, and Users API. Tagged areas include Code, Compiling, Development Environment, Programming Languages, and Version Control.


  The Replit catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Replit''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Replit Plans Pricing
  plan_count: 3
  slug: replit-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Replit Rate Limits
  slug: replit-rate-limits
rules:
- name: Replit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: replit-jsonschema-spectral-rules
- name: Replit API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 5
  slug: replit-rules
score:
  band: strong
  composite: 57.5
  delta: -6.9
  facets:
    commercial_clarity: 68.4
    contract_quality: 68.7
    developer_ergonomics: 43.5
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 64.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/replit/refs/heads/main/screenshots/replit-2026-06-20T192905.png
security:
- kind: authentication
  name: Replit Authentication
  slug: replit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Replit Domain Security
  slug: replit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Replit Trust Center
  slug: replit-trust-center
  summary_line: SOC 2
slug: replit
tags:
- Code
- Compiling
- Development Environment
- Programming Languages
- Version Control
website: https://replit.com
---
