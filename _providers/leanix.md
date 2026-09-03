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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Leanix Agentic Access
  operation_count: 22
  slug: leanix-agentic-access
  summary_line: 22 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The configurations API from LeanIX — 1 operation(s) for configurations.
  name: LeanIX configurations API
  slug: leanix-configurations-api
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The examples API from LeanIX — 2 operation(s) for examples.
  name: LeanIX examples API
  slug: leanix-examples-api
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The fastSynchronizationRuns API from LeanIX — 2 operation(s) for fastsynchronizationruns.
  name: LeanIX fastSynchronizationRuns API
  slug: leanix-fastsynchronizationruns-api
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The storages API from LeanIX — 1 operation(s) for storages.
  name: LeanIX storages API
  slug: leanix-storages-api
- baseURL: https://app.leanix.net/services/integration-api/v1
  baseurl_source: declared
  description: The synchronizationRuns API from LeanIX — 13 operation(s) for synchronizationruns.
  name: LeanIX synchronizationRuns API
  slug: leanix-synchronizationruns-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Integration configurations API
  slug: open-leanix-configurations-api
- collection_type: open
  name: Integration configurations examples API
  slug: open-leanix-examples-api
- collection_type: open
  name: Integration configurations fastSynchronizationRuns API
  slug: open-leanix-fastsynchronizationruns-api
- collection_type: open
  name: Integration configurations storages API
  slug: open-leanix-storages-api
- collection_type: open
  name: Integration configurations synchronizationRuns API
  slug: open-leanix-synchronizationruns-api
- collection_type: open
  name: Integration API
  slug: open-leanix
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leanix-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/leanix-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leanix-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leanix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leanix-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leanix
- group: company
  title: ''
  type: Website
  url: https://www.leanix.net
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/leanix/ea
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/leanix
- group: company
  title: ''
  type: Blog
  url: https://www.leanix.net/en/blog
created: '2026-03-27'
description: LeanIX (now SAP LeanIX) is an enterprise architecture and SaaS management platform providing IT portfolio management, application portfolio rationalization, SaaS discovery, and technology risk management. The platform exposes REST APIs for integrating with the fact sheet inventory, running inbound and outbound synchronizations, and managing workspace data.
finops:
- name: Leanix Finops
  service_category: API
  slug: leanix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leanix.png
layout: provider
modified: '2026-05-19'
name: LeanIX
nav: Providers
network: true
overview: 'LeanIX publishes 5 APIs on the [APIs.io](https://apis.io/) network, including configurations API, examples API, fastSynchronizationRuns API, and 2 more. Tagged areas include Enterprise Architecture, SaaS Management, IT Portfolio Management, Application Portfolio, and Technology Risk.


  LeanIX''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Leanix Plans Pricing
  plan_count: 3
  slug: leanix-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Leanix Rate Limits
  slug: leanix-rate-limits
scopes:
- name: Leanix Scopes
  scope_count: 0
  slug: leanix-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 39.9
    developer_ergonomics: 14.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 24.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/screenshots/leanix-2026-06-20T184359.png
security:
- kind: authentication
  name: Leanix Authentication
  slug: leanix-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Leanix Domain Security
  slug: leanix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Leanix Vulnerability Disclosure
  slug: leanix-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: leanix
tags:
- Enterprise Architecture
- SaaS Management
- IT Portfolio Management
- Application Portfolio
- Technology Risk
website: https://www.leanix.net
---
