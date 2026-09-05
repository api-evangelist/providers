---
access_model:
  confidence: high
  label: Free · No registration for the two institution-operated public endpoints
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probed
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lancaster Agentic Access
  operation_count: 1
  slug: lancaster-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- baseURL: https://eprints.lancs.ac.uk/cgi/oai2
  baseurl_source: declared
  description: The one unambiguous, institution-operated public API Lancaster runs. A single HTTP endpoint that dispatches on the OAI-PMH `verb` parameter and returns OAI-PMH 2.0 XML envelopes for the Lancaster EPri
  name: Lancaster EPrints OAI-PMH 2.0 Interface
  slug: lancaster-oai2-api
- baseURL: https://idp.lancs.ac.uk
  baseurl_source: declared
  description: Lancaster operates its own Shibboleth Identity Provider and self-publishes its SAML 2.0 EntityDescriptor at the canonical /idp/shibboleth location. The entity has been registered with the UK Access Fe
  name: Lancaster Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: identity-federation
- description: Lancaster's research information system and public research directory. The data — outputs, people, projects, impact — is Lancaster's; the platform and the contract are Elsevier's. research.lancaster-u
  name: Lancaster Research Directory (Elsevier Pure) — tenant
  slug: pure-research-directory
- description: 'Lancaster University Library runs on the Ex Libris platform: Primo VE for discovery (OneSearch, view identifier 44LAN_INST:LUL_VU1) and Alma for the library services platform behind it, whose getUser '
  name: Lancaster Library Discovery and Services (Ex Libris Alma / Primo VE) — tenant
  slug: library-discovery
- description: An AWS serverless application written and maintained by Lancaster University Library that listens for Ex Libris Alma webhook events and forwards them to backend SNS topics. It is Lancaster's own code,
  name: Lancaster Library Alma Webhook Handler (open source)
  slug: alma-webhook-handler
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lancaster EPrints OAI-PMH 2.0 Interface Oai2 API
  slug: open-lancaster-oai2-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.lancaster.ac.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://eprints.lancs.ac.uk/cgi/oai2?verb=Identify
- group: docs
  title: ''
  type: APIReference
  url: https://eprints.lancs.ac.uk/cgi/oai2?verb=ListMetadataFormats
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lancaster-university
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lulibrary
- group: other
  title: ''
  type: ResearchRepository
  url: https://eprints.lancs.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.lancaster-university.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://onesearch.lancaster-university.uk/discovery/search?vid=44LAN_INST:LUL_VU1
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.lancaster.ac.uk/study/undergraduate/courses/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.lancs.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: http://mdq.ukfederation.org.uk/entities/https%3A%2F%2Fidp.lancs.ac.uk%2Fidp%2Fshibboleth
- group: other
  title: ''
  type: AIPolicy
  url: https://www.lancaster.ac.uk/embed-digital/digital-teaching-and-learning/generative-artificial-intelligence/
- group: build
  title: ''
  type: AITooling
  url: https://www.lancaster.ac.uk/iss/itpi/luca-lancaster-university-careers-assistant/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lancaster.ac.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lancaster.ac.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.lancaster.ac.uk/iss/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/lancaster-university/
- group: design
  title: ''
  type: Conformance
  url: conformance/lancaster-education-standards-conformance.yml
- group: design
  title: ''
  type: Errors
  url: errors/lancaster-errors.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lancaster-authentication.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/lancaster-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lancaster-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lancaster-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lancaster-domain-security.yml
- group: design
  title: ''
  type: Rules
  url: rules/lancaster-rules.yml
- group: design
  title: ''
  type: Rules
  url: rules/lancaster-jsonschema-spectral-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/lancaster-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lancaster-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lancaster-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Lancaster University is a collegiate public research university in Lancaster, United Kingdom, a member of the N8 Research Partnership and, at the time of writing, not a Russell Group member. It operates no central developer portal, no API gateway, no API key programme and no published API programme, and this profile records that plainly. What it does operate, on hosts it owns, is a small but genuine set of machine-readable surfaces: the Lancaster EPrints institutional repository answers a complete, unauthenticated OAI-PMH 2.0 interface at eprints.lancs.ac.uk with seven metadata formats including RIOXX and uketd_dc, and Lancaster runs its own Shibboleth Identity Provider at idp.lancs.ac.uk, self-publishing SAML 2.0 metadata and registered with the UK Access Federation since 2014 and exported to eduGAIN. Both are institution-operated and both are recorded here as such. Two further surfaces look like Lancaster''s and are not: the research directory at research.lancaster-university.uk
  CNAMEs to lancaster.elsevierpure.com and the OneSearch discovery layer CNAMEs to lancaster.primo.exlibrisgroup.com, so Elsevier Pure and Ex Libris Primo VE wrote those contracts, not Lancaster — they are recorded as tenant relationships and their specifications are deliberately not saved under this slug. Lancaster''s most substantial public engineering output is not an API at all: the github.com/lancaster-university organisation is where the BBC micro:bit runtime (microbit-dal) and its successor CODAL were written, and github.com/lulibrary holds the University Library''s own open-source Alma, Pure and research-data tooling.'
examples:
- key_count: 2
  name: Lancaster Getrecord Example
  slug: lancaster-getrecord-example
- key_count: 2
  name: Lancaster Identify Example
  slug: lancaster-identify-example
finops:
- name: Lancaster Finops
  service_category: Education
  slug: lancaster-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lancaster.png
json_schemas:
- name: Lancaster EPrints OAI Identify
  property_count: 7
  slug: lancaster-identify
- name: Lancaster EPrints OAI Record
  property_count: 2
  slug: lancaster-record
json_structures:
- name: Lancaster Record Structure
  property_count: 2
  slug: lancaster-record-structure
jsonld:
- class_count: 18
  name: Lancaster Context
  property_count: 3
  slug: lancaster-context
layout: provider
modified: '2026-08-30'
name: Lancaster University
nav: Providers
network: true
overview: 'Lancaster University publishes 2 APIs on the [APIs.io](https://apis.io/) network: Lancaster EPrints OAI-PMH 2.0 Interface and Lancaster Shibboleth Identity Provider (SAML 2.0 metadata). Tagged areas include University, Higher Education, Education, United Kingdom, and N8 Research Partnership.


  The Lancaster University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Lancaster University''s developer surface includes documentation, API reference, support, authentication, and 26 more developer resources.'
plans:
- name: Lancaster Plans Pricing
  plan_count: 2
  slug: lancaster-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Lancaster Rate Limits
  slug: lancaster-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Lancaster University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: lancaster-jsonschema-spectral-rules
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Lancaster University API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: lancaster-rules
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 13.6
    contract_quality: 57.9
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 23.7
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lancaster/refs/heads/main/screenshots/lancaster-2026-06-20T184256.png
security:
- kind: authentication
  name: Lancaster Authentication
  slug: lancaster-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lancaster Domain Security
  slug: lancaster-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lancaster Vulnerability Disclosure
  slug: lancaster-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: lancaster
tags:
- University
- Higher Education
- Education
- United Kingdom
- N8 Research Partnership
- Research Data
- Institutional Repository
- Identity Federation
- Library
- Open-Source
website: https://www.lancaster.ac.uk/
---
