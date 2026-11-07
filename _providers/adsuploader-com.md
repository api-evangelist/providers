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
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Ads Uploader provides an API for bulk uploading Meta ads.
  name: Ads Uploader API
  slug: ads-uploader-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/adsuploader-com/plans/adsuploader-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adsuploader-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/adsuploader-com/authentication/adsuploader-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adsuploader-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/adsuploader-com/mcp/adsuploader-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adsuploader-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adsuploader-com/well-known/adsuploader-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adsuploader-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/adsuploader-com/hosts/adsuploader-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adsuploader-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adsuploader-com/vendors/adsuploader-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adsuploader-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/adsuploader-com/packages/adsuploader-com-packages.yml
  title: ''
  type: SDKs
  url: packages/adsuploader-com-packages.yml
- group: build
  href: https://artifacts.apis.io/adsuploader-com/packages/adsuploader-com-packages.yml
  title: ''
  type: Packages
  url: packages/adsuploader-com-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adsuploader.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://adsuploader.com/docs/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adsuploader
- group: auth
  href: https://artifacts.apis.io/adsuploader-com/security/adsuploader-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adsuploader-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adsuploader.com/
- group: docs
  title: ''
  type: Documentation
  url: https://adsuploader.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://adsuploader.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://adsuploader.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://adsuploader.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://adsuploader.com/signup
- group: operate
  title: ''
  type: Support
  url: https://adsuploader.com/docs/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adsuploader.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adsuploader.com/privacy-policy
coverage:
  checked: '2026-11-01'
  detail: Documentation is publicly available but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://adsuploader.com/docs/automation/api-keys
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Ads Uploader enables bulk launch of Meta ads in minutes—simple, fast, unlimited. Upload hundreds of Meta ads in minutes, not hours. Auto‑match variations, configure settings instantly, and launch directly via API. Stop the busywork, scale your creative testing. Features include bulk media upload for Meta Ads, automated thumbnail matching, and AI‑driven ad launches.
image: https://adsuploader.com/ogimage.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at adsuploader.com.
  name: Ads Uploader MCP Server
  slug: adsuploader-com-mcp-yml
modified: '2026-10-31'
name: Ads Uploader
nav: Providers
network: true
overview: 'Ads Uploader is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Meta Ads, Automation, Bulk Upload, Creative Testing, and Marketing.


  Ads Uploader''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Adsuploader Com Plans Pricing
  plan_count: 2
  slug: adsuploader-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Adsuploader Com Rate Limits
  slug: adsuploader-com-rate-limits
scopes:
- name: Adsuploader Com Scopes
  scope_count: 0
  slug: adsuploader-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 36.9
    discoverability: 56.7
    operational_transparency: 10.5
  previous_composite: 34.7
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adsuploader Com Authentication
  slug: adsuploader-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adsuploader Com Domain Security
  slug: adsuploader-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adsuploader-com
tags:
- Meta Ads
- Automation
- Bulk Upload
- Creative Testing
- Marketing
website: https://adsuploader.com/
---
