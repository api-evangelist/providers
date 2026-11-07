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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Keycloak Agentic Access
  operation_count: 40
  slug: keycloak-agentic-access
  summary_line: 40 operations · 24 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL_template: https://{host}/admin/realms
  baseurl_source: spec_template
  description: Manage OAuth/OIDC clients within a realm
  name: Keycloak Clients API
  slug: keycloak-clients-api
- baseURL_template: https://{host}/admin/realms
  baseurl_source: spec_template
  description: Manage user groups within a realm
  name: Keycloak Groups API
  slug: keycloak-groups-api
- baseURL_template: https://{host}/admin/realms
  baseurl_source: spec_template
  description: Manage identity providers for federated authentication
  name: Keycloak Identity Providers API
  slug: keycloak-identity-providers-api
- baseURL_template: https://{host}/admin/realms
  baseurl_source: spec_template
  description: Manage Keycloak realms
  name: Keycloak Realms API
  slug: keycloak-realms-api
- baseURL_template: https://{host}/admin/realms
  baseurl_source: spec_template
  description: Manage realm-level and client-level roles
  name: Keycloak Roles API
  slug: keycloak-roles-api
- baseURL_template: https://{host}/admin/realms
  baseurl_source: spec_template
  description: Manage users within a realm
  name: Keycloak Users API
  slug: keycloak-users-api
- description: The Admin API from Keycloak — 22 operation(s) for admin.
  name: Keycloak Admin API
  slug: keycloak-admin-api
- description: The Attack Detection API from Keycloak — 2 operation(s) for attack detection.
  name: Keycloak Attack Detection API
  slug: keycloak-attack-detection-api
- description: The Authentication Management API from Keycloak — 28 operation(s) for authentication management.
  name: Keycloak Authentication Management API
  slug: keycloak-authentication-management-api
- description: The Client Attribute Certificate API from Keycloak — 7 operation(s) for client attribute certificate.
  name: Keycloak Client Attribute Certificate API
  slug: keycloak-client-attribute-certificate-api
- description: The Client Initial Access API from Keycloak — 2 operation(s) for client initial access.
  name: Keycloak Client Initial Access API
  slug: keycloak-client-initial-access-api
- description: The Client Registration Policy API from Keycloak — 1 operation(s) for client registration policy.
  name: Keycloak Client Registration Policy API
  slug: keycloak-client-registration-policy-api
- description: The Client Role Mappings API from Keycloak — 9 operation(s) for client role mappings.
  name: Keycloak Client Role Mappings API
  slug: keycloak-client-role-mappings-api
- description: The Client Scopes API from Keycloak — 4 operation(s) for client scopes.
  name: Keycloak Client Scopes API
  slug: keycloak-client-scopes-api
- description: The Component API from Keycloak — 3 operation(s) for component.
  name: Keycloak Component API
  slug: keycloak-component-api
- description: The Key API from Keycloak — 1 operation(s) for key.
  name: Keycloak Key API
  slug: keycloak-key-api
- description: The Organizations API from Keycloak — 24 operation(s) for organizations.
  name: Keycloak Organizations API
  slug: keycloak-organizations-api
- description: The Protocol Mappers API from Keycloak — 12 operation(s) for protocol mappers.
  name: Keycloak Protocol Mappers API
  slug: keycloak-protocol-mappers-api
- description: The Realms Admin API from Keycloak — 28 operation(s) for realms admin.
  name: Keycloak Realms Admin API
  slug: keycloak-realms-admin-api
- description: The Role Mapper API from Keycloak — 12 operation(s) for role mapper.
  name: Keycloak Role Mapper API
  slug: keycloak-role-mapper-api
- description: The Roles (by ID) API from Keycloak — 5 operation(s) for roles (by id).
  name: Keycloak Roles (by ID) API
  slug: keycloak-roles-by-id-api
- description: The Scope Mappings API from Keycloak — 21 operation(s) for scope mappings.
  name: Keycloak Scope Mappings API
  slug: keycloak-scope-mappings-api
- description: The Workflows API from Keycloak — 6 operation(s) for workflows.
  name: Keycloak Workflows API
  slug: keycloak-workflows-api
