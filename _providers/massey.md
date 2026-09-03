---
access_model:
  confidence: medium
  label: Free · open harvesting endpoints, key-gated general API
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://mro.massey.ac.nz/server/oai/request
  baseurl_source: declared
  description: OAI-PMH 2.0 metadata-harvesting interface for Massey Research Online (Pātaka Rangahau), the university's DSpace institutional repository of theses, dissertations and research outputs. Fully anonymous,
  name: Massey Research Online OAI-PMH
  slug: mro-oai-pmh
- baseURL: https://mro.massey.ac.nz/server/api
  baseurl_source: declared
  description: HAL/JSON REST API for Massey Research Online, running DSpace 8.3. Anonymous read is permitted on the repository root, communities (19 of them) and collections; item and bitstream listings return 401 "
  name: Massey Research Online DSpace REST API
  slug: mro-rest
- baseURL: https://www.massey.ac.nz/api/v1/massey.cfc
  baseurl_source: declared
  description: Massey University's own news, events and staff-directory web service. A single endpoint, /api/v1/massey.cfc, selects a resource with a `path` parameter - news/articles, news/types, news/categories, ev
  name: Massey M-API WebService API v1
  slug: mapi-v1
- description: Massey University's own SAML 2.0 / Shibboleth Identity Provider. The metadata document is public, machine-readable and continuously published to federation partners. It advertises SAML 2.0, SAML 1.1 a
  name: Massey University Shibboleth Identity Provider
  slug: idp-shibboleth
- description: Massey University's Microsoft Entra ID tenant, discoverable by domain. The OpenID Connect discovery document is public and machine-readable and gives the issuer, authorization, token and JWKS endpoint
  name: Massey University Microsoft Entra ID Tenant
  slug: entra-id
- description: 'Massey University is a DataCite member organization within the DataCite New Zealand consortium and mints DOIs through two active repositories - massey.eqpliw, "Pātaka Rangahau Massey Research Online" '
  name: DataCite Membership — Massey University
  slug: datacite
- description: Massey University registers DOIs with Crossref under member id 12895, prefixes 10.33217 and 10.54322, 314 DOIs recorded (22 current, 292 backfile). A second Massey member, 22782, covers the Centre for
  name: Crossref Membership — Massey University
  slug: crossref
- description: Massey University's entry in the Research Organization Registry. This is the canonical machine-readable identifier for the institution and the anchor every other registry record in this profile points
  name: ROR Registration — Massey University
  slug: ror
- description: '"Discover" is Massey University Library''s discovery layer, an EBSCO Discovery Service tenancy under customer scope 4egzpd, selected by the library in 2012. It searches the library catalogue and subscr'
  name: Discover — EBSCO Discovery Service (Massey tenancy)
  slug: ebsco-discover
- description: Massey University Library's opening hours, room bookings and events run on a Springshare LibCal tenancy. LibCal exposes a REST API at /api/1.1/ which returned HTTP 403 without credentials on 2026-09-0
  name: Massey Library Hours & Bookings — Springshare LibCal (Massey tenancy)
  slug: libcal
- description: Massey University Library's public enquiry and FAQ service, running on a Springshare LibAnswers tenancy. Verified live 2026-09-01. Springshare's contract, Massey's tenancy and Massey's content.
  name: Massey Library Enquiries — Springshare LibAnswers (Massey tenancy)
  slug: libanswers
artifact_total: 25
common:
- group: company
  title: ''
  type: Website
  url: https://www.massey.ac.nz/
- group: docs
  title: ''
  type: Documentation
  url: https://www.massey.ac.nz/api/v1/
- group: docs
  title: ''
  type: APIReference
  url: https://www.massey.ac.nz/api/v1/
- group: other
  title: ''
  type: ResearchRepository
  url: https://mro.massey.ac.nz/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.massey.ac.nz/idp/shibboleth
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.massey.ac.nz/study/library/how-to-find-information-and-resources/using-discover-to-get-started/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.massey.ac.nz/study/study-and-assignment-support-and-guides/academic-integrity-student-guide/artificial-intelligence-ai-usage-and-detection/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Massey-Uni
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.massey.ac.nz/about/policies-procedures-and-guidelines/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.massey.ac.nz/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.massey.ac.nz/about/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://sites.massey.ac.nz/library/
- group: company
  title: ''
  type: BlogRSS
  url: https://sites.massey.ac.nz/library/feed/
