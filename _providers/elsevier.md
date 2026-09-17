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
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Elsevier Agentic Access
  operation_count: 106
  slug: elsevier-agentic-access
  summary_line: 106 operations · 1 acting
api_count: 8
apis:
- description: Embase APIs provide access to biomedical and pharmacological abstracts and indexing for life sciences research, drug development, and evidence-based medicine.
  name: Elsevier Embase API
  slug: elsevier-embase-api
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
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Abstract Citation count API
  name: Elsevier Abstract Citation Count API
  slug: elsevier-abstract-citation-count-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Abstract Retrieval API
  name: Elsevier Abstract Retrieval API
  slug: elsevier-abstract-retrieval-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Affiliation Retrieval API
  name: Elsevier Affiliation Retrieval API
  slug: elsevier-affiliation-retrieval-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Affiliation Search API
  name: Elsevier Affiliation Search API
  slug: elsevier-affiliation-search-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Article Entitlement Retrieval API
  name: Elsevier Article Entitlement Retrieval API
  slug: elsevier-article-entitlement-retrieval-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Article Metadata API
  name: Elsevier Article Metadata API
  slug: elsevier-article-metadata-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Article Retrieval API
  name: Elsevier Article Retrieval API
  slug: elsevier-article-retrieval-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Author Retrieval API
  name: Elsevier Author Retrieval API
  slug: elsevier-author-retrieval-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Author Search API
  name: Elsevier Author Search API
  slug: elsevier-author-search-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Citations Overview API
  name: Elsevier Citations Overview API
  slug: elsevier-citations-overview-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Engineering Village Retrieval API
  name: Elsevier Engineering Village Retrieval API
  slug: elsevier-engineering-village-retrieval-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Engineering Village Search API
  name: Elsevier Engineering Village Search API
  slug: elsevier-engineering-village-search-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Nonserial Title API
  name: Elsevier Nonserial Title API
  slug: elsevier-nonserial-title-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Object Retrieval API
  name: Elsevier Object Retrieval API
  slug: elsevier-object-retrieval-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: ScienceDirect Search V2 API
  name: Elsevier Science Direct Search V2 API
  slug: elsevier-sciencedirect-search-v2-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Author Lookup API API from Elsevier — 4 operation(s) for scival author lookup api.
  name: Elsevier SciVal Author Lookup API
  slug: elsevier-scival-author-lookup-api-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Country Group Lookup API V1 API from Elsevier — 3 operation(s) for scival country group lookup api v1.
  name: Elsevier SciVal Country Group Lookup API V1 API
  slug: elsevier-scival-country-group-lookup-api-v1-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Country Lookup API V1 API from Elsevier — 4 operation(s) for scival country lookup api v1.
  name: Elsevier SciVal Country Lookup API V1 API
  slug: elsevier-scival-country-lookup-api-v1-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Institution Group Lookup API V1 API from Elsevier — 3 operation(s) for scival institution group lookup api v1.
  name: Elsevier SciVal Institution Group Lookup API V1 API
  slug: elsevier-scival-institution-group-lookup-api-v1-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Institution Lookup API V1 API from Elsevier — 7 operation(s) for scival institution lookup api v1.
  name: Elsevier SciVal Institution Lookup API V1 API
  slug: elsevier-scival-institution-lookup-api-v1-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Publication Lookup API V1 API from Elsevier — 2 operation(s) for scival publication lookup api v1.
  name: Elsevier SciVal Publication Lookup API V1 API
  slug: elsevier-scival-publication-lookup-api-v1-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Scopus Source Lookup API API from Elsevier — 3 operation(s) for scival scopus source lookup api.
  name: Elsevier SciVal Scopus Source Lookup API
  slug: elsevier-scival-scopus-source-lookup-api-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Subject Area Lookup API API from Elsevier — 3 operation(s) for scival subject area lookup api.
  name: Elsevier SciVal Subject Area Lookup API
  slug: elsevier-scival-subject-area-lookup-api-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Topic Cluster Lookup API API from Elsevier — 7 operation(s) for scival topic cluster lookup api.
  name: Elsevier SciVal Topic Cluster Lookup API
  slug: elsevier-scival-topic-cluster-lookup-api-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal Topic Lookup API API from Elsevier — 7 operation(s) for scival topic lookup api.
  name: Elsevier SciVal Topic Lookup API
  slug: elsevier-scival-topic-lookup-api-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: The SciVal World Lookup API API from Elsevier — 1 operation(s) for scival world lookup api.
  name: Elsevier SciVal World Lookup API
  slug: elsevier-scival-world-lookup-api-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Scopus Search API
  name: Elsevier Scopus Search API
  slug: elsevier-scopus-search-api
- baseURL: https://api.elsevier.com/content
  baseurl_source: declared
  description: Serial Title API
  name: Elsevier Serial Title API
  slug: elsevier-serial-title-api
artifact_total: 44
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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/overlays/elsevier-scopus-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elsevier-scopus-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/overlays/elsevier-sciencedirect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elsevier-sciencedirect-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/overlays/elsevier-scival-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elsevier-scival-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/overlays/elsevier-engineering-village-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elsevier-engineering-village-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/overlays/elsevier-retrieval-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elsevier-retrieval-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/overlays/elsevier-metadata-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elsevier-metadata-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.elsevier.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/agentic-access/elsevier-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elsevier-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/security/elsevier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elsevier-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/authentication/elsevier-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elsevier-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/scopes/elsevier-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/elsevier-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://id.elsevier.com/.well-known/openid-configuration
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/well-known/elsevier-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elsevier-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/conformance/elsevier-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elsevier-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.elsevier.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/conventions/elsevier-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elsevier-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/errors/elsevier-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elsevier-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/lifecycle/elsevier-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elsevier-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/changelog/elsevier-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elsevier-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://dev.elsevier.com/release_notes.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/data-model/elsevier-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elsevier-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/components/elsevier-components.yml
  title: ''
  type: Components
  url: components/elsevier-components.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/plans/elsevier-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elsevier-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/rate-limits/elsevier-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elsevier-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/packages/elsevier-packages.yml
  title: ''
  type: Packages
  url: packages/elsevier-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/packages/elsevier-packages.yml
  title: ''
  type: SDKs
  url: packages/elsevier-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/llms/elsevier-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elsevier-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/mcp/elsevier-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/elsevier-mcp.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/sandbox/elsevier-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/elsevier-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://dev.elsevier.com/interactive.html
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/wadl/_index.yml
  title: ''
  type: WADL
  url: wadl/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/elsevier/refs/heads/main/collections/elsevier.postman_collection.json
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
overview: 'Elsevier publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Abstract API, Search API, Abstract Citation Count API, and 27 more. Tagged areas include Content, Journals, Medical, Research, and Scientific.


  Elsevier''s developer surface includes authentication, changelog, release notes, sandbox, developer console, developer portal, documentation, and 38 more developer resources.'
plans:
- name: Elsevier Plans Pricing
  plan_count: 3
  slug: elsevier-plans-pricing
random_paper: 5
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
  composite: 60.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 81.6
    contract_governance: 4.5
    contract_quality: 50.7
    developer_ergonomics: 62.5
    discoverability: 68.5
    operational_transparency: 50.0
  previous_composite: 60.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 93.3
      total: 30
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 58.8
  schema_version: 0.22.0
  scored_at: '2026-09-16'
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
