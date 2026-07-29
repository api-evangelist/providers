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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Verato Agentic Access
  operation_count: 50
  slug: verato-agentic-access
  summary_line: 50 operations · 50 acting
api_count: 20
apis:
- description: The AddRelationshipService API from Verato — 1 operation(s) for addrelationshipservice.
  name: Verato AddRelationshipService API
  slug: verato-addrelationshipservice-api
- description: The CreateDataSource API from Verato — 1 operation(s) for createdatasource.
  name: Verato CreateDataSource API
  slug: verato-createdatasource-api
- description: The DeactivateSourceWs API from Verato — 1 operation(s) for deactivatesourcews.
  name: Verato DeactivateSourceWs API
  slug: verato-deactivatesourcews-api
- description: The DeleteRelationshipService API from Verato — 1 operation(s) for deleterelationshipservice.
  name: Verato DeleteRelationshipService API
  slug: verato-deleterelationshipservice-api
- description: The DeleteSourceIdentity API from Verato — 1 operation(s) for deletesourceidentity.
  name: Verato DeleteSourceIdentity API
  slug: verato-deletesourceidentity-api
- description: The DemographicsQuery API from Verato — 2 operation(s) for demographicsquery.
  name: Verato DemographicsQuery API
  slug: verato-demographicsquery-api
- description: The DemographicsSearch API from Verato — 2 operation(s) for demographicssearch.
  name: Verato DemographicsSearch API
  slug: verato-demographicssearch-api
- description: The HouseholdQuery API from Verato — 1 operation(s) for householdquery.
  name: Verato HouseholdQuery API
  slug: verato-householdquery-api
- description: The IdentityIdQuery API from Verato — 2 operation(s) for identityidquery.
  name: Verato IdentityIdQuery API
  slug: verato-identityidquery-api
- description: The LinkIdentities API from Verato — 1 operation(s) for linkidentities.
  name: Verato LinkIdentities API
  slug: verato-linkidentities-api
- description: The MergeIdentities API from Verato — 1 operation(s) for mergeidentities.
  name: Verato MergeIdentities API
  slug: verato-mergeidentities-api
- description: The NativeIdQuery API from Verato — 2 operation(s) for nativeidquery.
  name: Verato NativeIdQuery API
  slug: verato-nativeidquery-api
- description: The PostIdentity API from Verato — 2 operation(s) for postidentity.
  name: Verato PostIdentity API
  slug: verato-postidentity-api
- description: The ReactivateSourceWs API from Verato — 1 operation(s) for reactivatesourcews.
  name: Verato ReactivateSourceWs API
  slug: verato-reactivatesourcews-api
- description: The RestoreSource API from Verato — 1 operation(s) for restoresource.
  name: Verato RestoreSource API
  slug: verato-restoresource-api
- description: The SearchNotifications API from Verato — 1 operation(s) for searchnotifications.
  name: Verato SearchNotifications API
  slug: verato-searchnotifications-api
- description: The SearchRelationshipsService API from Verato — 1 operation(s) for searchrelationshipsservice.
  name: Verato SearchRelationshipsService API
  slug: verato-searchrelationshipsservice-api
- description: The SoftDeleteSource API from Verato — 1 operation(s) for softdeletesource.
  name: Verato SoftDeleteSource API
  slug: verato-softdeletesource-api
- description: The UnlinkIdentities API from Verato — 1 operation(s) for unlinkidentities.
  name: Verato UnlinkIdentities API
  slug: verato-unlinkidentities-api
- description: The UnmergeIdentities API from Verato — 1 operation(s) for unmergeidentities.
  name: Verato UnmergeIdentities API
  slug: verato-unmergeidentities-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/verato-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://verato.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.verato.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.verato.com/docs/reference/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developer.verato.com/docs/reference/intro
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.verato.com/docs/quickstart/intro
- group: operate
  title: ''
  type: Support
  url: https://support.verato.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://verato.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://support.verato.com/hc/en-us/articles/40628559657492-Verato-Status-Page
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.verato.com/hc/en-us/sections/8836852287764-Release-Notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/verato-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/verato-trust-center.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://verato.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://verato.com/terms-and-conditions/
- group: auth
  title: ''
  type: TrustCenter
  url: https://verato.trustshare.com/
- group: auth
  title: ''
  type: Compliance
  url: https://verato.com/platform/why-verato/security/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/verato-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/verato-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/verato-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/verato-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/verato-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/verato-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/verato-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/verato-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/verato-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verato-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Verato is a healthcare identity company whose Universal Identity Platform (MDM Cloud) resolves and matches records for people, providers, and organizations against a proprietary nationwide referential database to create and maintain a single source of truth (golden record). Verato publishes a developer portal with three RESTful JSON web-service APIs — the Person API (patient/consumer identity, demographics search, linking, merging, households, relationships), the Organization API, and the Provider API (Practitioner Type-1 and Health Facility Type-2 identities) — used for enterprise master data management, patient matching, provider data management, identity resolution, and downstream data enrichment. APIs authenticate with HTTP basic credentials over mutual TLS, with keys provisioned per tenant by a Customer Success Manager.
image: https://verato.com/wp-content/uploads/2022/09/cropped-verato_favicon-_1_-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: verato-mcp.yml
  slug: verato-mcpyml
modified: '2026-07-21'
name: Verato
nav: Providers
network: true
overview: 'Verato publishes 20 APIs on the [APIs.io](https://apis.io/) network, including AddRelationshipService API, CreateDataSource API, DeactivateSourceWs API, and 17 more. Tagged areas include Company, Cybersecurity, Healthcare, Identity, and Identity Resolution.


  Verato''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 20 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 47.2
  delta: -3.2
  facets:
    commercial_clarity: 36.8
    contract_quality: 52.9
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 43.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Verato Authentication
  slug: verato-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Verato Domain Security
  slug: verato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Verato Trust Center
  slug: verato-trust-center
  summary_line: HITRUST r2, SOC 2 Type II, PCI DSS, HIPAA
slug: verato
tags:
- Company
- Cybersecurity
- Healthcare
- Identity
- Identity Resolution
- Master Data Management
- Patient Matching
- Provider Data Management
- Data Quality
- EMPI
website: https://verato.com/
---
