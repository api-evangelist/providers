---
aid: nginx
url: https://raw.githubusercontent.com/api-evangelist/nginx/refs/heads/main/apis.yml
apis:
- aid: nginx:nginx
  name: NGINX
  description: NGINX is a versatile open-source software for web serving, reverse proxying, caching, load balancing, media streaming, and API gateway functionality powering a significant portion of the world's web traffic.
  humanURL: https://nginx.org/
  tags:
  - API Gateway
  - Reverse Proxy
  - Web Server
  properties:
  - type: Documentation
    url: https://nginx.org/en/docs/
  - type: Getting Started
    url: https://nginx.org/en/docs/beginners_guide.html
  - type: Reference
    url: https://nginx.org/en/docs/dirindex.html
  - type: Change Log
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
  properties:
  - type: Documentation
    url: https://nginx.org/en/docs/http/ngx_http_api_module.html
  - type: Reference
    url: https://nginx.org/en/docs/http/ngx_http_api_module.html#api
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
- aid: nginx:nginx-njs
  name: NGINX Njs Scripting API
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
  - type: Reference
    url: https://nginx.org/en/docs/njs/reference.html
  - type: Getting Started
    url: https://nginx.org/en/docs/njs/install.html
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
  - type: Getting Started
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
name: NGINX
tags:
- API Gateway
- Load Balancer
- Open Source
- Reverse Proxy
- Web Server
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: NGINX is a high-performance open-source web server, reverse proxy, and API gateway widely used for load balancing, SSL termination, caching, and traffic management for APIs and microservices.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

