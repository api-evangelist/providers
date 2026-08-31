---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: 'CAVATICA is a pediatric-research data analysis platform Seven Bridges operates with the Children''s Hospital of Philadelphia and the NIH Common Fund. It exposes the same v2 REST API surface on its own '
  name: Seven Bridges CAVATICA API
  slug: seven-bridges-cavatica-api
- description: The Action API from Seven Bridges — 3 operation(s) for action.
  name: Seven Bridges Action API
  slug: seven-bridges-action-api
- description: The API Settings API from Seven Bridges — 1 operation(s) for api settings.
  name: Seven Bridges API Settings API
  slug: seven-bridges-api-settings-api
- description: The Apps API from Seven Bridges — 8 operation(s) for apps.
  name: Seven Bridges Apps API
  slug: seven-bridges-apps-api
- description: The Billing API from Seven Bridges — 8 operation(s) for billing.
  name: Seven Bridges Billing API
  slug: seven-bridges-billing-api
- description: The Bulk API from Seven Bridges — 1 operation(s) for bulk.
  name: Seven Bridges Bulk API
  slug: seven-bridges-bulk-api
- description: The Files API from Seven Bridges — 10 operation(s) for files.
  name: Seven Bridges Files API
  slug: seven-bridges-files-api
- description: 'The Https: API from Seven Bridges — 1 operation(s) for https:.'
  name: 'Seven Bridges Https: API'
  slug: seven-bridges-https-api
- description: The Projects API from Seven Bridges — 9 operation(s) for projects.
  name: Seven Bridges Projects API
  slug: seven-bridges-projects-api
- description: The Rate Limit API from Seven Bridges — 1 operation(s) for rate limit.
  name: Seven Bridges Rate Limit API
  slug: seven-bridges-rate-limit-api
- description: The Search API from Seven Bridges — 1 operation(s) for search.
  name: Seven Bridges Search API
  slug: seven-bridges-search-api
- description: The Seven Bridges Platform API from Seven Bridges — 1 operation(s) for seven bridges platform.
  name: Seven Bridges Seven Bridges Platform API
  slug: seven-bridges-seven-bridges-platform-api
- description: The Storage API from Seven Bridges — 14 operation(s) for storage.
  name: Seven Bridges Storage API
  slug: seven-bridges-storage-api
- description: The Tasks API from Seven Bridges — 8 operation(s) for tasks.
  name: Seven Bridges Tasks API
  slug: seven-bridges-tasks-api
- description: The Upload API from Seven Bridges — 8 operation(s) for upload.
  name: Seven Bridges Upload API
  slug: seven-bridges-upload-api
- description: The User API from Seven Bridges — 1 operation(s) for user.
  name: Seven Bridges User API
  slug: seven-bridges-user-api
- description: The Users API from Seven Bridges — 1 operation(s) for users.
  name: Seven Bridges Users API
  slug: seven-bridges-users-api
artifact_total: 22
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/seven-bridges-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seven-bridges-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sevenbridges.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sevenbridges.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sevenbridges.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sevenbridges.com/reference/the-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sevenbridges.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.sevenbridges.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.sevenbridges.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sbg
- group: start
  title: ''
  type: Login
  url: https://accounts.sbgenomics.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sevenbridges.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sevenbridges.com/privacy-policy/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/seven-bridges-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seven-bridges-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/seven-bridges-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/seven-bridges-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/seven-bridges-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seven-bridges-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/seven-bridges-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/seven-bridges-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/seven-bridges-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/seven-bridges-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/seven-bridges-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seven-bridges-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/seven-bridges-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/seven-bridges-platform-overlay.yaml
created: '2026-08-27'
description: Seven Bridges (a Velsera company) is a biomedical data analysis company whose cloud platform lets research organizations store, organize and analyze genomic and multi-omic data at scale. The Seven Bridges Platform exposes a public REST API at api.sbgenomics.com/v2 (AWS US) and eu-api.sbgenomics.com/v2 (AWS EU) covering projects, members and permissions, files and folders, file metadata and tags, multipart uploads, cloud storage volumes with import/export jobs, CWL and Nextflow apps and their revisions, task creation/execution/batching, billing groups, invoices and cost breakdowns, plus rate limit and advanced file search. The same API powers two NIH/NCI-funded deployments Seven Bridges operates - the Cancer Genomics Cloud (cgc-api.sbgenomics.com) and CAVATICA (cavatica-api.sbgenomics.com). Authentication is a per-user X-SBG-Auth-Token header, first-party Python and R client libraries and an `sb` command line interface are published, and the API is documented on a ReadMe developer
  hub that also serves an llms.txt index.
image: https://www.sevenbridges.com/wp-content/uploads/2016/09/fb-image.png
layout: provider
modified: '2026-08-27'
name: Seven Bridges
nav: Providers
network: true
overview: 'Seven Bridges publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Action API, API Settings API, Apps API, and 13 more. Tagged areas include Genomics, Bioinformatics, Life Sciences, Healthcare, and Cloud Computing.


  Seven Bridges'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, CLI, authentication, and 21 more developer resources.'
plans:
- name: Seven Bridges Plans Pricing
  plan_count: 0
  slug: seven-bridges-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Seven Bridges Rate Limits
  slug: seven-bridges-rate-limits
score:
  band: developing
  composite: 48.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 45.2
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 49.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Seven Bridges Authentication
  slug: seven-bridges-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Seven Bridges Domain Security
  slug: seven-bridges-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Seven Bridges Trust Center
  slug: seven-bridges-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: seven-bridges
tags:
- Genomics
- Bioinformatics
- Life Sciences
- Healthcare
- Cloud Computing
- Data Analysis
- Workflow-Automation
- Research
- Precision Medicine
- Common Workflow Language
- File Storage
- Company
website: https://www.sevenbridges.com/
---
