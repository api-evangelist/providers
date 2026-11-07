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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Community-maintained, reverse-engineered Python library for communicating with Lennox S30, S40, E30, and M30 climate controls via the Lennox cloud or local LAN. Powers the popular Home Assistant integ
  name: Lennox S30 Community API
  slug: lennox-s30-community-api
- description: TypeScript port of the community Python library for controlling Lennox S30, S40, E30, and M30 thermostats over a local LAN connection. No cloud required.
  name: lennoxapi (TypeScript)
  slug: lennoxapi-typescript
- description: Official partner integrations for the Lennox iComfort S30, E30, and M30 smart thermostats. Connectivity is provided through Control4, Amazon Alexa, Apple HomeKit, Google Assistant, and IFTTT rather th
  name: Lennox iComfort Smart Home Integrations
  slug: lennox-icomfort-smart-home-integrations
artifact_total: 7
common:
- group: other
  href: https://artifacts.apis.io/lennox-international/hosts/lennox-international-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lennox-international-hosts.yml
- group: build
  href: https://artifacts.apis.io/lennox-international/integrations/lennox-international-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/lennox-international-integration-edges.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.lennox.com/residential/media-room/news/
- group: commercial
  href: https://artifacts.apis.io/lennox-international/plans/lennox-international-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lennox-international-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lennox-international/rate-limits/lennox-international-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lennox-international-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lennox-international/finops/lennox-international-finops.yml
  title: ''
  type: FinOps
  url: finops/lennox-international-finops.yml
- group: auth
  href: https://artifacts.apis.io/lennox-international/security/lennox-international-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lennox-international-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lennox-international
- group: company
  title: ''
  type: Website
  url: https://www.lennox.com/
- group: company
  title: ''
  type: Website
  url: https://www.lennoxinternational.com/
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.lennoxpros.com/
- group: operate
  title: ''
  type: Support
  url: https://www.support.lennoxicomfort.com/
- group: company
  title: ''
  type: Blog
  url: https://www.lennox.com/commercial/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lennox.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lennox.com/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://www.lennox.com/residential/owners/register-and-review/
coverage:
  checked: '2026-10-20'
  detail: Lennox publishes no developer portal or API contract; api.lennox.com, api.lennoxpros.com and api.lennoxicomfort.com returned no OpenAPI/GraphQL/MCP surface, and iComfort access exists only through partner smart-home integrations and community reverse-engineered libraries.
  evidence:
  - status: 200
    url: https://www.lennox.com/
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: Lennox International is a global leader in the heating, air conditioning, and refrigeration markets, providing climate control solutions for residential and commercial applications. Lennox does not publish a general developer portal for HVAC system access. Smart-home integrations with the iComfort S30, E30, and M30 thermostat product lines are delivered through partnerships (Control4, Amazon Alexa, Apple HomeKit, Google Assistant, IFTTT) and through community-maintained, reverse-engineered Python and TypeScript libraries.
finops:
- has_sources: false
  method: generated
  name: Lennox International Finops
  primary_unit: request
  service_category: API
  slug: lennox-international-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lennox-international.png
layout: provider
modified: '2026-07-25'
name: Lennox International
nav: Providers
network: true
overview: 'Lennox International is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include HVAC, Smart Home, Thermostat, IoT, and Climate Control.


  Lennox International''s developer surface includes support, engineering blog, signup flow, and 13 more developer resources.'
plans:
- name: Lennox International Plans Pricing
  plan_count: 3
  slug: lennox-international-plans-pricing
press:
- date: ''
  title: Lennox Reaffirms 2026 Guidance and Announces 2030 ...
  url: https://investor.lennox.com/news-releases/news-release-details/lennox-reaffirms-2026-guidance-and-announces-2030-long-term
- date: ''
  title: Lennox Invests in AI Agents to Enhance Technician ...
  url: https://www.prnewswire.com/news-releases/lennox-invests-in-ai-agents-to-enhance-technician-support-and-customer-experience-302552797.html
- date: ''
  title: Lennox Reports First Quarter Results
  url: https://investor.lennox.com/news-releases/news-release-details/lennox-reports-first-quarter-results
- date: ''
  title: Lennox Reports Second Quarter Results
  url: https://investor.lennox.com/news-releases/news-release-details/lennox-reports-second-quarter-results
- date: ''
  title: Lennox International Inc. Profile
  url: https://www.bccresearch.com/company-index/profile/lennox-international-inc?srsltid=AfmBOorRBARnkkRZj2UsZOk6uoXXDrepIdMjx4-APHTr8IL-wATR43Ah
random_paper: 17
rate_limits:
- limit_count: 5
  name: Lennox International Rate Limits
  slug: lennox-international-rate-limits
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 63.4
    operational_transparency: 13.2
  previous_composite: 19.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lennox-international/lennox-international-2026-06-20T184421.png
security:
- kind: domain-security
  name: Lennox International Domain Security
  slug: lennox-international-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lennox-international
tags:
- HVAC
- Smart Home
- Thermostat
- IoT
- Climate Control
- Fortune 1000
website: https://www.lennox.com/
---
