---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://plancraft.com/
- group: operate
  title: ''
  type: Support
  url: https://help.plancraft.com/de/
- group: company
  title: ''
  type: Blog
  url: https://plancraft.com/de-de/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://plancraft.com/de-de/preises
- group: start
  title: ''
  type: SignUp
  url: https://plancraft.com/de-de/register
- group: start
  title: ''
  type: Login
  url: https://plancraft.com/de-de/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plancraft.com/de-de/agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plancraft.com/de-de/datenschutz
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/plancraft-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plancraft-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plancraft-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/plancraft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://plancraft.com/.well-known/security.txt
created: '2026-07-17'
description: plancraft is a German cloud-based business management software for craftspeople and trades businesses (Handwerk). It digitizes administrative workflows end to end — quote and estimate creation, project planning, time tracking, on-site documentation, material and labor costing, and invoicing — inside one integrated platform aimed at small and mid-sized construction and trade companies. plancraft supports DATEV export for tax/accounting workflows and DATANORM and GAEB catalog imports for material data and tender processing. It is a venture-backed SaaS company (portfolio company of Creandum). As of this enrichment pass plancraft publishes no public developer API, SDK, or OpenAPI surface — integrations are delivered as prebuilt connectors and standardized file-format import/export.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plancraft.png
layout: provider
modified: '2026-07-20'
name: plancraft
nav: Providers
network: true
overview: 'plancraft is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Construction, Trades, and Handwerk.


  plancraft''s developer surface includes support, engineering blog, pricing, signup flow, and 9 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 13.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plancraft/refs/heads/main/screenshots/plancraft-2026-09-02T151424.png
security:
- kind: domain-security
  name: Plancraft Domain Security
  slug: plancraft-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Plancraft Vulnerability Disclosure
  slug: plancraft-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: plancraft
tags:
- Company
- Software-as-a-Service
- Construction
- Trades
- Handwerk
- Field Service
- Invoicing
- Project Management
- Germany
website: https://plancraft.com/
---
