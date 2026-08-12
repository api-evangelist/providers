---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Ipgeolocation Agentic Access
  operation_count: 13
  slug: ipgeolocation-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 7
apis:
- description: API endpoint for retrieving Autonomous System Number (ASN) information associated with IPv4 addresses, IPv6 addresses, or specific ASN numbers. The response includes ASN metadata such as the ASN numbe
  name: IPGeolocation.io ASN Lookup API
  slug: ipgeolocation-asn-lookup-api
- description: API endpoints for retrieving astronomical information for a given location, including sunrise and sunset times, moonrise and moonset times, twilight phases, golden hour and blue hour windows, solar no
  name: IPGeolocation.io Astronomy API
  slug: ipgeolocation-astronomy-api
- description: 'API endpoint for retrieving abuse contact information associated with IPv4 and IPv6 addresses. The response contains registry-based contact details for reporting malicious or abusive network activity '
  name: IPGeolocation.io IP Abuse Contact API
  slug: ipgeolocation-ip-abuse-contact-api
- description: IP geolocation API endpoints for looking up geographic location, network routing, ASN ownership, company attribution, timezone, currency, security threat intelligence, abuse contact, and User-Agent da
  name: IPGeolocation.io IP Geolocation API
  slug: ipgeolocation-ip-geolocation-api
- description: IP security intelligence endpoints used to detect VPNs, proxies, Tor exit nodes, relay networks, bot activity, spam activity, cloud providers, and other anonymization technologies associated with IP a
  name: IPGeolocation.io IP Security API
  slug: ipgeolocation-ip-security-api
- description: API endpoints for retrieving current date, time, and timezone information for a given input such as an IANA timezone identifier, geographic coordinates, location address, IPv4 or IPv6 address, airport
  name: IPGeolocation.io Timezone API
  slug: ipgeolocation-timezone-api
- description: API endpoints for parsing user agent strings into browser, device, layout engine, and operating system details. Supports single lookups via request header, custom string lookups via JSON body, and bul
  name: IPGeolocation.io User Agent API
  slug: ipgeolocation-user-agent-api
artifact_total: 169
collections:
- collection_type: open
  name: 'IPGeolocation.io: Abuse Contact API'
  slug: open-ipgeolocation-abuse
- collection_type: open
  name: 'IPGeolocation.io: ASN Lookup API'
  slug: open-ipgeolocation-asn
- collection_type: open
  name: 'IPGeolocation.io: Astronomy API'
  slug: open-ipgeolocation-astronomy
- collection_type: open
  name: 'IPGeolocation.io: IPGeolocation API'
  slug: open-ipgeolocation-ip-location
- collection_type: open
  name: 'IPGeolocation.io: IP Security API'
  slug: open-ipgeolocation-security
- collection_type: open
  name: 'IPGeolocation.io: Date, Time & Timezone API'
  slug: open-ipgeolocation-timezone
- collection_type: open
  name: 'IPGeolocation.io: User Agent API'
  slug: open-ipgeolocation-user-agent
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ipgeolocation-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ipgeolocation-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ipgeolocation-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://ipgeolocation.io/blog
- group: company
  title: ''
  type: Website
  url: https://ipgeolocation.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ipgeolocation.io/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://ipgeolocation.io/pricing.html
- group: start
  title: ''
  type: Signup
  url: https://app.ipgeolocation.io/signup
- group: other
  title: ''
  type: Dashboard
  url: https://app.ipgeolocation.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IPGeolocation
- group: docs
  title: Combined OpenAPI Spec
  type: OpenAPI
  url: https://github.com/IPGeolocation/openapi
- group: build
  title: ''
  type: CLI
  url: https://github.com/IPGeolocation/cli
- group: build
  title: MCP Server
  type: Tools
  url: https://github.com/IPGeolocation/ipgeolocation-io-mcp
- group: build
  title: Steampipe Plugin
  type: Tools
  url: https://github.com/IPGeolocation/steampipe-plugin-ipgeolocation
- group: build
  title: Vercel Edge Middleware
  type: Tools
  url: https://github.com/IPGeolocation/vercel-middleware
- group: build
  title: n8n Node
  type: Tools
  url: https://github.com/IPGeolocation/n8n-nodes-ipgeolocation
- group: build
  title: Google Sheets Add-on
  type: Tools
  url: https://github.com/IPGeolocation/google-sheets
- group: build
  title: Elasticsearch Ingest Processor
  type: Tools
  url: https://github.com/IPGeolocation/es-ipgeo-ingest-processor
