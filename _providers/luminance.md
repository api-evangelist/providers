---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-17'
api_count: 21
apis:
- description: The Accounts API from Luminance — 6 operation(s) for accounts.
  name: Luminance Accounts API
  slug: luminance-accounts-api
- description: The Annotation Source Relations API from Luminance — 2 operation(s) for annotation source relations.
  name: Luminance Annotation Source Relations API
  slug: luminance-annotation-source-relations-api
- description: The Annotation Sources API from Luminance — 2 operation(s) for annotation sources.
  name: Luminance Annotation Sources API
  slug: luminance-annotation-sources-api
- description: The Annotation Types API from Luminance — 2 operation(s) for annotation types.
  name: Luminance Annotation Types API
  slug: luminance-annotation-types-api
- description: The Annotations API from Luminance — 12 operation(s) for annotations.
  name: Luminance Annotations API
  slug: luminance-annotations-api
- description: The Contract Creation API from Luminance — 4 operation(s) for contract creation.
  name: Luminance Contract Creation API
  slug: luminance-contract-creation-api
- description: The Document Templates API from Luminance — 4 operation(s) for document templates.
  name: Luminance Document Templates API
  slug: luminance-document-templates-api
- description: The Documents API from Luminance — 19 operation(s) for documents.
  name: Luminance Documents API
  slug: luminance-documents-api
- description: The Folders API from Luminance — 10 operation(s) for folders.
  name: Luminance Folders API
  slug: luminance-folders-api
- description: The Matter Versions API from Luminance — 4 operation(s) for matter versions.
  name: Luminance Matter Versions API
  slug: luminance-matter-versions-api
- description: The Matters API from Luminance — 22 operation(s) for matters.
  name: Luminance Matters API
  slug: luminance-matters-api
- description: The Project Users API from Luminance — 2 operation(s) for project users.
  name: Luminance Project Users API
  slug: luminance-project-users-api
- description: The Projects API from Luminance — 6 operation(s) for projects.
  name: Luminance Projects API
  slug: luminance-projects-api
- description: The Reviews API from Luminance — 3 operation(s) for reviews.
  name: Luminance Reviews API
  slug: luminance-reviews-api
- description: The Root API from Luminance — 1 operation(s) for root.
  name: Luminance Root API
  slug: luminance-root-api
- description: The Search API from Luminance — 3 operation(s) for search.
  name: Luminance Search API
  slug: luminance-search-api
- description: The System API from Luminance — 1 operation(s) for system.
  name: Luminance System API
  slug: luminance-system-api
- description: The Tasks API from Luminance — 14 operation(s) for tasks.
  name: Luminance Tasks API
  slug: luminance-tasks-api
- description: The Traffic Light Analysis API from Luminance — 3 operation(s) for traffic light analysis.
  name: Luminance Traffic Light Analysis API
  slug: luminance-traffic-light-analysis-api
- description: The Users API from Luminance — 10 operation(s) for users.
  name: Luminance Users API
  slug: luminance-users-api
- description: The Workflows API from Luminance — 4 operation(s) for workflows.
  name: Luminance Workflows API
  slug: luminance-workflows-api
artifact_total: 48
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Luminance Accounts API
  slug: open-luminance-accounts-api
- collection_type: open
  name: Luminance Public API v2 Annotation Source Relations API
  slug: open-luminance-annotation-source-relations-api
- collection_type: open
  name: Luminance Public API v2 Annotation Sources API
  slug: open-luminance-annotation-sources-api
- collection_type: open
  name: Luminance Public API v2 Annotation Types API
  slug: open-luminance-annotation-types-api
- collection_type: open
  name: Luminance Annotations API
  slug: open-luminance-annotations-api
- collection_type: open
  name: Luminance Contract Creation API
  slug: open-luminance-contract-creation-api
- collection_type: open
  name: Luminance Public API v2 Document Templates API
  slug: open-luminance-document-templates-api
- collection_type: open
  name: Luminance Documents API
  slug: open-luminance-documents-api
- collection_type: open
  name: Luminance Folders API
  slug: open-luminance-folders-api
- collection_type: open
  name: Luminance Matter Versions API
  slug: open-luminance-matter-versions-api
