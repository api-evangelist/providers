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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Jumpcloud Agentic Access
  operation_count: 13
  slug: jumpcloud-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- description: REST API for managing core directory resources including users, systems, system users, tags, commands, policies, and SSO applications. Uses API key authentication via the x-api-key header.
  name: JumpCloud API V1
  slug: v1-api
- description: REST API V2 for managing groups, group memberships, associations, directory insights, system insights, organizations, and modern policies. Uses API key authentication via the x-api-key header.
  name: JumpCloud API V2
  slug: v2-api
- description: API for managed systems to interact with JumpCloud on their own behalf using HTTP Signatures authentication. Used for system-initiated actions such as user provisioning and event reporting.
  name: JumpCloud System Context API
  slug: system-context-api
- description: SSO/SAML application templates available for use.
  name: JumpCloud Application Templates API
  slug: jumpcloud-application-templates-api
- description: SSO/SAML applications configured in the organization.
  name: JumpCloud Applications API
  slug: jumpcloud-applications-api
- description: Execution results produced by commands run against systems.
  name: JumpCloud Command Results API
  slug: jumpcloud-command-results-api
- description: Commands that can be executed across managed systems.
  name: JumpCloud Commands API
  slug: jumpcloud-commands-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: JumpCloud API V1 Application Templates API
  slug: open-jumpcloud-application-templates-api
- collection_type: open
  name: JumpCloud API V1 Application Templates Applications API
  slug: open-jumpcloud-applications-api
- collection_type: open
  name: JumpCloud API V1 Application Templates Command Results API
  slug: open-jumpcloud-command-results-api
- collection_type: open
  name: JumpCloud API V1 Application Templates Commands API
  slug: open-jumpcloud-commands-api
- collection_type: open
  name: JumpCloud API V1
  slug: open-jumpcloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jumpcloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jumpcloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jumpcloud-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jumpcloud
- group: company
  title: ''
  type: Website
  url: https://jumpcloud.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jumpcloud.com
- group: operate
  title: ''
  type: Support
  url: https://jumpcloud.com/support
- group: start
  title: ''
  type: Signup
  url: https://console.jumpcloud.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://jumpcloud.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheJumpCloud
- group: agent
  title: ''
  type: LlmsText
  url: https://jumpcloud.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://jumpcloud.com/blog/feed
created: '2026-05-11'
description: JumpCloud is an open directory platform that unifies identity, access, and device management across users, devices, networks, and SaaS applications. Its cloud directory supports SSO, MFA, device management (MDM), conditional access policies, RADIUS, LDAP, and HR system integration. JumpCloud's REST APIs (V1 and V2) provide programmatic access to users, groups, systems, policies, applications, and directory insights for IT automation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jumpcloud.png
layout: provider
modified: '2026-05-11'
name: JumpCloud
nav: Providers
network: true
overview: 'JumpCloud publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Application Templates API, Applications API, Command Results API, and 1 more. Tagged areas include Identity, Directory Services, SSO, MFA, and Device Management.


  JumpCloud''s developer surface includes authentication, documentation, support, signup flow, pricing, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 8
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 28.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jumpcloud/refs/heads/main/screenshots/jumpcloud-2026-06-20T183831.png
security:
- kind: authentication
  name: Jumpcloud Authentication
  slug: jumpcloud-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jumpcloud Domain Security
  slug: jumpcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jumpcloud
tags:
- Identity
- Directory Services
- SSO
- MFA
- Device Management
- MDM
- IT Operations
- Zero Trust
website: https://jumpcloud.com
---