arazzos:
- description: Resolve a user and a group by name, add the membership, and verify it landed.
  name: Keycloak Assign a User to a Group
  slug: keycloak-assign-user-to-group-workflow
- description: Resolve a group by name, read its roles and roster, and spot-check the effective roles of a member.
  name: Keycloak Audit Group Membership
  slug: keycloak-audit-group-membership-workflow
- description: Resolve a user by username and assemble their profile, realm role mappings, and group membership.
  name: Keycloak Audit a User's Effective Access
  slug: keycloak-audit-user-access-workflow
- description: Snapshot a client registration, disable it, and optionally delete it after a soak period.
  name: Keycloak Decommission a Client
  slug: keycloak-decommission-client-workflow
- description: Upsert an OIDC or SAML identity provider by alias and verify the stored configuration.
  name: Keycloak Federate an Identity Provider
  slug: keycloak-federate-identity-provider-workflow
- description: Capture a realm's current settings, apply brute force protection and session hardening, and verify the result.
  name: Keycloak Apply a Realm Security Baseline
  slug: keycloak-harden-realm-workflow
- description: Discover available realms and assemble a full read-only inventory of one realm's clients, roles, groups, and identity providers.
  name: Keycloak Inventory a Realm
  slug: keycloak-inventory-realm-workflow
- description: Disable a user, strip realm role mappings and group membership, and optionally delete the account.
  name: Keycloak Offboard a User
  slug: keycloak-offboard-user-workflow
- description: Provision a realm user, set an initial password, and grant a realm-level role.
  name: Keycloak Onboard a User
  slug: keycloak-onboard-user-workflow
- description: Create a top-level group, resolve its id, nest a child group beneath it, and read back the hierarchy.
  name: Keycloak Provision a Group Hierarchy
  slug: keycloak-provision-group-hierarchy-workflow
- description: Register an OpenID Connect client in a realm, resolve its internal UUID, and retrieve its generated secret.
  name: Keycloak Register a Confidential OIDC Client
  slug: keycloak-register-oidc-client-workflow
- description: Resolve a client by clientId, capture the outgoing secret, regenerate it, and verify the new value.
  name: Keycloak Rotate a Client Secret
  slug: keycloak-rotate-client-secret-workflow
- description: Create a realm-level role if it is missing, update it if it already exists, then read it back.
  name: Keycloak Upsert a Realm Role
  slug: keycloak-upsert-realm-role-workflow
artifact_total: 51
collections:
- collection_type: open
  name: Keycloak Admin REST API
  slug: open-keycloak-admin-rest-api
- collection_type: open
  name: Keycloak Admin REST Clients API
  slug: open-keycloak-clients-api
- collection_type: open
  name: Keycloak Admin REST Clients Groups API
  slug: open-keycloak-groups-api
- collection_type: open
  name: Keycloak Admin REST Clients Identity Providers API
  slug: open-keycloak-identity-providers-api
- collection_type: open
  name: Keycloak Admin REST Clients Realms API
  slug: open-keycloak-realms-api
- collection_type: open
  name: Keycloak Admin REST Clients Roles API
  slug: open-keycloak-roles-api
- collection_type: open
  name: Keycloak Admin REST Clients Users API
  slug: open-keycloak-users-api
common:
- group: commercial
  href: https://artifacts.apis.io/keycloak/plans/keycloak-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/keycloak-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/keycloak/rate-limits/keycloak-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/keycloak-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/keycloak/finops/keycloak-finops.yml
  title: ''
  type: FinOps
  url: finops/keycloak-finops.yml
- group: other
  href: https://artifacts.apis.io/keycloak/capabilities/keycloak-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/keycloak-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/keycloak/vendor-facets/keycloak-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/keycloak-vendor-facets.yml
- group: agent
  href: https://artifacts.apis.io/keycloak/mcp/keycloak-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/keycloak-mcp.yml
