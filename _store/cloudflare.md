---
aid: cloudflare
url: https://raw.githubusercontent.com/api-search/infrastructure/main/_apis/cloudflare/apis.md
apis:
  - aid: cloudflare:cloudflare-api
    name: Cloudflare API
    tags:
      - Cloud
      - Infrastructure
    baseURL: https://api.cloudflare.com
    contact:
      - FN: Support
        url: https://support.cloudflare.com/
        email: ''
    humanURL: https://developers.cloudflare.com/api/
    properties:
      - url: openapi/cloudflare-openapi-original.yml
        type: OpenAPI
      - url: asyncapi/cloudflare-notifications-webhooks-asyncapi.yml
        type: AsyncAPI
      - url: https://developers.cloudflare.com/api/
        type: Documentation
      - url: https://developers.cloudflare.com/fundamentals/api/get-started/
        type: GettingStarted
      - url: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
        type: Authentication
      - url: https://developers.cloudflare.com/fundamentals/api/reference/sdks/
        type: SDK
      - url: https://developers.cloudflare.com/fundamentals/api/reference/limits/
        type: RateLimits
    description: Easily integrate with Cloudflare's products and services using the Cloudflare API. Authentication is essential when utilizing the API to ensure proper authorization and access control. Generate an API token to enable performing various actions with the API.
  - aid: cloudflare:cloudflare-accounts-api
    name: Cloudflare Accounts API
    tags:
      - Accounts
      - Management
    humanURL: https://developers.cloudflare.com/api/operations/accounts-list-accounts
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-accounts--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/operations/accounts-list-accounts
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/accounts/
        type: APIReference
    description: Managing all the details of your Cloudflare Account using the API.
  - aid: cloudflare:cloudflare-certificates-api
    name: Cloudflare Certificates API
    tags:
      - Certificates
      - Security
      - SSL
    humanURL: https://developers.cloudflare.com/api/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-certificates--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/
        type: Documentation
      - url: https://developers.cloudflare.com/ssl/
        type: APIReference
    description: Managing certificates used across Cloudflare.
  - aid: cloudflare:cloudflare-ip-addresses-api
    name: Cloudflare IP Addresses API
    tags:
      - IP Addresses
    humanURL: https://developers.cloudflare.com/api/operations/ip-access-rules-for-a-user-list-ip-access-rules
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-ips--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/operations/ip-access-rules-for-a-user-list-ip-access-rules
        type: Documentation
    description: Provides the ability to manage IP addresses used across a Cloudflare account.
  - aid: cloudflare:cloudflare-memberships-api
    name: Cloudflare Memberships API
    tags:
      - Details
      - Memberships
    humanURL: https://developers.cloudflare.com/api/operations/user'-s-account-memberships-list-memberships
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-memberships--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/operations/user'-s-account-memberships-list-memberships
        type: Documentation
    description: Provides the ability to manage memberships across accounts.
  - aid: cloudflare:cloudflare-radar-api
    name: Cloudflare Radar API
    tags:
      - Analytics
      - Internet Traffic
      - Radar
    humanURL: https://developers.cloudflare.com/api/operations/radar-get-search-global
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-radar--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/operations/radar-get-search-global
        type: Documentation
      - url: https://developers.cloudflare.com/radar/
        type: APIReference
      - url: https://developers.cloudflare.com/radar/get-started/
        type: GettingStarted
    description: Provides the ability to access all of Cloudflare's radar capabilities.
  - aid: cloudflare:cloudflare-user-api
    name: Cloudflare User API
    tags:
      - Users
    humanURL: https://developers.cloudflare.com/api/operations/user-user-details
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-user--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/operations/user-user-details
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/user/
        type: APIReference
    description: Provides the ability to manage all of the users across a Cloudflare account.
  - aid: cloudflare:cloudflare-zones-api
    name: Cloudflare Zones API
    tags:
      - DNS
      - Domains
      - Zones
    humanURL: https://developers.cloudflare.com/api/operations/zones-get
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-zones--openapi-original.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/api/operations/zones-get
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/zones/
        type: APIReference
    description: Provides the ability to manage DNS Zones across the Cloudflare platform.
  - aid: cloudflare:cloudflare-dns-api
    name: Cloudflare DNS API
    tags:
      - DNS
      - Domains
      - Nameservers
    humanURL: https://developers.cloudflare.com/dns/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-dns-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/dns/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/dns/
        type: APIReference
    description: The Cloudflare DNS API allows developers to programmatically manage DNS records for their zones, including creating, listing, updating, and deleting records. It also supports batch operations, DNS record scanning, and DNSSEC configuration.
  - aid: cloudflare:cloudflare-workers-api
    name: Cloudflare Workers API
    tags:
      - Edge Computing
      - Functions
      - Serverless
    humanURL: https://developers.cloudflare.com/workers/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-workers-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/workers/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/workers/
        type: APIReference
      - url: https://developers.cloudflare.com/workers/get-started/
        type: GettingStarted
    description: Cloudflare Workers allows developers to deploy serverless code to Cloudflare's global network. The Workers API provides endpoints for managing worker scripts, versions, deployments, and configuration including bindings, routes, and custom domains.
  - aid: cloudflare:cloudflare-workers-ai-api
    name: Cloudflare Workers AI API
    tags:
      - Artificial Intelligence
      - Inference
      - Machine Learning
    humanURL: https://developers.cloudflare.com/workers-ai/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-workers-ai-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/workers-ai/
        type: Documentation
      - url: https://developers.cloudflare.com/workers-ai/get-started/rest-api/
        type: GettingStarted
      - url: https://developers.cloudflare.com/workers-ai/configuration/open-ai-compatibility/
        type: APIReference
    description: The Cloudflare Workers AI API enables developers to run machine learning models on Cloudflare's global network via a REST API. It supports text generation, embeddings, image classification, speech recognition, and other AI tasks with OpenAI-compatible endpoints.
  - aid: cloudflare:cloudflare-ai-gateway-api
    name: Cloudflare AI Gateway API
    tags:
      - Artificial Intelligence
      - Gateway
      - Observability
    humanURL: https://developers.cloudflare.com/ai-gateway/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-ai-gateway-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/ai-gateway/
        type: Documentation
      - url: https://developers.cloudflare.com/ai-gateway/get-started/
        type: GettingStarted
    description: Cloudflare AI Gateway provides visibility and control over AI applications with analytics, logging, caching, rate limiting, request retries, and model fallback. It supports multiple AI providers including OpenAI, Anthropic, and Google Gemini through a unified interface.
  - aid: cloudflare:cloudflare-r2-api
    name: Cloudflare R2 API
    tags:
      - Object Storage
      - S3 Compatible
      - Storage
    humanURL: https://developers.cloudflare.com/r2/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-r2-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/r2/
        type: Documentation
      - url: https://developers.cloudflare.com/r2/api/s3/api/
        type: APIReference
      - url: https://developers.cloudflare.com/r2/get-started/
        type: GettingStarted
    description: Cloudflare R2 is S3-compatible object storage with zero egress fees. The R2 API allows developers to create and manage buckets, upload and retrieve objects, and configure access controls. R2 supports the S3 API for compatibility with existing tools and SDKs.
  - aid: cloudflare:cloudflare-d1-api
    name: Cloudflare D1 API
    tags:
      - Database
      - Serverless
      - SQL
    humanURL: https://developers.cloudflare.com/d1/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-d1-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/d1/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/d1/
        type: APIReference
      - url: https://developers.cloudflare.com/d1/get-started/
        type: GettingStarted
    description: The Cloudflare D1 API provides endpoints for managing serverless SQL databases on Cloudflare's network. Developers can create, list, and delete databases, as well as execute raw queries and export database contents via the REST API.
  - aid: cloudflare:cloudflare-kv-api
    name: Cloudflare KV API
    tags:
      - Key Value
      - Serverless
      - Storage
    humanURL: https://developers.cloudflare.com/kv/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-kv-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/kv/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/kv/
        type: APIReference
      - url: https://developers.cloudflare.com/kv/get-started/
        type: GettingStarted
    description: Cloudflare Workers KV is a global, low-latency key-value data store. The KV API allows developers to create namespaces, write and read key-value pairs, list keys, and perform bulk operations with support for up to 10,000 key-value pairs per request.
  - aid: cloudflare:cloudflare-queues-api
    name: Cloudflare Queues API
    tags:
      - Messaging
      - Queues
      - Serverless
    humanURL: https://developers.cloudflare.com/queues/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-queues-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/queues/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/queues/
        type: APIReference
      - url: https://developers.cloudflare.com/queues/get-started/
        type: GettingStarted
    description: The Cloudflare Queues API enables developers to create and manage message queues that integrate with Cloudflare Workers. Queues support guaranteed delivery, work offloading from requests, worker-to-worker communication, and data buffering and batching.
  - aid: cloudflare:cloudflare-durable-objects-api
    name: Cloudflare Durable Objects API
    tags:
      - Serverless
      - Stateful
      - Storage
    humanURL: https://developers.cloudflare.com/durable-objects/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-durable-objects-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/durable-objects/
        type: Documentation
      - url: https://developers.cloudflare.com/durable-objects/get-started/
        type: GettingStarted
      - url: https://developers.cloudflare.com/durable-objects/api/
        type: APIReference
    description: Cloudflare Durable Objects combine compute with persistent storage in a single Worker. The API provides transactional and strongly consistent storage with support for SQL, key-value, alarms, and WebSocket hibernation for building stateful serverless applications.
  - aid: cloudflare:cloudflare-vectorize-api
    name: Cloudflare Vectorize API
    tags:
      - AI
      - Embeddings
      - Vector Database
    humanURL: https://developers.cloudflare.com/vectorize/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-vectorize-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/vectorize/
        type: Documentation
      - url: https://developers.cloudflare.com/vectorize/get-started/intro/
        type: GettingStarted
      - url: https://developers.cloudflare.com/vectorize/reference/client-api/
        type: APIReference
    description: Cloudflare Vectorize is a globally distributed vector database for building AI-powered applications. The API allows developers to create indexes, insert and upsert vectors, and perform similarity queries for semantic search, recommendations, and classification tasks.
  - aid: cloudflare:cloudflare-pages-api
    name: Cloudflare Pages API
    tags:
      - Deployment
      - Hosting
      - JAMstack
    humanURL: https://developers.cloudflare.com/pages/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-pages-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/pages/
        type: Documentation
      - url: https://developers.cloudflare.com/pages/configuration/api/
        type: APIReference
      - url: https://developers.cloudflare.com/pages/get-started/
        type: GettingStarted
    description: The Cloudflare Pages API enables developers to build automations and integrate Pages with their development workflow. It provides endpoints to manage projects, deployments, and builds, including creating deployments, rolling back, and configuring build settings.
  - aid: cloudflare:cloudflare-stream-api
    name: Cloudflare Stream API
    tags:
      - Media
      - Streaming
      - Video
    humanURL: https://developers.cloudflare.com/stream/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-stream-openapi.yml
        type: OpenAPI
      - url: asyncapi/cloudflare-stream-webhooks-asyncapi.yml
        type: AsyncAPI
      - url: https://developers.cloudflare.com/stream/
        type: Documentation
      - url: https://developers.cloudflare.com/stream/get-started/
        type: GettingStarted
      - url: https://developers.cloudflare.com/api/resources/stream/
        type: APIReference
    description: Cloudflare Stream provides a single API for uploading, storing, encoding, and delivering live and on-demand video. The API supports direct uploads, TUS resumable uploads, live streaming via RTMPS and SRT, video playback with a built-in player, and signed URL access control.
  - aid: cloudflare:cloudflare-images-api
    name: Cloudflare Images API
    tags:
      - Images
      - Media
      - Transformation
    humanURL: https://developers.cloudflare.com/images/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-images-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/images/
        type: Documentation
      - url: https://developers.cloudflare.com/images/get-started/
        type: GettingStarted
      - url: https://developers.cloudflare.com/api/resources/images/
        type: APIReference
    description: The Cloudflare Images API allows developers to upload, store, and transform images at scale. It supports direct uploads, URL-based uploads, on-the-fly image transformations via URL parameters, and integration with Workers for programmatic image processing.
  - aid: cloudflare:cloudflare-turnstile-api
    name: Cloudflare Turnstile API
    tags:
      - Bot Protection
      - CAPTCHA
      - Security
    humanURL: https://developers.cloudflare.com/turnstile/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-turnstile-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/turnstile/
        type: Documentation
      - url: https://developers.cloudflare.com/turnstile/get-started/
        type: GettingStarted
      - url: https://developers.cloudflare.com/api/resources/turnstile/
        type: APIReference
    description: Cloudflare Turnstile is a CAPTCHA replacement that verifies visitors without showing a challenge. The API provides a widget for client-side integration and a server-side siteverify endpoint for token validation, with support for managed, non-interactive, and invisible modes.
  - aid: cloudflare:cloudflare-load-balancing-api
    name: Cloudflare Load Balancing API
    tags:
      - Load Balancing
      - Performance
      - Traffic Management
    humanURL: https://developers.cloudflare.com/load-balancing/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/load-balancing/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/load_balancers/
        type: APIReference
      - url: https://developers.cloudflare.com/load-balancing/get-started/
        type: GettingStarted
    description: The Cloudflare Load Balancing API enables developers to distribute traffic across endpoints to reduce strain and latency. It provides endpoints for managing load balancers, pools, monitors, and health checks with support for geographic steering and session affinity.
  - aid: cloudflare:cloudflare-waf-api
    name: Cloudflare WAF API
    tags:
      - Rules
      - Security
      - Web Application Firewall
    humanURL: https://developers.cloudflare.com/waf/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/waf/
        type: Documentation
      - url: https://developers.cloudflare.com/waf/get-started/
        type: GettingStarted
    description: The Cloudflare Web Application Firewall API checks incoming web and API requests and filters undesired traffic using rulesets. It supports managed rules, custom rules, rate limiting rules, and provides endpoints for deploying and managing rulesets via the Rulesets API.
  - aid: cloudflare:cloudflare-logpush-api
    name: Cloudflare Logpush API
    tags:
      - Analytics
      - Logs
      - Observability
    humanURL: https://developers.cloudflare.com/logs/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-logpush-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/logs/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/logpush/
        type: APIReference
      - url: https://developers.cloudflare.com/logs/get-started/
        type: GettingStarted
    description: The Cloudflare Logpush API allows developers to configure jobs that push logs to storage services, SIEMs, and log management providers. It supports datasets including HTTP requests, firewall events, DNS logs, and spectrum events with configurable output options.
  - aid: cloudflare:cloudflare-graphql-analytics-api
    name: Cloudflare GraphQL Analytics API
    tags:
      - Analytics
      - GraphQL
      - Reporting
    humanURL: https://developers.cloudflare.com/analytics/graphql-api/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/analytics/graphql-api/
        type: Documentation
      - url: https://developers.cloudflare.com/analytics/graphql-api/getting-started/
        type: GettingStarted
    description: The Cloudflare GraphQL Analytics API provides flexible access to analytics data across Cloudflare products including HTTP requests, firewall events, and load balancing metrics. Developers can query specific datasets, filter by dimensions, and aggregate data for custom reporting.
  - aid: cloudflare:cloudflare-magic-transit-api
    name: Cloudflare Magic Transit API
    tags:
      - DDoS Protection
      - Network Security
      - Networking
    humanURL: https://developers.cloudflare.com/magic-transit/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/magic-transit/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/magic_transit/
        type: APIReference
      - url: https://developers.cloudflare.com/magic-transit/get-started/
        type: GettingStarted
    description: The Cloudflare Magic Transit API provides endpoints for managing network security and performance for on-premises, cloud-hosted, and hybrid networks. It supports managing sites, site ACLs, static routes, GRE tunnels, and network interconnects for DDoS protection and traffic acceleration.
  - aid: cloudflare:cloudflare-email-routing-api
    name: Cloudflare Email Routing API
    tags:
      - Email
      - Messaging
      - Routing
    humanURL: https://developers.cloudflare.com/email-routing/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/email-routing/
        type: Documentation
    description: The Cloudflare Email Routing API enables developers to create and manage custom email addresses and routing rules for their domains. It supports forwarding emails to destination addresses, creating catch-all rules, and integrating with Workers for programmatic email processing.
  - aid: cloudflare:cloudflare-waiting-room-api
    name: Cloudflare Waiting Room API
    tags:
      - Performance
      - Queue
      - Traffic Management
    humanURL: https://developers.cloudflare.com/waiting-room/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/waiting-room/
        type: Documentation
    description: The Cloudflare Waiting Room API allows developers to manage virtual waiting rooms that route excess visitors to a customizable queue during high traffic. It provides endpoints for creating waiting rooms, configuring thresholds, and managing rules for session handling.
  - aid: cloudflare:cloudflare-spectrum-api
    name: Cloudflare Spectrum API
    tags:
      - DDoS Protection
      - TCP
      - UDP
    humanURL: https://developers.cloudflare.com/spectrum/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/spectrum/
        type: Documentation
    description: Cloudflare Spectrum extends Cloudflare's DDoS protection and performance benefits to any TCP or UDP application. The API enables developers to manage Spectrum applications, configure origin connections, and apply IP firewall rules to non-HTTP traffic.
  - aid: cloudflare:cloudflare-hyperdrive-api
    name: Cloudflare Hyperdrive API
    tags:
      - Connection Pooling
      - Database
      - Performance
    humanURL: https://developers.cloudflare.com/hyperdrive/
    baseURL: https://api.cloudflare.com
    properties:
      - url: openapi/cloudflare-hyperdrive-openapi.yml
        type: OpenAPI
      - url: https://developers.cloudflare.com/hyperdrive/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/hyperdrive/
        type: APIReference
      - url: https://developers.cloudflare.com/hyperdrive/get-started/
        type: GettingStarted
    description: Cloudflare Hyperdrive accelerates access to existing databases from Cloudflare Workers by providing connection pooling and query caching at the edge. The API allows developers to create and manage Hyperdrive configurations that connect to PostgreSQL and other databases.
  - aid: cloudflare:cloudflare-api-shield-api
    name: Cloudflare API Shield API
    tags:
      - API Gateway
      - API Security
      - Schema Validation
    humanURL: https://developers.cloudflare.com/api-shield/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/api-shield/
        type: Documentation
      - url: https://developers.cloudflare.com/api-shield/get-started/
        type: GettingStarted
      - url: https://developers.cloudflare.com/api/resources/api_gateway/
        type: APIReference
    description: Cloudflare API Shield provides API discovery, schema validation, and security features to protect APIs from abuse. It includes API Gateway capabilities for routing, authentication, and rate limiting, along with sequence-based fraud detection and mTLS client certificate enforcement.
  - aid: cloudflare:cloudflare-zero-trust-api
    name: Cloudflare Zero Trust API
    tags:
      - Access Control
      - Security
      - Zero Trust
    humanURL: https://developers.cloudflare.com/cloudflare-one/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/cloudflare-one/
        type: Documentation
      - url: https://developers.cloudflare.com/cloudflare-one/api-terraform/
        type: APIReference
    description: The Cloudflare Zero Trust API enables developers to manage secure access to applications and networks without a traditional VPN. It includes Access policies, Gateway DNS and HTTP filtering, Tunnel management, device posture checks, and Data Loss Prevention configuration.
  - aid: cloudflare:cloudflare-registrar-api
    name: Cloudflare Registrar API
    tags:
      - DNS
      - Domains
      - Registration
    humanURL: https://developers.cloudflare.com/registrar/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/registrar/
        type: Documentation
    description: The Cloudflare Registrar API allows developers to manage domain registrations at cost. It provides endpoints for listing domains, updating domain contacts, configuring DNSSEC, and managing domain transfers and renewals.
  - aid: cloudflare:cloudflare-workflows-api
    name: Cloudflare Workflows API
    tags:
      - Durable Execution
      - Serverless
      - Workflows
    humanURL: https://developers.cloudflare.com/workflows/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/workflows/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/workflows/
        type: APIReference
      - url: https://developers.cloudflare.com/workflows/get-started/
        type: GettingStarted
    description: Cloudflare Workflows enables developers to build durable, multi-step applications on Workers that automatically retry failed tasks and persist state for minutes, hours, or weeks. The API provides endpoints for creating, managing, and monitoring workflow instances with support for step functions, sleep, and event-driven execution.
  - aid: cloudflare:cloudflare-browser-rendering-api
    name: Cloudflare Browser Rendering API
    tags:
      - Browser Automation
      - Headless Browser
      - Rendering
    humanURL: https://developers.cloudflare.com/browser-rendering/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/browser-rendering/
        type: Documentation
      - url: https://developers.cloudflare.com/browser-rendering/rest-api/
        type: APIReference
      - url: https://developers.cloudflare.com/api/resources/browser_rendering/
        type: APIReference
    description: The Cloudflare Browser Rendering API enables developers to control headless browser instances on Cloudflare's global network. The REST API provides endpoints for capturing screenshots, extracting HTML content, generating PDFs, scraping elements, and converting pages to markdown, with support for Puppeteer and Playwright automation.
  - aid: cloudflare:cloudflare-realtime-api
    name: Cloudflare Realtime API
    tags:
      - Audio
      - Real-Time Communication
      - Video
      - WebRTC
    humanURL: https://developers.cloudflare.com/realtime/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/realtime/
        type: Documentation
      - url: https://developers.cloudflare.com/realtime/sfu/https-api/
        type: APIReference
      - url: https://developers.cloudflare.com/realtime/turn/
        type: APIReference
    description: The Cloudflare Realtime API provides WebRTC infrastructure for building real-time audio and video applications. It includes a Selective Forwarding Unit (SFU) for media routing across Cloudflare's global network, a managed TURN relay service for NAT traversal, and the RealtimeKit SDK for simplified integration.
  - aid: cloudflare:cloudflare-containers-api
    name: Cloudflare Containers API
    tags:
      - Compute
      - Containers
      - Serverless
    humanURL: https://developers.cloudflare.com/containers/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/containers/
        type: Documentation
      - url: https://developers.cloudflare.com/containers/get-started/
        type: GettingStarted
    description: The Cloudflare Containers API allows developers to run container workloads on Cloudflare's global network, managed directly from Workers code. Containers support full isolation, on-demand scaling, GPU access, and a hybrid model that combines serverless speed with container flexibility for stateful and stateless workloads.
  - aid: cloudflare:cloudflare-ai-search-api
    name: Cloudflare AI Search API
    tags:
      - Artificial Intelligence
      - RAG
      - Search
    humanURL: https://developers.cloudflare.com/ai-search/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/ai-search/
        type: Documentation
      - url: https://developers.cloudflare.com/ai-search/usage/rest-api/
        type: APIReference
      - url: https://developers.cloudflare.com/ai-search/get-started/
        type: GettingStarted
    description: The Cloudflare AI Search API provides fully managed retrieval-augmented generation (RAG) pipelines. Developers upload documents to R2 and AI Search handles embeddings, indexing, retrieval, and response generation via a REST API, enabling context-aware AI search without managing infrastructure.
  - aid: cloudflare:cloudflare-agents-api
    name: Cloudflare Agents API
    tags:
      - Agents
      - Artificial Intelligence
      - Serverless
    humanURL: https://developers.cloudflare.com/agents/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/agents/
        type: Documentation
      - url: https://developers.cloudflare.com/agents/api-reference/
        type: APIReference
      - url: https://developers.cloudflare.com/agents/getting-started/
        type: GettingStarted
    description: The Cloudflare Agents SDK enables developers to build and deploy AI-powered agents that autonomously perform tasks, communicate with clients in real time, call AI models, persist state, schedule tasks, and support human-in-the-loop interactions. It integrates with Workers AI, Durable Objects, and MCP.
  - aid: cloudflare:cloudflare-pipelines-api
    name: Cloudflare Pipelines API
    tags:
      - Data Ingestion
      - ETL
      - Streaming
    humanURL: https://developers.cloudflare.com/pipelines/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/pipelines/
        type: Documentation
      - url: https://developers.cloudflare.com/pipelines/getting-started/
        type: GettingStarted
    description: The Cloudflare Pipelines API enables developers to ingest events via HTTP endpoints or Worker bindings, transform data with SQL, and deliver it to R2 as Apache Iceberg tables or Parquet and JSON files. Pipelines support durable buffered queues with exactly-once delivery guarantees.
  - aid: cloudflare:cloudflare-ddos-protection-api
    name: Cloudflare DDoS Protection API
    tags:
      - DDoS Protection
      - Rules
      - Security
    humanURL: https://developers.cloudflare.com/ddos-protection/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/ddos-protection/
        type: Documentation
      - url: https://developers.cloudflare.com/ddos-protection/get-started/
        type: GettingStarted
    description: The Cloudflare DDoS Protection API provides managed rulesets for mitigating DDoS attacks at both the application and network layers. Developers can configure HTTP and network-layer attack protection overrides, adjust sensitivity levels, and customize actions via the Rulesets API.
  - aid: cloudflare:cloudflare-zaraz-api
    name: Cloudflare Zaraz API
    tags:
      - Analytics
      - Performance
      - Third-Party Tools
    humanURL: https://developers.cloudflare.com/zaraz/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/zaraz/
        type: Documentation
      - url: https://developers.cloudflare.com/zaraz/get-started/
        type: GettingStarted
    description: The Cloudflare Zaraz API allows developers to load and manage third-party tools in the cloud instead of the browser. It provides a unified web API with track, set, and ecommerce methods for sending events to third-party tools, improving page load performance and privacy.
  - aid: cloudflare:cloudflare-secrets-store-api
    name: Cloudflare Secrets Store API
    tags:
      - Configuration
      - Secrets Management
      - Security
    humanURL: https://developers.cloudflare.com/secrets-store/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/secrets-store/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/secrets_store/
        type: APIReference
    description: The Cloudflare Secrets Store API enables developers to securely encrypt and store sensitive information as secrets that are reusable across a Cloudflare account. It provides endpoints for managing stores and secrets, with integration into Workers and AI Gateway for runtime access.
  - aid: cloudflare:cloudflare-web-analytics-api
    name: Cloudflare Web Analytics API
    tags:
      - Analytics
      - Performance
      - RUM
    humanURL: https://developers.cloudflare.com/web-analytics/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/web-analytics/
        type: Documentation
      - url: https://developers.cloudflare.com/web-analytics/get-started/
        type: GettingStarted
    description: The Cloudflare Web Analytics API provides privacy-first real user measurement (RUM) analytics for websites. It uses a lightweight JavaScript beacon to collect performance data via the Performance API without cookies or IP tracking, with support for automatic and manual injection.
  - aid: cloudflare:cloudflare-cache-api
    name: Cloudflare Cache API
    tags:
      - Caching
      - CDN
      - Performance
    humanURL: https://developers.cloudflare.com/cache/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/cache/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/cache/
        type: APIReference
    description: The Cloudflare Cache API enables developers to manage CDN caching behavior across Cloudflare's global network. It provides endpoints for purging cached content by URL, prefix, cache tag, or hostname, as well as configuring cache rules, cache reserve, and tiered caching.
  - aid: cloudflare:cloudflare-argo-smart-routing-api
    name: Cloudflare Argo Smart Routing API
    tags:
      - Network Optimization
      - Performance
      - Routing
    humanURL: https://developers.cloudflare.com/argo-smart-routing/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/argo-smart-routing/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/argo/subresources/smart_routing/
        type: APIReference
      - url: https://developers.cloudflare.com/argo-smart-routing/get-started/
        type: GettingStarted
    description: The Cloudflare Argo Smart Routing API enables developers to manage intelligent traffic routing that detects real-time network congestion and routes web traffic across the fastest network paths. It provides endpoints for enabling, disabling, and monitoring smart routing performance.
  - aid: cloudflare:cloudflare-page-shield-api
    name: Cloudflare Page Shield API
    tags:
      - Client-Side Security
      - Script Monitoring
      - Security
    humanURL: https://developers.cloudflare.com/page-shield/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/page-shield/
        type: Documentation
      - url: https://developers.cloudflare.com/page-shield/reference/page-shield-api/
        type: APIReference
      - url: https://developers.cloudflare.com/page-shield/get-started/
        type: GettingStarted
    description: The Cloudflare Page Shield API enables developers to monitor and manage client-side resources loaded by website visitors. It provides endpoints for detecting scripts, connections, and cookies, with malicious script detection alerts and configurable security policies.
  - aid: cloudflare:cloudflare-workers-for-platforms-api
    name: Cloudflare Workers for Platforms API
    tags:
      - Multi-Tenant
      - Platform
      - Serverless
    humanURL: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/
        type: Documentation
      - url: https://developers.cloudflare.com/api/resources/workers_for_platforms/
        type: APIReference
      - url: https://developers.cloudflare.com/cloudflare-for-platforms/workers-for-platforms/get-started/
        type: GettingStarted
    description: The Cloudflare Workers for Platforms API enables SaaS providers to deploy and manage customer code at scale using dispatch namespaces. It provides endpoints for creating namespaces, uploading user worker scripts, and dynamically routing requests to the appropriate worker with unlimited script limits and isolation.
  - aid: cloudflare:cloudflare-1111-dns-resolver-api
    name: Cloudflare 1.1.1.1 DNS Resolver API
    tags:
      - DNS
      - Privacy
      - Resolver
    humanURL: https://developers.cloudflare.com/1.1.1.1/
    properties:
      - url: https://developers.cloudflare.com/1.1.1.1/
        type: Documentation
      - url: https://developers.cloudflare.com/1.1.1.1/setup/
        type: GettingStarted
    description: The Cloudflare 1.1.1.1 DNS Resolver is a fast and privacy-focused public DNS resolver. It supports DNS over HTTPS (DoH) and DNS over TLS (DoT) for encrypted DNS queries, with WARP integration for device-level traffic protection and family-friendly filtering options.
  - aid: cloudflare:cloudflare-r2-sql-api
    name: Cloudflare R2 SQL API
    tags:
      - Analytics
      - Data Warehouse
      - SQL
    humanURL: https://developers.cloudflare.com/r2-sql/
    baseURL: https://api.cloudflare.com
    properties:
      - url: https://developers.cloudflare.com/r2-sql/
        type: Documentation
    description: The Cloudflare R2 SQL API enables developers to query data stored in R2 using standard SQL syntax. It provides a serverless query engine for analyzing Iceberg tables and structured data in R2 buckets without requiring separate data warehouse infrastructure.
