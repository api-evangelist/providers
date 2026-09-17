---
access_model:
  confidence: high
  label: Free · Access by request
  onboarding: unknown
  pricing: free
  public: false
  source:
  - openapi
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: HBKU's research information system, Elmi, runs Elsevier Pure on the university's own subdomain and exposes a public, unauthenticated OAI-PMH 2.0 harvesting endpoint at elmi.hbku.edu.qa/ws/oai. Confirm
  name: Elmi Research Portal — OAI-PMH
  slug: elmi-oai-pmh
- description: 'HBKU publishes its academic catalog on its own host, catalog.hbku.edu.qa, running CourseLeaf. The catalog ships a JSON course-search endpoint at /course-search/api/ that answers unauthenticated POSTs '
  name: HBKU Academic Catalog — Course Search
  slug: course-catalog-search
- description: HBKU's scholarly output is deposited in Manara — Qatar Research Repository, a Figshare platform operated by Qatar National Library, with an HBKU portal at manara.qnl.qa/hbku. The deposits, DOIs and au
  name: Manara — Qatar Research Repository (HBKU portal)
  slug: manara-repository
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: Arabic language processing modules.
  name: Hamad Bin Khalifa University Arabic NLP API
  slug: hbku-arabic-nlp-api
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: The Audio API from Hamad Bin Khalifa University — 4 operation(s) for audio.
  name: Hamad Bin Khalifa University Audio API
  slug: hbku-audio-api
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: The Chat API from Hamad Bin Khalifa University — 1 operation(s) for chat.
  name: Hamad Bin Khalifa University Chat API
  slug: hbku-chat-api
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: The Images API from Hamad Bin Khalifa University — 1 operation(s) for images.
  name: Hamad Bin Khalifa University Images API
  slug: hbku-images-api
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: The Models API from Hamad Bin Khalifa University — 1 operation(s) for models.
  name: Hamad Bin Khalifa University Models API
  slug: hbku-models-api
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: The Moderations API from Hamad Bin Khalifa University — 1 operation(s) for moderations.
  name: Hamad Bin Khalifa University Moderations API
  slug: hbku-moderations-api
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: The Poems API from Hamad Bin Khalifa University — 1 operation(s) for poems.
  name: Hamad Bin Khalifa University Poems API
  slug: hbku-poems-api
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: The Tokens API from Hamad Bin Khalifa University — 1 operation(s) for tokens.
  name: Hamad Bin Khalifa University Tokens API
  slug: hbku-tokens-api
- baseURL: https://api.fanar.qa
  baseurl_source: declared
  description: The Translations API from Hamad Bin Khalifa University — 1 operation(s) for translations.
  name: Hamad Bin Khalifa University Translations API
  slug: hbku-translations-api
artifact_total: 24
common:
- group: company
  title: ''
  type: Website
  url: https://www.hbku.edu.qa/en/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hbku.edu.qa/en/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.hbku.edu.qa/en/news
- group: build
  title: ''
  type: AITooling
  url: https://fanar.qa/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.fanar.qa/docs
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.hbku.edu.qa/en/qcri
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.hbku.edu.qa/
- group: other
  title: ''
  type: ResearchRepository
  url: https://elmi.hbku.edu.qa/
- group: other
  title: ''
  type: ResearchRepository
  url: https://manara.qnl.qa/hbku
- group: build
  title: ''
  type: Library
  url: https://www.hbku.edu.qa/en/hbku-library
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qcri
- group: build
  title: ''
  type: SourceCode
  url: https://huggingface.co/QCRI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/hamad-bin-khalifa-university/
