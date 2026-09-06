---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
  scored_at: '2026-09-05'
api_count: 10
apis:
- description: 'REST API of TUdatalib, the institutional research-data repository of TU Darmstadt. Verified live 2026-09-01: the API root returns HAL/JSON with dspaceName "TUdatalib System", dspaceVersion "DSpace 9.3'
  name: TUdatalib DSpace REST API
  slug: tudatalib-rest
- description: 'OAI-PMH 2.0 metadata harvesting interface for TUdatalib. Verified live 2026-09-01: Identify returns repositoryName "TUdatalib System", protocolVersion 2.0, adminEmail tudatalib@ulb.tu-darmstadt.de. Th'
  name: TUdatalib OAI-PMH
  slug: tudatalib-oai
- description: 'The university''s own SAML 2.0 identity provider, operated by the Hochschulrechenzentrum (HRZ). Verified live 2026-09-01 (HTTP 200, 15,371 bytes of XML): entityID https://idp.hrz.tu-darmstadt.de/idp/sh'
  name: TU Darmstadt Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: shibboleth-idp
- description: 'TU Darmstadt''s identity provider is published in DFN-AAI, the German research-and-education identity federation run by DFN, and is reachable through eduGAIN by extension. Verified live 2026-09-01: the'
  name: DFN-AAI federation membership (eduGAIN)
  slug: dfn-aai
- description: A DBRepo deployment run by the Universitaets- und Landesbibliothek for publishing and querying research databases. Hosted on the institution's own infrastructure — dbrepo.ulb.tu-darmstadt.de is a CNAM
  name: DBRepo API (research database repository)
  slug: dbrepo
- description: TUjournals is TU Darmstadt's open-access journal platform, publisher of record "Universitaets- und Landesbibliothek Darmstadt". It runs a live, fully anonymous JSON REST API — verified 2026-09-01, /ap
  name: TUjournals REST API (Janeway tenancy)
  slug: tujournals-janeway
- description: 'TU Darmstadt registers DOIs through DataCite. Verified live 2026-09-01 via api.datacite.org/providers/hlqc: provider HLQC, "Universitaets- und Landesbibliothek Darmstadt", organizationType academicIns'
  name: DataCite membership (provider HLQC)
  slug: datacite-membership
- description: TU Darmstadt is registered in the Research Organization Registry as https://ror.org/05n911h24, established 1877, domain tu-darmstadt.de, with GRID grid.6546.1 and Crossref Funder IDs 501100005714 / 50
  name: ROR registration
  slug: ror
- description: tuprints is the open-access publication repository of TU Darmstadt, on the institution's own host and registered with DataCite as client hlqc.jslnah. It runs EPrints, whose OAI-PMH 2.0 base path is /c
  name: tuprints OAI-PMH (EPrints)
  slug: tuprints-oai
- description: TUbiblio is the publication bibliography of TU Darmstadt, on the institution's own host (tubiblio18.ulb.tu-darmstadt.de, 130.83.152.163), running EPrints with an OAI-PMH 2.0 base path of /cgi/oai2. St
  name: TUbiblio OAI-PMH (EPrints)
  slug: tubiblio-oai
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.tu-darmstadt.de/index.en.jsp
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TU-Darmstadt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tu-darmstadt/
- group: auth
  title: ''
  type: Authentication
  url: authentication/technical-university-of-darmstadt-authentication.yml
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.hrz.tu-darmstadt.de/idp/shibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://tudatalib.ulb.tu-darmstadt.de/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.hrz.tu-darmstadt.de/hlr/index.en.jsp
- group: other
  title: ''
  type: AIPolicy
  url: https://www.hda.tu-darmstadt.de/hochschuldidaktik/infoseiten_hd/handreichung_ki_hd/handreichung_ki_verteilerseite.de.jsp
- group: build
  title: ''
  type: AITooling
  url: https://www.e-learning.tu-darmstadt.de/online_lehre/ki_in_der_lehre/index.de.jsp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tu-darmstadt.de/impressum/index.en.jsp
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tu-darmstadt.de/datenschutzerklaerung
- group: operate
  title: ''
  type: Support
  url: https://www.tu-darmstadt.de/kontakt_1/index.en.jsp
- group: company
  title: ''
  type: Blog
  url: https://www.tu-darmstadt.de/universitaet/aktuelles_meldungen/index.en.jsp
- group: design
  title: ''
  type: Conformance
  url: conformance/technical-university-of-darmstadt-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/technical-university-of-darmstadt-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/technical-university-of-darmstadt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/technical-university-of-darmstadt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/technical-university-of-darmstadt-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/technical-university-of-darmstadt-context.jsonld
created: '2026-06-03'
description: 'The Technical University of Darmstadt (Technische Universitaet Darmstadt, TU Darmstadt) is a public technical research university in Darmstadt, Hesse, Germany, founded in 1877 and registered as ROR 05n911h24. It operates no central developer portal, publishes no OpenAPI description of its own, and its GitHub organization (TU-Darmstadt) is live but holds zero public repositories. What it does operate, and what makes this profile non-empty, is scholarly and identity infrastructure on its own domain: TUdatalib, the institutional research-data repository, runs DSpace 9.3 and exposes both a live HAL/JSON REST API and an OAI-PMH 2.0 interface; a DBRepo deployment at dbrepo.ulb.tu-darmstadt.de serves a live JSON API for research databases; and the Hochschulrechenzentrum (HRZ) runs the university''s own Shibboleth SAML 2.0 identity provider, whose metadata is publicly retrievable and published into the German DFN-AAI federation and eduGAIN. TUbiblio and tuprints run on EPrints with
  OAI-PMH endpoints that are WAF-protected. The ULB is a DataCite consortium member (provider HLQC) registering DOIs for six repositories. TUjournals is real, machine-readable and busy, but it is a tenancy on Janeway shared hosting, not TU Darmstadt engineering. Every surface below is labelled with who actually operates it.'
finops:
- name: Technical University Of Darmstadt Finops
  service_category: Education
  slug: technical-university-of-darmstadt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/technical-university-of-darmstadt.png
jsonld:
- class_count: 19
  name: Technical University Of Darmstadt Context
  property_count: 2
  slug: technical-university-of-darmstadt-context
layout: provider
modified: '2026-09-01'
name: Technical University of Darmstadt
nav: Providers
network: true
overview: 'Technical University of Darmstadt publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Technical University, and Germany.


  The Technical University of Darmstadt catalog on APIs.io includes 1 JSON-LD context.


  Technical University of Darmstadt''s developer surface includes GitHub presence, authentication, support, engineering blog, and 16 more developer resources.'
plans:
- name: Technical University Of Darmstadt Plans Pricing
  plan_count: 2
  slug: technical-university-of-darmstadt-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Technical University Of Darmstadt Rate Limits
  slug: technical-university-of-darmstadt-rate-limits
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 67.0
    catalog_earned_first_party: 0.0
    catalog_gap: 48.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 32.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/technical-university-of-darmstadt/refs/heads/main/screenshots/technical-university-of-darmstadt-2026-06-20T195009.png
security:
- kind: authentication
  name: Technical University Of Darmstadt Authentication
  slug: technical-university-of-darmstadt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Technical University Of Darmstadt Domain Security
  slug: technical-university-of-darmstadt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: technical-university-of-darmstadt
tags:
- Education
- Higher Education
- University
- Technical University
- Germany
- Research Data
- Open Access
- Scholarly Publishing
- Library
- OAI-PMH
- DSpace
- Identity Federation
- Shibboleth
- Research Computing
website: https://www.tu-darmstadt.de/index.en.jsp
---
