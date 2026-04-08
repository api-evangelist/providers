---
aid: fastly
url: https://raw.githubusercontent.com/api-evangelist/fastly/refs/heads/main/apis.yml
apis:
- aid: fastly:services-api
  name: Fastly Services API
  tags:
  - CDN
  - Configuration
  - Edge Cloud
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/services/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/services/
    type: Documentation
  - url: openapi/fastly-services-openapi.yml
    type: OpenAPI
  description: The Fastly Services API allows developers to create, configure, and manage Fastly CDN services and their versions programmatically. Services are the primary organizational unit in Fastly, representing a configuration that maps domains to backends. The API supports creating service versions, activating and deactivating configurations, cloning versions, and managing the complete lifecycle of a CDN service deployment.
- aid: fastly:purging-api
  name: Fastly Purging API
  tags:
  - Cache
  - CDN
  - Content Delivery
  - Purging
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/purging/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/purging/
    type: Documentation
  - url: openapi/fastly-purging-openapi.yml
    type: OpenAPI
  description: The Fastly Purging API enables developers to instantly remove cached content from Fastly's edge network so it can be refreshed from origin servers. It supports single URL purges, surrogate key purges for invalidating groups of related objects, and purge-all operations to clear an entire service cache. Surrogate key and URL purges are separately limited to an average of 100,000 purges per hour per customer and are not counted against the general API rate limit.
- aid: fastly:logging-api
  name: Fastly Real-Time Logging API
  tags:
  - Analytics
  - Logging
  - Monitoring
  - Observability
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/logging/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/logging/
    type: Documentation
  - url: openapi/fastly-logging-openapi.yml
    type: OpenAPI
  description: The Fastly Real-Time Logging API allows developers to configure and manage logging endpoints that receive streamed log data from Fastly's edge network. Fastly supports logging to a variety of formats and platforms including syslog, Amazon S3, Google Cloud Storage, BigQuery, Datadog, Splunk, Elasticsearch, and many other providers.
- aid: fastly:metrics-and-stats-api
  name: Fastly Metrics and Stats API
  tags:
  - Analytics
  - Metrics
  - Monitoring
  - Real-Time
  - Statistics
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://rt.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/metrics-stats/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/metrics-stats/
    type: Documentation
  - url: openapi/fastly-metrics-and-stats-openapi.yml
    type: OpenAPI
  description: The Fastly Metrics and Stats API provides access to both real-time and historical analytics data for Fastly services. The real-time analytics endpoint, served on rt.fastly.com, delivers second-by-second stats including request counts, bandwidth, cache hit ratios, and error rates. Historical stats provide aggregated data over longer time periods. The API also includes the Domain Inspector for per-domain metrics and the Origin Inspector for origin-level performance data.
- aid: fastly:tls-api
  name: Fastly TLS API
  tags:
  - Certificates
  - Encryption
  - Security
  - SSL
  - TLS
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/tls/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/tls/
    type: Documentation
  - url: openapi/fastly-tls-openapi.yml
    type: OpenAPI
  description: The Fastly TLS API enables developers to manage TLS certificates, private keys, and domain configurations for securing traffic delivered through Fastly's edge network. It supports both platform TLS (managed certificates) and custom TLS configurations where customers bring their own certificates. The API allows uploading certificates, managing bulk certificate operations, configuring TLS activations, and managing mutual TLS authentication for origin connections.
- aid: fastly:vcl-services-api
  name: Fastly VCL Services API
  tags:
  - Caching
  - CDN
  - Configuration
  - Edge Logic
  - VCL
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/vcl-services/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/vcl-services/
    type: Documentation
  - url: openapi/fastly-vcl-services-openapi.yml
    type: OpenAPI
  description: The Fastly VCL Services API provides programmatic access to configure Varnish Configuration Language (VCL) objects that power most Fastly services. Developers can upload custom VCL code or use the API to generate VCL through configuration objects including backends, conditions, cache settings, request settings, response objects, headers, and VCL snippets. This API is central to defining how Fastly processes, routes, and caches HTTP requests at the edge.
- aid: fastly:account-api
  name: Fastly Account API
  tags:
  - Account
  - Administration
  - IAM
  - Users
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/account/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/account/
    type: Documentation
  - url: openapi/fastly-account-openapi.yml
    type: OpenAPI
  description: The Fastly Account API provides endpoints for managing customer accounts, users, and identity and access management (IAM) resources. Developers can programmatically manage user invitations, roles, permissions, and service groups to control access to Fastly resources. The API supports retrieving and updating customer information, managing user profiles, and configuring organizational settings for enterprise accounts.