- group: other
  title: ''
  type: x
  url: https://x.com/hbku
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/vocabulary/hbku-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hbku-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/json-ld/hbku-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hbku-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/conformance/hbku-education-standards.yml
  title: ''
  type: Conformance
  url: conformance/hbku-education-standards.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/lifecycle/hbku-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hbku-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/authentication/hbku-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hbku-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/errors/hbku-fanar-errors.yml
  title: ''
  type: ErrorCatalog
  url: errors/hbku-fanar-errors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/security/hbku-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hbku-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/plans/hbku-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hbku-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/rate-limits/hbku-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hbku-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/finops/hbku-finops.yml
  title: ''
  type: FinOps
  url: finops/hbku-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Hamad Bin Khalifa University (HBKU) is a research-intensive graduate university founded in 2010 within Qatar Foundation, in Education City, Doha, Qatar. Its central administration publishes no developer portal, no open-data portal and no identity federation entry — HBKU appears in no eduGAIN federation, and api.hbku.edu.qa answers every request with a WAF rejection. What it does operate comes almost entirely from one research institute, the Qatar Computing Research Institute (QCRI), whose domain qcri.org redirects into hbku.edu.qa: Fanar, Qatar''s Arabic generative-AI platform, which publishes a first-party OpenAPI 3.1 at api.fanar.qa/openapi.json covering chat, speech, vision, translation, poetry and moderation, with a fourteen-code error vocabulary and a published per-model rate-limit table; and Farasa, a keyed Arabic NLP web API. Three further surfaces are tenant deployments on HBKU hosts and are recorded as relationships, not as HBKU contracts: a working public OAI-PMH
  2.0 endpoint over its Elsevier Pure research portal at elmi.hbku.edu.qa/ws/oai, a CourseLeaf course-search API at catalog.hbku.edu.qa whose term database is currently unavailable, and its research deposits in Manara — Qatar Research Repository, a Figshare platform run by Qatar National Library. The eleven "HBKU" Figshare API definitions this profile previously carried were one vendor contract, split eleven ways by tag and recorded under the university''s name; they have been removed.'
examples:
- key_count: 5
  name: Hbku Fanar Chat Completion Example
  slug: hbku-fanar-chat-completion-example
- key_count: 5
  name: Hbku Fanar Models 401 Example
  slug: hbku-fanar-models-401-example
- key_count: 5
  name: Hbku Farasa Invalid Key Example
  slug: hbku-farasa-invalid-key-example
finops:
- name: Hbku Finops
  service_category: Education
  slug: hbku-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hbku.png
json_schemas:
- name: Error
  property_count: 5
  slug: hbku-fanar-error
- name: ModelsResponse
  property_count: 2
  slug: hbku-fanar-models-response
jsonld:
- class_count: 8
  name: Hbku Context
  property_count: 8
  slug: hbku-context
layout: provider
modified: '2026-08-30'
name: Hamad Bin Khalifa University
nav: Providers
network: true
overview: 'Hamad Bin Khalifa University publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Arabic NLP API, Audio API, Chat API, and 6 more. Tagged areas include University, Higher Education, Education, Research, and Qatar.


  The Hamad Bin Khalifa University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hamad Bin Khalifa University''s developer surface includes engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Hbku Plans Pricing
  plan_count: 2
  slug: hbku-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Hbku Rate Limits
  slug: hbku-rate-limits
rules:
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Hamad Bin Khalifa University API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 5
  slug: hbku-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 47.4
    contract_governance: 15.2
    contract_quality: 63.9
    developer_ergonomics: 40.5
    discoverability: 59.3
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 42.3
  provenance:
    conformance: derived
    contracts:
      callable: 11.1
      derived: 1
      marker_coverage: 11.1
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/hbku/refs/heads/main/screenshots/hbku-2026-06-20T182545.png
security:
- kind: authentication
  name: Hbku Authentication
  slug: hbku-authentication
  summary_line: http-bearer/api-key-in-body · 2 schemes
- kind: domain-security
  name: Hbku Domain Security
  slug: hbku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hbku
tags:
- University
- Higher Education
- Education
- Research
- Qatar
- Middle East
- Artificial Intelligence
- LLM
- Natural Language Processing
- Arabic
- Research Computing
- Research Data
- Course Catalog
- Repository
- Open Access
website: https://www.hbku.edu.qa/en/home
---
