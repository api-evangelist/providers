---
access_model:
  confidence: high
  label: Free · anonymous metadata harvesting
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probed
  trial: false
  try_now: true
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
  scored_at: '2026-09-03'
api_count: 9
apis:
- description: OAI-PMH 2.0 metadata harvesting endpoint for Leiden University Scholarly Publications, the Islandora-based institutional repository holding PhD theses, articles, journals, book series and conference p
  name: Scholarly Publications OAI-PMH
  slug: scholarly-oai
- description: Leiden University's own SAML 2.0 identity-provider metadata document, authored and XML-DSig signed by Leiden and served as text/xml from login.uaccess.leidenuniv.nl. Asserts the scopes leidenuniv.nl a
  name: Leiden University SAML 2.0 Identity Provider Metadata
  slug: saml-idp
- description: Leiden University's IDPSSODescriptor is published in the SURFconext national identity federation aggregate operated by SURF B.V., carrying mdui:DisplayName "Leiden University" and shibmd:Scope leidenu
  name: SURFconext Federation Membership
  slug: surfconext
- description: Leiden University is a DataCite consortium_organization with symbol VIOJ, organizationType academicInstitution, country NL, and rorId https://ror.org/027bh9e22, registered 2023-02-08. Two repositories
  name: DataCite Consortium Membership (VIOJ)
  slug: datacite
- description: Leiden University Press, Leiden University's own academic press, is Crossref member 22598 with 2,588 registered DOIs. A registry membership and a fact about the institution; the Crossref REST API cont
  name: Crossref Membership — Leiden University Press
  slug: crossref
- description: Leiden University is registered in the Research Organization Registry as https://ror.org/027bh9e22, domain leidenuniv.nl. A registry entry about the institution; the ROR API contract is ROR's and is n
  name: ROR Registration
  slug: ror
- description: Leiden University's research data management portal runs as an institution-specific tenancy of Yoda/iRODS hosted by SURF at leiden-yoda.irods.surfsara.nl. The tenancy is real and is Leiden's — it is r
  name: Yoda Research Data Management Portal (Leiden tenancy)
  slug: yoda
- description: Leiden's learning management system is a D2L Brightspace tenancy on Leiden's own hostname, brightspace.universiteitleiden.nl, authenticating through SURFconext. Its D2L Valence API version manifest is
  name: D2L Brightspace LMS (Leiden tenancy)
  slug: brightspace
- description: Leiden University Libraries' discovery catalogue at catalogue.leidenuniv.nl CNAMEs to leiden.primo.exlibrisgroup.com and serves Ex Libris Primo VE with view id 31UKB_LEU:UBL_NDE. The institution-speci
  name: Library Discovery Catalogue (Ex Libris Primo VE tenancy)
  slug: primo
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.universiteitleiden.nl/en
- group: company
  title: ''
  type: Website
  url: https://www.leidenuniv.nl/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.universiteitleiden.nl/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://www.staff.universiteitleiden.nl/binaries/content/assets/ul2staff/ict/responsible-disclosure-eng.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.organisatiegids.universiteitleiden.nl/en/regulations/general/privacy-statements
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.organisatiegids.universiteitleiden.nl/en/regulations/general/university-website-disclaimer
- group: other
  title: ''
  type: IdentityFederation
  url: authentication/leiden-identity-federation.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholarlypublications.universiteitleiden.nl/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://catalogue.leidenuniv.nl/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://studiegids.universiteitleiden.nl/
- group: other
  title: ''
  type: OpenData
  url: https://home.strw.leidenuniv.nl/~moldata/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LeidenUniversityLibrary
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CWTSLeiden
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/leiden-university/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leiden-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/leiden-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leiden-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leiden-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Leiden University (Universiteit Leiden), founded 1575, is the oldest university in the Netherlands and a founding member of LERU. It operates a federation of bought systems, not a developer program: it publishes no public REST API and no developer portal, api.universiteitleiden.nl, api.leidenuniv.nl, developer.universiteitleiden.nl and data.universiteitleiden.nl do not resolve, and neither of its GitHub organisations holds a single OpenAPI or Swagger file. What it does operate, on its own infrastructure, are three verified machine-readable surfaces: an OAI-PMH 2.0 endpoint for the Scholarly Publications repository, a signed SAML 2.0 identity-provider metadata document registered in the SURFconext national federation, and a PGP-signed RFC 9116 security.txt. Everything else that looks programmable belongs to a vendor Leiden buys from — Ex Libris Primo, D2L Brightspace, SURF Yoda — and is recorded below as a tenancy, never as Leiden''s engineering.'
finops:
- name: Leiden Finops
  service_category: Education
  slug: leiden-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leiden.png
jsonld:
- class_count: 22
  name: Leiden Context
  property_count: 5
  slug: leiden-context
layout: provider
modified: '2026-09-01'
name: Leiden University
nav: Providers
network: true
overview: 'Leiden University publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Netherlands, and LERU.


  The Leiden University catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Leiden Plans Pricing
  plan_count: 2
  slug: leiden-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Leiden Rate Limits
  slug: leiden-rate-limits
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 21.4
    discoverability: 85.2
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.3
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leiden/refs/heads/main/screenshots/leiden-2026-06-20T184415.png
security:
- kind: domain-security
  name: Leiden Domain Security
  slug: leiden-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: leiden
tags:
- University
- Higher Education
- Education
- Netherlands
- LERU
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- Library
- Research Data Management
website: https://www.universiteitleiden.nl/en
---
