---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://sms.cresclab.com/api
  baseurl_source: declared
  description: Bulk (1-to-many) SMS. Small batches dispatch inline; >30 recipients queue asynchronously.
  name: Crescendo Lab Broadcast API
  slug: crescendo-lab-broadcast-api
- baseURL: https://sms.cresclab.com/api
  baseurl_source: declared
  description: Address book with NCC-consent tracking.
  name: Crescendo Lab Contacts API
  slug: crescendo-lab-contacts-api
- baseURL: https://sms.cresclab.com/api
  baseurl_source: declared
  description: Transactional (1-to-1) SMS send + status.
  name: Crescendo Lab SMS API
  slug: crescendo-lab-sms-api
- baseURL: https://sms.cresclab.com/api
  baseurl_source: declared
  description: Cost-attribution teams. Tag sends with a team to see which team sent/spent how much (shared wallet — reporting only, not a wallet split).
  name: Crescendo Lab Teams API
  slug: crescendo-lab-teams-api
- baseURL: https://sms.cresclab.com/api
  baseurl_source: declared
  description: The MAAC Go API API from Crescendo Lab — 0 operation(s) for maac go api.
  name: Crescendo Lab MAAC Go API
  slug: crescendo-lab-maac-go-api-api
artifact_total: 21
asyncapis:
- description: ''
  name: Crescendo Lab Maacgo Webhooks
  slug: crescendo-lab-maacgo-webhooks
collections:
- collection_type: open
  name: MAAC Go Broadcast API
  slug: open-crescendo-lab-broadcast-api
- collection_type: open
  name: MAAC Go Broadcast Contacts API
  slug: open-crescendo-lab-contacts-api
- collection_type: open
  name: MAAC Go Broadcast SMS API
  slug: open-crescendo-lab-sms-api
- collection_type: open
  name: MAAC Go Broadcast Teams API
  slug: open-crescendo-lab-teams-api
common:
- group: other
  href: https://artifacts.apis.io/crescendo-lab/capabilities/crescendo-lab-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/crescendo-lab-capability-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.cresclab.com/zh-tw/rss.xml
- group: other
  href: https://artifacts.apis.io/crescendo-lab/overlays/crescendo-lab-maacgo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crescendo-lab-maacgo-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://cresclab.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sms.cresclab.com/developers.html
- group: docs
  title: ''
  type: Documentation
  url: https://sms.cresclab.com/developers.html#api
- group: company
  title: ''
  type: Blog
  url: https://blog.cresclab.com/zh-tw
- group: operate
  title: ''
  type: HelpCenter
  url: https://crescendolab.zendesk.com/hc/zh-tw
- group: commercial
  title: ''
  type: Pricing
  url: https://cresclab.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sms.cresclab.com/signup.html
- group: start
  title: ''
  type: Login
  url: https://sms.cresclab.com/app.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sms.cresclab.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sms.cresclab.com/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Crescendo-Lab
- group: agent
  href: https://artifacts.apis.io/crescendo-lab/llms/crescendo-lab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crescendo-lab-llms.txt
- group: build
  href: https://artifacts.apis.io/crescendo-lab/packages/crescendo-lab-packages.yml
  title: ''
  type: SDKs
  url: packages/crescendo-lab-packages.yml
- group: build
  href: https://artifacts.apis.io/crescendo-lab/packages/crescendo-lab-packages.yml
  title: ''
  type: Packages
  url: packages/crescendo-lab-packages.yml
- group: build
  href: https://artifacts.apis.io/crescendo-lab/cli/crescendo-lab-cli.yml
  title: ''
  type: CLI
  url: cli/crescendo-lab-cli.yml
- group: agent
  href: https://artifacts.apis.io/crescendo-lab/mcp/crescendo-lab-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crescendo-lab-mcp.yml
