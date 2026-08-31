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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Doctave Agentic Access
  operation_count: 14
  slug: doctave-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 1
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
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Doctave Deployments API
  slug: open-doctave-deployments-api
- collection_type: open
  name: Doctave API
  slug: open-doctave-doctave
- collection_type: open
  name: Doctave Deployments Pages API
  slug: open-doctave-pages-api
- collection_type: open
  name: Doctave Deployments Search API
  slug: open-doctave-search-api
- collection_type: open
  name: Doctave Deployments Sites API
  slug: open-doctave-sites-api
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
overview: 'Doctave publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Deployments API, Pages API, Search API, and 1 more. Tagged areas include Documentation, OpenAPI, Platform, and Portal.


  The Doctave catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Doctave''s developer surface includes authentication, documentation, engineering blog, pricing, and 5 more developer resources.'
plans:
- name: Doctave Plans Pricing
  plan_count: 3
  slug: doctave-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Doctave Rate Limits
  slug: doctave-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Doctave API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: doctave-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 67.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 62.6
    developer_ergonomics: 23.8
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 10.5
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Portal
website: https://www.doctave.com/
---
