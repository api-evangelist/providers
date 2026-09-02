---
access_model:
  confidence: high
  label: Free · No registration (institution-operated read surfaces)
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probe
  trial: false
  try_now: true
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-01'
api_count: 12
apis:
- description: 'ASU''s own Shibboleth Identity Provider, entityID urn:mace:incommon:asu.edu, asserting the scope asu.edu. ASU publishes the signed entity descriptor from its own host at shibboleth2.asu.edu (200, 1559 '
  name: ASU Shibboleth SAML 2.0 Identity Provider
  slug: shibboleth-idp
- description: ASU's registration in the InCommon Federation, retrievable as signed SAML metadata from the InCommon MDQ service and flowing onward into eduGAIN. This is the federation-operated copy of the record who
  name: InCommon Federation registration (urn:mace:incommon:asu.edu)
  slug: incommon-federation-registration
- description: The ASU Library Research Data Repository runs on the open-source Dataverse platform, on ASU's own host, from an ASU-local build — /api/info/version returns "6.11 asu-6.11-oai-rights". The native Datav
  name: ASU Library Research Data Repository API (Dataverse)
  slug: dataverse-api
- description: OAI-PMH 2.0 metadata harvesting endpoint for the ASU Library Research Data Repository. repositoryName "ASU Library Research Data Repository Dataverse OAI Archive", adminEmail dataverse@asu.edu, earlie
  name: ASU Research Data Repository OAI-PMH
  slug: dataverse-oai
