---
aid: nginx
name: NGINX
description: NGINX is a high-performance open-source web server, reverse proxy, and API gateway widely used for load balancing, SSL termination, caching, and traffic management for APIs and microservices. Originally written by Igor Sysoev and released under the 2-clause BSD license, NGINX powers a significant portion of the world's web traffic. Enterprise support and commercial features are available from F5, Inc.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Gateway
  - Caching
  - Cloud Native
  - Load Balancer
  - Open Source
  - Reverse Proxy
  - Web Server
url: https://raw.githubusercontent.com/api-evangelist/nginx/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nginx:nginx
    name: NGINX
    description: NGINX is a versatile open-source software for web serving, reverse proxying, caching, load balancing, media streaming, and API gateway functionality powering a significant portion of the world's web traffic. Licensed under the 2-clause BSD license and governed by F5, Inc.
    humanURL: https://nginx.org/
    tags:
      - API Gateway
      - Load Balancer
      - Open Source
      - Reverse Proxy
      - Web Server
    properties:
      - type: Documentation
        url: https://nginx.org/en/docs/
      - type: GettingStarted
        url: https://nginx.org/en/docs/beginners_guide.html
      - type: APIReference
        url: https://nginx.org/en/docs/dirindex.html
      - type: ChangeLog
        url: https://nginx.org/en/CHANGES
      - type: GitHubRepository
        url: https://github.com/nginx/nginx
  - aid: nginx:nginx-http-api
    name: NGINX Plus HTTP API
    description: The NGINX Plus HTTP API provides a RESTful interface for dynamic configuration and real-time monitoring of a running NGINX Plus instance. It supports managing upstream servers, key-value pairs, and retrieving connection, cache, and rate-limiting statistics without requiring configuration reloads. Available as part of the NGINX commercial subscription.
    humanURL: https://nginx.org/en/docs/http/ngx_http_api_module.html
    tags:
      - Admin
      - Management
      - Monitoring
      - NGINX Plus
      - REST API
    properties:
      - type: Documentation
        url: https://nginx.org/en/docs/http/ngx_http_api_module.html
      - type: APIReference
        url: https://nginx.org/en/docs/http/ngx_http_api_module.html#api
      - type: OpenAPI
        url: openapi/nginx-plus-http-api-openapi.yaml
      - type: JSONLD
        url: json-ld/nginx-plus-http-api-context.jsonld
      - type: SDK
        url: https://github.com/nginx/nginx-plus-go-client
        title: Go SDK
  - aid: nginx:nginx-stub-status
    name: NGINX Stub Status API
    description: The NGINX Stub Status module exposes a simple HTTP endpoint providing basic server performance metrics including active connections, total accepts, handled connections, and request counts. It is available in open-source NGINX and must be enabled at compile time with the --with-http_stub_status_module flag.
    humanURL: https://nginx.org/en/docs/http/ngx_http_stub_status_module.html
    tags:
      - Metrics
      - Monitoring
      - Open Source
      - Status
    properties:
      - type: Documentation
        url: https://nginx.org/en/docs/http/ngx_http_stub_status_module.html
      - type: OpenAPI
        url: openapi/nginx-stub-status-openapi.yaml
  - aid: nginx:nginx-njs
    name: NGINX njs Scripting API
    description: The NGINX njs module embeds a JavaScript (ECMAScript 5.1+) runtime into NGINX, allowing developers to write custom request/response handlers, access control logic, and content filters. It provides HTTP and stream request objects, a Fetch-compatible web API, cryptographic functions, and built-in modules for file system, XML, and query string operations.
    humanURL: https://nginx.org/en/docs/njs/
    tags:
      - Extensibility
      - JavaScript
      - Modules
      - Scripting
    properties:
      - type: Documentation
        url: https://nginx.org/en/docs/njs/
      - type: APIReference
        url: https://nginx.org/en/docs/njs/reference.html
      - type: GettingStarted
        url: https://nginx.org/en/docs/njs/install.html
      - type: OpenAPI
        url: openapi/nginx-njs-openapi.yaml
      - type: JSONLD
        url: json-ld/nginx-context.jsonld
      - type: GitHubRepository
        url: https://github.com/nginx/njs
  - aid: nginx:nginx-ingress-controller
    name: NGINX Ingress Controller
    description: The NGINX Ingress Controller is a Kubernetes-native ingress controller built on NGINX that manages external access to services in a Kubernetes cluster. It supports TLS termination, path-based routing, rate limiting, and advanced traffic management through annotations and custom resources.
    humanURL: https://github.com/nginx/kubernetes-ingress
    tags:
      - Cloud Native
      - Ingress
      - Kubernetes
      - Traffic Management
    properties:
      - type: Documentation
        url: https://docs.nginx.com/nginx-ingress-controller/
      - type: GettingStarted
        url: https://docs.nginx.com/nginx-ingress-controller/installation/installing-nic/
      - type: GitHubRepository
        url: https://github.com/nginx/kubernetes-ingress
  - aid: nginx:nginx-gateway-fabric
    name: NGINX Gateway Fabric
    description: NGINX Gateway Fabric is a Kubernetes Gateway API implementation using NGINX as the data plane. It provides standards-based traffic management through Gateway API resources including Gateway, HTTPRoute, GRPCRoute, and TLSRoute, enabling fine-grained control over ingress and routing in Kubernetes environments.
    humanURL: https://github.com/nginx/nginx-gateway-fabric
    tags:
      - Cloud Native
      - Gateway API
      - Kubernetes
      - Routing
    properties:
      - type: Documentation
        url: https://docs.nginx.com/nginx-gateway-fabric/
      - type: GitHubRepository
        url: https://github.com/nginx/nginx-gateway-fabric
  - aid: nginx:nginx-agent
    name: NGINX Agent
    description: NGINX Agent provides an administrative entry point to remotely manage, configure, and collect metrics and events from NGINX instances. It enables centralized management of distributed NGINX deployments through a gRPC-based control plane interface.
    humanURL: https://github.com/nginx/agent
    tags:
      - Agent
      - Management
      - Monitoring
      - Remote Administration
    properties:
      - type: Documentation
        url: https://github.com/nginx/agent
      - type: GitHubRepository
        url: https://github.com/nginx/agent
