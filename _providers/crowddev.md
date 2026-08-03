---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Crowddev Agentic Access
  operation_count: 56
  slug: crowddev-agentic-access
  summary_line: 56 operations · 28 acting · 1 human-in-the-loop
api_count: 16
apis:
- description: 'Security advisories for a package, split out of package detail. The draft contract gates these behind a dedicated read:advisories scope; until Auth0 issues it, the implementation reuses read:packages '
  name: Crowd.dev Advisories API
  slug: crowddev-advisories-api
- description: Bulk contributor affiliation lookups by GitHub handle.
  name: Crowd.dev Affiliations API
  slug: crowddev-affiliations-api
- description: 'Security contacts for a package — includes contact PII (e.g. reporter emails). The contract gates these behind a dedicated cdp:maintainers:read scope and forbids reaching them via the packages scope; '
  name: Crowd.dev Contacts API
  slug: crowddev-contacts-api
- description: KPI bar metrics and activity feed.
  name: Crowd.dev Dashboard API
  slug: crowddev-dashboard-api
- description: Retrieve maintainer roles for a member.
  name: Crowd.dev Maintainer Roles API
  slug: crowddev-maintainer-roles-api
- description: API endpoints for managing project affiliations, including listing and bulk updating affiliation relationships within a profile.
  name: Crowd.dev Member Affiliations API API
  slug: crowddev-member-affiliations-api-api
- description: Manage and verify member identities across platforms.
  name: Crowd.dev Member Identities API
  slug: crowddev-member-identities-api
- description: API endpoints for managing work history organizations, including creating, reading, updating, and deleting organization relationships for profiles.
  name: Crowd.dev Member Organizations API API
  slug: crowddev-member-organizations-api-api
- description: Resolve member profiles by identity.
  name: Crowd.dev Members API
  slug: crowddev-members-api
- description: Look up and create organizations.
  name: Crowd.dev Organizations API
  slug: crowddev-organizations-api
- description: Package detail — requires read:packages and read:stewardships (see TODO above).
  name: Crowd.dev Packages API
  slug: crowddev-packages-api
- description: View and override per-project affiliation data for a member.
  name: Crowd.dev Project Affiliations API
  slug: crowddev-project-affiliations-api
- description: Admin-initiated stewardship mutations.
  name: Crowd.dev Stewardship Actions API
  slug: crowddev-stewardship-actions-api
- description: Stewardship state — individual and batch.
  name: Crowd.dev Stewardship API
  slug: crowddev-stewardship-api
- description: Open, assign, escalate, and update stewardship status.
  name: Crowd.dev Stewardships API
  slug: crowddev-stewardships-api
- description: Manage and verify member work experiences (organization affiliations).
  name: Crowd.dev Work Experiences API
  slug: crowddev-work-experiences-api
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crowddev-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crowddev-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/crowddev-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crowddev-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://crowd.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.crowd.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crowd.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.crowd.dev/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.crowd.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CrowdDotDev
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/linuxfoundation/crowd.dev
- group: commercial
  title: ''
  type: License
  url: https://github.com/linuxfoundation/crowd.dev/blob/main/LICENSE
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lfx.dev
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crowddev-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crowddev-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crowddev-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crowddev-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crowddev-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crowddev-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/crowddev-cdp-public-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crowddev-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crowddev-changelog.yml
created: '2026-07-17'
description: Crowd.dev is an open-source developer data platform that centralizes community, product, and commercial data to unify contributor identities, resolve who is engaging with an open-source project, and activate that data for developer relations and community-led growth. Founded in Berlin and backed by Seedcamp, crowd.dev was acquired by the Linux Foundation in April 2024 and now powers the LFX Community Data Platform (CDP). The codebase is Apache-2.0 open source at github.com/CrowdDotDev (now linuxfoundation/crowd.dev), and the CDP Public API exposes transactional REST endpoints for member and organization profiles, identity verification, work-experience and project-affiliation management, contributor affiliation lookups, and open-source package/stewardship intelligence.
image: https://avatars.githubusercontent.com/u/85551972?v=4
layout: provider
mcp_servers:
- description: ''
  name: crowddev-mcp.yml
  slug: crowddev-mcpyml
modified: '2026-07-18'
name: Crowd.dev
nav: Providers
network: true
overview: 'Crowd.dev publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Advisories API, Affiliations API, Contacts API, and 13 more. Tagged areas include Company, Community, Developer Relations, Developer Data Platform, and Identity Resolution.


  Crowd.dev''s developer surface includes authentication, documentation, API reference, changelog, and 19 more developer resources.'
random_paper: 7
scopes:
- name: Crowddev Scopes
  scope_count: 13
  slug: crowddev-scopes
  summary_line: 13 scopes · clientCredentials
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 60.9
    developer_ergonomics: 38.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crowddev/refs/heads/main/screenshots/crowddev-2026-07-25T210805.png
security:
- kind: authentication
  name: Crowddev Authentication
  slug: crowddev-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Crowddev Domain Security
  slug: crowddev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crowddev
tags:
- Company
- Community
- Developer Relations
- Developer Data Platform
- Identity Resolution
- Open Source
- Community Data Platform
- Open Source Intelligence
website: https://crowd.dev
---
