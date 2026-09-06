---
access_model:
  confidence: high
  label: Free and open, no registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://www.fdr.uni-hamburg.de/api/records/?size=1
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://www.fdr.uni-hamburg.de/api
  baseurl_source: declared
  description: Read API of the ZFDM Repository (Forschungsdatenrepositorium), operated by Universität Hamburg's Zentrum für nachhaltiges Forschungsdatenmanagement on the institution's own host. Returns records, comm
  name: ZFDM Research Data Repository API
  slug: zfdm-repository-api
- description: 'OAI-PMH 2.0 harvesting interface of the ZFDM Research Data Repository. Verified live 2026-09-01: repositoryName "ZFDM Repository", adminEmail repository.fdm@uni-hamburg.de, earliest datestamp 2019-04-'
  name: ZFDM Repository OAI-PMH
  slug: zfdm-oai
- description: OAI-PMH 2.0 metadata-harvesting interface for the DSpace-based institutional repository of electronic dissertations and habilitations of Universität Hamburg, operated by the Staats- und Universitätsbi
  name: E-Dissertationen (ediss.sub.hamburg) OAI-PMH
  slug: ediss-oai
- description: OAI-PMH 2.0 interface of Hamburg University Press, the open-access publishing house of the Staats- und Universitätsbibliothek Hamburg, running on OJS. Verified live 2026-09-01 with 15 sets and the oai
  name: Hamburg University Press OAI-PMH
  slug: hup-oai
- description: 'OAI-PMH 2.0 interface of the journal server of Hamburg University Press. Verified live 2026-09-01: repositoryName "Journal Server of Hamburg University Press - Publishing House of the State and Univer'
  name: HUP Journal Server OAI-PMH
  slug: journals-oai
- description: OAI-PMH 2.0 interface over the digitized collections of the Staats- und Universitätsbibliothek Hamburg, running Kitodo.Presentation. Verified live 2026-09-01 serving real PPN identifiers with the oai_
  name: Digitized Collections (Kitodo.Presentation) OAI-PMH
  slug: digitalisate-oai
- description: The institution's own SAML 2.0 Identity Provider metadata, served from its own host. entityID https://login.uni-hamburg.de/idp/shibboleth, mdui:DisplayName "Universität Hamburg (UHH)", three SingleSig
  name: Universität Hamburg Shibboleth SAML 2.0 Identity Provider Metadata
  slug: saml-idp
- description: Universität Hamburg's IdP is registered in DFN-AAI, the German national identity federation and eduGAIN member, and its metadata is resolvable through the DFN-AAI MDQ service. registrationAuthority ht
  name: DFN-AAI / eduGAIN Federation Membership
  slug: dfn-aai
- description: Universität Hamburg is a DataCite registrant. DOI prefix 10.25592 resolves to DataCite client tib.fdmuh, named "Universität Hamburg", registered 2017 and used by the ZFDM Repository. The university li
  name: DataCite Registrant (prefix 10.25592)
  slug: datacite-registrant
- description: 'The Staats- und Universitätsbibliothek Hamburg Carl von Ossietzky — the university library and publisher of Hamburg University Press — is Crossref member 25426, depositing under prefix 10.15460, with '
  name: Crossref Member 25426 (prefix 10.15460)
  slug: crossref-member
- description: Universität Hamburg is registered in the Research Organization Registry as https://ror.org/00g30e956. Membership recorded; the ROR API is ROR's.
  name: ROR Registration (00g30e956)
  slug: ror
- description: Open Access discovery portal aggregating freely available publications, research data, teaching materials and scientific collections of Universität Hamburg. Human-facing only — no documented REST API.
  name: Open-Access-Portal Universität Hamburg
  slug: open-access-portal
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.uni-hamburg.de/en.html
- group: company
  title: ''
  type: Blog
  url: https://www.uni-hamburg.de/en/newsroom.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uni-hamburg.de/en/impressum.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uni-hamburg.de/en/datenschutz.html
- group: operate
  title: ''
  type: Support
  url: https://www.uni-hamburg.de/en/uhh/kontakt.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Uni-Hamburg
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/subhh
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.rrz.uni-hamburg.de/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universitaet-hamburg/
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.fdr.uni-hamburg.de/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://kataloge.uni-hamburg.de/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.stine.uni-hamburg.de/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.uni-hamburg.de/idp/shibboleth
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.rrz.uni-hamburg.de/en/services/hpc.html
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uni-hamburg.de/lehre-navi/lehrende/orientierungsrahmen-gki
- group: auth
  title: ''
  type: Authentication
  url: https://www.rrz.uni-hamburg.de/services/weitere/authentifizierung/shibboleth/configure.html
- group: design
  title: ''
  type: Conformance
  url: conformance/universitat-hamburg-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/universitat-hamburg-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/universitat-hamburg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/universitat-hamburg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/universitat-hamburg-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universität Hamburg is a public research university in Hamburg, Germany, and one of the largest in the country. It operates no central developer portal, publishes no OpenAPI of its own, and has no course, registrar, campus-life or open-data API — the STiNE campus-management system and the Katalogplus discovery service are both behind an authorization wall. What it does operate, on its own hosts and with its own engineering, is scholarly-communication and identity infrastructure: a research-data repository (ZFDM, www.fdr.uni-hamburg.de) whose read API returns unauthenticated JSON with CORS and rate-limit headers; five live OAI-PMH 2.0 repositories across dissertations, research data, the university press, its journal server and its digitized collections; and its own Shibboleth SAML 2.0 Identity Provider, whose metadata is published at login.uni-hamburg.de and registered in the DFN-AAI federation and thereby in eduGAIN. It is a DataCite registrant (prefix 10.25592) and its library
  is a Crossref member (prefix 10.15460). Almost all of this is library-and-computing-centre infrastructure rather than a product; none of it is documented for third-party developers.'
examples:
- key_count: 11
  name: Universitat Hamburg Zfdm Community Uhh Example
  slug: universitat-hamburg-zfdm-community-uhh-example
- key_count: 3
  name: Universitat Hamburg Zfdm Licenses Example
  slug: universitat-hamburg-zfdm-licenses-example
finops:
- name: Universitat Hamburg Finops
  service_category: Education
  slug: universitat-hamburg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universitat-hamburg.png
jsonld:
- class_count: 8
  name: Universitat Hamburg Context
  property_count: 2
  slug: universitat-hamburg-context
layout: provider
modified: '2026-09-01'
name: Universität Hamburg
nav: Providers
network: true
overview: 'Universität Hamburg publishes 1 API on the [APIs.io](https://apis.io/) network: ZFDM Research Data Repository API. Tagged areas include Education, Higher Education, University, Germany, and Research Data.


  The Universität Hamburg catalog on APIs.io includes 1 JSON-LD context.


  Universität Hamburg''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: Universitat Hamburg Plans Pricing
  plan_count: 2
  slug: universitat-hamburg-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Universitat Hamburg Rate Limits
  slug: universitat-hamburg-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 23.5
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 35.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/universitat-hamburg/refs/heads/main/screenshots/universitat-hamburg-2026-06-20T200115.png
security:
- kind: authentication
  name: Universitat Hamburg Authentication
  slug: universitat-hamburg-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Universitat Hamburg Domain Security
  slug: universitat-hamburg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: universitat-hamburg
tags:
- Education
- Higher Education
- University
- Germany
- Research Data
- Research Repository
- Library
- Open Access
- Metadata
- OAI-PMH
- Identity Federation
- DataCite
website: https://www.uni-hamburg.de/en.html
---