- group: build
  title: MMDB CLI (mmdbio)
  type: Tools
  url: https://github.com/IPGeolocation/mmdbio
- group: build
  title: Database Reader
  type: Tools
  url: https://github.com/IPGeolocation/ipgeolocation-database-reader
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/ipgeolocation-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ipgeolocation-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ipgeolocation-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ipgeolocation-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/ipgeolocation-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ipgeolocation-context.jsonld
created: '2026-05-28'
description: IPGeolocation.io is a multi-product IP intelligence platform offering IP geolocation, IP security/threat intelligence, ASN lookup, abuse contact, timezone, astronomy (sunrise, sunset, moon phase, celestial position), and user-agent parsing APIs. All endpoints are served under https://api.ipgeolocation.io with API-key authentication. The free plan offers 1,000 credits/day; paid plans (Starter through Premium) scale from 150K to 5M requests/month, with custom Enterprise pricing on top.
examples:
- key_count: 8
  name: Abuse Abuse Example
  slug: abuse-abuse-example
- key_count: 2
  name: Abuse Abuse Lookup Response Example
  slug: abuse-abuse-lookup-response-example
- key_count: 16
  name: Asn Asn Example
  slug: asn-asn-example
- key_count: 3
  name: Asn Asnconnection Example
  slug: asn-asnconnection-example
- key_count: 2
  name: Asn Asnlookup Response Example
  slug: asn-asnlookup-response-example
- key_count: 26
  name: Astronomy Astronomy Data Example
  slug: astronomy-astronomy-data-example
- key_count: 3
  name: Astronomy Astronomy Lookup Response Example
  slug: astronomy-astronomy-lookup-response-example
- key_count: 15
  name: Astronomy Astronomy Time Series Entry Example
  slug: astronomy-astronomy-time-series-entry-example
- key_count: 3
  name: Astronomy Astronomy Time Series Response Example
  slug: astronomy-astronomy-time-series-response-example
- key_count: 17
  name: Astronomy Location Example
  slug: astronomy-location-example
- key_count: 10
  name: Astronomy Twilight Phase Example
  slug: astronomy-twilight-phase-example
- key_count: 8
  name: Ip Location Abuse Example
  slug: ip-location-abuse-example
- key_count: 7
  name: Ip Location Asn Example
  slug: ip-location-asn-example
- key_count: 1
  name: Ip Location Bulk Geolocation Error Item Example
  slug: ip-location-bulk-geolocation-error-item-example
- key_count: 1
  name: Ip Location Bulk Geolocation Request Example
  slug: ip-location-bulk-geolocation-request-example
- key_count: 13
  name: Ip Location Bulk Geolocation Success Item Example
  slug: ip-location-bulk-geolocation-success-item-example
- key_count: 3
  name: Ip Location Company Example
  slug: ip-location-company-example
- key_count: 3
  name: Ip Location Country Metadata Example
  slug: ip-location-country-metadata-example
- key_count: 3
  name: Ip Location Currency Example
  slug: ip-location-currency-example
- key_count: 6
  name: Ip Location Dst Transition Example
  slug: ip-location-dst-transition-example
- key_count: 13
  name: Ip Location Ip Geolocation Response Example
  slug: ip-location-ip-geolocation-response-example
- key_count: 22
  name: Ip Location Location Example
  slug: ip-location-location-example
- key_count: 3
  name: Ip Location Network Example
  slug: ip-location-network-example
- key_count: 19
  name: Ip Location Security Example
  slug: ip-location-security-example
- key_count: 16
  name: Ip Location Time Zone Example
  slug: ip-location-time-zone-example
- key_count: 4
  name: Ip Location User Agent Device Example
  slug: ip-location-user-agent-device-example
- key_count: 4
  name: Ip Location User Agent Engine Example
  slug: ip-location-user-agent-engine-example
- key_count: 8
  name: Ip Location User Agent Example
  slug: ip-location-user-agent-example
- key_count: 5
  name: Ip Location User Agent Operating System Example
  slug: ip-location-user-agent-operating-system-example
- key_count: 1
  name: Security Bulk Security Error Item Example
  slug: security-bulk-security-error-item-example
- key_count: 1
  name: Security Bulk Security Request Example
  slug: security-bulk-security-request-example
- key_count: 2
  name: Security Bulk Security Success Item Example
  slug: security-bulk-security-success-item-example
- key_count: 2
  name: Security Ip Security Response Example
  slug: security-ip-security-response-example
