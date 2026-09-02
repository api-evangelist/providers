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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The university''s own OpenID Connect 1.0 provider, on its own API gateway at api.svc.waikato.ac.nz/uowidp/v1. Verified live 2026-09-01: the discovery document returns HTTP 200 declaring issuer https://'
  name: University of Waikato Identity Provider (uowidp)
  slug: uowidp
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
artifact_total: 25
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
  title: ''
  type: x-conformance
  url: conformance/university-of-waikato-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-waikato-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/university-of-waikato-scopes.yml
- group: design
  title: ''
  type: Errors
  url: errors/university-of-waikato-errors.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/university-of-waikato-vocabulary.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-waikato-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-waikato-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-waikato-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-waikato-finops.yml
- group: other
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
- name: University Of Waikato Finops
  service_category: Education
  slug: university-of-waikato-finops
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
overview: 'University of Waikato publishes 1 API on the [APIs.io](https://apis.io/) network: Identity Provider (uowidp). Tagged areas include Education, Higher Education, University, New Zealand, and Research.


  The University of Waikato catalog on APIs.io includes 1 JSON-LD context.


  University of Waikato''s developer surface includes GitHub presence, support, engineering blog, authentication, and 24 more developer resources.'
plans:
- name: University Of Waikato Plans Pricing
  plan_count: 2
  slug: university-of-waikato-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: University Of Waikato Rate Limits
  slug: university-of-waikato-rate-limits
scopes:
- name: University Of Waikato Scopes
  scope_count: 3
  slug: university-of-waikato-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 48.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 14.3
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 3.8
    contract_quality: 27.0
    developer_ergonomics: 28.6
    discoverability: 66.7
    governance: 3.8
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 0.0
  previous_composite: 21.0
  provenance:
    conformance: first-party
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
    score: 64.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-waikato/refs/heads/main/screenshots/university-of-waikato-2026-06-20T200327.png
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
- OpenID Connect
- Learning Management
- Machine Learning
website: https://www.waikato.ac.nz/
---
