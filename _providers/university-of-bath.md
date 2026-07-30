---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 183
  human_in_the_loop: 1
  name: University Of Bath Agentic Access
  operation_count: 663
  slug: university-of-bath-agentic-access
  summary_line: 663 operations · 183 acting · 1 human-in-the-loop
api_count: 26
apis:
- description: OAI-PMH 2.0 metadata harvesting interface for the University of Bath Open Access Repository, served by the institution's Elsevier Pure research information system. Confirmed live via the Identify verb
  name: Research Portal (Pure) OAI-PMH
  slug: pure-oai
- description: OAI-PMH 2.0 metadata harvesting endpoint for the University of Bath Research Data Archive, an EPrints 3.4 institutional data repository. Confirmed live; the archive footer advertises OAI 2.0 support a
  name: Research Data Archive OAI-PMH
  slug: researchdata-oai
- description: EPrints REST/XML interface and Atom/RSS feeds for the University of Bath Research Data Archive, exposing dataset records and search. The /rest path resolves (HTTP 200); EPrints provides RSS 1.0, RSS 2
  name: Research Data Archive REST/Feeds
  slug: researchdata-rest
- description: The University of Bath library catalogue runs on Ex Libris Alma with the Primo discovery service. Primo VE exposes search/discovery interfaces (Primo REST/Search APIs) typically requiring an Ex Libris
  name: Library Discovery (Ex Libris Primo)
  slug: primo-discovery
- description: The University operates a Microsoft Azure API Management developer portal. The publicly reachable instance is a non-production "test" environment (portal.apim.test.bath.ac.uk, HTTP 200) with sign-in/s
  name: Azure API Management Developer Portal (non-production)
  slug: apim-portal
- description: The activity API from University of Bath — 38 operation(s) for activity.
  name: University of Bath activity API
  slug: university-of-bath-activity-api
- description: The application API from University of Bath — 36 operation(s) for application.
  name: University of Bath application API
  slug: university-of-bath-application-api
- description: The authorCollaboration API from University of Bath — 9 operation(s) for authorcollaboration.
  name: University of Bath authorCollaboration API
  slug: university-of-bath-authorcollaboration-api
- description: The award API from University of Bath — 35 operation(s) for award.
  name: University of Bath award API
  slug: university-of-bath-award-api
- description: The classificationScheme API from University of Bath — 7 operation(s) for classificationscheme.
  name: University of Bath classificationScheme API
  slug: university-of-bath-classificationscheme-api
- description: The dataSet API from University of Bath — 29 operation(s) for dataset.
  name: University of Bath dataSet API
  slug: university-of-bath-dataset-api
- description: The equipment API from University of Bath — 26 operation(s) for equipment.
  name: University of Bath equipment API
  slug: university-of-bath-equipment-api
- description: The event API from University of Bath — 21 operation(s) for event.
  name: University of Bath event API
  slug: university-of-bath-event-api
- description: The externalOrganization API from University of Bath — 29 operation(s) for externalorganization.
  name: University of Bath externalOrganization API
  slug: university-of-bath-externalorganization-api
- description: The externalPerson API from University of Bath — 22 operation(s) for externalperson.
  name: University of Bath externalPerson API
  slug: university-of-bath-externalperson-api
- description: The journal API from University of Bath — 22 operation(s) for journal.
  name: University of Bath journal API
  slug: university-of-bath-journal-api
- description: The organization API from University of Bath — 33 operation(s) for organization.
  name: University of Bath organization API
  slug: university-of-bath-organization-api
- description: The person API from University of Bath — 57 operation(s) for person.
  name: University of Bath person API
  slug: university-of-bath-person-api
- description: The pressMedia API from University of Bath — 24 operation(s) for pressmedia.
  name: University of Bath pressMedia API
  slug: university-of-bath-pressmedia-api
- description: The prize API from University of Bath — 28 operation(s) for prize.
  name: University of Bath prize API
  slug: university-of-bath-prize-api
- description: The project API from University of Bath — 33 operation(s) for project.
  name: University of Bath project API
  slug: university-of-bath-project-api
- description: The publisher API from University of Bath — 18 operation(s) for publisher.
  name: University of Bath publisher API
  slug: university-of-bath-publisher-api
- description: The researchOutput API from University of Bath — 66 operation(s) for researchoutput.
  name: University of Bath researchOutput API
  slug: university-of-bath-researchoutput-api
