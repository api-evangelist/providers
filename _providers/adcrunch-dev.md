---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 5
  name: Adcrunch Dev Agentic Access
  operation_count: 88
  slug: adcrunch-dev-agentic-access
  summary_line: 88 operations · 49 acting · 5 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: The ad groups of your advertisers. The providers use different words for one concept. Meta calls it an **ad set**. TikTok and Google Ads call it an **ad group**. Each row keeps the word of its provide
  name: AdCrunch Ad groups API
  slug: adcrunch-dev-ad-groups-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: The ads of your advertisers. Meta and TikTok call it an `ad`. Google Ads calls it an **`ad_group_ad`**. That is a link resource, and its id is the composite `{adGroupId}~{adId}`. Filter by `adGroupId`
  name: AdCrunch Ads API
  slug: adcrunch-dev-ads-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: The asset groups of your advertisers. Performance Max’s delivery container, and Google Ads only. A Performance Max campaign has no ad groups and no ads — the asset group holds what its automation asse
  name: AdCrunch Asset groups API
  slug: adcrunch-dev-asset-groups-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: An organization's source media. Reserve an upload, transfer the bytes directly to storage, then read the Asset — which is where what actually landed is validated.
  name: AdCrunch Assets API
  slug: adcrunch-dev-assets-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'Your organization''s brand context: identity, voice, guidelines and messaging, written as markdown. A list gives you the name, the description, the logo and which of the four sections carry prose. Read'
  name: AdCrunch Brands API
  slug: adcrunch-dev-brands-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'What your organization intends to run, before it buys: on which channels, for whom, for how much, and over what period. **A Campaign Plan is not a provider campaign.** It belongs to AdCrunch, and it c'
  name: AdCrunch Campaign Plans API
  slug: adcrunch-dev-campaign-plans-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: The campaigns of your advertisers. Every provider calls a campaign `campaign`. This tag holds the live reads and the changes of one advertiser. For the stored list of every advertiser of your organiza
  name: AdCrunch Campaigns API
  slug: adcrunch-dev-campaigns-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'The creatives of your advertisers. A provider assembles a creative for an ad: the image or video, the headline, the body copy and the call to action. A Creative belongs to the **account**. Meta is the'
  name: AdCrunch Creatives API
  slug: adcrunch-dev-creatives-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'The Meta Custom Audiences of an ad account: the groups of people that an ad set can include or exclude. A Custom Audience is configuration of the ad account, not an entity: it has no Insight, and AdCr'
  name: AdCrunch Custom audiences API
  slug: adcrunch-dev-custom-audiences-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'The custom conversions of an ad account. A custom conversion is configuration of the ad account, not an entity: it has no Insight, and AdCrunch stores none. An ad set can optimize for one custom conve'
  name: AdCrunch Custom conversions API
  slug: adcrunch-dev-custom-conversions-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'Files attached to a Brand, such as a logo or a guidelines PDF. The bytes do not go through this API: reserve the upload, send the bytes to the URL you get back, then finalize. A Document is reference '
  name: AdCrunch Documents API
  slug: adcrunch-dev-documents-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'Aggregated metrics for any level: advertiser, campaign, ad group or ad. The metrics include spend, impressions, clicks, reach and conversions. Group the rows into days, weeks or months, and break them'
  name: AdCrunch Insights API
  slug: adcrunch-dev-insights-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'The rows of a Campaign Plan. One Line Item is one thing you buy. It is coarser than an ad set: it holds the **envelope** of an intent, and it can produce more than one provider object. Therefore it ho'
  name: AdCrunch Line Items API
  slug: adcrunch-dev-line-items-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: Poll a Mutation that you started, and read the organization history. The route of each change sits under the tag of the object that it changes, beside the reads of that object. `POST /mutations` is de
  name: AdCrunch Mutations API
  slug: adcrunch-dev-mutations-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'The Facebook Pages that the Meta connection of an advertiser can advertise from. A Page is configuration of the connection, not an entity: it has no Insight, and AdCrunch stores none. Each creative na'
  name: AdCrunch Pages API
  slug: adcrunch-dev-pages-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: The audiences a Brand speaks **to**, described as people. A Persona belongs to one Brand only, and you address it through that Brand. Its handle is thus the pair of slugs, and two Brands can each hold
  name: AdCrunch Personas API
  slug: adcrunch-dev-personas-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'The Meta Pixels of an ad account. A Pixel is configuration of the ad account, not an entity: it has no Insight, and AdCrunch stores none. An ad set that optimizes for a conversion names one Pixel.'
  name: AdCrunch Pixels API
  slug: adcrunch-dev-pixels-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: Your organization's ad-ops playbooks. List them, read one, or write one. The slug is the handle an agent uses. You can also import a Catalog Skill from the Skill Catalog, the playbooks that AdCrunch w
  name: AdCrunch Skills API
  slug: adcrunch-dev-skills-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: The stored lists of campaigns, ad groups, ads, creatives and asset groups. A stored read answers from what the AdCrunch ingestion stored. It reads every advertiser of your organization in one request.
  name: AdCrunch Stored reads API
  slug: adcrunch-dev-stored-reads-api
