---
aid: squid
name: Squid
description: Squid is a high-performance caching and forwarding HTTP web proxy used for content caching, access control, and bandwidth management. It supports HTTP, HTTPS, FTP, and other protocols, providing caching proxy features, access control lists, SSL/TLS inspection, and web content filtering for enterprises and internet service providers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Caching Proxy
  - Proxy
  - HTTP Proxy
  - Web Cache
  - Access Control
  - Content Filtering
url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: squid:squid-cache-manager
    name: Squid Cache Manager API
    description: The Squid Cache Manager is a built-in HTTP management interface that exposes internal statistics, cache operations, and runtime configuration via HTTP requests. It provides endpoints for retrieving cache statistics, managing active connections, viewing access control lists, and performing cache operations such as reconfigure and log rotation.
    humanURL: http://www.squid-cache.org/Doc/config/cachemgr_passwd/
    baseURL: http://localhost:3128/squid-internal-mgr
    tags:
      - Caching Proxy
      - Cache Manager
      - HTTP Proxy
      - Web Cache
    properties:
      - type: Documentation
        url: http://www.squid-cache.org/Doc/
      - type: Getting Started
        url: http://www.squid-cache.org/Doc/config/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/openapi/squid-cache-manager-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/json-schema/squid-cache-stats-schema.json
    contact:
      - FN: Squid Project
        url: http://www.squid-cache.org/Support/
  - aid: squid:squid-access-control
    name: Squid Access Control Configuration API
    description: Squid provides extensive access control configuration through its squid.conf file and runtime reload capabilities. The access control system supports ACLs for IP addresses, domain names, URL patterns, user authentication, time-of-day restrictions, and MIME type filtering.
    humanURL: http://www.squid-cache.org/Doc/config/acl/
    baseURL: http://localhost:3128/squid-internal-mgr
    tags:
      - Access Control
      - Configuration
      - HTTP Proxy
    properties:
      - type: Documentation
        url: http://www.squid-cache.org/Doc/config/acl/
      - type: Getting Started
        url: http://www.squid-cache.org/Doc/config/
common:
  - type: Website
    url: http://www.squid-cache.org/
  - type: Documentation
    url: http://www.squid-cache.org/Doc/
  - type: GitHub Organization
    url: https://github.com/squid-cache
  - type: Changelog
    url: http://www.squid-cache.org/Versions/
  - type: FAQ
    url: http://wiki.squid-cache.org/SquidFaq
  - type: Mailing List
    url: http://www.squid-cache.org/Support/mailing-lists.html
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/openapi/squid-cache-manager-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/json-schema/squid-cache-stats-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/json-structure/squid-cache-stats-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/json-ld/squid-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/rules/squid-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/capabilities/proxy-management.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/vocabulary/squid-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