- key_count: 19
  name: Security Security Example
  slug: security-security-example
- key_count: 12
  name: Timezone Airport Details Example
  slug: timezone-airport-details-example
- key_count: 6
  name: Timezone Dsttransition Example
  slug: timezone-dsttransition-example
- key_count: 16
  name: Timezone Location Example
  slug: timezone-location-example
- key_count: 8
  name: Timezone Locode Details Example
  slug: timezone-locode-details-example
- key_count: 4
  name: Timezone Time Conversion Response Example
  slug: timezone-time-conversion-response-example
- key_count: 26
  name: Timezone Timezone Example
  slug: timezone-timezone-example
- key_count: 5
  name: Timezone Timezone Lookup Response Example
  slug: timezone-timezone-lookup-response-example
- key_count: 4
  name: User Agent Device Example
  slug: user-agent-device-example
- key_count: 4
  name: User Agent Engine Example
  slug: user-agent-engine-example
- key_count: 5
  name: User Agent Operating System Example
  slug: user-agent-operating-system-example
- key_count: 8
  name: User Agent User Agent Response Example
  slug: user-agent-user-agent-response-example
finops:
- name: Ipgeolocation Finops
  service_category: IP Intelligence + Geocoding
  slug: ipgeolocation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ipgeolocation.png
json_schemas:
- name: AbuseLookupResponse
  property_count: 2
  slug: abuse-abuse-lookup-response
- name: Abuse
  property_count: 8
  slug: abuse-abuse
- name: ASN
  property_count: 16
  slug: asn-asn
- name: ASNConnection
  property_count: 3
  slug: asn-asnconnection
- name: ASNLookupResponse
  property_count: 2
  slug: asn-asnlookup-response
- name: AstronomyData
  property_count: 26
  slug: astronomy-astronomy-data
- name: AstronomyLookupResponse
  property_count: 3
  slug: astronomy-astronomy-lookup-response
- name: AstronomyTimeSeriesEntry
  property_count: 15
  slug: astronomy-astronomy-time-series-entry
- name: AstronomyTimeSeriesResponse
  property_count: 3
  slug: astronomy-astronomy-time-series-response
- name: Location
  property_count: 17
  slug: astronomy-location
- name: TwilightPhase
  property_count: 10
  slug: astronomy-twilight-phase
- name: Abuse
  property_count: 8
  slug: ip-location-abuse
- name: Asn
  property_count: 7
  slug: ip-location-asn
- name: BulkGeolocationErrorItem
  property_count: 1
  slug: ip-location-bulk-geolocation-error-item
- name: BulkGeolocationRequest
  property_count: 1
  slug: ip-location-bulk-geolocation-request
- name: BulkGeolocationResponseItem
  property_count: 0
  slug: ip-location-bulk-geolocation-response-item
- name: BulkGeolocationSuccessItem
  property_count: 13
  slug: ip-location-bulk-geolocation-success-item
- name: Company
  property_count: 3
  slug: ip-location-company
- name: CountryMetadata
  property_count: 3
  slug: ip-location-country-metadata
- name: Currency
  property_count: 3
  slug: ip-location-currency
- name: DstTransition
  property_count: 6
  slug: ip-location-dst-transition
- name: IpGeolocationResponse
  property_count: 13
  slug: ip-location-ip-geolocation-response
- name: Location
  property_count: 22
  slug: ip-location-location
- name: Network
  property_count: 3
  slug: ip-location-network
- name: Security
  property_count: 19
  slug: ip-location-security
- name: TimeZone
  property_count: 16
  slug: ip-location-time-zone
- name: UserAgentDevice
  property_count: 4
  slug: ip-location-user-agent-device
- name: UserAgentEngine
  property_count: 4
  slug: ip-location-user-agent-engine
- name: UserAgentOperatingSystem
  property_count: 5
  slug: ip-location-user-agent-operating-system
- name: UserAgent
  property_count: 8
  slug: ip-location-user-agent
- name: BulkSecurityErrorItem
  property_count: 1
  slug: security-bulk-security-error-item
- name: BulkSecurityRequest
  property_count: 1
  slug: security-bulk-security-request
- name: BulkSecurityResponseItem
  property_count: 0
  slug: security-bulk-security-response-item
- name: BulkSecuritySuccessItem
  property_count: 2
  slug: security-bulk-security-success-item
- name: IpSecurityResponse
  property_count: 2
  slug: security-ip-security-response
- name: Security
  property_count: 19
  slug: security-security
