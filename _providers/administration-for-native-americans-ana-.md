---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://www.acf.hhs.gov/ana'', ''status'': 301, ''note'': ''declared website redirects to https://acf.gov:443/ana — a different registrable domain (hhs.gov -> acf.gov), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 2
apis:
- description: The ANA Projects Report dataset provides results and impact analysis for ANA-funded projects in Native American communities. Available through the data.gov and healthdata.gov catalogs, the dataset inc
  name: ANA Projects Report Dataset
  slug: ana-projects-report
- description: Metadata-only catalog record in the HHS enterprise data inventory for the FY 2013 Congressional Report on the Social and Economic Conditions of Native Americans, published by the Administration for Ch
  name: FY 2013 Congressional Report on the Social and Economic Conditions of Native Americans
  slug: ana-fy2013-congressional-report
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/administration-for-native-americans-ana--domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/administration-for-native-americans-ana--conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/administration-for-native-americans-ana--lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/administration-for-native-americans-ana--llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/administration-for-native-americans-ana--plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/administration-for-native-americans-ana--rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://acf.gov/ana/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acf.gov/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/administration-for-native-americans
- group: company
  title: ''
  type: Website
  url: https://www.acf.hhs.gov/ana
- group: start
  title: ''
  type: Portal
  url: https://acf.gov/ana
- group: other
  title: ''
  type: Resources
  url: https://acf.gov/ana/resource-library
- group: operate
  title: ''
  type: Contact
  url: https://acf.gov/ana/about
coverage:
  checked: '2026-08-30'
  detail: ANA is a federal grant-making program office inside ACF/HHS with no software product and no developer surface; its entire machine-readable footprint is two Socrata metadata-only "href" records on healthdata.gov whose row API answers 403 "no row or column access to non-tabular tables", and the only distribution the flagship record advertises (www.acf.hhs.gov/ana/research) is itself a 404.
  evidence:
  - status: 403
    url: https://healthdata.gov/resource/c57a-jjpd.json
  - status: 404
    url: https://www.acf.hhs.gov/ana/research
  - status: 404
    url: https://catalog.data.gov/api/3/action/package_show?id=administration-for-native-americans-ana-projects-report
  - status: 404
    url: https://acf.gov/.well-known/api-catalog
  - status: 200
    url: https://healthdata.gov/data.json
  reason: not-a-software-company
  state: none
created: '2024-11-20'
description: 'The Administration for Native Americans (ANA) is an agency within the Administration for Children and Families (ACF), U.S. Department of Health and Human Services. ANA promotes self-sufficiency and cultural preservation for Native Americans, Alaska Natives, Native Hawaiians, and other Pacific Islander communities by providing social and economic development opportunities through financial assistance, training, and technical assistance. ANA administers a $45 million discretionary grant program in three primary areas: Social and Economic Development Strategies (SEDS), Native Language Preservation and Maintenance, and Environmental Regulatory Enhancement. ANA data on funded projects is publicly available through data.gov and healthdata.gov.'
features:
- description: Competitive financial assistance grants supporting locally determined projects designed to reduce community problems and achieve social and economic self-sufficiency goals in Native American communities.
  name: Social And Economic Development Strategies (SEDS) Grants
- description: Funding for projects that assess, plan, restore, and implement native language curricula to support community language preservation goals, including language nest and survival school programs.
  name: Native Language Preservation And Maintenance Grants
- description: Grants for immersive, site-based Native American language education programs for children, including language nest programs for young children and language survival schools.
  name: Esther Martinez Immersion (EMI) Grants
- description: Grants providing tribes with resources to develop legal, technical, and organizational capacities for protecting their natural environments and exercising environmental regulatory authority.
  name: Environmental Regulatory Enhancement Grants
- description: Capacity building support and technical assistance to Native American communities and tribal organizations to strengthen grant management and program implementation.
  name: Training And Technical Assistance
- description: ANA publishes grant outcome data and project reports as open data through data.gov and healthdata.gov under open licenses for public access and research use.
  name: Open Data Publication
finops:
- name: Administration For Native Americans Ana  Finops
  service_category: API
  slug: administration-for-native-americans-ana--finops
image: /assets/icons/administration-for-native-americans-ana-.png
layout: provider
modified: '2026-08-30'
name: Administration for Native Americans (ANA)
nav: Providers
network: true
overview: 'Administration for Native Americans (ANA) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Federal-Government, Indigenous, Native Americans, Grants, and Social Services.


  Administration for Native Americans (ANA)''s developer surface includes engineering blog, developer portal, and 11 more developer resources.'
plans:
- name: Administration For Native Americans Ana  Plans Pricing
  plan_count: 0
  slug: administration-for-native-americans-ana--plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Administration For Native Americans Ana  Rate Limits
  slug: administration-for-native-americans-ana--rate-limits
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 15.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/administration-for-native-americans-ana-/refs/heads/main/screenshots/administration-for-native-americans-ana--2026-06-20T164731.png
security:
- kind: domain-security
  name: Administration For Native Americans Ana  Domain Security
  slug: administration-for-native-americans-ana--domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: administration-for-native-americans-ana-
tags:
- Federal-Government
- Indigenous
- Native Americans
- Grants
- Social Services
- Language Preservation
- Open Data
use_cases:
- description: Tribal organizations and Native communities can review ANA project report data to learn from successful models for social and economic development initiatives when applying for ANA grants.
  name: Tribal Grant Research And Planning
- description: Researchers and language advocates can access ANA program data on language preservation projects to analyze the effectiveness of immersion and curriculum-based approaches to language revitalization.
  name: Native Language Revitalization Research
- description: Federal and state policymakers and advocacy organizations can use ANA project outcome data to evaluate the effectiveness of grant programs in improving conditions in Native American communities.
  name: Policy Impact Analysis
- description: Tribal governments and community organizations can reference ANA SEDS grant data to identify successful models for economic self-sufficiency initiatives in Native communities.
  name: Community Economic Development Planning
- description: Environmental researchers and tribal environmental programs can use ANA data to understand the scope and effectiveness of tribal environmental regulatory capacity building efforts.
  name: Environmental Justice Research
website: https://www.acf.hhs.gov/ana
---
