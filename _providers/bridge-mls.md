---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Bridge Mls Agentic Access
  operation_count: 21
  slug: bridge-mls-agentic-access
  summary_line: 21 operations · 4 acting
api_count: 13
apis:
- description: Manage webhook endpoints that receive real-time POST events from Bridge for listing create/update/delete and other dataset changes, eliminating the need to poll the Web API. Endpoints require an HTTPS
  name: Bridge Webhooks API
  slug: bridge-webhooks-api
- description: Zillow Group Data feeds delivered through Bridge — parcels, assessments, transactions, and Zillow Group Econ Data (ZHVI, ZORI, market metrics) — accessible via the same OData/RESO Web API surface as M
  name: Zillow Group Data (ZG Data) API
  slug: zillow-group-data-api
- description: The Agents API from Bridge — 1 operation(s) for agents.
  name: Bridge Agents API
  slug: bridge-mls-agents-api
- description: The Listings API from Bridge — 2 operation(s) for listings.
  name: Bridge Listings API
  slug: bridge-mls-listings-api
- description: RESO Media resource (photos, virtual tours)
  name: Bridge Media API
  slug: bridge-mls-media-api
- description: RESO Member resource (agents)
  name: Bridge Member API
  slug: bridge-mls-member-api
- description: Service document and CSDL schema discovery
  name: Bridge Metadata API
  slug: bridge-mls-metadata-api
- description: RESO Office resource (brokerages)
  name: Bridge Office API
  slug: bridge-mls-office-api
- description: The Offices API from Bridge — 1 operation(s) for offices.
  name: Bridge Offices API
  slug: bridge-mls-offices-api
- description: RESO OpenHouse resource
  name: Bridge OpenHouse API
  slug: bridge-mls-openhouse-api
- description: The OpenHouses API from Bridge — 1 operation(s) for openhouses.
  name: Bridge OpenHouses API
  slug: bridge-mls-openhouses-api
- description: RESO Property resource (listings)
  name: Bridge Property API
  slug: bridge-mls-property-api
- description: The Webhooks API from Bridge — 3 operation(s) for webhooks.
  name: Bridge Webhooks API
  slug: bridge-mls-webhooks-api
artifact_total: 67
collections:
- collection_type: postman
  name: Bridge RESO Web Agents API
  slug: postman-bridge-mls-agents-api
- collection_type: postman
  name: Bridge RESO Web Agents Listings API
  slug: postman-bridge-mls-listings-api
- collection_type: postman
  name: Bridge RESO Web Agents Media API
  slug: postman-bridge-mls-media-api
- collection_type: postman
  name: Bridge RESO Web Agents Member API
  slug: postman-bridge-mls-member-api
- collection_type: postman
  name: Bridge RESO Web Agents Metadata API
  slug: postman-bridge-mls-metadata-api
- collection_type: postman
  name: Bridge RESO Web Agents Office API
  slug: postman-bridge-mls-office-api
- collection_type: postman
  name: Bridge RESO Web Agents Offices API
  slug: postman-bridge-mls-offices-api
- collection_type: postman
  name: Bridge RESO Web Agents OpenHouse API
  slug: postman-bridge-mls-openhouse-api
- collection_type: postman
  name: Bridge RESO Web Agents OpenHouses API
  slug: postman-bridge-mls-openhouses-api
- collection_type: postman
  name: Bridge RESO Web Agents Property API
  slug: postman-bridge-mls-property-api
- collection_type: postman
  name: Bridge RESO Web Agents Webhooks API
  slug: postman-bridge-mls-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bridge RESO Web Agents API
  slug: open-bridge-mls-agents-api
- collection_type: open
  name: Bridge RESO Web Agents Listings API
  slug: open-bridge-mls-listings-api
- collection_type: open
  name: Bridge RESO Web Agents Media API
  slug: open-bridge-mls-media-api
- collection_type: open
  name: Bridge RESO Web Agents Member API
  slug: open-bridge-mls-member-api
- collection_type: open
  name: Bridge RESO Web Agents Metadata API
  slug: open-bridge-mls-metadata-api
- collection_type: open
  name: Bridge RESO Web Agents Office API
  slug: open-bridge-mls-office-api
- collection_type: open
  name: Bridge RESO Web Agents Offices API
  slug: open-bridge-mls-offices-api
- collection_type: open
  name: Bridge RESO Web Agents OpenHouse API
  slug: open-bridge-mls-openhouse-api
- collection_type: open
  name: Bridge RESO Web Agents OpenHouses API
  slug: open-bridge-mls-openhouses-api
- collection_type: open
  name: Bridge RESO Web Agents Property API
  slug: open-bridge-mls-property-api
- collection_type: open
  name: Bridge RESO Web Agents Webhooks API
  slug: open-bridge-mls-webhooks-api
- collection_type: open
  name: Bridge RESO Web API
  slug: open-bridge-reso-web-api
- collection_type: open
  name: Bridge Web API
  slug: open-bridge-web-api
- collection_type: open
  name: Bridge Webhooks API
  slug: open-bridge-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/bridge/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bridge-mls-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bridge-mls-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bridge-mls-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.bridgeinteractive.com
- group: start
  title: ''
  type: Portal
  url: https://bridgedataoutput.com
- group: docs
  title: ''
  type: Documentation
  url: https://bridgedataoutput.com/docs/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://bridgedataoutput.com/docs/platform/Introduction/Signing-up-with-Bridge-API
