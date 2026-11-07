---
access_model:
  confidence: high
  label: No public developer programme · open protocol endpoints, otherwise affiliation-gated
  onboarding: unknown
  pricing: free
  public: false
  source:
  - probed
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'OAI-PMH 2.0 metadata harvesting interface for Research Commons, the university''s open-access institutional repository, on the institution''s own host. Verified live 2026-09-01: verb=Identify returns pr'
  name: Research Commons OAI-PMH
  slug: research-commons-oai
- description: DSpace 7.6.5 REST API backing Research Commons, giving programmatic access to communities, collections, items, bitstreams and discovery search over the university's theses and research outputs. Verifi
  name: Research Commons DSpace REST API
  slug: research-commons-rest
- description: 'eLearn, the university''s Moodle learning management system on its own registrable domain, acts as an LTI 1.3 platform. Verified live 2026-09-01: /mod/lti/certs.php returns HTTP 200 with a JSON Web Key'
  name: eLearn LTI 1.3 Platform (Moodle)
  slug: elearn-lti
- description: A One-Time Secret service run by University of Waikato IT Services on its own host, for sharing a secret that can be retrieved exactly once. The published API page enumerates a complete endpoint set o
  name: One-Time Secret (OTS) API
  slug: ots
- description: JSON REST API for the User-friendly Deep Learning framework built by the University of Waikato's Faculty of Computing and Mathematical Sciences to make deep learning accessible to domain experts. Docu
  name: User-friendly Deep Learning (UFDL) API
  slug: ufdl
- description: The University of Waikato's Shibboleth Identity Provider, entityID https://idp.waikato.ac.nz/idp/shibboleth, registered in the signed Tuakiri (New Zealand Access Federation) metadata aggregate since 2
  name: Waikato SAML 2.0 Identity Provider in Tuakiri
  slug: tuakiri-idp
- description: 'The university''s Microsoft Entra ID tenant, 220f5dc3-9452-48e5-9b4f-888df42f7a2d, is the identity source behind both the uowidp OpenID Connect provider and the eLearn Moodle SAML login. Verified live '
  name: University of Waikato Microsoft Entra ID Tenant
  slug: entra-tenant
- description: The University of Waikato is a Crossref member — member id 6347, primary name "University of Waikato", DOI prefix 10.15663. Verified 2026-09-01 against api.crossref.org/members. This is a membership t
  name: Crossref Membership (member 6347)
  slug: crossref-member
- description: The University of Waikato is registered in the Research Organization Registry as https://ror.org/013fsnh78, with names "University of Waikato" and "Te Whare Wananga o Waikato" and website https://www.
  name: ROR Registration (ror.org/013fsnh78)
  slug: ror
- description: 'profiles.waikato.ac.nz is the university''s researcher-profile and research-information service, and it is a tenancy: the host CNAMEs to waikato.discovery.symplectic.org, on Digital Science''s Symplecti'
  name: Waikato Research Profiles on Symplectic Discovery (tenant)
  slug: symplectic-discovery
- description: The University of Waikato Library's discovery layer is a named tenancy on Ex Libris's shared Primo VE platform — waikato.primo.exlibrisgroup.com with view code vid=64WAIKATO_INST:64WAIKATO, verified l
  name: Waikato Library Discovery on Ex Libris Primo VE (tenant)
  slug: primo-discovery
- description: waikato.figshare.com resolves (CNAME to figshare.com) and answers HTTP 202 with an empty body — a bot-management challenge, so the tenancy is live but not readable by us. This is the institution's Fig
  name: Waikato Figshare Research Data Repository (tenant)
  slug: figshare-tenant
- description: libraryguides.waikato.ac.nz, which hosts the library's subject guides including its "Using Generative AI in Academic Study" guide, CNAMEs to region-au.libguides.com — a tenancy on Springshare's LibGui
  name: Waikato Library Guides on Springshare LibGuides (tenant)
  slug: libguides
- baseURL: https://api.svc.waikato.ac.nz/uowidp/v1
  baseurl_source: declared
  description: Authorization Code and hybrid flows against the university identity provider.
  name: University of Waikato Authentication API
  slug: university-of-waikato-authentication-api
- baseURL: https://api.svc.waikato.ac.nz/uowidp/v1
  baseurl_source: declared
  description: OpenID Provider metadata and signing keys.
  name: University of Waikato Discovery API
  slug: university-of-waikato-discovery-api
- baseURL: https://api.svc.waikato.ac.nz/uowidp/v1
  baseurl_source: declared
  description: Front-channel session termination.
  name: University of Waikato Session API
  slug: university-of-waikato-session-api
artifact_total: 28
common:
- group: company
  title: ''
  type: Website
  url: https://www.waikato.ac.nz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Waikato
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Waikato
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Waikato/waikato-repositories
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Waikato/waikato-repositories/issues
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/universityofwaikato/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/waikato
- group: operate
  title: ''
  type: Support
  url: https://www.waikato.ac.nz/students/it-services/
- group: company
  title: ''
  type: Blog
  url: https://www.waikato.ac.nz/news-events/news/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.waikato.ac.nz/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.waikato.ac.nz/copyright-and-disclaimer/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://timetable.waikato.ac.nz/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://waikato.primo.exlibrisgroup.com/discovery/search?vid=64WAIKATO_INST:64WAIKATO
- group: other
  title: ''
  type: ResearchRepository
  url: https://researchcommons.waikato.ac.nz/
- group: other
  title: ''
  type: IdentityFederation
  url: https://directory.tuakiri.ac.nz/metadata/tuakiri-metadata-signed.xml
- group: other
  title: ''
  type: AIPolicy
  url: https://www.waikato.ac.nz/students/student-assessment-handbook/gen-ai/
