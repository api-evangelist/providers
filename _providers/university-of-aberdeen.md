---
access_model:
  confidence: high
  label: Free · No registration (public metadata surfaces)
  onboarding: unknown
  pricing: free
  public: true
  source:
  - probe
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
  scored_at: '2026-09-03'
api_count: 10
apis:
- description: The University's own Shibboleth Identity Provider, entityID https://shibserv.abdn.ac.uk/shibboleth, asserting shibmd:Scope abdn.ac.uk. Its entity descriptor is published as signed, machine-readable SA
  name: Shibboleth SAML Identity Provider (UK Access Management Federation)
  slug: shibboleth-saml-idp
- description: The University's Microsoft Entra ID tenant, 8c2b19ad-5f9c-49d4-9077-3ec3cfc52b3f, resolvable from the abdn.ac.uk domain name. It publishes a live OpenID Connect discovery document (issuer https://logi
  name: Microsoft Entra ID tenant (institutional identity)
  slug: entra-id-tenant
- description: The Aberdeen University Research Archive (AURA) runs DSpace 8.1-SNAPSHOT and exposes a public HATEOAS REST API advertising 79 endpoint families — communities, collections, items, bitstreams, discovery
  name: AURA DSpace REST API (tenancy on Edinburgh IS infrastructure)
  slug: aura-dspace-rest
- description: AURA's OAI-PMH 2.0 endpoint, repositoryName "Aura", repositoryIdentifier aura.abdn.ac.uk, adminEmail aura-manager@abdn.ac.uk, earliest datestamp 2005-10-10. ListMetadataFormats offers thirteen formats
  name: AURA OAI-PMH Metadata Harvesting (tenancy on Edinburgh IS infrastructure)
  slug: aura-oai-pmh
- description: The University's tenancy of Elsevier Pure, its current research information system, published as "The University of Aberdeen Research Portal" at abdn.elsevierpure.com, which CNAMEs to eu.prod.elsevier
  name: Elsevier Pure CRIS tenancy (research portal, REST + OAI-PMH)
  slug: pure-cris-tenancy
- description: MyAberdeen, the University's virtual learning environment, is a Blackboard Learn tenancy at abdn.blackboard.com (www.abdn.ac.uk/myaberdeen redirects to it). The Blackboard Learn public REST API is pre
  name: MyAberdeen — Blackboard Learn tenancy
  slug: blackboard-learn-tenancy
- description: Library discovery runs on Ex Libris Primo VE at abdn.primo.exlibrisgroup.com with institution view 44ABE_INST:44ABE_VU1. The Primo and Alma REST APIs are Ex Libris products gated behind developer.exli
  name: Library discovery — Ex Libris Primo tenancy
  slug: primo-discovery-tenancy
- description: 'The University of Aberdeen is a DataCite member — provider symbol HUGZ, memberType consortium_organization, organizationType academicInstitution, country GB, region EMEA — and operates one registered '
  name: DataCite membership and registered repository
  slug: datacite-membership
- description: The University of Aberdeen is Crossref member 12669, located "Aberdeen, United Kingdom", holding DOI prefixes 10.57064 and 10.57132 with 795 DOIs deposited as of 2026-09-01. Recorded as a registry mem
  name: Crossref membership and DOI prefixes
  slug: crossref-membership
- description: The University of Aberdeen is registered in the Research Organization Registry as https://ror.org/016476m91, cross-walked to GRID grid.7107.1, ISNI 0000 0004 1936 7291, Wikidata Q270532 and Crossref F
  name: ROR organization registration
  slug: ror-registration
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.abdn.ac.uk/
- group: company
  title: ''
  type: Blog
  url: https://www.abdn.ac.uk/news/
- group: operate
  title: ''
  type: Support
  url: https://www.abdn.ac.uk/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.abdn.ac.uk/privacy
- group: other
  title: ''
  type: Accessibility
  url: https://www.abdn.ac.uk/accessibility
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uofa
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-aberdeen/
- group: other
  title: ''
  type: IdentityFederation
  url: http://mdq.ukfederation.org.uk/entities/https%3A%2F%2Fshibserv.abdn.ac.uk%2Fshibboleth
- group: other
  title: ''
  type: ResearchRepository
  url: https://www.abdn.ac.uk/library/open-research/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://abdn.primo.exlibrisgroup.com/discovery/search?vid=44ABE_INST:44ABE_VU1
