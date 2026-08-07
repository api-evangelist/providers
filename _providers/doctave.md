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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Doctave Agentic Access
  operation_count: 14
  slug: doctave-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 4
apis:
- description: Trigger and monitor documentation site deployments.
  name: Doctave Deployments API
  slug: doctave-deployments-api
- description: Create, read, update, and delete documentation pages.
  name: Doctave Pages API
  slug: doctave-pages-api
- description: Search across documentation site content.
  name: Doctave Search API
  slug: doctave-search-api
- description: Manage documentation sites and their configurations.
  name: Doctave Sites API
  slug: doctave-sites-api
artifact_total: 15
collections:
- collection_type: open
  name: Doctave API
  slug: open-doctave-doctave
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/doctave-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doctave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/doctave-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Doctave
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/doctave
- group: company
  title: ''
  type: Website
  url: https://www.doctave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.doctave.com/
- group: company
  title: ''
  type: Blog
  url: https://www.doctave.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doctave.com/pricing
created: '2025-01-08'
description: Doctave is a platform for building modern technical documentation sites. Bring your guides, your API references and SDK documentation, and build developer portals that make your product stand out. It supports a docs-as-code workflow powered by Markdown and OpenAPI, with Git-friendly version control, full-text search, and automated deployments.
finops:
- name: Doctave Finops
  service_category: API
  slug: doctave-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doctave.png
json_schemas:
- name: Doctave Deployment
  property_count: 13
  slug: doctave-deployment
- name: Doctave Site
  property_count: 12
  slug: doctave-site
jsonld:
- class_count: 33
  name: Doctave Context
  property_count: 3
  slug: doctave-context
layout: provider
modified: '2026-05-19'
name: Doctave
nav: Providers
network: true
overview: 'Doctave publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Deployments API, Pages API, Search API, and 1 more. Tagged areas include Documentation, OpenAPI, Platform, and Portals.


  The Doctave catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Doctave''s developer surface includes authentication, documentation, engineering blog, pricing, and 5 more developer resources.'
plans:
- name: Doctave Plans Pricing
  plan_count: 3
  slug: doctave-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 5
  name: Doctave Rate Limits
  slug: doctave-rate-limits
rules:
- name: Doctave API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: doctave-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.3
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doctave/refs/heads/main/screenshots/doctave-2026-06-20T180112.png
security:
- kind: authentication
  name: Doctave Authentication
  slug: doctave-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Doctave Domain Security
  slug: doctave-domain-security
  summary_line: TLSv1.3 · DMARC
slug: doctave
tags:
- Documentation
- OpenAPI
- Platform
- Portals
website: https://www.doctave.com/
---
