---
access_model:
  confidence: high
  label: Free
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: Public REST API for the 4TU.ResearchData repository, the science/engineering/design research data repository of the 4TU.Federation, hosted and operated by TU Delft Library. Twelve endpoints verified l
  name: 4TU.ResearchData API
  slug: 4tu-researchdata
- description: TU Delft's SimpleSAMLphp identity provider — the machine-readable half of NetID. It publishes a signed SAML 2.0 EntityDescriptor with an IDPSSODescriptor and is registered in SURFconext, the Dutch nat
  name: TU Delft SAML 2.0 Identity Provider (NetID)
  slug: identity-federation
- description: TU Delft runs an Elsevier Pure current research information system, exposed to the public as the research portal at research.tudelft.nl / pure.tudelft.nl and to integrators as the Pure Web Service und
  name: Elsevier Pure research portal (TU Delft tenancy)
  slug: pure
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://www.tudelft.nl/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tu-delft/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/4TUResearchData
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/4TUResearchData/djehuty
- group: docs
  title: ''
  type: Documentation
  url: https://djehuty.4tu.nl/
- group: docs
  title: ''
  type: APIReference
  url: https://djehuty.4tu.nl/
- group: other
  title: ''
  type: OpenData
  url: https://data.4tu.nl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://repository.tudelft.nl/
- group: other
  title: ''
  type: ResearchRepository
  url: https://research.tudelft.nl/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://tudelft.on.worldcat.org/discovery
- group: learn
  title: ''
  type: CourseCatalog
  url: https://studiegids.tudelft.nl/
- group: other
  title: ''
  type: IdentityFederation
  url: https://login.tudelft.nl/sso/saml2/idp/metadata.php
- group: other
  title: ''
  type: ResearchComputing
  url: https://doc.dhpc.tudelft.nl/delftblue/
- group: other
  title: ''
  type: AIPolicy
  url: https://www.tudelft.nl/en/teaching-support/educational-advice/assess/guidelines/ai-chatbots-in-unsupervised-assessment
- group: build
  title: ''
  type: AITooling
  url: https://www.tudelft.nl/en/ai
- group: learn
  title: ''
  type: OpenCourseWare
  url: https://ocw.tudelft.nl/
- group: build
  title: ''
  type: Library
  url: https://www.tudelft.nl/en/library/
- group: company
  title: ''
  type: Blog
  url: https://community.data.4tu.nl/
- group: operate
  title: ''
  type: Support
  url: https://www.tudelft.nl/en/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tudelft.nl/en/privacy-statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.4tu.nl/info/about-4turesearchdata/policies-guidelines
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.tudelft.nl/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tu-delft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tu-delft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tu-delft-authentication.yml
- group: auth
  title: ''
  type: Scopes
  url: scopes/tu-delft-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tu-delft-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tu-delft-lifecycle.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tu-delft-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tu-delft-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/tu-delft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tu-delft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tu-delft-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Delft University of Technology (TU Delft) is the oldest and largest public technical university in the Netherlands and a member of the 4TU.Federation. Its programmable footprint is narrow, and this profile states that plainly rather than padding it. TU Delft operates exactly one public, unauthenticated API: the 4TU.ResearchData repository at data.4tu.nl, which runs on djehuty, open-source repository software written by 4TU.ResearchData and Nikhef. The /v2 surface is deliberately shape-compatible with the Figshare v2 API because that was a requirement of the 2023 migration OFF Figshare — the contract is not Figshare''s, and the service runs inside TU Delft''s own RIPE netblock (DUNET, 131.180.0.0/16). The other genuinely institution-operated machine-readable surface is a SAML 2.0 identity provider at login.tudelft.nl, published into the SURFconext national federation and onward to eduGAIN. Beyond those two, the picture is retirement and tenancy. The general-purpose institutional
  API platform at api.tudelft.nl — campus, buildings, courses, schedules, study results, organisation — no longer answers on port 80 or 443, and its documentation host apidoc.tudelft.nl has no DNS record at all. The research information portal at pure.tudelft.nl / research.tudelft.nl is an Elsevier Pure tenancy whose own API documentation canonicalises to api.elsevierpure.com: TU Delft''s data, Elsevier''s contract. The library discovery layer is an OCLC WorldCat tenancy. No working OAI-PMH endpoint exists on any TU Delft-operated host despite third-party registry entries claiming otherwise. TU Delft publishes no OpenAPI, no llms.txt, no scope vocabulary and no API changelog.'
examples:
- key_count: 5
  name: Tu Delft 4Tu Researchdata Examples
  slug: tu-delft-4tu-researchdata-examples
finops:
- name: Tu Delft Finops
  service_category: Education
  slug: tu-delft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tu-delft.png
json_schemas:
- name: 4TU.ResearchData Dataset
  property_count: 42
  slug: tu-delft-4tu-dataset
jsonld:
- class_count: 16
  name: Tu Delft Context
  property_count: 0
  slug: tu-delft-context
layout: provider
modified: '2026-08-19'
name: Delft University of Technology
nav: Providers
network: true
overview: 'Delft University of Technology publishes 1 API on the [APIs.io](https://apis.io/) network: 4TU.ResearchData API. Tagged areas include University, Higher Education, Education, Technical University, and Research Data.


  The Delft University of Technology catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Delft University of Technology''s developer surface includes documentation, API reference, engineering blog, support, authentication, and 29 more developer resources.'
plans:
- name: Tu Delft Plans Pricing
  plan_count: 2
  slug: tu-delft-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Tu Delft Rate Limits
  slug: tu-delft-rate-limits
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Delft University of Technology API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 2
  slug: tu-delft-4tu-rules
scopes:
- name: Tu Delft Scopes
  scope_count: 0
  slug: tu-delft-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.3
  delta: 0.9
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 67.4
    contract_quality: 68.0
    developer_ergonomics: 35.7
    discoverability: 85.2
    governance: 67.4
    operational_transparency: 23.7
  previous_composite: 62.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 90.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Tu Delft Authentication
  slug: tu-delft-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tu Delft Domain Security
  slug: tu-delft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tu Delft Vulnerability Disclosure
  slug: tu-delft-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tu-delft
tags:
- University
- Higher Education
- Education
- Technical University
- Research Data
- Open Access
- Identity Federation
- Research Repository
- Research Computing
- 4TU.Federation
- Netherlands
- Europe
website: https://www.tudelft.nl/
---
