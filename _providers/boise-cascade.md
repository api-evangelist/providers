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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 13
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/security/boise-cascade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boise-cascade-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boise-cascade
- group: company
  title: ''
  type: Website
  url: https://www.bc.com
- group: company
  title: ''
  type: About
  url: https://www.bc.com/company/
- group: other
  title: ''
  type: Products
  url: https://www.bc.com/ewp/
- group: other
  title: ''
  type: Software
  url: https://www.bc.com/ewp/software/
- group: other
  title: ''
  type: Distribution
  url: https://www.bc.com/distribution/
- group: company
  title: ''
  type: Blog
  url: https://www.bc.com/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.bc.com/contact/
- group: other
  title: ''
  type: Leadership
  url: https://www.bc.com/leadership/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bc.com/news/
- group: company
  title: ''
  type: Investors
  url: https://www.bc.com/investors/
- group: company
  title: ''
  type: Careers
  url: https://www.bc.com/careers/
- group: operate
  title: ''
  type: Support
  url: https://www.bc.com/ewp/support/
- group: other
  title: ''
  type: EULA
  url: https://www.bc.com/software/eula/
- group: start
  title: ''
  type: CustomerPortal
  url: https://www.bc.com/bmd-ecatalog/
- group: other
  title: ''
  type: EDI
  url: https://www.bc.com/portal/customers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bc.com/terms-conditions/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bc.com/privacy-policy/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/well-known/boise-cascade-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/boise-cascade-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/conformance/boise-cascade-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boise-cascade-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/llms/boise-cascade-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boise-cascade-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/regulatory/boise-cascade-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/boise-cascade-regulatory-posture.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/regulatory/boise-cascade-regulatory-posture.yml
  title: ''
  type: GlobalPrivacyControl
  url: regulatory/boise-cascade-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/regulatory/boise-cascade-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/boise-cascade-regulatory-posture.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/plans/boise-cascade-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boise-cascade-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/rate-limits/boise-cascade-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/boise-cascade-rate-limits.yml
coverage:
  checked: '2026-09-19'
  detail: Boise Cascade ships software only as end-user applications (BC Connect, BC Calc, BC Framer, BC FastPlan, BC Estimator, BC FloorValue) and markets no API — www.bc.com/developers and /api 404, the BC Connect backend api.bcconnect.com is an AWS API Gateway answering 403 Forbidden to every path with no documentation anywhere, the eCatalog and Wood Orders portals redirect to logins, every /.well-known/ path misses on all seven hosts, and the only published machine integration is an ANSI X12 EDI exchange over VAN/FTP arranged by email.
  evidence:
  - status: 404
    url: https://www.bc.com/developers/
  - status: 404
    url: https://www.bc.com/openapi.json
  - status: 403
    url: https://api.bcconnect.com/openapi.json
  - status: 302
    url: https://www.bcconnect.com/api
  - status: 302
    url: https://ecatalog.bc.com/
  - status: 404
    url: https://www.bc.com/.well-known/agent-card.json
  - status: 200
    url: https://www.bc.com/portal/customers/
  reason: no-developer-program
  state: none
created: '2024-01-01'
description: Boise Cascade is a leading North American manufacturer and distributor of building materials for the residential and commercial construction industry. The company produces engineered wood products (EWP) including I-joists, LVL beams, and glulam, as well as structural panels and lumber, and distributes a broad range of building materials through its wholesale distribution network.
features:
- features:
  - Engineering Analysis
  - Beam Analysis
  - Joist Analysis
  - Column Analysis
  - Stud Analysis
  - Load Entry
  - Product Selection
  - EWP Sizing
  name: BC Calc
  url: https://www.bc.com/ewp/software/bc-calc/
- features:
  - Floor Framing
  - Roof Framing
  - 3D Framing Layouts
  - Framing Drawings
  - Schedule Creation
  name: BC Framer
  url: https://www.bc.com/ewp/software/
- features:
  - Project File Exchange
  - Collaboration Hub
  - Multi-Stakeholder Access
  name: BC Connect
  url: https://www.bc.com/ewp/software/bc-connect/
