---
access_model:
  confidence: high
  label: Free · unauthenticated public read, no registration offered
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Humboldt Universitat Zu Berlin Agentic Access
  operation_count: 8
  slug: humboldt-universitat-zu-berlin-agentic-access
  summary_line: 8 operations
api_count: 3
apis:
- description: Public, unauthenticated read API of the edoc-Server, the Open Access institutional repository of Humboldt-Universität zu Berlin, operated by the University Library's Arbeitsgruppe Elektronisches Publi
  name: edoc-Server DSpace REST API
  slug: edoc-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for the edoc institutional repository, on HU's own host. ?verb=Identify returned 200 on 2026-09-01 with repositoryName "edoc-Server", repositoryIdentifier edoc
  name: edoc-Server OAI-PMH 2.0 Interface
  slug: edoc-oai
- description: Documented, versioned, public read API of the LAUDATIO-Repository (Long-term Access and Usage of Deeply Annotated Information), the open-access research-data repository for historical linguistic corpo
  name: LAUDATIO-Repository REST API
  slug: laudatio-repository-api
- description: Humboldt-Universität zu Berlin operates its own Shibboleth/SAML identity provider, entityID https://shib-idp.cms.hu-berlin.de/idp/shibboleth, registered by DFN-AAI (registrationAuthority https://www.a
  name: HU-IAM Shibboleth Identity Provider (SAML 2.0)
  slug: shibboleth-idp
- description: 'Humboldt-Universität zu Berlin is a DataCite member — provider symbol VLEF, memberType consortium_organization, country DE, ROR https://ror.org/01hcx6992, created 2020-12-11 — with its own DOI prefix '
  name: DataCite Membership (VLEF)
  slug: datacite-membership
- description: HU's Computer- und Medienservice operates its own GitLab instance at scm.cms.hu-berlin.de, hosting institutional projects including the LAUDATIO repository source. GitLab exposes a REST API at /api/v4
  name: HU Berlin GitLab (scm.cms.hu-berlin.de)
  slug: hu-gitlab
- description: Primus, the University Library's central search portal, is an Ex Libris Primo deployment backed by Alma, served from hu-berlin.primo.exlibrisgroup.com under view 49KOBV_HUB:HUB_UB within the KOBV netw
  name: University Library Primus Discovery (Ex Libris Primo/Alma tenancy)
  slug: primo-discovery
- description: The NOMAD Repository for computational materials-science data is registered under HU Berlin's DataCite membership as repository tib.hu ("HU Berlin - NOMAD Repository"), and the NOMAD Laboratory / FAIR
  name: NOMAD Repository (FAIRmat) — HU DOI tenancy
  slug: nomad-repository
- description: GenderOpen is the shared open-access repository for gender studies run jointly by the Freie Universität Berlin, Humboldt-Universität zu Berlin and Technische Universität Berlin. It is a DSpace deploym
  name: GenderOpen Repositorium — HU DOI tenancy
  slug: genderopen
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: edoc-Server DSpace REST API (Humboldt-Universität zu Berlin) Core API
  slug: open-humboldt-universitat-zu-berlin-core-api
- collection_type: open
  name: edoc-Server DSpace REST API (Humboldt-Universität zu Berlin) Core Discovery API
  slug: open-humboldt-universitat-zu-berlin-discovery-api
- collection_type: open
  name: edoc-Server DSpace REST API (Humboldt-Universität zu Berlin) Core Root API
  slug: open-humboldt-universitat-zu-berlin-root-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.hu-berlin.de/en
- group: other
  title: ''
  type: ResearchRepository
  url: https://edoc.hu-berlin.de/
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.laudatio-repository.org/
- group: other
  title: ''
  type: ResearchRepository
  url: https://media.hu-berlin.de/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://hu-berlin.primo.exlibrisgroup.com/discovery/search?vid=49KOBV_HUB:HUB_UB
- group: learn
  title: ''
  type: CourseCatalog
  url: https://agnes.hu-berlin.de/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.cms.hu-berlin.de/de/dl/hu-iam/shibboleth
- group: build
  title: ''
  type: AITooling
  url: https://ai-skills.hu-berlin.de/
- group: docs
  title: ''
  type: APIReference
  url: https://www.laudatio-repository.org/docs/elasticapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UB-HU-Berlin
- group: other
  title: ''
  type: VCS
  url: https://scm.cms.hu-berlin.de/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/humboldt-universitat-zu-berlin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hu-berlin.de/de/hu/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hu-berlin.de/de/hu/impressum/datenschutzerklaerung
- group: auth
  title: ''
  type: Authentication
  url: https://www.cms.hu-berlin.de/de/dl/hu-iam/shibboleth