- group: other
  href: https://artifacts.apis.io/keycloak/overlays/keycloak-admin-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/keycloak-admin-rest-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-onboard-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-onboard-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-offboard-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-offboard-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-audit-user-access-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-audit-user-access-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-register-oidc-client-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-register-oidc-client-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-rotate-client-secret-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-rotate-client-secret-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-decommission-client-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-decommission-client-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-upsert-realm-role-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-upsert-realm-role-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-provision-group-hierarchy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-provision-group-hierarchy-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-assign-user-to-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-assign-user-to-group-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-audit-group-membership-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-audit-group-membership-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-federate-identity-provider-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-federate-identity-provider-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-harden-realm-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-harden-realm-workflow.yml
- group: design
  href: https://artifacts.apis.io/keycloak/arazzo/keycloak-inventory-realm-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/keycloak-inventory-realm-workflow.yml
- group: agent
  href: https://artifacts.apis.io/keycloak/agentic-access/keycloak-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/keycloak-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/keycloak/packages/keycloak-packages.yml
  title: ''
  type: Packages
  url: packages/keycloak-packages.yml
- group: agent
  href: https://artifacts.apis.io/keycloak/well-known/keycloak-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/keycloak-well-known.yml
- group: auth
  href: https://artifacts.apis.io/keycloak/well-known/keycloak-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/keycloak-security.txt
- group: agent
  href: https://artifacts.apis.io/keycloak/llms/keycloak-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keycloak-llms.txt
- group: design
  href: https://artifacts.apis.io/keycloak/conformance/keycloak-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keycloak-conformance.yml
- group: design
  href: https://artifacts.apis.io/keycloak/lifecycle/keycloak-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/keycloak-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/keycloak/conventions/keycloak-conventions.yml
  title: ''
  type: Conventions
  url: conventions/keycloak-conventions.yml
- group: operate
  href: https://artifacts.apis.io/keycloak/changelog/keycloak-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/keycloak-changelog.yml
- group: build
  href: https://artifacts.apis.io/keycloak/cli/keycloak-cli.yml
  title: ''
  type: CLI
  url: cli/keycloak-cli.yml
- group: auth
  href: https://artifacts.apis.io/keycloak/security/keycloak-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/keycloak-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/keycloak/security/keycloak-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keycloak-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/keycloak/authentication/keycloak-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keycloak-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.keycloak.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.keycloak.org/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://www.keycloak.org/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keycloak/keycloak
- group: company
  title: ''
  type: Blog
  url: https://www.keycloak.org/blog
- group: operate
  title: ''
  type: Community
  url: https://www.keycloak.org/community
created: '2025-01-01'
description: Keycloak is an open source identity and access management solution for modern applications and services, providing single sign-on, identity brokering, user federation, and fine-grained authorization using OAuth 2.0 and OpenID Connect.
finops:
- has_sources: false
  method: generated
  name: Keycloak Finops
  primary_unit: request
  service_category: API
  slug: keycloak-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keycloak.png
layout: provider
modified: '2026-06-20'
name: Keycloak
nav: Providers
network: true
overview: 'Keycloak publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Clients API, Groups API, Identity Providers API, and 20 more. Tagged areas include Authentication, Authorization, Identity and Access Management, OAuth, and OpenID Connect.


  The Keycloak catalog on APIs.io includes 1 Spectral governance ruleset.


  Keycloak''s developer surface includes changelog, CLI, authentication, documentation, getting-started guide, engineering blog, and 33 more developer resources.'
plans:
- name: Keycloak Plans Pricing
  plan_count: 3
  slug: keycloak-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Keycloak Rate Limits
  slug: keycloak-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Keycloak — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: keycloak-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 50.3
    catalog_earned_first_party: 0.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 7.9
    contract_governance: 28.0
    contract_quality: 45.3
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 36.8
  previous_composite: 36.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/keycloak/keycloak-2026-06-20T184004.png
security:
- kind: authentication
  name: Keycloak Authentication
  slug: keycloak-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Keycloak Domain Security
  slug: keycloak-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Keycloak Vulnerability Disclosure
  slug: keycloak-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: keycloak
tags:
- Authentication
- Authorization
- Identity and Access Management
- OAuth
- OpenID Connect
- Security
- SSO
- Identity Federation
website: https://www.keycloak.org/
---