- features:
  - Fast Estimation
  - Plan Takeoffs
  name: BC FastPlan
  url: https://www.bc.com/ewp/software/
- features:
  - Project Estimating
  - Cost Estimation
  name: BC Estimator
  url: https://www.bc.com/ewp/software/
- features:
  - Saw Optimization
  - Cutting Schedules
  name: SawTek
  url: https://www.bc.com/ewp/software/
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boise-cascade.png
layout: provider
modified: '2026-09-19'
name: Boise Cascade
nav: Providers
network: true
overview: 'Boise Cascade is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Building Materials, Construction, Distribution, Engineered Wood, and Forest Products.


  Boise Cascade''s developer surface includes engineering blog, support, and 25 more developer resources.'
plans:
- name: Boise Cascade Plans Pricing
  plan_count: 0
  slug: boise-cascade-plans-pricing
press:
- date: ''
  title: Boise Cascade Company (BCC) Q4 2023 Earnings Call ...
  url: https://seekingalpha.com/article/4672147-boise-cascade-company-bcc-q4-2023-earnings-call-transcript
- date: ''
  title: Boise Cascade named one of the Most Trustworthy Companies in America in 2026
  url: https://www.bc.com/boise-cascade-named-one-of-the-most-trustworthy-companies-in-america-in-2026/
- date: ''
  title: Boise Cascade reports fourth quarter and full year 2025 results
  url: https://www.bc.com/boise-cascade-reports-fourth-quarter-and-full-year-2025-results/
- date: ''
  title: Boise Cascade announces quarterly dividend of $0.22 per share
  url: https://www.bc.com/boise-cascade-announces-quarterly-dividend-of-0-22-per-share/
- date: ''
  title: Boise Cascade announces quarterly dividend of $0.22 per share
  url: https://www.bc.com/boise-cascade-announces-quarterly-dividend-of-0-22-per-share-2/
- date: ''
  title: Boise Cascade schedules fourth quarter and full year 2025 earnings webcast and conference call
  url: https://www.bc.com/boise-cascade-schedules-fourth-quarter-and-full-year-2025-earnings-webcast-and-conference-call/
- date: ''
  title: Boise Cascade Reports Lower Sales, Profit as Home ...
  url: https://www.wsj.com/business/earnings/boise-cascade-reports-lower-sales-profit-as-home-construction-slows-45a19c5d
- date: ''
  title: Perkins Coie Represents Boise Cascade Company in Its ...
  url: https://perkinscoie.com/news/press-release/perkins-coie-represents-boise-cascade-company-its-acquisition-brockway-smith
random_paper: 7
rate_limits:
- limit_count: 0
  name: Boise Cascade Rate Limits
  slug: boise-cascade-rate-limits
score:
  band: emerging
  composite: 12.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 12.8
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/boise-cascade/refs/heads/main/screenshots/boise-cascade-2026-06-20T173552.png
security:
- kind: domain-security
  name: Boise Cascade Domain Security
  slug: boise-cascade-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boise-cascade
tags:
- Building Materials
- Construction
- Distribution
- Engineered Wood
- Forest Products
- Lumber
- Manufacturing
- Fortune 1000
use_cases:
- features:
  - Beam Sizing
  - Joist Sizing
  - Column Design
  - Structural Analysis
  - Load Calculations
  - Span Tables
  name: Engineered Wood Product Design
  url: https://www.bc.com/ewp/software/bc-calc/
- features:
  - Framing Layouts
  - Floor Framing
  - Roof Framing
  - 3D Drafting
  - Piece Reports
  - Price Reports
  name: Floor and Roof Framing
  url: https://www.bc.com/ewp/software/bc-framer/
- features:
  - File Exchange
  - Project Management
  - Stakeholder Collaboration
  - Document Sharing
  name: Project Collaboration
  url: https://www.bc.com/ewp/software/bc-connect/
- features:
  - Wholesale Distribution
  - Product Sourcing
  - Dealer Supply
  - Home Improvement Centers
  - Industrial Supply
  name: Building Materials Distribution
  url: https://www.bc.com/distribution/
website: https://www.bc.com
---
