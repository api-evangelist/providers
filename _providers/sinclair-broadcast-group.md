---
access_model:
  confidence: high
  label: Open / No Registration
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://sbgi.net/wp-json/wp/v2/posts?per_page=1
  - https://sbgi.net/wp-json/sbg/v1/station-map
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'The public WordPress REST API (wp-json) of the Sinclair, Inc. website at sbgi.net: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Sinclair, Inc. Website (WordPress REST)
  slug: sbgi-net-website-wordpress-rest
artifact_total: 33
common:
- group: company
  title: ''
  type: Website
  url: https://www.sbgi.net/
- group: other
  href: https://artifacts.apis.io/sinclair-broadcast-group/capabilities/sinclair-broadcast-group-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sinclair-broadcast-group-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sinclair-broadcast-group/mcp/sinclair-broadcast-group-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sinclair-broadcast-group-mcp.yml
- group: auth
  href: https://artifacts.apis.io/sinclair-broadcast-group/security/sinclair-broadcast-group-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sinclair-broadcast-group-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sinclair-broadcast-group/security/sinclair-broadcast-group-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/sinclair-broadcast-group-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sinclair-broadcast-group/security/sinclair-broadcast-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sinclair-broadcast-group-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/sinclair-broadcast-group/well-known/sinclair-broadcast-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sinclair-broadcast-group-well-known.yml
- group: auth
  href: https://artifacts.apis.io/sinclair-broadcast-group/well-known/sinclair-broadcast-group-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sinclair-broadcast-group-security.txt
- group: agent
  href: https://artifacts.apis.io/sinclair-broadcast-group/llms/sinclair-broadcast-group-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sinclair-broadcast-group-llms.txt
- group: agent
  href: https://artifacts.apis.io/sinclair-broadcast-group/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/sinclair-broadcast-group/packages/sinclair-broadcast-group-packages.yml
  title: ''
  type: Packages
  url: packages/sinclair-broadcast-group-packages.yml
- group: commercial
  href: https://artifacts.apis.io/sinclair-broadcast-group/plans/sinclair-broadcast-group-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sinclair-broadcast-group-plans-pricing.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sbgi.net/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sbgi.net/terms-conditions/
- group: operate
  title: ''
  type: Support
  url: https://sbgi.net/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://sbgi.net/feed/
- group: start
  title: ''
  type: Portal
  url: https://sbgi.net
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SinclairBroadcastGroup
- group: company
  title: ''
  type: InvestorRelations
  url: https://sbgi.net/investor-relations/
- group: auth
  href: https://artifacts.apis.io/sinclair-broadcast-group/authentication/sinclair-broadcast-group-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sinclair-broadcast-group-authentication.yml
- group: design
  href: https://artifacts.apis.io/sinclair-broadcast-group/conventions/sinclair-broadcast-group-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sinclair-broadcast-group-conventions.yml
- group: design
  href: https://artifacts.apis.io/sinclair-broadcast-group/errors/sinclair-broadcast-group-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sinclair-broadcast-group-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sinclair-broadcast-group/data-model/sinclair-broadcast-group-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sinclair-broadcast-group-data-model.yml
- group: operate
  href: https://artifacts.apis.io/sinclair-broadcast-group/rate-limits/sinclair-broadcast-group-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sinclair-broadcast-group-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/sinclair-broadcast-group/conformance/sinclair-broadcast-group-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sinclair-broadcast-group-conformance.yml
- group: design
  href: https://artifacts.apis.io/sinclair-broadcast-group/lifecycle/sinclair-broadcast-group-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sinclair-broadcast-group-lifecycle.yml
