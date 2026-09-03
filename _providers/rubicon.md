---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rubicon-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rubicon-global
- group: company
  title: ''
  type: Website
  url: https://www.rubicon.com
- group: company
  title: ''
  type: Blog
  url: https://www.rubicon.com/feed/
created: '2026-07-03'
description: 'Rubicon (formerly NYSE: RBT) is a waste, recycling, and sustainability technology company founded in 2008. It went public in 2022 via a SPAC merger with Founder SPAC at a pro forma valuation of roughly $1.7 billion, branding itself a "digital challenger" to the traditional waste-hauling industry with a marketplace connecting waste generators to independent haulers plus the RUBICONSmartCity fleet-and-routing platform used by more than 70 municipalities. Operating Status: the company subsequently faced severe financial distress - layoffs and debt restructuring in 2023, a June 2024 NYSE delisting, and a May 2024 divestiture of its entire fleet technology and smart-city business unit (RUBICONSmartCity, RUBICONPro, RUBICONPremier) to Rodina Capital for roughly $68 million plus a possible $12 million earnout; those assets were subsequently absorbed by Routeware. In early 2025 Rubicon deregistered its securities and became a privately held company, majority-owned by Jose Miguel Enrich
  through MBI Holdings, and remains the subject of shareholder litigation over the change-of-control terms. The surviving company operates as a smaller enterprise waste brokerage and sustainability-data business built around the RUBICONConnect platform (service, equipment, pickup, and cost visibility for enterprise customers such as Chipotle and FedEx), alongside RUBICONRegWatch compliance tooling, sustainability reporting, technical advisory services, and the Rubicon Now on-demand dumpster-rental service in a handful of cities. rubicon.com publishes no developer portal, no public API reference, and no OpenAPI specification. The only discoverable API artifact tied to the rubicon.com domain is a "Routeware Smartcity Public Api" Swagger UI hosted at a dev subdomain (haulerpublic-api.dev.aws.rubicon.com) - leftover infrastructure from the divested fleet/smart-city business - which returned a 503 Service Unavailable on every check during this review and is not publicly documented or reachable.
  Any hauler or municipal system integration Rubicon references (for example, connecting to city 311 systems) is negotiated per partner and gated behind sales and onboarding rather than exposed through self-serve developer documentation. Pricing across RUBICONConnect and Rubicon''s enterprise services is entirely quote-based and negotiated per contract; no public pricing, tiers, or rate limits are published. This entry is maintained as an honest stub pending any future public API surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rubicon.png
layout: provider
modified: '2026-07-03'
name: Rubicon
nav: Providers
network: true
overview: 'Rubicon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Waste Management, Recycling, Sustainability, Circular Economy, and Fleet Management.


  Rubicon''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rubicon/refs/heads/main/screenshots/rubicon-2026-09-02T154155.png
security:
- kind: domain-security
  name: Rubicon Domain Security
  slug: rubicon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: rubicon
tags:
- Waste Management
- Recycling
- Sustainability
- Circular Economy
- Fleet Management
- Smart City
- Enterprise
- Gated API
website: https://www.rubicon.com
---