- group: build
  title: ''
  type: AITooling
  url: https://libraryguides.waikato.ac.nz/genaiguide
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.waikato.ac.nz/llms.txt
- group: design
  href: https://artifacts.apis.io/university-of-waikato/conformance/university-of-waikato-conformance.yml
  title: ''
  type: x-conformance
  url: conformance/university-of-waikato-conformance.yml
- group: auth
  href: https://artifacts.apis.io/university-of-waikato/authentication/university-of-waikato-authentication.yml
  title: ''
  type: Authentication
  url: authentication/university-of-waikato-authentication.yml
- group: auth
  href: https://artifacts.apis.io/university-of-waikato/scopes/university-of-waikato-scopes.yml
  title: ''
  type: Scopes
  url: scopes/university-of-waikato-scopes.yml
- group: design
  href: https://artifacts.apis.io/university-of-waikato/errors/university-of-waikato-errors.yml
  title: ''
  type: Errors
  url: errors/university-of-waikato-errors.yml
- group: design
  href: https://artifacts.apis.io/university-of-waikato/vocabulary/university-of-waikato-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-waikato-vocabulary.yml
- group: auth
  href: https://artifacts.apis.io/university-of-waikato/security/university-of-waikato-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/university-of-waikato-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-waikato/plans/university-of-waikato-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/university-of-waikato-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/university-of-waikato/rate-limits/university-of-waikato-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/university-of-waikato-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/university-of-waikato/finops/university-of-waikato-finops.yml
  title: ''
  type: FinOps
  url: finops/university-of-waikato-finops.yml
- group: other
  href: https://artifacts.apis.io/university-of-waikato/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Waikato (Te Whare Wananga o Waikato) is a public research university in Hamilton and Tauranga, Aotearoa New Zealand, founded in 1964. It runs no developer programme, no developer portal and no self-serve public API, and this profile says so plainly. What it does operate itself is narrow but real and unusually well evidenced for this cohort: an OpenID Connect provider of its own on api.svc.waikato.ac.nz/uowidp/v1, publishing a live discovery document and JWKS and used by the university''s own Blazor timetable and its MyWaikato student portal; Research Commons, a DSpace 7.6.5 institutional repository on its own host serving a DSpace REST API and an OAI-PMH 2.0 interface with twelve metadata formats back to 1972; a One-Time Secret API run by IT Services with documented endpoints under HTTP Basic against a Stella account; a Moodle LMS acting as an LTI 1.3 platform with live platform keys; and the UFDL deep-learning framework API from the Computing and Mathematical
  Sciences faculty, alongside four active GitHub organisations (Waikato, waikato-ufdl, waikato-datamining, waikato-llm) that include WEKA. Its identity is federated twice over — a Shibboleth IdP entity registered in Tuakiri since 2012 with REFEDS Research & Scholarship and Sirtfi, exported to eduGAIN, and a Microsoft Entra ID tenant that is the live SAML issuer for eLearn. The university also publishes an llms.txt with explicit attribution and generative-model usage terms, which almost no institution in this cohort does. Everything else that looks like a Waikato API is a tenancy on somebody else''s platform — Symplectic Discovery behind profiles.waikato.ac.nz, Ex Libris Primo VE, Springshare LibGuides behind libraryguides.waikato.ac.nz, and waikato.figshare.com — and is recorded here as a relationship, never as a University of Waikato contract.'
examples:
- key_count: 5
  name: University Of Waikato Protocol Endpoints Example
  slug: university-of-waikato-protocol-endpoints-example
- key_count: 3
  name: University Of Waikato Uowidp Discovery Example
  slug: university-of-waikato-uowidp-discovery-example
finops:
- has_sources: true
  method: generated
  name: University Of Waikato Finops
  primary_unit: ''
  service_category: Education
  slug: university-of-waikato-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-waikato.png
json_schemas:
- name: University of Waikato uowidp JSON Web Key Set
  property_count: 1
  slug: university-of-waikato-uowidp-jwks
- name: University of Waikato uowidp OpenID Provider Metadata
  property_count: 15
  slug: university-of-waikato-uowidp-provider-metadata
jsonld:
- class_count: 18
  name: University Of Waikato Context
  property_count: 4
  slug: university-of-waikato-context
layout: provider
modified: '2026-09-01'
name: University of Waikato
nav: Providers
network: true
overview: 'University of Waikato publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Discovery API, Session API, and 13 more. Tagged areas include Education, Higher Education, University, New Zealand, and Research.


  The University of Waikato catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  University of Waikato''s developer surface includes GitHub presence, support, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: University Of Waikato Plans Pricing
  plan_count: 2
  slug: university-of-waikato-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: University Of Waikato Rate Limits
  slug: university-of-waikato-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: University of Waikato API Rules
  rule_count: 66
  severity_counts:
    error: 60
    hint: 0
    info: 5
    warn: 1
  slug: university-of-waikato-rules
scopes:
- name: University Of Waikato Scopes
  scope_count: 3
  slug: university-of-waikato-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 51.3
    catalog_earned_first_party: 0.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 26.3
    contract_governance: 17.4
    contract_quality: 24.1
    developer_ergonomics: 28.6
    discoverability: 64.3
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - new-zealand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 26.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/university-of-waikato/university-of-waikato-2026-06-20T200327.png
security:
- kind: authentication
  name: University Of Waikato Authentication
  slug: university-of-waikato-authentication
  summary_line: openIdConnect/http/saml2 · 6 schemes
- kind: domain-security
  name: University Of Waikato Domain Security
  slug: university-of-waikato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-waikato
tags:
- Education
- Higher Education
- University
- New Zealand
- Research
- Research Repository
- Open Access
- OAI-PMH
- Identity Federation
- SAML
- LMS
- Machine Learning
website: https://www.waikato.ac.nz/
---
