---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Contensis Agentic Access
  operation_count: 7
  slug: contensis-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: 'The Contensis Delivery API focuses on delivering content created in content types and entries to websites and applications. It is a read-only HTTP API designed for high-performance content retrieval, '
  name: Contensis Delivery API
  slug: delivery-api
- description: 'The Contensis Management API allows developers to import and manage content within content types and entries. It provides full CRUD access to content models, entries, projects, and related resources, '
  name: Contensis Management API
  slug: management-api
- description: The Contensis Image API provides real-time image manipulation and optimization features as part of the Delivery API. It supports on-the-fly transformations such as resizing, cropping, format conversio
  name: Contensis Image API
  slug: image-api
- baseURL: https://cms-{alias}.cloud.contensis.com
  baseurl_source: declared
  description: The Content Types API from Contensis — 2 operation(s) for content types.
  name: Contensis Content Types API
  slug: contensis-content-types-api
- baseURL: https://cms-{alias}.cloud.contensis.com
  baseurl_source: declared
  description: The Entries API from Contensis — 3 operation(s) for entries.
  name: Contensis Entries API
  slug: contensis-entries-api
- baseURL: https://cms-{alias}.cloud.contensis.com
  baseurl_source: declared
  description: The Projects API from Contensis — 1 operation(s) for projects.
  name: Contensis Projects API
  slug: contensis-projects-api
- baseURL: https://cms-{alias}.cloud.contensis.com
  baseurl_source: declared
  description: The Taxonomy API from Contensis — 1 operation(s) for taxonomy.
  name: Contensis Taxonomy API
  slug: contensis-taxonomy-api
artifact_total: 23
asyncapis:
- description: ''
  name: Contensis Webhooks
  slug: contensis-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Contensis Delivery API (HTTP) Content Types API
  slug: open-contensis-content-types-api
- collection_type: open
  name: Contensis Delivery API (HTTP) Content Types Entries API
  slug: open-contensis-entries-api
- collection_type: open
  name: Contensis Delivery API (HTTP) Content Types Projects API
  slug: open-contensis-projects-api
- collection_type: open
  name: Contensis Delivery API (HTTP) Content Types Taxonomy API
  slug: open-contensis-taxonomy-api
- collection_type: open
  name: Contensis Delivery API (HTTP)
  slug: open-contensis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contensis-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/contensis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/contensis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contensis-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contensis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/contensis
- group: company
  title: ''
  type: Website
  url: https://www.contensis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.contensis.com/help-and-docs/apis
- group: company
  title: ''
  type: Blog
  url: https://www.contensis.com/community/blog
- group: operate
  title: ''
  type: Community
  url: https://www.contensis.com/community
- group: operate
  title: ''
  type: Support
  url: https://www.contensis.com/help-and-docs
- group: build
  title: ''
  type: Packages
  url: packages/contensis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/contensis-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/contensis-cli.yml
- group: design
  title: ''
  type: Components
  url: components/contensis-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/contensis-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/contensis-security.txt
- group: auth
  title: ''
  type: Security
  url: security/contensis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/contensis-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/contensis-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contensis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/contensis-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/contensis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/contensis-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/contensis-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zengenti.cloud/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/contensis-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/contensis-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/contensis-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/contensis-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/contensis-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/contensis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/contensis-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.contensis.com/help-and-docs/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.contensis.com/help-and-docs/developers/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.contensis.com/help-and-docs/guides/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.contensis.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.contensis.com/contact-us/request-demo
- group: start
  title: ''
  type: Login
  url: https://www.contensis.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.contensis.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.contensis.com/privacy-and-cookies
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.contensis.com/support
created: '2024-11-13'
description: Contensis is an enterprise-level Content Management System (CMS) developed by Zengenti, designed to help organizations create, manage, and deliver digital content across multiple platforms and devices through HTTP, JavaScript, and .Net APIs.
finops:
- name: Contensis Finops
  service_category: API
  slug: contensis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/contensis.png
layout: provider
modified: '2026-09-06'
name: Contensis
nav: Providers
network: true
overview: 'Contensis publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Content Types API, Entries API, Projects API, and 1 more. Tagged areas include CMS, Content, Headless CMS, Content Management, and Digital Experience Platform.


  The Contensis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Contensis'' developer surface includes documentation, engineering blog, support, CLI, authentication, changelog, API reference, and 36 more developer resources.'
plans:
- name: Contensis Plans Pricing
  plan_count: 0
  slug: contensis-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Contensis Rate Limits
  slug: contensis-rate-limits
scopes:
- name: Contensis Scopes
  scope_count: 0
  slug: contensis-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 48.1
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 51.0
    developer_ergonomics: 78.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 24.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 85.2
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/contensis/refs/heads/main/screenshots/contensis-2026-06-20T174925.png
security:
- kind: authentication
  name: Contensis Authentication
  slug: contensis-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Contensis Domain Security
  slug: contensis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Contensis Vulnerability Disclosure
  slug: contensis-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Contensis Trust Center
  slug: contensis-trust-center
  summary_line: ISO 27001
slug: contensis
tags:
- CMS
- Content
- Headless CMS
- Content Management
- Digital Experience Platform
- Content Delivery
- Webhooks
- Higher Education
website: https://www.contensis.com/
---
