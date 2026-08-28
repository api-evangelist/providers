---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sparefoot-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sparefoot
- group: company
  title: ''
  type: Website
  url: https://www.sparefoot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.sparefoot.com/
- group: operate
  title: ''
  type: Support
  url: https://support.sparefoot.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/sparefoot-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sparefoot-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sparefoot-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sparefoot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.storable.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/sparefoot-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sparefoot-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sparefoot.com/self-storage/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpareFoot
- group: start
  title: ''
  type: SignUp
  url: https://my.sparefoot.com/signup-start
- group: start
  title: ''
  type: Login
  url: https://my.sparefoot.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storable.com/privacy/sparefoot-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storable.com/privacy/sparefoot-privacy-policy/
coverage:
  checked: '2026-08-14'
  detail: SpareFoot's own knowledge base markets a facility "data feed (API)" and the Storable status page tracks sibling brands' integration APIs as named components ("SiteLink API", "Storable Edge API", "Storable Easy API") but ships no SpareFoot equivalent - the only route in is SpareFoot/Storable's integrations team, with no endpoint, schema, base URL, or auth scheme published anywhere.
  evidence:
  - status: 200
    url: https://support.sparefoot.com/sparefoot-marketplace/account-management/marketplace-integrations/integration-with-storable-marketplace/integration-with-storable-marketplace-overview~7603116932556493992
  - status: 200
    url: https://status.storable.com/api/v2/summary.json
  - status: 403
    url: https://www.sparefoot.com/openapi.json
  - status: 403
    url: https://docs.sparefoot.com/
  reason: sales-gate
  state: gated
created: '2026-07-03'
description: SpareFoot is the largest online marketplace for finding and reserving self-storage units, owned by Storable (the same parent that owns the storEDGE and SiteLink property-management systems, cataloged separately at api-evangelist/storable). SpareFoot itself does not publish a developer portal, API reference, or self-serve API keys for third parties to call. Instead, storage facilities' pricing, unit availability, and promotions reach SpareFoot through one-way, partner-gated data-feed integrations built by property-management software vendors - Storable Edge (storEDGE), SiteLink Web Edition, Storable Easy, Self Storage Manager (E-SoftSys), eDOMICO, and DoorSwap - each of which pushes its own facilities' inventory into the marketplace and receives reservation/lead data back. No endpoint list, request/response schema, or authentication scheme for this feed mechanism is publicly documented; a facility operator or software vendor must go through SpareFoot/Storable's integrations team
  to be onboarded. This entry documents that access model honestly rather than fabricating an API surface. The one machine-readable document SpareFoot does serve is an llms.txt at the site root - a crawler-directive-and-attribution file aimed at language models rather than a developer contract - alongside a robots.txt that allows GPTBot while disallowing ChatGPT-User, CCBot, anthropic-ai and Claude-Web.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sparefoot.png
layout: provider
modified: '2026-08-14'
name: SpareFoot
nav: Providers
network: true
overview: 'SpareFoot is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Self Storage, Marketplace, Storage Unit Listings, Lead Generation, and Reservations.


  SpareFoot''s developer surface includes documentation, support, engineering blog, signup flow, and 14 more developer resources.'
plans:
- name: Sparefoot Plans Pricing
  plan_count: 3
  slug: sparefoot-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Sparefoot Rate Limits
  slug: sparefoot-rate-limits
score:
  band: emerging
  composite: 24.6
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 24.6
  provenance:
    conformance: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Sparefoot Domain Security
  slug: sparefoot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sparefoot
tags:
- Self Storage
- Marketplace
- Storage Unit Listings
- Lead Generation
- Reservations
- Partner Integration
- Data Feed
- Storable
- SiteLink
- storEDGE
website: https://www.sparefoot.com/
---