- aid: fastly:authentication-tokens-api
  name: Fastly Authentication Tokens API
  tags:
  - API Keys
  - Authentication
  - Security
  - Tokens
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/auth-tokens/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/auth-tokens/
    type: Documentation
  - url: openapi/fastly-authentication-tokens-openapi.yml
    type: OpenAPI
  description: The Fastly Authentication Tokens API enables developers to create and manage API tokens used to authenticate requests to the Fastly API. Tokens can be scoped to specific services and permissions, allowing fine-grained access control for users and automated systems. The API supports creating user tokens, automation tokens for CI/CD pipelines, and managing token lifecycle including listing, revoking, and expiring tokens.
- aid: fastly:acls-api
  name: Fastly Access Control Lists API
  tags:
  - Access Control
  - Edge Security
  - IP Filtering
  - Security
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/acls/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/acls/
    type: Documentation
  - url: openapi/fastly-acls-openapi.yml
    type: OpenAPI
  description: The Fastly Access Control Lists API allows developers to create and manage ACLs that can be used to control access to content at the edge. ACLs contain entries of IP addresses or CIDR ranges that can be referenced in VCL to allow or deny requests. The API supports creating ACL containers, adding and removing individual entries, and performing bulk updates to efficiently manage large IP allowlists or blocklists without requiring a new service version deployment.
- aid: fastly:dictionaries-api
  name: Fastly Edge Dictionaries API
  tags:
  - Dictionaries
  - Dynamic Configuration
  - Edge Configuration
  - Key-Value
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/dictionaries/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/dictionaries/
    type: Documentation
  - url: openapi/fastly-dictionaries-openapi.yml
    type: OpenAPI
  description: The Fastly Edge Dictionaries API provides endpoints for creating and managing key-value lookup tables that are accessible at the edge without requiring a service version change. Dictionaries can store configuration data, feature flags, redirect mappings, and other dynamic values that VCL or Compute services can reference during request processing.
- aid: fastly:compute-api
  name: Fastly Compute API
  tags:
  - Compute
  - Edge Computing
  - Serverless
  - WebAssembly
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/guides/compute/
  properties:
  - url: https://www.fastly.com/documentation/guides/compute/
    type: Documentation
  - url: openapi/fastly-compute-openapi.yml
    type: OpenAPI
  description: The Fastly Compute platform enables developers to build and deploy serverless applications that run on Fastly's global edge network using WebAssembly. Compute services support custom application logic written in Rust, JavaScript, or Go using official Fastly SDKs.
- aid: fastly:waf-api
  name: Fastly Next-Gen WAF API
  tags:
  - DDoS Protection
  - Security
  - WAF
  - Web Application Firewall
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/waf/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/waf/
    type: Documentation
  - url: openapi/fastly-waf-openapi.yml
    type: OpenAPI
  description: The Fastly Next-Gen WAF API provides programmatic access to configure and manage web application firewall rules that protect applications delivered through Fastly's edge network. It enables developers to manage WAF firewall configurations, rule sets, and exclusions to defend against common web attacks including SQL injection, cross-site scripting, and other OWASP Top 10 vulnerabilities.
- aid: fastly:domain-management-api
  name: Fastly Domain Management API
  tags:
  - CDN
  - Configuration
  - DNS
  - Domains
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/services/domain/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/services/domain/
    type: Documentation
  - url: openapi/fastly-domain-management-openapi.yml
    type: OpenAPI
  description: The Fastly Domain Management API allows developers to programmatically associate domain names with Fastly services. Domains serve as the entry point for traffic routed through Fastly's edge network. The API supports adding, listing, and removing domains from service versions, checking domain DNS configurations, and validating that domains are correctly pointed to Fastly. It is essential for managing the routing configuration that connects end-user requests to the appropriate Fastly service.
- aid: fastly:products-api
  name: Fastly Products API
  tags:
  - Configuration
  - Features
  - Platform
  - Products
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.fastly.com
  humanURL: https://www.fastly.com/documentation/reference/api/products/
  properties:
  - url: https://www.fastly.com/documentation/reference/api/products/
    type: Documentation
  - url: openapi/fastly-products-openapi.yml
    type: OpenAPI
  description: The Fastly Products API provides endpoints for enabling and managing Fastly product features on services, including Bot Management, DDoS Protection, Image Optimizer, API Discovery, and other add-on capabilities. Developers can use this API to check which products are enabled for a service, enable or disable product features, and configure product-specific settings.
name: Fastly
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Fastly is an edge cloud platform that helps customers create great digital experiences quickly, securely, and reliably by processing, serving, and securing their applications closer to their users.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

