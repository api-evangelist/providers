---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.franklinresources.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.franklintempleton.com/corporate/ — a different registrable domain (franklinresources.com -> franklintempleton.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  - '{''url'': ''http://developer.franklintempleton.com/user/register'', ''status'': 0, ''note'': ''the only documented API onboarding path; host has no DNS A record as of 2026-09-10 — archived 2019-07-21 through 2023-03-13''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.2
  scored_at: '2026-09-16'
api_count: 3
apis:
- baseURL: https://api.franklintempleton.com/v1
  baseurl_source: declared
  description: The Detailed Product APIs API from Franklin Resources — 7 operation(s) for detailed product apis.
  name: Franklin Resources Detailed Product APIs API
  slug: franklin-resources-detailed-product-apis-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/security/franklin-resources-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/franklin-resources-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/franklin-templeton
- group: company
  title: ''
  type: Website
  url: https://www.franklinresources.com/
- group: company
  title: ''
  type: Website
  url: https://www.franklintempleton.com/
- group: company
  title: ''
  type: Website
  url: https://digitalassets.franklintempleton.com/benji/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/llms/franklin-resources-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/franklin-resources-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.franklintempleton.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/authentication/franklin-resources-authentication.yml
  title: ''
  type: Authentication
  url: authentication/franklin-resources-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/conventions/franklin-resources-conventions.yml
  title: ''
  type: Conventions
  url: conventions/franklin-resources-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/errors/franklin-resources-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/franklin-resources-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/data-model/franklin-resources-data-model.yml
  title: ''
  type: DataModel
  url: data-model/franklin-resources-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/conformance/franklin-resources-conformance.yml
  title: ''
  type: Conformance
  url: conformance/franklin-resources-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/lifecycle/franklin-resources-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/franklin-resources-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/rate-limits/franklin-resources-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/franklin-resources-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/plans/franklin-resources-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/franklin-resources-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/packages/franklin-resources-packages.yml
  title: ''
  type: Packages
  url: packages/franklin-resources-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/overlays/franklin-resources-detailed-product-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/franklin-resources-detailed-product-apis-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/mcp/franklin-resources-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/franklin-resources-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/well-known/franklin-resources-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/franklin-resources-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.franklintempleton.com/help/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.franklintempleton.com/help/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.franklintempleton.com/accounts/accounts-services-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.franklintempleton.com/help/faqs
- group: company
  title: ''
  type: Blog
  url: https://www.franklintempleton.com/insights/investment-themes
created: '2026-03-21'
description: Franklin Resources, doing business as Franklin Templeton, is a global investment management organization offering investment management and related services to retail, institutional, and high net worth clients. It ran a public developer program — the "Detailed Product APIs", seven read-only fund reference, NAV, distribution and AUM operations at api.franklintempleton.com/v1, fronted by a portal at developer.franklintempleton.com — and retired it without a published deprecation notice. Both hosts now have no DNS record; the Swagger 2.0 contract is still served publicly from Franklin Templeton's own SwaggerHub organization, and the company publishes a first-party llms.txt on its main site.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/franklin-resources.png
layout: provider
modified: '2026-09-10'
name: Franklin Resources
nav: Providers
network: true
overview: 'Franklin Resources publishes 1 API on the [APIs.io](https://apis.io/) network: Detailed Product APIs API. Tagged areas include Fortune 500, Investment Management, Asset Management, Financial-Services, and Mutual Funds.


  Franklin Resources'' developer surface includes authentication, support, engineering blog, and 21 more developer resources.'
plans:
- name: Franklin Resources Plans Pricing
  plan_count: 0
  slug: franklin-resources-plans-pricing
press:
- date: '2026-05-25'
  title: Press Release Details - Investor Relations - Franklin Resources
  url: https://investors.franklinresources.com/news-center/press-releases/press-release-details/2024/Franklin-Templeton-Collaborates-with-Microsoft-on-Personalized-Financial-AI-Platform/default.aspx
- date: '2026-05-25'
  title: FRANKLIN RESOURCES INC Earnings Call Transcript ...
  url: https://www.stockinsights.ai/us/BEN/earnings-transcript/fy24-q4-e953
- date: '2026-05-25'
  title: Franklin Templeton and Wand AI Forge Multi-Year Strategic ...
  url: https://investors.franklinresources.com/news-center/press-releases/press-release-details/2025/Franklin-Templeton-and-Wand-AI-Forge-Multi-Year-Strategic-Partnership-to-Advance-Agentic-AI-in-Asset-Management/default.aspx
- date: '2026-05-25'
  title: Three reasons tech could lead the market—again
  url: https://www.franklinresources.com/articles/2025/equity/three-reasons-tech-could-lead-the-market-again
- date: '2026-05-25'
  title: New Intelligence Hub Marks Expansion of Franklin ...
  url: https://investors.franklinresources.com/news-center/press-releases/press-release-details/2026/New-Intelligence-Hub-Marks-Expansion-of-Franklin-Templetons-Strategic-Collaboration-with-Microsoft/default.aspx
random_paper: 15
rate_limits:
- limit_count: 0
  name: Franklin Resources Rate Limits
  slug: franklin-resources-rate-limits
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 49.0
    developer_ergonomics: 19.0
    discoverability: 81.5
    operational_transparency: 0.0
  previous_composite: 30.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/franklin-resources/refs/heads/main/screenshots/franklin-resources-2026-06-20T181511.png
security:
- kind: authentication
  name: Franklin Resources Authentication
  slug: franklin-resources-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Franklin Resources Domain Security
  slug: franklin-resources-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: franklin-resources
tags:
- Fortune 500
- Investment Management
- Asset Management
- Financial-Services
- Mutual Funds
- Exchange-Traded Funds
- Fund Data
- Market Data
website: https://www.franklinresources.com/
---
