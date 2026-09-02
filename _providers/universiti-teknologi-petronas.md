---
access_model:
  confidence: high
  label: Free · open, no registration
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
    error_semantics: documented
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
  score: 23.4
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: UTPedia ("UTP Electronic and Digital Intellectual Asset") holds theses, dissertations and final-year projects. It serves an open OAI-PMH 2.0 endpoint (formats oai_dc, mets, didl, rdf, oai_bibl, uketd_
  name: UTPedia Institutional Repository
  slug: utpedia
- description: The second EPrints repository UTP runs, holding staff publication records back to 2010. Open OAI-PMH 2.0, an unauthenticated EPrints REST interface, a search endpoint with selectable serialisations (A
  name: UTP Scholarly Publication Repository
  slug: scholars
- description: 'UTP federates identity through its own Microsoft Entra ID tenant rather than a Shibboleth IdP. Both the SAML 2.0 federation metadata (IDPSSODescriptor, HTTP-POST and HTTP-Redirect SingleSignOnService '
  name: UTP Identity Federation (Microsoft Entra ID tenant)
  slug: entra-federation
- description: 'UTP registers DOIs with Crossref under its own prefix 10.61762 — 405 DOIs (113 current, 292 backfile) across "Platform: A Journal of Science and Technology" and "Platform: A Journal of Management and '
  name: Crossref membership (DOI prefix 10.61762)
  slug: crossref-membership
- description: The institution's Research Organization Registry record — the canonical machine-readable identity used by DOI metadata, funder systems and repository software to disambiguate UTP. The registry's own A
  name: ROR registration (048g2sh07)
  slug: ror
- description: 'UTP''s Digital Commons instance, holding the archive of "Platform: A Journal of Engineering (PAJE)" back to 2000. Serves OAI-PMH 2.0 at /do/oai/. Recorded as a tenancy: the repository and its metadata '
  name: 'Platform: A Journal of Engineering archive (bepress Digital Commons tenancy)'
  slug: journal-digital-commons
- description: 'UTP''s Moodle LMS. The Moodle web-service layer is enabled and answers with a structured invalidtoken exception, so it is real but token-gated. The instance acts as an LTI 1.3 platform and publishes a '
  name: uLearn learning management system (Moodle tenancy)
  slug: ulearn-moodle
- description: UTP's OpenLearning deployment, used for open and online course delivery alongside Moodle. No institution-published machine-readable descriptor was found on the host; the relationship is recorded so th
  name: uLearn+ (OpenLearning tenancy)
  slug: ulearnplus-openlearning
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://www.utp.edu.my/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universiti-teknologi-petronas/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Universiti-Teknologi-PETRONAS
- group: other
  title: ''
  type: ResearchRepository
  url: https://utpedia.utp.edu.my/
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholars.utp.edu.my/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.microsoftonline.com/utp.edu.my/federationmetadata/2007-06/federationmetadata.xml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/universiti-teknologi-petronas-utpedia-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/universiti-teknologi-petronas-scholars-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/universiti-teknologi-petronas-eprint-json-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/universiti-teknologi-petronas-examples.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/universiti-teknologi-petronas-education-standards-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/universiti-teknologi-petronas-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/universiti-teknologi-petronas-errors.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/universiti-teknologi-petronas-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/universiti-teknologi-petronas-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/universiti-teknologi-petronas-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/universiti-teknologi-petronas-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Teknologi PETRONAS (UTP) is a private research university in Seri Iskandar, Perak, Malaysia, established in 1997 and wholly owned by the national oil company PETRONAS. UTP publishes no developer portal, no API documentation and no OpenAPI of its own, and its main website — a SharePoint deployment — answers HTTP 200 to unknown /.well-known/ paths, so a presence check there proves nothing. What it does operate, verified by probe on 2026-09-01, is two self-hosted EPrints repositories on its own domain: UTPedia (utpedia.utp.edu.my, theses and final-year projects) and UTP Scholarly Publication (scholars.utp.edu.my, staff publications). Each serves an open OAI-PMH 2.0 endpoint, an unauthenticated EPrints REST dataset interface, an OpenSearch description document and RSS feeds; UTPedia additionally serves per-record JSON. The institution runs its own Microsoft Entra ID tenant for single sign-on, whose SAML 2.0 federation metadata and OIDC discovery document are public —
  it is not in eduGAIN or the Malaysian SIFULAN federation. UTP is a Crossref member (prefix 10.61762, 405 DOIs) and holds ROR 048g2sh07. Its learning platforms (Moodle via Pukunui at ulearn, OpenLearning at ulearnplus), its Digital Commons journal archive at journal.utp.edu.my and its MyJMS journals are vendor-operated tenancies recorded here as relationships, not as UTP engineering. No course catalog, timetable, open-data portal or research-computing API was found on any public host.'
finops:
- name: Universiti Teknologi Petronas Finops
  service_category: Education
  slug: universiti-teknologi-petronas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/universiti-teknologi-petronas.png
json_schemas:
- name: UTPedia EPrint record (JSON export)
  property_count: 24
  slug: universiti-teknologi-petronas-eprint-json
jsonld:
- class_count: 6
  name: Universiti Teknologi Petronas Context
  property_count: 2
  slug: universiti-teknologi-petronas-context
layout: provider
modified: '2026-09-01'
name: Universiti Teknologi PETRONAS
nav: Providers
network: true
overview: 'Universiti Teknologi PETRONAS publishes 2 APIs on the [APIs.io](https://apis.io/) network: UTPedia Institutional Repository and UTP Scholarly Publication Repository. Tagged areas include University, Higher Education, Education, Malaysia, and Private Research University.


  The Universiti Teknologi PETRONAS catalog on APIs.io includes 1 JSON-LD context.


  Universiti Teknologi PETRONAS''s developer surface includes code examples, authentication, and 16 more developer resources.'
plans:
- name: Universiti Teknologi Petronas Plans Pricing
  plan_count: 2
  slug: universiti-teknologi-petronas-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Universiti Teknologi Petronas Rate Limits
  slug: universiti-teknologi-petronas-rate-limits
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 50.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 25.6
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 22.0
  provenance:
    conformance: first-party
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
    score: 31.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/universiti-teknologi-petronas/refs/heads/main/screenshots/universiti-teknologi-petronas-2026-06-20T200138.png
security:
- kind: authentication
  name: Universiti Teknologi Petronas Authentication
  slug: universiti-teknologi-petronas-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Universiti Teknologi Petronas Domain Security
  slug: universiti-teknologi-petronas-domain-security
  summary_line: TLSv1.2 · DMARC
slug: universiti-teknologi-petronas
tags:
- University
- Higher Education
- Education
- Malaysia
- Private Research University
- Research
- Research Repository
- Institutional Repository
- Open Access
- OAI-PMH
- EPrints
- Identity Federation
- Learning Management
- Scholarly Publishing
website: https://www.utp.edu.my/
---