- group: design
  title: ''
  type: Conformance
  url: conformance/humboldt-universitat-zu-berlin-conformance.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/humboldt-universitat-zu-berlin-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/humboldt-universitat-zu-berlin-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/humboldt-universitat-zu-berlin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/humboldt-universitat-zu-berlin-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/humboldt-universitat-zu-berlin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/humboldt-universitat-zu-berlin-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/humboldt-universitat-zu-berlin-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Humboldt-Universität zu Berlin (HU Berlin) is a public research university in Berlin, Germany, founded in 1810 and ranked #126 in the QS World University Rankings 2025. Like almost every university, HU is a federation of buyers rather than an API producer: it publishes no developer portal, no API terms, no SDKs and not one OpenAPI of its own, and every OpenAPI in this repository was authored by API Evangelist from live probes and says so in its own info.description. What HU does genuinely operate is scholarly and identity infrastructure on its own hosts. The edoc-Server institutional repository at edoc.hu-berlin.de (DSpace 8, self-hosted by the University Library) exposes an unauthenticated read REST API and a full OAI-PMH 2.0 interface advertising eighteen metadata formats including oai_datacite. The LAUDATIO-Repository for historical linguistic corpora, run by the Corpus Linguistics department with the Computer- und Medienservice, publishes a documented, versioned, public
  REST API over its Elasticsearch index. HU operates its own Shibboleth/SAML identity provider, registered in DFN-AAI and published to eduGAIN, and is a DataCite member (VLEF) minting 32,950 DOIs under its own prefix 10.18452 across ten registered repositories. Its library discovery is an Ex Libris Primo/Alma tenancy and is not HU engineering. Note for machine consumers: hu-berlin.de web hosts, including the GitLab instance at scm.cms.hu-berlin.de, sit behind an Anubis proof-of-work bot wall that returns HTTP 200 with a JavaScript challenge instead of content — the data hosts (edoc, LAUDATIO) do not.'
examples:
- key_count: 8
  name: Humboldt Universitat Zu Berlin Get Collection Example
  slug: humboldt-universitat-zu-berlin-get-collection-example
- key_count: 2
  name: Humboldt Universitat Zu Berlin List Communities Example
  slug: humboldt-universitat-zu-berlin-list-communities-example
- key_count: 1
  name: Humboldt Universitat Zu Berlin Search Objects Example
  slug: humboldt-universitat-zu-berlin-search-objects-example
finops:
- name: Humboldt Universitat Zu Berlin Finops
  service_category: Education
  slug: humboldt-universitat-zu-berlin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/humboldt-universitat-zu-berlin.png
json_schemas:
- name: DSpace Collection
  property_count: 8
  slug: humboldt-universitat-zu-berlin-collection
- name: DSpace Community
  property_count: 8
  slug: humboldt-universitat-zu-berlin-community
- name: DSpace Item
  property_count: 12
  slug: humboldt-universitat-zu-berlin-item
json_structures:
- name: Humboldt Universitat Zu Berlin Community Structure
  property_count: 7
  slug: humboldt-universitat-zu-berlin-community-structure
- name: Humboldt Universitat Zu Berlin Item Structure
  property_count: 11
  slug: humboldt-universitat-zu-berlin-item-structure
jsonld:
- class_count: 15
  name: Humboldt Universitat Zu Berlin Context
  property_count: 8
  slug: humboldt-universitat-zu-berlin-context
layout: provider
modified: '2026-09-01'
name: Humboldt-Universität zu Berlin
nav: Providers
network: true
overview: 'Humboldt-Universität zu Berlin publishes 3 APIs on the [APIs.io](https://apis.io/) network: edoc-Server DSpace REST API, edoc-Server OAI-PMH 2.0 Interface, and LAUDATIO-Repository REST API. Tagged areas include University, Higher Education, Education, Research, and Germany.


  The Humboldt-Universität zu Berlin catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Humboldt-Universität zu Berlin''s developer surface includes API reference, authentication, and 22 more developer resources.'
plans:
- name: Humboldt Universitat Zu Berlin Plans Pricing
  plan_count: 2
  slug: humboldt-universitat-zu-berlin-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Humboldt Universitat Zu Berlin Rate Limits
  slug: humboldt-universitat-zu-berlin-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Humboldt-Universität zu Berlin API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: humboldt-universitat-zu-berlin-jsonschema-spectral-rules
- effective_rule_count: 7
  extends: []
  name: Humboldt-Universität zu Berlin API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 3
  slug: humboldt-universitat-zu-berlin-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 49.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.0
    contract_quality: 19.2
    developer_ergonomics: 7.1
    discoverability: 64.8
    governance: 28.0
    operational_transparency: 26.3
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 72.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/humboldt-universitat-zu-berlin/refs/heads/main/screenshots/humboldt-universitat-zu-berlin-2026-06-20T182937.png
security:
- kind: domain-security
  name: Humboldt Universitat Zu Berlin Domain Security
  slug: humboldt-universitat-zu-berlin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Humboldt Universitat Zu Berlin Vulnerability Disclosure
  slug: humboldt-universitat-zu-berlin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: humboldt-universitat-zu-berlin
tags:
- University
- Higher Education
- Education
- Research
- Germany
- Berlin
- Institutional Repository
- Research Data
- Open Access
- Library
- Identity Federation
- OAI-PMH
- DataCite
- Shibboleth
- Corpus Linguistics
website: https://www.hu-berlin.de/en
---