- group: learn
  title: ''
  type: CourseCatalog
  url: https://www.abdn.ac.uk/study/courses/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.abdn.ac.uk/staffnet/education/generative-ai-in-education/university-of-aberdeen-ai-principles/
- group: build
  title: ''
  type: AITooling
  url: https://www.abdn.ac.uk/staffnet/education/generative-ai-in-education/guidance-and-resources-on-genai/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-aberdeen-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-aberdeen-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-aberdeen-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-aberdeen-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-aberdeen-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-aberdeen-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Aberdeen is a public research university in Aberdeen, Scotland, founded in 1495 and one of the four ancient universities of Scotland. Its programmable footprint is small, real, and almost entirely operated by somebody else. The University publishes NO institution-operated API contract: there is no api.abdn.ac.uk, no developer.abdn.ac.uk, no data.abdn.ac.uk, no open data portal, no public course, timetable or student-information-system API, no llms.txt and no sitemap.xml, and its verified GitHub organization (github.com/uofa) holds seventeen repositories of which every single one is a fork. What it does operate in machine-readable form is its identity estate: a Shibboleth SAML 2.0 Identity Provider, entityID https://shibserv.abdn.ac.uk/shibboleth, scope abdn.ac.uk, registered in the Jisc UK Access Management Federation and served as signed metadata through the federation MDQ service and directly from shibserv2.abdn.ac.uk, plus a Microsoft Entra ID tenant (8c2b19ad-5f9c-49d4-9077-3ec3cfc52b3f)
  with live OIDC discovery and WS-Federation metadata. Everything else that looks like an Aberdeen API is a tenancy. AURA, the Aberdeen University Research Archive, runs DSpace 8.1 and exposes a HATEOAS REST API and a thirteen-format OAI-PMH 2.0 endpoint — but aura.abdn.ac.uk CNAMEs to aura.abdn-lb.is.ed.ac.uk and resolves into University of Edinburgh Information Services address space, so the deployment is Edinburgh''s and the software is DSpace''s. The research portal at abdn.elsevierpure.com is Elsevier Pure; it serves a second OAI-PMH repository and a publicly readable 1.3MB openapi.yaml whose own info.title is "Pure API" and whose contact is pure-support@elsevier.com — that contract is Elsevier''s and is deliberately not held under this slug. MyAberdeen is Blackboard Learn and library discovery is Ex Libris Primo. The University is a Crossref member (12669, prefixes 10.57064 and 10.57132) and a DataCite member (HUGZ) operating the registered institutional repository BL.ABDN. Recorded
  honestly: one institution-operated surface class, five tenancies, three registry memberships, and zero API contracts of its own.'
finops:
- name: University Of Aberdeen Finops
  service_category: Education
  slug: university-of-aberdeen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-aberdeen.png
jsonld:
- class_count: 22
  name: University Of Aberdeen Context
  property_count: 3
  slug: university-of-aberdeen-context
layout: provider
modified: '2026-09-01'
name: University of Aberdeen
nav: Providers
network: true
overview: 'University of Aberdeen publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research, and United Kingdom.


  The University of Aberdeen catalog on APIs.io includes 1 JSON-LD context.


  University of Aberdeen''s developer surface includes engineering blog, support, GitHub presence, and 17 more developer resources.'
plans:
- name: University Of Aberdeen Plans Pricing
  plan_count: 2
  slug: university-of-aberdeen-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: University Of Aberdeen Rate Limits
  slug: university-of-aberdeen-rate-limits
score:
  band: thin
  composite: 27.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 48.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 14.3
    developer_ergonomics: 16.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 38.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-aberdeen/refs/heads/main/screenshots/university-of-aberdeen-2026-06-20T200131.png
security:
- kind: domain-security
  name: University Of Aberdeen Domain Security
  slug: university-of-aberdeen-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Aberdeen Vulnerability Disclosure
  slug: university-of-aberdeen-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: university-of-aberdeen
tags:
- Education
- Higher Education
- University
- Research
- United Kingdom
- Scotland
- Identity Federation
- Shibboleth
- Research Data
- Open Access
- Institutional Repository
- OAI-PMH
- DSpace
- Library
website: https://www.abdn.ac.uk/
---
