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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://app.indico.io/restapi
  baseurl_source: declared
  description: Exchange an API token for a short-lived JWT access token
  name: Indico Data Authentication API
  slug: indico-data-authentication-api
- baseURL: https://app.indico.io/restapi
  baseurl_source: declared
  description: Datasets that back workflows and models
  name: Indico Data Datasets API
  slug: indico-data-datasets-api
- baseURL: https://app.indico.io/restapi
  baseurl_source: declared
  description: Objects stored on the Indico platform
  name: Indico Data Storage API
  slug: indico-data-storage-api
- baseURL: https://app.indico.io/restapi
  baseurl_source: declared
  description: Documents submitted to a workflow and their results
  name: Indico Data Submissions API
  slug: indico-data-submissions-api
- baseURL: https://app.indico.io/restapi
  baseurl_source: declared
  description: Document processing workflows
  name: Indico Data Workflows API
  slug: indico-data-workflows-api
artifact_total: 17
collections:
- collection_type: open
  name: Indico REST Authentication API
  slug: open-indico-data-authentication-api
- collection_type: open
  name: Indico REST Authentication Datasets API
  slug: open-indico-data-datasets-api
- collection_type: open
  name: Indico REST Authentication Storage API
  slug: open-indico-data-storage-api
- collection_type: open
  name: Indico REST Authentication Submissions API
  slug: open-indico-data-submissions-api
- collection_type: open
  name: Indico REST Authentication Workflows API
  slug: open-indico-data-workflows-api
common:
- group: other
  href: https://artifacts.apis.io/indico-data/capabilities/indico-data-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/indico-data-capability-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://indicodata.ai/
- group: commercial
  href: https://artifacts.apis.io/indico-data/plans/indico-data-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/indico-data-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/indico-data/overlays/indico-data-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/indico-data-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://indicodata.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.indicodata.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.indicodata.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developer.indicodata.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.indicodata.ai/docs/getting-started
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.indicodata.ai/
- group: company
  title: ''
  type: Blog
  url: https://indicodata.ai/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IndicoDataSolutions
- group: start
  title: ''
  type: Login
  url: https://app.indico.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://indicodata.ai/eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://indicodata.ai/privacypolicy
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.carbidesecure.com/trust/indico
- group: auth
  title: ''
  type: Compliance
  url: https://app.carbidesecure.com/trust/indico
- group: operate
  href: https://artifacts.apis.io/indico-data/changelog/indico-data-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/indico-data-changelog.yml
- group: auth
  href: https://artifacts.apis.io/indico-data/authentication/indico-data-authentication.yml
  title: ''
  type: Authentication
  url: authentication/indico-data-authentication.yml
- group: design
  href: https://artifacts.apis.io/indico-data/conventions/indico-data-conventions.yml
  title: ''
  type: Conventions
  url: conventions/indico-data-conventions.yml
- group: design
  href: https://artifacts.apis.io/indico-data/conformance/indico-data-conformance.yml
  title: ''
  type: Conformance
  url: conformance/indico-data-conformance.yml
- group: design
  href: https://artifacts.apis.io/indico-data/lifecycle/indico-data-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/indico-data-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/indico-data/packages/indico-data-packages.yml
  title: ''
  type: Packages
  url: packages/indico-data-packages.yml
- group: build
  href: https://artifacts.apis.io/indico-data/packages/indico-data-packages.yml
  title: ''
  type: SDKs
  url: packages/indico-data-packages.yml
- group: agent
  href: https://artifacts.apis.io/indico-data/llms/indico-data-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/indico-data-llms.txt
- group: agent
  href: https://artifacts.apis.io/indico-data/mcp/indico-data-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/indico-data-mcp.yml
- group: agent
  href: https://artifacts.apis.io/indico-data/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/indico-data/security/indico-data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/indico-data-domain-security.yml
created: '2026-07-17'
description: Indico Data is an enterprise intelligent document processing (IDP) and intelligent process automation (IPA) company that turns unstructured content — documents, emails, images, and free text — into structured, usable data. Its Agents & Workflows platform lets teams build extraction and classification models from as few as ~200 sample documents (no rules or templates) and deploy them as document-processing pipelines. Developers integrate via a REST API and a companion GraphQL API, authenticating with an API token exchanged for a short-lived JWT, and via first-party Python, C#, and Java client libraries. The platform is commonly deployed on a dedicated per-customer cluster and is used to automate high-volume unstructured-data workflows across insurance, financial services, and other document-heavy industries.
finops:
- has_sources: true
  method: derived
  name: Indico Data Finops
  primary_unit: ''
  service_category: ''
  slug: indico-data-finops
  template: true
image: https://indicodata.ai/wp-content/uploads/2023/01/indico-data-logo.png
layout: provider
modified: '2026-07-19'
name: Indico Data
nav: Providers
network: true
overview: 'Indico Data publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Datasets API, Storage API, and 2 more. Tagged areas include Company, Intelligent Document Processing, Intelligent Process Automation, Document AI, and Machine Learning.


  Indico Data''s developer surface includes pricing, documentation, API reference, getting-started guide, engineering blog, changelog, authentication, and 21 more developer resources.'
plans:
- name: Indico Data Plans Pricing
  plan_count: 0
  slug: indico-data-plans-pricing
random_paper: 5
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 36.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 24.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/indico-data/indico-data-2026-07-25T222311.png
security:
- kind: authentication
  name: Indico Data Authentication
  slug: indico-data-authentication
  summary_line: http-basic/http-bearer · 2 schemes
- kind: domain-security
  name: Indico Data Domain Security
  slug: indico-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Indico Data Trust Center
  slug: indico-data-trust-center
  summary_line: SOC 2 Type II
skill_count: 2
skills:
- name: List, review, and retry submissions
  slug: indico-data-review-and-retry
- name: Submit a document and retrieve results
  slug: indico-data-submit-and-retrieve
slug: indico-data
tags:
- Company
- Intelligent Document Processing
- Intelligent Process Automation
- Document AI
- Machine Learning
- Unstructured Data
- Data Extraction
- Insurance
website: https://indicodata.ai/
---
