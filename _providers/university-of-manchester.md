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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-09-23'
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
- baseURL: https://www.digitalcollections.manchester.ac.uk/iiif
  baseurl_source: declared
  description: IIIF Image API 2.0 level 1 endpoints.
  name: University of Manchester Image API
  slug: university-of-manchester-image-api
- baseURL: https://www.digitalcollections.manchester.ac.uk/iiif
  baseurl_source: declared
  description: IIIF Presentation API 2.1 manifests and collections.
  name: University of Manchester Presentation API
  slug: university-of-manchester-presentation-api
artifact_total: 67
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pure activity API
  slug: open-university-of-manchester-activity-api
- collection_type: open
  name: Pure activity application API
  slug: open-university-of-manchester-application-api
- collection_type: open
  name: Pure activity authorCollaboration API
  slug: open-university-of-manchester-authorcollaboration-api
- collection_type: open
  name: Pure activity award API
  slug: open-university-of-manchester-award-api
- collection_type: open
  name: Pure activity classificationScheme API
  slug: open-university-of-manchester-classificationscheme-api
- collection_type: open
  name: Pure activity concept API
  slug: open-university-of-manchester-concept-api
- collection_type: open
  name: Pure activity contract API
  slug: open-university-of-manchester-contract-api
- collection_type: open
  name: Pure activity course API
  slug: open-university-of-manchester-course-api
- collection_type: open
  name: Pure activity dataSet API
  slug: open-university-of-manchester-dataset-api
- collection_type: open
  name: Pure activity education API
  slug: open-university-of-manchester-education-api
- collection_type: open
  name: Pure activity equipment API
  slug: open-university-of-manchester-equipment-api
- collection_type: open
  name: Pure activity event API
  slug: open-university-of-manchester-event-api
- collection_type: open
  name: Pure activity externalOrganization API
  slug: open-university-of-manchester-externalorganization-api
- collection_type: open
  name: Pure activity externalPerson API
  slug: open-university-of-manchester-externalperson-api
- collection_type: open
  name: Pure activity fingerprint API
  slug: open-university-of-manchester-fingerprint-api
- collection_type: open
  name: Pure activity fundingOpportunity API
  slug: open-university-of-manchester-fundingopportunity-api
- collection_type: open
  name: Pure activity impact API
  slug: open-university-of-manchester-impact-api
- collection_type: open
  name: Pure activity journal API
  slug: open-university-of-manchester-journal-api
- collection_type: open
  name: Pure activity keywordGroupConfiguration API
  slug: open-university-of-manchester-keywordgroupconfiguration-api
- collection_type: open
  name: Pure activity milestone API
  slug: open-university-of-manchester-milestone-api
- collection_type: open
  name: Pure activity organization API
  slug: open-university-of-manchester-organization-api
- collection_type: open
  name: Pure activity person API
  slug: open-university-of-manchester-person-api
- collection_type: open
  name: Pure activity personExpertise API
  slug: open-university-of-manchester-personexpertise-api
- collection_type: open
  name: Pure activity pressMedia API
  slug: open-university-of-manchester-pressmedia-api
- collection_type: open
  name: Pure activity prize API
  slug: open-university-of-manchester-prize-api
- collection_type: open
  name: Pure activity project API
  slug: open-university-of-manchester-project-api
- collection_type: open
  name: Pure activity publisher API
  slug: open-university-of-manchester-publisher-api
- collection_type: open
  name: Pure activity researchOutput API
  slug: open-university-of-manchester-researchoutput-api
- collection_type: open
  name: Pure activity role API
  slug: open-university-of-manchester-role-api
- collection_type: open
  name: Pure activity semester API
  slug: open-university-of-manchester-semester-api
- collection_type: open
  name: Pure activity specialization API
  slug: open-university-of-manchester-specialization-api
- collection_type: open
  name: Pure activity studentProject API
  slug: open-university-of-manchester-studentproject-api
- collection_type: open
  name: Pure activity studentThesis API
  slug: open-university-of-manchester-studentthesis-api
- collection_type: open
  name: Pure activity thesaurus API
  slug: open-university-of-manchester-thesaurus-api
