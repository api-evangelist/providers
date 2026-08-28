---
access_model:
  confidence: high
  label: No public API programme · institutional key on request
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication/university-of-amsterdam-authentication.yml
  - https://github.com/uva/UvA-HvA-Agentic-Tools
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-26'
api_count: 9
apis:
- description: The shared AI gateway the University of Amsterdam and the Amsterdam University of Applied Sciences run for their students, staff and developers. It fronts GPT, Claude and open-weight models behind one
  name: UvA/HvA AI Gateway
  slug: llm-gateway
- description: The university's own SAML 2.0 identity provider, entity ID http://login.uva.nl/adfs/services/trust. Signed federation metadata is served from the institution's own host and the entity is registered in
  name: UvA Identity Provider (SAML 2.0 / SURFconext)
  slug: identity-federation
- description: DataNose is the course, registration, timetable and thesis-administration system used by the University of Amsterdam's Faculty of Science. Its API host resolves into UVANET1, the university's own RIPE
  name: DataNose API
  slug: datanose
- description: The University of Amsterdam Library publishes its digitised collections — books, letters, maps, images, audio, video, sheet music, archaeological objects and the Beeldbank image repository — as linked
  name: UvA Library Linked Open Data (TriplyDB tenancy)
  slug: lod-triply
- description: 'UvA-DARE, the university''s digital academic repository, and the research information system behind it run on Elsevier Pure: pure.uva.nl CNAMEs to uva.elsevierpure.com. The OAI-PMH provider answers Ide'
  name: UvA-DARE OAI-PMH and Pure Web Service (Elsevier Pure tenancy)
  slug: oai-pure-dare
- description: OAI-PMH provider exposing EAD collection descriptions and inventories from the University of Amsterdam Library archives and the Allard Pierson heritage collections, under PDDL. The host is a UvA subdo
  name: UvA Archives Collection Descriptions OAI-PMH (ArchivesSpace tenancy)
  slug: oai-archives
- description: The harvesting endpoint the university library documents for its central catalogue — roughly 2.5 million bibliographic records in MARC-XML and unqualified Dublin Core. It runs on the library's Ex Libr
  name: UvA Central Catalogue OAI-PMH (Ex Libris Alma tenancy)
  slug: oai-catalogue
- description: The shared research data repository of the University of Amsterdam and the Amsterdam University of Applied Sciences, running on Figshare at uvaauas.figshare.com. DOIs are minted under the institution'
  name: UvA/HvA Research Data Repository (Figshare tenancy)
  slug: research-data-figshare
- description: The university timetable at rooster.uva.nl exposes a JSON API under /api/ that answers 401 with a structured error to unauthenticated callers, so the surface is real and gated behind institutional sig
  name: UvA Timetable API (MyTimetable tenancy)
  slug: timetable
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.uva.nl/en
- group: other
  title: ''
  type: OpenData
  url: https://uba.uva.nl/en/support/open-data/open-data.html
- group: other
  title: ''
  type: OpenData
  url: https://uba.uva.nl/en/support/open-data/data-sets-and-publication-channels/data-sets-and-publication-channels.html
- group: docs
  title: ''
  type: Documentation
  url: https://uba.uva.nl/en/support/open-data/licences/licences.html
- group: other
  title: ''
  type: ResearchRepository
  url: https://dare.uva.nl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://uvaauas.figshare.com/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://uba.uva.nl/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://studiegids.uva.nl/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://datanose.nl/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.uva.nl/federationmetadata/2007-06/federationmetadata.xml
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uva.nl/en/about-the-uva/about-the-university/ai/ai.html
- group: build
  title: ''
  type: AITooling
  url: https://github.com/uva/UvA-HvA-Agentic-Tools
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uva
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.uva.nl/.well-known/security.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uva.nl/en/home/disclaimers/about-this-site
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uva.nl/en/home/disclaimers/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://www.uva.nl/en/about-the-uva/contact-and-locations/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.uva.nl/en/news-events/news/uva-news.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-amsterdam/
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-amsterdam-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-amsterdam-conformance.yml
- group: design
  title: ''
  type: x-errors
  url: errors/university-of-amsterdam-errors.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/university-of-amsterdam-vocabulary.yml
- group: design
  title: ''
  type: x-json-ld-context
  url: json-ld/university-of-amsterdam-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-amsterdam-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-amsterdam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-amsterdam-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-amsterdam-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Amsterdam (Universiteit van Amsterdam, UvA) is a public research university in Amsterdam, Netherlands, a LERU member and one of the two large research universities in the city. It operates no central developer portal and issues no public API keys, and the honest shape of its programmable footprint is three institution-run surfaces surrounded by six vendor platforms it is a tenant of. What it genuinely runs itself: a shared AI gateway with the Amsterdam University of Applied Sciences at llmproxy.uva.nl that serves a full OpenAPI 3.1 description and issues keys to staff, students and developers on request; a SAML 2.0 identity provider whose signed federation metadata is published on its own host and registered in SURFconext and eduGAIN; and the DataNose course and registration API on its own network, whose Swagger UI answers but whose generated description currently returns 500. Everything else that looks like a UvA API is a contract someone else wrote: the
  library''s Linked Open Data platform is a TriplyDB tenancy, the research repository is Figshare, UvA-DARE and its OAI-PMH feed are Elsevier Pure, the archives OAI provider is LYRASIS-hosted ArchivesSpace, the central catalogue OAI endpoint is Ex Libris Alma and now returns 403 to the public, and the timetable API is Eveoh MyTimetable behind SSO. The data in those systems is the university''s; the interfaces are not.'
examples:
- key_count: 20
  name: University Of Amsterdam Get Dataset Example
  slug: university-of-amsterdam-get-dataset-example
- key_count: 2
  name: University Of Amsterdam Sparql Query Example
  slug: university-of-amsterdam-sparql-query-example
finops:
- name: University Of Amsterdam Finops
  service_category: Education
  slug: university-of-amsterdam-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-amsterdam.png
jsonld:
- class_count: 15
  name: University Of Amsterdam Context
  property_count: 14
  slug: university-of-amsterdam-context
layout: provider
modified: '2026-08-19'
name: University of Amsterdam
nav: Providers
network: true
overview: 'University of Amsterdam publishes 1 API on the [APIs.io](https://apis.io/) network: UvA/HvA AI Gateway. Tagged areas include University, Higher Education, Education, Public Research University, and Netherlands.


  The University of Amsterdam catalog on APIs.io includes 1 JSON-LD context.


  University of Amsterdam''s developer surface includes documentation, support, engineering blog, authentication, and 25 more developer resources.'
plans:
- name: University Of Amsterdam Plans Pricing
  plan_count: 2
  slug: university-of-amsterdam-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: University Of Amsterdam Rate Limits
  slug: university-of-amsterdam-rate-limits
score:
  band: developing
  composite: 46.0
  delta: 1.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 35.7
    discoverability: 85.2
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 44.6
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
    score: 46.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-amsterdam/refs/heads/main/screenshots/university-of-amsterdam-2026-08-17T083414.png
security:
- kind: authentication
  name: University Of Amsterdam Authentication
  slug: university-of-amsterdam-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: University Of Amsterdam Domain Security
  slug: university-of-amsterdam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: university-of-amsterdam
tags:
- University
- Higher Education
- Education
- Public Research University
- Netherlands
- Europe
- LERU
- Open Data
- Linked Data
- Library
- Research Data
- Research Repository
- Course Catalog
- Identity Federation
- OAI-PMH
- Artificial Intelligence
website: https://www.uva.nl/en
---
