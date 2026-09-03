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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Formance Agentic Access
  operation_count: 95
  slug: formance-agentic-access
  summary_line: 95 operations · 46 acting
api_count: 1
apis:
- baseURL: https://{organization}.{environment}.formance.cloud/api/ledger
  baseurl_source: declared
  description: OAuth2 / OIDC authorization server, clients, and users.
  name: Formance Auth API
  slug: formance-auth-api
- baseURL: https://{organization}.{environment}.formance.cloud/api/ledger
  baseurl_source: declared
  description: Programmable double-entry ledger (v2).
  name: Formance Ledger API
  slug: formance-ledger-api
- baseURL: https://{organization}.{environment}.formance.cloud/api/ledger
  baseurl_source: declared
  description: Flows workflows, instances, and triggers (v2).
  name: Formance Orchestration API
  slug: formance-orchestration-api
- baseURL: https://{organization}.{environment}.formance.cloud/api/ledger
  baseurl_source: declared
  description: Unified payments connectivity, connectors, and transfers.
  name: Formance Payments API
  slug: formance-payments-api
- baseURL: https://{organization}.{environment}.formance.cloud/api/ledger
  baseurl_source: declared
  description: Reconciliation policies and runs.
  name: Formance Reconciliation API
  slug: formance-reconciliation-api
- baseURL: https://{organization}.{environment}.formance.cloud/api/ledger
  baseurl_source: declared
  description: Cross-module search.
  name: Formance Search API
  slug: formance-search-api
- baseURL: https://{organization}.{environment}.formance.cloud/api/ledger
  baseurl_source: declared
  description: White-label wallets, balances, and holds.
  name: Formance Wallets API
  slug: formance-wallets-api
- baseURL: https://{organization}.{environment}.formance.cloud/api/ledger
  baseurl_source: declared
  description: Webhook subscription configuration.
  name: Formance Webhooks API
  slug: formance-webhooks-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Formance Platform Auth API
  slug: open-formance-auth-api
- collection_type: open
  name: Formance Platform Auth Ledger API
  slug: open-formance-ledger-api
- collection_type: open
  name: Formance Platform Auth Orchestration API
  slug: open-formance-orchestration-api
- collection_type: open
  name: Formance Platform Auth Payments API
  slug: open-formance-payments-api
- collection_type: open
  name: Formance Platform Auth Reconciliation API
  slug: open-formance-reconciliation-api
- collection_type: open
  name: Formance Platform Auth Search API
  slug: open-formance-search-api
- collection_type: open
  name: Formance Platform Auth Wallets API
  slug: open-formance-wallets-api
- collection_type: open
  name: Formance Platform Auth Webhooks API
  slug: open-formance-webhooks-api
- collection_type: open
  name: Formance Platform API
  slug: open-formance
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/formance-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/formance-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/formance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/formance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/formance-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/formancehq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/formance
- group: company
  title: ''
  type: Website
  url: https://www.formance.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formance.com
- group: commercial
  title: ''
  type: Plans
  url: plans/formance-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/formance-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/formance-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.formance.com/blog/rss.xml
created: '2026-07-01'
description: Formance builds open-source financial infrastructure for money movement. The platform pairs a programmable double-entry Ledger (with the Numscript DSL) with a unified Payments connectivity layer and Flows orchestration, plus Wallets, Reconciliation, Auth, and Webhooks. It is delivered as open-source components and as a managed multi-tenant Formance Cloud, exposing REST APIs secured with OAuth2 client-credentials Bearer tokens.
finops:
- name: Formance Finops
  service_category: Financial Infrastructure
  slug: formance-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/formance.png
layout: provider
modified: '2026-07-01'
name: Formance
nav: Providers
network: true
overview: 'Formance publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Ledger API, Orchestration API, and 5 more. Tagged areas include Financial Infrastructure, Ledger, double-entry-accounting, Payments, and Orchestration.


  Formance''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Formance Plans Pricing
  plan_count: 3
  slug: formance-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Formance Rate Limits
  slug: formance-rate-limits
scopes:
- name: Formance Scopes
  scope_count: 6
  slug: formance-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.2
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/formance/refs/heads/main/screenshots/formance-2026-07-25T214946.png
security:
- kind: authentication
  name: Formance Authentication
  slug: formance-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Formance Domain Security
  slug: formance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Formance Vulnerability Disclosure
  slug: formance-vulnerability-disclosure
  summary_line: disclosure policy published
slug: formance
tags:
- Financial Infrastructure
- Ledger
- double-entry-accounting
- Payments
- Orchestration
- Money Movement
- Open-Source
- Fintech
website: https://www.formance.com
---