created: '2026-05-05'
description: 'Sinclair, Inc. (Nasdaq: SBGI), formerly Sinclair Broadcast Group, is a diversified media company and one of the largest U.S. local television broadcasters. The company operates 177-185+ TV stations across roughly 79-86 markets affiliated with all major broadcast networks (Fox, NBC, CBS, ABC, MyNetworkTV, The CW), owns Tennis Channel, holds a stake in YES Network, and runs digital multicast networks Comet, Charge!, Roar, and The Nest. Sinclair Ventures houses the company''s non-broadcast operations, including ad/martech units (AMP, Drive Auto, Free State, Digital Remedy/Compulse) and broadcast technology subsidiaries (Dielectric, ONE Media Technologies, Bitpath, CAST.ERA, Broadspan Wireless). In 2019 Sinclair acquired the Fox Sports regional sports networks for ~$9.6 billion through a Diamond Sports Group joint venture; Diamond was rebranded Bally Sports in 2021, filed Chapter 11 in March 2023, exited bankruptcy in January 2025 as Main Street Sports Group, rebranded again as
  FanDuel Sports Network, and is winding down operations in mid-2026. Sinclair runs no developer program and publishes no API documentation, but its corporate site at sbgi.net serves a live, public, unauthenticated WordPress REST API whose first-party sbg/v1 namespace publishes the company''s full television station footprint — 197 primary stations and 365 digital subchannels across 87 Nielsen DMAs, with network affiliation, market rank and O&O/JSA/LMA/MSA ownership status attached to every call sign — alongside 1,753 press releases and the regional sports network territories.'
features:
- description: Operates roughly 177-185 owned-and-operated and affiliate-managed local television stations across ~79-100 U.S. markets, reaching roughly 40% of U.S. households with local news, weather, and sports.
  name: Local Broadcast Footprint
- description: Largest owner of stations affiliated with Fox, NBC, CBS, ABC, MyNetworkTV, The CW, and The CW Plus.
  name: Network Affiliations
- description: 'Owns and programs four free over-the-air digital networks: Comet (sci-fi), Charge! (action/police), Roar (comedy), and The Nest (true crime / lifestyle, launched October 2023 in the slot vacated by Stadium).'
  name: Digital Multicast Networks
- description: 24/7 multi-platform tennis cable and streaming network, acquired in March 2016 for $350M; ~38M U.S. pay-TV households as of late 2023. Includes T2 FAST channel, Pickleball.tv (with the United Pickleball Association), and a Tennis Channel direct-to-consumer subscription launched November 2024.
  name: Tennis Channel
- description: Centrally produced national news (The National Desk) and Sharyl Attkisson's investigative program Full Measure distributed across the Sinclair station footprint.
  name: National Desk / Full Measure
- description: Through ONE Media Technologies, Dielectric, CAST.ERA, Bitpath, and Broadspan Wireless, Sinclair is a leading commercial driver of ATSC 3.0 deployment, dynamic ad insertion, datacasting, and broadcast-as-IP (B2X) infrastructure.
  name: NextGen TV / ATSC 3.0
- description: AMP Sales & Marketing Solutions sells across TV, digital, audio, social, and streaming inventory. Vertical units include Drive Auto (automotive) and Free State (government).
  name: Multi-Platform Advertising
- description: Compulse (rebranded as Digital Remedy in 2024-2025) offers OTT, programmatic, and managed-services martech for SMBs and agencies; the Compulse 360 SaaS platform continues under the Digital Remedy brand.
  name: Marketing Technology Services
- description: Through the spun-off Diamond Sports Group (now Main Street Sports Group), Sinclair previously controlled the largest RSN footprint in North America under the Fox Sports / Bally Sports / FanDuel Sports Network brands.
  name: Regional Sports Networks (Legacy)
integrations:
- description: Carriage / affiliation agreements with Fox, NBC, CBS, ABC, MyNetworkTV, The CW, and The CW Plus.
  name: Major Broadcast Networks
- description: Tennis Channel and the regional sports networks are distributed via national cable, satellite, and vMVPD operators (Comcast, Charter, DirecTV, Dish, YouTube TV, Fubo, etc.).
  name: Pay-TV Distributors
