---
access_model:
  confidence: high
  label: Free · affiliation-gated except one keyless surface
  onboarding: unknown
  pricing: free
  public: false
  source:
  - probes
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The JSON backend of Dartmouth Class Search, the institution''s public timetable of class meetings. Keyless: an unauthenticated POST returned 1393 sections for term 202609 on 2026-08-30. Two routes — se'
  name: Dartmouth Class Search API
  slug: class-search
- description: 'Dartmouth''s institutional API platform, serving resource APIs such as People (directory identity) and Nextgen class schedules. Live and institution-operated: every resource path on api.dartmouth.edu r'
  name: DartAPI
  slug: dartapi
- description: 'An OpenAI- and Anthropic-compatible API over large language, embedding and reranking models running on Dartmouth''s own research-computing infrastructure, plus third-party cloud models the institution '
  name: Dartmouth Chat AI API
  slug: chat-ai
- description: Dartmouth's SAML identity provider, registered in the InCommon federation under entityID urn:mace:incommon:dartmouth.edu and retrievable as machine-readable metadata over the InCommon MDQ protocol. Th
  name: Dartmouth Identity Federation (InCommon)
  slug: identity-federation
- description: Dartmouth's open-data portal, a tenant site on Esri's ArcGIS Hub. The data and the catalog are Dartmouth's; the search API behind it is Esri's Hub Search API on the shared host hub.arcgis.com, which e
  name: Dartmouth Open Data (ArcGIS Hub tenant)
  slug: open-data
- description: Dartmouth's institutional repository for scholarly, research and educational output, running on bepress/Elsevier Digital Commons under a Dartmouth subdomain. Its OAI-PMH 2.0 endpoint is live and answe
  name: Dartmouth Digital Commons (bepress/Elsevier tenant)
  slug: digital-commons
- description: Dartmouth's research-data repository, a Dataverse 6.11 deployment on Dartmouth's own host. The native Dataverse API answers unauthenticated — /api/info/version returns 200 with the running version — b
  name: Dartmouth Dataverse
  slug: dataverse
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: company
  title: ''
  type: Website
  url: https://home.dartmouth.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dartmouth.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://courses.dartmouth.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Adartmouth.edu
- group: other
  title: ''
  type: OpenData
  url: https://data-dartmouth.opendata.arcgis.com/
- group: other
  title: ''
  type: ResearchRepository
  url: https://digitalcommons.dartmouth.edu/
- group: other
  title: ''
  type: ResearchComputing
  url: https://rc.dartmouth.edu/
- group: build
  title: ''
  type: AITooling
  url: https://chat.dartmouth.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://policies.dartmouth.edu/policy/guidelines-using-generative-artificial-intelligence-genai-coursework
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.library.dartmouth.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dartmouth
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dartmouth-dltg
- group: operate
  title: ''
  type: Support
  url: https://services.dartmouth.edu/TDClient/1806/Portal/Home/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://home.dartmouth.edu/privacy
- group: other
  title: ''
  type: SignIn
  url: https://login.dartmouth.edu/cas/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/dartmouth-college/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/dartmouth
- group: company
  title: ''
  type: Blog
  url: https://home.dartmouth.edu/rss.xml
