---
access_model:
  confidence: high
  label: Public docs and specs, approval-gated keys
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - documentation
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 390
  human_in_the_loop: 0
  name: Vaultre Agentic Access
  operation_count: 974
  slug: vaultre-agentic-access
  summary_line: 974 operations · 390 acting
api_count: 3
apis:
- description: The core VaultRE REST API - the open API a third-party developer integrates an agency website or application against. Version 1.3 documents 324 paths and 453 operations covering contacts, properties a
  name: VaultRE API
  slug: vaultre-api
- description: A distinct set of endpoints that operate at the integrator level rather than at an individual agency-account level, letting an approved integrator enumerate the accounts that have granted it an access
  name: VaultRE Integrator API
  slug: vaultre-integrator-api
- description: A deliberately separate write-only ingestion API that lets other CRM systems feed property data into VaultRE on behalf of a franchise-group agency. Six documented operations accept staff records and p
  name: VaultRE Aggregator API
  slug: vaultre-aggregator-api
artifact_total: 9
asyncapis:
- description: ''
  name: Vaultre Webhooks
  slug: vaultre-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vaultre-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vaultre-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vaultre-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mrisoftware.com/au/products/vault/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.api.vaultre.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.vaultre.com.au/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.vaultre.com.au/swagger/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.vaultre.com.au/basics.html
- group: auth
  title: ''
  type: Authentication
  url: https://docs.api.vaultre.com.au/oauth.html
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.api.vaultre.com.au/guide.html
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.api.vaultre.com.au/changelog.html
- group: build
  title: ''
  type: CodeExamples
  url: https://docs.api.vaultre.com.au/samples.html
- group: start
  title: ''
  type: SignUp
  url: https://www.mrisoftware.com/au/products/vault/api-integrations/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VaultGroup
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/VaultGroup/api-samples
- group: start
  title: ''
  type: Login
  url: https://login.vaultre.com.au/
- group: operate
  title: ''
  type: Support
  url: https://docs.api.vaultre.com.au/guide.html#assistance
- group: company
  title: ''
  type: Blog
  url: https://www.mrisoftware.com/au/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mrisoftware.com/au/products/vault/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mrisoftware.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mrisoftware.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mrisoftware.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vaultre-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vaultre-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vaultre-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vaultre-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vaultre-conformance.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vaultre-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/vaultre-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vaultre-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vaultre-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vaultre-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/vaultre-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vaultre-llms.txt
created: '2026-07-26'
description: 'VaultRE - now marketed as MRI Vault CRM, after VaultRE''s parent Vault Group / PropTech Group was absorbed into MRI Software - is an Australian cloud real estate CRM and transaction platform used by residential, commercial, rural, land, business and property-management agencies across Australia and New Zealand. It sits in the agency and CRM layer of the value chain rather than the portal or registry layer: it holds the agency''s contacts, appraisals, listings, offers, open homes, feedback, tenancies, maintenance, invoicing and AML records, and feeds listings outward to Australia''s portal duopoly (realestate.com.au and Domain) instead of being a portal, a land registry or a conveyancing rail itself. Unlike most of this sector, VaultRE publishes a genuinely open, versioned, machine-readable contract - a public MkDocs developer site at docs.api.vaultre.com.au carrying downloadable OpenAPI 3.0.1 documents for v1.1, v1.2 and v1.3 of the core API (324 paths and 453 operations in
  v1.3) plus a separate Aggregator API for franchise-group CRM data feeds. The API surface is documented openly but access is not self-serve: anyone can read the docs and download the specs, but API keys are issued only after an integrator-registration request is reviewed and approved (VaultRE states new integrations are generally created within two business days), and each agency must then mint a scoped access token for that integrator from inside its own VaultRE account. RESO plays no part here - Australia has no RESO mandate and no RESO, OData or $metadata reference appears anywhere in VaultRE''s documentation or specifications; the local listing-distribution seam is REAXML and portal-specific feeds instead. Auth is a static X-Api-Key integrator key paired with a per-account Bearer access token, with an OAuth2-style authorisation-code flow available for token minting, scoped tokens readable via GET /scopes, HMAC-SHA512-signed webhooks, and published rate limits of 10 requests per second
  and 10,000 requests per day.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vaultre.png
layout: provider
mcp_servers:
- description: ''
  name: vaultre-mcp.yml
  slug: vaultre-mcpyml
modified: '2026-07-26'
name: VaultRE
nav: Providers
network: true
overview: 'VaultRE publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Integrator API, Aggregator API, and 1 more. Tagged areas include Real Estate, Australia, New Zealand, PropTech, and CRM.


  The VaultRE catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  VaultRE''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, code examples, signup flow, and 28 more developer resources.'
random_paper: 42
scopes:
- name: Vaultre Scopes
  scope_count: 0
  slug: vaultre-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.8
  delta: -1.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 64.7
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vaultre/refs/heads/main/screenshots/vaultre-2026-07-27T125402.png
security:
- kind: authentication
  name: Vaultre Authentication
  slug: vaultre-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Vaultre Domain Security
  slug: vaultre-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vaultre
tags:
- Real Estate
- Australia
- New Zealand
- PropTech
- CRM
- Property Listings
- Property Management
- Rentals
- Commercial Real Estate
- Webhooks
website: https://www.mrisoftware.com/au/products/vault/
---
