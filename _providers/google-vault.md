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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Google Vault Agentic Access
  operation_count: 33
  slug: google-vault-agentic-access
  summary_line: 33 operations · 22 acting
api_count: 1
apis:
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Exports API from Google Vault — 2 operation(s) for exports.
  name: Google Vault Exports API
  slug: google-vault-exports-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The HeldAccounts API from Google Vault — 2 operation(s) for heldaccounts.
  name: Google Vault HeldAccounts API
  slug: google-vault-heldaccounts-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Holds API from Google Vault — 4 operation(s) for holds.
  name: Google Vault Holds API
  slug: google-vault-holds-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Matters API from Google Vault — 8 operation(s) for matters.
  name: Google Vault Matters API
  slug: google-vault-matters-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The Operations API from Google Vault — 3 operation(s) for operations.
  name: Google Vault Operations API
  slug: google-vault-operations-api
- baseURL: https://vault.googleapis.com
  baseurl_source: declared
  description: The SavedQueries API from Google Vault — 2 operation(s) for savedqueries.
  name: Google Vault SavedQueries API
  slug: google-vault-savedqueries-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Vault Exports API
  slug: open-google-vault-exports-api
- collection_type: open
  name: Google Vault Exports HeldAccounts API
  slug: open-google-vault-heldaccounts-api
- collection_type: open
  name: Google Vault Exports Holds API
  slug: open-google-vault-holds-api
- collection_type: open
  name: Google Vault Exports Matters API
  slug: open-google-vault-matters-api
- collection_type: open
  name: Google Vault Exports Operations API
  slug: open-google-vault-operations-api
- collection_type: open
  name: Google Vault Exports SavedQueries API
  slug: open-google-vault-savedqueries-api
- collection_type: open
  name: Google Vault API
  slug: open-google-vault
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-vault-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-vault-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-vault-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-vault-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-vault-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/vault/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/vault/release-notes
- group: company
  title: ''
  type: Blog
  url: https://workspace.google.com/blog/
created: '2025-01-01'
description: A collection of APIs for Google Vault, an information governance and eDiscovery tool for Google Workspace.
finops:
- name: Google Vault Finops
  service_category: API
  slug: google-vault-finops
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
layout: provider
modified: '2026-04-28'
name: Google Vault
nav: Providers
network: true
overview: 'Google Vault publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Exports API, HeldAccounts API, Holds API, and 3 more.


  Google Vault''s developer surface includes authentication, getting-started guide, developer console, changelog, engineering blog, and 7 more developer resources.'
plans:
- name: Google Vault Plans Pricing
  plan_count: 3
  slug: google-vault-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Google Vault Rate Limits
  slug: google-vault-rate-limits
scopes:
- name: Google Vault Scopes
  scope_count: 2
  slug: google-vault-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 23.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: false
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-vault/refs/heads/main/screenshots/google-vault-2026-06-20T182245.png
security:
- kind: authentication
  name: Google Vault Authentication
  slug: google-vault-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Vault Domain Security
  slug: google-vault-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Vault Vulnerability Disclosure
  slug: google-vault-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-vault
website: https://developers.google.com/vault
---
