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
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://catalog.lib.kyushu-u.ac.jp/mmd/mmd_api/oai-pmh/
  baseurl_source: declared
  description: Live OAI-PMH 2.0 metadata harvesting interface for the Kyushu University Institutional Repository (QIR) and the library's other digital collections, run by Kyushu University Library on the university'
  name: Kyushu University Institutional Repository (QIR) OAI-PMH
  slug: qir-oai-pmh
- description: Quarterly full-metadata TSV exports for the Kyushu University Library digital collections, distributed through the Handle system under the university's own 2324 prefix. Covers the institutional reposi
  name: QIR / Kyushu University Collections Bulk Metadata (TSV via Handle)
  slug: qir-bulk-tsv
- description: Kyushu University's own SAML 2.0 Identity Provider, registered in GakuNin — the Japanese academic access-management federation operated by NII — and exported to eduGAIN. entityID https://idp.kyushu-u.
  name: GakuNin Shibboleth Identity Provider
  slug: gakunin-shibboleth-idp
- description: 'Kyushu University is a DataCite consortium organization — provider id `kyushuu`, symbol KYUSHUU, region APAC, country JP, active since 2023-02-28 — inside the Japan Link Center (`jalcco`) consortium, '
  name: DataCite DOI Registration Membership
  slug: datacite-membership
- description: Two Kyushu University units are Crossref members registering DOIs under their own prefixes, verified against api.crossref.org on 2026-09-01 — member 3044 "Kyushu University" (prefix 10.5109, 6,284 DOI
  name: Crossref DOI Registration Membership
  slug: crossref-membership
- description: Kyushu University's Research Organization Registry record, ROR ID 00p4k0j84, carrying the English, romanized (Kyūshū Daigaku) and Japanese (九州大学) names. The identifier that makes the DataCite provider
  name: ROR Organization Record
  slug: ror-registration
- description: Kyushu University's research information portal, an Elsevier Pure tenant at kyushu-u.elsevierpure.com. The researchers, publications, organizational units and research outputs behind it are the univer
  name: Kyushu University Pure Research Portal (Elsevier tenant)
  slug: pure-research-portal
- description: Kyushu University's research computing service, operated by the Research Institute for Information Technology (RIIT) around the Genkai supercomputer. Three machine-facing portals run on the university
  name: Genkai Supercomputer System (Research Institute for Information Technology)
  slug: genkai-research-computing
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.kyushu-u.ac.jp/en/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lib.kyushu-u.ac.jp/en/metadata
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RIIT-KyushuUniv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/kyushu-university/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kyushu-u.ac.jp/en/website/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kyushu-u.ac.jp/en/website/sitepolicy
- group: operate
  title: ''
  type: Support
  url: https://www.kyushu-u.ac.jp/en/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.kyushu-u.ac.jp/en/news/
- group: other
  title: ''
  type: ResearchRepository
  url: https://catalog.lib.kyushu-u.ac.jp/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalog.lib.kyushu-u.ac.jp/opac_search/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://syllabus.kyushu-u.ac.jp/
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.gakunin.nii.ac.jp/gakunin-metadata.xml
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.cc.kyushu-u.ac.jp/scp/
- group: other
  title: ''
  type: AIPolicy
  url: https://mirai.kyushu-u.ac.jp/curriculum/generative-ai/
- group: build
  title: ''
  type: AITooling
  url: https://guides.lib.kyushu-u.ac.jp/AI-and-academia
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/kyushu-qir-oai-pmh-openapi.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kyushu-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kyushu-authentication.yml
- group: design
  title: ''
  type: Errors
  url: errors/kyushu-qir-oai-pmh-errors.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/kyushu-qir-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/kyushu-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kyushu-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kyushu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kyushu-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kyushu-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Kyushu University (九州大学) is a Japanese national research university in Fukuoka, one of the seven former Imperial Universities and a Designated National University, ranked #171 in the QS World University Rankings 2027. Its programmable footprint is small and concentrated in scholarly infrastructure rather than in a developer platform, and this profile says so rather than padding it. Exactly one unambiguously institution-operated API was found and exercised end to end: the OAI-PMH 2.0 metadata interface for the Kyushu University Institutional Repository and the library''s digital collections, at catalog.lib.kyushu-u.ac.jp. That endpoint is unusual for this cohort — most Japanese university repositories are tenants on NII''s JAIRO Cloud, while Kyushu runs the protocol implementation itself on its own registrable domain, with a kyushu-u.ac.jp administrative contact, four metadata formats and seven collection sets. Everything else is a relationship rather than a contract: the university
  operates its own SAML 2.0 Shibboleth Identity Provider registered in the GakuNin national federation since 2011 and exported to eduGAIN; it is a DataCite consortium organization under the Japan Link Center and a Crossref member through two units; its research portal is an Elsevier Pure tenant whose live OpenAPI is Elsevier''s contract, not Kyushu''s, and is deliberately not saved here. There is no central developer portal, no API key issuance, no open-data platform, no llms.txt, no MCP server and no OpenAPI published anywhere on kyushu-u.ac.jp. The public syllabus and the Genkai supercomputer portals are HTML and login walls, not APIs.'
examples:
- key_count: 7
  name: Kyushu Qir Oai Pmh Getrecord Example
  slug: kyushu-qir-oai-pmh-getrecord-example
- key_count: 7
  name: Kyushu Qir Oai Pmh Identify Example
  slug: kyushu-qir-oai-pmh-identify-example
- key_count: 7
  name: Kyushu Qir Oai Pmh Listmetadataformats Example
  slug: kyushu-qir-oai-pmh-listmetadataformats-example
- key_count: 7
  name: Kyushu Qir Oai Pmh Listsets Example
  slug: kyushu-qir-oai-pmh-listsets-example
finops:
- name: Kyushu Finops
  service_category: Education
  slug: kyushu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kyushu.png
jsonld:
- class_count: 28
  name: Kyushu Context
  property_count: 1
  slug: kyushu-context
layout: provider
modified: '2026-09-01'
name: Kyushu University
nav: Providers
network: true
overview: 'Kyushu University publishes 1 API on the [APIs.io](https://apis.io/) network: Institutional Repository (QIR) OAI-PMH. Tagged areas include University, Higher Education, Education, Research, and Japan.


  The Kyushu University catalog on APIs.io includes 1 JSON-LD context.


  Kyushu University''s developer surface includes documentation, support, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Kyushu Plans Pricing
  plan_count: 2
  slug: kyushu-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Kyushu Rate Limits
  slug: kyushu-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 13
    catalog_gap: 46.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 19.7
    contract_quality: 22.3
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 19.7
    operational_transparency: 26.3
  previous_composite: 36.7
  provenance:
    conformance: derived
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kyushu/refs/heads/main/screenshots/kyushu-2026-06-20T184233.png
security:
- kind: authentication
  name: Kyushu Authentication
  slug: kyushu-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Kyushu Domain Security
  slug: kyushu-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: kyushu
tags:
- University
- Higher Education
- Education
- Research
- Japan
- National University
- Public Research University
- Institutional Repository
- Research Data
- Identity Federation
- Library
- Course Catalog
- Open Access
- OAI-PMH
- Metadata
- Research Computing
website: https://www.kyushu-u.ac.jp/en/
---
