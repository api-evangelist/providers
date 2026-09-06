---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Public-facing website of the Defense Security Cooperation Agency that describes its mission, leadership, programs, and partners. The site links to news, the security cooperation library, and the FMS p
  name: DSCA Website
  slug: defense-security-cooperation-agency-website
- description: DSCA publishes Major Arms Sales notifications and supporting transmittal documents that Congress and the public use to track potential Foreign Military Sales cases. Notifications are posted as web pag
  name: DSCA Major Arms Sales Notifications
  slug: defense-security-cooperation-agency-major-arms-sales
- description: 'Government-to-government portal that hosts case management, financial, and logistical information for security cooperation partners. SCIP requires authenticated access and operates outside the public '
  name: Security Cooperation Information Portal (SCIP)
  slug: defense-security-cooperation-agency-scip
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-security-cooperation-agency-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defense-security-cooperation-agency
- group: company
  title: ''
  type: Website
  url: https://www.dsca.mil
- group: company
  title: ''
  type: News
  url: https://www.dsca.mil/press-media/news-articles
- group: build
  title: ''
  type: Library
  url: https://www.dsca.mil/security-cooperation-library
- group: operate
  title: ''
  type: ContactUs
  url: https://www.dsca.mil/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dsca.mil/privacy-and-security-policy
- group: other
  title: ''
  type: FOIA
  url: https://open.defense.gov/Transparency/FOIA.aspx
- group: other
  title: ''
  type: ProductPage
  url: https://www.dscu.edu
created: '2024-12-03'
description: The Defense Security Cooperation Agency (DSCA) is the U.S. Department of Defense agency that leads, directs, and manages security cooperation programs and resources to support U.S. policy and interests with foreign partners. DSCA administers the Foreign Military Sales (FMS) program, Foreign Military Financing (FMF) execution, International Military Education and Training (IMET), and humanitarian assistance programs. Public-facing surfaces include the Major Arms Sales notifications published in cooperation with Congress, the DSCA newsroom and library, and the Security Cooperation Workforce certification portal. DSCA does not publish a general-purpose developer API; partner-nation systems interact through controlled, government-to-government channels such as the Security Cooperation Information Portal (SCIP).
finops:
- name: Defense Security Cooperation Agency Finops
  service_category: API
  slug: defense-security-cooperation-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-security-cooperation-agency.png
layout: provider
modified: '2026-07-25'
name: Defense Security Cooperation Agency
nav: Providers
network: true
overview: 'Defense Security Cooperation Agency publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Defense, Department of Defense, DSCA, Federal-Government, and Foreign Military Sales.


  Defense Security Cooperation Agency''s developer surface includes product news and 8 more developer resources.'
plans:
- name: Defense Security Cooperation Agency Plans Pricing
  plan_count: 3
  slug: defense-security-cooperation-agency-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Defense Security Cooperation Agency Rate Limits
  slug: defense-security-cooperation-agency-rate-limits
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  previous_composite: 14.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/defense-security-cooperation-agency/refs/heads/main/screenshots/defense-security-cooperation-agency-2026-06-20T175837.png
security:
- kind: domain-security
  name: Defense Security Cooperation Agency Domain Security
  slug: defense-security-cooperation-agency-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: defense-security-cooperation-agency
tags:
- Defense
- Department of Defense
- DSCA
- Federal-Government
- Foreign Military Sales
- International
- Security Cooperation
website: https://www.dsca.mil
---
