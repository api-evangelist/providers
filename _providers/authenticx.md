---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Authenticx Agentic Access
  operation_count: 46
  slug: authenticx-agentic-access
  summary_line: 46 operations · 18 acting
api_count: 3
apis:
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Agent API from Authenticx — 3 operation(s) for agent.
  name: Authenticx Agent API
  slug: authenticx-agent-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Conversations API from Authenticx — 4 operation(s) for conversations.
  name: Authenticx Conversations API
  slug: authenticx-conversations-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Evaluations API from Authenticx — 2 operation(s) for evaluations.
  name: Authenticx Evaluations API
  slug: authenticx-evaluations-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Hierarchy API from Authenticx — 3 operation(s) for hierarchy.
  name: Authenticx Hierarchy API
  slug: authenticx-hierarchy-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Interactions API from Authenticx — 2 operation(s) for interactions.
  name: Authenticx Interactions API
  slug: authenticx-interactions-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Media API from Authenticx — 1 operation(s) for media.
  name: Authenticx Media API
  slug: authenticx-media-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Metadata API from Authenticx — 2 operation(s) for metadata.
  name: Authenticx Metadata API
  slug: authenticx-metadata-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The ModelResults API from Authenticx — 2 operation(s) for modelresults.
  name: Authenticx Model Results API
  slug: authenticx-modelresults-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Receipts API from Authenticx — 1 operation(s) for receipts.
  name: Authenticx Receipts API
  slug: authenticx-receipts-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Roles API from Authenticx — 1 operation(s) for roles.
  name: Authenticx Roles API
  slug: authenticx-roles-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The (Scim) ResourceTypes API from Authenticx — 2 operation(s) for (scim) resourcetypes.
  name: Authenticx (Scim) ResourceTypes API
  slug: authenticx-scim-resourcetypes-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The (Scim) Schemas API from Authenticx — 2 operation(s) for (scim) schemas.
  name: Authenticx (Scim) Schemas API
  slug: authenticx-scim-schemas-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The (Scim) ServiceProviderConfig API from Authenticx — 1 operation(s) for (scim) serviceproviderconfig.
  name: Authenticx (Scim) ServiceProviderConfig API
  slug: authenticx-scim-serviceproviderconfig-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The (Scim) Users API from Authenticx — 2 operation(s) for (scim) users.
  name: Authenticx (Scim) Users API
  slug: authenticx-scim-users-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The TextMedia API from Authenticx — 1 operation(s) for textmedia.
  name: Authenticx Text Media API
  slug: authenticx-textmedia-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The User API from Authenticx — 3 operation(s) for user.
  name: Authenticx User API
  slug: authenticx-user-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The UserHierarchy API from Authenticx — 2 operation(s) for userhierarchy.
  name: Authenticx User Hierarchy API
  slug: authenticx-userhierarchy-api
- baseURL: https://api.beauthenticx.com
  baseurl_source: declared
  description: The Workflows API from Authenticx — 1 operation(s) for workflows.
  name: Authenticx Workflows API
  slug: authenticx-workflows-api
artifact_total: 45
asyncapis:
- description: ''
  name: Authenticx Emissions Webhooks
  slug: authenticx-emissions-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AcxApi Production Agent API
  slug: open-authenticx-agent-api
- collection_type: open
  name: AcxApi Production Conversations API
  slug: open-authenticx-conversations-api
- collection_type: open
  name: AcxApi Production Evaluations API
  slug: open-authenticx-evaluations-api
- collection_type: open
  name: AcxApi Production Hierarchy API
  slug: open-authenticx-hierarchy-api
- collection_type: open
  name: AcxApi Production Interactions API
  slug: open-authenticx-interactions-api
- collection_type: open
  name: AcxApi Production Media API
  slug: open-authenticx-media-api
- collection_type: open
  name: AcxApi Production Metadata API
  slug: open-authenticx-metadata-api
- collection_type: open
  name: AcxApi Production Model Results API
  slug: open-authenticx-modelresults-api
- collection_type: open
  name: AcxApi Production Receipts API
  slug: open-authenticx-receipts-api
- collection_type: open
  name: AcxApi Production Roles API
  slug: open-authenticx-roles-api
- collection_type: open
  name: AcxApi Production (Scim) ResourceTypes (Scim) ResourceTypes API
  slug: open-authenticx-scim-resourcetypes-api
- collection_type: open
  name: AcxApi Production (Scim) Schemas (Scim) Schemas API
  slug: open-authenticx-scim-schemas-api
- collection_type: open
  name: AcxApi Production (Scim) ServiceProviderConfig (Scim) ServiceProviderConfig API
  slug: open-authenticx-scim-serviceproviderconfig-api
- collection_type: open
  name: AcxApi Production (Scim) Users (Scim) Users API
  slug: open-authenticx-scim-users-api
- collection_type: open
  name: AcxApi Production Text Media API
  slug: open-authenticx-textmedia-api
- collection_type: open
  name: AcxApi Production User API
  slug: open-authenticx-user-api
- collection_type: open
  name: AcxApi Production User Hierarchy API
  slug: open-authenticx-userhierarchy-api
- collection_type: open
  name: AcxApi Production Workflows API
  slug: open-authenticx-workflows-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/authenticx-capability-edges.yml
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
  type: X-MCPServerCandidate
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
- group: auth
  title: ''
  type: TrustCenter
  url: https://authenticx.com/privacy-security
- group: commercial
  title: ''
  type: Plans
  url: plans/authenticx-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/authenticx-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/authenticx-emissions-webhooks.yml
created: '2026-08-06'
description: Authenticx is a healthcare conversation intelligence platform that ingests contact-center interactions — call audio, chat transcripts, and email — and applies speech analytics and machine-learning classifiers to surface patient and member experience signals, quality-assurance scoring, and pharmacovigilance / adverse-event detection. Its AcxAPI is a REST API described by a live OpenAPI 3.0.1 definition covering conversation insights, transcriptions, model results, evaluations, metadata, workflows, audio and text media upload, agent, hierarchy and role administration, and SCIM 2.0 user provisioning. Interaction ingestion also runs through out-of-the-box connectors for Genesys Cloud, Amazon Connect, NICE CXone, Five9, Vonage Contact Center and Talkdesk, plus Salesforce/MuleSoft conversation enrichment and SFTP batch delivery. Authentication is OAuth 2.0 client credentials against an OpenID Connect provider, with separate production and experimental (staging) hosts.
image: https://files.readme.io/e7477e0-small-authenticx-logo-black.png
layout: provider
modified: '2026-08-14'
name: Authenticx
nav: Providers
network: true
overview: 'Authenticx publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Conversations API, Evaluations API, and 15 more. Tagged areas include Conversation Intelligence, Healthcare, Speech Analytics, Contact Center, and Customer Experience.


  The Authenticx catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Authenticx''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, sandbox, and 27 more developer resources.'
plans:
- name: Authenticx Plans Pricing
  plan_count: 0
  slug: authenticx-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Authenticx Rate Limits
  slug: authenticx-rate-limits
scopes:
- name: Authenticx Scopes
  scope_count: 1
  slug: authenticx-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 52.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 64.7
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- kind: trust-center
  name: Authenticx Trust Center
  slug: authenticx-trust-center
  summary_line: SOC 2 Type I & II, HIPAA, GDPR, CCPA
slug: authenticx
tags:
- Conversation Intelligence
- Healthcare
- Speech Analytics
- Contact Center
- Customer Experience
- Quality Assurance
- Pharmacovigilance
- Patient Experience
- Transcription
- Life Sciences
- SCIM
- Authentication
website: https://authenticx.com/
---