- group: design
  title: ''
  type: Conformance
  url: conformance/dartmouth-education-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dartmouth-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/dartmouth-errors.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dartmouth-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dartmouth-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dartmouth-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dartmouth-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'Dartmouth operates real APIs and almost all of them are closed. developer.dartmouth.edu, including every /docs/ page, 302s to Microsoft Entra SAML, so DartAPI''s endpoint inventory cannot be read from outside the institution and none is asserted here. api.dartmouth.edu answers 401 on every resource path and chat.dartmouth.edu/api answers 401 without a DARTMOUTH_API_KEY — both live, both credentialed, neither describable. What could be captured was captured: the keyless Dartmouth Class Search backend, described from live probes into a full artifact set, and Dartmouth''s InCommon SAML metadata. The research and data surfaces are tenant deployments whose contracts belong to Esri, bepress/Elsevier and the Dataverse project. Seven ArcGIS Hub Search OpenAPIs plus 26 files derived from them were removed from this repo on 2026-08-30; they described Esri''s product, were re-based onto chat.dartmouth.edu, and their sample data was a StoryMap about a park in Panama City.'
  evidence:
  - status: 200
    url: https://courses.dartmouth.edu/api/?page=fose&route=search
  - status: 401
    url: https://api.dartmouth.edu/api/people/
  - status: 405
    url: https://api.dartmouth.edu/api/jwt
  - status: 401
    url: https://chat.dartmouth.edu/api/models
  - status: 302
    url: https://developer.dartmouth.edu/docs/100_basic/010_introduction.md
  - status: 200
    url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Adartmouth.edu
  - status: 200
    url: https://digitalcommons.dartmouth.edu/do/oai/?verb=Identify
  - status: 200
    url: https://dataverse.dartmouth.edu/api/info/version
  - status: 503
    url: https://dataverse.dartmouth.edu/oai?verb=Identify
  - note: soft 404 — returns the Open WebUI SPA shell as text/html, not a specification
    status: 200
    url: https://chat.dartmouth.edu/openapi.json
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'Dartmouth College is a private Ivy League research university in Hanover, New Hampshire. Its programmable footprint is small, mostly gated, and largely operated by vendors on Dartmouth''s behalf — the ordinary shape for a research university, which is a federation of buyers rather than an API producer. Exactly one institution-operated interface is open to the public without credentials: the JSON backend of Dartmouth Class Search (courses.dartmouth.edu), which returns the full timetable of class meetings keyless and which Dartmouth does not document as an API. Everything else Dartmouth itself runs is behind authentication: DartAPI at api.dartmouth.edu answers 401 on every resource path and issues JWTs only against a hand-issued API key tied to a Dartmouth Service Account, its developer portal at developer.dartmouth.edu redirects to Microsoft Entra SAML so not one reference page is readable from outside, and the Dartmouth Chat AI API requires a DARTMOUTH_API_KEY. The one genuinely
  open machine-readable artifact Dartmouth publishes is its SAML identity-federation metadata in InCommon. The research and data surfaces — Dartmouth Open Data on ArcGIS Hub, Dartmouth Digital Commons on bepress/Elsevier, Dartmouth Dataverse — are Dartmouth''s data on someone else''s contract and are recorded here as tenant relationships, not as Dartmouth engineering.'
examples:
- key_count: 4
  name: Dartmouth Class Search Example
  slug: dartmouth-class-search-example
finops:
- name: Dartmouth Finops
  service_category: Education
  slug: dartmouth-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dartmouth.png
json_schemas:
- name: Dartmouth Class Search response
  property_count: 3
  slug: dartmouth-class-search-response
layout: provider
modified: '2026-08-30'
name: Dartmouth College
nav: Providers
network: true
overview: 'Dartmouth College publishes 1 API on the [APIs.io](https://apis.io/) network: Dartmouth Class Search API. Tagged areas include University, Higher Education, Education, United States, and Ivy League.


  The Dartmouth College catalog on APIs.io includes 1 Spectral governance ruleset.


  Dartmouth College''s developer surface includes GitHub presence, support, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Dartmouth Plans Pricing
  plan_count: 2
  slug: dartmouth-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Dartmouth Rate Limits
  slug: dartmouth-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: Dartmouth College API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 2
  slug: dartmouth-class-search-rules
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 22.7
    contract_quality: 61.2
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 22.7
    operational_transparency: 26.3
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dartmouth/refs/heads/main/screenshots/dartmouth-2026-07-25T211220.png
security:
- kind: authentication
  name: Dartmouth Authentication
  slug: dartmouth-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dartmouth Domain Security
  slug: dartmouth-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: dartmouth
tags:
- University
- Higher Education
- Education
- United States
- Ivy League
- Private Research University
- Course Catalog
- Identity Federation
- Research Data
- Open Data
- Artificial Intelligence
website: https://home.dartmouth.edu/
---
