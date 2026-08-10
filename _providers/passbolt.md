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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Passbolt Agentic Access
  operation_count: 90
  slug: passbolt-agentic-access
  summary_line: 90 operations · 51 acting
api_count: 27
apis:
- description: The legacy authentication method, using the GPGAuth protocol. Find more [here](https://www.passbolt.com/docs/development/authentication).
  name: Passbolt Authentication (GPGAuth) API
  slug: passbolt-authentication-gpgauth-api
- description: JWT-based authentication is the preferred way to interact with the Passbolt API. Find more [here](https://www.passbolt.com/docs/development)
  name: Passbolt Authentication (JWT) API
  slug: passbolt-authentication-jwt-api
- description: Query avatar images.
  name: Passbolt Avatars API
  slug: passbolt-avatars-api
- description: Manipulate comments for resources.
  name: Passbolt Comments API
  slug: passbolt-comments-api
- description: Run directory synchronization.
  name: Passbolt Directory Sync API
  slug: passbolt-directory-sync-api
- description: The favorite endpoints are used to add or remove a `Resource` from your favorites.
  name: Passbolt Favorites API
  slug: passbolt-favorites-api
- description: Organize your passwords and share them in bulk using folders.
  name: Passbolt Folders API
  slug: passbolt-folders-api
- description: In order to encrypt information, the server and the clients needs the user's public keys. These OpenPGP endpoints let you query the saved public key data.
  name: Passbolt GPG keys API
  slug: passbolt-gpg-keys-api
- description: Organize users in logical groups to make it easier to share resources with them.
  name: Passbolt Groups API
  slug: passbolt-groups-api
- description: Gather data about the passbolt instance's health.
  name: Passbolt Healthcheck API
  slug: passbolt-healthcheck-api
- description: Manipulate metadata keys.
  name: Passbolt Metadata keys API
  slug: passbolt-metadata-keys-api
- description: Manipulate private keys for metadata.
  name: Passbolt Metadata private keys API
  slug: passbolt-metadata-private-keys-api
- description: Gather information about metadata keys that needs to be rotated
  name: Passbolt Metadata rotate key API
  slug: passbolt-metadata-rotate-key-api
- description: Gather information on the saved encrypted session keys cache
  name: Passbolt Metadata session key API
  slug: passbolt-metadata-session-key-api
- description: Retrieve information about the resource types settings selected by the administrators
  name: Passbolt Metadata types settings API
  slug: passbolt-metadata-types-settings-api
- description: Upgrading elements to the new v5 metadata format
  name: Passbolt Metadata upgrade API
  slug: passbolt-metadata-upgrade-api
- description: Move a folder or a resource across folders.
  name: Passbolt Move API
  slug: passbolt-move-api
- description: Complete and validate authentication for users with MFA enabled.
  name: Passbolt Multi-Factor Authentication API
  slug: passbolt-multi-factor-authentication-api
- description: Query permissions for resources.
  name: Passbolt Permissions API
  slug: passbolt-permissions-api
- description: Resource-types are used for describing how and what data is stored for a resource and its associated secrets.
  name: Passbolt Resource types API
  slug: passbolt-resource-types-api
- description: A resource holds the metadata for its secrets.
  name: Passbolt Resources API
  slug: passbolt-resources-api
- description: Different categories of users.
  name: Passbolt Roles API
  slug: passbolt-roles-api
- description: Secrets associated to resources.
  name: Passbolt Secrets API
  slug: passbolt-secrets-api
- description: Retrieve the server settings
  name: Passbolt Settings API
  slug: passbolt-settings-api
- description: Share resources and folders to users with an exhaustive permission system.
  name: Passbolt Shares API
  slug: passbolt-shares-api
- description: Get tags and add tags to resources to categorize them.
  name: Passbolt Tags API
  slug: passbolt-tags-api
- description: User are entities with the ability to interact with the application.
  name: Passbolt Users API
  slug: passbolt-users-api
artifact_total: 34
common:
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


  Passbolt''s developer surface includes authentication, documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Passbolt Plans Pricing
  plan_count: 3
  slug: passbolt-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Passbolt Rate Limits
  slug: passbolt-rate-limits
score:
  band: thin
  composite: 38.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
