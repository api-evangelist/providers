---
access_model:
  confidence: high
  label: Free · public read endpoints, no signup
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
    auth_clarity: false
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
  score: 2.5
  scored_at: '2026-09-01'
api_count: 11
apis:
- description: The institution's research open-data repository, run by the Institute for the Future of Education on the institution's own host (datahub.tec.mx, an Azure deployment whose internal name prod031azms01.i
  name: Datahub Tec de Monterrey — Dataverse Research Data Repository API
  slug: datahub-dataverse
- description: OAI-PMH 2.0 harvesting endpoint for the Tecnológico de Monterrey Dataverse OAI Archive, re-verified live on 2026-09-01. The Identify verb returns repositoryName "Tecnológico de Monterrey Dataverse OAI
  name: Datahub Tec de Monterrey — OAI-PMH Metadata Harvesting Endpoint
  slug: datahub-oai
- description: RITEC (repositorio.tec.mx) is the institution's DSpace 8.0 institutional repository, holding 86,310 discoverable objects across theses, articles and academic works. Its HAL+JSON REST API is public and
  name: RITEC Institutional Repository — DSpace REST API
  slug: ritec-dspace-rest
- description: OAI-PMH 2.0 endpoint for RITEC, verified live on 2026-09-01. Identify returns repositoryName "Repositorio Institucional del Tecnológico de Monterrey", repositoryIdentifier repositorio.tec.mx and an ea
  name: RITEC Institutional Repository — OAI-PMH Endpoint
  slug: ritec-oai
- description: The institution's own SAML 2.0 / WS-Federation / OpenID Connect identity provider, on its own registrable domain itesm.mx. Signed SAML metadata is served at the standard AD FS path with Content-Type a
  name: Tec de Monterrey AD FS Identity Provider (fs.itesm.mx)
  slug: adfs-identity-provider
- description: A second institution-operated SAML 2.0 identity provider, a NetIQ/Micro Focus Access Manager deployment on tec.mx. It publishes signed SAML 2.0 metadata (entityID https://amfs.tec.mx/nidp/saml2/metada
  name: Tec de Monterrey Access Manager Identity Provider (amfs.tec.mx)
  slug: amfs-identity-provider
- description: 'A Shibboleth Service Provider operated in front of RITEC on the institution''s own host. The DSpace REST API advertises it explicitly in a WWW-Authenticate header (shibboleth realm="DSpace REST API"), '
  name: RITEC Shibboleth Service Provider
  slug: ritec-shibboleth-sp
- description: 'The institution''s Microsoft Entra ID tenant, c65a3ea6-0f7c-400b-8934-5a6dc1705645, covering both tec.mx and itesm.mx, with signed SAML 2.0 federation metadata and an OpenID Connect discovery document '
  name: Microsoft Entra ID Tenant Federation Metadata (tec.mx / itesm.mx)
  slug: entra-tenant-federation
- description: Tecnológico de Monterrey is a DataCite consortium organization, symbol ITESM, active, region AMER, country MX, linked to ROR 03ayjn504, holding DOI prefix 10.57687 and operating three registered repos
  name: DataCite Membership — ITESM
  slug: datacite-membership
- description: Registered Crossref member 25649, "Instituto Tecnologico y de Estudios Superiores de Monterrey", Monterrey, Nuevo Leon, Mexico, holding DOI prefix 10.46530 with 430 deposited DOIs (176 current, 254 ba
  name: Crossref Membership — member 25649
  slug: crossref-membership
- description: Research Organization Registry identifier https://ror.org/03ayjn504, established 1943, domain tec.mx, located in Monterrey, Nuevo León, Mexico, cross-referenced to GRID grid.419886.a, ISNI 0000 0001 2
  name: ROR Registration — 03ayjn504
  slug: ror-registration
artifact_total: 21
common:
- group: company
  title: ''
  type: Website
  url: https://tec.mx/en
- group: other
  title: ''
  type: OpenData
  url: https://datahub.tec.mx/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repositorio.tec.mx/
- group: other
  title: ''
  type: IdentityFederation
  url: https://fs.itesm.mx/FederationMetadata/2007-06/FederationMetadata.xml
- group: other
  title: ''
  type: AIPolicy
  url: https://tec.mx/en/academic-integrity/artificial-intelligence
- group: other
  title: ''
  type: AIPolicy
  url: https://tec.mx/sites/default/files/repositorio/integridad-academica/lineamientos-ia-profesores-tec-de-monterrey.pdf
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tecnologico-de-monterrey-oficial
- group: company
  title: ''
  type: Blog
  url: https://conecta.tec.mx/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tec.mx/en/privacy-notices
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tec.mx/es/terminos-y-condiciones
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tecdemonterrey/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/tecdemonterrey
- group: design
  title: ''
  type: Conformance
  url: conformance/tecnologico-de-monterrey-conformance.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tecnologico-de-monterrey-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tecnologico-de-monterrey-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tecnologico-de-monterrey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tecnologico-de-monterrey-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tecnologico-de-monterrey-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Tecnológico de Monterrey (ITESM) is a private Mexican multi-campus university system headquartered in Monterrey, Nuevo León, ranked #185 in the QS World University Rankings 2025. Its programmable footprint is real but narrow, and it is entirely infrastructure the institution runs rather than software it wrote. Two research surfaces are live and public: a Dataverse 5.9 research data repository at datahub.tec.mx and a DSpace 8 institutional repository (RITEC) at repositorio.tec.mx holding 86,310 works, each with a working OAI-PMH 2.0 endpoint. Its strongest institution-operated machine-readable surface is identity: two SAML 2.0 identity providers on its own domains (fs.itesm.mx AD FS, amfs.tec.mx NetIQ Access Manager) plus a Shibboleth Service Provider in front of RITEC. It is a registered DataCite consortium organization (ITESM, prefix 10.57687, three repositories), a Crossref member (25649, prefix 10.46530) and is registered in ROR as 03ayjn504. What it does NOT have is a working
  public API programme: the gated institutional API developer portal formerly at api.tec.mx no longer resolves in DNS, and no OpenAPI in this profile is authored by the institution — the repository contracts are generated by the Dataverse and DSpace software and are recorded here as deployments, not as the institution''s engineering.'
examples:
- key_count: 2
  name: Tecnologico De Monterrey Search Example
  slug: tecnologico-de-monterrey-search-example
- key_count: 2
  name: Tecnologico De Monterrey Version Example
  slug: tecnologico-de-monterrey-version-example
finops:
- name: Tecnologico De Monterrey Finops
  service_category: Education
  slug: tecnologico-de-monterrey-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tecnologico-de-monterrey.png
json_schemas:
- name: SearchResult
  property_count: 2
  slug: tecnologico-de-monterrey-searchresult
json_structures:
- name: Tecnologico De Monterrey Searchitem Structure
  property_count: 10
  slug: tecnologico-de-monterrey-searchitem-structure
jsonld:
- class_count: 14
  name: Tecnologico De Monterrey Context
  property_count: 1
  slug: tecnologico-de-monterrey-context
layout: provider
modified: '2026-09-01'
name: Tecnológico de Monterrey
nav: Providers
network: true
overview: 'Tecnológico de Monterrey publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Mexico, and Private Research University.


  The Tecnológico de Monterrey catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tecnológico de Monterrey''s developer surface includes engineering blog and 18 more developer resources.'
plans:
- name: Tecnologico De Monterrey Plans Pricing
  plan_count: 2
  slug: tecnologico-de-monterrey-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Tecnologico De Monterrey Rate Limits
  slug: tecnologico-de-monterrey-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tecnológico de Monterrey API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tecnologico-de-monterrey-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 38.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 26.8
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 32.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 35.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tecnologico-de-monterrey/refs/heads/main/screenshots/tecnologico-de-monterrey-2026-06-20T195020.png
security:
- kind: domain-security
  name: Tecnologico De Monterrey Domain Security
  slug: tecnologico-de-monterrey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tecnologico-de-monterrey
tags:
- University
- Higher Education
- Education
- Mexico
- Private Research University
- Research Data
- Open Data
- Research Repository
- Institutional Repository
- Identity Federation
- OAI-PMH
- Dataverse
- DSpace
- SAML
- Shibboleth
- DataCite
- Crossref
website: https://tec.mx/en
---
