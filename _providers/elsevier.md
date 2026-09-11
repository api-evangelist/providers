---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Elsevier Agentic Access
  operation_count: 8
  slug: elsevier-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Scopus delivers a comprehensive view of the world of research, allowing tracking, analysis, and visualization of research data across publishers, journals, books, conference proceedings, and trade pub
  name: Elsevier Scopus APIs
  slug: elsevier-scopus-apis
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: ScienceDirect APIs expose peer-reviewed full-text scientific, technical and medical content from all scholarly publications indexed by ScienceDirect, Elsevier's premier scientific platform.
  name: Elsevier ScienceDirect APIs
  slug: elsevier-sciencedirect-apis
- baseURL: https://api.elsevier.com/analytics/scival
  baseurl_source: declared
  description: The SciVal API gives access to a comprehensive set of metrics for researchers (Scopus Author profiles) and 8,500+ institutions available in SciVal, Elsevier's platform for research performance benchma
  name: Elsevier SciVal API
  slug: elsevier-scival-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Engineering Village APIs provide programmatic access to engineering research literature, indexed publications, and engineering-focused content across multiple databases.
  name: Elsevier Engineering Village API
  slug: elsevier-engineering-village-api
- description: Embase APIs provide access to biomedical and pharmacological abstracts and indexing for life sciences research, drug development, and evidence-based medicine.
  name: Elsevier Embase API
  slug: elsevier-embase-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: 'The Retrieval APIs return a single record by identifier across the Elsevier corpus — abstracts, full-text articles, article objects, entitlements, author profiles and affiliation profiles — reachable '
  name: Elsevier Retrieval APIs
  slug: elsevier-retrieval-apis
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: 'The Metadata APIs cover citation counts, the Citations Overview, and serial and non-serial title metadata and search — the bibliographic layer over Scopus rather than the content itself. Six paths on '
  name: Elsevier Metadata APIs
  slug: elsevier-metadata-apis
- description: Elsevier's COUNTER Code of Practice Release 5 and 5.1 API, delivering standards-compliant usage statistics and reports over SUSHI. Base https://api.elsevier.com/sushi/ for COP5 and https://api.elsevie
  name: Elsevier COUNTER SUSHI API
  slug: elsevier-sushi-api
- baseURL: https://api.elsevier.com
  baseurl_source: declared
  description: The Abstract API from Elsevier — 5 operation(s) for abstract.
  name: Elsevier Abstract API
  slug: elsevier-abstract-api
- baseURL: https://api.elsevier.com
  baseurl_source: declared
  description: The Search API from Elsevier — 3 operation(s) for search.
  name: Elsevier Search API
  slug: elsevier-search-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elsevier Scopus APIs Abstract API
  slug: open-elsevier-abstract-api
- collection_type: open
  name: Elsevier Scopus APIs Abstract Search API
  slug: open-elsevier-search-api
- collection_type: open
  name: Elsevier Scopus APIs
  slug: open-elsevier
common:
- group: company
  title: ''
  type: Website
  url: https://www.elsevier.com/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elsevier-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elsevier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elsevier-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elsevier-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://id.elsevier.com/.well-known/openid-configuration
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elsevier-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elsevier-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.elsevier.com/security
- group: design
  title: ''
  type: Conventions
  url: conventions/elsevier-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elsevier-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elsevier-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elsevier-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://dev.elsevier.com/release_notes.html
- group: design
  title: ''
  type: DataModel
  url: data-model/elsevier-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/elsevier-components.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elsevier-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elsevier-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/elsevier-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/elsevier-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elsevier-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/elsevier-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/elsevier-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://dev.elsevier.com/interactive.html
- group: other
  title: ''
  type: WADL
  url: wadl/_index.yml
- group: build
  title: ''
  type: Postman
  url: collections/elsevier.postman_collection.json
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elsevier
- group: start
  title: ''
  type: Portal
  url: https://dev.elsevier.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.elsevier.com/api_docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://dev.elsevier.com/api_docs.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.elsevier.com/api_service_agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elsevier.com/legal/privacy-policy
- group: build
  title: ''
  type: Examples
  url: https://dev.elsevier.com/examples.html
- group: learn
  title: ''
  type: Tutorials
  url: https://dev.elsevier.com/technical_documentation.html
- group: operate
  title: ''
  type: Support
  url: https://dev.elsevier.com/support.html
- group: start
  title: ''
  type: SignUp
  url: https://dev.elsevier.com/apikey/manage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ElsevierDev
- group: company
  title: ''
  type: Blog
  url: https://www.elsevier.com/connect
created: '2023-11-22'
description: Elsevier is a Dutch academic publishing company specializing in scientific, technical, and medical content. Its products include journals such as The Lancet and Cell, the ScienceDirect collection of electronic journals, the online citation database Scopus, the SciVal research performance platform, and the ClinicalKey search engine for clinicians. Its Research Products APIs expose Scopus, ScienceDirect, SciVal, Embase, Engineering Village and COUNTER usage reporting over a single host, api.elsevier.com, under an API key plus institutional entitlement model.
finops:
- name: Elsevier Finops
  service_category: API
  slug: elsevier-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elsevier.png
layout: provider
modified: '2026-09-06'
name: Elsevier
nav: Providers
network: true
overview: 'Elsevier publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Scopus APIs, ScienceDirect APIs, SciVal API, and 5 more. Tagged areas include Content, Journals, Medical, Research, and Scientific.


  Elsevier''s developer surface includes authentication, changelog, release notes, sandbox, developer console, developer portal, documentation, and 32 more developer resources.'
plans:
- name: Elsevier Plans Pricing
  plan_count: 3
  slug: elsevier-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 36
  name: Elsevier Rate Limits
  slug: elsevier-rate-limits
scopes:
- name: Elsevier Scopes
  scope_count: 0
  slug: elsevier-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 4.5
    contract_quality: 51.6
    developer_ergonomics: 62.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 77.8
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/screenshots/elsevier-2026-06-20T180616.png
security:
- kind: authentication
  name: Elsevier Authentication
  slug: elsevier-authentication
  summary_line: apiKey/bearer-like-token/oauth2 · 6 schemes
- kind: domain-security
  name: Elsevier Domain Security
  slug: elsevier-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Elsevier Trust Center
  slug: elsevier-trust-center
  summary_line: ISO/IEC 27001
slug: elsevier
tags:
- Content
- Journals
- Medical
- Research
- Scientific
- Technical
website: https://www.elsevier.com/
---
