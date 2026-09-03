---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 11
apis:
- description: Queen Mary's open-access institutional repository runs DSpace 8.4 and exposes the standard DSpace REST API on the university's own host. The HAL service document at /server/api answers unauthenticated
  name: Queen Mary Research Online (QMRO) — DSpace 8.4 REST API
  slug: qmro-dspace-rest
- description: 'QMplus, Queen Mary''s Moodle virtual learning environment, runs as an LTI 1.3 / LTI Advantage tool platform and publishes the four endpoints the standard requires an external learning tool to find: a J'
  name: QMplus LTI 1.3 Advantage Tool Platform
  slug: qmplus-lti-platform
- description: The standard Moodle web-services REST entry point on QMplus. It answers an unauthenticated request with a structured moodle_exception carrying ERRORCODE invalidtoken, which proves the endpoint is enab
  name: QMplus Moodle Web Services (REST)
  slug: qmplus-moodle-webservices
- description: Queen Mary's own Shibboleth Identity Provider, entityID https://idp.shibboleth.qmul.ac.uk/idp/shibboleth, asserting shibmd:Scope "qmul.ac.uk". Its entity descriptor is published as signed, machine-rea
  name: Shibboleth SAML Identity Provider (UK Access Management Federation)
  slug: shibboleth-saml-idp
- description: Queen Mary's Microsoft Entra ID tenant, GUID 569df091-b013-40e3-86ee-bd9cb9e25814, EU region scope. The OpenID Connect discovery document resolves from the qmul.ac.uk domain hint, which is what ties t
  name: Microsoft Entra ID Tenant — OpenID Connect Discovery
  slug: entra-id-tenant
- description: Apocrita is Queen Mary's own high-performance computing cluster, run by ITS Research, and its documentation site is genuinely institution-hosted — docs.hpc.qmul.ac.uk resolves to doc-01.hpc.qmul.ac.uk
  name: Apocrita — Queen Mary Research Computing Service
  slug: apocrita-hpc
- description: Queen Mary's library discovery layer is Ex Libris Primo VE over Alma, fronted by the vanity host librarysearch.qmul.ac.uk, which CNAMEs to qmul.primo.exlibrisgroup.com and on to eu06.primo.exlibrisgro
  name: Library Search — Ex Libris Primo VE / Alma discovery tenancy
  slug: primo-ve-discovery
- description: 'Every page on qmul.ac.uk, including the undergraduate course finder, queries a hosted Apache Solr index on SearchStax under Queen Mary''s own account 29847 and index qmu-1736. The endpoint returns 401 '
  name: Queen Mary site and course search — SearchStax Solr tenancy
  slug: searchstax-site-search
- description: Queen Mary is a DataCite member organisation, provider id "iuar", memberType consortium_organization, linked to ROR https://ror.org/026zzn846, with one registered repository client "bl.qmul" created 2
  name: DataCite member organisation and repository client
  slug: datacite-membership
- description: 'Queen Mary is a Crossref member, id 11031, holding DOI prefix 10.26494. Recorded as a registry membership on the same basis as the DataCite entry: it is a fact about the institution, not a contract th'
  name: Crossref member and DOI prefix
  slug: crossref-membership
- description: 'Queen Mary''s Research Organization Registry identifier, https://ror.org/026zzn846. It is the join key that connects the institution''s DataCite membership, its ORCID affiliation records and its funder '
  name: ROR organisation identifier
  slug: ror-identifier
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.qmul.ac.uk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QMUL
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/queen-mary-university-of-london
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qmul.ac.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.qmul.ac.uk/its/support/
- group: company
  title: ''
  type: Blog
  url: https://www.qmul.ac.uk/news/
- group: other
  title: ''
  type: ResearchRepository
  url: https://qmro.qmul.ac.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://librarysearch.qmul.ac.uk/nde/home?vid=44QMUL_INST:44QMUL
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.qmul.ac.uk/undergraduate/coursefinder/
- group: other
  title: ''
  type: OpenData
  url: https://www.qmul.ac.uk/about/foi/datasets/
- group: other
  title: ''
  type: IdentityFederation
  url: http://mdq.ukfederation.org.uk/entities/https%3A%2F%2Fidp.shibboleth.qmul.ac.uk%2Fidp%2Fshibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://docs.hpc.qmul.ac.uk/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.qmul.ac.uk/digital-education-studio/news-events/de26/february/queen-mary-ai-policy/