name: Cloudflare
tags:
  - AI Gateway
  - API Gateway
  - Artificial Intelligence
  - CDN
  - Cloud
  - Containers
  - DDoS Protection
  - DNS
  - Edge
  - Edge Computing
  - Object Storage
  - Platform
  - Real-Time Communication
  - Security
  - Serverless
  - Web Performance
type: Contract
access: 3rd-Party
created: 2024/04/14
modified: '2026-05-04'
position: Consuming
segments:
  - Gateways
description: Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable.
maintainers:
  - FN: Kin Lane
    url: http://apievangelist.com
    email: kin@apievangelist.com
  - name: Cloudflare
    email: api@cloudflare.com
    url: https://www.cloudflare.com
specificationVersion: '0.18'
common:
  - url: json-ld/cloudflare-context.jsonld
    type: JSON-LD
  - url: json-schema/cloudflare-dns-record-schema.json
    type: JSONSchema
  - url: json-schema/cloudflare-zone-schema.json
    type: JSONSchema
  - url: json-schema/cloudflare-worker-script-schema.json
    type: JSONSchema
  - url: json-schema/cloudflare-account-schema.json
    type: JSONSchema
  - url: json-schema/cloudflare-notification-webhook-payload-schema.json
    type: JSONSchema
  - url: json-schema/cloudflare-r2-bucket-schema.json
    type: JSONSchema
  - url: json-schema/cloudflare-d1-database-schema.json
    type: JSONSchema
  - url: https://developers.cloudflare.com/
    type: Portal
  - url: https://developers.cloudflare.com/fundamentals/get-started/
    type: GettingStarted
  - url: https://blog.cloudflare.com/
    type: Blog
  - url: https://dash.cloudflare.com/sign-up
    type: SignUp
  - url: https://dash.cloudflare.com/login
    type: SignUp
  - url: https://www.cloudflare.com/plans/
    type: Pricing
  - url: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
    type: Authentication
  - url: https://developers.cloudflare.com/fundamentals/api/reference/sdks/
    type: SDK
  - url: https://developers.cloudflare.com/fundamentals/api/reference/limits/
    type: RateLimits
  - url: https://developers.cloudflare.com/changelog/
    type: ChangeLog
  - url: https://www.cloudflarestatus.com/
    type: StatusPage
  - url: https://www.cloudflare.com/
    type: Portal
  - url: https://dash.cloudflare.com/
    type: Console
  - url: https://support.cloudflare.com/
    type: Support
  - url: https://community.cloudflare.com/
    type: Support
  - url: https://discord.com/invite/cloudflaredev
    type: Support
  - url: https://github.com/cloudflare
    type: GitHubOrganization
  - url: https://github.com/cloudflare/api-schemas
    type: GitHubRepository
  - url: https://www.cloudflare.com/privacypolicy/
    type: PrivacyPolicy
  - url: https://www.cloudflare.com/terms/
    type: TermsOfService
  - url: https://developers.cloudflare.com/directory/
    type: Documentation
  - url: https://x.com/CloudflareDev
    type: X
  - url: https://developers.cloudflare.com/terraform/
    type: Integrations
    name: Terraform Provider
  - url: https://developers.cloudflare.com/pulumi/
    type: Integrations
    name: Pulumi Provider
  - url: https://developers.cloudflare.com/workers/wrangler/
    type: CLI
  - url: https://github.com/cloudflare/cloudflare-python
    type: SDK
    name: Python SDK
  - url: https://github.com/cloudflare/cloudflare-go
    type: SDK
    name: Go SDK
  - url: https://github.com/cloudflare/cloudflare-typescript
    type: SDK
    name: TypeScript SDK
  - url: https://www.npmjs.com/package/cloudflare
    type: SDK
    name: Node.js SDK (npm)
  - url: https://pypi.org/project/cloudflare/
    type: SDK
    name: Python SDK (PyPI)
  - url: https://developers.cloudflare.com/learning-paths/
    type: KnowledgeCenter
  - url: https://developers.cloudflare.com/products/
    type: Documentation
  - type: Features
    data:
      - REST API at api.cloudflare.com/client/v4 (1,200 req/5min global cap)
      - GraphQL Analytics API for traffic, security, Workers analytics
      - Workers serverless edge compute (100k req/day Free, 10M+ Paid)
      - Workers KV low-latency key-value storage
      - R2 object storage with zero egress fees
      - D1 serverless SQLite database
      - Durable Objects for stateful coordination
      - Cloudflare Images for storage and on-the-fly resizing
      - Cloudflare Stream for VOD and live video
      - Pages for static site / JAMstack hosting
      - 'Free plan: unlimited bandwidth, DDoS, Universal SSL'
      - Pro at $25/zone/mo with WAF and image optimization
      - Business at $200/zone/mo with custom SSL, 100% SLA
      - Enterprise from ~$5k/zone/mo with Bot Management, Argo
      - AI Gateway for LLM proxying and observability
      - Vectorize for vector search; Hyperdrive for connection pooling
    sources:
      - https://www.cloudflare.com/plans/
      - https://developers.cloudflare.com/workers/platform/pricing/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - Accelerate and protect websites and web applications
      - Deploy serverless applications at the edge
      - Store and serve objects with S3-compatible storage
      - Run AI inference models globally with low latency
      - Manage DNS zones and domain registrations
      - Stream live and on-demand video content
      - Implement Zero Trust security architecture
      - Monitor and analyze internet traffic patterns
      - Build real-time collaborative applications
      - Protect APIs with schema validation and rate limiting
  - type: Integrations
    data:
      - Terraform provider for infrastructure as code
      - Pulumi provider for cloud engineering
      - GitHub Actions for CI/CD deployments
      - S3-compatible API for R2 storage
      - OpenAI-compatible API for Workers AI
      - Wrangler CLI for Workers development
      - Puppeteer and Playwright for browser rendering
      - SIEM and log management integrations via Logpush
      - MCP server support for AI agents
---