- group: company
  title: ''
  type: News
  url: https://www.massey.ac.nz/about/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/massey-university/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/massey-mapi-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/massey-mro-dspace-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/massey-mapi-envelope.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/massey-mro-dspace-root.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/massey-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/massey-errors.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/massey-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/massey-vocabulary.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/massey-lifecycle.yml
- group: design
  title: ''
  type: Rules
  url: rules/massey-openapi-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/massey-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/massey-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/massey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/massey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/massey-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Massey University (Te Kunenga ki Pūrehuroa) is a public research university in New Zealand with campuses in Palmerston North (Manawatū), Wellington and Albany (Auckland). Its machine-readable footprint is real but small, and it is three different things at once. The university itself operates three callable surfaces: an OAI-PMH 2.0 endpoint and a DSpace 8.3 HAL/JSON REST API on its own host for Massey Research Online / Pātaka Rangahau, and the M-API, a news, events and staff-directory web service documented at www.massey.ac.nz/api/v1/ which is live and answering but API-key gated, self-described as unsupported, and closed to new key applications; the later M-API v1_2 host, api.massey.ac.nz, now states the service is no longer available. It operates two identity surfaces that are stronger than any of its APIs: a Shibboleth SAML 2.0 Identity Provider at idp.massey.ac.nz published through the Tuakiri Federation and eduGAIN, and a Microsoft Entra ID tenant discoverable by domain.
  And it is registered in three identifier registries - DataCite (as a DataCite New Zealand consortium organization with two repositories), Crossref (two members, three prefixes) and ROR. Everything else that looks like a Massey API is a vendor''s: library discovery is EBSCO Discovery Service, opening hours and enquiries run on Springshare LibCal and LibAnswers. There is no central developer portal, no published API catalog, no llms.txt and no .well-known/apis.json.'
examples:
- key_count: 10
  name: Massey Idp Metadata Summary
  slug: massey-idp-metadata-summary
- key_count: 2
  name: Massey Mro Communities
  slug: massey-mro-communities
- key_count: 2
  name: Massey Mro Root
  slug: massey-mro-root
finops:
- name: Massey Finops
  service_category: Education
  slug: massey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/massey.png
json_schemas:
- name: Massey M-API Response Envelope
  property_count: 4
  slug: massey-mapi-envelope
- name: Massey M-API News Article
  property_count: 12
  slug: massey-mapi-news-article
- name: Massey Research Online Repository Root
  property_count: 6
  slug: massey-mro-dspace-root
- name: Massey Research Online Paged HAL Collection
  property_count: 3
  slug: massey-mro-paged-hal
jsonld:
- class_count: 14
  name: Massey Context
  property_count: 2
  slug: massey-context
layout: provider
modified: '2026-09-01'
name: Massey University
nav: Providers
network: true
overview: 'Massey University publishes 3 APIs on the [APIs.io](https://apis.io/) network: Massey Research Online OAI-PMH, Massey Research Online DSpace REST API, and Massey M-API WebService API v1. Tagged areas include Education, Higher Education, University, New Zealand, and Research.


  The Massey University catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Massey University''s developer surface includes documentation, API reference, support, engineering blog, product news, authentication, and 25 more developer resources.'
plans:
- name: Massey Plans Pricing
  plan_count: 2
  slug: massey-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Massey Rate Limits
  slug: massey-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: Massey University API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: massey-openapi-rules
score:
  band: developing
  composite: 39.9
  coverage:
    artifact_dirs: 16
    catalog_gap: 38.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 34.1
    contract_quality: 26.1
    developer_ergonomics: 35.7
    discoverability: 59.3
    governance: 34.1
    operational_transparency: 26.3
  previous_composite: 39.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/massey/refs/heads/main/screenshots/massey-2026-06-20T185021.png
security:
- kind: authentication
  name: Massey Authentication
  slug: massey-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Massey Domain Security
  slug: massey-domain-security
  summary_line: TLSv1.3 · DMARC
slug: massey
tags:
- Education
- Higher Education
- University
- New Zealand
- Research
- Research Data
- Open Access
- Institutional Repository
- OAI-PMH
- DSpace
- Identity Federation
- Shibboleth
- SAML
- DataCite
- Crossref
- Library
website: https://www.massey.ac.nz/
---
