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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/verra-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://verra.org
- group: start
  title: ''
  type: Registry
  url: https://registry.verra.org
- group: other
  title: ''
  type: ProjectHub
  url: https://projecthub.verra.org
- group: other
  title: ''
  type: Programs
  url: https://verra.org/programs/
- group: other
  title: ''
  type: VerifiedCarbonStandard
  url: https://verra.org/programs/verified-carbon-standard/
- group: design
  title: ''
  type: VCSVersion5
  url: https://verra.org/programs/verified-carbon-standard/verified-carbon-standard-version-5/
- group: other
  title: ''
  type: JurisdictionalAndNestedREDD
  url: https://verra.org/programs/jurisdictional-and-nested-redd-framework/
- group: build
  title: ''
  type: ClimateCommunityAndBiodiversityStandards
  url: https://verra.org/programs/ccbs/
- group: other
  title: ''
  type: SustainableDevelopmentVerifiedImpactStandard
  url: https://verra.org/programs/sd-vista/
- group: other
  title: ''
  type: PlasticWasteReductionStandard
  url: https://verra.org/programs/plastic-waste-reduction-standard/
- group: auth
  title: ''
  type: Scope3Standard
  url: https://verra.org/programs/scope-3-standard/
- group: other
  title: ''
  type: Methodologies
  url: https://verra.org/methodologies-main/
- group: other
  title: ''
  type: ValidationVerification
  url: https://verra.org/validation-verification/
- group: other
  title: ''
  type: PublicConsultations
  url: https://verra.org/consultations/public-consultation/
- group: start
  title: ''
  type: RegistryUserGuide
  url: https://verra.org/wp-content/uploads/Verra-Registry-User-Guide.pdf
- group: company
  title: ''
  type: News
  url: https://verra.org/news/
- group: operate
  title: ''
  type: Contact
  url: https://verra.org/contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/verra-co
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/verra_standards
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@verrastandards
- group: company
  title: ''
  type: Blog
  url: https://verra.org/news/feed/
created: '2026-05-25'
description: Verra is a Washington, D.C.-based nonprofit standards body that develops and manages the world's leading certification programs for climate action and sustainable development. Its flagship program, the Verified Carbon Standard (VCS), is the most widely used voluntary greenhouse gas crediting program globally, with more than 2,579 registered projects across 132+ countries and over 1.3 billion Verified Carbon Units (VCUs) issued. Verra also operates the Climate, Community & Biodiversity Standards (CCB), the Sustainable Development Verified Impact Standard (SD VISta), the Plastic Waste Reduction Standard (PWRP), the Scope 3 Standard Program, and the Jurisdictional and Nested REDD+ (JNR) framework. The Verra Registry at registry.verra.org is the system of record for projects, methodologies, issuances, retirements, and the AFOLU pooled buffer account across these programs; project documentation, public comment periods, and credit-lifecycle records are all surfaced through that registry.
  Verra recently launched VCS Version 5, modernizing program operations, strengthening safeguards, and clarifying credit rights. Verra does not publish a public developer API, OpenAPI specification, SDK, or GitHub organization; programmatic data access is limited to the registry's web interface and filtered report exports, and there is no open-source code or machine-readable spec catalog associated with the organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verra-org.png
layout: provider
modified: '2026-05-25'
name: Verra
nav: Providers
network: true
overview: 'Verra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Carbon, Carbon Credits, Carbon Markets, Voluntary Carbon Market, and Carbon Registry.


  Verra''s developer surface includes product news, YouTube channel, engineering blog, and 19 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verra-org/refs/heads/main/screenshots/verra-org-2026-06-20T200945.png
security:
- kind: domain-security
  name: Verra Org Domain Security
  slug: verra-org-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verra-org
tags:
- Carbon
- Carbon Credits
- Carbon Markets
- Voluntary Carbon Market
- Carbon Registry
- Climate
- Climate Action
- Greenhouse Gas
- Emissions Reduction
- Offsets
- Sustainability
- Sustainable Development
- REDD Plus
- Forestry
- AFOLU
- Nature-Based Solutions
- Plastic Waste
- Standards
- Certification
- Non-Profit
website: https://verra.org
---
