---
access_model:
  confidence: medium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
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
  description: Gather data about the passbolt instance's health.
  name: Passbolt Healthcheck API
  slug: passbolt-healthcheck-api
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
artifact_total: 62
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/passbolt-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/passbolt-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/passbolt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/passbolt-domain-security.yml
- group: auth
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
- name: Passbolt Finops
  service_category: API
  slug: passbolt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/passbolt.png
layout: provider
modified: '2026-05-19'
name: Passbolt
nav: Providers
network: true
overview: 'Passbolt publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Authentication (GPGAuth) API, Authentication (JWT) API, Avatars API, and 24 more. Tagged areas include Password Manager, Security, Secrets, and Identity.


  Passbolt''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Passbolt Plans Pricing
  plan_count: 3
  slug: passbolt-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Passbolt Rate Limits
  slug: passbolt-rate-limits
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.5
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/passbolt/refs/heads/main/screenshots/passbolt-2026-06-20T191434.png
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
