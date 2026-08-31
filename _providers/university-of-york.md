---
access_model:
  confidence: high
  label: Free · keyless, no registration, CORS open
  onboarding: open
  pricing: free
  public: true
  source:
  - authentication
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 30.4
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The keyless JSON search interface behind discover.york.ac.uk, the University of York's Digital Collections. Two live endpoints — /api/search-simple, which the public search page calls, and /api/search
  name: University of York Digital Collections Search API
  slug: digital-collections-search
- description: 'The University of York serves its digitised material through two IIIF specifications on its own host: IIIF Image API 3.0 at compliance level 2 (the served info.json declares "profile": "level2", "type'
  name: University of York Digital Collections IIIF APIs
  slug: digital-collections-iiif
- description: OAI-PMH 2.0 harvesting on the University's own registrable domain. The Identify response names the repository "The University of York", gives adminEmail pure-support@york.ac.uk and an earliest datesta
  name: University of York Research Portal OAI-PMH
  slug: research-portal-oai-pmh
- description: The University's own SAML 2.0 identity provider at shib.york.ac.uk, running Shibboleth. It is the authentication surface through which every bought platform — Pure, Primo, the VLE — is actually reache
  name: University of York Shibboleth Identity Provider
  slug: shibboleth-idp
- description: The Elsevier Pure REST Web Service running on the University of York's tenant host. The documentation index answers without a key and the versioned API serves a 1.1 MB OpenAPI document, but the API it
  name: Elsevier Pure Web Services (University of York tenant)
  slug: pure-web-services
- description: YorSearch is the University of York library discovery service, an Ex Libris Primo front end over an Alma backend (view id 44YORK_INST:NUI). The discovery UI is live on a York host, but programmatic ac
  name: YorSearch Library Discovery (Ex Libris Primo / Alma)
  slug: yorsearch-primo
- description: White Rose Research Online is the shared EPrints institutional repository of the Universities of York, Leeds and Sheffield, on the consortium's own whiterose.ac.uk domain. Its OAI-PMH 2.0 interface is
  name: White Rose Research Online OAI-PMH (consortium)
  slug: wrro-oai
- description: White Rose eTheses Online is the shared EPrints theses repository of York, Leeds and Sheffield, running on the consortium's own domain. Its OAI-PMH 2.0 interface Identifies as "White Rose eTheses Onli
  name: White Rose eTheses Online OAI-PMH (consortium)
  slug: wreo-oai
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: company
  title: ''
  type: Website
  url: https://www.york.ac.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://discover.york.ac.uk/about/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/university-of-york
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/school/uniofyork/
- group: operate
  title: ''
  type: Status
  url: https://status.york.ac.uk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.york.ac.uk/about/legal-statements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.york.ac.uk/about/legal-statements/#privacy
- group: operate
  title: ''
  type: Support
  url: https://www.york.ac.uk/it-services/
- group: company
  title: ''
  type: Blog
  url: https://www.york.ac.uk/news-and-events/
- group: other
  title: ''
  type: OpenData
  url: https://discover.york.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://pure.york.ac.uk/portal/
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.whiterose.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://etheses.whiterose.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://yorsearch.york.ac.uk/discovery/search?vid=44YORK_INST:NUI
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.york.ac.uk/study/undergraduate/courses/
- group: other
  title: ''
  type: ResearchComputing
  url: https://vikingdocs.york.ac.uk/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.york.ac.uk/it-services/tools/viking/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.york.ac.uk/about/ai/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.york.ac.uk/students/studying/assessment-and-examination/ai/taught-student-guidance/
- group: build
  title: ''
  type: AITooling
  url: https://www.york.ac.uk/it-services/tools/generative-ai-tools/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-york-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-york-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-york-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-york-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-york-conformance.yml
- group: auth
  title: ''
  type: x-authentication
  url: authentication/university-of-york-authentication.yml
- group: design
  title: ''
  type: x-errors
  url: errors/university-of-york-errors.yml
- group: design
  title: ''
  type: x-lifecycle
  url: lifecycle/university-of-york-lifecycle.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/university-of-york-vocabulary.yml
- group: design
  title: ''
  type: x-rules
  url: rules/university-of-york-rules.yml
- group: design
  title: ''
  type: x-rules
  url: rules/university-of-york-jsonschema-spectral-rules.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/university-of-york-context.jsonld
created: '2026-06-03'
description: 'The University of York is a public research university in York, United Kingdom, and a member of the Russell Group. It operates no central developer portal, no API gateway, no self-service key issuance and no documented course, timetable or student-information API — and this profile says so rather than padding it. What it does operate, found by probing rather than by reading claims, is a genuinely first-party machine-readable estate around its digitised collections: a keyless JSON search API over 415,165 archive, library and cultural-heritage records at discover.york.ac.uk, a IIIF Image API 3.0 deployment at compliance level 2, IIIF Presentation API 3.0 manifests and canvases, all under the University''s own ARK namespace (NAAN 36941); plus a live OAI-PMH 2.0 harvesting endpoint on its own research-portal host that emits ORCID iDs in its MODS records, and a Shibboleth SAML 2.0 identity provider. Everything else that looks like a York API is someone else''s contract running under
  York''s name: the Elsevier Pure REST Web Service, Ex Libris Primo/Alma discovery (YorSearch), and the White Rose Research Online and White Rose eTheses Online EPrints repositories shared with Leeds and Sheffield. Those are recorded here as tenant relationships, which they are, and not as York engineering, which they are not.'
examples:
- key_count: 7
  name: University Of York Digital Collections Search Example
  slug: university-of-york-digital-collections-search-example
- key_count: 7
  name: University Of York Iiif Image Info Example
  slug: university-of-york-iiif-image-info-example
- key_count: 7
  name: University Of York Iiif Presentation Manifest Example
  slug: university-of-york-iiif-presentation-manifest-example
finops:
- name: University Of York Finops
  service_category: Education
  slug: university-of-york-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-york.png
json_schemas:
- name: University of York Digital Collections Item
  property_count: 48
  slug: university-of-york-digital-collections-item
- name: University of York IIIF Image API 3.0 Information Document
  property_count: 12
  slug: university-of-york-iiif-image-info
jsonld:
- class_count: 18
  name: University Of York Context
  property_count: 14
  slug: university-of-york-context
layout: provider
modified: '2026-08-30'
name: University of York
nav: Providers
network: true
overview: 'University of York publishes 3 APIs on the [APIs.io](https://apis.io/) network: Digital Collections Search API, Digital Collections IIIF APIs, and Research Portal OAI-PMH. Tagged areas include University, Higher Education, Education, United Kingdom, and Russell Group.


  The University of York catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of York''s developer surface includes documentation, status page, support, engineering blog, and 29 more developer resources.'
plans:
- name: University Of York Plans Pricing
  plan_count: 2
  slug: university-of-york-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: University Of York Rate Limits
  slug: university-of-york-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of York API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: university-of-york-jsonschema-spectral-rules
- effective_rule_count: 14
  extends: []
  name: University of York API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 5
  slug: university-of-york-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 41.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 13.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 62.8
    developer_ergonomics: 26.2
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 30.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-york/refs/heads/main/screenshots/university-of-york-2026-06-20T200333.png
security:
- kind: authentication
  name: University Of York Authentication
  slug: university-of-york-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of York Domain Security
  slug: university-of-york-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-york
tags:
- University
- Higher Education
- Education
- United Kingdom
- Russell Group
- Digital Collections
- Cultural Heritage
- Archives
- IIIF
- Research Data
- Open Access
- OAI-PMH
- Identity Federation
- Library
- Research Computing
website: https://www.york.ac.uk/
---
