---
access_model:
  confidence: high
  label: Open metadata harvesting, no signup; everything else is affiliation-gated
  onboarding: unknown
  pricing: free
  public: true
  source:
  - live probe
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
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: 'Live OAI-PMH 2.0 harvesting interface for the TU/e Research Portal, served by Elsevier Pure at TU/e''s own pure.tue.nl. Verified with a real harvest, not link presence: verb=Identify returns repository'
  name: TU/e Research Portal OAI-PMH
  slug: research-oai-pmh
- description: 'TU/e''s deployment of the Elsevier Pure Web Service REST API, the research-information (CRIS) interface behind the TU/e Research Portal. The deployment''s own generated documentation is live and public '
  name: TU/e Pure Web Service (Elsevier Pure deployment)
  slug: pure-web-service
- description: TU/e's SAML 2.0 identity-provider entity as published in the SURFconext federation metadata, which feeds eduGAIN. The EntityDescriptor carries OrganizationName "Technische Universiteit Eindhoven" / "E
  name: TU/e SAML Identity Provider (SURFconext / eduGAIN)
  slug: surfconext-saml-idp
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.tue.nl/en/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.tue.nl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://data.4tu.nl/search?q=&categories=&organizations=Eindhoven%20University%20of%20Technology
- group: other
  title: ''
  type: IdentityFederation
  url: https://metadata.surfconext.nl/idps-metadata.xml
- group: learn
  title: ''
  type: CourseCatalog
  url: https://educationguide.tue.nl/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.tueindhoven.ai/education/guidelines/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://pure.tue.nl/ws/api/documentation/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tue.nl/en/storage/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tue.nl/en/our-university/about-the-university/support-services/library-and-information-services/privacy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TUEIndhoven
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tue-datastewards
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/eindhoven-university-of-technology/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eindhoven-university-of-technology-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eindhoven-university-of-technology-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/eindhoven-university-of-technology-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/eindhoven-university-of-technology-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eindhoven-university-of-technology-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/eindhoven-university-of-technology-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  checked: '2026-08-30'
  detail: 'TU/e publishes no institution-authored API contract and operates no developer portal. Every machine-readable surface found is a vendor''s product running under TU/e''s name: Elsevier Pure (research portal, Pure Web Service, OAI-PMH), Caci Osiris (student mobile), OCLC WorldCat (library discovery), Figshare via the 4TU.ResearchData consortium (datasets), and Microsoft Entra ID behind SURFconext (identity). Three of those are TU/e''s own deployments and are recorded as tenant surfaces; the rest belong in the vendors'' own repositories. The one fully public, keyless, verified-by-real-request surface is the OAI-PMH endpoint. Probed and NOT found, so the absence is measured rather than assumed: data.tue.nl, api.tue.nl, developer.tue.nl, opendata.tue.nl, ooapi.tue.nl, api.ooapi.tue.nl, idp.tue.nl, login.tue.nl, sts.tue.nl, sis.tue.nl, mytimetable.tue.nl and rooster.tue.nl all fail to resolve in DNS — they are not gated, they do not exist. purefaq.tue.nl, the Pure FAQ this repo previously
    carried as a Documentation pointer, now returns a deliberate TU/e "Off-site access blocked" page: it is VPN/campus-network-only, so it is recorded as evidence here and removed as a pointer. TU/e is named by SURF as a 2019 Open Onderwijs API (OOAPI) participant, but Dutch OOAPI endpoints are SURFconext-gated and none is publicly discoverable. github.com/TUEIndhoven resolves but holds zero public repositories; the departmental orgs (tue-datastewards, tue-robotics, tue-mdse, tue-aga, TUe-ICTLab, 3DCP-TUe) are research-group code, not an institutional API programme.'
  evidence:
  - note: OAI-PMH 2.0 live; repositoryName "Pure OAI Repository"; adminEmail pure@tue.nl; OpenAIRE CERIF 1.2.
    status: 200
    url: https://pure.tue.nl/ws/oai?verb=Identify
  - note: Seven metadata prefixes served.
    status: 200
    url: https://pure.tue.nl/ws/oai?verb=ListMetadataFormats
  - note: Real records returned (110,958 bytes, cerif:Person, resumptionToken) — a harvest, not a link check.
    status: 200
    url: https://pure.tue.nl/ws/oai?verb=ListRecords&metadataPrefix=oai_cerif_openaire&set=openaire_cris_persons
  - note: Elsevier Pure Web Service generated documentation for TU/e's deployment; the API itself is api-key gated.
    status: 200
    url: https://pure.tue.nl/ws/api/documentation/index.html
  - note: TU/e SAML 2.0 IdP EntityDescriptor present in the SURFconext federation metadata.
    status: 200
    url: https://metadata.surfconext.nl/idps-metadata.xml
  - note: Institutional website; no developer, API or docs section anywhere in navigation.
    status: 200
    url: https://www.tue.nl/en/
  - note: No llms.txt (soft-404 — returns the 246KB site 404 page, not an empty body).
    status: 404
    url: https://www.tue.nl/llms.txt
  - note: 'Deliberate institutional gate, not a bot block: body is TU/e''s own "Off-site access blocked — only accessible via the TU/e network or the TU/e VPN" page. Removed as a pointer.'
    status: 403
    url: https://purefaq.tue.nl/pure/faq/index.php?action=overview
  - note: Pure portal edge challenge; research.tue.nl root is 200, so the host is live.
    status: 403
    url: https://research.tue.nl/en/organisations/
  - note: SPA shell only (2,931 bytes, title "Osiris Student Mobile"); its CSP names the vendor backend rontw.osiris-student.nl. Caci vendor product, not a TU/e API.
    status: 200
    url: https://osiris.tue.nl/
  - note: OCLC WorldCat Discovery SPA shell — vendor library discovery, no institution-operated catalog API.
    status: 200
    url: https://tue.on.worldcat.org/discovery
  - note: 4TU.ResearchData (Figshare) consortium repository; TU/e is one of four member institutions, not the operator.
    status: 200
    url: https://data.4tu.nl/search?q=&categories=&organizations=Eindhoven%20University%20of%20Technology
  - note: TU/e Framework for AI in Engineering Education; adopted by the educational board and program directors in 2024. Governance document, not an API.
    status: 200
    url: https://www.tueindhoven.ai/education/guidelines/index.html
  - note: PGP-signed security.txt, Expires 2027-02-09; contact and policy both the TU/e CERT RFC 2350 document.
    status: 200
    url: https://www.tue.nl/.well-known/security.txt
  - note: TU/e GitHub organization exists but publishes zero public repositories.
    status: 200
    url: https://github.com/TUEIndhoven
  - note: Course catalog is a rendered web guide; /api and /openapi.json both 404. No public course API.
    status: 200
    url: https://educationguide.tue.nl/
  reason: tenant_only
  state: none
