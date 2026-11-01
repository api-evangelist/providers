---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 244
  human_in_the_loop: 12
  name: Vertesiahq Agentic Access
  operation_count: 473
  slug: vertesiahq-agentic-access
  summary_line: 473 operations · 244 acting · 12 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Access Control Entry endpoints manage account-, project-, and app-level role assignments for users, groups, and API keys.
  name: Vertesia Access Control Entries API
  slug: vertesiahq-access-control-entries-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Account API from Vertesia — 2 operation(s) for account.
  name: Vertesia Account API
  slug: vertesiahq-account-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Account endpoints manage the current account, account membership, invites, onboarding state, and account-scoped integrations.
  name: Vertesia Accounts API
  slug: vertesiahq-accounts-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Agent runs are long-running conversational workflow executions with stable IDs, message streams, artifacts, child workflow inspection, lifecycle controls, and searchable metadata.
  name: Vertesia Agent Runs API
  slug: vertesiahq-agent-runs-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: API Key endpoints manage project and account API credentials used to authenticate automation and external clients.
  name: Vertesia API Keys API
  slug: vertesiahq-api-keys-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: App endpoints manage app manifests, project installations, installation settings, and installation-scoped tool visibility.
  name: Vertesia Apps API
  slug: vertesiahq-apps-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Audit Trail endpoints expose account and project audit events for administrative review and investigation.
  name: Vertesia Audit Trail API
  slug: vertesiahq-audit-trail-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Bulk Operation endpoints create, update, delete, or retag many content objects in a single request.
  name: Vertesia Bulk Operations API
  slug: vertesiahq-bulk-operations-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Collections organize content objects into searchable groups. Collections can be static or dynamic and can carry ACLs, child collections, and shared-property synchronization rules.
  name: Vertesia Collections API
  slug: vertesiahq-collections-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Command endpoints control project embeddings, Elasticsearch indexing, and operational content maintenance flows such as synchronous migrations.
  name: Vertesia Commands API
  slug: vertesiahq-commands-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Content object types define schema, layout, and metadata structure for content objects.
  name: Vertesia Content Object Types API
  slug: vertesiahq-content-object-types-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Content Query API from Vertesia — 1 operation(s) for content query.
  name: Vertesia Content Query API
  slug: vertesiahq-content-query-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Cost endpoints expose billing analytics, model pricing, and run-level metering for project and account usage.
  name: Vertesia Costs API
  slug: vertesiahq-costs-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Data endpoints manage versioned project data stores, SQL schema evolution, imports, snapshots, queries, and dashboards.
  name: Vertesia Data API
  slug: vertesiahq-data-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Delegation Grants API from Vertesia — 4 operation(s) for delegation grants.
  name: Vertesia Delegation Grants API
  slug: vertesiahq-delegation-grants-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Email API from Vertesia — 4 operation(s) for email.
  name: Vertesia Email API
  slug: vertesiahq-email-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Environments configure model providers, endpoints, credentials, enabled models, and provider-specific execution settings. Use these endpoints to list, create, update, inspect, and operate model enviro
  name: Vertesia Environments API
  slug: vertesiahq-environments-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Event Ingest Channels API from Vertesia — 2 operation(s) for event ingest channels.
  name: Vertesia Event Ingest Channels API
  slug: vertesiahq-event-ingest-channels-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Event Subscriptions API from Vertesia — 2 operation(s) for event subscriptions.
  name: Vertesia Event Subscriptions API
  slug: vertesiahq-event-subscriptions-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Events API from Vertesia — 4 operation(s) for events.
  name: Vertesia Events API
  slug: vertesiahq-events-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: File endpoints manage project-scoped object storage, including signed upload and download URLs, metadata updates, copies, and deletes.
  name: Vertesia Files API
  slug: vertesiahq-files-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Inference Profiles API from Vertesia — 3 operation(s) for inference profiles.
  name: Vertesia Inference Profiles API
  slug: vertesiahq-inference-profiles-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The `/runs` endpoints manage interaction execution records. Every interaction execution, whether synchronous, asynchronous, conversation-based, streamed, or batch, creates a run that tracks its input,
  name: Vertesia Interaction Runs API
  slug: vertesiahq-interaction-runs-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Interactions define executable GenAI tasks. Use these endpoints to create drafts, inspect and update definitions, publish immutable versions, fork interactions, resolve executable environment and mode
  name: Vertesia Interactions API
  slug: vertesiahq-interactions-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The OAuth API from Vertesia — 2 operation(s) for oauth.
  name: Vertesia OAuth API
  slug: vertesiahq-oauth-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: OAuth Client endpoints manage clients registered against the built-in OAuth server.
  name: Vertesia OAuth Clients API
  slug: vertesiahq-oauth-clients-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: OAuth Grant endpoints list granted OAuth access, inspect grant details, and revoke one or more OAuth grants.
  name: Vertesia OAuth Grants API
  slug: vertesiahq-oauth-grants-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: OAuth Provider endpoints manage project-scoped OAuth providers and the associated authorization flows and token lifecycle.
  name: Vertesia OAuth Providers API
  slug: vertesiahq-oauth-providers-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Content objects represent documents, files, images, and extracted data stored in Vertesia Content. Use these endpoints to search and retrieve content records for downstream processing and retrieval wo
  name: Vertesia Objects API
  slug: vertesiahq-objects-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The OIDC Federation API from Vertesia — 2 operation(s) for oidc federation.
  name: Vertesia OIDC Federation API
  slug: vertesiahq-oidc-federation-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Pending Asks API from Vertesia — 3 operation(s) for pending asks.
  name: Vertesia Pending Asks API
  slug: vertesiahq-pending-asks-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Process endpoints manage versioned process definitions, revisions, publishing, rollback, and isolated process test suites and test runs.
  name: Vertesia Processes API
  slug: vertesiahq-processes-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Project endpoints manage project records, configuration, integrations, enabled plugins, and project-scoped app assets.
  name: Vertesia Projects API
  slug: vertesiahq-projects-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Prompts are reusable template segments used by interactions. Use these endpoints to create draft prompts, update prompt content and schemas, inspect published versions, find interactions that use a pr
  name: Vertesia Prompt Templates API
  slug: vertesiahq-prompt-templates-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Quota API from Vertesia — 2 operation(s) for quota.
  name: Vertesia Quota API
  slug: vertesiahq-quota-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Remote MCP Connection endpoints manage OAuth discovery, authorization, connection status, and token access for third-party MCP tool collections installed through apps.
  name: Vertesia Remote MCP Connections API
  slug: vertesiahq-remote-mcp-connections-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Rendering endpoints convert markdown content or stored objects into rendered artifacts such as PDF and DOCX files through asynchronous workflows.
  name: Vertesia Rendering API
  slug: vertesiahq-rendering-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Role endpoints expose the built-in Vertesia role catalog and the permissions granted by each role.
  name: Vertesia Roles API
  slug: vertesiahq-roles-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Secrets API from Vertesia — 3 operation(s) for secrets.
  name: Vertesia Secrets API
  slug: vertesiahq-secrets-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Task endpoints manage durable human tasks used by process runs and agent asks.
  name: Vertesia Tasks API
  slug: vertesiahq-tasks-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Security Token Service endpoints issue short-lived project, user, environment, service-account, and agent tokens.
  name: Vertesia Token Service API
  slug: vertesiahq-token-service-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Tools API from Vertesia — 3 operation(s) for tools.
  name: Vertesia Tools API
  slug: vertesiahq-tools-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: User Group endpoints manage account-level groups and their membership for access control and app visibility.
  name: Vertesia User Groups API
  slug: vertesiahq-user-groups-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: User endpoints retrieve, update, and delete account members within the current account context.
  name: Vertesia Users API
  slug: vertesiahq-users-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: The Views API from Vertesia — 4 operation(s) for views.
  name: Vertesia Views API
  slug: vertesiahq-views-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Workflow definitions describe reusable DSL workflows and their activity graph.
  name: Vertesia Workflow Definitions API
  slug: vertesiahq-workflow-definitions-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Workflow rules bind named endpoints and execution defaults to workflow definitions so they can be triggered consistently.
  name: Vertesia Workflow Rules API
  slug: vertesiahq-workflow-rules-api
