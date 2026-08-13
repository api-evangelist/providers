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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Google Vault Agentic Access
  operation_count: 33
  slug: google-vault-agentic-access
  summary_line: 33 operations · 22 acting
api_count: 6
apis:
- description: The Exports API from Google Vault — 2 operation(s) for exports.
  name: Google Vault Exports API
  slug: google-vault-exports-api
- description: The HeldAccounts API from Google Vault — 2 operation(s) for heldaccounts.
  name: Google Vault HeldAccounts API
  slug: google-vault-heldaccounts-api
- description: The Holds API from Google Vault — 4 operation(s) for holds.
  name: Google Vault Holds API
  slug: google-vault-holds-api
- description: The Matters API from Google Vault — 8 operation(s) for matters.
  name: Google Vault Matters API
  slug: google-vault-matters-api
- description: The Operations API from Google Vault — 3 operation(s) for operations.
  name: Google Vault Operations API
  slug: google-vault-operations-api
- description: The SavedQueries API from Google Vault — 2 operation(s) for savedqueries.
  name: Google Vault SavedQueries API
  slug: google-vault-savedqueries-api
artifact_total: 15
collections:
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
random_paper: 38
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
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 52.2
    developer_ergonomics: 30.4
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
