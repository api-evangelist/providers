---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Passbolt Agentic Access
  operation_count: 90
  slug: passbolt-agentic-access
  summary_line: 90 operations · 51 acting
api_count: 1
apis:
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: The legacy authentication method, using the GPGAuth protocol. Find more [here](https://www.passbolt.com/docs/development/authentication).
  name: Passbolt Authentication (GPGAuth) API
  slug: passbolt-authentication-gpgauth-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: JWT-based authentication is the preferred way to interact with the Passbolt API. Find more [here](https://www.passbolt.com/docs/development)
  name: Passbolt Authentication (JWT) API
  slug: passbolt-authentication-jwt-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Query avatar images.
  name: Passbolt Avatars API
  slug: passbolt-avatars-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Manipulate comments for resources.
  name: Passbolt Comments API
  slug: passbolt-comments-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Run directory synchronization.
  name: Passbolt Directory Sync API
  slug: passbolt-directory-sync-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: The favorite endpoints are used to add or remove a `Resource` from your favorites.
  name: Passbolt Favorites API
  slug: passbolt-favorites-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Organize your passwords and share them in bulk using folders.
  name: Passbolt Folders API
  slug: passbolt-folders-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: In order to encrypt information, the server and the clients needs the user's public keys. These OpenPGP endpoints let you query the saved public key data.
  name: Passbolt GPG keys API
  slug: passbolt-gpg-keys-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Organize users in logical groups to make it easier to share resources with them.
  name: Passbolt Groups API
  slug: passbolt-groups-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Manipulate metadata keys.
  name: Passbolt Metadata keys API
  slug: passbolt-metadata-keys-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Manipulate private keys for metadata.
  name: Passbolt Metadata private keys API
  slug: passbolt-metadata-private-keys-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Gather information about metadata keys that needs to be rotated
  name: Passbolt Metadata rotate key API
  slug: passbolt-metadata-rotate-key-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Gather information on the saved encrypted session keys cache
  name: Passbolt Metadata session key API
  slug: passbolt-metadata-session-key-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Retrieve information about the resource types settings selected by the administrators
  name: Passbolt Metadata types settings API
  slug: passbolt-metadata-types-settings-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Upgrading elements to the new v5 metadata format
  name: Passbolt Metadata upgrade API
  slug: passbolt-metadata-upgrade-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Move a folder or a resource across folders.
  name: Passbolt Move API
  slug: passbolt-move-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Complete and validate authentication for users with MFA enabled.
  name: Passbolt Multi-Factor Authentication API
  slug: passbolt-multi-factor-authentication-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Query permissions for resources.
  name: Passbolt Permissions API
  slug: passbolt-permissions-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Resource-types are used for describing how and what data is stored for a resource and its associated secrets.
  name: Passbolt Resource types API
  slug: passbolt-resource-types-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: A resource holds the metadata for its secrets.
  name: Passbolt Resources API
  slug: passbolt-resources-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Different categories of users.
  name: Passbolt Roles API
  slug: passbolt-roles-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Secrets associated to resources.
  name: Passbolt Secrets API
  slug: passbolt-secrets-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Retrieve the server settings
  name: Passbolt Settings API
  slug: passbolt-settings-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Share resources and folders to users with an exhaustive permission system.
  name: Passbolt Shares API
  slug: passbolt-shares-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Get tags and add tags to resources to categorize them.
  name: Passbolt Tags API
  slug: passbolt-tags-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: User are entities with the ability to interact with the application.
  name: Passbolt Users API
  slug: passbolt-users-api
- baseURL: https://passbolt.local
  baseurl_source: declared
  description: Gather data about the passbolt instance's health.
  name: Passbolt Health Check API
  slug: passbolt-health-check-api
artifact_total: 62
collections:
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Authentication (GPGAuth) API
  slug: open-passbolt-authentication-gpgauth-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Authentication (JWT) API
  slug: open-passbolt-authentication-jwt-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Avatars API
  slug: open-passbolt-avatars-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Comments API
  slug: open-passbolt-comments-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Directory Sync API
  slug: open-passbolt-directory-sync-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Favorites API
  slug: open-passbolt-favorites-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Folders API
  slug: open-passbolt-folders-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) GPG keys API
  slug: open-passbolt-gpg-keys-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Groups API
  slug: open-passbolt-groups-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Healthcheck API
  slug: open-passbolt-healthcheck-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Metadata keys API
  slug: open-passbolt-metadata-keys-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Metadata private keys API
  slug: open-passbolt-metadata-private-keys-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Metadata rotate key API
  slug: open-passbolt-metadata-rotate-key-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Metadata session key API
  slug: open-passbolt-metadata-session-key-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Metadata types settings API
  slug: open-passbolt-metadata-types-settings-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Metadata upgrade API
  slug: open-passbolt-metadata-upgrade-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Move API
  slug: open-passbolt-move-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Multi-Factor Authentication API
  slug: open-passbolt-multi-factor-authentication-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Permissions API
  slug: open-passbolt-permissions-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Resource types API
  slug: open-passbolt-resource-types-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Resources API
  slug: open-passbolt-resources-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Roles API
  slug: open-passbolt-roles-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Secrets API
  slug: open-passbolt-secrets-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Settings API
  slug: open-passbolt-settings-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Shares API
  slug: open-passbolt-shares-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Tags API
  slug: open-passbolt-tags-api
- collection_type: open
  name: Passbolt Authentication (GPGAuth) Authentication (GPGAuth) Users API
  slug: open-passbolt-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/passbolt/plans/passbolt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/passbolt-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/passbolt/rate-limits/passbolt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/passbolt-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/passbolt/finops/passbolt-finops.yml
  title: ''
  type: FinOps
  url: finops/passbolt-finops.yml
- group: other
  href: https://artifacts.apis.io/passbolt/capabilities/passbolt-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/passbolt-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/passbolt/agentic-access/passbolt-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/passbolt-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/passbolt/security/passbolt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/passbolt-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/passbolt/security/passbolt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/passbolt-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/passbolt/authentication/passbolt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/passbolt-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/passbolt
- group: company
  title: ''
  type: Website
  url: https://www.passbolt.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.passbolt.com/docs/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/passbolt
- group: company
  title: ''
  type: Blog
  url: https://www.passbolt.com/blog
created: '2025-02-21'
description: Passbolt is an open source password manager for teams. The Passbolt API provides programmatic access to manage resources (passwords), folders, users, groups, sharing, comments, metadata, and authentication via GPGAuth or JWT.
finops:
- has_sources: false
  method: generated
  name: Passbolt Finops
  primary_unit: request
  service_category: API
  slug: passbolt-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/passbolt.png
layout: provider
modified: '2026-05-19'
name: Passbolt
nav: Providers
network: true
overview: 'Passbolt publishes 27 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication (GPGAuth) API, Authentication (JWT) API, Avatars API, and 24 more. Tagged areas include Password Manager, Security, Secrets, and Identity.


  The Passbolt catalog on APIs.io includes 1 Spectral governance ruleset.


  Passbolt''s developer surface includes authentication, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Passbolt Plans Pricing
  plan_count: 3
  slug: passbolt-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Passbolt Rate Limits
  slug: passbolt-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Passbolt API Rules
  rule_count: 53
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 9
  slug: passbolt-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 48.4
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 23.7
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/passbolt/passbolt-2026-06-20T191434.png
security:
- kind: authentication
  name: Passbolt Authentication
  slug: passbolt-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Passbolt Domain Security
  slug: passbolt-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Passbolt Vulnerability Disclosure
  slug: passbolt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: passbolt
tags:
- Password Manager
- Security
- Secrets
- Identity
website: https://www.passbolt.com
---