- description: OAI-PMH 2.0 endpoint for KEEP, the ASU Library digital repository, running on Islandora that ASU Library builds and deploys itself in public at github.com/asulibraries (islandora-repo, "ASU Digital Re
  name: ASU Library KEEP OAI-PMH
  slug: keep-oai
- description: OAI-PMH 2.0 endpoint for PRISM, ASU Library's second Islandora digital-collections repository. repositoryName "ASU Library | PRISM", adminEmail digitalrepository@asu.edu, earliestDatestamp 2011-05-11,
  name: ASU Library PRISM OAI-PMH
  slug: prism-oai
- description: ASU's own course, class and subject search API, running at eadvs-cscc-catalog-api.apps.asu.edu/catalog-microservices/api/v1 and consumed by the public class-search single-page application at catalog.a
  name: ASU Course Catalog microservices API
  slug: course-catalog-api
- description: ASU's internal data-platform API gateway, the issuer of the OAuth scopes the course-catalog application requests (scopes/acad-plan/read, scopes/person/read, scopes/principal/read). The host is live an
  name: myASU Data Platform API (api.myasuplat-dpl.asu.edu)
  slug: myasu-data-platform
- description: ASU operates an enterprise single sign-on service using the Central Authentication Service (CAS) protocol for authenticating ASURITE accounts across university web applications. A bare GET returns a s
  name: ASU WebAuth (CAS single sign-on)
  slug: sso-cas
- description: ASU is a DataCite member (provider symbol ASU, memberType consortium_organization, created 2020-09-22) and mints DOIs through the institutional repository account ASU.ASUL, "Arizona State University L
  name: DataCite membership and repository registration
  slug: datacite-registration
- description: ASU is a Crossref member, id 37851, primary-name "Arizona State University", located in Tempe, AZ, depositing under DOI prefix 10.58875 with 351 DOIs registered as of 2026-09-01. Recorded as a registr
  name: Crossref membership (member 37851)
  slug: crossref-registration
- description: ASU's Research Organization Registry record, ror.org/03efmqc40, established 1885, status active, domain asu.edu, carrying 11 Crossref Funder IDs, GRID grid.215654.1 and two ISNIs. A registry membershi
  name: ROR organization record (03efmqc40)
  slug: ror-registration
artifact_total: 19
common:
- group: company
  title: ''
  type: Website
  url: https://www.asu.edu/
- group: company
  title: ''
  type: Blog
  url: https://news.asu.edu/
- group: company
  title: ''
  type: BlogRSS
  url: https://news.asu.edu/rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asu.edu/privacy/
- group: operate
  title: ''
  type: Support
  url: https://links.asu.edu/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ASU
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/asulibraries
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/arizona-state-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ASU
- group: auth
  title: ''
  type: Authentication
  url: authentication/arizona-state-university-authentication.yml
- group: other
  title: ''
  type: IdentityFederation
  url: https://mdq.incommon.org/entities/urn%3Amace%3Aincommon%3Aasu.edu
- group: other
  title: ''
  type: ResearchRepository
  url: https://lib.asu.edu/research/research-data-repository
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.asu.edu/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://catalog.apps.asu.edu/catalog/classes
- group: other
  title: ''
  type: AIPolicy
  url: https://provost.asu.edu/generative-ai
- group: build
  title: ''
  type: AITooling
  url: https://ai.asu.edu/ai-tools
- group: design
  title: ''
  type: Conformance
  url: conformance/arizona-state-university-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/arizona-state-university-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arizona-state-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/arizona-state-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/arizona-state-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/arizona-state-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Arizona State University (ASU) is a large public research university based in Tempe, Arizona, United States, and one of the largest by enrolment in the country. Its programmable footprint is real but narrow, and almost none of it is presented as a developer product. ASU operates no public developer portal, no self-service API keys and no open data portal — api.asu.edu, data.asu.edu, open.asu.edu and developer.asu.edu do not resolve. What it does operate, verified by live probe on 2026-09-01, is an identity and metadata layer: a Shibboleth SAML 2.0 Identity Provider registered in the InCommon Federation under entityID urn:mace:incommon:asu.edu, serving its own signed metadata from shibboleth2.asu.edu; a CAS single sign-on service at weblogin.asu.edu; and THREE independent OAI-PMH 2.0 repositories on ASU''s own hosts — the Library Research Data Repository (a self-built Dataverse, build string asu-6.11-oai-rights, 104 datasets under DOI prefix 10.48349/ASU) plus KEEP and PRISM,
  the ASU Library Islandora deployments developed in public at github.com/asulibraries. ASU also runs its own course-catalog microservices API and a myASU data platform on its own hosts, but both are OAuth-gated and undocumented for outside developers. It is a registrant in DataCite (member ASU, repository ASU.ASUL), Crossref (member 37851, prefix 10.58875) and ROR (03efmqc40). No vendor contract is held under this slug: the repository software ASU runs is open source and self-hosted, and the specification for it belongs to the projects that wrote it, not to ASU.'
finops:
- name: Arizona State University Finops
  service_category: Education
  slug: arizona-state-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arizona-state-university.png
jsonld:
- class_count: 11
  name: Arizona State University Context
  property_count: 2
  slug: arizona-state-university-context
layout: provider
modified: '2026-09-01'
name: Arizona State University
nav: Providers
network: true
overview: 'Arizona State University publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, United States, and Arizona.


  The Arizona State University catalog on APIs.io includes 1 JSON-LD context.


  Arizona State University''s developer surface includes engineering blog, support, authentication, and 20 more developer resources.'
plans:
- name: Arizona State University Plans Pricing
  plan_count: 2
  slug: arizona-state-university-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Arizona State University Rate Limits
  slug: arizona-state-university-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 7.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 17.3
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/arizona-state-university/refs/heads/main/screenshots/arizona-state-university-2026-06-20T172431.png
security:
- kind: authentication
  name: Arizona State University Authentication
  slug: arizona-state-university-authentication
  summary_line: saml2/cas/oauth2/none · 4 schemes
- kind: domain-security
  name: Arizona State University Domain Security
  slug: arizona-state-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arizona State University Vulnerability Disclosure
  slug: arizona-state-university-vulnerability-disclosure
  summary_line: disclosure policy published
slug: arizona-state-university
tags:
- University
- Higher Education
- Education
- United States
- Arizona
- Public Research University
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
- Course Catalog
- Library
website: https://www.asu.edu/
---
