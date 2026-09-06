---
access_model:
  confidence: high
  label: No public API; commercial engagement is bilateral through affiliate or ad sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - https://www.amcglobalmedia.com/
  - https://connect.amcglobalmedia.com/
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
api_count: 1
apis:
- description: AMC Global Media delivers entertainment content through cable networks, FAST channels and subscription streaming platforms. There is no public API, developer portal or machine-readable contract. Affil
  name: AMC Global Media
  slug: amc-networks
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amc-networks-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amc-networks-llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amc-networks-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amc-networks-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/amc-networks-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.amcglobalmedia.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amc-global-media
- group: company
  title: ''
  type: Website
  url: https://www.amcglobalmedia.com/
- group: start
  title: ''
  type: AffiliatePortal
  url: https://affiliate.amcnetworks.com/
- group: operate
  title: ''
  type: Support
  url: https://www.amcglobalmedia.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amcglobalmedia.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amcglobalmedia.com/privacy-policy/
coverage:
  checked: '2026-09-02'
  detail: AMC Global Media's full public page inventory was walked from its WordPress sitemap and contains no developer, API or documentation page at all; the only JSON served on an AMC host is the incidental WordPress REST root at /wp-json/, and every /openapi.json, /swagger.json and /.well-known/ path 404s on www.amcglobalmedia.com, www.amcnetworks.com and affiliate.amcnetworks.com.
  evidence:
  - status: 200
    url: https://amcglobalmedia.com/sitemap.xml
  - status: 404
    url: https://www.amcglobalmedia.com/openapi.json
  - status: 404
    url: https://www.amcglobalmedia.com/.well-known/api-catalog
  - status: 404
    url: https://affiliate.amcnetworks.com/openapi.json
  - status: 404
    url: https://www.amcglobalmedia.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-03-23'
description: 'AMC Global Media Inc. (NASDAQ: AMCX), known as AMC Networks until its 2026 rebrand, is a global entertainment company that owns and operates AMC, BBC America, IFC, SundanceTV and We TV, the AMC+, Acorn TV, Shudder, Sundance Now, HIDIVE and ALLBLK streaming services, AMC Studios, IFC Films and AMC Networks International. It distributes 33 FAST channels across 22 platforms and sells advertising through its Audience+ audience data platform and AMCN Outcomes measurement product. The company publishes no public developer program and no machine-readable API contract: affiliate distribution runs through a login-gated partner portal, advertising is booked through sales, and broadcast delivery is contracted through its Broadcasting & Technology group. The legacy domain www.amcnetworks.com now redirects to www.amcglobalmedia.com.'
features:
- description: Proprietary data platform for creating audience segments and reaching viewers across linear and streaming properties with targeted advertising. Accessed through AMC ad sales, not through a self-serve API.
  name: Audience+ Data Platform
- description: Outcome-based advertising measurement product enabling brands to gauge consumer response to ad spending across AMC Global Media properties.
  name: AMCN Outcomes
- description: 33 free ad-supported streaming television channels distributed across 22 platforms, providing digital advertising inventory.
  name: FAST Channels
- description: AMC+, Acorn TV, Shudder, Sundance Now, HIDIVE and ALLBLK subscription streaming services. HIDIVE runs on the third-party DICE platform (dce-frontoffice.imggaming.com), so its runtime API belongs to that vendor rather than to AMC.
  name: Streaming Services
- description: Login-gated partner portal providing marketing materials, key art, promotional videos, social toolkits, legal certifications, and technical launch documents for cable and streaming distribution partners.
  name: Affiliate Portal
- description: Program origination, encoding, satellite uplinking and studio production for AMC and third-party networks; transmission requests are handled through a credentialed operations portal, not an API.
  name: Broadcasting and Technology Services
- description: AI-powered content indexing of AMC's original content library enabling contextual ad placement adjacent to relevant scenes.
  name: Contextual AI Advertising
finops:
- name: Amc Networks Finops
  service_category: Media & Entertainment
  slug: amc-networks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amc-networks.png
integrations:
- description: Expanded global streaming licensing relationship announced with AMC's Q2 2026 results, bringing AMC titles to Netflix.
  name: Netflix
- description: AMC expanded its advertising initiative to theatrical moviegoing via a partnership with Fandango.
  name: Fandango
- description: AI partnership with Runway for content creation and advertising enhancement capabilities.
  name: Runway
- description: HIDIVE's streaming delivery runs on the third-party DICE platform, a vendor-operated surface rather than an AMC-published API.
  name: DICE (IMG Arena)
layout: provider
modified: '2026-09-02'
name: AMC Global Media
nav: Providers
network: true
overview: 'AMC Global Media publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Entertainment, Streaming, Cable Television, Advertising, and Media.


  AMC Global Media''s developer surface includes engineering blog, support, and 10 more developer resources.'
plans:
- name: Amc Networks Plans Pricing
  plan_count: 0
  slug: amc-networks-plans-pricing
press:
- date: '2026-05-25'
  title: AMC Networks enlists AI startup
  url: https://www.linkedin.com/news/story/amc-networks-enlists-ai-startup-6889537/
- date: '2026-05-25'
  title: 'PRISM - AMC Networks Success Story: Adopting GenAI to ...'
  url: https://www.nabshow.com/video/prism-amc-networks-success-story-adopting-genai-to-streamline-workflow/
- date: '2026-05-25'
  title: AMC Networks Partners with Runway to Use AI for Content ...
  url: https://ottverse.com/amc-networks-partners-with-runway-to-use-ai-for-content-and-marketing/
- date: '2026-05-25'
  title: AMC Networks partners with Runway AI for video generation
  url: https://www.facebook.com/groups/glblfilmmakers/posts/10161468723473424/
- date: '2026-05-25'
  title: As AMC Networks Embraces AI, CEO Kristin Dolan ...
  url: https://deadline.com/2025/08/amc-networks-embraces-ai-ceo-kristin-dolan-technology-ip-1236482175/
random_paper: 4
rate_limits:
- limit_count: 0
  name: Amc Networks Rate Limits
  slug: amc-networks-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amc-networks/refs/heads/main/screenshots/amc-networks-2026-06-20T171857.png
security:
- kind: domain-security
  name: Amc Networks Domain Security
  slug: amc-networks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amc-networks
tags:
- Entertainment
- Streaming
- Cable Television
- Advertising
- Media
- FAST Channels
- Broadcasting
- Content Licensing
- Fortune 1000
use_cases:
- description: Distributors access marketing and technical resources for AMC channel launches and affiliate partnerships through the gated affiliate portal.
  name: Cable and Streaming Affiliate Distribution
- description: Advertisers reach audiences across AMC's linear, FAST and streaming properties using Audience+ targeting and AMCN Outcomes measurement.
  name: Digital Advertising
- description: Platforms and international broadcasters license AMC Studios and AMC Networks International content and FAST channel feeds.
  name: Content Licensing and Streaming Distribution
website: https://www.amcglobalmedia.com/
---
