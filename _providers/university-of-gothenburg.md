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
  try_now: false
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
  score: 26.3
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: Språkbanken Text's corpus search engine, and the largest publicly callable surface the University of Gothenburg operates. Fourteen operations over 1,133 corpora — concordance query, sampling, frequenc
  name: Korp API v8 — Corpus Concordance Search
  slug: korp-api
- description: The catalogue over everything Språkbanken Text publishes — corpora, lexicons, models, analyses, utilities and collections — with BibTeX citation export, a published JSON schema endpoint and its own Op
  name: Språkbanken Text Metadata API v3
  slug: sbx-metadata-api
- description: Mink lets a researcher upload their own text, run it through the Sparv annotation pipeline and publish it into Korp. Sixty-three paths, the largest contract in this profile and the only one with a rea
  name: Mink API v3 — Bring Your Own Corpus
  slug: mink-api
- description: 'Sparv is Språkbanken Text''s annotation pipeline exposed as a job-submission web service: upload a corpus, generate a makefile, run the pipeline, poll status, download the annotated result. Institution'
  name: Sparv API v3 — Text Annotation Pipeline
  slug: sparv-api
- description: The editing and query surface over Språkbanken Text's lexical resources — entry CRUD, entry history and diff, resource permissions, field statistics, and inflection-table generation for the SAOL and S
  name: Karp API v7 — Lexical Resource Editing
  slug: karp-api
- description: 'The read-only search surface over the same lexical resources — three operations: config, search and count, across 31 lexical resources. Institution-operated, served from spraakbanken4.it.gu.se. Verifi'
  name: Karp Search API v1 — Karps sökgränssnitt
  slug: karp-search-api
- description: 'GUPEA (Gothenburg University Publications Electronic Archive) is the Gothenburg University Library''s institutional repository, running DSpace 8.3. Its OAI-PMH 2.0 endpoint is institution-operated: the'
  name: GUPEA Repository OAI-PMH 2.0 Interface
  slug: gupea-oai-pmh
- description: 'The HAL+JSON REST API of the same repository, on the same University host. Verified live 2026-09-01: anonymous GET https://gupea.ub.gu.se/server/api returned HTTP 200 application/hal+json, 8,531 bytes'
  name: GUPEA DSpace 8 REST API
  slug: gupea-dspace-rest
- description: The University's own Shibboleth identity provider, entityID https://idp3.it.gu.se/idp/shibboleth, which resolved directly to HTTP 200 on 2026-09-01 and is also published as signed metadata through the
  name: Shibboleth Identity Provider — SAML 2.0 Metadata
  slug: shibboleth-idp
- description: 'A second University of Gothenburg entity registered in the SWAMID aggregate, entityID http://idp.auth.gu.se/adfs/services/trust, DisplayName "University of Gothenburg (ADFS)" / "Göteborgs Universitet '
  name: Microsoft AD FS Identity Provider (SWAMID entity)
  slug: adfs-idp
- description: 'REGISTRY MEMBERSHIP, recorded as a fact about the institution, with no registry contract stored. The University''s Språkbanken Text unit is a live DataCite repository registrant: https://api.datacite.o'
  name: DataCite DOI Registration (client SND.SPRKB, via the Swedish National Data Service)
  slug: datacite-registration
- description: 'REGISTRY MEMBERSHIP, recorded as a fact about the institution. Two Crossref member records carry the primary name "University of Gothenburg", both returning HTTP 200 on 2026-09-01: member 36737 with D'
  name: Crossref Membership (members 36737 and 51378)
  slug: crossref-membership
- description: The Quality of Government Institute at the University of Gothenburg publishes open-access governance datasets (Standard, Basic, OECD, EU Regional and original datasets) as direct file downloads in CSV
  name: Quality of Government (QoG) Open Data
  slug: qog-data
- description: TENANT RELATIONSHIP, recorded with no contract stored. The staff portal at medarbetarportalen.gu.se redirects to login.microsoftonline.com with Entra tenant id 0798ed31-f5b0-4935-863c-73ee2505806e and
  name: Microsoft 365 / Entra ID Tenancy (medarbetarportalen.gu.se)
  slug: microsoft-365-tenancy
artifact_total: 31
common:
- group: company
  title: ''
  type: Website
  url: https://www.gu.se/en
- group: docs
  title: ''
  type: APIReference
  url: https://ws.spraakbanken.gu.se/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://spraakbanken.gu.se/en/resources
- group: other
  title: ''
  type: ResearchRepository
  url: https://gupea.ub.gu.se/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp3.it.gu.se/idp/shibboleth
- group: other
  title: ''
  type: OpenData
  url: https://www.gu.se/en/quality-government/qog-data/data-downloads
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.gu.se/en/study-in-gothenburg/programs-and-courses
- group: build
  title: ''
  type: GitHub
  url: https://github.com/spraakbanken
