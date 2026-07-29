---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Apache Http Agentic Access
  operation_count: 3
  slug: apache-http-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 3
apis:
- description: Maven artifact for Apache HttpComponents HttpClient 5.x providing full HTTP client functionality including fluent API, async client, and reactive streams support.
  name: Apache HttpComponents Java SDK
  slug: apache-http-java-sdk
- description: Client configuration operations
  name: Apache HttpComponents Configuration API
  slug: apache-http-configuration-api
- description: HTTP request execution operations
  name: Apache HttpComponents Requests API
  slug: apache-http-requests-api
artifact_total: 42
collections:
- collection_type: open
  name: Apache HttpComponents Client API
  slug: open-apache-http-client
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-http-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-http-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-http-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://hc.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://hc.apache.org/httpcomponents-client-5.3.x/quickstart.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/httpcomponents-client
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-http-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-http-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://hc.apache.org/news.html
created: '2026-03-16'
description: Apache HttpComponents is a set of Java HTTP components, including a feature-rich HTTP client (HttpClient 5.x) and HTTP server components. It provides connection pooling, async I/O, TLS/SSL support, authentication, cookie management, and content negotiation for Java applications making HTTP requests.
examples:
- key_count: 5
  name: Http Client Connectionconfig Example
  slug: http-client-connectionconfig-example
- key_count: 5
  name: Http Client Httprequest Example
  slug: http-client-httprequest-example
- key_count: 5
  name: Http Client Httpresponse Example
  slug: http-client-httpresponse-example
- key_count: 5
  name: Http Client Proxyconfig Example
  slug: http-client-proxyconfig-example
features:
- description: Configurable connection pool with per-route and total connection limits for efficient HTTP connection reuse.
  name: Connection Pooling
- description: Non-blocking async HTTP client based on Java NIO for high-concurrency request execution.
  name: Async HTTP Client
- description: Full TLS/SSL support with customizable trust stores, client certificates, and hostname verification.
  name: TLS/SSL Support
- description: Pluggable authentication framework supporting Basic, Digest, NTLM, and Bearer token schemes.
  name: Authentication Framework
- description: RFC-compliant cookie management with customizable cookie stores and policies.
  name: Cookie Management
- description: HTTP, HTTPS, and SOCKS proxy support with proxy authentication.
  name: Proxy Support
- description: Built-in content encoding, compression (gzip/deflate), and charset negotiation.
  name: Content Negotiation
- description: High-level fluent API for simplified one-liner HTTP request execution.
  name: Fluent API
finops:
- name: Apache Http Finops
  service_category: API
  slug: apache-http-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-http.png
integrations:
- description: Spring RestTemplate and WebClient use Apache HttpComponents as a configurable HTTP backend.
  name: Spring Framework
- description: Apache CXF JAX-RS client uses HttpComponents for HTTP transport in web service calls.
  name: Apache CXF
- description: Elasticsearch Java client uses HttpComponents for transport-layer HTTP communication.
  name: Elasticsearch Java Client
- description: Apache Solr Java client (SolrJ) uses HttpComponents for Solr HTTP API calls.
  name: Apache Solr
json_schemas:
- name: ConnectionConfig
  property_count: 5
  slug: http-client-connectionconfig
- name: HttpRequest
  property_count: 5
  slug: http-client-httprequest
- name: HttpResponse
  property_count: 5
  slug: http-client-httpresponse
- name: ProxyConfig
  property_count: 5
  slug: http-client-proxyconfig
json_structures:
- name: Http Client Connectionconfig Structure
  property_count: 5
  slug: http-client-connectionconfig-structure
- name: Http Client Httprequest Structure
  property_count: 5
  slug: http-client-httprequest-structure
- name: Http Client Httpresponse Structure
  property_count: 5
  slug: http-client-httpresponse-structure
- name: Http Client Proxyconfig Structure
  property_count: 5
  slug: http-client-proxyconfig-structure
jsonld:
- class_count: 17
  name: Apache Http Client Context
  property_count: 0
  slug: apache-http-client-context
layout: provider
modified: '2026-05-19'
name: Apache HttpComponents
nav: Providers
network: true
overview: 'Apache HttpComponents publishes 2 APIs on the [APIs.io](https://apis.io/) network: Configuration API and Requests API. Tagged areas include Apache, HTTP Client, Java, Open Source, and SDK.


  The Apache HttpComponents catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache HttpComponents'' developer surface includes documentation, getting-started guide, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Http Plans Pricing
  plan_count: 3
  slug: apache-http-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 5
  name: Apache Http Rate Limits
  slug: apache-http-rate-limits
rules:
- name: Apache HttpComponents API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-http-jsonschema-spectral-rules
- name: Apache HttpComponents API Rules
  rule_count: 13
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 8
  slug: apache-http-spectral-rules
score:
  band: developing
  composite: 46.4
  delta: -5.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.5
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-http/refs/heads/main/screenshots/apache-http-2026-06-20T172105.png
security:
- kind: domain-security
  name: Apache Http Domain Security
  slug: apache-http-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Http Vulnerability Disclosure
  slug: apache-http-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-http
tags:
- Apache
- HTTP Client
- Java
- Open Source
- SDK
use_cases:
- description: Consume REST APIs from Java applications with connection pooling and retry logic.
  name: REST API Client Integration
- description: Crawl and fetch web content with cookie handling and redirect following.
  name: Web Scraping
- description: Make service-to-service HTTP calls with connection reuse and timeout configuration.
  name: Microservices HTTP Communication
- description: Implement OAuth2 token refresh flows using the authentication interceptor framework.
  name: Authentication Token Refresh
- description: Stream large file uploads and downloads via multipart or chunked transfer encoding.
  name: File Upload and Download
---
