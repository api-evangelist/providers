---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Crowdin Agentic Access
  operation_count: 23
  slug: crowdin-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 1
apis:
- description: Full-coverage REST API for Crowdin and Crowdin Enterprise. Resources include projects, files, source strings, string translations, string comments, screenshots, glossaries, MT engines, TMs, tasks, wor
  name: Crowdin REST API v2
  slug: api-v2
- description: Single-endpoint GraphQL API for Crowdin Enterprise. Authentication via Bearer token using a Personal Access Token or OAuth 2 access token.
  name: Crowdin GraphQL API
  slug: graphql
- baseURL: https://api.crowdin.com/api/v2
  baseurl_source: declared
  description: The Files API from Crowdin — 2 operation(s) for files.
  name: Crowdin Files API
  slug: crowdin-files-api
- baseURL: https://api.crowdin.com/api/v2
  baseurl_source: declared
  description: The Glossaries API from Crowdin — 2 operation(s) for glossaries.
  name: Crowdin Glossaries API
  slug: crowdin-glossaries-api
- baseURL: https://api.crowdin.com/api/v2
  baseurl_source: declared
  description: The Projects API from Crowdin — 2 operation(s) for projects.
  name: Crowdin Projects API
  slug: crowdin-projects-api
- baseURL: https://api.crowdin.com/api/v2
  baseurl_source: declared
  description: The Screenshots API from Crowdin — 1 operation(s) for screenshots.
  name: Crowdin Screenshots API
  slug: crowdin-screenshots-api
- baseURL: https://api.crowdin.com/api/v2
  baseurl_source: declared
  description: The SourceStrings API from Crowdin — 2 operation(s) for sourcestrings.
  name: Crowdin SourceStrings API
  slug: crowdin-sourcestrings-api
- baseURL: https://api.crowdin.com/api/v2
  baseurl_source: declared
  description: The StringTranslations API from Crowdin — 1 operation(s) for stringtranslations.
  name: Crowdin StringTranslations API
  slug: crowdin-stringtranslations-api
- baseURL: https://api.crowdin.com/api/v2
  baseurl_source: declared
  description: The Webhooks API from Crowdin — 1 operation(s) for webhooks.
  name: Crowdin Webhooks API
  slug: crowdin-webhooks-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Crowdin REST API v2 Files API
  slug: open-crowdin-files-api
- collection_type: open
  name: Crowdin REST API v2 Files Glossaries API
  slug: open-crowdin-glossaries-api
- collection_type: open
  name: Crowdin REST API v2 Files Projects API
  slug: open-crowdin-projects-api
- collection_type: open
  name: Crowdin REST API v2 Files Screenshots API
  slug: open-crowdin-screenshots-api
- collection_type: open
  name: Crowdin REST API v2 Files SourceStrings API
  slug: open-crowdin-sourcestrings-api
- collection_type: open
  name: Crowdin REST API v2 Files StringTranslations API
  slug: open-crowdin-stringtranslations-api
- collection_type: open
  name: Crowdin REST API v2 Files Webhooks API
  slug: open-crowdin-webhooks-api
- collection_type: open
  name: Crowdin REST API v2
  slug: open-crowdin
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crowdin-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/crowdin-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crowdin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crowdin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crowdin-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://crowdin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.crowdin.com/developer/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/crowdin
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crowdin
- group: commercial
  title: ''
  type: Plans
  url: plans/crowdin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crowdin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/crowdin-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.crowdin.com/feed.xml
created: '2026-05-23'
description: Crowdin is a localization management platform for software, mobile, games, and documentation. It offers a REST API v2 covering projects, files, strings, translations, screenshots, glossaries, MT engines, and webhooks, plus a single GraphQL endpoint. Authentication uses Personal Access Tokens or OAuth 2. Official client libraries are published for JavaScript/TypeScript, Python, PHP, .NET, Java, and Ruby. Crowdin Enterprise customers get a per-tenant domain (e.g. https://{domain}.api.crowdin.com).
finops:
- name: Crowdin Finops
  service_category: API
  slug: crowdin-finops
graphqls:
- description: Single-endpoint GraphQL API for Crowdin Enterprise. Authentication via Bearer token using a Personal Access Token or OAuth 2 access token.
  name: Crowdin GraphQL API
  slug: crowdin-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crowdin.png
layout: provider
modified: '2026-05-23'
name: Crowdin
nav: Providers
network: true
overview: 'Crowdin publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Files API, Glossaries API, Projects API, and 4 more. Tagged areas include Localization, Translation, TMS, REST, and GraphQL.


  Crowdin''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Crowdin Plans Pricing
  plan_count: 1
  slug: crowdin-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Crowdin Rate Limits
  slug: crowdin-rate-limits
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crowdin/refs/heads/main/screenshots/crowdin-2026-06-20T175254.png
security:
- kind: authentication
  name: Crowdin Authentication
  slug: crowdin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crowdin Domain Security
  slug: crowdin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crowdin Vulnerability Disclosure
  slug: crowdin-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Crowdin Trust Center
  slug: crowdin-trust-center
  summary_line: ISO 27001, HIPAA, GDPR
slug: crowdin
tags:
- Localization
- Translation
- TMS
- REST
- GraphQL
- Developer Tools
- Enterprise
website: https://crowdin.com/
---