- group: build
  title: ''
  type: GitHub
  url: https://github.com/bcfgothenburg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-gothenburg/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gu.se/en/about-the-website/processing-personal-data
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gu.se/en/about-the-university-of-gothenburg/organisation/policy-rules-and-plans
- group: operate
  title: ''
  type: Support
  url: https://www.gu.se/en/contact
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-gothenburg-korp-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-gothenburg-metadata-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-gothenburg-mink-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-gothenburg-sparv-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-gothenburg-karp-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-gothenburg-karp-search-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/university-of-gothenburg-gupea-oai-pmh-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-gothenburg-sbx-resource.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/university-of-gothenburg-korp-info.json
- group: build
  title: ''
  type: Examples
  url: examples/README.md
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-gothenburg-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-gothenburg-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-gothenburg-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-gothenburg-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-gothenburg-oai-metadata-formats-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/university-of-gothenburg-rules.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-gothenburg-lifecycle.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-gothenburg-organization.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/university-of-gothenburg-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-gothenburg-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-gothenburg-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-gothenburg-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-gothenburg-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Gothenburg (Göteborgs universitet) is a public research university in Sweden, founded in 1891, with roughly 37,000 students and 6,000 employees. Its programmable footprint is larger and more genuinely its own than the June 2026 profile of this repository recorded, and it is concentrated in one place: Språkbanken Text, the Swedish Language Bank''s text division at the Department of Swedish, Multilingualism, Language Technology. Språkbanken publishes SIX OpenAPI documents from a single documentation index at ws.spraakbanken.gu.se/docs — Korp (corpus concordance search over 1,133 corpora), Karp v7 and Karp search v1 (lexical resources), Mink (upload, annotate and publish your own corpus), Sparv (the annotation pipeline as a job service) and the Språkbanken Text Metadata API (a 1,499-resource catalogue with BibTeX export). All six run on University of Gothenburg hosts, carry sb-info@svenska.gu.se as contact, and answered anonymous requests with HTTP 200 on 2026-09-01.
  The Gothenburg University Library separately operates GUPEA on DSpace 8.3, exposing both an OAI-PMH 2.0 harvesting endpoint (fourteen metadata formats, including the Swedish national uppsok thesis profile) and a HAL+JSON REST API on gupea.ub.gu.se. The University also runs its own Shibboleth SAML 2.0 identity provider, published as machine-readable metadata through SWAMID and eduGAIN. What is thin here is PRODUCT, not surface. There is no central developer portal, no API programme, no changelog, no status page, no rate-limit signal, no support channel and no documented credential-issuance route for any of the write surfaces. Five of the six contracts declare a security scheme and not one explains how to obtain a credential; two of them publish relative servers[] and no contact at all. This is a research unit''s engineering that happens to be excellent, published without any of the institutional scaffolding that would make it findable. Everything else that looks like a University of Gothenburg
  API is a relationship rather than a contract — DOI registration with DataCite through the Swedish National Data Service and with Crossref directly, a Microsoft Entra tenancy on medarbetarportalen.gu.se — and those are recorded here with x-operator and no vendor contract stored.'
examples:
- key_count: 6
  name: University Of Gothenburg Gupea Dspace Rest Root Example
  slug: university-of-gothenburg-gupea-dspace-rest-root-example
- key_count: 4
  name: University Of Gothenburg Karp Search Config Example
  slug: university-of-gothenburg-karp-search-config-example
- key_count: 6
  name: University Of Gothenburg Korp Info Example
  slug: university-of-gothenburg-korp-info-example
- key_count: 3
  name: University Of Gothenburg Metadata List Ids Example
  slug: university-of-gothenburg-metadata-list-ids-example
- key_count: 7
  name: University Of Gothenburg Mink Info Example
  slug: university-of-gothenburg-mink-info-example
- key_count: 2
  name: University Of Gothenburg Sparv Ping Example
  slug: university-of-gothenburg-sparv-ping-example
finops:
- name: University Of Gothenburg Finops
  service_category: Education
  slug: university-of-gothenburg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-gothenburg.png
json_schemas:
- name: Korp /info response
  property_count: 5
  slug: university-of-gothenburg-korp-info
- name: Språkbanken Text resource (corpus / lexicon / model / analysis / utility)
  property_count: 18
  slug: university-of-gothenburg-sbx-resource
jsonld:
- class_count: 23
  name: University Of Gothenburg Context
  property_count: 3
  slug: university-of-gothenburg-context
- class_count: 0
  name: University Of Gothenburg Organization Context
  property_count: 0
  slug: university-of-gothenburg-organization
layout: provider
modified: '2026-09-01'
name: University of Gothenburg
nav: Providers
network: true
overview: 'University of Gothenburg publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Korp API v8 — Corpus Concordance Search, Språkbanken Text Metadata API v3, Mink API v3 — Bring Your Own Corpus, and 4 more. Tagged areas include University, Higher Education, Education, Sweden, and Research.


  The University of Gothenburg catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  University of Gothenburg''s developer surface includes API reference, documentation, GitHub presence, support, code examples, authentication, and 31 more developer resources.'
plans:
- name: University Of Gothenburg Plans Pricing
  plan_count: 2
  slug: university-of-gothenburg-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: University Of Gothenburg Rate Limits
  slug: university-of-gothenburg-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: University of Gothenburg API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: university-of-gothenburg-rules
scopes:
- name: University Of Gothenburg Scopes
  scope_count: 0
  slug: university-of-gothenburg-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 39.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 33.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 40.9
    contract_quality: 60.7
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 40.9
    operational_transparency: 26.3
  previous_composite: 18.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-gothenburg/refs/heads/main/screenshots/university-of-gothenburg-2026-06-20T200152.png
security:
- kind: authentication
  name: University Of Gothenburg Authentication
  slug: university-of-gothenburg-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: University Of Gothenburg Domain Security
  slug: university-of-gothenburg-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: university-of-gothenburg
tags:
- University
- Higher Education
- Education
- Sweden
- Research
- Research Data
- Research Repository
- Open Data
- Library
- OAI-PMH
- Identity Federation
- Language Technology
- Natural Language Processing
- Corpus Linguistics
website: https://www.gu.se/en
---