- collection_type: open
  name: Pure activity user API
  slug: open-university-of-manchester-user-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/capabilities/university-of-manchester-capability-edges.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/authentication/university-of-manchester-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-manchester-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/conformance/university-of-manchester-conformance.yml
  title: ''
  type: Conformance
  url: conformance/university-of-manchester-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/errors/university-of-manchester-errors.yml
  title: ''
  type: Errors
  url: errors/university-of-manchester-errors.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/lifecycle/university-of-manchester-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-manchester-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/rules/university-of-manchester-rules.yml
  title: ''
  type: Rules
  url: rules/university-of-manchester-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/vocabulary/university-of-manchester-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-manchester-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/json-ld/university-of-manchester-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/university-of-manchester-context.jsonld
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/agentic-access/university-of-manchester-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-manchester-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/security/university-of-manchester-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-manchester-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/plans/university-of-manchester-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-manchester-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/rate-limits/university-of-manchester-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-manchester-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/finops/university-of-manchester-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-manchester-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Manchester is a public research university in Manchester, England, a founding member of the Russell Group and, on the QS World University Rankings, a consistent global top-40 institution. Its programmable footprint is small, real, and almost entirely mis-stated by its own domain names. The University operates exactly three machine-readable surfaces of its own: a IIIF Presentation API and a IIIF Image API serving the John Rylands Library''s digitised manuscripts from the University''s own hosts and its own JANET address space, and a Shibboleth SAML 2.0 Identity Provider registered in the Jisc UK Access Management Federation under entityID https://shib.manchester.ac.uk/shibboleth. Everything else that looks like a Manchester API is a tenancy: pure.manchester.ac.uk and research.manchester.ac.uk both CNAME to uom-aws.elsevierpure.com and serve Elsevier''s Pure product API and OAI-PMH implementation; figshare.manchester.ac.uk CNAMEs to figshare.com. Those are Manchester''s
  records on a supplier''s platform, under a supplier''s contract, and they are recorded here as tenant relationships rather than credited as the University''s engineering. There is no central developer portal, no self-service API keys, no open data portal at data.manchester.ac.uk, and no public course, timetable or SIS API. Thirty-six OpenAPI documents previously held in this repository were Elsevier''s Pure 5.35.2-2 specification split by tag and re-titled; they have been quarantined, not counted.'
examples:
- key_count: 13
  name: University Of Manchester Activity Example
  slug: university-of-manchester-activity-example
- key_count: 2
  name: University Of Manchester Iiif Collection Example
  slug: university-of-manchester-iiif-collection-example
- key_count: 2
  name: University Of Manchester Iiif Image Info Example
  slug: university-of-manchester-iiif-image-info-example
- key_count: 2
  name: University Of Manchester Iiif Manifest Example
  slug: university-of-manchester-iiif-manifest-example
- key_count: 17
  name: University Of Manchester Person Example
  slug: university-of-manchester-person-example
- key_count: 15
  name: University Of Manchester Project Example
  slug: university-of-manchester-project-example
- key_count: 4
  name: University Of Manchester Research Outputs List Example
  slug: university-of-manchester-research-outputs-list-example
finops:
- name: University Of Manchester Finops
  service_category: Education
  slug: university-of-manchester-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-manchester.png
json_schemas:
- name: Activity
  property_count: 39
  slug: university-of-manchester-activity
- name: University of Manchester IIIF Image API information document
  property_count: 8
  slug: university-of-manchester-iiif-image-info
- name: University of Manchester IIIF Presentation manifest
  property_count: 8
  slug: university-of-manchester-iiif-manifest
- name: Person
  property_count: 51
  slug: university-of-manchester-person
- name: Project
  property_count: 47
  slug: university-of-manchester-project
- name: ResearchOutput
  property_count: 53
  slug: university-of-manchester-researchoutput
json_structures:
- name: University Of Manchester Activity Structure
  property_count: 39
  slug: university-of-manchester-activity-structure
- name: University Of Manchester Person Structure
  property_count: 51
  slug: university-of-manchester-person-structure
- name: University Of Manchester Project Structure
  property_count: 47
  slug: university-of-manchester-project-structure
- name: University Of Manchester Researchoutput Structure
  property_count: 53
  slug: university-of-manchester-researchoutput-structure
jsonld:
- class_count: 10
  name: University Of Manchester Context
  property_count: 22
  slug: university-of-manchester-context
layout: provider
modified: '2026-08-19'
name: University of Manchester
nav: Providers
network: true
overview: 'University of Manchester publishes 2 APIs on the [APIs.io](https://apis.io/) network: Image API and Presentation API. Tagged areas include University, Higher Education, Education, Research, and United Kingdom.


  The University of Manchester catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Manchester''s developer surface includes engineering blog, support, GitHub presence, authentication, and 27 more developer resources.'
plans:
- name: University Of Manchester Plans Pricing
  plan_count: 2
  slug: university-of-manchester-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: University Of Manchester Rate Limits
  slug: university-of-manchester-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of Manchester API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: university-of-manchester-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: University of Manchester API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: university-of-manchester-rules
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 85.3
    catalog_earned_first_party: 0.0
    catalog_gap: 29.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.2
  facets:
    access_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 71.3
    developer_ergonomics: 28.6
    discoverability: 68.5
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 49.1
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
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-manchester/refs/heads/main/screenshots/university-of-manchester-2026-06-20T200205.png
security:
- kind: authentication
  name: University Of Manchester Authentication
  slug: university-of-manchester-authentication
  summary_line: apiKey · 1 scheme
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