- description: The role API from University of Bath — 2 operation(s) for role.
  name: University of Bath role API
  slug: university-of-bath-role-api
- description: The studentThesis API from University of Bath — 26 operation(s) for studentthesis.
  name: University of Bath studentThesis API
  slug: university-of-bath-studentthesis-api
- description: The user API from University of Bath — 7 operation(s) for user.
  name: University of Bath user API
  slug: university-of-bath-user-api
artifact_total: 50
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/university-of-bath-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bath-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-bath-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bath.ac.uk/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uniofbathdmc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-bath/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.apim.test.bath.ac.uk/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bath-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bath-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bath-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Bath is a public research university in Bath, United Kingdom, ranked #150 in the QS World University Rankings 2025. Its public, machine-readable developer footprint is centered on scholarly metadata rather than a commercial developer program: an Elsevier Pure research portal exposing an OAI-PMH interface, an EPrints 3.4 Research Data Archive with OAI-PMH and a REST interface, and an Ex Libris Alma/Primo library discovery platform. The University operates an Azure API Management developer portal, but the publicly reachable instance is a non-production ("test") environment with no openly documented production APIs. Administrative and identity services are gated behind institutional affiliation.'
examples:
- key_count: 3
  name: University Of Bath Activity List Example
  slug: university-of-bath-activity-list-example
- key_count: 3
  name: University Of Bath Dataset List Example
  slug: university-of-bath-dataset-list-example
- key_count: 3
  name: University Of Bath Organization List Example
  slug: university-of-bath-organization-list-example
- key_count: 3
  name: University Of Bath Person List Example
  slug: university-of-bath-person-list-example
- key_count: 3
  name: University Of Bath Researchoutput List Example
  slug: university-of-bath-researchoutput-list-example
finops:
- name: University Of Bath Finops
  service_category: Education
  slug: university-of-bath-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bath.png
json_schemas:
- name: University of Bath Pure API Activity
  property_count: 36
  slug: university-of-bath-activity
- name: University of Bath Pure API DataSet
  property_count: 52
  slug: university-of-bath-dataset
- name: University of Bath Pure API Organization
  property_count: 31
  slug: university-of-bath-organization
- name: University of Bath Pure API Person
  property_count: 49
  slug: university-of-bath-person
- name: University of Bath Pure API ResearchOutput
  property_count: 48
  slug: university-of-bath-researchoutput
json_structures:
- name: University Of Bath Activity Structure
  property_count: 36
  slug: university-of-bath-activity-structure
- name: University Of Bath Dataset Structure
  property_count: 52
  slug: university-of-bath-dataset-structure
- name: University Of Bath Organization Structure
  property_count: 31
  slug: university-of-bath-organization-structure
- name: University Of Bath Person Structure
  property_count: 49
  slug: university-of-bath-person-structure
- name: University Of Bath Researchoutput Structure
  property_count: 48
  slug: university-of-bath-researchoutput-structure
jsonld:
- class_count: 17
  name: University Of Bath Context
  property_count: 12
  slug: university-of-bath-context
layout: provider
modified: '2026-06-03'
name: University of Bath
nav: Providers
network: true
overview: 'University of Bath publishes 21 APIs on the [APIs.io](https://apis.io/) network, including activity API, application API, authorCollaboration API, and 18 more. Tagged areas include Education, Higher Education, University, United Kingdom, and Research.


  The University of Bath catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of Bath''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: University Of Bath Plans Pricing
  plan_count: 2
  slug: university-of-bath-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: University Of Bath Rate Limits
  slug: university-of-bath-rate-limits
rules:
- name: University of Bath API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: university-of-bath-jsonschema-spectral-rules
- name: University of Bath API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 1
    info: 0
    warn: 3
  slug: university-of-bath-rules
score:
  band: thin
  composite: 39.7
  delta: -5.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.0
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bath/refs/heads/main/screenshots/university-of-bath-2026-06-20T200134.png
security:
- kind: authentication
  name: University Of Bath Authentication
  slug: university-of-bath-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: University Of Bath Domain Security
  slug: university-of-bath-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-bath
tags:
- Education
- Higher Education
- University
- United Kingdom
- Research
- Open Data
- Library
- Metadata
website: https://www.bath.ac.uk/
---
