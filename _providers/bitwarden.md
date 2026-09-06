---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    error_semantics: verified
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
  score: 28.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Bitwarden Agentic Access
  operation_count: 24
  slug: bitwarden-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 1
apis:
- description: OAuth2 / OpenID Connect token endpoint that issues bearer tokens for the Public API and Vault Management API. Organization API keys use the client_credentials grant with scope api.organization; bearer
  name: Bitwarden Identity API
  slug: identity
- description: 'SCIM 2.0 endpoint for directory-driven provisioning of users and groups (used by Okta, Entra ID, OneLogin, JumpCloud, Google Workspace via SCIM). Supports automatic invite, update, and offboard flows '
  name: Bitwarden SCIM API
  slug: scim
- description: Local Bitwarden CLI HTTP API for managing personal vault items, folders, sends, collections, organizations, the generator, and miscellaneous operations. Exposed by the bw CLI in serve mode and intende
  name: Bitwarden Vault Management API
  slug: vault-management
- description: Secrets Manager API for storing and retrieving application secrets and managing projects, service accounts, secrets, and access tokens used by infrastructure and developer tooling.
  name: Bitwarden Secrets Manager API
  slug: secrets-manager
- baseURL: https://api.bitwarden.com/public
  baseurl_source: declared
  description: The Collections API from Bitwarden — 2 operation(s) for collections.
  name: Bitwarden Collections API
  slug: bitwarden-collections-api
- baseURL: https://api.bitwarden.com/public
  baseurl_source: declared
  description: The Events API from Bitwarden — 1 operation(s) for events.
  name: Bitwarden Events API
  slug: bitwarden-events-api
- baseURL: https://api.bitwarden.com/public
  baseurl_source: declared
  description: The Groups API from Bitwarden — 3 operation(s) for groups.
  name: Bitwarden Groups API
  slug: bitwarden-groups-api
- baseURL: https://api.bitwarden.com/public
  baseurl_source: declared
  description: The Members API from Bitwarden — 4 operation(s) for members.
  name: Bitwarden Members API
  slug: bitwarden-members-api
- baseURL: https://api.bitwarden.com/public
  baseurl_source: declared
  description: The Organization API from Bitwarden — 1 operation(s) for organization.
  name: Bitwarden Organization API
  slug: bitwarden-organization-api
- baseURL: https://api.bitwarden.com/public
  baseurl_source: declared
  description: The Policies API from Bitwarden — 3 operation(s) for policies.
  name: Bitwarden Policies API
  slug: bitwarden-policies-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bitwarden Public Collections API
  slug: open-bitwarden-collections-api
- collection_type: open
  name: Bitwarden Public Collections Events API
  slug: open-bitwarden-events-api
- collection_type: open
  name: Bitwarden Public Collections Groups API
  slug: open-bitwarden-groups-api
- collection_type: open
  name: Bitwarden Public Collections Members API
  slug: open-bitwarden-members-api
- collection_type: open
  name: Bitwarden Public Collections Organization API
  slug: open-bitwarden-organization-api
- collection_type: open
  name: Bitwarden Public Collections Policies API
  slug: open-bitwarden-policies-api
- collection_type: open
  name: Bitwarden Public API
  slug: open-bitwarden-public-swagger
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitwarden-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/bitwarden-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitwarden-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bitwarden-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bitwarden-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bitwarden
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bitwarden1
- group: company
  title: ''
  type: Website
  url: https://bitwarden.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bitwarden.com/help/public-api/
- group: docs
  title: ''
  type: APIReference
  url: https://bitwarden.com/help/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/bitwarden-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bitwarden-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bitwarden-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://bitwarden.com/blog/feed.xml
created: '2026-05-08'
description: Bitwarden is an open-source password and secret management platform. The Bitwarden Public API exposes organization-level resources - members, groups, collections, policies, and event logs - plus a separate Vault Management API for personal vault items, an Identity (OAuth2) endpoint for token issuance, a SCIM endpoint for directory-based provisioning, and the Secrets Manager API for application secrets.
finops:
- name: Bitwarden Finops
  service_category: Identity and Access Management
  slug: bitwarden-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bitwarden.png
layout: provider
modified: '2026-05-19'
name: Bitwarden
nav: Providers
network: true
overview: 'Bitwarden publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Events API, Groups API, and 3 more. Tagged areas include Security, Password Manager, Open-Source, Vault, and Identity.


  Bitwarden''s developer surface includes authentication, documentation, API reference, engineering blog, and 10 more developer resources.'
plans:
- name: Bitwarden Plans Pricing
  plan_count: 6
  slug: bitwarden-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Bitwarden Rate Limits
  slug: bitwarden-rate-limits
scopes:
- name: Bitwarden Scopes
  scope_count: 1
  slug: bitwarden-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 32.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 55.0
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 32.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitwarden/refs/heads/main/screenshots/bitwarden-2026-06-20T173325.png
security:
- kind: authentication
  name: Bitwarden Authentication
  slug: bitwarden-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Bitwarden Domain Security
  slug: bitwarden-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Bitwarden Trust Center
  slug: bitwarden-trust-center
  summary_line: SOC 2, GDPR
slug: bitwarden
tags:
- Security
- Password Manager
- Open-Source
- Vault
- Identity
- SCIM
website: https://bitwarden.com/
---
