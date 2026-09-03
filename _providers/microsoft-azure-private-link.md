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
- acting_count: 3
  human_in_the_loop: 0
  name: Microsoft Azure Private Link Agentic Access
  operation_count: 7
  slug: microsoft-azure-private-link-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 2
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: microsoft-azure-private-link Operations API
  slug: microsoft-azure-private-link-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Private Endpoints operations
  name: microsoft-azure-private-link Private Endpoints API
  slug: microsoft-azure-private-link-private-endpoints-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Private Link REST Operations API
  slug: open-microsoft-azure-private-link-operations-api
- collection_type: open
  name: Azure Private Link REST Operations Private Endpoints API
  slug: open-microsoft-azure-private-link-private-endpoints-api
- collection_type: open
  name: Azure Private Link REST API
  slug: open-microsoft-azure-private-link
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-private-link-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-private-link-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-private-link-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-private-link-scopes.yml
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
description: Microsoft Azure Private Link enables access to Azure PaaS services and Azure-hosted customer-owned services over a private endpoint in a virtual network, eliminating exposure to the public internet.
finops:
- name: Microsoft Azure Private Link Finops
  service_category: API
  slug: microsoft-azure-private-link-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-private-link.png
layout: provider
modified: '2026-05-19'
name: Microsoft Azure Private Link
nav: Providers
network: true
overview: 'Microsoft Azure Private Link publishes 2 APIs on the [APIs.io](https://apis.io/) network: microsoft-azure-private-link Operations API and microsoft-azure-private-link Private Endpoints API.


  Microsoft Azure Private Link''s developer surface includes authentication, developer portal, pricing, support, and 7 more developer resources.'
plans:
- name: Microsoft Azure Private Link Plans Pricing
  plan_count: 3
  slug: microsoft-azure-private-link-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Microsoft Azure Private Link Rate Limits
  slug: microsoft-azure-private-link-rate-limits
scopes:
- name: Microsoft Azure Private Link Scopes
  scope_count: 1
  slug: microsoft-azure-private-link-scopes
  summary_line: 1 scope · implicit
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/screenshots/microsoft-azure-private-link-2026-06-20T185432.png
security:
- kind: authentication
  name: Microsoft Azure Private Link Authentication
  slug: microsoft-azure-private-link-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Private Link Domain Security
  slug: microsoft-azure-private-link-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-azure-private-link
website: https://portal.azure.com/
---
