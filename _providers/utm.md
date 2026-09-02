---
access_model:
  confidence: high
  label: Free · no registration, no credential available to outsiders
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
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
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: UTM's institutional knowledge repository, running DSpace-CRIS on utmik.utm.my (161.139.22.165, inside UTM's own APNIC allocation 161.139.0.0/16, netname UTM-MY). The OAI-PMH 2.0 endpoint answers anony
  name: UTMIK Repository (DSpace-CRIS) — OAI-PMH and REST
  slug: utmik-repository
- description: Penerbit UTM Press runs the university's journal estate on PKP Open Journal Systems at journals.utm.my (161.139.22.105, UTM's own allocation). The site-wide OAI-PMH 2.0 interface answers anonymously a
  name: UTM Press Journals (Open Journal Systems) — OAI-PMH
  slug: utmpress-journals-oai
- description: UTM's institutional identity provider. The tenant (9c827912-3502-4333-ba47-1b242c3d20e6) is bound to UTM by domain ownership — realm discovery on user@utm.my returns FederationBrandName "Universiti Te
  name: UTM identity federation — Microsoft Entra ID tenant (SAML 2.0 / OpenID Connect)
  slug: entra-identity-federation
- description: 'UTM''s own university press is a Crossref member in its own right, not a customer of someone else''s prefix: member id 4787, DOI prefix 10.11113, 12,640 registered DOIs. Its flagship title, Jurnal Tekno'
  name: Crossref membership — Penerbit UTM Press (member 4787, prefix 10.11113)
  slug: crossref-member
- description: UTM is registered in the Research Organization Registry as ror.org/026w31v75, with domain utm.my, established 1975, GRID grid.410877.d, ISNI 0000 0001 2296 1505, Wikidata Q24401, and four Crossref Ope
  name: ROR registration — https://ror.org/026w31v75
  slug: ror-registration
- description: The older EPrints institutional repository, registered with ROAR (record 1358), OpenDOAR and Sherpa (record 987) and still linked from the UTM Library as http://eprints.utm.my. The host resolves to 16
  name: UTM Institutional Repository (UTM-IR) EPrints OAI-PMH — unreachable
  slug: eprints-oai
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.utm.my/
- group: build
  title: ''
  type: Library
  url: https://library.utm.my/
- group: other
  title: ''
  type: ResearchRepository
  url: https://utmik.utm.my/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.microsoftonline.com/utm.my/v2.0/.well-known/openid-configuration
- group: other
  title: ''
  type: SingleSignOn
  url: https://my.utm.my/login
- group: other
  title: ''
  type: AIPolicy
  url: https://fke.utm.my/wp-content/uploads/2024/11/Guidelines-for-the-Use-of-Generative-Artificial-Intelligence-in-Teaching-and-Learning-UTM-1.pdf
- group: company
  title: ''
  type: Blog
  url: https://news.utm.my/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.utm.my/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universiti-teknologi-malaysia/
