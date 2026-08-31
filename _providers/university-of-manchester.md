---
access_model:
  confidence: high
  label: Free · No registration (institution-operated surfaces)
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probe
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: University Of Manchester Agentic Access
  operation_count: 4
  slug: university-of-manchester-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- description: The University's own Shibboleth Identity Provider, entityID https://shib.manchester.ac.uk/shibboleth, asserting the scope manchester.ac.uk. Its entity descriptor is published as signed, machine-readab
  name: Shibboleth SAML Identity Provider (UK Access Management Federation)
  slug: shibboleth-saml-idp
- description: The University's tenancy of Elsevier Pure, its Current Research Information System, reached at pure.manchester.ac.uk and surfaced publicly as Research Explorer at research.manchester.ac.uk. Both hostn
  name: Elsevier Pure CRIS tenancy (REST + OAI-PMH)
  slug: pure-cris-tenancy
- description: The University's institutional research data repository, presented at figshare.manchester.ac.uk, which CNAMEs to figshare.com. Manchester's researchers deposit here and the deposits carry Manchester's
  name: Figshare research data repository tenancy
  slug: figshare-tenancy
- description: IIIF Image API 2.0 level 1 endpoints.
  name: University of Manchester Image API
  slug: university-of-manchester-image-api
- description: IIIF Presentation API 2.1 manifests and collections.
  name: University of Manchester Presentation API
  slug: university-of-manchester-presentation-api
artifact_total: 18
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/university-of-manchester-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.manchester.ac.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.manchester.ac.uk/rss
- group: operate
  title: ''
  type: Support
  url: https://www.manchester.ac.uk/connect/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.manchester.ac.uk/disclaimer/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.manchester.ac.uk/about/privacy-information/data-protection/
- group: other
  title: ''
  type: Copyright
  url: https://www.manchester.ac.uk/copyright/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-university-of-manchester/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/University-of-Manchester
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UoMResearchIT
- group: other
  title: ''
  type: IdentityFederation
  url: http://mdq.ukfederation.org.uk/entities/https%3A%2F%2Fshib.manchester.ac.uk%2Fshibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.library.manchester.ac.uk/
- group: build
  title: ''
  type: DigitalCollections
  url: https://www.digitalcollections.manchester.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.manchester.ac.uk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.manchester.ac.uk/study/undergraduate/courses/
- group: other
  title: ''
  type: ResearchComputing
  url: https://research-it.manchester.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.staffnet.manchester.ac.uk/ai-hub/ai-guidelines-and-policies/
- group: build
  title: ''
  type: AITooling
  url: https://www.staffnet.manchester.ac.uk/ai-hub/tools-and-resources/
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-manchester-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-manchester-conformance.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-manchester-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-manchester-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-manchester-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-manchester-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-manchester-context.jsonld
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-manchester-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-manchester-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-manchester-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-manchester-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-manchester-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Manchester is a public research university in Manchester, England, a founding member of the Russell Group and, on the QS World University Rankings, a consistent global top-40 institution. Its programmable footprint is small, real, and almost entirely mis-stated by its own domain names. The University operates exactly three machine-readable surfaces of its own: a IIIF Presentation API and a IIIF Image API serving the John Rylands Library''s digitised manuscripts from the University''s own hosts and its own JANET address space, and a Shibboleth SAML 2.0 Identity Provider registered in the Jisc UK Access Management Federation under entityID https://shib.manchester.ac.uk/shibboleth. Everything else that looks like a Manchester API is a tenancy: pure.manchester.ac.uk and research.manchester.ac.uk both CNAME to uom-aws.elsevierpure.com and serve Elsevier''s Pure product API and OAI-PMH implementation; figshare.manchester.ac.uk CNAMEs to figshare.com. Those are Manchester''s
  records on a supplier''s platform, under a supplier''s contract, and they are recorded here as tenant relationships rather than credited as the University''s engineering. There is no central developer portal, no self-service API keys, no open data portal at data.manchester.ac.uk, and no public course, timetable or SIS API. Thirty-six OpenAPI documents previously held in this repository were Elsevier''s Pure 5.35.2-2 specification split by tag and re-titled; they have been quarantined, not counted.'
examples:
- key_count: 2
  name: University Of Manchester Iiif Collection Example
  slug: university-of-manchester-iiif-collection-example
- key_count: 2
  name: University Of Manchester Iiif Image Info Example
  slug: university-of-manchester-iiif-image-info-example
- key_count: 2
  name: University Of Manchester Iiif Manifest Example
  slug: university-of-manchester-iiif-manifest-example
finops:
- name: University Of Manchester Finops
  service_category: Education
  slug: university-of-manchester-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-manchester.png
json_schemas:
- name: University of Manchester IIIF Image API information document
  property_count: 8
  slug: university-of-manchester-iiif-image-info
- name: University of Manchester IIIF Presentation manifest
  property_count: 8
  slug: university-of-manchester-iiif-manifest
jsonld:
- class_count: 15
  name: University Of Manchester Context
  property_count: 14
  slug: university-of-manchester-context
layout: provider
modified: '2026-08-19'
name: University of Manchester
nav: Providers
network: true
overview: 'University of Manchester publishes 2 APIs on the [APIs.io](https://apis.io/) network: Image API and Presentation API. Tagged areas include University, Higher Education, Education, Research, and United Kingdom.


  The University of Manchester catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Manchester''s developer surface includes engineering blog, support, GitHub presence, authentication, and 27 more developer resources.'
plans:
- name: University Of Manchester Plans Pricing
  plan_count: 2
  slug: university-of-manchester-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: University Of Manchester Rate Limits
  slug: university-of-manchester-rate-limits
rules:
- effective_rule_count: 10
  extends: []
  name: University of Manchester API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: university-of-manchester-rules
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 26.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 34.1
    contract_quality: 71.8
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 34.1
    operational_transparency: 23.7
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/screenshots/university-of-manchester-2026-06-20T200205.png
security:
- kind: authentication
  name: University Of Manchester Authentication
  slug: university-of-manchester-authentication
  summary_line: saml2/none · 2 schemes
- kind: domain-security
  name: University Of Manchester Domain Security
  slug: university-of-manchester-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-manchester
tags:
- University
- Higher Education
- Education
- Research
- United Kingdom
- Russell Group
- Library
- Digital Collections
- IIIF
- Identity Federation
- Research Data
- Research Computing
website: https://www.manchester.ac.uk/
---
