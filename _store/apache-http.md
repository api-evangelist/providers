---
aid: apache-http
name: Apache HttpComponents
description: Apache HttpComponents is a set of Java HTTP components, including a feature-rich HTTP client (HttpClient 5.x) and HTTP server components. It provides connection pooling, async I/O, TLS/SSL support, authentication, cookie management, and content negotiation for Java applications making HTTP requests.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - HTTP Client
  - Java
  - Open Source
  - SDK
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-http/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-http:apache-http-client-api
    name: Apache HttpComponents Client API
    description: Java HTTP client library API for executing HTTP requests with connection pooling, async I/O, TLS/SSL, authentication, cookie management, and proxy support via Apache HttpComponents 5.x.
    humanURL: https://hc.apache.org/httpcomponents-client-5.3.x/
    tags:
      - Authentication
      - Connection Pooling
      - HTTP Client
      - Java
      - TLS
    properties:
      - type: Documentation
        url: https://hc.apache.org/httpcomponents-client-5.3.x/
      - type: OpenAPI
        url: openapi/apache-http-client-openapi.yml
      - type: JSONSchema
        url: json-schema/http-client-httprequest-schema.json
      - type: JSON-LD
        url: json-ld/apache-http-client-context.jsonld
  - aid: apache-http:apache-http-java-sdk
    name: Apache HttpComponents Java SDK
    description: Maven artifact for Apache HttpComponents HttpClient 5.x providing full HTTP client functionality including fluent API, async client, and reactive streams support.
    humanURL: https://hc.apache.org/httpcomponents-client-5.3.x/dependency-info.html
    tags:
      - Java
      - Maven
      - SDK
    properties:
      - type: Documentation
        url: https://hc.apache.org/httpcomponents-client-5.3.x/dependency-info.html
      - type: SDK
        url: https://search.maven.org/artifact/org.apache.httpcomponents.client5/httpclient5
        title: Java SDK (Maven Central)
common:
  - type: Documentation
    url: https://hc.apache.org/
  - type: GettingStarted
    url: https://hc.apache.org/httpcomponents-client-5.3.x/quickstart.html
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/httpcomponents-client
  - type: SpectralRules
    url: rules/apache-http-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-http-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/http-client-integration.yaml
  - type: Features
    data:
      - name: Connection Pooling
        description: Configurable connection pool with per-route and total connection limits for efficient HTTP connection reuse.
      - name: Async HTTP Client
        description: Non-blocking async HTTP client based on Java NIO for high-concurrency request execution.
      - name: TLS/SSL Support
        description: Full TLS/SSL support with customizable trust stores, client certificates, and hostname verification.
      - name: Authentication Framework
        description: Pluggable authentication framework supporting Basic, Digest, NTLM, and Bearer token schemes.
      - name: Cookie Management
        description: RFC-compliant cookie management with customizable cookie stores and policies.
      - name: Proxy Support
        description: HTTP, HTTPS, and SOCKS proxy support with proxy authentication.
      - name: Content Negotiation
        description: Built-in content encoding, compression (gzip/deflate), and charset negotiation.
      - name: Fluent API
        description: High-level fluent API for simplified one-liner HTTP request execution.
  - type: UseCases
    data:
      - name: REST API Client Integration
        description: Consume REST APIs from Java applications with connection pooling and retry logic.
      - name: Web Scraping
        description: Crawl and fetch web content with cookie handling and redirect following.
      - name: Microservices HTTP Communication
        description: Make service-to-service HTTP calls with connection reuse and timeout configuration.
      - name: Authentication Token Refresh
        description: Implement OAuth2 token refresh flows using the authentication interceptor framework.
      - name: File Upload and Download
        description: Stream large file uploads and downloads via multipart or chunked transfer encoding.
  - type: Integrations
    data:
      - name: Spring Framework
        description: Spring RestTemplate and WebClient use Apache HttpComponents as a configurable HTTP backend.
      - name: Apache CXF
        description: Apache CXF JAX-RS client uses HttpComponents for HTTP transport in web service calls.
      - name: Elasticsearch Java Client
        description: Elasticsearch Java client uses HttpComponents for transport-layer HTTP communication.
      - name: Apache Solr
        description: Apache Solr Java client (SolrJ) uses HttpComponents for Solr HTTP API calls.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
