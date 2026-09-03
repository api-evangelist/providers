---
access_model:
  confidence: high
  label: Free · Campus affiliation required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - scopes
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Ucsd Agentic Access
  operation_count: 7
  slug: ucsd-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 4
apis:
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: 'Chat completion endpoints on the OpenAI-compatible LLM gateway UC San Diego operates for approved campus faculty, staff, researchers and teams. The gateway runs on the campus Data Science and Machine '
  name: TritonAI Developer API — chat
  slug: tritonai-chat-api
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: Text completion endpoints on the UC San Diego TritonAI LLM gateway. Institution-operated on campus infrastructure; access requires an issued TritonAI API key.
  name: TritonAI Developer API — completions
  slug: tritonai-completions-api
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: Embedding generation endpoints on the UC San Diego TritonAI LLM gateway. Institution-operated on campus infrastructure; access requires an issued TritonAI API key.
  name: TritonAI Developer API — embeddings
  slug: tritonai-embeddings-api
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: Model discovery endpoints on the UC San Diego TritonAI LLM gateway. The catalogue of models the gateway exposes is published for campus users through the TritonAI Model Hub.
  name: TritonAI Developer API — models
  slug: tritonai-models-api
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: Image generation endpoints on the UC San Diego TritonAI LLM gateway. Institution-operated on campus infrastructure; access requires an issued TritonAI API key.
  name: TritonAI Developer API — images
  slug: tritonai-images-api
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: Speech synthesis and transcription endpoints on the UC San Diego TritonAI LLM gateway. Institution-operated on campus infrastructure; access requires an issued TritonAI API key.
  name: TritonAI Developer API — audio
  slug: tritonai-audio-api
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: SCIM 2.0 (RFC 7643 / RFC 7644) user and group provisioning surface exposed by the TritonAI gateway on UC San Diego infrastructure — 18 operations across /scim/v2/Users, /scim/v2/Groups, /scim/v2/Schem
  name: TritonAI Developer API — SCIM 2.0 provisioning
  slug: tritonai-scim-api
- description: The campus API gateway, running WSO2 API Manager 4.1.0 at api.ucsd.edu on UC San Diego address space (169.228.220.90), with a developer portal, a publisher console and a legacy carbon admin console. T
  name: UC San Diego API Gateway (WSO2 API Manager)
  slug: api-gateway
- description: UC San Diego's SAML 2.0 identity provider, "TritON", registered in the InCommon Federation under entityID urn:mace:incommon:ucsd.edu and distributed through the InCommon MDQ metadata service. The meta
  name: UC San Diego Shibboleth Identity Provider (InCommon / eduGAIN)
  slug: identity-federation
- description: The campus Web API Portal and REST API guidelines. TENANT, not institution-engineered — https://collab.ucsd.edu/api/api-documentation issues a 302 to https://ucsdcollab.atlassian.net/wiki and the cont
  name: UC San Diego Web API Portal (Atlassian Confluence Cloud tenant)
  slug: confluence-api-portal
- description: UC San Diego Library mints DOIs for its Digital Collections under DataCite repository account CDL.UCSD ("UC San Diego", registered 2012), prefix 10.6075. 22,934 DOIs resolve to library.ucsd.edu/dc lan
  name: UC San Diego DOI registration (DataCite / California Digital Library)
  slug: datacite-doi-registration
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: Retrieval of a single digital object or assembled collection record.
  name: University of California, San Diego Objects API
  slug: ucsd-objects-api
- baseURL: https://tritonai-api.ucsd.edu
  baseurl_source: declared
  description: Faceted search across publicly discoverable digital objects and collections.
  name: University of California, San Diego Search API
  slug: ucsd-search-api
artifact_total: 37
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio API
  slug: open-ucsd-audio-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio chat API
  slug: open-ucsd-chat-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio completions API
  slug: open-ucsd-completions-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio embeddings API
  slug: open-ucsd-embeddings-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio images API
  slug: open-ucsd-images-api
- collection_type: open
  name: TritonAI Developer API (LiteLLM Gateway) audio models API
  slug: open-ucsd-models-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/ucsd-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucsd.edu/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ucsd.edu/
- group: docs
  title: ''
  type: APIReference
  url: https://tritonai.ucsd.edu/developer-apis/index.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.ucsd.edu/devportal
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aucsd.edu
- group: other
  title: ''
  type: ResearchRepository
  url: https://library.ucsd.edu/dc/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.ucsd.edu/dc/p/about
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.ucsd.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://datahub.ucsd.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://tritonai.ucsd.edu/about/trust-architecture.html
- group: build
  title: ''
  type: AITooling
  url: https://tritongpt.ucsd.edu/
