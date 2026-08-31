---
access_model:
  confidence: high
  label: Free · no credential required
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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Documented HTTP GET service that exports the publication list of one ULB scholar (identified by matricule or DAI) or of a group of scholars, in APA, BibTeX, RIS, CSV, xml-brief, xml-brief-ext or xml-f
  name: DI-fusion Export API
  slug: difusion-export
- description: 'OAI-PMH 2.0 endpoint for the DI-fusion repository. Answers verb=Identify and verb=ListMetadataFormats with valid protocol documents (advertising oai_dc only), but under HTTP 500 and with an HTML page '
  name: DI-fusion OAI-PMH Harvesting Endpoint
  slug: difusion-oai-pmh
- description: OpenSearch 1.1 description document for the DI-fusion discovery interface, allowing a client to register DI-fusion as a search provider and construct query URLs programmatically. HTTP 200, text/xml, 7
  name: DI-fusion OpenSearch Description
  slug: difusion-opensearch
- description: ULB's institutional SAML 2.0 identity provider publishes complete, unauthenticated metadata at https://auth.ulb.be/idp/metadata — IDPSSODescriptor and AttributeAuthorityDescriptor roles, SingleSignOnS
  name: ULB Shibboleth Identity Provider (SAML 2.0 metadata)
  slug: shibboleth-idp
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.ulb.be/en
- group: start
  title: ''
  type: Portal
  url: https://difusion.ulb.ac.be/
- group: other
  title: ''
  type: ResearchRepository
  url: https://bib.ulb.be/en/find-documents/di-fusion
- group: docs
  title: ''
  type: Documentation
  url: https://bib.ulb.be/medias/fichier/difusion-download-and-api_1678451163130-pdf?ID_FICHE=10054&INLINE=FALSE
- group: other
  title: ''
  type: IdentityFederation
  url: https://auth.ulb.be/idp/metadata
- group: build
  title: ''
  type: LibraryCatalog
  url: https://bib.ulb.be/en
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.ulb.be/fr/se-former/catalogue-des-formations
- group: other
  title: ''
  type: AIPolicy
  url: https://www.ulb.be/fr/intelligence-artificielle/note-dintention-relative-aux-outils-dia-dans-lenseignement-a-lulb
- group: build
  title: ''
  type: AITooling
  url: https://www.ulb.be/fr/intelligence-artificielle/academ-ia
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ulb
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bib.ulb.be/en/find-documents/di-fusion/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ulb.be/fr/mentions-legales/politique-de-protection-des-donnees-a-lulb
- group: operate
  title: ''
  type: Support
  url: https://www.ulb.be/en/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.ulb.be/fr/actus-et-agenda
- group: company
  title: ''
  type: LinkedIn
  url: https://be.linkedin.com/school/universite-libre-de-bruxelles/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ulb-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ulb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ulb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ulb-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Université libre de Bruxelles (ULB) is a French-speaking research university in Brussels, Belgium, founded in 1834 and funded through the Fédération Wallonie-Bruxelles. Unusually for this cohort, ULB operates its research infrastructure itself rather than renting it: there is no Figshare, Elsevier Pure, Dataverse or Ex Libris Esploro tenant under ULB''s name, and the one documented API it publishes is its own engineering. DI-fusion, the institutional repository run by the ULB Libraries, exposes a bespoke HTTP export service at difusion-svc.ulb.ac.be that renders a scholar''s or a group''s publication list in APA, BibTeX, RIS, CSV and three ULB XML formats, documented in a 15-page PDF the library publishes itself. ULB also runs a Shibboleth SAML 2.0 identity provider registered in the Belnet R&E Federation and visible in eduGAIN, an OAI-PMH endpoint and an OpenSearch description on its self-hosted VuFind discovery layer, and mints its own info:ulb-repo/semantics/ publication-type
  vocabulary. The footprint is small and visibly under-maintained: the richest documented export format returns 403, the format added by the most recent documentation revision returns 500, the OAI-PMH endpoint answers Identify but rejects the metadata prefix it advertises so nothing can actually be harvested, the advertised unAPI server does not answer, and the DSpace instance behind its full-text links is erroring. There is no developer portal, no changelog, no status page, no OpenAPI of ULB''s own, and every other ULB system — timetable, registrar, library discovery, researcher CVs — is behind the central ULB login or unreachable from the public internet.'
finops:
- name: Ulb Finops
  service_category: Education
  slug: ulb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ulb.png
json_schemas:
- name: DI-fusion publication list (xml-brief)
  property_count: 2
  slug: ulb-difusion-publist
jsonld:
- class_count: 11
  name: Ulb Context
  property_count: 5
  slug: ulb-context
layout: provider
modified: '2026-08-30'
name: Université libre de Bruxelles
nav: Providers
network: true
overview: 'Université libre de Bruxelles publishes 2 APIs on the [APIs.io](https://apis.io/) network: DI-fusion Export API and DI-fusion OAI-PMH Harvesting Endpoint. Tagged areas include University, Higher Education, Education, Belgium, and Europe.


  The Université libre de Bruxelles catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Université libre de Bruxelles'' developer surface includes developer portal, documentation, support, engineering blog, and 16 more developer resources.'
plans:
- name: Ulb Plans Pricing
  plan_count: 2
  slug: ulb-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Ulb Rate Limits
  slug: ulb-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Université libre de Bruxelles API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: ulb-difusion-rules
scopes:
- name: Ulb Scopes
  scope_count: 0
  slug: ulb-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 40.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 30.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 60.5
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 15.2
    operational_transparency: 23.7
  previous_composite: 19.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/ulb/refs/heads/main/screenshots/ulb-2026-06-20T200008.png
security:
- kind: authentication
  name: Ulb Authentication
  slug: ulb-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ulb Domain Security
  slug: ulb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ulb
tags:
- University
- Higher Education
- Education
- Belgium
- Europe
- Research
- Research Data
- Institutional Repository
- Open Access
- Identity Federation
- OAI-PMH
- Library
website: https://www.ulb.be/en
---
