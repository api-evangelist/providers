---
access_model:
  confidence: high
  label: Free — CIViC reads anonymously, an optional key is free; everything else is gated
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  - documentation
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
api_count: 10
apis:
- description: A free, open, community-curated knowledgebase of the clinical significance of variants in cancer, built and operated by The McDonnell Genome Institute at Washington University School of Medicine and r
  name: CIViC — Clinical Interpretation of Variants in Cancer
  slug: civic
- description: Institutional integration APIs published in a MuleSoft Anypoint Exchange tenant and described publicly as "Data at WashU", covering the Person, Financial, Supplier, Location, Academic and Organization
  name: WashU Enterprise Integration APIs (MuleSoft Anypoint)
  slug: enterprise-apis
- description: Washington University's own SAML 2.0 identity provider, entityID https://login.wustl.edu/idp/shibboleth, published as signed metadata through the InCommon per-entity metadata query service. The docume
  name: WashU Shibboleth Identity Provider (InCommon)
  slug: incommon-idp
- description: The university's institutional repository, "WashU Scholarly Repository", serving a live OAI-PMH 2.0 interface with nine metadata formats including oai_etdms for theses and oai_openaire for OpenAIRE ha
  name: WashU Scholarly Repository (OAI-PMH)
  slug: open-scholarship
- description: The Becker Medical Library and School of Medicine research data repository, publishing an API documentation page and a live OAI-PMH 2.0 endpoint that serves the datacite, oai_datacite and oai_dc metad
  name: Digital Commons Data@Becker (Research Data Repository)
  slug: digital-commons-data
- description: Washington University in St. Louis Libraries is a DataCite direct member, symbol WUSTL, registered 2018-08-30, region AMER, and linked from DataCite's own record to https://ror.org/01yc7t268 — the sam
  name: DataCite Membership — Washington University in St. Louis Libraries
  slug: datacite
- description: The institution's Research Organization Registry record, https://ror.org/01yc7t268, carrying its display name, multilingual name variants, the WUSTL acronym, a St. Louis location, and cross-references
  name: ROR Registration — Washington University in St. Louis
  slug: ror
- description: 'Every WashU departmental site probed exposes a live, unauthenticated WordPress REST API with a complete route discovery document — data.wustl.edu ("Data at WashU", 467 routes), source.washu.edu ("The '
  name: WashU WordPress REST APIs (CampusPress)
  slug: wordpress-rest
- description: WashU's neuroimaging data archive, running XNAT — imaging informatics software that originated at the university's own Neuroinformatics Research Group. cnda.wustl.edu resolves inside WashU's network a
  name: CNDA — Central Neuroimaging Data Archive (XNAT)
  slug: cnda
- description: 'A WashU-operated database of neuroimaging scenes and datasets at balsa.wustl.edu, and now the destination of db.humanconnectome.org, which CNAMEs to proxy.nrg.wustl.edu and redirects here — the Human '
  name: BALSA Neuroimaging Database
  slug: balsa
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://washu.edu
- group: company
  title: ''
  type: Website
  url: https://wustl.edu
- group: docs
  title: ''
  type: Documentation
  url: https://data.wustl.edu/api-portal/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.civicdb.org/en/latest/api.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.wustl.edu/api-portal/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WashU-IT-RIS
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wustl
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/washington-university-in-st-louis/
- group: other
  title: ''
  type: ResearchRepository
  url: https://openscholarship.wustl.edu/
- group: other
  title: ''
  type: ResearchRepository
  url: https://digitalcommonsdata.wustl.edu/
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/https%3A%2F%2Flogin.wustl.edu%2Fidp%2Fshibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://ris.wustl.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://registrar.washu.edu/
- group: other
  title: ''
  type: AIPolicy
  url: https://ai.washu.edu/
- group: build
  title: ''
  type: AITooling
  url: https://ai.washu.edu/tools/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://registrar.washu.edu/student-records-resources/ferpa-overview/
- group: operate
  title: ''
  type: Support
  url: https://it.washu.edu/
