---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/askthegrid-com/plans/askthegrid-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askthegrid-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/askthegrid-com/changelog/askthegrid-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/askthegrid-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/askthegrid-com/llms/askthegrid-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/askthegrid-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/askthegrid-com/well-known/askthegrid-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/askthegrid-com-security.txt
- group: agent
  href: https://artifacts.apis.io/askthegrid-com/well-known/askthegrid-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askthegrid-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/askthegrid-com/hosts/askthegrid-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askthegrid-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/askthegrid-com/vendors/askthegrid-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/askthegrid-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askthegrid.com/terms
- group: operate
  title: ''
  type: Support
  url: https://askthegrid.com/help
- group: auth
  title: ''
  type: Security
  url: https://askthegrid.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askthegrid.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://askthegrid.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://static.askthegrid.com/media/demos/homepage/understand.mp4
- group: start
  title: ''
  type: Login
  url: https://askthegrid.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://askthegrid.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://askthegrid.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://askthegrid.com/blog
- group: auth
  href: https://artifacts.apis.io/askthegrid-com/security/askthegrid-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/askthegrid-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/askthegrid-com/security/askthegrid-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askthegrid-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://askthegrid.com/
coverage:
  checked: '2026-11-02'
  detail: Documentation page https://askthegrid.com/developers/console/docs returns a Cloudflare bot challenge, preventing machine‑readable access.
  evidence:
  - status: 403
    url: https://askthegrid.com/developers/console/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-01'
description: Ask the Grid provides a live power grid map for the US, Canada, and Mexico, offering real‑time data on prices, transmission, outages, and weather across markets. Users can query the platform in plain English to receive sourced answers, set up radar alerts for assets or collections, and access detailed reports and briefings. The service aggregates data from utilities, ISOs, RTOs, data centers, and other grid operators, delivering comprehensive insights for traders, utilities, and large energy consumers.
image: https://askthegrid.com/og/card?title=Ask+the+Grid&description=AI+platform+for+power+and+energy+professionals%3A+live+maps+of+BC+Hydro%2C+Manitoba+Hydro%2C+SaskPower+and+22+more+North+American+grids%2C+an+agent+that+explains+why%2C+and+price+forecasts.&path=askthegrid.com&image=%2Fsite%2Fproduct%2Fagent-source-citations.jpg&fit=contain
layout: provider
modified: '2026-11-01'
name: Ask the Grid
nav: Providers
network: true
overview: 'Ask the Grid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Data, Mapping, Real-Time, and Analytics.


  Ask the Grid''s developer surface includes changelog, support, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Askthegrid Com Plans Pricing
  plan_count: 2
  slug: askthegrid-com-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 49.1
    operational_transparency: 13.2
  previous_composite: 26.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Askthegrid Com Domain Security
  slug: askthegrid-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Askthegrid Com Vulnerability Disclosure
  slug: askthegrid-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: askthegrid-com
tags:
- Energy
- Data
- Mapping
- Real-Time
- Analytics
website: https://askthegrid.com/
---