common:
  - type: Website
    url: https://nginx.org/
  - type: Documentation
    url: https://nginx.org/en/docs/
  - type: GettingStarted
    url: https://nginx.org/en/docs/beginners_guide.html
  - type: Blog
    url: https://blog.nginx.org/
  - type: ChangeLog
    url: https://nginx.org/en/CHANGES
  - type: Security
    url: https://nginx.org/en/security_advisories.html
  - type: Support
    url: https://community.nginx.org
  - type: GitHubOrganization
    url: https://github.com/nginx
  - type: GitHubRepository
    url: https://github.com/nginx/nginx
  - type: YouTube
    url: https://www.youtube.com/nginxinc
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/nginx
  - type: X
    url: https://x.com/nginxorg
  - type: FAQ
    url: https://nginx.org/en/docs/faq.html
  - type: CLI
    url: https://github.com/nginx/nginx-prometheus-exporter
    title: Prometheus Exporter
  - type: SDK
    url: https://www.npmjs.com/package/@nginx/reference-lib
    title: Directive Reference Library (npm)
  - type: SDK
    url: https://crates.io/crates/ngx
    title: Rust Bindings (crates.io)
  - type: CodeExamples
    url: https://github.com/nginx/nginx-demos
    title: NGINX Demos
  - type: CodeExamples
    url: https://github.com/nginx/njs-examples
    title: njs Examples
  - type: SpectralRules
    url: rules/nginx-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/nginx-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/traffic-management.yaml
    title: Traffic Management
  - type: NaftikoCapability
    url: capabilities/monitoring-and-observability.yaml
    title: Monitoring and Observability
  - type: Features
    data:
      - name: HTTP Web Server
        description: High-performance HTTP and HTTPS server with support for HTTP/1.1, HTTP/2, HTTP/3, and early hints (103).
      - name: Reverse Proxy
        description: Forward client requests to backend application servers with load balancing, buffering, and caching.
      - name: Load Balancing
        description: Distribute traffic across upstream servers using round-robin, least-connections, IP hash, and sticky session algorithms.
      - name: SSL/TLS Termination
        description: Terminate and offload SSL/TLS connections at the proxy layer with support for SNI, OCSP stapling, and encrypted client hello.
      - name: Content Caching
        description: Cache responses from upstream servers to reduce backend load and improve response times.
      - name: gRPC Proxying
        description: Route and load balance gRPC traffic to backend services.
      - name: WebSocket Support
        description: Proxy WebSocket connections for real-time bidirectional communication.
      - name: TCP/UDP Proxy
        description: Stream module for proxying and load balancing arbitrary TCP and UDP traffic.
      - name: Mail Proxy
        description: Proxy IMAP, POP3, and SMTP mail protocols with authentication support.
      - name: Dynamic Modules
        description: Extend functionality at runtime through loadable modules without recompiling.
      - name: njs Scripting
        description: Embed JavaScript logic for custom request handling, access control, and content filtering.
      - name: OpenTelemetry
        description: Built-in OpenTelemetry module for distributed tracing and observability.
  - type: UseCases
    data:
      - name: API Gateway
        description: Route, authenticate, rate limit, and load balance API traffic across microservices.
      - name: Kubernetes Ingress
        description: Manage external access to Kubernetes services with the NGINX Ingress Controller or Gateway Fabric.
      - name: Content Delivery
        description: Cache and serve static content close to users with high throughput and low latency.
      - name: Microservices Proxy
        description: Act as a sidecar or edge proxy for service-to-service communication in microservices architectures.
      - name: SSL Offloading
        description: Terminate TLS at the edge to reduce cryptographic overhead on backend application servers.
      - name: Load Balancing
        description: Distribute HTTP, TCP, UDP, and gRPC traffic across pools of upstream servers for high availability.
  - type: Integrations
    data:
      - name: Kubernetes
        description: Native Kubernetes integration through NGINX Ingress Controller and Gateway Fabric.
      - name: OpenTelemetry
        description: Built-in ngx_otel_module for exporting traces to OpenTelemetry collectors.
      - name: Prometheus
        description: Expose metrics for scraping by Prometheus via stub status or the NGINX Plus API.
      - name: Ansible
        description: Official Ansible roles for automated NGINX installation and configuration management.
      - name: Docker
        description: Official Docker images for containerized NGINX deployments.
      - name: Helm
        description: Helm charts for deploying NGINX Ingress Controller and Gateway Fabric on Kubernetes.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