- group: build
  title: ''
  type: AITooling
  url: https://www.qmul.ac.uk/library/academic-skills/student-guide-to-generative-ai/
- group: other
  title: ''
  type: x-research-publications
  url: https://researchpublications.its.qmul.ac.uk/publications/
- group: other
  title: ''
  type: x-open-research
  url: https://www.qmul.ac.uk/library/open-research/
- group: learn
  title: ''
  type: x-learning-platform
  url: https://qmplus.qmul.ac.uk/
- group: design
  title: ''
  type: Conformance
  url: conformance/queen-mary-university-of-london-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/queen-mary-university-of-london-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/queen-mary-university-of-london-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/queen-mary-university-of-london-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/queen-mary-university-of-london-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/queen-mary-university-of-london-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: company
  title: ''
  type: x-blogs
  url: blogs/blogs.json
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/queen-mary-university-of-london-context.jsonld
created: '2026-06-03'
description: 'Queen Mary University of London (QMUL) is a public research university in London and a member of the Russell Group. It runs no developer portal, publishes no OpenAPI, and offers no self-service API credentials — but the claim that it therefore has no programmable surface is wrong, and this profile replaces it. Four surfaces are institution-operated and were verified live: Queen Mary Research Online (QMRO) runs DSpace 8.4 and answers an unauthenticated HAL service document at qmro.qmul.ac.uk/server/api advertising 79 endpoint families; QMplus, the university''s Moodle learning platform, is an LTI 1.3 Advantage tool platform publishing its own RSA key set, OIDC auth, token and services endpoints; the QMplus Moodle web-services REST entry point is live and token-gated; and Apocrita, the university''s own HPC service, publishes machine-readable documentation at docs.hpc.qmul.ac.uk on Queen Mary''s own address space. Two more are federated identity the institution genuinely owns:
  a Shibboleth Identity Provider registered in the Jisc UK Access Management Federation with the scope qmul.ac.uk, and a Microsoft Entra ID tenant whose OpenID Connect discovery document resolves from the qmul.ac.uk domain. Two are tenant relationships on suppliers'' platforms and are recorded as relationships, not as Queen Mary''s engineering: the Ex Libris Primo VE / Alma library discovery deployment behind librarysearch.qmul.ac.uk, whose public configuration API and SRU endpoint both answer, and the SearchStax Solr index that powers site and course search. Three are registry memberships — a DataCite provider record, a Crossref member id with its own DOI prefix, and a ROR identifier. Student-facing systems (MySIS, timetables, MyQMUL) are authentication-gated, no open-data portal exists, and the institution''s public dataset publishing amounts to CSV files under the Freedom of Information publication scheme.'
examples:
- key_count: 6
  name: Queen Mary University Of London Qmro Dspace Api Root
  slug: queen-mary-university-of-london-qmro-dspace-api-root
finops:
- name: Queen Mary University Of London Finops
  service_category: Education
  slug: queen-mary-university-of-london-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/queen-mary-university-of-london.png
jsonld:
- class_count: 13
  name: Queen Mary University Of London Context
  property_count: 6
  slug: queen-mary-university-of-london-context
layout: provider
modified: '2026-09-01'
name: Queen Mary University of London
nav: Providers
network: true
overview: 'Queen Mary University of London publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and United Kingdom.


  The Queen Mary University of London catalog on APIs.io includes 1 JSON-LD context.


  Queen Mary University of London''s developer surface includes support, engineering blog, authentication, and 23 more developer resources.'
plans:
- name: Queen Mary University Of London Plans Pricing
  plan_count: 2
  slug: queen-mary-university-of-london-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Queen Mary University Of London Rate Limits
  slug: queen-mary-university-of-london-rate-limits
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: authentication
  name: Queen Mary University Of London Authentication
  slug: queen-mary-university-of-london-authentication
  summary_line: saml2/openid_connect/jwt_bearer/none · 5 schemes
- kind: domain-security
  name: Queen Mary University Of London Domain Security
  slug: queen-mary-university-of-london-domain-security
  summary_line: TLSv1.3 · DMARC
slug: queen-mary-university-of-london
tags:
- University
- Higher Education
- Education
- Research
- United Kingdom
- London
- Russell Group
- Open Access
- Research Repository
- Identity Federation
- Library
- Learning Management
- LTI
- Research Computing
website: https://www.qmul.ac.uk/
---
