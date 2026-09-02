---
access_model:
  confidence: high
  label: Free · No signup, no key
  onboarding: unknown
  pricing: free
  public: true
  source:
  - authentication
  - probes
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
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The one institution-operated, keyless, machine-readable API surface the University of Bristol publishes. OAI-PMH 2.0 metadata harvesting for the University of Bristol Research Portal, served from the '
  name: University of Bristol Research Portal OAI-PMH
  slug: research-portal-oai-pmh
- description: Bristol operates its own Shibboleth identity provider at idp.bris.ac.uk, publishing SAML 2.0 metadata anonymously at /idp/shibboleth (200, application/xml, 5,990 bytes) and registered in the UK Access
  name: University of Bristol Identity Provider (Shibboleth / SAML 2.0)
  slug: idp-shibboleth
- description: data.bris is the University of Bristol's own research data repository — institution-built and institution-hosted, not a Figshare, Dataverse or DSpace tenancy. DataCite lists it as client BL.BRISTOL, "
  name: data.bris Research Data Repository
  slug: data-bris-research-data-repository
- description: TENANT RELATIONSHIP, NOT A BRISTOL CONTRACT. Bristol runs Elsevier Pure as its research information system, and Pure's product API answers on Bristol's own host at research-information.bris.ac.uk/ws/a
  name: Elsevier Pure Web Services (University of Bristol tenancy)
  slug: pure-web-services
- description: TENANT RELATIONSHIP, NOT A BRISTOL CONTRACT. Bristol's library discovery layer is an OCLC WorldCat Discovery tenancy at bris.on.worldcat.org — an institution-specific subdomain on the vendor's platfor
  name: University of Bristol Library Discovery (OCLC WorldCat Discovery)
  slug: library-discovery-worldcat
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://www.bristol.ac.uk/
- group: start
  title: ''
  type: Portal
  url: https://research-information.bris.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research-information.bris.ac.uk/
- group: other
  title: ''
  type: ResearchRepository
  url: https://data.bris.ac.uk/datasets/
- group: other
  title: ''
  type: OpenData
  url: https://data.bris.ac.uk/datasets/
- group: other
  title: ''
  type: IdentityFederation
  url: https://idp.bris.ac.uk/idp/shibboleth
- group: other
  title: ''
  type: IdentityFederation
  url: https://www.ukfederation.org.uk/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://bris.on.worldcat.org/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.bristol.ac.uk/bilt/sharing-practice/guides/guidance-on-ai/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.bristol.ac.uk/academic-quality/pg/ai-tools-and-thesis-writing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uob-hpc
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cs-uob
- group: docs
  title: ''
  type: Documentation
  url: https://www.bristol.ac.uk/staff/researchers/data/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bristol.ac.uk/web/policies/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bristol.ac.uk/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bristol.ac.uk/it-services/advice/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/university-of-bristol/
- group: design
  title: ''
  type: Conformance
  url: conformance/university-of-bristol-domain-standards.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/university-of-bristol-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/university-of-bristol-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-bristol-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/university-of-bristol-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/university-of-bristol-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/university-of-bristol-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of Bristol is a public research university in Bristol, United Kingdom, and a member of the Russell Group. Its programmable footprint is small, real, and mostly indirect: it operates no developer portal, no open-data platform and no central API programme, and api.bris.ac.uk, developer.bristol.ac.uk, timetable.bristol.ac.uk and status.bristol.ac.uk do not resolve. The one institution-operated, keyless, machine-readable API surface found is the University of Bristol Research Portal OAI-PMH 2.0 endpoint at research-information.bris.ac.uk, which advertises 590,974 records across 3,878 sets in seven metadata formats including the OpenAIRE CERIF 1.2 profile, with no authentication — although its mandatory Identify verb returns HTTP 500. Beyond it, Bristol operates a Shibboleth SAML 2.0 identity provider registered in the UK Access Management Federation since 2010 and asserting REFEDS Research & Scholarship, and data.bris, its own research data repository, which has
  minted 1,552 DataCite DOIs under the institution''s own prefix 10.5523/bris since 2012. Everything else that looks like a Bristol API is a vendor''s contract running under Bristol''s name — Elsevier Pure for the research portal''s /ws/api web services, OCLC WorldCat Discovery for library search. Those relationships are recorded here as tenant surfaces; the vendors'' contracts are not.'
examples:
- key_count: 7
  name: University Of Bristol Oai Pmh Examples
  slug: university-of-bristol-oai-pmh-examples
finops:
- name: University Of Bristol Finops
  service_category: Education
  slug: university-of-bristol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-bristol.png
layout: provider
modified: '2026-08-30'
name: University of Bristol
nav: Providers
network: true
overview: 'University of Bristol publishes 1 API on the [APIs.io](https://apis.io/) network: Research Portal OAI-PMH. Tagged areas include University, Higher Education, Education, United Kingdom, and Russell Group.


  The University of Bristol catalog on APIs.io includes 1 Spectral governance ruleset.


  University of Bristol''s developer surface includes developer portal, documentation, support, authentication, and 21 more developer resources.'
plans:
- name: University Of Bristol Plans Pricing
  plan_count: 2
  slug: university-of-bristol-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: University Of Bristol Rate Limits
  slug: university-of-bristol-rate-limits
rules:
- effective_rule_count: 8
  extends: []
  name: University of Bristol API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 0
    warn: 2
  slug: university-of-bristol-oai-pmh-spectral-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 13
    catalog_gap: 47.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -8.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 34.1
    contract_quality: 17.5
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 34.1
    operational_transparency: 23.7
  previous_composite: 46.4
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
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-bristol/refs/heads/main/screenshots/university-of-bristol-2026-06-20T200140.png
security:
- kind: authentication
  name: University Of Bristol Authentication
  slug: university-of-bristol-authentication
  summary_line: none/apiKey/saml · 0 schemes
- kind: domain-security
  name: University Of Bristol Domain Security
  slug: university-of-bristol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: university-of-bristol
tags:
- University
- Higher Education
- Education
- United Kingdom
- Russell Group
- Research Data
- Research Repository
- Metadata Harvesting
- OAI-PMH
- Identity Federation
- Open Data
website: https://www.bristol.ac.uk/
---
