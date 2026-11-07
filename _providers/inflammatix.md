---
access_model:
  confidence: low
  gated_conflict: 'x-api-posture: private but 2 published API entries'
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Inflammatix website at inflammatix.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate A'
  name: Inflammatix Website (WordPress REST)
  slug: inflammatix-com-website-wordpress-rest
- description: 'The public WordPress REST API (wp-json) of the Inflammatix website at support.inflammatix.com: the route index of the site''s content management system, catalogued as one site surface rather than as se'
  name: Inflammatix Website (WordPress REST)
  slug: support-inflammatix-com-website-wordpress-rest
artifact_total: 10
collections:
- collection_type: open
  name: Inflammatix Site Content API (WordPress REST)
  slug: open-inflammatix-content
- collection_type: open
  name: Inflammatix Support & Training Content API (WordPress REST)
  slug: open-inflammatix-support-content
common:
- group: other
  href: https://artifacts.apis.io/inflammatix/overlays/inflammatix-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/inflammatix-content-overlay.yaml
- group: other
  href: https://artifacts.apis.io/inflammatix/overlays/inflammatix-support-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/inflammatix-support-content-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/inflammatix/mcp/inflammatix-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/inflammatix-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://inflammatix.com/
- group: operate
  title: ''
  type: Support
  url: https://support.inflammatix.com/
- group: start
  title: ''
  type: Login
  url: https://support.inflammatix.com/login/
- group: company
  title: ''
  type: Blog
  url: https://inflammatix.com/newsroom/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://inflammatix.com/feed/
- group: operate
  title: ''
  type: PressReleases
  url: https://inflammatix.com/newsroom/press-releases/
- group: operate
  title: ''
  type: Roadmap
  url: https://inflammatix.com/pipeline/
- group: auth
  title: ''
  type: Compliance
  url: https://inflammatix.com/about-us/
- group: other
  title: ''
  type: Patents
  url: https://inflammatix.com/patents/
- group: other
  title: ''
  type: Research
  url: https://inflammatix.com/evidence/
- group: company
  title: ''
  type: Careers
  url: https://inflammatix.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://inflammatix.com/contact-inflammatix/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inflammatix.com/privacy-and-cookies-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inflammatix.com/terms-and-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inflammatix/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/inflammatix_stock/
- group: auth
  href: https://artifacts.apis.io/inflammatix/authentication/inflammatix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inflammatix-authentication.yml
- group: design
  href: https://artifacts.apis.io/inflammatix/conventions/inflammatix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/inflammatix-conventions.yml
- group: design
  href: https://artifacts.apis.io/inflammatix/errors/inflammatix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inflammatix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/inflammatix/data-model/inflammatix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inflammatix-data-model.yml
- group: design
  href: https://artifacts.apis.io/inflammatix/lifecycle/inflammatix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/inflammatix-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/inflammatix/conformance/inflammatix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inflammatix-conformance.yml
- group: auth
  href: https://artifacts.apis.io/inflammatix/security/inflammatix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inflammatix-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/inflammatix/llms/inflammatix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inflammatix-llms.txt
- group: agent
  href: https://artifacts.apis.io/inflammatix/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: Inflammatix is a molecular diagnostics company headquartered in Sunnyvale, California that reads the patient's own immune response to speed up decisions in emergency and critical care. Its FDA-cleared TriVerity Test System measures a 29-mRNA host-response panel from whole blood on the benchtop Myrna instrument using RT-LAMP, returning three machine-learning-derived scores — bacterial infection likelihood, viral infection likelihood, and risk of severe illness within seven days — in about 30 minutes, with under a minute of no-prep sample handling. The company was co-founded out of Stanford by Tim Sweeney and Purvesh Khatri, is backed by Khosla Ventures, Northpond Ventures, Think.Health Ventures, Iberis Capital, OSF HealthCare and Vesalius BioCapital plus federal funding from NIH, BARDA, DRIVe and DARPA, and holds ISO 13485:2016 certification and a State of California medical device manufacturing license. Inflammatix publishes no developer API for its clinical products; the Myrna
  instrument advertises "multiple LIS connectivity options" and remote notification, but no public interface specification. The machine-readable surfaces it does serve are the WordPress REST content APIs behind inflammatix.com and its customer support/training portal, which expose the company's peer-reviewed publication library and the TriVerity/Myrna course catalogue as JSON.
image: https://inflammatix.com/wp-content/uploads/2025/05/logo-revdark-850-1024x242.webp
layout: provider
modified: '2026-08-01'
name: Inflammatix
nav: Providers
network: true
overview: 'Inflammatix is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Diagnostics, and Medical Devices.


  The Inflammatix catalog on APIs.io includes 1 Spectral governance ruleset.


  Inflammatix''s developer surface includes support, engineering blog, authentication, and 25 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Inflammatix API Rules
  rule_count: 61
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 4
  slug: inflammatix-rules
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 78.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 35.5
    contract_governance: 31.8
    contract_quality: 1.7
    developer_ergonomics: 25.6
    discoverability: 65.2
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 26.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/inflammatix/inflammatix-2026-08-07T170701.png
security:
- kind: authentication
  name: Inflammatix Authentication
  slug: inflammatix-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inflammatix Domain Security
  slug: inflammatix-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Browse the Inflammatix clinical evidence library
  slug: inflammatix-browse-clinical-evidence
- name: List the TriVerity and Myrna training catalogue
  slug: inflammatix-list-training-catalogue
- name: Track the Inflammatix newsroom
  slug: inflammatix-track-newsroom
slug: inflammatix
tags:
- Company
- Health
- Healthcare
- Diagnostics
- Medical Devices
- In Vitro Diagnostics
- Molecular Diagnostics
- Sepsis
- Machine Learning
- Life Sciences
- Point of Care
- Content
website: https://inflammatix.com/
---
