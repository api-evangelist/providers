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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Fanar is Qatar's Arabic generative-AI platform, developed by the Qatar Computing Research Institute at Hamad Bin Khalifa University with support from Qatar's Ministry of Communications and Information
  name: Fanar API
  slug: fanar-api
- description: Farasa ("insight") is the Arabic text-processing toolkit built by the Arabic Language Technologies group at QCRI, Hamad Bin Khalifa University, and offered free to registered users as a keyed web API.
  name: Farasa Web API
  slug: farasa-api
- description: HBKU's research information system, Elmi, runs Elsevier Pure on the university's own subdomain and exposes a public, unauthenticated OAI-PMH 2.0 harvesting endpoint at elmi.hbku.edu.qa/ws/oai. Confirm
  name: Elmi Research Portal — OAI-PMH
  slug: elmi-oai-pmh
- description: 'HBKU publishes its academic catalog on its own host, catalog.hbku.edu.qa, running CourseLeaf. The catalog ships a JSON course-search endpoint at /course-search/api/ that answers unauthenticated POSTs '
  name: HBKU Academic Catalog — Course Search
  slug: course-catalog-search
- description: HBKU's scholarly output is deposited in Manara — Qatar Research Repository, a Figshare platform operated by Qatar National Library, with an HBKU portal at manara.qnl.qa/hbku. The deposits, DOIs and au
  name: Manara — Qatar Research Repository (HBKU portal)
  slug: manara-repository
artifact_total: 17
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
  title: ''
  type: Vocabulary
  url: vocabulary/hbku-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hbku-context.jsonld
- group: design
  title: ''
  type: Conformance
  url: conformance/hbku-education-standards.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/hbku-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hbku-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/hbku-fanar-errors.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hbku-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hbku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hbku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hbku-finops.yml
- group: other
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
overview: 'Hamad Bin Khalifa University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Fanar API and Farasa Web API. Tagged areas include University, Higher Education, Education, Research, and Qatar.


  The Hamad Bin Khalifa University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Hamad Bin Khalifa University''s developer surface includes engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Hbku Plans Pricing
  plan_count: 2
  slug: hbku-plans-pricing
random_paper: 6
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
  composite: 43.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -9.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 15.2
    contract_quality: 51.7
    developer_ergonomics: 40.5
    discoverability: 59.3
    governance: 15.2
    operational_transparency: 18.4
  previous_composite: 53.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
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
- Large Language Models
- Natural Language Processing
- Arabic
- Research Computing
- Research Data
- Course Catalog
- Repository
- Open Access
website: https://www.hbku.edu.qa/en/home
---
