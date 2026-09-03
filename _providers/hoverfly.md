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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
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
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Hoverfly Agentic Access
  operation_count: 42
  slug: hoverfly-agentic-access
  summary_line: 42 operations · 23 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Inspect and clear the cache of matched request-response pairs.
  name: Hoverfly Cache API
  slug: hoverfly-cache-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Inspect and clear response difference reports.
  name: Hoverfly Diff API
  slug: hoverfly-diff-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Manage Hoverfly runtime configuration.
  name: Hoverfly Hoverfly API
  slug: hoverfly-hoverfly-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Inspect and filter the journal of intercepted requests.
  name: Hoverfly Journal API
  slug: hoverfly-journal-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Retrieve runtime logs.
  name: Hoverfly Logs API
  slug: hoverfly-logs-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Manage post-serve actions executed after responses are served.
  name: Hoverfly Post-Serve Actions API
  slug: hoverfly-post-serve-actions-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Manage simulation request-response pairs and metadata.
  name: Hoverfly Simulation API
  slug: hoverfly-simulation-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Manage stateful keys used during simulation.
  name: Hoverfly State API
  slug: hoverfly-state-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: System-level controls.
  name: Hoverfly System API
  slug: hoverfly-system-api
- baseURL: http://localhost:8888
  baseurl_source: declared
  description: Manage CSV-based templating data sources.
  name: Hoverfly Templating Data API
  slug: hoverfly-templating-data-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hoverfly Admin Cache API
  slug: open-hoverfly-cache-api
- collection_type: open
  name: Hoverfly Admin Cache Diff API
  slug: open-hoverfly-diff-api
- collection_type: open
  name: Admin Cache Hoverfly API
  slug: open-hoverfly-hoverfly-api
- collection_type: open
  name: Hoverfly Admin Cache Journal API
  slug: open-hoverfly-journal-api
- collection_type: open
  name: Hoverfly Admin Cache Logs API
  slug: open-hoverfly-logs-api
- collection_type: open
  name: Hoverfly Admin Cache Post-Serve Actions API
  slug: open-hoverfly-post-serve-actions-api
- collection_type: open
  name: Hoverfly Admin Cache Simulation API
  slug: open-hoverfly-simulation-api
- collection_type: open
  name: Hoverfly Admin Cache State API
  slug: open-hoverfly-state-api
- collection_type: open
  name: Hoverfly Admin Cache System API
  slug: open-hoverfly-system-api
- collection_type: open
  name: Hoverfly Admin Cache Templating Data API
  slug: open-hoverfly-templating-data-api
- collection_type: open
  name: Hoverfly Admin API
  slug: open-hoverfly
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/SpectoLabs/hoverfly/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/SpectoLabs/hoverfly/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/SpectoLabs/hoverfly/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/SpectoLabs/hoverfly/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hoverfly-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hoverfly-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hoverfly
- group: company
  title: ''
  type: Website
  url: https://hoverfly.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hoverfly.io
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/SpectoLabs/hoverfly
created: '2026-03-25'
description: Hoverfly is an open source API simulation tool for creating realistic mock services and capturing-replaying HTTP traffic for testing.
finops:
- name: Hoverfly Finops
  service_category: API
  slug: hoverfly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hoverfly.png
layout: provider
modified: '2026-05-19'
name: Hoverfly
nav: Providers
network: true
overview: 'Hoverfly publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Cache API, Diff API, Hoverfly API, and 7 more. Tagged areas include Mocking and Testing.


  Hoverfly''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Hoverfly Plans Pricing
  plan_count: 3
  slug: hoverfly-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Hoverfly Rate Limits
  slug: hoverfly-rate-limits
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 9
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 16.7
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 50.0
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hoverfly/refs/heads/main/screenshots/hoverfly-2026-06-20T182852.png
security:
- kind: domain-security
  name: Hoverfly Domain Security
  slug: hoverfly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hoverfly
tags:
- Mocking
- Testing
website: https://hoverfly.io
---