- group: company
  title: ''
  type: Blog
  url: https://source.washu.edu/
- group: company
  title: ''
  type: BlogRSS
  url: https://source.washu.edu/feed/
- group: docs
  title: ''
  type: GraphQL
  url: graphql/washington-university-in-st-louis-civic-schema.graphql
- group: auth
  title: ''
  type: Authentication
  url: authentication/washington-university-in-st-louis-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/washington-university-in-st-louis-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/washington-university-in-st-louis-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/washington-university-in-st-louis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/washington-university-in-st-louis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/washington-university-in-st-louis-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/washington-university-in-st-louis-context.jsonld
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Washington University in St. Louis (WashU) is a private research university in St. Louis, Missouri, now presenting itself on washu.edu with the historic wustl.edu domain redirecting to it. Its programmable footprint is small but, unusually for this cohort, not empty and not entirely someone else''s: the McDonnell Genome Institute at WashU School of Medicine builds and operates CIViC, the Clinical Interpretation of Variants in Cancer knowledgebase, whose public GraphQL API at civicdb.org/api/graphql answers anonymous introspection with a 502-type schema, 112 root queries and 47 mutations, documents a bearer-token API key and a 3 request/second rate limit, and is released CC0. WashU also operates its own Shibboleth SAML 2.0 identity provider, published as signed metadata in InCommon with REFEDS Research & Scholarship and SIRTFI assurance — machine readable institutional infrastructure almost no university in this cohort catalogues. Its enterprise integration APIs (Person, Financial,
  Supplier, Location, Academic, Organization) are real but wholly gated: they live in a MuleSoft Anypoint Exchange tenant and access is granted by internal ServiceNow request, with no public specification, endpoint or sign-up. Everything else is a relationship rather than WashU engineering. The two research repositories that harvest cleanly over OAI-PMH 2.0 — the WashU Scholarly Repository and Digital Commons Data@Becker — both sit on wustl.edu hostnames that CNAME straight to Elsevier infrastructure (bepress and Mendeley Data), so the data and the DOIs are WashU''s and the contracts are Elsevier''s. WashU is a DataCite direct member with two registered repositories. There is no public open-data portal, no documented course or SIS API, and courses.wustl.edu no longer answers at all.'
finops:
- name: Washington University In St Louis Finops
  service_category: Education
  slug: washington-university-in-st-louis-finops
graphqls:
- description: '```yaml'
  name: CIViC GraphQL API — Washington University in St. Louis
  slug: washington-university-in-st-louis-civic
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/washington-university-in-st-louis.png
jsonld:
- class_count: 32
  name: Washington University In St Louis Context
  property_count: 5
  slug: washington-university-in-st-louis-context
layout: provider
modified: '2026-09-01'
name: Washington University in St. Louis
nav: Providers
network: true
overview: 'Washington University in St. Louis publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, United States, and Missouri.


  The Washington University in St. Louis catalog on APIs.io includes 1 JSON-LD context.


  Washington University in St. Louis'' developer surface includes documentation, API reference, GitHub presence, support, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Washington University In St Louis Plans Pricing
  plan_count: 2
  slug: washington-university-in-st-louis-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Washington University In St Louis Rate Limits
  slug: washington-university-in-st-louis-rate-limits
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 60.0
    catalog_earned_first_party: 12.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 50.6
    developer_ergonomics: 52.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.4
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/washington-university-in-st-louis/refs/heads/main/screenshots/washington-university-in-st-louis-2026-06-20T201236.png
security:
- kind: authentication
  name: Washington University In St Louis Authentication
  slug: washington-university-in-st-louis-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Washington University In St Louis Domain Security
  slug: washington-university-in-st-louis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: washington-university-in-st-louis
tags:
- University
- Higher Education
- Education
- United States
- Missouri
- Private Research University
- Research Data
- Research Repository
- Identity Federation
- Genomics
- Bioinformatics
- GraphQL
- OAI-PMH
- Shibboleth
- DataCite
- MuleSoft
website: https://washu.edu
---