- baseURL: https://api.adcrunch.dev
  baseurl_source: declared
  description: 'The Meta interests and job titles that an ad set can target. An option is configuration of Meta, not an entity: it has no Insight, and AdCrunch stores none. Search them by name, and send their ids whe'
  name: AdCrunch Targeting options API
  slug: adcrunch-dev-targeting-options-api
artifact_total: 30
common:
- group: agent
  href: https://artifacts.apis.io/adcrunch-dev/agentic-access/adcrunch-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adcrunch-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/adcrunch-dev/plans/adcrunch-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adcrunch-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adcrunch-dev/rules/adcrunch-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/adcrunch-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/adcrunch-dev/vocabulary/adcrunch-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adcrunch-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adcrunch-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/adcrunch-dev/authentication/adcrunch-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adcrunch-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/adcrunch-dev/errors/adcrunch-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adcrunch-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adcrunch-dev/conformance/adcrunch-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adcrunch-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adcrunch-dev/llms/adcrunch-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adcrunch-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/adcrunch-dev/mcp/adcrunch-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adcrunch-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adcrunch-dev/well-known/adcrunch-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adcrunch-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/adcrunch-dev/hosts/adcrunch-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adcrunch-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/adcrunch-dev/vendors/adcrunch-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adcrunch-dev-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adcrunchdev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adcrunch.dev/quickstart
- group: auth
  href: https://artifacts.apis.io/adcrunch-dev/security/adcrunch-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adcrunch-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adcrunch.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adcrunch.dev
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adcrunch.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.adcrunch.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://adcrunch.dev/pricing/
- group: company
  title: ''
  type: Blog
  url: https://adcrunch.dev/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adcrunch.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adcrunch.dev/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://sign.adcrunch.dev/login?mode=signup
created: '2026-10-31'
description: AdCrunch provides agentic media buying automation for Meta, TikTok, and Google Ads. It offers AI‑driven campaign management with real‑time guardrails, budgeting limits, and detailed activity logs. Users can set rules, monitor performance, and let the platform execute changes across ad accounts without writing code, while maintaining full audit trails and compliance.
image: https://adcrunch.dev/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.adcrunch.dev.
  name: AdCrunch MCP Server
  slug: adcrunch-dev-mcp-yml
modified: '2026-10-31'
name: AdCrunch
nav: Providers
network: true
overview: 'AdCrunch publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad groups API, Ads API, Asset groups API, and 17 more. Tagged areas include Advertising, Artificial Intelligence, Marketing, Automation, and Media Buying.


  The AdCrunch catalog on APIs.io includes 1 Spectral governance ruleset.


  AdCrunch''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Adcrunch Dev Plans Pricing
  plan_count: 2
  slug: adcrunch-dev-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: AdCrunch API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: adcrunch-dev-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 52.5
    developer_ergonomics: 33.9
    discoverability: 65.0
    operational_transparency: 2.6
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adcrunch Dev Authentication
  slug: adcrunch-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adcrunch Dev Domain Security
  slug: adcrunch-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 4
skills:
- name: adcrunch-dev-create-and-register-asset
  slug: adcrunch-dev-create-and-register-asset
- name: adcrunch-dev-create-campaign
  slug: adcrunch-dev-create-campaign
- name: adcrunch-dev-line-items-create-validate-record
  slug: adcrunch-dev-line-items-create-validate-record
- name: adcrunch-dev-manage-creatives
  slug: adcrunch-dev-manage-creatives
slug: adcrunch-dev
tags:
- Advertising
- Artificial Intelligence
- Marketing
- Automation
- Media Buying
website: https://adcrunch.dev/
---