- baseURL: https://api.us1.vertesia.io/api/v1
  baseurl_source: declared
  description: Workflow run endpoints start workflows, inspect execution state, stream updates, and apply runtime actions such as signaling or cancellation.
  name: Vertesia Workflow Runs API
  slug: vertesiahq-workflow-runs-api
artifact_total: 66
asyncapis:
- description: ''
  name: Vertesiahq Webhooks
  slug: vertesiahq-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/vertesiahq/well-known/vertesiahq-vertesia-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vertesiahq-vertesia-security.txt
- group: agent
  href: https://artifacts.apis.io/vertesiahq/agentic-access/vertesiahq-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vertesiahq-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/vertesiahq/rules/vertesiahq-rules.yml
  title: ''
  type: Spectral
  url: rules/vertesiahq-rules.yml
- group: design
  href: https://artifacts.apis.io/vertesiahq/json-ld/vertesiahq-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vertesiahq-context.jsonld
- group: design
  href: https://artifacts.apis.io/vertesiahq/vocabulary/vertesiahq-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vertesiahq-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/vertesiahq/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/vertesiahq/asyncapi/vertesiahq-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vertesiahq-webhooks.yml
- group: design
  href: https://artifacts.apis.io/vertesiahq/data-model/vertesiahq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vertesiahq-data-model.yml
- group: operate
  href: https://artifacts.apis.io/vertesiahq/changelog/vertesiahq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vertesiahq-changelog.yml
- group: design
  href: https://artifacts.apis.io/vertesiahq/conventions/vertesiahq-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/vertesiahq-conventions.yml
- group: design
  href: https://artifacts.apis.io/vertesiahq/conventions/vertesiahq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vertesiahq-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://vertesiahq.com/security