- collection_type: open
  name: Luminance Matters API
  slug: open-luminance-matters-api
- collection_type: open
  name: Luminance Public API v2 Project Users API
  slug: open-luminance-project-users-api
- collection_type: open
  name: Luminance Projects API
  slug: open-luminance-projects-api
- collection_type: open
  name: Luminance Root API
  slug: open-luminance-root-api
- collection_type: open
  name: Luminance Public API v2 Search API
  slug: open-luminance-search-api
- collection_type: open
  name: Luminance Public API v2 System API
  slug: open-luminance-system-api
- collection_type: open
  name: Luminance Tasks API
  slug: open-luminance-tasks-api
- collection_type: open
  name: Luminance Traffic Light Analysis API
  slug: open-luminance-traffic-light-analysis-api
- collection_type: open
  name: Luminance Users API
  slug: open-luminance-users-api
- collection_type: open
  name: Luminance Workflows API
  slug: open-luminance-workflows-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/luminance-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/luminance-public-api-v2-overlay.yaml
- group: auth
  title: ''
  type: TrustCenter
  url: security/luminance-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.luminance.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.luminance.com/swagger-docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.luminance.com/swagger-docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.luminance.com/swagger-docsv150
- group: operate
  title: ''
  type: Support
  url: https://help.luminance.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.luminance.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.luminance.com/resources/blog/
- group: start
  title: ''
  type: SignUp
  url: https://www.luminance.com/demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.luminance.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.luminance.com/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.luminance.com/security/
- group: auth
  title: ''
  type: Authentication
  url: authentication/luminance-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/luminance-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/luminance-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/luminance-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/luminance-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/luminance-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/luminance-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/luminance-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/luminance-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/luminance-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/luminance-domain-security.yml
created: '2026-08-04'
description: 'Luminance Technologies Ltd. is a UK-headquartered legal-AI company, founded in 2015 out of Cambridge mathematics research, that builds what it markets as Legal-Grade AI for the full contract lifecycle — drafting, negotiation, analysis, compliance, investigation and collaboration. The platform is delivered as a per-customer instance (an "instance moniker" subdomain) and exposes a documented RESTful HTTP/JSON API that lets external software read and act on projects, folders, documents, matters, matter versions, tasks, reviews, annotations, workflows and document templates, plus machine-learning surfaces such as Traffic Light Analysis and annotation-driven contract intelligence. Three OpenAPI 3.0 versions are published from Luminance''s own API host: v1.3.0 and v1.4.0 (OAuth2 client-credentials) and the newer "Public API v2" v1.5, which is deployed by standard to Luminance product versions 1.43.0 onward. Authentication is OAuth2 client credentials against the customer instance
  token endpoint, and API traffic is rate limited to 100 requests every 10 minutes.'
image: https://api.luminance.com/img/general_resources/luminance_logos/Luminance-logo.png
layout: provider
mcp_servers:
- description: ''
  name: luminance-mcp.yml
  slug: luminance-mcpyml
modified: '2026-08-04'
name: Luminance
nav: Providers
network: true
overview: 'Luminance publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Annotation Source Relations API, Annotation Sources API, and 18 more. Tagged areas include Company, Legal, Artificial Intelligence, Contracts, and Contract Lifecycle Management.


  Luminance''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 20 more developer resources.'
random_paper: 62
rate_limits:
- limit_count: 1
  name: Luminance Rate Limits
  slug: luminance-rate-limits
scopes:
- name: Luminance Scopes
  scope_count: 0
  slug: luminance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 47.4
    developer_ergonomics: 45.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 45.4
  provenance:
    conformance: first-party
    contracts:
      callable: 62.5
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/luminance/refs/heads/main/screenshots/luminance-2026-08-07T171838.png
security:
- kind: authentication
  name: Luminance Authentication
  slug: luminance-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Luminance Domain Security
  slug: luminance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Luminance Trust Center
  slug: luminance-trust-center
  summary_line: SOC 2, ISO 27001
slug: luminance
tags:
- Company
- Legal
- Artificial Intelligence
- Contracts
- Contract Lifecycle Management
- Document Intelligence
- Compliance
- Legal Technology
- Enterprise Software
- Automation
website: https://www.luminance.com/
---
