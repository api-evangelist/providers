---
access_model:
  confidence: high
  label: Free · Anonymous metadata harvesting; everything else behind institutional SSO
  onboarding: unknown
  pricing: free
  public: false
  source:
  - authentication
  - identity-federation
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
    error_semantics: false
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
  score: 23.0
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://repository.uantwerpen.be/oai/abua/
  baseurl_source: declared
  description: 'Open Archives Initiative Protocol for Metadata Harvesting 2.0 interface for the Institutional Repository University of Antwerp (IRUA). Verified live on 2026-09-01: Identify returns repositoryName "Ins'
  name: IRUA OAI-PMH Metadata Interface
  slug: irua-oai-pmh
- description: The university's federated login, published as a SAML 2.0 EntityDescriptor at https://idpx.ua.ac.be/idp/shibboleth (HTTP 200, application/xml, 16,305 bytes). Declares four SingleSignOnService bindings
  name: University of Antwerp Identity Provider (Shibboleth / SAML 2.0)
  slug: idp
- description: The Belgian national research and education identity federation, operated by Belnet, in which the university's identity provider is registered. The registration is asserted inside the university's own
  name: Belnet R&E Federation membership
  slug: belnet-federation
- description: Wander is the integrated library, collection and research-information platform the University of Antwerp Library & Archive has built since 1998, when it was called Brocade and the department was calle
  name: Wander (formerly Brocade) — library platform built by UAntwerpen Library & Archive
  slug: brocade
- description: The university's learning management system, running as an Anthology-hosted tenant on the institution hostname blackboard.uantwerpen.be. Anthology's Blackboard Learn REST API answers there — /learn/ap
  name: Blackboard Learn (Anthology) — tenant
  slug: blackboard
- description: The university is one of the five Flemish university partners in the Vlaams Supercomputer Centrum and operates the CalcUA tier-2 cluster locally. The shared account and allocation portal at account.vs
  name: Flemish Supercomputer Centre (VSC) participation
  slug: vsc
- description: 'The university is Crossref member 29262 "University of Antwerp", holding DOI prefixes 10.52034 and 10.63028 with 565 registered DOIs (37 current, 528 backfile) as of the 2026 status check returned by '
  name: Crossref membership
  slug: crossref
- description: Research Organization Registry identifier https://ror.org/008x57b05, resolved live from https://api.ror.org/v2/organizations. Declares domain uantwerpen.be, established 2003, location Antwerp, Flander
  name: ROR registration
  slug: ror
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.uantwerpen.be/en/
- group: other
  title: ''
  type: IdentityFederation
  url: identity-federation/university-of-antwerp-identity-federation.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-antwerp-conformance.yml
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.uantwerpen.be/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://anet.uantwerpen.be/desktop/uantwerpen/opacuantwerpen/E
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.uantwerpen.be/en/study/programmes/
- group: other
  title: ''
  type: ResearchComputing
  url: https://www.uantwerpen.be/en/research-facilities/calcua/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.uantwerpen.be/en/research/policy/ethics-integrity/artificial-intelligence/
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-antwerp-authentication.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/anet-be
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/anet-be
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uantwerpen.be/en/about-uantwerp/organisation/information-security-and-privacy/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uantwerpen.be/en/about-uantwerp/organisation/information-security-and-privacy/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://www.uantwerpen.be/en/about-uantwerp/news/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-antwerp/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/uantwerpen
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/UAntwerpen
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-antwerp-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-antwerp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-antwerp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-antwerp-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Antwerp (Universiteit Antwerpen) is a public research university in Antwerp, Belgium. Unusually for this cohort it is a producer as well as a buyer: the library and archive department builds Wander — the platform that began in 1998 as Brocade — and hosts it on the university''s own infrastructure, so a vendor-looking domain (go.wander.be) resolves to 143.169.239.17 inside inetnum 143.169.0.0/16, netname UA, org "Universiteit Antwerpen" (RIPE). Other Flemish institutions are its tenants, not the other way round. Two institution-operated machine-readable surfaces were verified live in September 2026, both in that same address space. The Institutional Repository University of Antwerp (IRUA) serves a complete OAI-PMH 2.0 interface at repository.uantwerpen.be with six metadata formats (including CERIF 1.5, MARC 21 and Flemish VABB-SHW and FWO MODS profiles), four harvesting sets, ORCID iDs usable as set specifications, and deletedRecord=persistent. The Shibboleth
  identity provider publishes a signed SAML 2.0 EntityDescriptor at the legacy entityID https://idpx.ua.ac.be/idp/shibboleth, registered in the Belnet R&E Federation since 2012 and interfederated into eduGAIN; it is the strongest contract in this profile, it is institution-run on institution hardware, and the June 2026 pass missed it entirely. What the university does NOT operate is equally clear and is stated rather than padded: there is no developer portal, no API key programme, no open data portal (data.uantwerpen.be and api.uantwerpen.be do not resolve), no OpenAPI or AsyncAPI of its own, and no machine-readable course catalog — the programme catalog is HTML only. The learning management system is Anthology''s Blackboard running as a tenant on blackboard.uantwerpen.be, whose REST API answers on the university''s hostname but is Anthology''s contract, not the university''s. DOIs are registered through Crossref (member 29262); there is no DataCite membership.'
finops:
- name: University Of Antwerp Finops
  service_category: Education
  slug: university-of-antwerp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-antwerp.png
jsonld:
- class_count: 21
  name: University Of Antwerp Context
  property_count: 10
  slug: university-of-antwerp-context
layout: provider
modified: '2026-09-01'
name: University of Antwerp
nav: Providers
network: true
overview: 'University of Antwerp publishes 1 API on the [APIs.io](https://apis.io/) network: IRUA OAI-PMH Metadata Interface. Tagged areas include Education, Higher Education, University, Belgium, and Europe.


  The University of Antwerp catalog on APIs.io includes 1 JSON-LD context.


  University of Antwerp''s developer surface includes authentication, GitHub presence, engineering blog, YouTube channel, and 18 more developer resources.'
plans:
- name: University Of Antwerp Plans Pricing
  plan_count: 2
  slug: university-of-antwerp-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: University Of Antwerp Rate Limits
  slug: university-of-antwerp-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.2
    contract_quality: 24.1
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 15.2
    operational_transparency: 26.3
  previous_composite: 34.8
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
    score: 46.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-antwerp/refs/heads/main/screenshots/university-of-antwerp-2026-06-20T200126.png
security:
- kind: authentication
  name: University Of Antwerp Authentication
  slug: university-of-antwerp-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: University Of Antwerp Domain Security
  slug: university-of-antwerp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: university-of-antwerp
tags:
- Education
- Higher Education
- University
- Belgium
- Europe
- Flanders
- Institutional Repository
- OAI-PMH
- Identity Federation
- Library
- Research Repository
- Research Computing
- Learning Management
website: https://www.uantwerpen.be/en/
---
