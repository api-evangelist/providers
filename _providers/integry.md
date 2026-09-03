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
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Integry Agentic Access
  operation_count: 6
  slug: integry-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.integry.io
  baseurl_source: declared
  description: The Apps API from Integry — 2 operation(s) for apps.
  name: Integry Apps API
  slug: integry-apps-api
- baseURL: https://api.integry.io
  baseurl_source: declared
  description: The Functions API from Integry — 4 operation(s) for functions.
  name: Integry Functions API
  slug: integry-functions-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Integry Apps API
  slug: open-integry-apps-api
- collection_type: open
  name: Integry Apps Functions API
  slug: open-integry-functions-api
- collection_type: open
  name: Integry API
  slug: open-integry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/integry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/integry-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/integry-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/integryio
- group: company
  title: ''
  type: Website
  url: https://integry.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.integry.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IntegryHQ
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.integry.ai/llms.txt
created: '2026-03-27'
description: Integry is an embedded integration platform that lets SaaS companies offer native integrations to their users.
finops:
- name: Integry Finops
  service_category: API
  slug: integry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/integry.png
layout: provider
modified: '2026-05-19'
name: Integry
nav: Providers
network: true
overview: 'Integry publishes 2 APIs on the [APIs.io](https://apis.io/) network: Apps API and Functions API. Tagged areas include Embedded iPaaS, Integration, and Native Integrations.


  Integry''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Integry Plans Pricing
  plan_count: 3
  slug: integry-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Integry Rate Limits
  slug: integry-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.1
    developer_ergonomics: 21.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/integry/refs/heads/main/screenshots/integry-2026-06-20T183535.png
security:
- kind: authentication
  name: Integry Authentication
  slug: integry-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Integry Domain Security
  slug: integry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: integry
tags:
- Embedded iPaaS
- Integration
- Native Integrations
website: https://integry.io
---
