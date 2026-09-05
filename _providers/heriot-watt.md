---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
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
  scored_at: '2026-09-04'
api_count: 6
apis:
- description: The university's own institutional repository of theses and research outputs, running DSpace 8 on www.ros.hw.ac.uk — a host under Heriot-Watt's registrable domain with a matching PTR record, an open.a
  name: Heriot-Watt Research Output Service (ROS)
  slug: research-output-service
- description: Heriot-Watt operates its own SAML 2.0 / Shibboleth identity provider and is a registered member of the UK Access Management Federation (registrationAuthority http://ukfederation.org.uk), which in turn
  name: Heriot-Watt University Identity Provider (UK Access Management Federation)
  slug: identity-federation
- description: Heriot-Watt's public research information portal — publications, projects, research data, activities and researcher profiles. It carries a hw.ac.uk hostname but is not institution-operated infrastruct
  name: Heriot-Watt Research Portal (Elsevier Pure)
  slug: research-portal
- description: Library discovery and catalog search for Heriot-Watt's Edinburgh, Scottish Borders, Orkney, Dubai and Malaysia libraries, running Ex Libris Primo under the institution's view code 44HWA_V1 at discover
  name: Heriot-Watt Library Discovery (Ex Libris Primo)
  slug: library-discovery
- description: The university's virtual learning environment, an Instructure Canvas tenancy at canvas.hw.ac.uk (CNAME hwu-vanity.instructure.com). Canvas ships a documented REST API and LTI 1.3 platform role as prod
  name: Heriot-Watt Canvas (Instructure)
  slug: canvas
- description: Springshare LibCal tenancy for library room bookings, events and opening hours at hw.ac.libcal.com (CNAME region-eu.libcal.com). LibCal's REST API exists at this host — the OAuth2 token endpoint /1.1/
  name: Heriot-Watt LibCal (Springshare)
  slug: libcal
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.hw.ac.uk/
- group: company
  title: ''
  type: About
  url: https://www.hw.ac.uk/about/professional-services/information-services/find-resources
- group: operate
  title: ''
  type: Status
  url: https://www.hwstatus.info/
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/school/heriot-watt-university/
- group: company
  title: ''
  type: Blog
  url: https://www.hw.ac.uk/news/blog
- group: operate
  title: ''
  type: Support
  url: https://www.hw.ac.uk/about/professional-services/information-services/contact-visit-us/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hw.ac.uk/about/our-policies/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hw.ac.uk/about/professional-services/governance-and-legal-services/information-governance/protect-information/data-protection-overview/privacy-and-your-data-rights
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.ros.hw.ac.uk/
- group: docs
  title: ''
  type: APIReference
  url: https://www.ros.hw.ac.uk/server/api
- group: other
  title: ''
  type: IdentityFederation
  url: http://mdq.ukfederation.org.uk/entities/https%3A%2F%2Fshib1.hw.ac.uk%2Fshibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://discovery.hw.ac.uk/primo-explore/search?vid=44HWA_V1
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.hw.ac.uk/search/programmes
- group: other
  title: ''
  type: OpenData
  url: https://www.hw.ac.uk/about/professional-services/governance-and-legal-services/information-governance/access-information/foi/publication-scheme/external-and-government-relations-open-data/8.19-open-data
- group: design
  title: ''
  type: Conformance
  url: conformance/heriot-watt-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/heriot-watt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heriot-watt-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/heriot-watt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heriot-watt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/heriot-watt-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Heriot-Watt University is a public research university based in Edinburgh, Scotland, with further campuses in the Scottish Borders, Orkney, Dubai and Malaysia, ROR 04mghma93. Its programmable footprint is small but — unusually for this cohort — not empty and not entirely rented. Two surfaces are genuinely institution-operated and openly callable without credentials: the Research Output Service (ROS) at www.ros.hw.ac.uk, a DSpace 8 deployment on the university''s own domain with a live OAI-PMH 2.0 endpoint and an unauthenticated DSpace REST/HAL API over its theses and research outputs; and the university''s SAML 2.0 identity provider, registered in the UK Access Management Federation as Heriot-Watt University, whose signed metadata is machine-readable through the federation''s MDQ service. Everything else that looks like a Heriot-Watt API is a vendor platform the university rents under its own name and is recorded here as a tenant relationship, not as Heriot-Watt engineering:
  the research portal at researchportal.hw.ac.uk is Elsevier Pure (the host CNAMEs to hwu.elsevierpure.com), library discovery at discovery.hw.ac.uk is Ex Libris Primo, canvas.hw.ac.uk is Instructure Canvas, and hw.ac.libcal.com is Springshare LibCal. Heriot-Watt operates no central developer portal, no public API documentation, no open-data portal and no course-catalog or timetabling API; the programme search at hw.ac.uk is server-rendered HTML with no JSON backend, and timetable.hw.ac.uk, though on the university''s own network, exposes no reachable public endpoint.'
finops:
- name: Heriot Watt Finops
  service_category: Education
  slug: heriot-watt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heriot-watt.png
jsonld:
- class_count: 11
  name: Heriot Watt Context
  property_count: 4
  slug: heriot-watt-context
layout: provider
modified: '2026-08-30'
name: Heriot-Watt University
nav: Providers
network: true
overview: 'Heriot-Watt University publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Scotland, and United Kingdom.


  The Heriot-Watt University catalog on APIs.io includes 1 JSON-LD context.


  Heriot-Watt University''s developer surface includes status page, engineering blog, support, API reference, and 17 more developer resources.'
plans:
- name: Heriot Watt Plans Pricing
  plan_count: 2
  slug: heriot-watt-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Heriot Watt Rate Limits
  slug: heriot-watt-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 32.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heriot-watt/refs/heads/main/screenshots/heriot-watt-2026-06-20T182645.png
security:
- kind: domain-security
  name: Heriot Watt Domain Security
  slug: heriot-watt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Heriot Watt Vulnerability Disclosure
  slug: heriot-watt-vulnerability-disclosure
  summary_line: security.txt
slug: heriot-watt
tags:
- University
- Higher Education
- Education
- Scotland
- United Kingdom
- Universities Scotland
- Research
- Research Data
- Institutional Repository
- Open Access
- OAI-PMH
- Identity Federation
- Library
- Learning Management
website: https://www.hw.ac.uk/
---
