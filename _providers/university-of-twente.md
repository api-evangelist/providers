---
access_model:
  confidence: high
  label: Free · public · no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - openapi
  - probed
  trial: false
  try_now: true
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
    dry_run_mode: false
    dynamic_client_registration: false
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
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The university's own API, and the only contract in this profile it wrote. A public, unauthenticated REST service on the university's own network (energyapi.utwente.nl, 130.89.3.170, ASP.NET Core / Kes
  name: University of Twente Energy API
  slug: energy-api
- description: The university's own SAML 2.0 identity provider, entityID https://sts.windows.net/723246a1-c3f5-43c5-acdc-43adb404ac4d/, running on a Microsoft Entra ID tenant in the EU region and registered in SURFc
  name: University of Twente SAML 2.0 Identity Provider (SURFconext)
  slug: saml-idp-surfconext
- description: A live Erasmus Without Paper discovery manifest served on a University of Twente hostname, declaring fifteen EWP APIs with every endpoint URL scoped to the HEI ID utwente.nl — institutions, organizati
  name: University of Twente Erasmus Without Paper Node
  slug: ewp-mobility-node
- description: 'The University Library registers DOIs with Crossref in the university''s own name. Crossref member 2372, "University Library/University of Twente", located AE Enschede, Netherlands, holding DOI prefix '
  name: University of Twente Library Crossref Membership
  slug: crossref-membership
- description: The university's research information system and publication repository, at research.utwente.nl with the back-office at ris.utwente.nl and persistent-URL resolvers at purl.utwente.nl and doc.utwente.n
  name: UT Research Information (Elsevier Pure)
  slug: pure-research-information
- description: The university's learning management system, canvas.utwente.nl, a CNAME to utwente-vanity.instructure.com. Its LTI 1.3 platform JWKS at /api/lti/security/jwks is public and returns three RS256 signing
  name: University of Twente Canvas LMS Tenant
  slug: canvas-lms
- description: The registrar and course-registration system. osiris.utwente.nl redirects to utwente.osiris-student.nl, an institution-specific subdomain on CACI's OSIRIS platform (213.206.219.219). This is where the
  name: University of Twente OSIRIS Student Information System
  slug: osiris-student-information
- description: 4TU.ResearchData is the research-data repository the University of Twente co-founded, hosted and governed by TU Delft on the open-source djehuty platform at data.4tu.nl. The university holds two named
  name: University of Twente collections in 4TU.ResearchData
  slug: 4tu-researchdata
- description: A machine-readable study-programme document the university serves from its own web root at www.utwente.nl/llms.txt, addressed explicitly at language models. It carries organisation identity, English a
  name: University of Twente llms.txt Programme Catalog
  slug: llms-txt
artifact_total: 29
common:
- group: company
  title: ''
  type: Website
  url: https://www.utwente.nl/en/
- group: docs
  title: ''
  type: APIReference
  url: https://energyapi.utwente.nl/
- group: other
  title: ''
  type: OpenData
  url: https://energydata.utwente.nl/
- group: docs
  title: ''
  type: Documentation
  url: https://www.utwente.nl/en/sustainability/sustainability-on-campus/resources/open-data/
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.surfconext.nl/idps-metadata.xml
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.utwente.nl/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.utwente.nl/llms.txt
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.utwente.nl/en/service-portal/university-library/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.utwente.nl/en/service-portal/dossiers/ai/
- group: build
  title: ''
  type: AITooling
  url: https://www.utwente.nl/en/cyber-safety/ai-act/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/utwente
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/utwente-fmt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.utwente.nl/en/about-our-website/disclaimer/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.utwente.nl/en/about-our-website/
- group: auth
  title: ''
  type: Security
  url: https://www.utwente.nl/en/cyber-safety/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-twente-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-twente-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://www.utwente.nl/en/service-portal/
- group: company
  title: ''
  type: Blog
  url: https://www.utwente.nl/en/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-twente/
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-twente-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-twente-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-twente-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Twente (Universiteit Twente, UT), founded in 1961 in Enschede, Netherlands, is a public technical research university. Its programmable footprint is small but, unusually for this cohort, not empty and not borrowed: the university operates one API of its own. The University of Twente Energy API at energyapi.utwente.nl publishes an OpenAPI 3.0.1 contract and a Swagger UI, requires no authentication, and serves historical electricity, gas, heat, water and solar metering for 103 named campus resources — with a CO2-equivalent mode computed against the Dutch national energy mix — from the university''s own network. It backs the public Energy Data Platform at energydata.utwente.nl. Around that single owned contract, everything else is a relationship rather than an engineering artifact, and is recorded as such. The university runs its own SAML 2.0 identity provider on a Microsoft Entra ID tenant, registered in the SURFconext national federation with the Shibboleth
  scope utwente.nl — the strongest institution-operated surface it has after the Energy API. Its library is a Crossref member in its own name (prefix 10.3990). It publishes a live Erasmus Without Paper node declaring fifteen student-mobility APIs scoped to HEI ID utwente.nl. Its research information system, learning management system, student information system and research-data repository are all tenancies on Elsevier Pure, Instructure Canvas, CACI OSIRIS and 4TU.ResearchData respectively — real institutional facts, none of them the university''s contract. There is no central developer portal, no API catalog and no published terms for the one API that exists. A previously catalogued OAI-PMH endpoint on the Pure host was re-probed on 2026-09-01 and does not respond; that claim has been corrected rather than carried forward.'
examples:
- key_count: 10
  name: University Of Twente Energy Dashboard Example
  slug: university-of-twente-energy-dashboard-example
- key_count: 10
  name: University Of Twente Energy Resources Example
  slug: university-of-twente-energy-resources-example
- key_count: 10
  name: University Of Twente Energy Series Example
  slug: university-of-twente-energy-series-example
finops:
- name: University Of Twente Finops
  service_category: Education
  slug: university-of-twente-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-twente.png
json_schemas:
- name: Building
  property_count: 2
  slug: building
- name: Dashboard
  property_count: 3
  slug: dashboard
- name: Data Point
  property_count: 3
  slug: data-point
- name: Energy Response
  property_count: 2
  slug: energy
- name: Measure
  property_count: 3
  slug: measure
- name: Resource Response
  property_count: 2
  slug: resource
- name: Result
  property_count: 2
  slug: result
- name: Saving
  property_count: 5
  slug: saving
jsonld:
- class_count: 16
  name: University Of Twente Context
  property_count: 4
  slug: university-of-twente-context
layout: provider
modified: '2026-09-01'
name: University of Twente
nav: Providers
network: true
overview: 'University of Twente publishes 1 API on the [APIs.io](https://apis.io/) network: Energy API. Tagged areas include University, Higher Education, Education, Technical University, and Netherlands.


  The University of Twente catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Twente''s developer surface includes API reference, documentation, support, engineering blog, and 20 more developer resources.'
plans:
- name: University Of Twente Plans Pricing
  plan_count: 2
  slug: university-of-twente-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: University Of Twente Rate Limits
  slug: university-of-twente-rate-limits
rules:
- effective_rule_count: 11
  extends: []
  name: University of Twente API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 4
    warn: 6
  slug: university-of-twente-openapi-spectral-rules
scopes:
- name: University Of Twente Scopes
  scope_count: 0
  slug: university-of-twente-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 17
    catalog_gap: 35.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 39.2
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 61.4
    contract_quality: 59.2
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 61.4
    operational_transparency: 36.8
  previous_composite: 20.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 90.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-twente/refs/heads/main/screenshots/university-of-twente-2026-06-20T200328.png
security:
- kind: authentication
  name: University Of Twente Authentication
  slug: university-of-twente-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Twente Domain Security
  slug: university-of-twente-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: University Of Twente Vulnerability Disclosure
  slug: university-of-twente-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-twente
tags:
- University
- Higher Education
- Education
- Technical University
- Netherlands
- Europe
- Open Data
- Energy
- Sustainability
- Research Data
- Identity Federation
- Student Mobility
- Open Science
website: https://www.utwente.nl/en/
---
