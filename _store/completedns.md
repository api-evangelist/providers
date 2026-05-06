---
aid: completedns
name: CompleteDNS
description: CompleteDNS is a DNS research platform that tracks nameserver modifications and domain drops, with over twenty years of history and billions of recorded changes. The CompleteDNS API exposes domain-scoped lookups that return the chronological history of nameserver changes, drop events, and parking status for a given domain. Both a current v2 API and a legacy v1 API are available, authenticated by API key.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/completedns/refs/heads/main/apis.yml
tags:
  - DNS
  - DNS History
  - Domain Intelligence
  - Domains
  - Nameservers
  - Threat Intelligence
created: '2025-02-09'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: company
apis:
  - aid: completedns:dns-history-api
    name: CompleteDNS API v2
    description: The CompleteDNS API v2 returns the historical nameserver record for a domain, including counts of changes and drops, years of history, and a chronologically ordered list of events. Authentication uses an API key passed as a query parameter.
    humanURL: https://completedns.com/api/documentation/v2
    baseURL: https://api.completedns.com/v2
    tags:
      - DNS History
      - Domains
      - Lookup
      - Nameservers
    properties:
      - type: Documentation
        url: https://completedns.com/api/documentation/v2
      - type: OpenAPI
        url: openapi/completedns-v2-openapi.yml
      - type: Spectral Rules
        url: rules/completedns-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/completedns-dns-history-lookup.yml
    features:
      - title: Domain DNS History
        description: Retrieve the full nameserver history for a domain by name.
      - title: Drop Tracking
        description: Surface domain drop events captured by CompleteDNS.
      - title: Parking Detection
        description: Indicates whether a domain was parked at any point in its history.
      - title: API Key Authentication
        description: Authentication via API key passed as a query parameter.
    useCases:
      - title: Threat Intelligence
        description: Investigate suspicious domains by reviewing nameserver pivots over time.
      - title: Brand Protection
        description: Track unauthorized nameserver changes on monitored domains.
      - title: Domain Acquisition Research
        description: Analyze the historical reliability of a domain prior to acquisition.
  - aid: completedns:ns-history-api
    name: CompleteDNS API v1
    description: The CompleteDNS API v1 (legacy) returns the historical nameserver record for a domain. Includes drop and change counts, TLD support indicator, and chronologically ordered events with added/removed nameservers. CompleteDNS recommends migrating to v2.
    humanURL: https://completedns.com/api/documentation/v1
    baseURL: https://api.completedns.com/v1
    tags:
      - DNS History
      - Legacy
      - Lookup
      - Nameservers
    properties:
      - type: Documentation
        url: https://completedns.com/api/documentation/v1
      - type: OpenAPI
        url: openapi/completedns-v1-openapi.yml
      - type: Spectral Rules
        url: rules/completedns-rules.yml
      - type: Naftiko Capabilities
        url: capabilities/completedns-dns-history-lookup.yml
    features:
      - title: Legacy Nameserver History
        description: Returns nameserver history events with added/removed nameserver records.
      - title: Quota Header
        description: requestsLeft response header surfaces remaining API quota.
    useCases:
      - title: Legacy Integrations
        description: Maintain compatibility with existing tooling that consumes the v1 API.
common:
  - type: Portal
    url: https://completedns.com/
  - type: Documentation
    url: https://completedns.com/api/documentation/v2
  - type: Sign Up
    url: https://completedns.com/register
  - type: Login
    url: https://completedns.com/login
  - type: Pricing
    url: https://completedns.com/pricing
  - type: Contact
    url: https://completedns.com/contact
  - type: Terms of Service
    url: https://completedns.com/terms
  - type: Privacy Policy
    url: https://completedns.com/privacy
  - type: JSON-LD
    url: json-ld/completedns-context.jsonld
  - type: JSONSchema
    url: json-schema/completedns-dns-history-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
