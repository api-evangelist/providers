---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Public REST API for the 4TU.ResearchData repository (data.4tu.nl), which TU Delft co-founded and leads. Provides versioned endpoints (v2/v3) for published articles (datasets), collections, categories,
  name: 4TU.ResearchData API
  slug: researchdata
- description: OAI-PMH metadata harvesting interface for the 4TU.ResearchData repository, enabling programmatic harvesting of dataset and software metadata (findable via DataCite, Google Dataset Search and aggregato
  name: 4TU.ResearchData OAI-PMH
  slug: researchdata-oaipmh
- description: Institutional repository for publicly available TU Delft research output, peer-reviewed articles, technical reports and 46,000+ bachelor/master theses. Metadata is licensed CC0 and exposed for program
  name: TU Delft Repository (OAI-PMH)
  slug: repository-oaipmh
- description: TU Delft single sign-on and identity service (NetID) used for authentication across TU Delft web services and as the OAuth2 authorization service (oauth.tudelft.nl) for institutional API access, suppo
  name: TU Delft NetID / OAuth2 SSO
  slug: identity
- description: Legacy general-purpose TU Delft API platform (api.tudelft.nl) exposing campus, buildings, computer workspaces, educations, study-years, courses, course schedules, study results/progress and TU Delft o
  name: TU Delft API Platform (legacy / suspended)
  slug: institutional-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tu-delft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tu-delft-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tudelft.nl/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/4TUResearchData
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/tu-delft/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://djehuty.4tu.nl/
- group: auth
  title: ''
  type: Authentication
  url: https://login.tudelft.nl/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/4TUResearchData/djehuty
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
description: 'Delft University of Technology (TU Delft) is the largest and oldest public technical university in the Netherlands, ranked #51 in the QS World University Rankings 2025. Its public developer footprint centers on research and library data infrastructure rather than a unified developer portal: the 4TU.ResearchData repository (data.4tu.nl), which TU Delft co-founded and leads, exposes a public REST API (v2/v3, the open-source "djehuty" platform) plus OAI-PMH metadata harvesting; the TU Delft Repository (repository.tudelft.nl) publishes open-access theses and research output with OAI-PMH metadata; and TU Delft operates a NetID/OAuth2 single sign-on identity service. TU Delft historically ran a general institutional API platform at api.tudelft.nl (campus, buildings, courses, education and organisation data) secured with OAuth2, but that platform has been publicly announced as being suspended with no new client registrations accepted, so it is documented here as gated/legacy.'
finops:
- name: Tu Delft Finops
  service_category: Education
  slug: tu-delft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tu-delft.png
jsonld:
- class_count: 16
  name: Tu Delft Context
  property_count: 0
  slug: tu-delft-context
layout: provider
modified: '2026-06-03'
name: Delft University of Technology
nav: Providers
network: true
overview: 'Delft University of Technology publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Higher Education, University, Research Data, and Open Access.


  The Delft University of Technology catalog on APIs.io includes 1 JSON-LD context.


  Delft University of Technology''s developer surface includes GitHub presence, authentication, and 10 more developer resources.'
plans:
- name: Tu Delft Plans Pricing
  plan_count: 2
  slug: tu-delft-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Tu Delft Rate Limits
  slug: tu-delft-rate-limits
score:
  band: emerging
  composite: 25.8
  delta: -3.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
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
- Education
- Higher Education
- University
- Research Data
- Open Access
- Library
- Open Data
- Netherlands
- Europe
website: https://www.tudelft.nl/
---
