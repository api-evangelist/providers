---
access_model:
  confidence: high
  label: Free · anonymous, no registration
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: 'Public, anonymous, read-only GraphQL API for jMorp — the Japanese Multi Omics Reference Panel published by the Tohoku Medical Megabank Organization (ToMMo), an institute of Tohoku University. Runs on '
  name: jMorp GraphQL API (Tohoku Medical Megabank Organization)
  slug: jmorp-graphql
- description: OAI-PMH 2.0 metadata harvesting endpoint for TOUR (TOhoku University Repository). The collection, the departmental set hierarchy and the administrative contact (syskan@grp.tohoku.ac.jp) are Tohoku Uni
  name: TOUR Institutional Repository OAI-PMH
  slug: tour-oai-pmh
- description: Tohoku University's own SAML 2.0 Identity Provider, registered in GakuNin — the Japanese academic access-management federation operated by NII. entityID https://idp.auth.tohoku.ac.jp/idp/shibboleth, O
  name: GakuNin Shibboleth Identity Provider
  slug: gakunin-shibboleth-idp
- description: Three Tohoku University units are Crossref members registering DOIs under their own prefixes, verified against api.crossref.org on 2026-09-01 — member 622 Tohoku University Medical Press (10.1620, 11,
  name: Crossref DOI Registration Membership
  slug: crossref-membership
- description: Tohoku University's Research Organization Registry record, ROR ID 01dq60k83, carrying the English, romanized and Japanese names and the canonical institutional URL. The identifier that makes the Cross
  name: ROR Organization Record
  slug: ror-registration
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.tohoku.ac.jp/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cl-tohoku
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tohoku-univ/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tohoku.ac.jp/en/misc/privacy_policy.html
- group: operate
  title: ''
  type: Support
  url: https://www.tohoku.ac.jp/en/misc/contact.html
- group: company
  title: ''
  type: Blog
  url: https://www.tohoku.ac.jp/en/news/
- group: docs
  title: ''
  type: Documentation
  url: https://www.library.tohoku.ac.jp/support/openaccess/
- group: other
  title: ''
  type: ResearchRepository
  url: https://tohoku.repo.nii.ac.jp/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://opac.library.tohoku.ac.jp/opac/opac_search/?lang=1&smode=1
- group: learn
  title: ''
  type: CourseCatalog
  url: https://qsl.cds.tohoku.ac.jp/qsl/
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.gakunin.nii.ac.jp/gakunin-metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.cc.tohoku.ac.jp/en/
- group: other
  title: ''
  type: AIPolicy
  url: https://olg.cds.tohoku.ac.jp/forstaff/ai-tools
- group: other
  title: ''
  type: OpenData
  url: https://jmorp.megabank.tohoku.ac.jp/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tohoku-context.jsonld
- group: design
  title: ''
  type: Conformance
  url: conformance/tohoku-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tohoku-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tohoku-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tohoku-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tohoku-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tohoku University is a Japanese national research university in Sendai, founded in 1907, one of the seven former Imperial Universities and a Designated National University. Its programmable footprint is small, unevenly distributed, and mostly NOT operated by central IT — which is the honest shape for a university, and the profile says so rather than padding it. Exactly one unambiguously institution-operated API was found: jMorp, the Japanese Multi Omics Reference Panel published by the Tohoku Medical Megabank Organization at jmorp.megabank.tohoku.ac.jp, which answers anonymous GraphQL queries and full schema introspection over a 305-field read-only query root. Everything else is a relationship rather than a contract: the TOUR institutional repository is a tenant on NII''s JAIRO Cloud (WEKO3) with a live OAI-PMH 2.0 endpoint; the university operates its own SAML 2.0 Shibboleth Identity Provider registered in the GakuNin national academic federation; and three of its units are
  Crossref DOI-registering members. There is no central developer portal, no API key issuance, no open-data platform, no llms.txt, no MCP server and no published OpenAPI anywhere on tohoku.ac.jp. Public course information is served as HTML by the university''s own QuickSyllabus, not as an API.'
examples:
- key_count: 7
  name: Tohoku Jmorp Datasets Example
  slug: tohoku-jmorp-datasets-example
- key_count: 7
  name: Tohoku Jmorp Gene Lookup Example
  slug: tohoku-jmorp-gene-lookup-example
- key_count: 7
  name: Tohoku Tour Oai Pmh Identify Example
  slug: tohoku-tour-oai-pmh-identify-example
finops:
- name: Tohoku Finops
  service_category: Education
  slug: tohoku-finops
graphqls:
- description: 'generated: 2026-09-01'
  name: jMorp GraphQL API — Tohoku University (ToMMo)
  slug: tohoku-jmorp-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tohoku.png
jsonld:
- class_count: 28
  name: Tohoku Context
  property_count: 6
  slug: tohoku-context
layout: provider
modified: '2026-09-01'
name: Tohoku University
nav: Providers
network: true
overview: 'Tohoku University publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Research, and Japan.


  The Tohoku University catalog on APIs.io includes 1 JSON-LD context.


  Tohoku University''s developer surface includes support, engineering blog, documentation, and 18 more developer resources.'
plans:
- name: Tohoku Plans Pricing
  plan_count: 2
  slug: tohoku-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Tohoku Rate Limits
  slug: tohoku-rate-limits
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 51.6
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 34.4
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tohoku/refs/heads/main/screenshots/tohoku-2026-06-20T195441.png
security:
- kind: authentication
  name: Tohoku Authentication
  slug: tohoku-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Tohoku Domain Security
  slug: tohoku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tohoku
tags:
- University
- Higher Education
- Education
- Research
- Japan
- National University
- Public Research University
- Genomics
- Research Data
- Institutional Repository
- Identity Federation
- Course Catalog
- Library
- Open Access
- OAI-PMH
- GraphQL
website: https://www.tohoku.ac.jp/en/
---
