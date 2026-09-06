---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 32
  human_in_the_loop: 2
  name: Immuta Agentic Access
  operation_count: 83
  slug: immuta-agentic-access
  summary_line: 83 operations · 32 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: The Immuta Govern app API — the tenant-hosted REST surface for registering data sources and connections, authoring data, subscription and write policies, managing domains, projects, purposes, tags, fr
  name: Immuta Govern API
  slug: govern-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs for managing data access
  name: Immuta Access Request API
  slug: immuta-access-request-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs for managing assets
  name: Immuta Asset API
  slug: immuta-asset-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: The Auth API from Immuta — 3 operation(s) for auth.
  name: Immuta Auth API
  slug: immuta-auth-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs for managing data products
  name: Immuta Data Product API
  slug: immuta-data-product-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs for managing data sources
  name: Immuta Data Source API
  slug: immuta-data-source-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs for managing data use agreements
  name: Immuta Data Use Agreement API
  slug: immuta-data-use-agreement-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs for checking the health of the service
  name: Immuta Health API
  slug: immuta-health-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs used to retrieve metadata from Immuta to enrich the marketplace
  name: Immuta Metadata API
  slug: immuta-metadata-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs for managing notifications
  name: Immuta Notification API
  slug: immuta-notification-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs for managing request forms
  name: Immuta Request Form API
  slug: immuta-request-form-api
- baseURL: https://na.api.immutacloud.com/marketplace
  baseurl_source: declared
  description: APIs used to retrieve metadata settings
  name: Immuta Settings API
  slug: immuta-settings-api
artifact_total: 20
asyncapis:
- description: ''
  name: Immuta Webhooks
  slug: immuta-webhooks
collections:
- collection_type: open
  name: Immuta Data Marketplace
  slug: open-immuta-marketplace-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/immuta-marketplace-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/immuta-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.immuta.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.immuta.com/saas/developer-guides/api-intro
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.immuta.com/saas
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.immuta.com/saas/developer-guides/api-intro
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.immuta.com/saas/developer-guides/api-intro/integrations-api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.immuta.com/en/customer-portal
- group: company
  title: ''
  type: Blog
  url: https://www.immuta.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/immuta
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.immuta.com/en
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/immuta-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.immuta.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://documentation.immuta.com/saas/releases/deprecations
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/immuta-lifecycle.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.immuta.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.immuta.com/legal/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.immutacloud.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/immuta-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://www.immuta.com/trust/
- group: auth
  title: ''
  type: Compliance
  url: https://www.immuta.com/trust/
- group: auth
  title: ''
  type: Security
  url: https://bugcrowd.com/61d7ba4d-be53-4704-9a73-761d6f108df9/external/report
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/immuta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/immuta-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/immuta-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/immuta-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/immuta-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/immuta-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/immuta-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/immuta-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/immuta-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/immuta-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/immuta-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/immuta-llms.txt
- group: operate
  title: ''
  type: SLA
  url: https://www.immuta.com/wp-content/uploads/2025/01/Immuta-Support-Policy-SLA-February-2025.pdf
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/immuta/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/immuta
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Immuta
created: '2026-08-01'
description: 'Immuta is a data security and access-governance platform that lets organizations register their cloud data platforms — Snowflake, Databricks (Unity Catalog, Lakebase, Spark), Amazon Redshift and Redshift Spectrum, Amazon S3, AWS Lake Formation, Google BigQuery, Azure Synapse Analytics, Starburst (Trino) and Teradata — and then author, enforce and audit subscription, data and write policies against that data from a single control plane. The platform is split into the Govern, Provision (Request) and Comply apps, with attribute-based access control, sensitive data discovery and tagging, dynamic masking and row-level filtering, purpose-based restrictions, data products and an access-request workflow, plus agentic data access controls for governing how AI agents and LLMs query sensitive data. Immuta exposes this surface through several REST APIs: the Data Marketplace / Request app API (published as OpenAPI 3.0), the Govern V1 and V2 APIs, the integrations API and the connections
  API, alongside the Immuta CLI, a webhook event surface and a Terraform provider.'
image: https://www.immuta.com/wp-content/uploads/2024/10/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: Immuta MCP Server
  slug: immuta-mcp-server
modified: '2026-08-01'
name: Immuta
nav: Providers
network: true
overview: 'Immuta publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Access Request API, Asset API, Auth API, and 8 more. Tagged areas include Company, Data Governance, Data Access Control, Data Security, and Data Privacy.


  The Immuta catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Immuta''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 32 more developer resources.'
random_paper: 2
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 63.3
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/immuta/refs/heads/main/screenshots/immuta-2026-08-07T170630.png
security:
- kind: authentication
  name: Immuta Authentication
  slug: immuta-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Immuta Domain Security
  slug: immuta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Immuta Vulnerability Disclosure
  slug: immuta-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Immuta Trust Center
  slug: immuta-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: immuta
tags:
- Company
- Data Governance
- Data Access Control
- Data Security
- Data Privacy
- Policy Management
- Data Marketplace
- Compliance
- Snowflake
- Databricks
- Analytics
- Agentic Data Access
website: https://www.immuta.com/
---
