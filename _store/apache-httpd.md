---
aid: apache-httpd
name: Apache HTTP Server
description: Apache HTTP Server (httpd) is the world's most widely used web server software. It serves static and dynamic content, acts as a reverse proxy and load balancer, and exposes a mod_status monitoring API and balancer-manager management interface for operational visibility.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Load Balancer
  - Open Source
  - Proxy
  - Reverse Proxy
  - Web Server
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-httpd/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-httpd:apache-httpd-status-api
    name: Apache HTTP Server Status API
    description: Status and monitoring API for Apache HTTP Server (httpd) provided by mod_status, exposing server metrics, worker state, and load balancer information via HTTP endpoints.
    humanURL: https://httpd.apache.org/docs/current/mod/mod_status.html
    baseURL: http://localhost:80
    tags:
      - Balancer
      - Metrics
      - Monitoring
      - REST
      - Status
    properties:
      - type: Documentation
        url: https://httpd.apache.org/docs/current/mod/mod_status.html
      - type: OpenAPI
        url: openapi/apache-httpd-status-openapi.yml
      - type: JSONSchema
        url: json-schema/httpd-serverstatus-schema.json
      - type: JSON-LD
        url: json-ld/apache-httpd-status-context.jsonld
  - aid: apache-httpd:apache-httpd-config-api
    name: Apache HTTP Server Configuration Reference
    description: Configuration directive reference for Apache HTTP Server covering VirtualHost, mod_ssl, mod_rewrite, mod_proxy, and all core directives for web server, proxy, and SSL configuration.
    humanURL: https://httpd.apache.org/docs/current/mod/directives.html
    tags:
      - Configuration
      - Reference
    properties:
      - type: Documentation
        url: https://httpd.apache.org/docs/current/mod/directives.html
common:
  - type: Documentation
    url: https://httpd.apache.org/docs/current/
  - type: GettingStarted
    url: https://httpd.apache.org/docs/current/getting-started.html
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/httpd
  - type: SpectralRules
    url: rules/apache-httpd-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-httpd-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/httpd-server-monitoring.yaml
  - type: Features
    data:
      - name: mod_status Monitoring
        description: Real-time server status endpoint providing request rates, worker states, and CPU usage.
      - name: mod_proxy Reverse Proxy
        description: Full-featured reverse proxy with HTTP, HTTPS, WebSocket, and AJP protocol support.
      - name: mod_proxy_balancer Load Balancing
        description: Load balancing across backend servers with byrequests, bytraffic, and bybusyness algorithms.
      - name: mod_ssl TLS Termination
        description: TLS/SSL termination with client certificate authentication and OCSP stapling support.
      - name: mod_rewrite URL Rewriting
        description: Powerful rule-based URL rewriting engine for redirects, proxying, and access control.
      - name: Virtual Hosting
        description: Name-based and IP-based virtual hosting for serving multiple domains from a single server.
      - name: CGI and FastCGI
        description: CGI and FastCGI support for dynamic content generation with external applications.
      - name: .htaccess Per-Directory Config
        description: Per-directory configuration files for decentralized access control and configuration.
  - type: UseCases
    data:
      - name: Static Web Hosting
        description: Serve HTML, CSS, JavaScript, and media files with high performance and caching headers.
      - name: Reverse Proxy for Applications
        description: Proxy requests to application servers (Node.js, Python, Java) with SSL termination.
      - name: Load Balancing
        description: Distribute traffic across multiple backend application instances with health checking.
      - name: API Gateway
        description: Route and transform API requests using mod_rewrite and mod_proxy rules.
      - name: Legacy CGI Application Hosting
        description: Run legacy CGI or PHP applications via mod_cgi, mod_fcgid, or mod_php.
  - type: Integrations
    data:
      - name: mod_php
        description: Embeds PHP interpreter directly in the Apache process for PHP application hosting.
      - name: Tomcat AJP Connector
        description: AJP protocol integration with Apache Tomcat for Java web application proxying.
      - name: Let's Encrypt / Certbot
        description: Automated TLS certificate provisioning with Certbot and the mod_md module.
      - name: Nginx
        description: Often deployed alongside Nginx, with Nginx handling static files and Apache handling dynamic content.
      - name: ModSecurity WAF
        description: ModSecurity web application firewall module for OWASP rule-based request filtering.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
