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
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Cache For Redis Agentic Access
  operation_count: 7
  slug: microsoft-azure-cache-for-redis-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- description: Operations operations
  name: microsoft-azure-cache-for-redis Operations API
  slug: microsoft-azure-cache-for-redis-operations-api
- description: Redis operations
  name: microsoft-azure-cache-for-redis Redis API
  slug: microsoft-azure-cache-for-redis-redis-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Cache for Redis REST Operations API
  slug: open-microsoft-azure-cache-for-redis-operations-api
- collection_type: open
  name: Azure Cache for REST Operations Redis API
  slug: open-microsoft-azure-cache-for-redis-redis-api
- collection_type: open
  name: Azure Cache for Redis REST API
  slug: open-microsoft-azure-cache-for-redis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-cache-for-redis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-cache-for-redis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-cache-for-redis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-cache-for-redis-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://portal.azure.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
created: '2026-03-13'
description: Reference for Azure Cache for Redis REST APIs.
finops:
- name: Microsoft Azure Cache For Redis Finops
  service_category: API
  slug: microsoft-azure-cache-for-redis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-cache-for-redis.png
layout: provider
modified: '2026-05-19'
name: microsoft-azure-cache-for-redis
nav: Providers
network: true
overview: 'microsoft-azure-cache-for-redis publishes 2 APIs on the [APIs.io](https://apis.io/) network: Operations API and Redis API.


  microsoft-azure-cache-for-redis'' developer surface includes authentication, developer portal, pricing, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Azure Cache For Redis Plans Pricing
  plan_count: 3
  slug: microsoft-azure-cache-for-redis-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Microsoft Azure Cache For Redis Rate Limits
  slug: microsoft-azure-cache-for-redis-rate-limits
scopes:
- name: Microsoft Azure Cache For Redis Scopes
  scope_count: 1
  slug: microsoft-azure-cache-for-redis-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 38.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/screenshots/microsoft-azure-cache-for-redis-2026-06-20T185402.png
security:
- kind: authentication
  name: Microsoft Azure Cache For Redis Authentication
  slug: microsoft-azure-cache-for-redis-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Cache For Redis Domain Security
  slug: microsoft-azure-cache-for-redis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-cache-for-redis
website: https://portal.azure.com/
---