- name: AirportDetails
  property_count: 12
  slug: timezone-airport-details
- name: DSTTransition
  property_count: 6
  slug: timezone-dsttransition
- name: Location
  property_count: 16
  slug: timezone-location
- name: LocodeDetails
  property_count: 8
  slug: timezone-locode-details
- name: TimeConversionResponse
  property_count: 4
  slug: timezone-time-conversion-response
- name: TimezoneLookupResponse
  property_count: 5
  slug: timezone-timezone-lookup-response
- name: Timezone
  property_count: 26
  slug: timezone-timezone
- name: Device
  property_count: 4
  slug: user-agent-device
- name: Engine
  property_count: 4
  slug: user-agent-engine
- name: OperatingSystem
  property_count: 5
  slug: user-agent-operating-system
- name: UserAgentResponse
  property_count: 8
  slug: user-agent-user-agent-response
json_structures:
- name: Abuse Abuse Lookup Response Structure
  property_count: 2
  slug: abuse-abuse-lookup-response-structure
- name: Abuse Abuse Structure
  property_count: 8
  slug: abuse-abuse-structure
- name: Asn Asn Structure
  property_count: 16
  slug: asn-asn-structure
- name: Asn Asnconnection Structure
  property_count: 3
  slug: asn-asnconnection-structure
- name: Asn Asnlookup Response Structure
  property_count: 2
  slug: asn-asnlookup-response-structure
- name: Astronomy Astronomy Data Structure
  property_count: 26
  slug: astronomy-astronomy-data-structure
- name: Astronomy Astronomy Lookup Response Structure
  property_count: 3
  slug: astronomy-astronomy-lookup-response-structure
- name: Astronomy Astronomy Time Series Entry Structure
  property_count: 15
  slug: astronomy-astronomy-time-series-entry-structure
- name: Astronomy Astronomy Time Series Response Structure
  property_count: 3
  slug: astronomy-astronomy-time-series-response-structure
- name: Astronomy Location Structure
  property_count: 17
  slug: astronomy-location-structure
- name: Astronomy Twilight Phase Structure
  property_count: 10
  slug: astronomy-twilight-phase-structure
- name: Ip Location Abuse Structure
  property_count: 8
  slug: ip-location-abuse-structure
- name: Ip Location Asn Structure
  property_count: 7
  slug: ip-location-asn-structure
- name: Ip Location Bulk Geolocation Error Item Structure
  property_count: 1
  slug: ip-location-bulk-geolocation-error-item-structure
- name: Ip Location Bulk Geolocation Request Structure
  property_count: 1
  slug: ip-location-bulk-geolocation-request-structure
- name: Ip Location Bulk Geolocation Response Item Structure
  property_count: 0
  slug: ip-location-bulk-geolocation-response-item-structure
- name: Ip Location Bulk Geolocation Success Item Structure
  property_count: 13
  slug: ip-location-bulk-geolocation-success-item-structure
- name: Ip Location Company Structure
  property_count: 3
  slug: ip-location-company-structure
- name: Ip Location Country Metadata Structure
  property_count: 3
  slug: ip-location-country-metadata-structure
- name: Ip Location Currency Structure
  property_count: 3
  slug: ip-location-currency-structure
- name: Ip Location Dst Transition Structure
  property_count: 6
  slug: ip-location-dst-transition-structure
- name: Ip Location Ip Geolocation Response Structure
  property_count: 13
  slug: ip-location-ip-geolocation-response-structure
- name: Ip Location Location Structure
  property_count: 22
  slug: ip-location-location-structure
- name: Ip Location Network Structure
  property_count: 3
  slug: ip-location-network-structure
- name: Ip Location Security Structure
  property_count: 19
  slug: ip-location-security-structure
- name: Ip Location Time Zone Structure
  property_count: 16
  slug: ip-location-time-zone-structure
- name: Ip Location User Agent Device Structure
  property_count: 4
  slug: ip-location-user-agent-device-structure
- name: Ip Location User Agent Engine Structure
  property_count: 4
  slug: ip-location-user-agent-engine-structure
- name: Ip Location User Agent Operating System Structure
  property_count: 5
  slug: ip-location-user-agent-operating-system-structure
- name: Ip Location User Agent Structure
  property_count: 8
  slug: ip-location-user-agent-structure
- name: Security Bulk Security Error Item Structure
  property_count: 1
  slug: security-bulk-security-error-item-structure
- name: Security Bulk Security Request Structure
  property_count: 1
  slug: security-bulk-security-request-structure
