---
access_model:
  confidence: high
  label: Free and keyless where public; institutional affiliation where not
  onboarding: unknown
  pricing: free
  public: true
  source:
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
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: 'Keyless OAI-PMH 2.0 metadata harvesting endpoint operated by Maastricht University on its own domain. Verified live 2026-08-30: all six verbs return 200, six metadata profiles are offered (oai_dc, qdc'
  name: Maastricht University Research Portal OAI-PMH
  slug: oai-pmh
- description: 'Maastricht University runs its own identity provider on login.maastrichtuniversity.nl and publishes two machine-readable discovery documents without authentication: an OpenID Connect configuration (is'
  name: Maastricht University Identity Provider (ADFS / SURFconext / eduGAIN)
  slug: identity-federation
- description: Self-hosted GitLab instance on the university's own domain, serving UM research and teaching projects. Its REST API v4 answers unauthenticated public-project queries — GET /api/v4/projects returned 20
  name: Maastricht University GitLab
  slug: gitlab
- description: The Institute of Data Science maintains an active public GitHub organization (220 public repositories) with institution-authored open-source data-science tooling — RDF knowledge-graph builders, rdflib
  name: Maastricht University Institute of Data Science (Open Source)
  slug: ids-github
- description: DataHub is Maastricht University's own research data management service, built and maintained by UM Research IT on an iRODS foundation. Its GitHub organization holds 38 institution-authored repositori
  name: DataHub Maastricht (Research IT) Open Source
  slug: datahub-github
- description: The University Library publishes 46 public repositories of research-data-management support material, open training content and open-source software, including DataverseNL analysis tooling and an Omek
  name: Maastricht University Library Open Source
  slug: library-github
- description: Maastricht University's published research data lives in a collection (alias "maastricht") inside DataverseNL, the shared national Dataverse installation. There is no maastricht.dataverse.nl — the rel
  name: Maastricht University research data collection on DataverseNL
  slug: dataversenl
- description: The Elsevier Pure web service on the university's CRIS host. Its documentation page canonicalises to https://api.elsevierpure.com/ws/api/documentation/index.html and /ws/api/524/openapi.yaml returns 4
  name: Maastricht University Research Portal (Pure) REST API
  slug: pure-ws-api
- description: Instructure Canvas tenant on the university's own hostname. GET /api/v1/accounts returned 401 on 2026-08-30, confirming a live Canvas REST API gated behind institutional credentials. Canvas implies LT
  name: Maastricht University Canvas LMS
  slug: canvas
- description: 'Library discovery runs on OCLC''s hosted WorldCat Discovery under an institution-specific subdomain. A textbook tenant: Maastricht''s holdings, OCLC''s platform and OCLC''s API contract. No institution-op'
  name: Maastricht University Library discovery (OCLC WorldCat)
  slug: worldcat-discovery
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.maastrichtuniversity.nl/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MaastrichtUniversity
- group: build
  title: ''
  type: GitHub
  url: https://github.com/MaastrichtU-IDS
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.maastrichtuniversity.nl/explore/projects
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/maastricht-university/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.maastrichtuniversity.nl/FederationMetadata/2007-06/FederationMetadata.xml
- group: auth
  title: ''
  type: Authentication
  url: https://login.maastrichtuniversity.nl/adfs/.well-known/openid-configuration
- group: other
  title: ''
  type: ResearchRepository
  url: https://dataverse.nl/dataverse/maastricht
- group: build
  title: ''
  type: LibraryCatalog
  url: https://maastrichtuniversity.on.worldcat.org/discovery
- group: other
  title: ''
  type: ResearchComputing
  url: https://dsri.maastrichtuniversity.nl/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.maastrichtuniversity.nl/news/policy-framework-generative-ai-officially-published
- group: build
  title: ''
  type: AITooling
  url: https://www.maastrichtuniversity.nl/education/edlab/ai-education-maastricht-university
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.maastrichtuniversity.nl/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.maastrichtuniversity.nl/disclaimer
- group: operate
  title: ''
  type: Support
  url: https://www.maastrichtuniversity.nl/contact
- group: company
  title: ''
  type: Blog
  url: https://www.maastrichtuniversity.nl/news
- group: other
  title: ''
  type: Research
  url: https://www.maastrichtuniversity.nl/research
- group: design
  title: ''
  type: Conformance
  url: conformance/maastricht-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maastricht-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/maastricht-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/maastricht-errors.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/maastricht-vocabulary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/maastricht-lifecycle.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/maastricht-capability-edges.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maastricht-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maastricht-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/maastricht-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/maastricht-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/maastricht-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Maastricht University (UM) is a public research university in Maastricht, Netherlands, founded in 1976 and known internationally for its Problem-Based Learning model. Measured honestly, UM operates no API programme: there is no developer portal, no api.maastrichtuniversity.nl, no status page, no published versioning or deprecation policy, and no first-party OpenAPI anywhere on its estate. What it does operate is a small set of standards-based surfaces on its own domain — a live, keyless OAI-PMH 2.0 harvesting endpoint at cris.maastrichtuniversity.nl serving 798,420 records across six metadata profiles including OpenAIRE CERIF 1.2 with resolvable ORCID iDs; a self-hosted GitLab whose REST API answers unauthenticated project queries; and its own ADFS identity provider publishing both OpenID Connect discovery and signed SAML 2.0 federation metadata, with its entity carried in SURFconext and thereby eduGAIN. Everything else that looks like a Maastricht API is a purchase: research
  data lives in a collection inside the shared national DataverseNL installation, the CRIS is Elsevier Pure, the LMS is Instructure Canvas, and library discovery is OCLC WorldCat. Those are recorded here as tenant relationships, not as Maastricht''s engineering.'
examples:
- key_count: 26
  name: Maastricht Adfs Openid Configuration Example
  slug: maastricht-adfs-openid-configuration-example
finops:
- name: Maastricht Finops
  service_category: Education
  slug: maastricht-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maastricht.png
layout: provider
modified: '2026-08-30'
name: Maastricht University
nav: Providers
network: true
overview: 'Maastricht University publishes 1 API on the [APIs.io](https://apis.io/) network: Research Portal OAI-PMH. Tagged areas include University, Higher Education, Education, Netherlands, and Europe.


  Maastricht University''s developer surface includes GitHub presence, authentication, support, engineering blog, and 26 more developer resources.'
plans:
- name: Maastricht Plans Pricing
  plan_count: 2
  slug: maastricht-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Maastricht Rate Limits
  slug: maastricht-rate-limits
scopes:
- name: Maastricht Scopes
  scope_count: 10
  slug: maastricht-scopes
  summary_line: 10 scopes
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 15
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 51.0
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 15.2
    operational_transparency: 23.7
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 75.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maastricht/refs/heads/main/screenshots/maastricht-2026-06-20T184821.png
security:
- kind: authentication
  name: Maastricht Authentication
  slug: maastricht-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Maastricht Domain Security
  slug: maastricht-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Maastricht Vulnerability Disclosure
  slug: maastricht-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: maastricht
tags:
- University
- Higher Education
- Education
- Netherlands
- Europe
- Research Data
- Research Repository
- Identity Federation
- OAI-PMH
- Open Access
- Public Research University
website: https://www.maastrichtuniversity.nl/
---