created: '2026-06-03'
description: 'Eindhoven University of Technology (TU/e) is a public technical university in Eindhoven, the Netherlands, and one of the four institutions of the 4TU federation. It operates no public developer portal, publishes no institution-authored API contract, and offers no self-serve API keys — and this profile says so rather than padding the gap. Everything machine-readable that carries the TU/e name is a deployment of somebody else''s software: the TU/e Research Portal and its Pure Web Service REST API are Elsevier Pure 5.35.x running at pure.tue.nl, the student mobile app at osiris.tue.nl is Caci Osiris, library discovery is OCLC WorldCat, and research datasets are minted through the 4TU.ResearchData Figshare consortium. What TU/e genuinely operates on its own domain is narrower and real: a live, fully conformant OAI-PMH 2.0 harvesting endpoint at pure.tue.nl/ws/oai serving seven metadata formats and the OpenAIRE CERIF 1.2 CRIS profile, and a SAML 2.0 identity-provider entity registered
  in the SURFconext federation and so reachable through eduGAIN. Thirty-seven OpenAPI documents previously attributed to TU/e in this repository were Elsevier''s Pure product contract (info.title "Pure …", contact pure-support@elsevier.com, relative servers "/ws/api", shipped identically by nine other universities) and have been removed; the tenant relationships they described are recorded here instead. Departmental research groups publish open source across many separate GitHub organizations, but the university runs no single official engineering org.'
finops:
- name: Eindhoven University Of Technology Finops
  service_category: Education
  slug: eindhoven-university-of-technology-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eindhoven-university-of-technology.png
layout: provider
modified: '2026-08-30'
name: Eindhoven University of Technology
nav: Providers
network: true
overview: 'Eindhoven University of Technology publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Technical University, and Netherlands.


  Eindhoven University of Technology''s developer surface includes documentation, GitHub presence, and 17 more developer resources.'
plans:
- name: Eindhoven University Of Technology Plans Pricing
  plan_count: 2
  slug: eindhoven-university-of-technology-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Eindhoven University Of Technology Rate Limits
  slug: eindhoven-university-of-technology-rate-limits
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -12.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 37
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/eindhoven-university-of-technology/refs/heads/main/screenshots/eindhoven-university-of-technology-2026-06-20T180525.png
security:
- kind: domain-security
  name: Eindhoven University Of Technology Domain Security
  slug: eindhoven-university-of-technology-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Eindhoven University Of Technology Vulnerability Disclosure
  slug: eindhoven-university-of-technology-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: eindhoven-university-of-technology
tags:
- University
- Higher Education
- Education
- Technical University
- Netherlands
- Europe
- 4TU
- Research Data
- Research Information
- Research Repository
- Identity Federation
- OAI-PMH
- Open Metadata
website: https://www.tue.nl/en/
---