- group: build
  title: ''
  type: AITooling
  url: https://tritonai.ucsd.edu/skills/index.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UCSD
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucsdlib
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucsd-ets
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ucsd.edu/about/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ucsd.edu/about/privacy.html
- group: operate
  title: ''
  type: Status
  url: https://status.ucsd.edu/
- group: operate
  title: ''
  type: Support
  url: https://support.ucsd.edu/services
- group: company
  title: ''
  type: Blog
  url: https://today.ucsd.edu/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uc-san-diego/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ucsd-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucsd-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucsd-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ucsd-conformance.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/ucsd-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/ucsd-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ucsd-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ucsd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucsd-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucsd-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'University of California, San Diego is a public research university in La Jolla, California, and a campus of the University of California system. Its programmable footprint is real but almost entirely inward-facing, and the honest summary is that UC San Diego operates infrastructure rather than publishing products. Four surfaces are genuinely institution-operated: TritonAI, an OpenAI-compatible LLM gateway running on the campus Data Science and Machine Learning Platform at tritonai-api.ucsd.edu, which publishes a live OpenAPI document and a SCIM 2.0 provisioning surface; a WSO2 API Manager 4.1.0 gateway at api.ucsd.edu whose catalogue is closed to anonymous clients; a Shibboleth identity provider registered in InCommon as urn:mace:incommon:ucsd.edu, whose SAML metadata is the one fully public machine-readable contract the institution has; and the Library Digital Collections, a locally developed Fedora/Solr repository that answers undocumented but live JSON at library.ucsd.edu/dc.
  What is NOT UC San Diego''s own engineering is the campus API portal — collab.ucsd.edu redirects to an Atlassian Confluence Cloud tenant — and the DOI registration behind the repository, which runs on a California Digital Library DataCite account. There is no open, self-service, externally documented API; every campus API requires a UC San Diego Single Sign-On account or an issued credential, and the institution says so plainly.'
examples:
- key_count: 3
  name: Ucsd Chat Completion Example
  slug: ucsd-chat-completion-example
- key_count: 3
  name: Ucsd Embeddings Example
  slug: ucsd-embeddings-example
- key_count: 3
  name: Ucsd Library Dc Search Example
  slug: ucsd-library-dc-search-example
finops:
- name: Ucsd Finops
  service_category: Education
  slug: ucsd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucsd.png
json_schemas:
- name: TritonAI Chat Completion Request
  property_count: 7
  slug: ucsd-chat-completion-request
- name: TritonAI Embedding Request
  property_count: 3
  slug: ucsd-embedding-request
json_structures:
- name: Ucsd Chat Completion Structure
  property_count: 7
  slug: ucsd-chat-completion-structure
- name: Ucsd Embedding Structure
  property_count: 3
  slug: ucsd-embedding-structure
jsonld:
- class_count: 14
  name: Ucsd Context
  property_count: 3
  slug: ucsd-context
layout: provider
modified: '2026-08-19'
name: University of California, San Diego
nav: Providers
network: true
overview: 'University of California, San Diego publishes 9 APIs on the [APIs.io](https://apis.io/) network, including TritonAI Developer API — chat, TritonAI Developer API — completions, TritonAI Developer API — embeddings, and 6 more. Tagged areas include Education, Higher Education, University, Public Research University, and UC System.


  The University of California, San Diego catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of California, San Diego''s developer surface includes documentation, API reference, GitHub presence, status page, support, engineering blog, authentication, and 26 more developer resources.'
plans:
- name: Ucsd Plans Pricing
  plan_count: 2
  slug: ucsd-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Ucsd Rate Limits
  slug: ucsd-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of California, San Diego API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ucsd-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: University of California, San Diego API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 3
  slug: ucsd-rules
scopes:
- name: Ucsd Scopes
  scope_count: 0
  slug: ucsd-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 9.8
    contract_quality: 63.4
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 54.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ucsd/refs/heads/main/screenshots/ucsd-2026-06-20T195946.png
security:
- kind: authentication
  name: Ucsd Authentication
  slug: ucsd-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ucsd Domain Security
  slug: ucsd-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ucsd
tags:
- Education
- Higher Education
- University
- Public Research University
- UC System
- United States
- California
- Research
- Research Data
- Digital Collections
- Identity Federation
- API Gateway
- Artificial Intelligence
- Research Computing
website: https://www.ucsd.edu/
---
