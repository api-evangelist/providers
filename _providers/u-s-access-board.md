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
api_count: 0
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/u-s-access-board-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atbcb
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/us-access-board
- group: company
  title: ''
  type: Website
  url: https://www.access-board.gov/
- group: company
  title: ''
  type: About
  url: https://www.access-board.gov/about/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.access-board.gov/guidance.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.access-board.gov/about/policy/
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/u-s-access-board/refs/heads/main/vocabulary/u-s-access-board-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/u-s-access-board/refs/heads/main/json-ld/u-s-access-board-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://www.access-board.gov/news/
created: '2024-11-20'
description: The U.S. Access Board is an independent federal agency that promotes equality for people with disabilities through the development of accessibility guidelines and standards. The Board develops criteria for accessibility in the built environment, transportation, communication, and information and communication technology (ICT). It enforces the Architectural Barriers Act (ABA) for federally funded facilities and provides technical assistance, training, and guidance documents to help organizations implement accessibility requirements under the Americans with Disabilities Act (ADA) and Section 508 of the Rehabilitation Act.
features:
- description: Minimum accessibility guidelines for places of public accommodation, commercial facilities, and state and local government facilities under the Americans with Disabilities Act.
  name: ADA Accessibility Standards
- description: Technical and functional requirements for information and communication technology procured or developed by federal agencies under Section 508 of the Rehabilitation Act.
  name: Section 508 ICT Standards
- description: Accessibility requirements for telecommunications equipment and customer premises equipment manufacturers under the Telecommunications Act.
  name: Section 255 Guidelines
- description: Accessibility standards for facilities designed, built, altered, or leased with federal funds under the Architectural Barriers Act.
  name: ABA Standards
- description: Free technical assistance through webinars, training sessions, and direct responses to accessibility questions from designers, builders, and individuals with disabilities.
  name: Technical Assistance
- description: Comprehensive guidance documents, animations, and technical aids explaining how to apply accessibility standards in practice.
  name: Guidance Documents
finops:
- name: U S Access Board Finops
  service_category: API
  slug: u-s-access-board-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/u-s-access-board.png
integrations:
- description: GSA-administered government-wide IT accessibility program that implements Section 508 Standards and provides guidance and tools for federal agencies.
  name: Section508.gov
- description: Web Content Accessibility Guidelines developed by W3C, harmonized with Section 508 ICT Standards for web and software accessibility.
  name: WCAG
- description: European accessibility standard for ICT products and services, harmonized with Section 508 to facilitate international procurement.
  name: European EN 301 549
- description: Standards issued by the DOJ and DOT that incorporate Access Board ADA guidelines and apply them to specific regulated entities.
  name: ADA Standards for Accessible Design
jsonld:
- class_count: 5
  name: U S Access Board Context
  property_count: 21
  slug: u-s-access-board-context
layout: provider
modified: '2026-07-25'
name: U.S. Access Board
nav: Providers
network: true
overview: 'U.S. Access Board is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Accessibility, Disability, Standards, and Built Environment.


  The U.S. Access Board catalog on APIs.io includes 1 JSON-LD context.


  U.S. Access Board''s developer surface includes getting-started guide, engineering blog, and 8 more developer resources.'
plans:
- name: U S Access Board Plans Pricing
  plan_count: 3
  slug: u-s-access-board-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: U S Access Board Rate Limits
  slug: u-s-access-board-rate-limits
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 52.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 15.2
    contract_quality: 14.7
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 15.2
    operational_transparency: 10.5
  previous_composite: 20.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 27.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/u-s-access-board/refs/heads/main/screenshots/u-s-access-board-2026-06-20T195910.png
security:
- kind: domain-security
  name: U S Access Board Domain Security
  slug: u-s-access-board-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: u-s-access-board
tags:
- Federal-Government
- Accessibility
- Disability
- Standards
- Built Environment
- Transportation
use_cases:
- description: Federal agencies use Section 508 Standards to ensure that ICT they procure or develop is accessible to employees and members of the public with disabilities.
  name: Federal ICT Procurement
- description: Architects, builders, and facility managers use ADA and ABA Standards to design and construct accessible facilities.
  name: Building Accessibility Compliance
- description: Telecommunications manufacturers use Section 255 Guidelines to build accessible telecommunications equipment and customer premises equipment.
  name: Telecommunications Accessibility
- description: Transportation engineers and municipalities use PROWAG guidelines for designing accessible pedestrian facilities, including crosswalks, curb ramps, and shared-use paths.
  name: Public Right-of-Way Design
- description: Organizations attend Access Board training and webinars to learn how to implement accessibility requirements across built environments and technology systems.
  name: Accessibility Training
website: https://www.access-board.gov/
---
