---
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
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Authenticx Agentic Access
  operation_count: 46
  slug: authenticx-agentic-access
  summary_line: 46 operations · 18 acting
api_count: 18
apis:
- description: The Agent API from Authenticx — 3 operation(s) for agent.
  name: Authenticx Agent API
  slug: authenticx-agent-api
- description: The Conversations API from Authenticx — 4 operation(s) for conversations.
  name: Authenticx Conversations API
  slug: authenticx-conversations-api
- description: The Evaluations API from Authenticx — 2 operation(s) for evaluations.
  name: Authenticx Evaluations API
  slug: authenticx-evaluations-api
- description: The Hierarchy API from Authenticx — 3 operation(s) for hierarchy.
  name: Authenticx Hierarchy API
  slug: authenticx-hierarchy-api
- description: The Interactions API from Authenticx — 2 operation(s) for interactions.
  name: Authenticx Interactions API
  slug: authenticx-interactions-api
- description: The Media API from Authenticx — 1 operation(s) for media.
  name: Authenticx Media API
  slug: authenticx-media-api
- description: The Metadata API from Authenticx — 2 operation(s) for metadata.
  name: Authenticx Metadata API
  slug: authenticx-metadata-api
- description: The ModelResults API from Authenticx — 2 operation(s) for modelresults.
  name: Authenticx Model Results API
  slug: authenticx-modelresults-api
- description: The Receipts API from Authenticx — 1 operation(s) for receipts.
  name: Authenticx Receipts API
  slug: authenticx-receipts-api
- description: The Roles API from Authenticx — 1 operation(s) for roles.
  name: Authenticx Roles API
  slug: authenticx-roles-api
- description: The (Scim) ResourceTypes API from Authenticx — 2 operation(s) for (scim) resourcetypes.
  name: Authenticx (Scim) ResourceTypes API
  slug: authenticx-scim-resourcetypes-api
- description: The (Scim) Schemas API from Authenticx — 2 operation(s) for (scim) schemas.
  name: Authenticx (Scim) Schemas API
  slug: authenticx-scim-schemas-api
- description: The (Scim) ServiceProviderConfig API from Authenticx — 1 operation(s) for (scim) serviceproviderconfig.
  name: Authenticx (Scim) ServiceProviderConfig API
  slug: authenticx-scim-serviceproviderconfig-api
- description: The (Scim) Users API from Authenticx — 2 operation(s) for (scim) users.
  name: Authenticx (Scim) Users API
  slug: authenticx-scim-users-api
- description: The TextMedia API from Authenticx — 1 operation(s) for textmedia.
  name: Authenticx Text Media API
  slug: authenticx-textmedia-api
- description: The User API from Authenticx — 3 operation(s) for user.
  name: Authenticx User API
  slug: authenticx-user-api
- description: The UserHierarchy API from Authenticx — 2 operation(s) for userhierarchy.
  name: Authenticx User Hierarchy API
  slug: authenticx-userhierarchy-api
- description: The Workflows API from Authenticx — 1 operation(s) for workflows.
  name: Authenticx Workflows API
  slug: authenticx-workflows-api
artifact_total: 23
common:
- group: company
  title: ''
  type: Website
  url: https://authenticx.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://authenticx.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://authenticx.readme.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://authenticx.readme.io/reference/acxapi
- group: start
  title: ''
  type: GettingStarted
  url: https://authenticx.readme.io/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://authenticx.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beacx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://authenticx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://authenticx.com/privacy
- group: start
  title: ''
  type: Login
  url: https://app.beauthenticx.com/
- group: auth
  title: ''
  type: Compliance
  url: https://authenticx.com/privacy-security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/authenticx-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/authenticx-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://api.beauthenticx.com/.well-known/openid-configuration
- group: auth
  title: ''
  type: Authentication
  url: authentication/authenticx-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/authenticx-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/authenticx-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/authenticx-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/authenticx-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/authenticx-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/authenticx-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/authenticx-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/authenticx-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/authenticx-acxapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/authenticx-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/authenticx-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/authenticx-domain-security.yml
created: '2026-08-06'
description: Authenticx is a healthcare conversation intelligence platform that ingests contact-center interactions — call audio, chat transcripts, and email — and applies speech analytics and machine-learning classifiers to surface patient and member experience signals, quality-assurance scoring, and pharmacovigilance / adverse-event detection. Its AcxAPI is a REST API described by a live OpenAPI 3.0.1 definition covering conversation insights, transcriptions, model results, evaluations, metadata, workflows, audio and text media upload, agent, hierarchy and role administration, and SCIM 2.0 user provisioning. Interaction ingestion also runs through out-of-the-box connectors for Genesys Cloud, Amazon Connect, NICE CXone, Five9, Vonage Contact Center and Talkdesk, plus Salesforce/MuleSoft conversation enrichment and SFTP batch delivery. Authentication is OAuth 2.0 client credentials against an OpenID Connect provider, with separate production and experimental (staging) hosts.
image: https://files.readme.io/e7477e0-small-authenticx-logo-black.png
layout: provider
mcp_servers:
- description: ''
  name: authenticx-mcp.yml
  slug: authenticx-mcpyml
modified: '2026-08-06'
name: Authenticx
nav: Providers
network: true
overview: 'Authenticx publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Conversations API, Evaluations API, and 15 more. Tagged areas include conversation-intelligence, healthcare, speech-analytics, contact-center, and customer-experience.


  Authenticx''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, sandbox, and 22 more developer resources.'
random_paper: 41
scopes:
- name: Authenticx Scopes
  scope_count: 1
  slug: authenticx-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 48.0
  delta: -0.2
  facets:
    commercial_clarity: 42.1
    contract_quality: 54.4
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/authenticx/refs/heads/main/screenshots/authenticx-2026-08-07T161942.png
security:
- kind: authentication
  name: Authenticx Authentication
  slug: authenticx-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Authenticx Domain Security
  slug: authenticx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: authenticx
tags:
- conversation-intelligence
- healthcare
- speech-analytics
- contact-center
- customer-experience
- quality-assurance
- pharmacovigilance
- patient-experience
- transcription
- life-sciences
- scim
- oauth2
website: https://authenticx.com/
---