- group: design
  href: https://artifacts.apis.io/vertesiahq/errors/vertesiahq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vertesiahq-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vertesiahq/conformance/vertesiahq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vertesiahq-conformance.yml
- group: agent
  href: https://artifacts.apis.io/vertesiahq/llms/vertesiahq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vertesiahq-llms.txt
- group: auth
  href: https://artifacts.apis.io/vertesiahq/well-known/vertesiahq-aws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vertesiahq-aws-security.txt
- group: agent
  href: https://artifacts.apis.io/vertesiahq/well-known/vertesiahq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vertesiahq-well-known.yml
- group: other
  href: https://artifacts.apis.io/vertesiahq/hosts/vertesiahq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vertesiahq-hosts.yml
- group: other
  href: https://artifacts.apis.io/vertesiahq/vendors/vertesiahq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vertesiahq-vendors.yml
- group: build
  href: https://artifacts.apis.io/vertesiahq/packages/vertesiahq-packages.yml
  title: ''
  type: SDKs
  url: packages/vertesiahq-packages.yml
- group: build
  href: https://artifacts.apis.io/vertesiahq/packages/vertesiahq-packages.yml
  title: ''
  type: Packages
  url: packages/vertesiahq-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vertesiahq.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.vertesiahq.com/
- group: operate
  title: ''
  type: StatusPage
  url: http://vertesia.statuspage.io/
- group: auth
  title: ''
  type: Security
  url: https://vertesiahq.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vertesiahq.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://vertesiahq.com/about/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vertesia
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.vertesiahq.com/release-notes
- group: company
  title: ''
  type: Blog
  url: https://vertesiahq.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vertesiahq.com/
- group: auth
  href: https://artifacts.apis.io/vertesiahq/scopes/vertesiahq-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vertesiahq-scopes.yml
- group: auth
  href: https://artifacts.apis.io/vertesiahq/authentication/vertesiahq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vertesiahq-authentication.yml
- group: auth
  href: https://artifacts.apis.io/vertesiahq/security/vertesiahq-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vertesiahq-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vertesiahq/security/vertesiahq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vertesiahq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vertesiahq.com/
created: '2026-10-21'
description: Vertesia provides a comprehensive platform for managing and optimizing digital experiences, offering tools for content delivery, performance monitoring, and user engagement analytics. The company focuses on helping enterprises streamline their online presence, improve load times, and gain actionable insights through real-time data. Vertesia’s solutions are built on a scalable architecture that supports high traffic volumes and integrates with existing tech stacks, enabling businesses to deliver seamless experiences across web and mobile channels. With a commitment to security, compliance, and continuous innovation, Vertesia empowers organizations to stay ahead in the competitive digital landscape.
image: https://vertesiahq.com/hubfs/Vertesia-Featured-Image.jpg
json_schemas:
- name: AgentRun
  property_count: 55
  slug: vertesiahq-agent-run
- name: AppManifestData
  property_count: 24
  slug: vertesiahq-app-manifest-data
- name: AppManifest
  property_count: 29
  slug: vertesiahq-app-manifest
- name: Dashboard
  property_count: 26
  slug: vertesiahq-dashboard
- name: IndexingStatusResponse
  property_count: 9
  slug: vertesiahq-indexing-status-response
- name: UpdateAppPayload
  property_count: 25
  slug: vertesiahq-update-app-payload
jsonld:
- class_count: 120
  name: Vertesiahq Context
  property_count: 424
  slug: vertesiahq-context
layout: provider
modified: '2026-10-21'
name: Vertesia
nav: Providers
network: true
overview: 'Vertesia publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Control Entries API, Account API, Accounts API, and 45 more. Tagged areas include Company, Digital Experience, Performance Monitoring, Analytics, and Content Delivery.


  The Vertesia catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Vertesia''s developer surface includes changelog, support, engineering blog, documentation, authentication, and 31 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Vertesia API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 2
  slug: vertesiahq-rules
scopes:
- name: Vertesiahq Scopes
  scope_count: 33
  slug: vertesiahq-scopes
  summary_line: 33 scopes · authorizationCode
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 76.0
    developer_ergonomics: 37.5
    discoverability: 67.9
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Vertesiahq Authentication
  slug: vertesiahq-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Vertesiahq Domain Security
  slug: vertesiahq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Vertesiahq Trust Center
  slug: vertesiahq-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP, GDPR
skill_count: 4
skills:
- name: vertesiahq-create-and-publish-interaction
  slug: vertesiahq-create-and-publish-interaction
- name: vertesiahq-event-delivery-management
  slug: vertesiahq-event-delivery-management
- name: vertesiahq-upload-and-set-text
  slug: vertesiahq-upload-and-set-text
- name: vertesiahq-view-account-details
  slug: vertesiahq-view-account-details
slug: vertesiahq
tags:
- Company
- Digital Experience
- Performance Monitoring
- Analytics
- Content Delivery
website: https://vertesiahq.com/
---
