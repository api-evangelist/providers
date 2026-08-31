---
access_model:
  confidence: high
  label: Free · Open harvesting endpoints · no signup
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 5
apis:
- description: 'OAI-PMH 2.0 metadata harvesting interface for the University of Bath Research Data Archive, an EPrints 3.4.7 repository the University runs on its own infrastructure (researchdata.bath.ac.uk resolves '
  name: Research Data Archive OAI-PMH
  slug: researchdata-oai
- description: 'EPrints REST/XML interface for the University of Bath Research Data Archive, on the same institution-operated host. Confirmed live 2026-08-30: /rest/ returns an "EPrints REST: Datasets" index exposing'
  name: Research Data Archive REST/XML
  slug: researchdata-rest
- description: The University's Elsevier Pure research information system exposes the Pure Web Service under a Bath hostname. The DEPLOYMENT is Bath's and the data is Bath's; the CONTRACT is Elsevier's. purehost.bat
  name: Research Portal (Elsevier Pure) Web Service — Bath tenancy
  slug: pure-ws-api
- description: OAI-PMH 2.0 harvesting interface served by the University's Elsevier Pure tenancy, advertising the OpenAIRE CERIF 1.2 profile alongside mods, qdc, nl_didl, oai_dc, xmetadiss and uketd_dc. Live but DEF
  name: Research Portal (Elsevier Pure) OAI-PMH — Bath tenancy
  slug: pure-oai
- description: The University of Bath library catalogue runs on Ex Libris Alma with Primo VE discovery. The public front end at bath.primo.exlibrisgroup.com redirects to the Bath view (vid=44BAT_INST:NDE) and return
  name: Library Discovery (Ex Libris Alma/Primo) — Bath tenancy
  slug: primo-discovery
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.bath.ac.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uniofbathdmc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-bath/
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchdata.bath.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchportal.bath.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://library.bath.ac.uk/home
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.bath.ac.uk/courses/
- group: other
  title: ''
  type: OpenData
  url: https://www.bath.ac.uk/topics/open-research/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.bath.ac.uk/professional-services/research-computing/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.bath.ac.uk/guides/student-guidance-on-uploading-documents-to-genai-tools-or-third-party-websites/
- group: build
  title: ''
  type: AITooling
  url: https://www.bath.ac.uk/announcements/support-for-students-to-use-genai-tools-effectively-and-responsibly/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bath.ac.uk/legal-information/data-protection-and-privacy-statement-summary/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bath.ac.uk/legal-information/digital-accessibility-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bath.ac.uk/services/pure/
- group: operate
  title: ''
  type: Status
  url: https://status.bath.ac.uk/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-bath-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bath-domain-security.yml
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
description: 'The University of Bath is a public research university in Bath, United Kingdom, and a member of the Russell Group. It operates no public developer program: a full crawl of its 21,530-URL sitemap on 2026-08-30 returned no developer portal, no API reference, and no published OpenAPI under any bath.ac.uk path. Its one genuinely institution-operated machine-readable surface is the Research Data Archive at researchdata.bath.ac.uk — EPrints 3.4.7 running on the University''s own infrastructure (138.38.44.144) — which serves a live OAI-PMH 2.0 interface, an EPrints REST/XML interface, and DataCite kernel-4 records carrying ORCID identifiers and DOIs under the University''s own 10.15125 prefix. Everything else that appears to be a Bath API is a vendor contract running under a Bath hostname: purehost.bath.ac.uk and researchportal.bath.ac.uk both CNAME to bath-prod.elsevierpure.com and are an Elsevier Pure tenancy; the library catalogue is an Ex Libris Alma/Primo tenancy; library.bath.ac.uk
  is Springshare LibGuides; status.bath.ac.uk is Better Stack. The programme and unit catalogue is entirely behind CAS authentication at auth.bath.ac.uk, and the student records system behind Microsoft Entra ID. An Azure API Management portal exists only as a non-production "test" instance and is not recorded as a surface. This profile is deliberately thin because the footprint is thin.'
finops:
- name: University Of Bath Finops
  service_category: Education
  slug: university-of-bath-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bath.png
layout: provider
modified: '2026-08-30'
name: University of Bath
nav: Providers
network: true
overview: 'University of Bath publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, United Kingdom, and Russell Group.


  University of Bath''s developer surface includes documentation, status page, and 19 more developer resources.'
plans:
- name: University Of Bath Plans Pricing
  plan_count: 2
  slug: university-of-bath-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: University Of Bath Rate Limits
  slug: university-of-bath-rate-limits
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -14.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 38.4
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
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bath/refs/heads/main/screenshots/university-of-bath-2026-06-20T200134.png
security:
- kind: domain-security
  name: University Of Bath Domain Security
  slug: university-of-bath-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-bath
tags:
- University
- Higher Education
- Education
- United Kingdom
- Russell Group
- Research Data
- Research Repository
- Open Data
- Library
- OAI-PMH
- Metadata
- Research Computing
website: https://www.bath.ac.uk/
---
