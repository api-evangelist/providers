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
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.0
  scored_at: '2026-11-06'
api_count: 1
apis:
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
- baseURL: https://www.fdr.uni-hamburg.de/api
  baseurl_source: declared
  description: Curated collections within the repository.
  name: Universität Hamburg Communities API
  slug: universitat-hamburg-communities-api
- baseURL: https://www.fdr.uni-hamburg.de/api
  baseurl_source: declared
  description: File buckets attached to a record.
  name: Universität Hamburg Files API
  slug: universitat-hamburg-files-api
- baseURL: https://www.fdr.uni-hamburg.de/api
  baseurl_source: declared
  description: Controlled license vocabulary used by records.
  name: Universität Hamburg Licenses API
  slug: universitat-hamburg-licenses-api
- baseURL: https://www.fdr.uni-hamburg.de/api
  baseurl_source: declared
  description: Published research-data records and their metadata.
  name: Universität Hamburg Records API
  slug: universitat-hamburg-records-api
artifact_total: 24
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
  href: https://artifacts.apis.io/universitat-hamburg/conformance/universitat-hamburg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/universitat-hamburg-conformance.yml
- group: auth
  href: https://artifacts.apis.io/universitat-hamburg/security/universitat-hamburg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/universitat-hamburg-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/universitat-hamburg/plans/universitat-hamburg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/universitat-hamburg-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/universitat-hamburg/rate-limits/universitat-hamburg-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/universitat-hamburg-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/universitat-hamburg/finops/universitat-hamburg-finops.yml
  title: ''
  type: FinOps
  url: finops/universitat-hamburg-finops.yml
- group: other
  href: https://artifacts.apis.io/universitat-hamburg/review.yml
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
- has_sources: true
  method: generated
  name: Universitat Hamburg Finops
  primary_unit: ''
  service_category: Education
  slug: universitat-hamburg-finops
  template: false
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
overview: 'Universität Hamburg publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Communities API, Files API, Licenses API, and 12 more. Tagged areas include Education, Higher Education, University, Germany, and Research Data.


  The Universität Hamburg catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Universität Hamburg''s developer surface includes engineering blog, support, authentication, and 19 more developer resources.'
plans:
- name: Universitat Hamburg Plans Pricing
  plan_count: 2
  slug: universitat-hamburg-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Universitat Hamburg Rate Limits
  slug: universitat-hamburg-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Universität Hamburg API Rules
  rule_count: 55
  severity_counts:
    error: 53
    hint: 0
    info: 1
    warn: 1
  slug: universitat-hamburg-rules
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.5
    catalog_earned_first_party: 0.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 23.7
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 27.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/universitat-hamburg/universitat-hamburg-2026-06-20T200115.png
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
