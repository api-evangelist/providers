---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
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
    error_semantics: documented
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
  score: 25.9
  scored_at: '2026-08-26'
api_count: 8
apis:
- description: Unauthenticated read API over the university's scholarly record — communities that mirror the faculty structure (理学部, 人文学部, 专利 with 25,721 items), their collections, items, Dublin Core metadata, attac
  name: PKU Institutional Repository REST API
  slug: ir-rest
- description: 'OAI-PMH 2.0 metadata-harvesting endpoint for the institutional repository, live since at least 2015-09-25 (its earliest datestamp). Advertises twelve metadata formats — oai_dc, qdc, mods, mets, didl, '
  name: PKU Institutional Repository OAI-PMH API
  slug: ir-oai-pmh
- description: OpenSearch 1.1 query interface returning an Atom feed of repository records, served from the institution's own host. Verified live 2026-08-19 (HTTP 200, 32KB Atom response for query=test).
  name: PKU Institutional Repository OpenSearch Feed
  slug: ir-opensearch
- description: The university's federated identity provider, publishing live Shibboleth/SAML 2.0 metadata as machine-readable XML. Declares SAML 2.0 POST, POST-SimpleSign and Redirect SSO/SLO bindings, the legacy Sh
  name: Peking University Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: idp-saml
- description: China's national identity federation for higher education and research, operated by Peking University and a full eduGAIN member. 1,042 SAML entities in eduGAIN carry CARSI as their registration author
  name: CARSI — CERNET Authentication and Resource Sharing Infrastructure
  slug: carsi
- description: OpenSCOW ("Super Computing On Web") is an HPC portal and management system authored at Peking University; CraneSched is its distributed scheduler for HPC and AI workloads. Their APIs are defined in ro
  name: OpenSCOW / CraneSched research-computing APIs
  slug: openscow
- description: Dataverse-based research data repository operated by the PKU Library across social science, health, bioinformatics and NLP collections. Verified live by this catalog on 2026-06-03 (183 dataverses, 485
  name: PKU Open Research Data Platform (Dataverse REST API)
  slug: opendata-rest
- description: OAI-PMH 2.0 metadata-harvesting endpoint for the Open Research Data Platform, verified responding to the Identify verb on 2026-06-03 with Dublin Core and DataCite support via the XOAI toolkit. Unreach
  name: PKU Open Research Data Platform (OAI-PMH)
  slug: opendata-oaipmh
artifact_total: 18
common:
- group: company
  title: ''
  type: Website
  url: https://www.pku.edu.cn/
- group: company
  title: ''
  type: About
  url: https://english.pku.edu.cn/
- group: other
  title: ''
  type: ResearchRepository
  url: https://ir.pku.edu.cn/
- group: other
  title: ''
  type: OpenData
  url: https://opendata.pku.edu.cn/
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.carsi.edu.cn/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://lib.pku.edu.cn/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://dean.pku.edu.cn/
- group: other
  title: ''
  type: ResearchComputing
  url: https://hpc.pku.edu.cn/
- group: other
  title: ''
  type: AIPolicy
  url: https://stl.pku.edu.cn/uploads/202411/26102211_98533_67921156%5B-%5DSTLAcademicRules-AIPolicy-Fall2024.pdf
- group: build
  title: ''
  type: AITooling
  url: https://lrcguides.stl.pku.edu.cn/c.php?g=967766&p=7037024
- group: company
  title: ''
  type: Blog
  url: https://news.pku.edu.cn/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PKUHPC
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/peking-university/
- group: auth
  title: ''
  type: Authentication
  url: authentication/peking-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/peking-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/peking-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/peking-errors.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/peking-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/peking-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/peking-ir-item.json
- group: build
  title: ''
  type: Examples
  url: examples/peking-ir-oai-identify-response.xml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/peking-context.jsonld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peking-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/peking-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/peking-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/peking-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: Peking University (北京大学, PKU) is a public research university in Beijing and, with Tsinghua, one of the two apex institutions of the Chinese system. Like most universities it operates no central developer portal and publishes no OpenAPI, but unlike most it runs three genuinely institution-operated machine-readable surfaces. Its Institutional Repository at ir.pku.edu.cn — PKU Library, Handle prefix 20.500.11897, content back to 2015 — answers an unauthenticated JSON REST API, a conforming OAI-PMH 2.0 endpoint advertising twelve metadata formats, and an OpenSearch Atom feed. Its Shibboleth identity provider publishes live SAML 2.0 metadata and has been in eduGAIN production since June 2019. Most significantly, the Peking University Computer Center operates CARSI, China's national research-and-education identity federation and a full eduGAIN member, which is the registration authority for 1,042 federated entities and serves 500+ Chinese universities; PKU also runs the national
  eduroam service. The PKU HPC group additionally authors OpenSCOW and CraneSched, open-source HPC platform and scheduler whose APIs are defined in some forty Protocol Buffer files, though those describe self-hosted software rather than a hosted endpoint. The Dataverse-based Open Research Data Platform at opendata.pku.edu.cn was verified live in June 2026 but did not answer any HTTPS request during this pass. No API is documented for developers, none carries a versioning or deprecation policy, and campus systems — IAAA authentication, the 教学网 LMS, the registrar — are gated. The footprint is small, real, and almost entirely a by-product of scholarly infrastructure rather than a developer programme.
finops:
- name: Peking Finops
  service_category: Education
  slug: peking-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peking.png
json_schemas:
- name: PKU Institutional Repository Collection
  property_count: 18
  slug: peking-ir-collection
- name: PKU Institutional Repository Community
  property_count: 15
  slug: peking-ir-community
- name: PKU Institutional Repository Item
  property_count: 14
  slug: peking-ir-item
jsonld:
- class_count: 17
  name: Peking Context
  property_count: 4
  slug: peking-context
layout: provider
modified: '2026-08-19'
name: Peking University
nav: Providers
network: true
overview: 'Peking University publishes 2 APIs on the [APIs.io](https://apis.io/) network: PKU Institutional Repository REST API and PKU Institutional Repository OAI-PMH API. Tagged areas include University, Higher Education, Education, China, and Public Research University.


  The Peking University catalog on APIs.io includes 1 JSON-LD context.


  Peking University''s developer surface includes engineering blog, authentication, code examples, and 24 more developer resources.'
plans:
- name: Peking Plans Pricing
  plan_count: 2
  slug: peking-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Peking Rate Limits
  slug: peking-rate-limits
scopes:
- name: Peking Scopes
  scope_count: 0
  slug: peking-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.7
  delta: 1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 63.6
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 22.0
    operational_transparency: 23.7
  previous_composite: 41.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peking/refs/heads/main/screenshots/peking-2026-06-20T191532.png
security:
- kind: authentication
  name: Peking Authentication
  slug: peking-authentication
  summary_line: saml2/shibboleth/cas/oauth2/none · 4 schemes
- kind: domain-security
  name: Peking Domain Security
  slug: peking-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: peking
tags:
- University
- Higher Education
- Education
- China
- Public Research University
- C9 League
- Research Repository
- Identity Federation
- Research Data
- Open Data
- Research Computing
- OAI-PMH
website: https://www.pku.edu.cn/
---