- group: start
  title: ''
  type: Sandbox
  url: https://bridgedataoutput.com/docs/explorer/reso-web-api
- group: start
  title: ''
  type: Sandbox
  url: https://bridgedataoutput.com/docs/explorer/mls-data
- group: start
  title: ''
  type: Signup
  url: https://bridgedataoutput.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.bridgeinteractive.com/developers/bridge-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bridgeinteractive.com/developers/data-access/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bridgeinteractive.com/developers/zillow-group-data/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bridgeinteractive.com/resources/api-documentation/
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.bridgedataoutput.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bridgeinteractive.com/bridge-platform-updates/
- group: operate
  title: ''
  type: Support
  url: https://bridgedataoutput.com/help
- group: operate
  title: ''
  type: Support
  url: mailto:support@bridgeinteractive.com
- group: company
  title: ''
  type: AboutUs
  url: https://www.bridgeinteractive.com/about/
- group: operate
  title: ''
  type: ContactForm
  url: https://www.bridgeinteractive.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bridgeinteractive.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bridgeinteractive.com/terms-of-use/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bridge-interact
- group: docs
  title: ''
  type: Documentation
  url: https://www.reso.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.reso.org/data-dictionary/
- group: docs
  title: ''
  type: Documentation
  url: https://www.reso.org/reso-web-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.reso.org/certification/
- group: commercial
  title: ''
  type: Plans
  url: plans/bridge-mls-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bridge-mls-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bridge-mls-finops.yml
created: '2026-05-25'
description: Bridge (Bridge Interactive / Bridge Data Output) is a Zillow Group company that runs the Bridge Platform — a RESO Platinum-certified MLS data distribution service used by Multiple Listing Services and brokerages across the US and Canada. The Bridge RESO Web API exposes normalized listing data (Property, Member, Office, OpenHouse, Media, Room, UnitType) via OData 4.0 at api.bridgedataoutput.com/api/v2/OData, with a parallel native Bridge Web API serving the same resources as flat JSON. A Webhooks API delivers real-time listing change events with PKI-signed payloads. Bridge also distributes Zillow Group Data — parcels, assessments, and ZHVI/ZORI economic feeds — through the same API surface.
examples:
- key_count: 2
  name: Bridge List Properties Example
  slug: bridge-list-properties-example
features:
- RESO Platinum-certified Web API serving normalized MLS listing data across the US and Canada
- OData 4.0 query surface with $filter, $select, $expand, $orderby, $top, $count plus Bridge unselect extension
- Resources include Property, Member, Office, OpenHouse, Media, Room, UnitType, and other RESO-defined entities
- Both v2 (api.bridgedataoutput.com/api/v2) and v3 (api.bridgedataoutput.com/api/v3) endpoints
- Native Bridge Web API serving the same resources as flat JSON for non-OData consumers
- Webhooks API for real-time listing change events with PKI-signed payloads and exponential-backoff retries
- Server Token and Access Token authentication scoped per dataset
- Data refreshed every 10 minutes or less per MLS feed
- Media returned as embedded object on Property records, CDN-hosted at highest available resolution
- Off-market and historical data available where licensed by the MLS
- DataSystem endpoint to discover dataset capabilities and metadata
- $metadata endpoint exposes the OData CSDL schema per dataset
- maxpagesize header (default 10, max 200) controls page size — Bridge interprets $top as page size, not total
- Zillow Group Data feeds (parcels, assessments, ZHVI/ZORI econ data) on the same API surface
- Parity Plus program lets MLSs customize the API the way they would with RETS
- Preparing datasets for RESO Data Dictionary 2.0 certification
- Public API Explorer with a test dataset for evaluation
finops:
- name: Bridge Mls Finops
  service_category: ''
  slug: bridge-mls-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bridge-mls.png
json_schemas:
- name: Bridge RESO Member
  property_count: 23
  slug: bridge-member
- name: Bridge RESO Property
  property_count: 51
  slug: bridge-property
jsonld:
- class_count: 31
  name: Bridge Mls Context
  property_count: 1
  slug: bridge-mls-context
layout: provider
modified: '2026-05-25'
name: Bridge
nav: Providers
network: true
overview: 'Bridge publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Listings API, Media API, and 8 more. Tagged areas include Real Estate, MLS, RESO, Listings, and Property Data.


  The Bridge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bridge''s developer surface includes authentication, developer portal, documentation, getting-started guide, sandbox, signup flow, changelog, and 24 more developer resources.'
plans:
- name: Bridge Mls Plans Pricing
  plan_count: 3
  slug: bridge-mls-plans-pricing
random_paper: 104
rate_limits:
- limit_count: 4
  name: Bridge Mls Rate Limits
  slug: bridge-mls-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bridge API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bridge-mls-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.8
  delta: -2.8
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 9.8
    contract_quality: 67.2
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 47.4
  previous_composite: 61.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bridge-mls/refs/heads/main/screenshots/bridge-mls-2026-06-20T173655.png
security:
- kind: authentication
  name: Bridge Mls Authentication
  slug: bridge-mls-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Bridge Mls Domain Security
  slug: bridge-mls-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bridge-mls
tags:
- Real Estate
- MLS
- RESO
- Listings
- Property Data
- Brokers
- Data Distribution
website: https://www.bridgeinteractive.com
---
