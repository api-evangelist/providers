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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Physna Agentic Access
  operation_count: 72
  slug: physna-agentic-access
  summary_line: 72 operations · 35 acting
api_count: 1
apis:
- baseURL: https://api.physna.com/v2
  baseurl_source: declared
  description: The ClientCredentials API from Physna — 2 operation(s) for clientcredentials.
  name: Physna ClientCredentials API
  slug: physna-clientcredentials-api
- baseURL: https://api.physna.com/v2
  baseurl_source: declared
  description: The Collections API from Physna — 13 operation(s) for collections.
  name: Physna Collections API
  slug: physna-collections-api
- baseURL: https://api.physna.com/v2
  baseurl_source: declared
  description: The Deprecated API from Physna — 8 operation(s) for deprecated.
  name: Physna Deprecated API
  slug: physna-deprecated-api
- baseURL: https://api.physna.com/v2
  baseurl_source: declared
  description: The Folders API from Physna — 3 operation(s) for folders.
  name: Physna Folders API
  slug: physna-folders-api
- baseURL: https://api.physna.com/v2
  baseurl_source: declared
  description: The Image Search API from Physna — 2 operation(s) for image search.
  name: Physna Image Search API
  slug: physna-image-search-api
- baseURL: https://api.physna.com/v2
  baseurl_source: declared
  description: The Metadata API from Physna — 6 operation(s) for metadata.
  name: Physna Metadata API
  slug: physna-metadata-api
- baseURL: https://api.physna.com/v2
  baseurl_source: declared
  description: The Models API from Physna — 16 operation(s) for models.
  name: Physna Models API
  slug: physna-models-api
- baseURL: https://api.physna.com/v2
  baseurl_source: declared
  description: The Users API from Physna — 4 operation(s) for users.
  name: Physna Users API
  slug: physna-users-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Physna Public ClientCredentials API
  slug: open-physna-clientcredentials-api
- collection_type: open
  name: Physna Public ClientCredentials Collections API
  slug: open-physna-collections-api
- collection_type: open
  name: Physna Public ClientCredentials Deprecated API
  slug: open-physna-deprecated-api
- collection_type: open
  name: Physna Public ClientCredentials Folders API
  slug: open-physna-folders-api
- collection_type: open
  name: Physna Public ClientCredentials Image Search API
  slug: open-physna-image-search-api
- collection_type: open
  name: Physna Public ClientCredentials Metadata API
  slug: open-physna-metadata-api
- collection_type: open
  name: Physna Public ClientCredentials Models API
  slug: open-physna-models-api
- collection_type: open
  name: Physna Public ClientCredentials Users API
  slug: open-physna-users-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/physna-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/physna-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/physna-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/physna-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/physna-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/physna-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/physna-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/physna-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/physna-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/physna-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/physna-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/physna-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.physna.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://physna.github.io/public-api-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://physna.github.io/public-api-guide/
- group: docs
  title: ''
  type: APIReference
  url: https://api.physna.com/v2/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://physna.github.io/public-api-guide/guides/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/physna
- group: company
  title: ''
  type: Blog
  url: https://physna.com/blog
- group: operate
  title: ''
  type: Support
  url: https://physna.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://physna.com/request-trial
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://physna.com/privacy-policy
created: '2026-07-17'
description: Physna is a geometric search and 3D deep-learning platform that lets you search, compare, analyze, and organize 3D models and physical parts by their actual geometry rather than by filename or metadata. Its public REST API (v2, OpenAPI 3.0) exposes model ingestion and reprocessing, geometric search (part-to-part, part-in-part, part, scan, visual, and geo-related matches), image-based search, collections and folders, model/collection metadata and metadata keys, assembly-tree traversal, match reports, user management, and client-credential provisioning. The API is JSON over HTTPS, is authenticated with OAuth 2.0 through Physna's Okta authorization server, and is used to detect duplicate designs, discover alternative components, and organize design inventory across manufacturing, engineering, and AI training use cases.
image: https://physna.com/assets/vectors/logo-p.svg
layout: provider
modified: '2026-07-20'
name: Physna
nav: Providers
network: true
overview: 'Physna publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ClientCredentials API, Collections API, Deprecated API, and 5 more. Tagged areas include Company, Artificial Intelligence, 3D, Geometric Search, and Manufacturing.


  Physna''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 16 more developer resources.'
random_paper: 8
scopes:
- name: Physna Scopes
  scope_count: 6
  slug: physna-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 47.6
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/physna/refs/heads/main/screenshots/physna-2026-09-02T151410.png
security:
- kind: authentication
  name: Physna Authentication
  slug: physna-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Physna Domain Security
  slug: physna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: physna
tags:
- Company
- Artificial Intelligence
- 3D
- Geometric Search
- Manufacturing
- Engineering
- Machine-Learning
- Search
- Computer-Vision
- Product Development
website: https://www.physna.com
---