- name: Security Bulk Security Response Item Structure
  property_count: 0
  slug: security-bulk-security-response-item-structure
- name: Security Bulk Security Success Item Structure
  property_count: 2
  slug: security-bulk-security-success-item-structure
- name: Security Ip Security Response Structure
  property_count: 2
  slug: security-ip-security-response-structure
- name: Security Security Structure
  property_count: 19
  slug: security-security-structure
- name: Timezone Airport Details Structure
  property_count: 12
  slug: timezone-airport-details-structure
- name: Timezone Dsttransition Structure
  property_count: 6
  slug: timezone-dsttransition-structure
- name: Timezone Location Structure
  property_count: 16
  slug: timezone-location-structure
- name: Timezone Locode Details Structure
  property_count: 8
  slug: timezone-locode-details-structure
- name: Timezone Time Conversion Response Structure
  property_count: 4
  slug: timezone-time-conversion-response-structure
- name: Timezone Timezone Lookup Response Structure
  property_count: 5
  slug: timezone-timezone-lookup-response-structure
- name: Timezone Timezone Structure
  property_count: 26
  slug: timezone-timezone-structure
- name: User Agent Device Structure
  property_count: 4
  slug: user-agent-device-structure
- name: User Agent Engine Structure
  property_count: 4
  slug: user-agent-engine-structure
- name: User Agent Operating System Structure
  property_count: 5
  slug: user-agent-operating-system-structure
- name: User Agent User Agent Response Structure
  property_count: 8
  slug: user-agent-user-agent-response-structure
jsonld:
- class_count: 2
  name: Ipgeolocation Abuse Context
  property_count: 10
  slug: ipgeolocation-abuse-context
- class_count: 3
  name: Ipgeolocation Asn Context
  property_count: 19
  slug: ipgeolocation-asn-context
- class_count: 6
  name: Ipgeolocation Astronomy Context
  property_count: 56
  slug: ipgeolocation-astronomy-context
- class_count: 43
  name: Ipgeolocation Context
  property_count: 175
  slug: ipgeolocation-context
- class_count: 19
  name: Ipgeolocation Ip Location Context
  property_count: 105
  slug: ipgeolocation-ip-location-context
- class_count: 6
  name: Ipgeolocation Security Context
  property_count: 23
  slug: ipgeolocation-security-context
- class_count: 7
  name: Ipgeolocation Timezone Context
  property_count: 65
  slug: ipgeolocation-timezone-context
- class_count: 4
  name: Ipgeolocation User Agent Context
  property_count: 11
  slug: ipgeolocation-user-agent-context
layout: provider
modified: '2026-05-29'
name: IPGeolocation.io
nav: Providers
network: true
overview: 'IPGeolocation.io publishes 7 APIs on the [APIs.io](https://apis.io/) network, including ASN Lookup API, Astronomy API, IP Abuse Contact API, and 4 more. Tagged areas include Geocoding, IP Geolocation, IP Intelligence, IP Security, and ASN Lookup.


  The IPGeolocation.io catalog on APIs.io includes 8 JSON-LD contexts and 2 Spectral governance rulesets.


  IPGeolocation.io''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, CLI, tooling, and 20 more developer resources.'
plans:
- name: Ipgeolocation Plans Pricing
  plan_count: 10
  slug: ipgeolocation-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 4
  name: Ipgeolocation Rate Limits
  slug: ipgeolocation-rate-limits
rules:
- name: IPGeolocation.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ipgeolocation-jsonschema-spectral-rules
- name: IPGeolocation.io API Rules
  rule_count: 40
  severity_counts:
    error: 18
    hint: 0
    info: 5
    warn: 17
  slug: ipgeolocation-rules
score:
  band: strong
  composite: 57.0
  delta: 1.9
  facets:
    commercial_clarity: 63.2
    contract_quality: 70.1
    developer_ergonomics: 28.3
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 55.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ipgeolocation/refs/heads/main/screenshots/ipgeolocation-2026-06-20T183555.png
security:
- kind: authentication
  name: Ipgeolocation Authentication
  slug: ipgeolocation-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ipgeolocation Domain Security
  slug: ipgeolocation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ipgeolocation
tags:
- Geocoding
- IP Geolocation
- IP Intelligence
- IP Security
- ASN Lookup
- Abuse Contact
- Timezone
- Astronomy
- User Agent
- Threat Intelligence
- Public APIs
website: https://ipgeolocation.io/
---
