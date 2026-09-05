---
access_model:
  confidence: high
  label: Free and anonymous for repository read surfaces; every other surface requires an AUB account
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
  scored_at: '2026-09-04'
api_count: 11
apis:
- description: Anonymous HAL/JSON REST API for AUB ScholarWorks, AUB's institutional repository, running DSpace 9.1 on AUB's own host. The service root self-describes as dspaceName "AUB ScholarWorks", dspaceServer h
  name: AUB ScholarWorks DSpace REST API
  slug: scholarworks-rest
- description: OAI-PMH 2.0 metadata harvesting endpoint for AUB ScholarWorks. Identify returns repositoryName "AUB ScholarWorks", repositoryIdentifier scholarworks.aub.edu.lb, adminEmail scholarworks@aub.edu.lb, ear
  name: AUB ScholarWorks OAI-PMH
  slug: scholarworks-oai
- description: AUB's own Shibboleth SAML 2.0 identity provider, the front door to campus single sign-on. The metadata endpoint serves a signed EntityDescriptor with entityID https://idp.aub.edu.lb/idp/shibboleth, sh
  name: AUB Shibboleth Identity Provider (SAML 2.0)
  slug: shibboleth-idp
- description: AUB's identity provider is registered in InCommon, the United States research and education identity federation, and is resolvable through the InCommon per-entity metadata (MDQ) service. Probed 2026-0
  name: InCommon federation registration (AUB IdP)
  slug: incommon-federation
- description: AUB's learning management system is a Moodle instance the university hosts itself at lms.aub.edu.lb (moodle.aub.edu.lb is a CNAME to it), fronted by an AWS load balancer in the AUB account. The Moodle
  name: AUB Moodle Web Services (REST)
  slug: moodle-webservices
- description: AUB's Moodle is configured as an IMS Global LTI 1.3 / LTI Advantage platform, and two of its platform endpoints are publicly reachable without credentials. The public JWKS at /mod/lti/certs.php return
  name: AUB Moodle LTI 1.3 platform endpoints
  slug: moodle-lti-platform
- description: AUB is a Crossref member in its own right — member id 13566, primary name "American University of Beirut", DOI prefix 10.63014. Probed against the Crossref REST API on 2026-09-01, the membership is re
  name: Crossref membership (AUB)
  slug: crossref-member
- description: AUB holds Handle System prefix 10938, the persistent identifier namespace behind every AUB ScholarWorks record — the repository's OAI sample identifier is oai:scholarworks.aub.edu.lb:10938/1234. Verif
  name: Handle System prefix 10938 (AUB ScholarWorks)
  slug: handle-prefix
- description: The American University of Beirut is registered in the Research Organization Registry as https://ror.org/04pznsd21. Three related AUB entities carry their own ROR identifiers — AUB Medical Center (00w
  name: ROR registration (AUB)
  slug: ror-record
- description: 'AUB''s library discovery and library services platform are Ex Libris products under AUB-specific tenancies: aub.primo.exlibrisgroup.com and aub.alma.exlibrisgroup.com both CNAME into Ex Libris''s eu06 r'
  name: AUB Libraries discovery and management (Ex Libris Primo / Alma)
  slug: library-discovery
- description: AUB Libraries runs a Springshare LibGuides estate at aub.edu.lb.libguides.com under site_id 4901 — the guides are AUB-authored (the ScholarWorks guide, an Artificial Intelligence guide, the A-Z databa
  name: AUB Libraries LibGuides (Springshare)
  slug: libguides
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.aub.edu.lb/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aub.edu.lb/Pages/privacy.aspx
- group: operate
  title: ''
  type: Support
  url: https://servicedesk.aub.edu.lb/TDClient/1398/Portal/Home/
- group: docs
  title: ''
  type: Documentation
  url: https://aub.edu.lb.libguides.com/AUB-Scholarworks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AUB-CMPS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/american-university-of-beirut
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholarworks.aub.edu.lb/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://aub.primo.exlibrisgroup.com/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.aub.edu.lb/idp/shibboleth
- group: auth
  title: ''
  type: Authentication
  url: authentication/aub-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aub-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aub-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/aub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aub-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: The American University of Beirut is a private, non-profit research university in Beirut, Lebanon, chartered in New York State and founded in 1866. AUB publishes no developer portal, no API gateway and no institution-authored API contract of any kind — every machine-readable surface it operates is a standards-based deployment of third-party software running on AUB's own hosts, and that distinction is the whole of this profile. Four such surfaces were verified live on 2026-09-01. AUB ScholarWorks (scholarworks.aub.edu.lb) is an AUB-hosted DSpace 9.1 institutional repository holding 24,318 items across 25 communities, serving an anonymous HAL/JSON REST API and an OAI-PMH 2.0 endpoint with thirteen metadata formats. AUB runs its own Shibboleth SAML 2.0 identity provider at idp.aub.edu.lb, scoped aub.edu.lb, and — the strongest institution-operated surface it has — that IdP is registered in InCommon and resolvable through the InCommon MDQ service with the REFEDS Sirtfi entity category
  asserted. AUB's learning management system is an AUB-hosted Moodle at lms.aub.edu.lb whose Web Services REST endpoint answers anonymously with a structured invalidtoken error and whose LTI 1.3 platform JWKS and token endpoints are publicly reachable. AUB is a Crossref member (id 13566, prefix 10.63014), holds Handle prefix 10938 and is registered in ROR as 04pznsd21. Its library discovery and management stack (Ex Libris Primo and Alma), its LibGuides estate (Springshare, site 4901) and its Ellucian Banner student information system are vendor tenancies recorded here as relationships, with no vendor contract saved under AUB's name.
finops:
- name: Aub Finops
  service_category: Education
  slug: aub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aub.png
jsonld:
- class_count: 11
  name: Aub Context
  property_count: 5
  slug: aub-context
layout: provider
modified: '2026-09-01'
name: American University of Beirut
nav: Providers
network: true
overview: 'American University of Beirut publishes 11 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Lebanon, and Middle East.


  The American University of Beirut catalog on APIs.io includes 1 JSON-LD context.


  American University of Beirut''s developer surface includes support, documentation, authentication, and 13 more developer resources.'
plans:
- name: Aub Plans Pricing
  plan_count: 2
  slug: aub-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: Aub Rate Limits
  slug: aub-rate-limits
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 26.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 28.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aub/refs/heads/main/screenshots/aub-2026-06-20T172544.png
security:
- kind: authentication
  name: Aub Authentication
  slug: aub-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aub Domain Security
  slug: aub-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: aub
tags:
- University
- Higher Education
- Education
- Lebanon
- Middle East
- Private Research University
- Research
- Research Data
- Open Access
- Libraries
- Institutional Repository
- Identity Federation
- Learning Management
website: https://www.aub.edu.lb/
---