- group: auth
  title: ''
  type: Authentication
  url: authentication/utm-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/utm-conformance.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/utm-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/utm-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/utm-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/utm-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/utm-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'UTM operates real institution-owned surfaces and they were read, but nothing it runs is consumable as an API by an unaffiliated caller. The two anonymously readable interfaces are metadata-harvesting protocols, not APIs UTM designed: OAI-PMH 2.0 on the UTMIK DSpace-CRIS repository and on the UTM Press OJS journal platform, both on UTM''s own APNIC allocation. Every REST interface behind them is closed — the OJS REST API v1 answers 401 with a JSON authorization error and publishes no route to request a token, and the DSpace REST collections answered 403 even though the HAL root is public. The one fully specified machine contract, UTM''s Microsoft Entra ID tenant, publishes signed SAML 2.0 metadata and an OIDC discovery document that anyone can read, but no registration_endpoint, so a client_id exists only if UTM Digital creates one. There is no developer portal: the www.utm.my sitemap contains exactly one policy page and no API, developer or open-data page, api.utm.my resolves
    and returns HTTP 200 with a 17-byte empty IIS document and 404s on every documented path, and no official UTM GitHub organization exists (the two name-matching orgs hold zero and one unrelated repository). Two limits are recorded rather than treated as findings about UTM. eprints.utm.my, the legacy EPrints repository still listed by ROAR, OpenDOAR and Sherpa, refused connections on both ports from three independent networks and is not credited as live. And utmik.utm.my answered fully at 17:26Z on 2026-09-01 — the OAI-PMH responseDate is the server''s own proof — then stopped answering this environment and two public proxies later the same day, so its pointers may grade dead on a re-probe while the surface is real. This is a correct thin profile, not a failed probe: more than fifty URLs were fetched successfully across eleven UTM hosts.'
  evidence:
  - status: 200
    url: https://utmik.utm.my/server/oai/request?verb=Identify
  - status: 200
    url: https://utmik.utm.my/server/oai/request?verb=ListMetadataFormats
  - status: 200
    url: https://utmik.utm.my/server/oai/request?verb=ListSets
  - status: 200
    url: https://utmik.utm.my/server/api
  - status: 403
    url: https://utmik.utm.my/server/api/core/communities
  - status: 200
    url: https://journals.utm.my/index.php/index/oai?verb=Identify
  - status: 200
    url: https://journals.utm.my/index.php/index/oai?verb=ListSets
  - status: 401
    url: https://journals.utm.my/jurnalteknologi/api/v1/issues
  - status: 200
    url: https://login.microsoftonline.com/utm.my/v2.0/.well-known/openid-configuration
  - status: 200
    url: https://login.microsoftonline.com/9c827912-3502-4333-ba47-1b242c3d20e6/federationmetadata/2007-06/federationmetadata.xml
  - status: 200
    url: https://login.microsoftonline.com/getuserrealm.srf?login=user@utm.my&json=1
  - status: 200
    url: https://api.crossref.org/members/4787
  - status: 200
    url: https://api.crossref.org/journals/2180-3722
  - status: 200
    url: https://api.ror.org/organizations/026w31v75
  - status: 200
    url: https://www.utm.my/
  - note: only one policy page in the whole sitemap; no API, developer or open-data page
    status: 200
    url: https://www.utm.my/wp-sitemap.xml
  - status: 200
    url: https://www.utm.my/privacy-policy/
  - status: 404
    url: https://www.utm.my/llms.txt
  - status: 404
    url: https://www.utm.my/.well-known/security.txt
  - note: 17-byte empty IIS document; soft-404, not credited as a surface
    status: 200
    url: https://api.utm.my/
  - status: 404
    url: https://api.utm.my/swagger/v1/swagger.json
  - status: 200
    url: https://library.utm.my/utm-institutional-repository/
  - status: 200
    url: https://my.utm.my/login
  - status: 200
    url: https://news.utm.my/
  - note: bot-challenged; not emitted as a BlogRSS pointer
    status: 403
    url: https://news.utm.my/feed/
  - note: Moodle is live but exposes no LTI 1.3 or web-service contract
    status: 404
    url: https://elearning.utm.my/mod/lti/auth.php
  - note: 7.8 MB parsed; zero entities matching utm.my or "teknologi malaysia"
    status: 200
    url: https://technical.edugain.org/api.php?action=list_entities&format=json
  - note: Malaysian Access Federation unreadable from here; SIFULAN membership neither confirmed nor denied
    status: 403
    url: https://www.sifulan.my/
  - note: zero results; UTM mints DOIs through Crossref, not DataCite
    status: 200
    url: https://api.datacite.org/clients?query=Universiti+Teknologi+Malaysia
  - note: connection refused on ports 80 and 443; HTTP 522 via two independent proxies
    status: 0
    url: http://eprints.utm.my/cgi/oai2?verb=Identify
  - note: linked from the UTM Library but does not connect; not emitted as a pointer
    status: 0
    url: https://openscience.utm.my/
  - note: research-computing host resolves but does not answer; no HPC service catalog found
    status: 0
    url: https://hpc.utm.my/
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'Universiti Teknologi Malaysia (UTM) is a public research university in Johor Bahru and Kuala Lumpur, Malaysia, one of the five institutions designated a Research University by the Ministry of Higher Education and ranked #181 in the QS World University Rankings 2025. UTM publishes no developer portal, no API documentation and no OpenAPI, AsyncAPI or JSON Schema of its own, and there is no route by which an unaffiliated developer can obtain a credential for anything it runs. Its programmable footprint is entirely made of standards it exposes rather than interfaces it designed, and every one of them sits on UTM''s own APNIC allocation (161.139.0.0/16, netname UTM-MY): the UTMIK Repository, a DSpace-CRIS institutional knowledge repository whose OAI-PMH 2.0 endpoint answers anonymously in twelve metadata formats including rioxx, etdms and an OpenAIRE CERIF-for-CRIS profile; the UTM Press journal platform, whose Open Journal Systems OAI-PMH interface has been harvestable since 2011
  and whose REST API v1 answers 401; and a Microsoft Entra ID tenant whose signed SAML 2.0 metadata and OpenID Connect discovery document are the most completely specified machine contract in this profile. UTM is registered in ROR, and its own publishing arm, Penerbit UTM Press, is Crossref member 4787 with prefix 10.11113 and 12,640 registered DOIs. The older EPrints repository at eprints.utm.my, still listed by ROAR, OpenDOAR and Sherpa and still linked from the UTM Library, refused connections on both ports from three independent networks on 2026-09-01 and is recorded here as unreachable rather than as a surface.'
finops:
- name: Utm Finops
  service_category: Education
  slug: utm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/utm.png
jsonld:
- class_count: 10
  name: Utm Context
  property_count: 1
  slug: utm-context
layout: provider
modified: '2026-09-01'
name: Universiti Teknologi Malaysia
nav: Providers
network: true
overview: 'Universiti Teknologi Malaysia publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Public Research University, and Technical University.


  The Universiti Teknologi Malaysia catalog on APIs.io includes 1 JSON-LD context.


  Universiti Teknologi Malaysia''s developer surface includes engineering blog, authentication, and 15 more developer resources.'
plans:
- name: Utm Plans Pricing
  plan_count: 2
  slug: utm-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Utm Rate Limits
  slug: utm-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 5.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 17.3
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/utm/refs/heads/main/screenshots/utm-2026-06-20T200738.png
security:
- kind: authentication
  name: Utm Authentication
  slug: utm-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Utm Domain Security
  slug: utm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: utm
tags:
- University
- Higher Education
- Education
- Public Research University
- Technical University
- Malaysia
- Research
- Open Access
- Institutional Repository
- Research Repository
- Scholarly Publishing
- OAI-PMH
- Identity Federation
- SAML
- Crossref
website: https://www.utm.my/
---
