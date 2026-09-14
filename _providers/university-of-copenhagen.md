---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
api_count: 1
apis:
- baseURL: https://curis.ku.dk/ws/oai
  baseurl_source: declared
  description: A complete, unauthenticated OAI-PMH 2.0 repository operated by the university on its own host. verb=Identify names the repository "University of Copenhagen", gives adminEmail curis@adm.ku.dk and attri
  name: University of Copenhagen CURIS OAI-PMH Repository Interface
  slug: curis-oai-pmh
- description: The university publishes a signed SAML 2.0 EntityDescriptor at https://id.ku.dk/nidp/saml2/metadata (200, 24,737 bytes, text/xml), entityID https://id.ku.dk/nidp/saml2/metadata. Three ku.dk SAML entit
  name: University of Copenhagen SAML 2.0 Identity Provider
  slug: identity-federation
- description: The Natural History Museum of Denmark, a University of Copenhagen faculty museum, publishes thirteen Darwin Core Archive exports from the Faculty of Science's own host specify-snm.science.ku.dk — ento
  name: Natural History Museum of Denmark Darwin Core Archive Feeds
  slug: nhmd-darwin-core
- description: ERDA (erda.ku.dk, erda.dk, sid.erda.dk) is the university's research data archive, operated by the SCIENCE HPC Center at the Faculty of Science and skinned erda-ucph-science. UCPH users authenticate t
  name: Electronic Research Data Archive (ERDA) and SCIENCE HPC Center
  slug: erda
- description: kurser.ku.dk is the university's course catalogue, on a Copenhagen hostname running on Arcanic infrastructure (courses.loadbalancer.arcanic.dk). It serves human-readable course pages keyed by course c
  name: University of Copenhagen Course Catalogue
  slug: course-catalog
- description: 'researchprofiles.ku.dk is the university''s public research portal and the front end of CURIS. It is an Elsevier Pure tenancy, not Copenhagen''s engineering: the hostname CNAMEs researchprofiles.ku.dk -'
  name: University of Copenhagen Research Portal (Elsevier Pure tenancy)
  slug: research-portal-pure
- description: 'The university is an active DataCite member — provider symbol XIZZ, memberType consortium_organization, isActive true — with two registered repositories: xizz.curis ("CURIS", pointed at researchprofil'
  name: University of Copenhagen DataCite Membership (XIZZ)
  slug: datacite-xizz
- description: 'github.com/ku-kom is the university''s GitHub account — a User account rather than an Organization, named "University of Copenhagen" and linked to www.ku.dk — publishing 52 public repositories: the KU '
  name: University of Copenhagen Web Platform Source (ku-kom)
  slug: ku-kom-github
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-copenhagen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ku.dk/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ku-kom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ku-kom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-copenhagen/
- group: company
  title: ''
  type: Blog
  url: https://news.ku.dk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchprofiles.ku.dk/
- group: other
  title: ''
  type: IdentityFederation
  url: https://id.ku.dk/nidp/saml2/metadata
- group: other
  title: ''
  type: OpenData
  url: https://specify-snm.science.ku.dk/static/depository/export_feed/DwCA-QZ.zip
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.ku.dk/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://kurser.ku.dk/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-copenhagen-curis-oai-pmh-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-copenhagen-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/university-of-copenhagen-oai-pmh-errors.yml
- group: build
  title: ''
  type: Examples
  url: examples/university-of-copenhagen-curis-oai-pmh-examples.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-copenhagen-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-copenhagen-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-copenhagen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-copenhagen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-copenhagen-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Copenhagen (Københavns Universitet, UCPH), founded in 1479, is Denmark''s oldest and largest university and one of the leading research institutions in the Nordic region. It operates no central developer portal, no REST API program and no open-data portal — api.ku.dk and developer.ku.dk do not resolve, and data.ku.dk redirects to the homepage. What it does operate, and what makes it unusually well-covered for this cohort, is a set of standards-based machine-readable surfaces on its own infrastructure: a complete OAI-PMH 2.0 repository at curis.ku.dk serving 440,535 research records across 7,430 sets in six metadata formats; a signed SAML 2.0 identity provider at id.ku.dk registered in the Danish WAYF federation; and thirteen Darwin Core Archive feeds published by the Natural History Museum of Denmark from specify-snm.science.ku.dk and harvested by GBIF. Its public research portal researchprofiles.ku.dk is by contrast an Elsevier Pure tenancy — it CNAMEs to
  ku.elsevierpure.com and its REST contract is Elsevier''s, api-key gated — and is recorded here as a tenant relationship rather than as the university''s own API. The only source code the institution publishes is the ku-kom GitHub account: 52 repositories of TYPO3 content elements and a Bootstrap styleguide that build the ku.dk web platform.'
finops:
- name: University Of Copenhagen Finops
  service_category: Education
  slug: university-of-copenhagen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-copenhagen.png
jsonld:
- class_count: 9
  name: University Of Copenhagen Context
  property_count: 6
  slug: university-of-copenhagen-context
layout: provider
modified: '2026-08-30'
name: University of Copenhagen
nav: Providers
network: true
overview: 'University of Copenhagen publishes 1 API on the [APIs.io](https://apis.io/) network: CURIS OAI-PMH Repository Interface. Tagged areas include Education, Higher Education, University, Research, and Denmark.


  The University of Copenhagen catalog on APIs.io includes 1 JSON-LD context.


  University of Copenhagen''s developer surface includes GitHub presence, engineering blog, authentication, code examples, and 17 more developer resources.'
plans:
- name: University Of Copenhagen Plans Pricing
  plan_count: 2
  slug: university-of-copenhagen-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: University Of Copenhagen Rate Limits
  slug: university-of-copenhagen-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-copenhagen/refs/heads/main/screenshots/university-of-copenhagen-2026-06-20T200145.png
security:
- kind: authentication
  name: University Of Copenhagen Authentication
  slug: university-of-copenhagen-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Copenhagen Domain Security
  slug: university-of-copenhagen-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-copenhagen
tags:
- Education
- Higher Education
- University
- Research
- Denmark
- Nordic
- Open-Source
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
- Open Data
- Research Computing
- Course Catalog
- Biodiversity
website: https://www.ku.dk/en
---