- description: October 2024 naming-rights agreement that rebranded the Bally Sports RSNs as the FanDuel Sports Network, with annual rights fees and an option for a post-bankruptcy equity stake.
  name: FanDuel
- description: Joint Pickleball.tv FAST channel operated with the UPA.
  name: United Pickleball Association
- description: ONE Media works with consumer-electronics OEMs, station groups, and standards bodies to commercialize NextGen TV.
  name: ATSC 3.0 Industry Partners
layout: provider
modified: '2026-08-12'
name: Sinclair
nav: Providers
network: true
overview: 'Sinclair publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Broadcasting, Television, Local News, Sports Media, and Regional Sports Networks.


  Sinclair''s developer surface includes support, engineering blog, developer portal, authentication, and 22 more developer resources.'
plans:
- name: Sinclair Broadcast Group Plans Pricing
  plan_count: 0
  slug: sinclair-broadcast-group-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Sinclair Broadcast Group Rate Limits
  slug: sinclair-broadcast-group-rate-limits
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 35.1
    discoverability: 60.7
    operational_transparency: 13.2
  previous_composite: 22.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/sinclair-broadcast-group/sinclair-broadcast-group-2026-06-20T193943.png
security:
- kind: authentication
  name: Sinclair Broadcast Group Authentication
  slug: sinclair-broadcast-group-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sinclair Broadcast Group Domain Security
  slug: sinclair-broadcast-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sinclair Broadcast Group Vulnerability Disclosure
  slug: sinclair-broadcast-group-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: sinclair-press-release-monitoring
  slug: sinclair-press-release-monitoring
- name: sinclair-station-footprint
  slug: sinclair-station-footprint
slug: sinclair-broadcast-group
solutions:
- description: Owned-and-operated local television stations and the associated local news, weather, and sports programming engine.
  name: Sinclair Broadcast Group
- description: Holding entity for non-broadcast operations, including Tennis Channel, the digital multicast networks, ad/martech, and broadcast technology subsidiaries.
  name: Sinclair Ventures
- description: Cable network, FAST channels (T2, Pickleball.tv), and DTC subscription product covering professional tennis, pickleball, and racquet-sports lifestyle programming.
  name: Tennis Channel
- description: Multi-platform local ad sales arm bundling Sinclair's broadcast, digital, OTT, social, and audio inventory for advertisers.
  name: AMP Sales & Marketing Solutions
- description: Managed services and SaaS martech (Compulse 360, OTT/CTV programmatic) for SMB advertisers and agencies.
  name: Compulse / Digital Remedy
- description: R&D and commercialization arm for ATSC 3.0 / NextGen TV, datacasting, B2X broadcast-as-IP, and dynamic ad insertion.
  name: ONE Media Technologies
- description: Long-standing manufacturer of broadcast transmitters, antennas, and RF systems, supplying U.S. and international broadcasters.
  name: Dielectric
tags:
- Broadcasting
- Television
- Local News
- Sports Media
- Regional Sports Networks
- Digital Marketing
- AdTech
- NextGen TV
- ATSC 3.0
- Media
use_cases:
- description: Producing and distributing daily local news, severe-weather coverage, and community programming across ~80 U.S. markets.
  name: Local News & Weather Delivery
- description: National tennis coverage via Tennis Channel and (legacy) local MLB / NBA / NHL coverage via the Bally Sports / FanDuel Sports Network RSNs and YES Network.
  name: Live Professional Sports
- description: Selling broadcast, digital, OTT, and connected-TV ad inventory to local SMBs, regional brands, automotive dealers, and political campaigns.
  name: Local & National Advertising
- description: Using ATSC 3.0 spectrum for targeted advertising, automotive telematics, public-safety datacasting, and broadcast-IP interoperability.
  name: Datacasting and NextGen TV Services
website: https://www.sbgi.net/
---
