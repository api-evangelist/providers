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
    error_semantics: documented
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
  score: 22.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Keycloak Agentic Access
  operation_count: 40
  slug: keycloak-agentic-access
  summary_line: 40 operations · 24 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Manage OAuth/OIDC clients within a realm
  name: Keycloak Clients API
  slug: keycloak-clients-api
- description: Manage user groups within a realm
  name: Keycloak Groups API
  slug: keycloak-groups-api
- description: Manage identity providers for federated authentication
  name: Keycloak Identity Providers API
  slug: keycloak-identity-providers-api
- description: Manage Keycloak realms
  name: Keycloak Realms API
  slug: keycloak-realms-api
- description: Manage realm-level and client-level roles
  name: Keycloak Roles API
  slug: keycloak-roles-api
- description: Manage users within a realm
  name: Keycloak Users API
  slug: keycloak-users-api
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
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: MCPServer
  url: mcp/keycloak-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/keycloak-admin-rest-api-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-onboard-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-offboard-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-audit-user-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-register-oidc-client-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-rotate-client-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-decommission-client-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-upsert-realm-role-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-provision-group-hierarchy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-assign-user-to-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-audit-group-membership-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-federate-identity-provider-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-harden-realm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/keycloak-inventory-realm-workflow.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keycloak-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/keycloak-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/keycloak-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/keycloak-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keycloak-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/keycloak-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/keycloak-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/keycloak-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/keycloak-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/keycloak-cli.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/keycloak-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keycloak-domain-security.yml
- group: auth
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
- name: Keycloak Finops
  service_category: API
  slug: keycloak-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keycloak.png
layout: provider
mcp_servers:
- description: ''
  name: Keycloak MCP Server
  slug: keycloak-mcp-server
modified: '2026-06-20'
name: Keycloak
nav: Providers
network: true
overview: 'Keycloak publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Groups API, Identity Providers API, and 3 more. Tagged areas include Authentication, Authorization, Identity Management, OpenID Connect, and Security.


  The Keycloak catalog on APIs.io includes 1 Spectral governance ruleset.


  Keycloak''s developer surface includes changelog, CLI, authentication, documentation, getting-started guide, engineering blog, and 28 more developer resources.'
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
- effective_rule_count: 5
  extends: []
  name: Keycloak API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: keycloak-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 26
    catalog_gap: 60.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.0
    contract_quality: 53.9
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 28.0
    operational_transparency: 26.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keycloak/refs/heads/main/screenshots/keycloak-2026-06-20T184004.png
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
- Identity Management
- OpenID Connect
- Security
- SSO
website: https://www.keycloak.org/
---
