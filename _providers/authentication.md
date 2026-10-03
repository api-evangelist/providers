---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 15
created: '2026-03-25'
description: A curated index of services, tooling, and open source solutions for API authentication, authorization, identity management, and secrets management. This collection covers identity providers, SSO platforms, privileged access management, MFA, open source identity servers, and authentication standards including OAuth 2.0, OpenID Connect, SAML 2.0, FIDO2/WebAuthn, and SCIM.
features:
- description: Comprehensive coverage of OAuth 2.0 authorization framework implementations from cloud providers, open source projects, and commercial platforms.
  name: OAuth 2.0 Protocol Coverage
- description: Index of OpenID Connect certified identity providers and implementations spanning cloud, on-premises, and self-hosted deployments.
  name: OpenID Connect Providers
- description: Coverage of MFA solutions including TOTP, SMS, push notification, WebAuthn/FIDO2, and hardware token implementations.
  name: Multi-Factor Authentication
- description: Open source identity servers that can be self-hosted including Keycloak, Authelia, Authentik, Zitadel, and Casdoor.
  name: Self-Hosted Identity Solutions
- description: Commercial enterprise IAM platforms including Okta, Auth0, ForgeRock, Ping Identity, and Microsoft Entra ID.
  name: Enterprise Identity Providers
- description: Privileged access management and secrets management tools including HashiCorp Vault and CyberArk for secure credential storage.
  name: Secrets and PAM
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: The foundational authorization framework implemented by every provider in this collection.
  name: OAuth 2.0 Standard
- description: Identity layer on top of OAuth 2.0 providing standardized user info, ID tokens, and discovery endpoints.
  name: OpenID Connect Standard
- description: XML-based authentication standard widely used for enterprise SSO and federation scenarios.
  name: SAML 2.0 Standard
- description: System for Cross-domain Identity Management for automated user provisioning and deprovisioning.
  name: SCIM 2.0 Standard
- description: Web Authentication standard for passwordless and hardware-backed authentication.
  name: FIDO2/WebAuthn Standard
layout: provider
modified: '2026-04-19'
name: Authentication
nav: Providers
network: true
overview: Authentication is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Authentication, Authorization, Identity, MFA, and OpenID Connect.
random_paper: 8
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: authentication
tags:
- Authentication
- Authorization
- Identity
- MFA
- OpenID Connect
- SAML
- Security
- SSO
use_cases:
- description: Compare authentication platforms across self-hosted, cloud, and enterprise tiers to select the right identity provider.
  name: Identity Provider Selection
- description: Find SSO platforms and libraries for implementing single sign-on across applications and services.
  name: SSO Implementation
- description: Research authentication standards, security patterns, and best practices for securing REST, GraphQL, and gRPC APIs.
  name: API Security Research
- description: Discover identity verification services for zero trust network access and continuous authentication architectures.
  name: Zero Trust Architecture
---