- group: build
  href: https://artifacts.apis.io/crescendo-lab/mcp/crescendo-lab-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/crescendo-lab-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/crescendo-lab/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/crescendo-lab/plans/crescendo-lab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crescendo-lab-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/crescendo-lab/rate-limits/crescendo-lab-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crescendo-lab-rate-limits.yml
- group: docs
  title: ''
  type: APIReference
  url: https://sms.cresclab.com/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://sms.cresclab.com/developers.html
- group: start
  href: https://artifacts.apis.io/crescendo-lab/sandbox/crescendo-lab-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/crescendo-lab-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/crescendo-lab/authentication/crescendo-lab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crescendo-lab-authentication.yml
- group: design
  href: https://artifacts.apis.io/crescendo-lab/conventions/crescendo-lab-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crescendo-lab-conventions.yml
- group: design
  href: https://artifacts.apis.io/crescendo-lab/conventions/crescendo-lab-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/crescendo-lab-conventions.yml
- group: auth
  href: https://artifacts.apis.io/crescendo-lab/security/crescendo-lab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crescendo-lab-domain-security.yml
created: '2026-07-17'
description: Crescendo Lab is a Taiwan-based, Asia-leading AI omnichannel customer communication software company (cresclab.com) serving 800+ global brands, and a LINE Biz-Solutions Gold Partner. Its platform spans MAAC (AI marketing automation), CAAC (conversational applications), and DAAC (data intelligence) across LINE, WhatsApp, SMS, email, and social channels. Its developer-facing surface is MAAC Go (sms.cresclab.com) — a self-serve, NCC-compliant Taiwan SMS API with a published OpenAPI spec, first-party Node/Python SDKs, a CLI, an official MCP server, and delivery webhooks. Surfaced as a 500 Global portfolio company and enriched into the API Evangelist network.
finops:
- has_sources: true
  method: derived
  name: Crescendo Lab Finops
  primary_unit: sms segment
  service_category: ''
  slug: crescendo-lab-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crescendo-lab.png
layout: provider
mcp_servers:
- description: Official hosted + local MCP server for MAAC Go (Crescendo Lab's self-serve Taiwan SMS platform). Lets Claude / Cursor / Windsurf / Codex send SMS, run broadcasts, pull logs, and check wallet balance o
  name: MAAC Go MCP
  slug: maac-go-mcp
modified: '2026-10-06'
name: Crescendo Lab
nav: Providers
network: true
overview: 'Crescendo Lab publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Broadcast API, Contacts API, SMS API, and 2 more. Tagged areas include Company, SMS, Messaging, Marketing Automation, and Customer Engagement.


  The Crescendo Lab catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crescendo Lab''s developer surface includes documentation, engineering blog, pricing, signup flow, CLI, API reference, getting-started guide, and 23 more developer resources.'
plans:
- name: Crescendo Lab Plans Pricing
  plan_count: 8
  slug: crescendo-lab-plans-pricing
- name: Crescendo Lab Price Estimates
  plan_count: 0
  slug: crescendo-lab-price-estimates
random_paper: 2
rate_limits:
- limit_count: 2
  name: Crescendo Lab Rate Limits
  slug: crescendo-lab-rate-limits
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 80.4
    discoverability: 65.0
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 56.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/crescendo-lab/crescendo-lab-2026-07-25T210727.png
security:
- kind: authentication
  name: Crescendo Lab Authentication
  slug: crescendo-lab-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crescendo Lab Domain Security
  slug: crescendo-lab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: send-broadcast-campaign
  slug: crescendo-lab-broadcast
- name: manage-contacts
  slug: crescendo-lab-manage-contacts
- name: send-transactional-sms
  slug: crescendo-lab-send-sms
- name: attribute-sms-cost-by-team
  slug: crescendo-lab-team-cost-attribution
slug: crescendo-lab
tags:
- Company
- SMS
- Messaging
- Marketing Automation
- Customer Engagement
- Taiwan
- Omnichannel
- MCP
website: https://cresclab.com
---
