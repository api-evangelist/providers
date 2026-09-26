---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Packlink Agentic Access
  operation_count: 24
  slug: packlink-agentic-access
  summary_line: 24 operations · 7 acting
api_count: 6
apis:
- baseURL: https://api.packlink.com
  baseurl_source: declared
  description: Client account, warehouses, and API keys.
  name: Packlink Clients API
  slug: packlink-clients-api
- baseURL: https://api.packlink.com
  baseurl_source: declared
  description: Customs invoices and customs-union lookups.
  name: Packlink Customs API
  slug: packlink-customs-api
- baseURL: https://api.packlink.com
  baseurl_source: declared
  description: Register and manage platform integrations.
  name: Packlink Integrations API
  slug: packlink-integrations-api
- baseURL: https://api.packlink.com
  baseurl_source: declared
  description: Postal code, postal zone, and drop-off lookups.
  name: Packlink Locations API
  slug: packlink-locations-api
- baseURL: https://api.packlink.com
  baseurl_source: declared
  description: Compare and query available shipping services.
  name: Packlink Services API
  slug: packlink-services-api
- baseURL: https://api.packlink.com
  baseurl_source: declared
  description: Create shipments, print labels, and track parcels.
  name: Packlink Shipments API
  slug: packlink-shipments-api
artifact_total: 17
asyncapis:
- description: ''
  name: Packlink Webhooks
  slug: packlink-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Packlink PRO Shipping Clients API
  slug: open-packlink-clients-api
- collection_type: open
  name: Packlink PRO Shipping Clients Customs API
  slug: open-packlink-customs-api
- collection_type: open
  name: Packlink PRO Shipping Clients Integrations API
  slug: open-packlink-integrations-api
- collection_type: open
  name: Packlink PRO Shipping Clients Locations API
  slug: open-packlink-locations-api
- collection_type: open
  name: Packlink PRO Shipping Clients Services API
  slug: open-packlink-services-api
- collection_type: open
  name: Packlink PRO Shipping Clients Shipments API
  slug: open-packlink-shipments-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/capabilities/packlink-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/packlink-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/overlays/packlink-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/packlink-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: http://www.packlink.com
- group: start
  title: ''
  type: Portal
  url: https://pro.packlink.com
- group: operate
  title: ''
  type: Support
  url: https://support.packlink.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://packlink.com/en-GB/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/packlink-dev
- group: start
  title: ''
  type: SignUp
  url: https://auth.packlink.com/register/?platform=PRO
- group: commercial
  title: ''
  type: TermsOfService
  url: https://packlink.com/en-GB/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://packlink.com/en-GB/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/authentication/packlink-authentication.yml
  title: ''
  type: Authentication
  url: authentication/packlink-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/agentic-access/packlink-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/packlink-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/mcp/packlink-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/packlink-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/conventions/packlink-conventions.yml
  title: ''
  type: Conventions
  url: conventions/packlink-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/lifecycle/packlink-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/packlink-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/errors/packlink-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/packlink-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/data-model/packlink-data-model.yml
  title: ''
  type: DataModel
  url: data-model/packlink-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/conformance/packlink-conformance.yml
  title: ''
  type: Conformance
  url: conformance/packlink-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/packages/packlink-packages.yml
  title: ''
  type: Packages
  url: packages/packlink-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/packages/packlink-packages.yml
  title: ''
  type: SDKs
  url: packages/packlink-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/asyncapi/packlink-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/packlink-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/llms/packlink-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/packlink-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/security/packlink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/packlink-domain-security.yml
created: '2026-07-17'
description: Packlink is a multi-carrier shipping comparison and management platform for e-commerce, founded in Spain and backed by Accel. It lets individuals and businesses compare courier services (UPS, DPD, DHL, Evri, Royal Mail and more) and send parcels nationally and internationally at negotiated rates. Its Packlink PRO product adds a business shipping dashboard with marketplace and e-commerce integrations (Shopify, WooCommerce, Magento, PrestaShop, Amazon, eBay). The Packlink PRO Shipping API (api.packlink.com) exposes service comparison, shipment creation, label printing, parcel tracking, warehouse management, customs invoicing, and integration management, and Packlink maintains open-source e-commerce integration modules on GitHub.
image: http://www.packlink.com
layout: provider
modified: '2026-07-20'
name: Packlink
nav: Providers
network: true
overview: 'Packlink publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Clients API, Customs API, Integrations API, and 3 more. Tagged areas include Company, E-Commerce, Shipping, Logistics, and Parcel Delivery.


  The Packlink catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Packlink''s developer surface includes developer portal, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 21.1
    developer_ergonomics: 37.5
    discoverability: 78.6
    operational_transparency: 10.5
  previous_composite: 27.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 20.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/packlink/refs/heads/main/screenshots/packlink-2026-08-07T191246.png
security:
- kind: authentication
  name: Packlink Authentication
  slug: packlink-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Packlink Domain Security
  slug: packlink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: packlink
tags:
- Company
- E-Commerce
- Shipping
- Logistics
- Parcel Delivery
- Carrier
- Fulfillment
website: http://www.packlink.com
---
