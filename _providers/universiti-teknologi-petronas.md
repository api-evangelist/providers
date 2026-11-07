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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-11-06'
api_count: 2
apis:
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
- baseURL: https://utpedia.utp.edu.my
  baseurl_source: declared
  description: The Discovery API from Universiti Teknologi PETRONAS — 4 operation(s) for discovery.
  name: Universiti Teknologi PETRONAS Discovery API
  slug: universiti-teknologi-petronas-discovery-api
- baseURL: https://utpedia.utp.edu.my
  baseurl_source: declared
  description: The EPrints REST API from Universiti Teknologi PETRONAS — 4 operation(s) for eprints rest.
  name: Universiti Teknologi PETRONAS EPrints REST API
  slug: universiti-teknologi-petronas-eprints-rest-api
- baseURL: https://utpedia.utp.edu.my
  baseurl_source: declared
  description: Per-record export in a named format.
  name: Universiti Teknologi PETRONAS Export API
  slug: universiti-teknologi-petronas-export-api
- baseURL: https://utpedia.utp.edu.my
  baseurl_source: declared
  description: The OAI-PMH API from Universiti Teknologi PETRONAS — 1 operation(s) for oai-pmh.
  name: Universiti Teknologi PETRONAS OAI PMH API
  slug: universiti-teknologi-petronas-oai-pmh-api
artifact_total: 18
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
  href: https://artifacts.apis.io/universiti-teknologi-petronas/openapi/_original/universiti-teknologi-petronas-utpedia-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/universiti-teknologi-petronas-utpedia-openapi.yml
- group: docs
  href: https://artifacts.apis.io/universiti-teknologi-petronas/openapi/_original/universiti-teknologi-petronas-scholars-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/universiti-teknologi-petronas-scholars-openapi.yml
- group: docs
  href: https://artifacts.apis.io/universiti-teknologi-petronas/json-schema/universiti-teknologi-petronas-eprint-json-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/universiti-teknologi-petronas-eprint-json-schema.json
- group: build
  href: https://artifacts.apis.io/universiti-teknologi-petronas/examples/universiti-teknologi-petronas-examples.yml
  title: ''
  type: Examples
  url: examples/universiti-teknologi-petronas-examples.yml
- group: design
  href: https://artifacts.apis.io/universiti-teknologi-petronas/conformance/universiti-teknologi-petronas-education-standards-conformance.yml
  title: ''
  type: Conformance
  url: conformance/universiti-teknologi-petronas-education-standards-conformance.yml
- group: auth
  href: https://artifacts.apis.io/universiti-teknologi-petronas/authentication/universiti-teknologi-petronas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/universiti-teknologi-petronas-authentication.yml
- group: design
  href: https://artifacts.apis.io/universiti-teknologi-petronas/errors/universiti-teknologi-petronas-errors.yml
  title: ''
  type: ErrorCatalog
  url: errors/universiti-teknologi-petronas-errors.yml
- group: auth
  href: https://artifacts.apis.io/universiti-teknologi-petronas/security/universiti-teknologi-petronas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/universiti-teknologi-petronas-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/universiti-teknologi-petronas/plans/universiti-teknologi-petronas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/universiti-teknologi-petronas-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/universiti-teknologi-petronas/rate-limits/universiti-teknologi-petronas-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/universiti-teknologi-petronas-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/universiti-teknologi-petronas/finops/universiti-teknologi-petronas-finops.yml
  title: ''
  type: FinOps
  url: finops/universiti-teknologi-petronas-finops.yml
- group: other
  href: https://artifacts.apis.io/universiti-teknologi-petronas/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Universiti Teknologi PETRONAS (UTP) is a private research university in Seri Iskandar, Perak, Malaysia, established in 1997 and wholly owned by the national oil company PETRONAS. UTP publishes no developer portal, no API documentation and no OpenAPI of its own, and its main website — a SharePoint deployment — answers HTTP 200 to unknown /.well-known/ paths, so a presence check there proves nothing. What it does operate, verified by probe on 2026-09-01, is two self-hosted EPrints repositories on its own domain: UTPedia (utpedia.utp.edu.my, theses and final-year projects) and UTP Scholarly Publication (scholars.utp.edu.my, staff publications). Each serves an open OAI-PMH 2.0 endpoint, an unauthenticated EPrints REST dataset interface, an OpenSearch description document and RSS feeds; UTPedia additionally serves per-record JSON. The institution runs its own Microsoft Entra ID tenant for single sign-on, whose SAML 2.0 federation metadata and OIDC discovery document are public —
  it is not in eduGAIN or the Malaysian SIFULAN federation. UTP is a Crossref member (prefix 10.61762, 405 DOIs) and holds ROR 048g2sh07. Its learning platforms (Moodle via Pukunui at ulearn, OpenLearning at ulearnplus), its Digital Commons journal archive at journal.utp.edu.my and its MyJMS journals are vendor-operated tenancies recorded here as relationships, not as UTP engineering. No course catalog, timetable, open-data portal or research-computing API was found on any public host.'
finops:
- has_sources: true
  method: generated
  name: Universiti Teknologi Petronas Finops
  primary_unit: ''
  service_category: Education
  slug: universiti-teknologi-petronas-finops
  template: false
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
modified: '2026-09-16'
name: Universiti Teknologi PETRONAS
nav: Providers
network: true
overview: 'Universiti Teknologi PETRONAS publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, EPrints REST API, Export API, and 7 more. Tagged areas include University, Higher Education, Education, Malaysia, and Private Research University.


  The Universiti Teknologi PETRONAS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


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
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Universiti Teknologi PETRONAS API Rules
  rule_count: 48
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 1
  slug: universiti-teknologi-petronas-rules
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.0
    catalog_earned_first_party: 0.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 22.8
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - malaysia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 19.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/universiti-teknologi-petronas/universiti-teknologi-petronas-2026-06-20T200138.png
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
- LMS
- Scholarly Publishing
website: https://www.utp.edu.my/
---
