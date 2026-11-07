---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 69.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2628
  human_in_the_loop: 106
  name: Cloudflare Agentic Access
  operation_count: 5254
  slug: cloudflare-agentic-access
  summary_line: 5254 operations · 2628 acting · 106 human-in-the-loop
api_count: 25
apis:
- baseURL: https://api.cloudflare.com/client/v4
  baseurl_source: declared
  description: 'Workers AI REST endpoints for Cloudflare''s Clef and Clef Flash decision models (@cf/cloudflare/clef, @cf/cloudflare/clef-flash), which answer typed noul, choice and score questions about a state with '
  name: Cloudflare Workers AI Clef Decision Models API
  slug: cloudflare-workers-ai-clef-decision-api
- description: The Cloudflare Load Balancing API enables developers to distribute traffic across endpoints to reduce strain and latency. It provides endpoints for managing load balancers, pools, monitors, and health
  name: Cloudflare Load Balancing API
  slug: cloudflare-load-balancing-api
- description: The Cloudflare Web Application Firewall API checks incoming web and API requests and filters undesired traffic using rulesets. It supports managed rules, custom rules, rate limiting rules, and provide
  name: Cloudflare WAF API
  slug: cloudflare-waf-api
- description: The Cloudflare GraphQL Analytics API provides flexible access to analytics data across Cloudflare products including HTTP requests, firewall events, and load balancing metrics. Developers can query sp
  name: Cloudflare GraphQL Analytics API
  slug: cloudflare-graphql-analytics-api
- description: The Cloudflare Magic Transit API provides endpoints for managing network security and performance for on-premises, cloud-hosted, and hybrid networks. It supports managing sites, site ACLs, static rout
  name: Cloudflare Magic Transit API
  slug: cloudflare-magic-transit-api
- description: The Cloudflare Email Routing API enables developers to create and manage custom email addresses and routing rules for their domains. It supports forwarding emails to destination addresses, creating ca
  name: Cloudflare Email Routing API
  slug: cloudflare-email-routing-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Waiting Room API allows developers to manage virtual waiting rooms that route excess visitors to a customizable queue during high traffic. It provides endpoints for creating waiting roo
  name: Cloudflare Waiting Room API
  slug: cloudflare-waiting-room-api
- description: Cloudflare Spectrum extends Cloudflare's DDoS protection and performance benefits to any TCP or UDP application. The API enables developers to manage Spectrum applications, configure origin connection
  name: Cloudflare Spectrum API
  slug: cloudflare-spectrum-api
- description: 'Cloudflare API Shield provides API discovery, schema validation, and security features to protect APIs from abuse. It includes API Gateway capabilities for routing, authentication, and rate limiting, '
  name: Cloudflare API Shield API
  slug: cloudflare-api-shield-api
- description: The Cloudflare Zero Trust API enables developers to manage secure access to applications and networks without a traditional VPN. It includes Access policies, Gateway DNS and HTTP filtering, Tunnel man
  name: Cloudflare Zero Trust API
  slug: cloudflare-zero-trust-api
- description: The Cloudflare Registrar API allows developers to manage domain registrations at cost. It provides endpoints for listing domains, updating domain contacts, configuring DNSSEC, and managing domain tran
  name: Cloudflare Registrar API
  slug: cloudflare-registrar-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Cloudflare Workflows enables developers to build durable, multi-step applications on Workers that automatically retry failed tasks and persist state for minutes, hours, or weeks. The API provides endp
  name: Cloudflare Workflows API
  slug: cloudflare-workflows-api
- description: The Cloudflare Browser Rendering API enables developers to control headless browser instances on Cloudflare's global network. The REST API provides endpoints for capturing screenshots, extracting HTML
  name: Cloudflare Browser Rendering API
  slug: cloudflare-browser-rendering-api
- description: The Cloudflare Realtime API provides WebRTC infrastructure for building real-time audio and video applications. It includes a Selective Forwarding Unit (SFU) for media routing across Cloudflare's glob
  name: Cloudflare Realtime API
  slug: cloudflare-realtime-api
- description: The Cloudflare Containers API allows developers to run container workloads on Cloudflare's global network, managed directly from Workers code. Containers support full isolation, on-demand scaling, GPU
  name: Cloudflare Containers API
  slug: cloudflare-containers-api
- description: The Cloudflare AI Search API provides fully managed retrieval-augmented generation (RAG) pipelines. Developers upload documents to R2 and AI Search handles embeddings, indexing, retrieval, and respons
  name: Cloudflare AI Search API
  slug: cloudflare-ai-search-api
- description: The Cloudflare Agents SDK enables developers to build and deploy AI-powered agents that autonomously perform tasks, communicate with clients in real time, call AI models, persist state, schedule tasks
  name: Cloudflare Agents API
  slug: cloudflare-agents-api
- description: The Cloudflare Pipelines API enables developers to ingest events via HTTP endpoints or Worker bindings, transform data with SQL, and deliver it to R2 as Apache Iceberg tables or Parquet and JSON files
  name: Cloudflare Pipelines API
  slug: cloudflare-pipelines-api
- description: The Cloudflare DDoS Protection API provides managed rulesets for mitigating DDoS attacks at both the application and network layers. Developers can configure HTTP and network-layer attack protection o
  name: Cloudflare DDoS Protection API
  slug: cloudflare-ddos-protection-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Zaraz API allows developers to load and manage third-party tools in the cloud instead of the browser. It provides a unified web API with track, set, and ecommerce methods for sending ev
  name: Cloudflare Zaraz API
  slug: cloudflare-zaraz-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Secrets Store API enables developers to securely encrypt and store sensitive information as secrets that are reusable across a Cloudflare account. It provides endpoints for managing sto
  name: Cloudflare Secrets Store API
  slug: cloudflare-secrets-store-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: 'The Cloudflare Web Analytics API provides privacy-first real user measurement (RUM) analytics for websites. It uses a lightweight JavaScript beacon to collect performance data via the Performance API '
  name: Cloudflare Web Analytics API
  slug: cloudflare-web-analytics-api
- description: 'The Cloudflare Cache API enables developers to manage CDN caching behavior across Cloudflare''s global network. It provides endpoints for purging cached content by URL, prefix, cache tag, or hostname, '
  name: Cloudflare Cache API
  slug: cloudflare-cache-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Argo Smart Routing API enables developers to manage intelligent traffic routing that detects real-time network congestion and routes web traffic across the fastest network paths. It pro
  name: Cloudflare Argo Smart Routing API
  slug: cloudflare-argo-smart-routing-api
- description: The Cloudflare Page Shield API enables developers to monitor and manage client-side resources loaded by website visitors. It provides endpoints for detecting scripts, connections, and cookies, with ma
  name: Cloudflare Page Shield API
  slug: cloudflare-page-shield-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Workers for Platforms API enables SaaS providers to deploy and manage customer code at scale using dispatch namespaces. It provides endpoints for creating namespaces, uploading user wor
  name: Cloudflare Workers for Platforms API
  slug: cloudflare-workers-for-platforms-api
- description: The Cloudflare 1.1.1.1 DNS Resolver is a fast and privacy-focused public DNS resolver. It supports DNS over HTTPS (DoH) and DNS over TLS (DoT) for encrypted DNS queries, with WARP integration for devi
  name: Cloudflare 1.1.1.1 DNS Resolver API
  slug: cloudflare-1111-dns-resolver-api
- description: 'The Cloudflare R2 SQL API enables developers to query data stored in R2 using standard SQL syntax including JOINs, subqueries, and multi-table queries (added May 2026). It provides a serverless query '
  name: Cloudflare R2 SQL API
  slug: cloudflare-r2-sql-api
- description: Cloudflare Workers VPC allows Workers to connect to private APIs, services, and databases in external clouds (AWS, Azure, GCP, on-premise) that are not accessible from the public Internet. As of May 2
  name: Cloudflare Workers VPC API
  slug: cloudflare-workers-vpc-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Cloudflare Artifacts is a versioned file storage system that speaks Git, enabling programmatic repository creation and access via Workers, REST API, and Git clients. Recent additions (May 2026) includ
  name: Cloudflare Artifacts API
  slug: cloudflare-artifacts-api
- description: Claude Managed Agents on Cloudflare is a partnership offering announced May 19, 2026 that exposes Anthropic-managed Claude agents running on Cloudflare's Agents SDK / Durable Objects substrate. It int
  name: Claude Managed Agents on Cloudflare API
  slug: cloudflare-agents-managed-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Accounts API from Cloudflare — 441 operation(s) for accounts.
  name: Cloudflare Accounts API
  phrasing_intents:
  - id: accounts-list-accounts
    intent: List the accounts I can access
    question: Which Cloudflare accounts do I own or have verified access to?
  - id: accounts-account-details
    intent: Get an account's details
    question: What information is stored about a specific account I belong to?
  - id: accounts-update-account
    intent: Rename or reconfigure an account
    question: How do I rename an existing account?
  - id: ip-address-management-address-maps-list-address-maps
    intent: List an account's address maps
    question: Which address maps does my account own?
  - id: ip-address-management-address-maps-create-address-map
    intent: Create an address map
    question: How do I create a new address map for my IPs?
  - id: ip-address-management-address-maps-delete-address-map
    intent: Delete an address map
    question: How do I delete an address map I no longer need?
  - id: ip-address-management-address-maps-address-map-details
    intent: Get one address map
    question: What IPs, zones and settings are on a particular address map?
  - id: ip-address-management-address-maps-update-address-map
    intent: Update an address map
    question: Can I change the default SNI on an existing address map?
  phrasing_ops: 740
  slug: cloudflare-accounts-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Execute AI models for text generation, embeddings, image classification, and other machine learning tasks.
  name: Cloudflare AI Inference API
  phrasing_intents:
  - id: executeAiModel
    intent: Run a Workers AI model
    question: How do I run a text generation model like Llama on Cloudflare's network?
  phrasing_ops: 1
  slug: cloudflare-ai-inference-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create, list, and delete R2 storage buckets.
  name: Cloudflare Buckets API
  phrasing_intents:
  - id: listR2Buckets
    intent: List R2 storage buckets
    question: What R2 buckets do I have in my account?
  - id: createR2Bucket
    intent: Create an R2 storage bucket
    question: How do I create a new object storage bucket in R2?
  - id: getR2Bucket
    intent: Get details of an R2 bucket
    question: How do I see the details of one R2 bucket?
  - id: deleteR2Bucket
    intent: Delete an empty R2 bucket
    question: How do I delete an R2 bucket?
  phrasing_ops: 4
  slug: cloudflare-buckets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Write, read, and delete multiple key-value pairs in a single request.
  name: Cloudflare Bulk Operations API
  phrasing_intents:
  - id: bulkWriteKvPairs
    intent: Write many KV pairs in one request
    question: How do I load thousands of keys into a KV namespace at once?
  - id: bulkDeleteKvPairs
    intent: Delete many KV pairs in one request
    question: Can I delete a whole list of KV keys in a single request?
  - id: bulkGetKvPairs
    intent: Read many KV pairs in one request
    question: Is there a way to fetch the values of several KV keys in one call?
  phrasing_ops: 3
  slug: cloudflare-bulk-operations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Certificates API from Cloudflare — 2 operation(s) for certificates.
  name: Cloudflare Certificates API
  phrasing_intents:
  - id: origin-ca-list-certificates
    intent: List Origin CA certificates for a zone
    question: Which Origin CA certificates have been issued for my zone?
  - id: origin-ca-create-certificate
    intent: Issue an Origin CA certificate
    question: How do I get an Origin CA certificate for my origin server?
  - id: origin-ca-revoke-certificate
    intent: Revoke an Origin CA certificate
    question: How do I revoke an origin certificate whose private key was exposed?
  - id: origin-ca-get-certificate
    intent: Get an Origin CA certificate
    question: How do I fetch one origin certificate by its serial number?
  phrasing_ops: 4
  slug: cloudflare-certificates-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Configure bucket settings including CORS, lifecycle rules, and public access.
  name: Cloudflare Configuration API
  phrasing_intents:
  - id: getR2BucketConfiguration
    intent: View an R2 bucket's CORS and lifecycle configuration
    question: What CORS and lifecycle rules are currently set on my R2 bucket?
  - id: updateR2BucketConfiguration
    intent: Change an R2 bucket's configuration settings
    question: How do I change the CORS or lifecycle settings on an R2 bucket?
  - id: getCronTriggers
    intent: See a Worker's cron trigger schedules
    question: Which cron schedules are set to run my Worker?
  - id: updateCronTriggers
    intent: Set the cron schedules for a Worker
    question: How do I schedule my Cloudflare Worker to run on a cron?
  - id: getScriptSettings
    intent: View a Worker script's bindings and settings
    question: What bindings and compatibility settings does my Worker script have?
  - id: updateScriptSettings
    intent: Change a Worker script's settings
    question: Can I change a Worker's bindings without re-uploading its code?
  phrasing_ops: 6
  slug: cloudflare-configuration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create, list, update, and delete Hyperdrive configurations that connect Workers to databases.
  name: Cloudflare Configurations API
  phrasing_intents:
  - id: listHyperdriveConfigs
    intent: List Hyperdrive configurations
    question: What Hyperdrive database connections have I set up in my account?
  - id: createHyperdriveConfig
    intent: Create a Hyperdrive configuration for a database
    question: How do I put Hyperdrive in front of my existing Postgres database?
  - id: getHyperdriveConfig
    intent: Get a Hyperdrive configuration's details
    question: How can I check the origin and caching settings of one Hyperdrive config?
  - id: updateHyperdriveConfig
    intent: Update a Hyperdrive configuration
    question: How do I point an existing Hyperdrive config at a new database origin?
  - id: deleteHyperdriveConfig
    intent: Delete a Hyperdrive configuration
    question: How do I remove a Hyperdrive configuration I'm not using anymore?
  phrasing_ops: 5
  slug: cloudflare-configurations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage consumers that process messages from queues.
  name: Cloudflare Consumers API
  phrasing_intents:
  - id: listQueueConsumers
    intent: List a queue's consumers
    question: Which consumers are reading messages from my Cloudflare queue?
  - id: createQueueConsumer
    intent: Add a consumer to a queue
    question: How do I attach a Worker to a queue so it processes the messages?
  - id: getQueueConsumer
    intent: Get a queue consumer's details
    question: What settings does one particular queue consumer use?
  - id: replaceQueueConsumer
    intent: Replace a queue consumer's configuration
    question: How do I change the settings of an existing queue consumer?
  - id: deleteQueueConsumer
    intent: Remove a consumer from a queue
    question: How do I detach a Worker consumer from a queue?
  phrasing_ops: 5
  slug: cloudflare-consumers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create, list, update, and delete D1 serverless SQL databases.
  name: Cloudflare Databases API
  phrasing_intents:
  - id: listD1Databases
    intent: List D1 databases in an account
    question: What D1 databases do I have in my account?
  - id: createD1Database
    intent: Create a new D1 SQL database
    question: How do I spin up a new serverless SQL database on Cloudflare?
  - id: getD1Database
    intent: Get details of a D1 database
    question: How do I look up the details of one specific D1 database?
  - id: updateD1Database
    intent: Rename or reconfigure a D1 database
    question: Can I rename a D1 database after creating it?
  - id: deleteD1Database
    intent: Delete a D1 database and its data
    question: How do I permanently delete a D1 database?
  phrasing_ops: 5
  slug: cloudflare-databases-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create, list, and manage deployments for Pages projects.
  name: Cloudflare Deployments API
  phrasing_intents:
  - id: listDeployments
    intent: List a Worker script's deployments
    question: What deployments has my Worker script had?
  - id: createDeployment
    intent: Deploy a Worker version to take traffic
    question: How do I send traffic to a specific version of my Worker?
  phrasing_ops: 2
  slug: cloudflare-deployments-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create one-time upload URLs for client-side image uploads.
  name: Cloudflare Direct Uploads API
  phrasing_intents:
  - id: createImageDirectUpload
    intent: Create a one-time image upload URL
    question: How can my users upload images straight from the browser without my API key?
  phrasing_ops: 1
  slug: cloudflare-direct-uploads-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Access DNS query analytics for a zone with aggregated and time-grouped metrics.
  name: Cloudflare DNS Analytics API
  phrasing_intents:
  - id: getDnsAnalyticsReport
    intent: Get aggregated DNS query analytics for a zone
    question: How many DNS queries did my zone get in total?
  - id: getDnsAnalyticsByTime
    intent: Get DNS analytics broken down over time
    question: How has my zone's DNS query volume changed hour by hour?
  phrasing_ops: 2
  slug: cloudflare-dns-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Execute multiple DNS record operations in a single API call.
  name: Cloudflare DNS Batch Operations API
  phrasing_intents:
  - id: batchDnsRecords
    intent: Apply many DNS record changes in one batch
    question: How do I create, update and delete many DNS records in a single request?
  phrasing_ops: 1
  slug: cloudflare-dns-batch-operations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Import and export DNS records using BIND zone file format.
  name: Cloudflare DNS Record Import/Export API
  phrasing_intents:
  - id: exportDnsRecords
    intent: Export a zone's DNS records as a BIND file
    question: How do I back up all my DNS records as a zone file?
  - id: importDnsRecords
    intent: Import DNS records from a BIND zone file
    question: How do I migrate my DNS records by uploading a zone file?
  phrasing_ops: 2
  slug: cloudflare-dns-record-import-export-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Scan for common DNS records on a domain and review discovered records.
  name: Cloudflare DNS Record Scanning API
  phrasing_intents:
  - id: triggerDnsRecordScan
    intent: Start a scan for a domain's DNS records
    question: How do I get Cloudflare to scan my domain for its existing DNS records?
  - id: listScannedDnsRecords
    intent: Review DNS records found by a scan
    question: What DNS records did the latest scan find on my domain?
  - id: reviewScannedDnsRecords
    intent: Accept scanned DNS records into a zone
    question: How do I add the records a DNS scan discovered to my zone?
  phrasing_ops: 3
  slug: cloudflare-dns-record-scanning-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage DNS records for a zone including A, AAAA, CNAME, MX, TXT, SRV, and other record types.
  name: Cloudflare DNS Records API
  phrasing_intents:
  - id: listDnsRecords
    intent: List and filter a zone's DNS records
    question: How do I see every DNS record configured on my domain?
  - id: createDnsRecord
    intent: Add a new DNS record to a zone
    question: How do I add a new A record for a subdomain on Cloudflare?
  - id: getDnsRecord
    intent: Get the details of one DNS record
    question: How can I view the full settings of a single DNS record by its ID?
  - id: updateDnsRecord
    intent: Change selected fields on a DNS record
    question: How do I turn the orange-cloud proxy on or off for just one existing record?
  - id: overwriteDnsRecord
    intent: Replace a DNS record entirely
    question: How do I completely replace an existing DNS record with new values?
  - id: deleteDnsRecord
    intent: Delete a DNS record from a zone
    question: How do I remove a DNS record I no longer need?
  phrasing_ops: 6
  slug: cloudflare-dns-records-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage DNSSEC settings for a zone to protect against DNS spoofing.
  name: Cloudflare DNSSEC API
  phrasing_intents:
  - id: getDnssecSettings
    intent: View a zone's DNSSEC status and DS record
    question: Is DNSSEC turned on for my domain?
  - id: updateDnssecSettings
    intent: Enable or disable DNSSEC on a zone
    question: Can I switch DNSSEC on for my zone?
  - id: deleteDnssecSettings
    intent: Remove DNSSEC from a zone
    question: How do I delete the DNSSEC configuration from a zone?
  phrasing_ops: 3
  slug: cloudflare-dnssec-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Attach and detach custom domains to Worker scripts.
  name: Cloudflare Domains API
  phrasing_intents:
  - id: listDomains
    intent: List custom domains on Workers
    question: Which custom domains are attached to my Worker scripts?
  - id: attachDomain
    intent: Attach a custom domain to a Worker
    question: How do I serve a Worker on my own custom domain?
  phrasing_ops: 2
  slug: cloudflare-domains-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create, list, update, and delete AI Gateway instances.
  name: Cloudflare Gateways API
  phrasing_intents:
  - id: listAiGateways
    intent: List AI Gateways
    question: Which AI Gateways have I set up in Cloudflare?
  - id: createAiGateway
    intent: Create an AI Gateway
    question: How do I set up a new AI Gateway in front of my model calls?
  - id: getAiGateway
    intent: Get an AI Gateway's configuration
    question: What caching and rate-limit settings does one of my AI Gateways use?
  - id: updateAiGateway
    intent: Update an AI Gateway's settings
    question: How do I change the cache TTL on an existing AI Gateway?
  - id: deleteAiGateway
    intent: Delete an AI Gateway
    question: How do I delete an AI Gateway I no longer need?
  phrasing_ops: 5
  slug: cloudflare-gateways-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Upload, list, update, and delete image assets.
  name: Cloudflare Images API
  phrasing_intents:
  - id: listImages
    intent: List the images stored in an account
    question: Which images have I stored in Cloudflare Images?
  - id: uploadImage
    intent: Upload an image from a file or URL
    question: How do I upload an image by pointing at a URL instead of a file?
  - id: getImage
    intent: Get the details of one image
    question: What details are stored for a specific uploaded image?
  - id: updateImage
    intent: Update an image's metadata or signing
    question: Can I change the metadata on an image I already uploaded?
  - id: deleteImage
    intent: Delete an image and all its variants
    question: Does deleting an image also remove its variants?
  phrasing_ops: 5
  slug: cloudflare-images-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Import SQL into and export SQL from D1 databases.
  name: Cloudflare Import/Export API
  phrasing_intents:
  - id: exportD1Database
    intent: Export a D1 database as a SQL dump
    question: How do I back up a D1 database as SQL?
  - id: importD1Database
    intent: Import SQL into a D1 database
    question: Can I load a SQL file into an existing D1 database?
  phrasing_ops: 2
  slug: cloudflare-import-export-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create, list, update, and delete vector indexes.
  name: Cloudflare Indexes API
  phrasing_intents:
  - id: listVectorizeIndexes
    intent: List Vectorize indexes
    question: Which vector indexes exist in my Vectorize account?
  - id: createVectorizeIndex
    intent: Create a Vectorize vector index
    question: How do I create a vector index for storing embeddings?
  - id: getVectorizeIndex
    intent: Get a Vectorize index's details
    question: What dimensions and distance metric does one of my Vectorize indexes use?
  - id: updateVectorizeIndex
    intent: Update a Vectorize index's description
    question: Can I change the description of a Vectorize index after it's created?
  - id: deleteVectorizeIndex
    intent: Delete a Vectorize index and its vectors
    question: How do I delete a vector index I no longer need?
  phrasing_ops: 5
  slug: cloudflare-indexes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Read, write, and delete individual key-value pairs.
  name: Cloudflare Key-Value Pairs API
  phrasing_intents:
  - id: readKvValue
    intent: Read the value of a single KV key
    question: How do I read the value stored under one key in Workers KV?
  - id: writeKvValue
    intent: Write a value to a single KV key
    question: How do I store a value under one key in Workers KV?
  - id: deleteKvValue
    intent: Delete a single KV key
    question: How do I remove one key and its value from a KV namespace?
  phrasing_ops: 3
  slug: cloudflare-key-value-pairs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: List and manage keys within a namespace.
  name: Cloudflare Keys API
  phrasing_intents:
  - id: listKvKeys
    intent: List keys in a KV namespace
    question: What keys are stored in my Workers KV namespace?
  phrasing_ops: 1
  slug: cloudflare-keys-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage live streaming inputs for RTMPS and SRT ingestion.
  name: Cloudflare Live Inputs API
  phrasing_intents:
  - id: listLiveInputs
    intent: List live stream inputs
    question: What live inputs are set up for streaming in my account?
  - id: createLiveInput
    intent: Create a live input for RTMPS or SRT streaming
    question: How do I get an RTMPS or SRT endpoint to broadcast a live stream to?
  phrasing_ops: 2
  slug: cloudflare-live-inputs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Access request logs and analytics for AI Gateway traffic.
  name: Cloudflare Logs API
  phrasing_intents:
  - id: listAiGatewayLogs
    intent: List AI Gateway request logs
    question: What requests have gone through my AI Gateway?
  phrasing_ops: 1
  slug: cloudflare-logs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Memberships API from Cloudflare — 2 operation(s) for memberships.
  name: Cloudflare Memberships API
  phrasing_intents:
  - id: user'-s-account-memberships-list-memberships
    intent: List the accounts I'm a member of
    question: Which Cloudflare accounts do I have access to?
  - id: user'-s-account-memberships-delete-membership
    intent: Leave an account by removing a membership
    question: Can I remove myself from an account I no longer need access to?
  - id: user'-s-account-memberships-membership-details
    intent: Get the details of one account membership
    question: What status is a specific membership of mine in?
  - id: user'-s-account-memberships-update-membership
    intent: Accept or reject an account invitation
    question: How do I accept an invitation to join a Cloudflare account?
  phrasing_ops: 4
  slug: cloudflare-memberships-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Send, pull, and acknowledge messages.
  name: Cloudflare Messages API
  phrasing_intents:
  - id: sendMessage
    intent: Send a single message to a queue
    question: How do I publish one message onto a Cloudflare Queue over HTTP?
  - id: sendMessageBatch
    intent: Send a batch of messages to a queue
    question: Can I push many messages onto a queue in one request?
  - id: pullMessages
    intent: Pull messages from a queue for processing
    question: How do I consume messages from a queue with an HTTP pull consumer?
  - id: ackMessages
    intent: Acknowledge or retry pulled queue messages
    question: How do I mark pulled queue messages as done so they're removed?
  phrasing_ops: 4
  slug: cloudflare-messages-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Read metadata associated with keys.
  name: Cloudflare Metadata API
  phrasing_intents:
  - id: readKvMetadata
    intent: Read the metadata stored on a KV key
    question: What metadata is attached to a key in my KV namespace?
  phrasing_ops: 1
  slug: cloudflare-metadata-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage Durable Object namespaces that group related object instances.
  name: Cloudflare Namespaces API
  phrasing_intents:
  - id: listDurableObjectNamespaces
    intent: List Durable Object namespaces
    question: Which Durable Object namespaces exist in my Cloudflare account?
  - id: listKvNamespaces
    intent: List KV namespaces
    question: What KV namespaces do I have in Cloudflare?
  - id: createKvNamespace
    intent: Create a KV namespace
    question: How do I create a new Workers KV namespace?
  - id: getKvNamespace
    intent: Get details of a KV namespace
    question: What are the details of one specific KV namespace?
  - id: renameKvNamespace
    intent: Rename a KV namespace
    question: How do I change the title of an existing KV namespace?
  - id: deleteKvNamespace
    intent: Delete a KV namespace and its keys
    question: How do I delete a KV namespace I no longer use?
  phrasing_ops: 6
  slug: cloudflare-namespaces-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: List and manage individual Durable Object instances within a namespace.
  name: Cloudflare Objects API
  phrasing_intents:
  - id: listDurableObjects
    intent: List Durable Objects in a namespace
    question: Which Durable Objects exist inside one of my namespaces?
  - id: listR2Objects
    intent: List objects in an R2 bucket
    question: What files are stored in my R2 bucket?
  phrasing_ops: 2
  slug: cloudflare-objects-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: OpenAI-compatible endpoints for chat completions, text completions, embeddings, and responses.
  name: Cloudflare OpenAI Compatible API
  phrasing_intents:
  - id: createChatCompletion
    intent: Generate a chat completion
    question: How do I send a list of chat messages to a Workers AI model and get a reply?
  - id: createTextCompletion
    intent: Complete a text prompt
    question: How do I have a model continue a plain text prompt rather than a chat?
  - id: createEmbeddings
    intent: Create text embeddings
    question: How do I turn text into vectors for semantic search?
  - id: createResponse
    intent: Generate a model response
    question: Is there a responses endpoint that supports tool use and structured output?
  phrasing_ops: 4
  slug: cloudflare-openai-compatible-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Organizations API from Cloudflare — 1 operation(s) for organizations.
  name: Cloudflare Organizations API
  phrasing_intents:
  - id: audit-logs-get-organization-audit-logs
    intent: Review an organization's audit logs
    question: How do I see who changed what across my organization?
  phrasing_ops: 1
  slug: cloudflare-organizations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Purge all messages from a queue.
  name: Cloudflare Purge API
  phrasing_intents:
  - id: getPurgeStatus
    intent: Check whether a queue purge has finished
    question: Has my queue purge finished yet?
  - id: purgeQueue
    intent: Delete every message in a queue
    question: How do I clear out all the messages in a queue without deleting it?
  phrasing_ops: 2
  slug: cloudflare-purge-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Execute SQL queries against D1 databases.
  name: Cloudflare Queries API
  phrasing_intents:
  - id: queryD1Database
    intent: Run a SQL query against a D1 database
    question: How do I run a SQL statement against my D1 database over the API?
  - id: rawQueryD1Database
    intent: Run a raw SQL query returning array rows
    question: Is there a faster D1 query mode that returns rows as arrays instead of objects?
  phrasing_ops: 2
  slug: cloudflare-queries-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create, list, update, and delete message queues.
  name: Cloudflare Queues API
  phrasing_intents:
  - id: listQueues
    intent: List all queues in an account
    question: Which message queues does my Cloudflare account have?
  - id: createQueue
    intent: Create a new message queue
    question: How do I create a new message queue?
  - id: getQueue
    intent: Get the details of one queue
    question: What are the details of a specific queue?
  - id: replaceQueue
    intent: Overwrite a queue's full configuration
    question: How do I overwrite a queue's whole configuration at once?
  - id: updateQueue
    intent: Partially update a queue's settings
    question: Can I rename a queue without resetting its other settings?
  - id: deleteQueue
    intent: Delete a queue and its messages
    question: What happens to pending messages when I delete a queue?
  phrasing_ops: 6
  slug: cloudflare-queues-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar API from Cloudflare — 169 operation(s) for radar.
  name: Cloudflare Radar API
  phrasing_intents:
  - id: radar-get-annotations-outages
    intent: List recent Internet outages and anomalies
    question: Where can I see the latest Internet outages Cloudflare Radar has recorded?
  - id: radar-get-annotations-outages-top
    intent: Count outages per location
    question: Which countries have had the most Internet outages lately?
  - id: radar-get-dns-as112-timeseries-by-dnssec
    intent: Summarize AS112 DNS queries by DNSSEC support
    question: What share of queries reaching AS112 ask for DNSSEC?
  - id: radar-get-dns-as112-timeseries-by-edns
    intent: Summarize AS112 DNS queries by EDNS support
    question: What percentage of AS112 queries use EDNS?
  - id: radar-get-dns-as112-timeseries-by-ip-version
    intent: Summarize AS112 DNS queries by IP version
    question: How much AS112 DNS traffic arrives over IPv6 compared to IPv4?
  - id: radar-get-dns-as112-timeseries-by-protocol
    intent: Summarize AS112 DNS queries by transport protocol
    question: What share of AS112 lookups travel over UDP versus TCP?
  - id: radar-get-dns-as112-timeseries-by-query-type
    intent: Summarize AS112 DNS queries by record type
    question: Which DNS record types are most commonly queried at AS112?
  - id: radar-get-dns-as112-timeseries-by-response-codes
    intent: Summarize AS112 DNS responses by response code
    question: What share of AS112 answers are NXDOMAIN?
  phrasing_ops: 169
  slug: cloudflare-radar-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Map URL patterns to Worker scripts within a zone.
  name: Cloudflare Routes API
  phrasing_intents:
  - id: listRoutes
    intent: List a zone's Worker routes
    question: Which URL patterns on my domain are routed to Workers?
  - id: createRoute
    intent: Map a URL pattern to a Worker
    question: How do I make a Worker run on a URL pattern like example.com/*?
  - id: getRoute
    intent: Get a Worker route's details
    question: What pattern and script does a specific Worker route use?
  - id: updateRoute
    intent: Change a Worker route's pattern or script
    question: How do I point an existing Worker route at a different script?
  - id: deleteRoute
    intent: Remove a Worker route
    question: How do I stop a Worker from running on a URL pattern?
  phrasing_ops: 5
  slug: cloudflare-routes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Upload, download, and manage Worker scripts by name.
  name: Cloudflare Scripts API
  phrasing_intents:
  - id: listScripts
    intent: List all Worker scripts in an account
    question: Which Worker scripts are uploaded to my account?
  - id: downloadScript
    intent: Download a Worker script's code
    question: How do I download the code of a deployed Worker script?
  - id: uploadScript
    intent: Upload or update a Worker script
    question: What's the way to push new code to a Worker script by name?
  - id: deleteScript
    intent: Delete a Worker script
    question: Can I delete a Worker script by its name?
  phrasing_ops: 4
  slug: cloudflare-scripts-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage encrypted environment variables for Worker scripts.
  name: Cloudflare Secrets API
  phrasing_intents:
  - id: listSecrets
    intent: List a Worker's secrets
    question: Which secrets are set on my Worker script?
  - id: addSecret
    intent: Add or update a Worker secret
    question: How do I store an API key as an encrypted secret for my Worker?
  phrasing_ops: 2
  slug: cloudflare-secrets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage signing keys for signed video URLs.
  name: Cloudflare Signing Keys API
  phrasing_intents:
  - id: listSigningKeys
    intent: List Stream signing keys
    question: Which signing keys do I have for creating signed video URLs?
  - id: createSigningKey
    intent: Create a Stream signing key
    question: How do I generate a new key so I can sign video URLs myself?
  phrasing_ops: 2
  slug: cloudflare-signing-keys-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Browse and restore D1 databases to previous points in time.
  name: Cloudflare Time Travel API
  phrasing_intents:
  - id: getD1Bookmark
    intent: Get a point-in-time bookmark for a D1 database
    question: How do I get a bookmark for my D1 database's current state?
  - id: restoreD1Database
    intent: Restore a D1 database to an earlier point in time
    question: Can I roll my D1 database back to before a bad migration?
  phrasing_ops: 2
  slug: cloudflare-time-travel-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User API from Cloudflare — 28 operation(s) for user.
  name: Cloudflare User API
  phrasing_intents:
  - id: user-user-details
    intent: Get my user profile details
    question: What personal details does my Cloudflare user profile hold?
  - id: user-edit-user
    intent: Edit my user profile
    question: How do I change the name on my user profile?
  - id: audit-logs-get-user-audit-logs
    intent: List audit logs for my user account
    question: Who changed settings on my account, and when?
  - id: user-billing-history-(-deprecated)-billing-history-details
    intent: View my billing history
    question: Where can I see my past charges and billing history?
  - id: user-billing-profile-(-deprecated)-billing-profile-details
    intent: View my billing profile
    question: What billing profile and payment details are on file for my user?
  - id: ip-access-rules-for-a-user-list-ip-access-rules
    intent: List my user-level IP Access rules
    question: Which IP addresses have I blocked or allowed across all my zones?
  - id: ip-access-rules-for-a-user-create-an-ip-access-rule
    intent: Create an IP Access rule for all my zones
    question: How do I block an IP address across every zone I own?
  - id: ip-access-rules-for-a-user-delete-an-ip-access-rule
    intent: Delete a user-level IP Access rule
    question: How do I remove an IP block that applies to all my zones?
  phrasing_ops: 46
  slug: cloudflare-user-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage image variants that define transformation presets.
  name: Cloudflare Variants API
  phrasing_intents:
  - id: listImageVariants
    intent: List image variant definitions
    question: Which image variants like thumbnail or hero have I defined for Images?
  - id: createImageVariant
    intent: Create an image variant with resize options
    question: How do I define a new thumbnail size for images I've uploaded?
  phrasing_ops: 2
  slug: cloudflare-variants-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Insert, upsert, query, get, and delete vectors within an index.
  name: Cloudflare Vectors API
  phrasing_intents:
  - id: insertVectors
    intent: Insert new vectors into an index
    question: How do I add new embeddings to a Vectorize index?
  - id: upsertVectors
    intent: Insert or replace vectors in an index
    question: Can I overwrite vectors that already exist in my index?
  - id: queryVectors
    intent: Find the nearest vectors to a query vector
    question: How do I run a similarity search against a Vectorize index?
  - id: getVectorsByIds
    intent: Fetch specific vectors by their IDs
    question: Can I fetch particular vectors if I know their IDs?
  - id: deleteVectorsByIds
    intent: Delete specific vectors by their IDs
    question: How do I remove particular vectors from an index?
  phrasing_ops: 5
  slug: cloudflare-vectors-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Verify Turnstile challenge tokens on the server side.
  name: Cloudflare Verification API
  phrasing_intents:
  - id: verifyTurnstileToken
    intent: Verify a Turnstile token server-side
    question: How do I check on my server that a visitor actually passed the Turnstile challenge?
  phrasing_ops: 1
  slug: cloudflare-verification-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage immutable snapshots of Worker code and configuration.
  name: Cloudflare Versions API
  phrasing_intents:
  - id: listVersions
    intent: List a Worker's versions
    question: What versions of my Worker's code have been uploaded?
  - id: createVersion
    intent: Create a new Worker version
    question: How do I snapshot my Worker's current code and configuration as a new version?
  phrasing_ops: 2
  slug: cloudflare-versions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Upload, list, update, and delete video assets.
  name: Cloudflare Videos API
  phrasing_intents:
  - id: listStreamVideos
    intent: List videos in a Stream account
    question: How do I see all the videos uploaded to my Stream account?
  - id: uploadStreamVideo
    intent: Upload a video to Stream from a URL
    question: How can I get Stream to fetch and ingest a video that's already hosted at a public URL?
  - id: getStreamVideo
    intent: Get a video's status and playback details
    question: Has my uploaded video finished processing yet?
  - id: updateStreamVideo
    intent: Update a video's metadata and playback settings
    question: How do I change the metadata on a video that's already in Stream?
  - id: deleteStreamVideo
    intent: Delete a video from Stream
    question: How do I permanently remove a video and its data from Stream?
  - id: createDirectUpload
    intent: Create a one-time direct upload URL for a video
    question: How can my users upload videos straight from their browser without going through my server?
  phrasing_ops: 6
  slug: cloudflare-videos-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Configure webhooks for video processing notifications.
  name: Cloudflare Webhooks API
  phrasing_intents:
  - id: getStreamWebhook
    intent: Get the Stream video webhook URL
    question: Which URL receives my Cloudflare Stream video processing notifications?
  - id: updateStreamWebhook
    intent: Set the Stream video webhook URL
    question: How do I get notified when a Stream video finishes processing?
  - id: deleteStreamWebhook
    intent: Remove the Stream video webhook
    question: How do I stop receiving Stream video processing webhooks?
  phrasing_ops: 3
  slug: cloudflare-webhooks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Create, list, update, and delete Turnstile widget configurations.
  name: Cloudflare Widgets API
  phrasing_intents:
  - id: listTurnstileWidgets
    intent: List Turnstile widgets
    question: Which Turnstile widgets are configured in my Cloudflare account?
  - id: createTurnstileWidget
    intent: Create a Turnstile widget
    question: How do I create a new Turnstile widget for my website?
  - id: getTurnstileWidget
    intent: Get a Turnstile widget's configuration
    question: What domains and mode is a particular Turnstile widget set to?
  - id: updateTurnstileWidget
    intent: Update a Turnstile widget's settings
    question: How do I add another allowed domain to an existing Turnstile widget?
  - id: deleteTurnstileWidget
    intent: Delete a Turnstile widget
    question: How do I remove a Turnstile widget I'm not using anymore?
  - id: rotateTurnstileSecret
    intent: Rotate a Turnstile widget's secret key
    question: How do I rotate the secret key for a Turnstile widget?
  phrasing_ops: 6
  slug: cloudflare-widgets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: Manage Worker resources including creating, updating, and deleting Workers.
  name: Cloudflare Workers API
  phrasing_intents:
  - id: listWorkers
    intent: List all Workers in an account
    question: Which Workers are deployed in my Cloudflare account?
  - id: createWorker
    intent: Create a new Worker
    question: How do I create a new Worker with a name and entry module?
  - id: getWorker
    intent: Get the details of one Worker
    question: What are the details of a particular Worker?
  - id: replaceWorker
    intent: Replace all of a Worker's properties
    question: How do I fully replace a Worker's properties in one request?
  - id: editWorker
    intent: Edit some of a Worker's fields
    question: Can I rename a Worker without touching its other fields?
  - id: deleteWorker
    intent: Delete a Worker and its resources
    question: Can I delete a Worker along with everything attached to it?
  phrasing_ops: 6
  slug: cloudflare-workers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zones API from Cloudflare — 265 operation(s) for zones.
  name: Cloudflare Zones API
  phrasing_intents:
  - id: zones-get
    intent: List and filter my zones
    question: How do I see every domain I have added to Cloudflare?
  - id: zones-post
    intent: Add a new domain as a zone
    question: How do I add a new domain to my account so it can be proxied?
  - id: zone-level-access-applications-list-access-applications
    intent: List Access applications in a zone
    question: What Access applications are protecting this zone?
  - id: zone-level-access-applications-add-a-bookmark-application
    intent: Add an Access application to a zone
    question: How do I put a new application behind Access on my zone?
  - id: zone-level-access-applications-delete-an-access-application
    intent: Delete an Access application
    question: How do I stop protecting an app with Access and remove it from my zone?
  - id: zone-level-access-applications-get-an-access-application
    intent: Get one Access application's details
    question: Where can I see the configuration of a single Access app on my zone?
  - id: zone-level-access-applications-update-a-bookmark-application
    intent: Update an Access application
    question: How do I change the configuration of an existing Access application?
  - id: zone-level-access-applications-revoke-service-tokens
    intent: Revoke all tokens issued for an app
    question: How do I force everyone to log in again to one Access application?
  phrasing_ops: 508
  slug: cloudflare-zones-api
- description: The canonical Cloudflare REST API at https://api.cloudflare.com/client/v4 covering account management, DNS and zones, SSL/TLS certificates, WAF and firewall rules, Workers and KV, R2 object storage, P
  name: Cloudflare API (canonical)
  slug: canonical
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Ips API from Cloudflare — 1 operation(s) for ips.
  name: Cloudflare Ips API
  phrasing_intents:
  - id: cloudflare-i-ps-cloudflare-ip-details
    intent: List the IP ranges Cloudflare uses
    question: What IP ranges should I allowlist on my origin firewall for Cloudflare traffic?
  phrasing_ops: 1
  slug: cloudflare-ips-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access application-scoped policies API from Cloudflare — 3 operation(s) for access application-scoped policies.
  name: Cloudflare Access application-scoped policies API
  slug: cloudflare-access-application-scoped-policies-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access applications API from Cloudflare — 5 operation(s) for access applications.
  name: Cloudflare Access applications API
  slug: cloudflare-access-applications-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access authentication logs API from Cloudflare — 1 operation(s) for access authentication logs.
  name: Cloudflare Access authentication logs API
  slug: cloudflare-access-authentication-logs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access Authenticator Device AAGUIDs API from Cloudflare — 1 operation(s) for access authenticator device aaguids.
  name: Cloudflare Access Authenticator Device AAGUIDs API
  slug: cloudflare-access-authenticator-device-aaguids-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access Bookmark applications (Deprecated) API from Cloudflare — 2 operation(s) for access bookmark applications (deprecated).
  name: Cloudflare Access Bookmark applications (Deprecated) API
  slug: cloudflare-access-bookmark-applications-deprecated-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access custom pages API from Cloudflare — 3 operation(s) for access custom pages.
  name: Cloudflare Access custom pages API
  slug: cloudflare-access-custom-pages-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access groups API from Cloudflare — 2 operation(s) for access groups.
  name: Cloudflare Access groups API
  slug: cloudflare-access-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access identity providers API from Cloudflare — 7 operation(s) for access identity providers.
  name: Cloudflare Access identity providers API
  slug: cloudflare-access-identity-providers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access IdP federation grants API from Cloudflare — 2 operation(s) for access idp federation grants.
  name: Cloudflare Access IdP federation grants API
  slug: cloudflare-access-idp-federation-grants-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access JIT request logs API from Cloudflare — 2 operation(s) for access jit request logs.
  name: Cloudflare Access JIT request logs API
  slug: cloudflare-access-jit-request-logs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access key configuration API from Cloudflare — 2 operation(s) for access key configuration.
  name: Cloudflare Access key configuration API
  slug: cloudflare-access-key-configuration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access mTLS authentication API from Cloudflare — 3 operation(s) for access mtls authentication.
  name: Cloudflare Access mTLS authentication API
  slug: cloudflare-access-mtls-authentication-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access policy tester API from Cloudflare — 3 operation(s) for access policy tester.
  name: Cloudflare Access policy tester API
  slug: cloudflare-access-policy-tester-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access reusable policies API from Cloudflare — 2 operation(s) for access reusable policies.
  name: Cloudflare Access reusable policies API
  slug: cloudflare-access-reusable-policies-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access SAML encryption certificates API from Cloudflare — 4 operation(s) for access saml encryption certificates.
  name: Cloudflare Access SAML encryption certificates API
  slug: cloudflare-access-saml-encryption-certificates-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access SCIM update logs API from Cloudflare — 1 operation(s) for access scim update logs.
  name: Cloudflare Access SCIM update logs API
  slug: cloudflare-access-scim-update-logs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access service tokens API from Cloudflare — 4 operation(s) for access service tokens.
  name: Cloudflare Access service tokens API
  slug: cloudflare-access-service-tokens-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access short-lived certificate CAs API from Cloudflare — 2 operation(s) for access short-lived certificate cas.
  name: Cloudflare Access short-lived certificate CAs API
  slug: cloudflare-access-short-lived-certificate-cas-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access tags API from Cloudflare — 2 operation(s) for access tags.
  name: Cloudflare Access tags API
  slug: cloudflare-access-tags-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Access user populations API from Cloudflare — 2 operation(s) for access user populations.
  name: Cloudflare Access user populations API
  slug: cloudflare-access-user-populations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account API from Cloudflare — 2 operation(s) for account.
  name: Cloudflare Account API
  slug: cloudflare-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Billing API from Cloudflare — 10 operation(s) for account billing.
  name: Cloudflare Account Billing API
  slug: cloudflare-account-billing-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Billing History API from Cloudflare — 1 operation(s) for account billing history.
  name: Cloudflare Account Billing History API
  slug: cloudflare-account-billing-history-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Billing Profile API from Cloudflare — 1 operation(s) for account billing profile.
  name: Cloudflare Account Billing Profile API
  slug: cloudflare-account-billing-profile-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Entitlements API from Cloudflare — 1 operation(s) for account entitlements.
  name: Cloudflare Account Entitlements API
  slug: cloudflare-account-entitlements-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account-Level Custom Nameservers API from Cloudflare — 2 operation(s) for account-level custom nameservers.
  name: Cloudflare Account-Level Custom Nameservers API
  slug: cloudflare-account-level-custom-nameservers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account-Level Custom Nameservers Usage for a Zone API from Cloudflare — 1 operation(s) for account-level custom nameservers usage for a zone.
  name: Cloudflare Account-Level Custom Nameservers Usage for a Zone API
  slug: cloudflare-account-level-custom-nameservers-usage-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Load Balancer Monitor Groups API from Cloudflare — 3 operation(s) for account load balancer monitor groups.
  name: Cloudflare Account Load Balancer Monitor Groups API
  slug: cloudflare-account-load-balancer-monitor-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Load Balancer Monitors API from Cloudflare — 5 operation(s) for account load balancer monitors.
  name: Cloudflare Account Load Balancer Monitors API
  slug: cloudflare-account-load-balancer-monitors-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Load Balancer Pools API from Cloudflare — 5 operation(s) for account load balancer pools.
  name: Cloudflare Account Load Balancer Pools API
  slug: cloudflare-account-load-balancer-pools-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Load Balancer Search API from Cloudflare — 1 operation(s) for account load balancer search.
  name: Cloudflare Account Load Balancer Search API
  slug: cloudflare-account-load-balancer-search-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Load Balancers API from Cloudflare — 3 operation(s) for account load balancers.
  name: Cloudflare Account Load Balancers API
  slug: cloudflare-account-load-balancers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Members API from Cloudflare — 2 operation(s) for account members.
  name: Cloudflare Account Members API
  slug: cloudflare-account-members-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Owned API Tokens API from Cloudflare — 5 operation(s) for account owned api tokens.
  name: Cloudflare Account Owned API Tokens API
  slug: cloudflare-account-owned-api-tokens-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Payment Methods API from Cloudflare — 3 operation(s) for account payment methods.
  name: Cloudflare Account Payment Methods API
  slug: cloudflare-account-payment-methods-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Permission Groups API from Cloudflare — 2 operation(s) for account permission groups.
  name: Cloudflare Account Permission Groups API
  slug: cloudflare-account-permission-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Request Tracer API from Cloudflare — 1 operation(s) for account request tracer.
  name: Cloudflare Account Request Tracer API
  slug: cloudflare-account-request-tracer-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Resource Groups API from Cloudflare — 2 operation(s) for account resource groups.
  name: Cloudflare Account Resource Groups API
  slug: cloudflare-account-resource-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Roles API from Cloudflare — 2 operation(s) for account roles.
  name: Cloudflare Account Roles API
  slug: cloudflare-account-roles-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Rulesets API from Cloudflare — 10 operation(s) for account rulesets.
  name: Cloudflare Account Rulesets API
  slug: cloudflare-account-rulesets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Settings API from Cloudflare — 2 operation(s) for account settings.
  name: Cloudflare Account Settings API
  slug: cloudflare-account-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account Subscriptions API from Cloudflare — 6 operation(s) for account subscriptions.
  name: Cloudflare Account Subscriptions API
  slug: cloudflare-account-subscriptions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account User Group Members API from Cloudflare — 2 operation(s) for account user group members.
  name: Cloudflare Account User Group Members API
  slug: cloudflare-account-user-group-members-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Account User Groups API from Cloudflare — 2 operation(s) for account user groups.
  name: Cloudflare Account User Groups API
  slug: cloudflare-account-user-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Active session API from Cloudflare — 6 operation(s) for active session.
  name: Cloudflare Active session API
  slug: cloudflare-active-session-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Audit API from Cloudflare — 2 operation(s) for ai audit.
  name: Cloudflare AI Audit API
  slug: cloudflare-ai-audit-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway API from Cloudflare — 11 operation(s) for ai gateway.
  name: Cloudflare AI Gateway API
  slug: cloudflare-ai-gateway-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Custom Domains API from Cloudflare — 2 operation(s) for ai gateway custom domains.
  name: Cloudflare AI Gateway Custom Domains API
  slug: cloudflare-ai-gateway-custom-domains-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Custom Provider Costs API from Cloudflare — 2 operation(s) for ai gateway custom provider costs.
  name: Cloudflare AI Gateway Custom Provider Costs API
  slug: cloudflare-ai-gateway-custom-provider-costs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Custom Providers API from Cloudflare — 2 operation(s) for ai gateway custom providers.
  name: Cloudflare AI Gateway Custom Providers API
  slug: cloudflare-ai-gateway-custom-providers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Datasets API from Cloudflare — 2 operation(s) for ai gateway datasets.
  name: Cloudflare AI Gateway Datasets API
  slug: cloudflare-ai-gateway-datasets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Dynamic Routes API from Cloudflare — 5 operation(s) for ai gateway dynamic routes.
  name: Cloudflare AI Gateway Dynamic Routes API
  slug: cloudflare-ai-gateway-dynamic-routes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Evaluations API from Cloudflare — 3 operation(s) for ai gateway evaluations.
  name: Cloudflare AI Gateway Evaluations API
  slug: cloudflare-ai-gateway-evaluations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Gateways API from Cloudflare — 3 operation(s) for ai gateway gateways.
  name: Cloudflare AI Gateway Gateways API
  slug: cloudflare-ai-gateway-gateways-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Logs API from Cloudflare — 4 operation(s) for ai gateway logs.
  name: Cloudflare AI Gateway Logs API
  slug: cloudflare-ai-gateway-logs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Gateway Provider Configs API from Cloudflare — 2 operation(s) for ai gateway provider configs.
  name: Cloudflare AI Gateway Provider Configs API
  slug: cloudflare-ai-gateway-provider-configs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Search Account Search API from Cloudflare — 2 operation(s) for ai search account search.
  name: Cloudflare AI Search Account Search API
  slug: cloudflare-ai-search-account-search-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Search Instances API from Cloudflare — 11 operation(s) for ai search instances.
  name: Cloudflare AI Search Instances API
  slug: cloudflare-ai-search-instances-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Search Instances Items API from Cloudflare — 5 operation(s) for ai search instances items.
  name: Cloudflare AI Search Instances Items API
  slug: cloudflare-ai-search-instances-items-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Search Instances Jobs API from Cloudflare — 6 operation(s) for ai search instances jobs.
  name: Cloudflare AI Search Instances Jobs API
  slug: cloudflare-ai-search-instances-jobs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Search Namespaces API from Cloudflare — 3 operation(s) for ai search namespaces.
  name: Cloudflare AI Search Namespaces API
  slug: cloudflare-ai-search-namespaces-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Search Tokens API from Cloudflare — 2 operation(s) for ai search tokens.
  name: Cloudflare AI Search Tokens API
  slug: cloudflare-ai-search-tokens-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AI Security for Apps API from Cloudflare — 2 operation(s) for ai security for apps.
  name: Cloudflare AI Security for Apps API
  slug: cloudflare-ai-security-for-apps-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Analytics API from Cloudflare — 1 operation(s) for analytics.
  name: Cloudflare Analytics API
  slug: cloudflare-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Analytics Engine API from Cloudflare — 1 operation(s) for analytics engine.
  name: Cloudflare Analytics Engine API
  slug: cloudflare-analytics-engine-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Analytics SQL API from Cloudflare — 4 operation(s) for analytics sql.
  name: Cloudflare Analytics SQL API
  slug: cloudflare-analytics-sql-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Analyze Certificate API from Cloudflare — 1 operation(s) for analyze certificate.
  name: Cloudflare Analyze Certificate API
  slug: cloudflare-analyze-certificate-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The API Shield API Discovery API from Cloudflare — 3 operation(s) for api shield api discovery.
  name: Cloudflare API Shield API Discovery API
  slug: cloudflare-api-shield-api-discovery-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The API Shield Client Certificates for a Zone API from Cloudflare — 3 operation(s) for api shield client certificates for a zone.
  name: Cloudflare API Shield Client Certificates for a Zone API
  slug: cloudflare-api-shield-client-certificates-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The API Shield Endpoint Management API from Cloudflare — 4 operation(s) for api shield endpoint management.
  name: Cloudflare API Shield Endpoint Management API
  slug: cloudflare-api-shield-endpoint-management-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The API Shield Labels API from Cloudflare — 8 operation(s) for api shield labels.
  name: Cloudflare API Shield Labels API
  slug: cloudflare-api-shield-labels-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The API Shield Schema Validation 2.0 API from Cloudflare — 7 operation(s) for api shield schema validation 2.0.
  name: Cloudflare API Shield Schema Validation 2.0 API
  slug: cloudflare-api-shield-schema-validation-2-0-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The API Shield Settings API from Cloudflare — 1 operation(s) for api shield settings.
  name: Cloudflare API Shield Settings API
  slug: cloudflare-api-shield-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The API Shield WAF Expression Templates API from Cloudflare — 1 operation(s) for api shield waf expression templates.
  name: Cloudflare API Shield WAF Expression Templates API
  slug: cloudflare-api-shield-waf-expression-templates-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Applications API from Cloudflare — 9 operation(s) for applications.
  name: Cloudflare Applications API
  slug: cloudflare-applications-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Approvals API from Cloudflare — 4 operation(s) for approvals.
  name: Cloudflare Approvals API
  slug: cloudflare-approvals-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Apps API from Cloudflare — 4 operation(s) for apps.
  name: Cloudflare Apps API
  slug: cloudflare-apps-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Argo Analytics for Geolocation API from Cloudflare — 1 operation(s) for argo analytics for geolocation.
  name: Cloudflare Argo Analytics for Geolocation API
  slug: cloudflare-argo-analytics-for-geolocation-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Argo Analytics for Zone API from Cloudflare — 1 operation(s) for argo analytics for zone.
  name: Cloudflare Argo Analytics for Zone API
  slug: cloudflare-argo-analytics-for-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Argo Smart Routing API from Cloudflare — 3 operation(s) for argo smart routing.
  name: Cloudflare Argo Smart Routing API
  slug: cloudflare-argo-smart-routing-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ART Analytics API from Cloudflare — 3 operation(s) for art analytics.
  name: Cloudflare ART Analytics API
  slug: cloudflare-art-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Artifacts API from Cloudflare — 15 operation(s) for artifacts.
  name: Cloudflare Artifacts API
  slug: cloudflare-artifacts-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ASN Intelligence API from Cloudflare — 2 operation(s) for asn intelligence.
  name: Cloudflare ASN Intelligence API
  slug: cloudflare-asn-intelligence-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Attacker API from Cloudflare — 1 operation(s) for attacker.
  name: Cloudflare Attacker API
  slug: cloudflare-attacker-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Audit Logs API from Cloudflare — 7 operation(s) for audit logs.
  name: Cloudflare Audit Logs API
  slug: cloudflare-audit-logs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Automatic SSL/TLS API from Cloudflare — 1 operation(s) for automatic ssl/tls.
  name: Cloudflare Automatic SSL/TLS API
  slug: cloudflare-automatic-ssl-tls-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AutoRAG Jobs API from Cloudflare — 3 operation(s) for autorag jobs.
  name: Cloudflare AutoRAG Jobs API
  slug: cloudflare-autorag-jobs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AutoRAG RAG API from Cloudflare — 2 operation(s) for autorag rag.
  name: Cloudflare AutoRAG RAG API
  slug: cloudflare-autorag-rag-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The AutoRAG RAG Search API from Cloudflare — 2 operation(s) for autorag rag search.
  name: Cloudflare AutoRAG RAG Search API
  slug: cloudflare-autorag-rag-search-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Available Page Rules settings API from Cloudflare — 1 operation(s) for available page rules settings.
  name: Cloudflare Available Page Rules settings API
  slug: cloudflare-available-page-rules-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Basin Catalog Management API from Cloudflare — 5 operation(s) for basin catalog management.
  name: Cloudflare Basin Catalog Management API
  slug: cloudflare-basin-catalog-management-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Billable Usage API from Cloudflare — 2 operation(s) for billable usage.
  name: Cloudflare Billable Usage API
  slug: cloudflare-billable-usage-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Billable Usage V2 API from Cloudflare — 3 operation(s) for billable usage v2.
  name: Cloudflare Billable Usage V2 API
  slug: cloudflare-billable-usage-v2-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The BinDB API from Cloudflare — 2 operation(s) for bindb.
  name: Cloudflare Bin DB API
  slug: cloudflare-bindb-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Bot Settings API from Cloudflare — 1 operation(s) for bot settings.
  name: Cloudflare Bot Settings API
  slug: cloudflare-bot-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Botnet Threat Feed API from Cloudflare — 4 operation(s) for botnet threat feed.
  name: Cloudflare Botnet Threat Feed API
  slug: cloudflare-botnet-threat-feed-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Brand Protection API from Cloudflare — 40 operation(s) for brand protection.
  name: Cloudflare Brand Protection API
  slug: cloudflare-brand-protection-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The brapi API from Cloudflare — 26 operation(s) for brapi.
  name: Cloudflare Brapi API
  slug: cloudflare-brapi-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Browser Extension Config API from Cloudflare — 2 operation(s) for browser extension config.
  name: Cloudflare Browser Extension Config API
  slug: cloudflare-browser-extension-config-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Browser Extension Inventories API from Cloudflare — 2 operation(s) for browser extension inventories.
  name: Cloudflare Browser Extension Inventories API
  slug: cloudflare-browser-extension-inventories-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Build Tokens API from Cloudflare — 2 operation(s) for build tokens.
  name: Cloudflare Build Tokens API
  slug: cloudflare-build-tokens-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Builds API from Cloudflare — 5 operation(s) for builds.
  name: Cloudflare Builds API
  slug: cloudflare-builds-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cache Reserve Clear API from Cloudflare — 1 operation(s) for cache reserve clear.
  name: Cloudflare Cache Reserve Clear API
  slug: cloudflare-cache-reserve-clear-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Catalog Sync API from Cloudflare — 4 operation(s) for catalog sync.
  name: Cloudflare Catalog Sync API
  slug: cloudflare-catalog-sync-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Category API from Cloudflare — 7 operation(s) for category.
  name: Cloudflare Category API
  slug: cloudflare-category-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Certificate Packs API from Cloudflare — 4 operation(s) for certificate packs.
  name: Cloudflare Certificate Packs API
  slug: cloudflare-certificate-packs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Changelog API from Cloudflare — 1 operation(s) for changelog.
  name: Cloudflare Changelog API
  slug: cloudflare-changelog-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Client-Side Security API from Cloudflare — 9 operation(s) for client-side security.
  name: Cloudflare Client-Side Security API
  slug: cloudflare-client-side-security-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Client Versions API from Cloudflare — 2 operation(s) for client versions.
  name: Cloudflare Client Versions API
  slug: cloudflare-client-versions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloud Integrations API from Cloudflare — 5 operation(s) for cloud integrations.
  name: Cloudflare Cloud Integrations API
  slug: cloudflare-cloud-integrations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Images API from Cloudflare — 8 operation(s) for cloudflare images.
  name: Cloudflare Cloudflare Images API
  slug: cloudflare-cloudflare-images-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Images Keys API from Cloudflare — 2 operation(s) for cloudflare images keys.
  name: Cloudflare Cloudflare Images Keys API
  slug: cloudflare-cloudflare-images-keys-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Images Sourcing Kit API from Cloudflare — 10 operation(s) for cloudflare images sourcing kit.
  name: Cloudflare Cloudflare Images Sourcing Kit API
  slug: cloudflare-cloudflare-images-sourcing-kit-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Images Variants API from Cloudflare — 3 operation(s) for cloudflare images variants.
  name: Cloudflare Cloudflare Images Variants API
  slug: cloudflare-cloudflare-images-variants-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare IPs API from Cloudflare — 1 operation(s) for cloudflare ips.
  name: Cloudflare Cloudflare IPs API
  slug: cloudflare-cloudflare-ips-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Tunnel API from Cloudflare — 13 operation(s) for cloudflare tunnel.
  name: Cloudflare Cloudflare Tunnel API
  slug: cloudflare-cloudflare-tunnel-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Cloudflare Tunnel Configuration API from Cloudflare — 2 operation(s) for cloudflare tunnel configuration.
  name: Cloudflare Cloudflare Tunnel Configuration API
  slug: cloudflare-cloudflare-tunnel-configuration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The CNIs API from Cloudflare — 2 operation(s) for cnis.
  name: Cloudflare CNIs API
  slug: cloudflare-cnis-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Collections API from Cloudflare — 7 operation(s) for collections.
  name: Cloudflare Collections API
  slug: cloudflare-collections-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Collections - Items API from Cloudflare — 2 operation(s) for collections - items.
  name: Cloudflare Collections - Items API
  slug: cloudflare-collections-items-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Communication Preferences API from Cloudflare — 1 operation(s) for communication preferences.
  name: Cloudflare Communication Preferences API
  slug: cloudflare-communication-preferences-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Connectivity Services API from Cloudflare — 2 operation(s) for connectivity services.
  name: Cloudflare Connectivity Services API
  slug: cloudflare-connectivity-services-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Container Images API from Cloudflare — 1 operation(s) for container images.
  name: Cloudflare Container Images API
  slug: cloudflare-container-images-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Container Instances API from Cloudflare — 3 operation(s) for container instances.
  name: Cloudflare Container Instances API
  slug: cloudflare-container-instances-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The content API from Cloudflare — 1 operation(s) for content.
  name: Cloudflare Content API
  slug: cloudflare-content-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Content Scanning API from Cloudflare — 5 operation(s) for content scanning.
  name: Cloudflare Content Scanning API
  slug: cloudflare-content-scanning-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Country API from Cloudflare — 1 operation(s) for country.
  name: Cloudflare Country API
  slug: cloudflare-country-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Credential Management API from Cloudflare — 4 operation(s) for credential management.
  name: Cloudflare Credential Management API
  slug: cloudflare-credential-management-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Credential Sets API from Cloudflare — 2 operation(s) for credential sets.
  name: Cloudflare Credential Sets API
  slug: cloudflare-credential-sets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Credentials API from Cloudflare — 2 operation(s) for credentials.
  name: Cloudflare Credentials API
  slug: cloudflare-credentials-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The CSAM Scanner Settings API from Cloudflare — 1 operation(s) for csam scanner settings.
  name: Cloudflare CSAM Scanner Settings API
  slug: cloudflare-csam-scanner-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The CT Alerting API from Cloudflare — 1 operation(s) for ct alerting.
  name: Cloudflare CT Alerting API
  slug: cloudflare-ct-alerting-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom assets for a zone API from Cloudflare — 2 operation(s) for custom assets for a zone.
  name: Cloudflare Custom assets for a zone API
  slug: cloudflare-custom-assets-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom assets for an account API from Cloudflare — 2 operation(s) for custom assets for an account.
  name: Cloudflare Custom assets for an account API
  slug: cloudflare-custom-assets-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom CSRs for a Zone API from Cloudflare — 2 operation(s) for custom csrs for a zone.
  name: Cloudflare Custom CSRs for a Zone API
  slug: cloudflare-custom-csrs-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom CSRs for an Account API from Cloudflare — 2 operation(s) for custom csrs for an account.
  name: Cloudflare Custom CSRs for an Account API
  slug: cloudflare-custom-csrs-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom Hostname Fallback Origin for a Zone API from Cloudflare — 1 operation(s) for custom hostname fallback origin for a zone.
  name: Cloudflare Custom Hostname Fallback Origin for a Zone API
  slug: cloudflare-custom-hostname-fallback-origin-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom Hostname for a Zone API from Cloudflare — 4 operation(s) for custom hostname for a zone.
  name: Cloudflare Custom Hostname for a Zone API
  slug: cloudflare-custom-hostname-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom Indicator Feeds API from Cloudflare — 10 operation(s) for custom indicator feeds.
  name: Cloudflare Custom Indicator Feeds API
  slug: cloudflare-custom-indicator-feeds-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom Nameserver Sets for an Account API from Cloudflare — 2 operation(s) for custom nameserver sets for an account.
  name: Cloudflare Custom Nameserver Sets for an Account API
  slug: cloudflare-custom-nameserver-sets-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom Origin Trust Store API from Cloudflare — 2 operation(s) for custom origin trust store.
  name: Cloudflare Custom Origin Trust Store API
  slug: cloudflare-custom-origin-trust-store-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom pages for a zone API from Cloudflare — 3 operation(s) for custom pages for a zone.
  name: Cloudflare Custom pages for a zone API
  slug: cloudflare-custom-pages-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom pages for an account API from Cloudflare — 3 operation(s) for custom pages for an account.
  name: Cloudflare Custom pages for an account API
  slug: cloudflare-custom-pages-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Custom SSL for a Zone API from Cloudflare — 3 operation(s) for custom ssl for a zone.
  name: Cloudflare Custom SSL for a Zone API
  slug: cloudflare-custom-ssl-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The D1 API from Cloudflare — 8 operation(s) for d1.
  name: Cloudflare D1 API
  slug: cloudflare-d1-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Dashboard Assets API from Cloudflare — 3 operation(s) for dashboard assets.
  name: Cloudflare Dashboard Assets API
  slug: cloudflare-dashboard-assets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Dashboard - Users API from Cloudflare — 1 operation(s) for dashboard - users.
  name: Cloudflare Dashboard - Users API
  slug: cloudflare-dashboard-users-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Data Security API from Cloudflare — 3 operation(s) for data security.
  name: Cloudflare Data Security API
  slug: cloudflare-data-security-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Dataset API from Cloudflare — 3 operation(s) for dataset.
  name: Cloudflare Dataset API
  slug: cloudflare-dataset-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Datasets API from Cloudflare — 1 operation(s) for datasets.
  name: Cloudflare Datasets API
  slug: cloudflare-datasets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DCV Delegation API from Cloudflare — 1 operation(s) for dcv delegation.
  name: Cloudflare DCV Delegation API
  slug: cloudflare-dcv-delegation-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Definitions API from Cloudflare — 1 operation(s) for definitions.
  name: Cloudflare Definitions API
  slug: cloudflare-definitions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Deploy Hooks API from Cloudflare — 3 operation(s) for deploy hooks.
  name: Cloudflare Deploy Hooks API
  slug: cloudflare-deploy-hooks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Deployment Groups API from Cloudflare — 2 operation(s) for deployment groups.
  name: Cloudflare Deployment Groups API
  slug: cloudflare-deployment-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Destinations API from Cloudflare — 2 operation(s) for destinations.
  name: Cloudflare Destinations API
  slug: cloudflare-destinations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Device Managed Networks API from Cloudflare — 2 operation(s) for device managed networks.
  name: Cloudflare Device Managed Networks API
  slug: cloudflare-device-managed-networks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Device Posture Integrations API from Cloudflare — 2 operation(s) for device posture integrations.
  name: Cloudflare Device Posture Integrations API
  slug: cloudflare-device-posture-integrations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Device posture rules API from Cloudflare — 2 operation(s) for device posture rules.
  name: Cloudflare Device posture rules API
  slug: cloudflare-device-posture-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Devices API from Cloudflare — 15 operation(s) for devices.
  name: Cloudflare Devices API
  slug: cloudflare-devices-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Devices Resilience API from Cloudflare — 1 operation(s) for devices resilience.
  name: Cloudflare Devices Resilience API
  slug: cloudflare-devices-resilience-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DEX Remote Commands API from Cloudflare — 4 operation(s) for dex remote commands.
  name: Cloudflare DEX Remote Commands API
  slug: cloudflare-dex-remote-commands-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DEX Rules API from Cloudflare — 2 operation(s) for dex rules.
  name: Cloudflare DEX Rules API
  slug: cloudflare-dex-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DEX Synthetic Application Monitoring API from Cloudflare — 17 operation(s) for dex synthetic application monitoring.
  name: Cloudflare DEX Synthetic Application Monitoring API
  slug: cloudflare-dex-synthetic-application-monitoring-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Diagnostics API from Cloudflare — 1 operation(s) for diagnostics.
  name: Cloudflare Diagnostics API
  slug: cloudflare-diagnostics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Custom Prompt Topics API from Cloudflare — 2 operation(s) for dlp custom prompt topics.
  name: Cloudflare DLP Custom Prompt Topics API
  slug: cloudflare-dlp-custom-prompt-topics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Data Classes API from Cloudflare — 2 operation(s) for dlp data classes.
  name: Cloudflare DLP Data Classes API
  slug: cloudflare-dlp-data-classes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Data Tag Categories API from Cloudflare — 2 operation(s) for dlp data tag categories.
  name: Cloudflare DLP Data Tag Categories API
  slug: cloudflare-dlp-data-tag-categories-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Data Tag Category Templates API from Cloudflare — 2 operation(s) for dlp data tag category templates.
  name: Cloudflare DLP Data Tag Category Templates API
  slug: cloudflare-dlp-data-tag-category-templates-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Data Tags API from Cloudflare — 2 operation(s) for dlp data tags.
  name: Cloudflare DLP Data Tags API
  slug: cloudflare-dlp-data-tags-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Datasets API from Cloudflare — 6 operation(s) for dlp datasets.
  name: Cloudflare DLP Datasets API
  slug: cloudflare-dlp-datasets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Document Fingerprints API from Cloudflare — 2 operation(s) for dlp document fingerprints.
  name: Cloudflare DLP Document Fingerprints API
  slug: cloudflare-dlp-document-fingerprints-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Email API from Cloudflare — 3 operation(s) for dlp email.
  name: Cloudflare DLP Email API
  slug: cloudflare-dlp-email-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Entries API from Cloudflare — 4 operation(s) for dlp entries.
  name: Cloudflare DLP Entries API
  slug: cloudflare-dlp-entries-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Integration Entries API from Cloudflare — 2 operation(s) for dlp integration entries.
  name: Cloudflare DLP Integration Entries API
  slug: cloudflare-dlp-integration-entries-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Predefined Entries API from Cloudflare — 2 operation(s) for dlp predefined entries.
  name: Cloudflare DLP Predefined Entries API
  slug: cloudflare-dlp-predefined-entries-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Profiles API from Cloudflare — 7 operation(s) for dlp profiles.
  name: Cloudflare DLP Profiles API
  slug: cloudflare-dlp-profiles-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Sensitivity Group Templates API from Cloudflare — 2 operation(s) for dlp sensitivity group templates.
  name: Cloudflare DLP Sensitivity Group Templates API
  slug: cloudflare-dlp-sensitivity-group-templates-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Sensitivity Groups API from Cloudflare — 3 operation(s) for dlp sensitivity groups.
  name: Cloudflare DLP Sensitivity Groups API
  slug: cloudflare-dlp-sensitivity-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Sensitivity Levels API from Cloudflare — 2 operation(s) for dlp sensitivity levels.
  name: Cloudflare DLP Sensitivity Levels API
  slug: cloudflare-dlp-sensitivity-levels-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLP Settings API from Cloudflare — 4 operation(s) for dlp settings.
  name: Cloudflare DLP Settings API
  slug: cloudflare-dlp-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DLS Regional Services API from Cloudflare — 3 operation(s) for dls regional services.
  name: Cloudflare DLS Regional Services API
  slug: cloudflare-dls-regional-services-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DNS Firewall Analytics API from Cloudflare — 2 operation(s) for dns firewall analytics.
  name: Cloudflare DNS Firewall Analytics API
  slug: cloudflare-dns-firewall-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DNS Firewall API from Cloudflare — 3 operation(s) for dns firewall.
  name: Cloudflare DNS Firewall API
  slug: cloudflare-dns-firewall-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DNS Internal Views for an Account API from Cloudflare — 2 operation(s) for dns internal views for an account.
  name: Cloudflare DNS Internal Views for an Account API
  slug: cloudflare-dns-internal-views-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DNS Records for a Zone API from Cloudflare — 9 operation(s) for dns records for a zone.
  name: Cloudflare DNS Records for a Zone API
  slug: cloudflare-dns-records-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DNS Records for an Account API from Cloudflare — 1 operation(s) for dns records for an account.
  name: Cloudflare DNS Records for an Account API
  slug: cloudflare-dns-records-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DNS Settings for a Zone API from Cloudflare — 1 operation(s) for dns settings for a zone.
  name: Cloudflare DNS Settings for a Zone API
  slug: cloudflare-dns-settings-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The DNS Settings for an Account API from Cloudflare — 1 operation(s) for dns settings for an account.
  name: Cloudflare DNS Settings for an Account API
  slug: cloudflare-dns-settings-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Domain Discovery API from Cloudflare — 5 operation(s) for domain discovery.
  name: Cloudflare Domain Discovery API
  slug: cloudflare-domain-discovery-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Domain History API from Cloudflare — 1 operation(s) for domain history.
  name: Cloudflare Domain History API
  slug: cloudflare-domain-history-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Domain Intelligence API from Cloudflare — 2 operation(s) for domain intelligence.
  name: Cloudflare Domain Intelligence API
  slug: cloudflare-domain-intelligence-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The domain_search API from Cloudflare — 8 operation(s) for domain_search.
  name: Cloudflare Domain Search API
  slug: cloudflare-domain-search-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The dos-flowtrackd-api_other API from Cloudflare — 16 operation(s) for dos-flowtrackd-api_other.
  name: Cloudflare Dos Flowtrackd API Other API
  slug: cloudflare-dos-flowtrackd-api-other-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Durable Objects Namespace API from Cloudflare — 3 operation(s) for durable objects namespace.
  name: Cloudflare Durable Objects Namespace API
  slug: cloudflare-durable-objects-namespace-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Auth API from Cloudflare — 2 operation(s) for email auth.
  name: Cloudflare Email Auth API
  slug: cloudflare-email-auth-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Routing destination addresses API from Cloudflare — 2 operation(s) for email routing destination addresses.
  name: Cloudflare Email Routing destination addresses API
  slug: cloudflare-email-routing-destination-addresses-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Routing routing rules API from Cloudflare — 5 operation(s) for email routing routing rules.
  name: Cloudflare Email Routing routing rules API
  slug: cloudflare-email-routing-routing-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Routing settings API from Cloudflare — 5 operation(s) for email routing settings.
  name: Cloudflare Email Routing settings API
  slug: cloudflare-email-routing-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Routing suppressions API from Cloudflare — 4 operation(s) for email routing suppressions.
  name: Cloudflare Email Routing suppressions API
  slug: cloudflare-email-routing-suppressions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Security Analytics API from Cloudflare — 1 operation(s) for email security analytics.
  name: Cloudflare Email Security Analytics API
  slug: cloudflare-email-security-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Security API from Cloudflare — 18 operation(s) for email security.
  name: Cloudflare Email Security API
  slug: cloudflare-email-security-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Security Settings API from Cloudflare — 24 operation(s) for email security settings.
  name: Cloudflare Email Security Settings API
  slug: cloudflare-email-security-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Sending API from Cloudflare — 5 operation(s) for email sending.
  name: Cloudflare Email Sending API
  slug: cloudflare-email-sending-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Sending subdomains API from Cloudflare — 6 operation(s) for email sending subdomains.
  name: Cloudflare Email Sending subdomains API
  slug: cloudflare-email-sending-subdomains-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Email Sending suppressions API from Cloudflare — 7 operation(s) for email sending suppressions.
  name: Cloudflare Email Sending suppressions API
  slug: cloudflare-email-sending-suppressions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Endpoint Health Checks API from Cloudflare — 2 operation(s) for endpoint health checks.
  name: Cloudflare Endpoint Health Checks API
  slug: cloudflare-endpoint-health-checks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Environment Variables API from Cloudflare — 2 operation(s) for environment variables.
  name: Cloudflare Environment Variables API
  slug: cloudflare-environment-variables-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Evaluation API from Cloudflare — 1 operation(s) for evaluation.
  name: Cloudflare Evaluation API
  slug: cloudflare-evaluation-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Event API from Cloudflare — 27 operation(s) for event.
  name: Cloudflare Event API
  slug: cloudflare-event-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Events API from Cloudflare — 1 operation(s) for events.
  name: Cloudflare Events API
  slug: cloudflare-events-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The exports API from Cloudflare — 6 operation(s) for exports.
  name: Cloudflare Exports API
  slug: cloudflare-exports-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Extension API from Cloudflare — 4 operation(s) for extension.
  name: Cloudflare Extension API
  slug: cloudflare-extension-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Feedback API from Cloudflare — 1 operation(s) for feedback.
  name: Cloudflare Feedback API
  slug: cloudflare-feedback-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Field Extractors API from Cloudflare — 1 operation(s) for field extractors.
  name: Cloudflare Field Extractors API
  slug: cloudflare-field-extractors-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Filters API from Cloudflare — 2 operation(s) for filters.
  name: Cloudflare Filters API
  slug: cloudflare-filters-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The finding_types API from Cloudflare — 3 operation(s) for finding_types.
  name: Cloudflare Finding Types API
  slug: cloudflare-finding-types-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The findings API from Cloudflare — 10 operation(s) for findings.
  name: Cloudflare Findings API
  slug: cloudflare-findings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Finetune Asset API from Cloudflare — 1 operation(s) for finetune asset.
  name: Cloudflare Finetune Asset API
  slug: cloudflare-finetune-asset-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Firewall rules API from Cloudflare — 2 operation(s) for firewall rules.
  name: Cloudflare Firewall rules API
  slug: cloudflare-firewall-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Flags API from Cloudflare — 2 operation(s) for flags.
  name: Cloudflare Flags API
  slug: cloudflare-flags-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Fraud Detection API from Cloudflare — 1 operation(s) for fraud detection.
  name: Cloudflare Fraud Detection API
  slug: cloudflare-fraud-detection-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Gateway CA API from Cloudflare — 2 operation(s) for gateway ca.
  name: Cloudflare Gateway CA API
  slug: cloudflare-gateway-ca-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The GitHub Integration API from Cloudflare — 1 operation(s) for github integration.
  name: Cloudflare GitHub Integration API
  slug: cloudflare-github-integration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Google Tag Gateway API from Cloudflare — 1 operation(s) for google tag gateway.
  name: Cloudflare Google Tag Gateway API
  slug: cloudflare-google-tag-gateway-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Groups API from Cloudflare — 4 operation(s) for groups.
  name: Cloudflare Groups API
  slug: cloudflare-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Health API from Cloudflare — 1 operation(s) for health.
  name: Cloudflare Health API
  slug: cloudflare-health-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Health Checks API from Cloudflare — 6 operation(s) for health checks.
  name: Cloudflare Health Checks API
  slug: cloudflare-health-checks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Hyperdrive API from Cloudflare — 4 operation(s) for hyperdrive.
  name: Cloudflare Hyperdrive API
  slug: cloudflare-hyperdrive-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Image Registries API from Cloudflare — 3 operation(s) for image registries.
  name: Cloudflare Image Registries API
  slug: cloudflare-image-registries-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Indicator API from Cloudflare — 9 operation(s) for indicator.
  name: Cloudflare Indicator API
  slug: cloudflare-indicator-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Indicator Types API from Cloudflare — 2 operation(s) for indicator types.
  name: Cloudflare Indicator Types API
  slug: cloudflare-indicator-types-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Indicators API from Cloudflare — 1 operation(s) for indicators.
  name: Cloudflare Indicators API
  slug: cloudflare-indicators-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Infrastructure Access Targets API from Cloudflare — 5 operation(s) for infrastructure access targets.
  name: Cloudflare Infrastructure Access Targets API
  slug: cloudflare-infrastructure-access-targets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Instant Logs jobs for a zone API from Cloudflare — 1 operation(s) for instant logs jobs for a zone.
  name: Cloudflare Instant Logs jobs for a zone API
  slug: cloudflare-instant-logs-jobs-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Integrations API from Cloudflare — 4 operation(s) for integrations.
  name: Cloudflare Integrations API
  slug: cloudflare-integrations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Interconnects API from Cloudflare — 5 operation(s) for interconnects.
  name: Cloudflare Interconnects API
  slug: cloudflare-interconnects-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Access rules for a user API from Cloudflare — 2 operation(s) for ip access rules for a user.
  name: Cloudflare IP Access rules for a user API
  slug: cloudflare-ip-access-rules-for-a-user-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Access rules for a zone API from Cloudflare — 2 operation(s) for ip access rules for a zone.
  name: Cloudflare IP Access rules for a zone API
  slug: cloudflare-ip-access-rules-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Access rules for an account API from Cloudflare — 2 operation(s) for ip access rules for an account.
  name: Cloudflare IP Access rules for an account API
  slug: cloudflare-ip-access-rules-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Address Management Address Maps API from Cloudflare — 5 operation(s) for ip address management address maps.
  name: Cloudflare IP Address Management Address Maps API
  slug: cloudflare-ip-address-management-address-maps-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Address Management BGP Prefixes API from Cloudflare — 2 operation(s) for ip address management bgp prefixes.
  name: Cloudflare IP Address Management BGP Prefixes API
  slug: cloudflare-ip-address-management-bgp-prefixes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Address Management Dynamic Advertisement API from Cloudflare — 1 operation(s) for ip address management dynamic advertisement.
  name: Cloudflare IP Address Management Dynamic Advertisement API
  slug: cloudflare-ip-address-management-dynamic-advertisement-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Address Management Leases API from Cloudflare — 1 operation(s) for ip address management leases.
  name: Cloudflare IP Address Management Leases API
  slug: cloudflare-ip-address-management-leases-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Address Management Prefix Delegation API from Cloudflare — 2 operation(s) for ip address management prefix delegation.
  name: Cloudflare IP Address Management Prefix Delegation API
  slug: cloudflare-ip-address-management-prefix-delegation-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Address Management Prefixes API from Cloudflare — 5 operation(s) for ip address management prefixes.
  name: Cloudflare IP Address Management Prefixes API
  slug: cloudflare-ip-address-management-prefixes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Address Management Service Bindings API from Cloudflare — 3 operation(s) for ip address management service bindings.
  name: Cloudflare IP Address Management Service Bindings API
  slug: cloudflare-ip-address-management-service-bindings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Intelligence API from Cloudflare — 1 operation(s) for ip intelligence.
  name: Cloudflare IP Intelligence API
  slug: cloudflare-ip-intelligence-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP List API from Cloudflare — 1 operation(s) for ip list.
  name: Cloudflare IP List API
  slug: cloudflare-ip-list-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The IP Profiles API from Cloudflare — 2 operation(s) for ip profiles.
  name: Cloudflare IP Profiles API
  slug: cloudflare-ip-profiles-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Issues API from Cloudflare — 11 operation(s) for issues.
  name: Cloudflare Issues API
  slug: cloudflare-issues-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Keyless SSL for a Zone API from Cloudflare — 2 operation(s) for keyless ssl for a zone.
  name: Cloudflare Keyless SSL for a Zone API
  slug: cloudflare-keyless-ssl-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Leaked Credential Checks API from Cloudflare — 3 operation(s) for leaked credential checks.
  name: Cloudflare Leaked Credential Checks API
  slug: cloudflare-leaked-credential-checks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Lists API from Cloudflare — 5 operation(s) for lists.
  name: Cloudflare Lists API
  slug: cloudflare-lists-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Live streams API from Cloudflare — 11 operation(s) for live streams.
  name: Cloudflare Live streams API
  slug: cloudflare-live-streams-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Live Tail API from Cloudflare — 2 operation(s) for live tail.
  name: Cloudflare Live Tail API
  slug: cloudflare-live-tail-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The LivestreamAnalytics API from Cloudflare — 2 operation(s) for livestreamanalytics.
  name: Cloudflare Livestream Analytics API
  slug: cloudflare-livestreamanalytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Load Balancer Healthcheck Events API from Cloudflare — 1 operation(s) for load balancer healthcheck events.
  name: Cloudflare Load Balancer Healthcheck Events API
  slug: cloudflare-load-balancer-healthcheck-events-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Load Balancer Monitors API from Cloudflare — 5 operation(s) for load balancer monitors.
  name: Cloudflare Load Balancer Monitors API
  slug: cloudflare-load-balancer-monitors-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Load Balancer Pools API from Cloudflare — 5 operation(s) for load balancer pools.
  name: Cloudflare Load Balancer Pools API
  slug: cloudflare-load-balancer-pools-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Load Balancer Regions API from Cloudflare — 3 operation(s) for load balancer regions.
  name: Cloudflare Load Balancer Regions API
  slug: cloudflare-load-balancer-regions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Load Balancers API from Cloudflare — 2 operation(s) for load balancers.
  name: Cloudflare Load Balancers API
  slug: cloudflare-load-balancers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Log Explorer Datasets API from Cloudflare — 6 operation(s) for log explorer datasets.
  name: Cloudflare Log Explorer Datasets API
  slug: cloudflare-log-explorer-datasets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Log Explorer Queries API from Cloudflare — 2 operation(s) for log explorer queries.
  name: Cloudflare Log Explorer Queries API
  slug: cloudflare-log-explorer-queries-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Logcontrol CMB config for an account API from Cloudflare — 1 operation(s) for logcontrol cmb config for an account.
  name: Cloudflare Logcontrol CMB config for an account API
  slug: cloudflare-logcontrol-cmb-config-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The logo_match API from Cloudflare — 7 operation(s) for logo_match.
  name: Cloudflare Logo Match API
  slug: cloudflare-logo-match-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Logpull API from Cloudflare — 2 operation(s) for logpull.
  name: Cloudflare Logpull API
  slug: cloudflare-logpull-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Logpush jobs for a zone API from Cloudflare — 9 operation(s) for logpush jobs for a zone.
  name: Cloudflare Logpush jobs for a zone API
  slug: cloudflare-logpush-jobs-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Logpush jobs for an account API from Cloudflare — 9 operation(s) for logpush jobs for an account.
  name: Cloudflare Logpush jobs for an account API
  slug: cloudflare-logpush-jobs-for-an-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Logpush transformers API from Cloudflare — 5 operation(s) for logpush transformers.
  name: Cloudflare Logpush transformers API
  slug: cloudflare-logpush-transformers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Logs Received API from Cloudflare — 4 operation(s) for logs received.
  name: Cloudflare Logs Received API
  slug: cloudflare-logs-received-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Account Apps API from Cloudflare — 2 operation(s) for magic account apps.
  name: Cloudflare Magic Account Apps API
  slug: cloudflare-magic-account-apps-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic BGP Filter Profiles API from Cloudflare — 2 operation(s) for magic bgp filter profiles.
  name: Cloudflare Magic BGP Filter Profiles API
  slug: cloudflare-magic-bgp-filter-profiles-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic BGP Settings API from Cloudflare — 1 operation(s) for magic bgp settings.
  name: Cloudflare Magic BGP Settings API
  slug: cloudflare-magic-bgp-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic CF1 Site Ramps API from Cloudflare — 2 operation(s) for magic cf1 site ramps.
  name: Cloudflare Magic CF1 Site Ramps API
  slug: cloudflare-magic-cf1-site-ramps-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic CF1 Sites API from Cloudflare — 2 operation(s) for magic cf1 sites.
  name: Cloudflare Magic CF1 Sites API
  slug: cloudflare-magic-cf1-sites-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Connectors API from Cloudflare — 9 operation(s) for magic connectors.
  name: Cloudflare Magic Connectors API
  slug: cloudflare-magic-connectors-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic GRE tunnels API from Cloudflare — 2 operation(s) for magic gre tunnels.
  name: Cloudflare Magic GRE tunnels API
  slug: cloudflare-magic-gre-tunnels-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Interconnects API from Cloudflare — 2 operation(s) for magic interconnects.
  name: Cloudflare Magic Interconnects API
  slug: cloudflare-magic-interconnects-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic IPsec tunnels API from Cloudflare — 4 operation(s) for magic ipsec tunnels.
  name: Cloudflare Magic IPsec tunnels API
  slug: cloudflare-magic-ipsec-tunnels-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Network Monitoring Configuration API from Cloudflare — 2 operation(s) for magic network monitoring configuration.
  name: Cloudflare Magic Network Monitoring Configuration API
  slug: cloudflare-magic-network-monitoring-configuration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Network Monitoring Rules API from Cloudflare — 4 operation(s) for magic network monitoring rules.
  name: Cloudflare Magic Network Monitoring Rules API
  slug: cloudflare-magic-network-monitoring-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Network Monitoring VPC Flow logs API from Cloudflare — 1 operation(s) for magic network monitoring vpc flow logs.
  name: Cloudflare Magic Network Monitoring VPC Flow logs API
  slug: cloudflare-magic-network-monitoring-vpc-flow-logs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic PCAP collection API from Cloudflare — 7 operation(s) for magic pcap collection.
  name: Cloudflare Magic PCAP collection API
  slug: cloudflare-magic-pcap-collection-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Redundancy Groups API from Cloudflare — 2 operation(s) for magic redundancy groups.
  name: Cloudflare Magic Redundancy Groups API
  slug: cloudflare-magic-redundancy-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Site ACLs API from Cloudflare — 2 operation(s) for magic site acls.
  name: Cloudflare Magic Site ACLs API
  slug: cloudflare-magic-site-acls-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Site App Configs API from Cloudflare — 2 operation(s) for magic site app configs.
  name: Cloudflare Magic Site App Configs API
  slug: cloudflare-magic-site-app-configs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Site LANs API from Cloudflare — 2 operation(s) for magic site lans.
  name: Cloudflare Magic Site LANs API
  slug: cloudflare-magic-site-lans-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Site NetFlow Config API from Cloudflare — 1 operation(s) for magic site netflow config.
  name: Cloudflare Magic Site NetFlow Config API
  slug: cloudflare-magic-site-netflow-config-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Site WANs API from Cloudflare — 2 operation(s) for magic site wans.
  name: Cloudflare Magic Site WANs API
  slug: cloudflare-magic-site-wans-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Sites API from Cloudflare — 2 operation(s) for magic sites.
  name: Cloudflare Magic Sites API
  slug: cloudflare-magic-sites-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Magic Static Routes API from Cloudflare — 2 operation(s) for magic static routes.
  name: Cloudflare Magic Static Routes API
  slug: cloudflare-magic-static-routes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Maintenance Configuration API from Cloudflare — 2 operation(s) for maintenance configuration.
  name: Cloudflare Maintenance Configuration API
  slug: cloudflare-maintenance-configuration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Managed Transforms API from Cloudflare — 1 operation(s) for managed transforms.
  name: Cloudflare Managed Transforms API
  slug: cloudflare-managed-transforms-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The MCP Portal Analytics API from Cloudflare — 3 operation(s) for mcp portal analytics.
  name: Cloudflare MCP Portal Analytics API
  slug: cloudflare-mcp-portal-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The MCP Portal API from Cloudflare — 3 operation(s) for mcp portal.
  name: Cloudflare MCP Portal API
  slug: cloudflare-mcp-portal-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The MCP Portal Servers API from Cloudflare — 3 operation(s) for mcp portal servers.
  name: Cloudflare MCP Portal Servers API
  slug: cloudflare-mcp-portal-servers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Meetings API from Cloudflare — 5 operation(s) for meetings.
  name: Cloudflare Meetings API
  slug: cloudflare-meetings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Memory API from Cloudflare — 9 operation(s) for memory.
  name: Cloudflare Memory API
  slug: cloudflare-memory-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Metrics Export API from Cloudflare — 1 operation(s) for metrics export.
  name: Cloudflare Metrics Export API
  slug: cloudflare-metrics-export-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Miscategorization API from Cloudflare — 1 operation(s) for miscategorization.
  name: Cloudflare Miscategorization API
  slug: cloudflare-miscategorization-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Monetization API from Cloudflare — 4 operation(s) for monetization.
  name: Cloudflare Monetization API
  slug: cloudflare-monetization-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The MoQ Relays API from Cloudflare — 4 operation(s) for moq relays.
  name: Cloudflare MoQ Relays API
  slug: cloudflare-moq-relays-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The mTLS Certificate Management API from Cloudflare — 3 operation(s) for mtls certificate management.
  name: Cloudflare mTLS Certificate Management API
  slug: cloudflare-mtls-certificate-management-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Namespace Management API from Cloudflare — 2 operation(s) for namespace management.
  name: Cloudflare Namespace Management API
  slug: cloudflare-namespace-management-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The NEL Settings API from Cloudflare — 1 operation(s) for nel settings.
  name: Cloudflare NEL Settings API
  slug: cloudflare-nel-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Notification Alert Types API from Cloudflare — 1 operation(s) for notification alert types.
  name: Cloudflare Notification Alert Types API
  slug: cloudflare-notification-alert-types-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Notification destinations with PagerDuty API from Cloudflare — 3 operation(s) for notification destinations with pagerduty.
  name: Cloudflare Notification destinations with PagerDuty API
  slug: cloudflare-notification-destinations-with-pagerduty-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Notification History API from Cloudflare — 1 operation(s) for notification history.
  name: Cloudflare Notification History API
  slug: cloudflare-notification-history-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Notification Mechanism Eligibility API from Cloudflare — 1 operation(s) for notification mechanism eligibility.
  name: Cloudflare Notification Mechanism Eligibility API
  slug: cloudflare-notification-mechanism-eligibility-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Notification policies API from Cloudflare — 4 operation(s) for notification policies.
  name: Cloudflare Notification policies API
  slug: cloudflare-notification-policies-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Notification Silences API from Cloudflare — 2 operation(s) for notification silences.
  name: Cloudflare Notification Silences API
  slug: cloudflare-notification-silences-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Notification webhooks API from Cloudflare — 2 operation(s) for notification webhooks.
  name: Cloudflare Notification webhooks API
  slug: cloudflare-notification-webhooks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The OAuth Clients API from Cloudflare — 4 operation(s) for oauth clients.
  name: Cloudflare OAuth Clients API
  slug: cloudflare-oauth-clients-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Observability API from Cloudflare — 2 operation(s) for observability.
  name: Cloudflare Observability API
  slug: cloudflare-observability-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Observatory API from Cloudflare — 6 operation(s) for observatory.
  name: Cloudflare Observatory API
  slug: cloudflare-observatory-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The On-ramps API from Cloudflare — 6 operation(s) for on-ramps.
  name: Cloudflare On Ramps API
  slug: cloudflare-on-ramps-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Origin CA API from Cloudflare — 2 operation(s) for origin ca.
  name: Cloudflare Origin CA API
  slug: cloudflare-origin-ca-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Origin Cloud Regions API from Cloudflare — 8 operation(s) for origin cloud regions.
  name: Cloudflare Origin Cloud Regions API
  slug: cloudflare-origin-cloud-regions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Origin Post-Quantum API from Cloudflare — 1 operation(s) for origin post-quantum.
  name: Cloudflare Origin Post-Quantum API
  slug: cloudflare-origin-post-quantum-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Origin TLS API from Cloudflare — 2 operation(s) for origin tls.
  name: Cloudflare Origin TLS API
  slug: cloudflare-origin-tls-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Override Codes API from Cloudflare — 1 operation(s) for override codes.
  name: Cloudflare Override Codes API
  slug: cloudflare-override-codes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Page Rules API from Cloudflare — 2 operation(s) for page rules.
  name: Cloudflare Page Rules API
  slug: cloudflare-page-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Pages Assets API from Cloudflare — 3 operation(s) for pages assets.
  name: Cloudflare Pages Assets API
  slug: cloudflare-pages-assets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Pages Build Cache API from Cloudflare — 1 operation(s) for pages build cache.
  name: Cloudflare Pages Build Cache API
  slug: cloudflare-pages-build-cache-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Pages Deployment API from Cloudflare — 7 operation(s) for pages deployment.
  name: Cloudflare Pages Deployment API
  slug: cloudflare-pages-deployment-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Pages Domains API from Cloudflare — 2 operation(s) for pages domains.
  name: Cloudflare Pages Domains API
  slug: cloudflare-pages-domains-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Pages Project API from Cloudflare — 4 operation(s) for pages project.
  name: Cloudflare Pages Project API
  slug: cloudflare-pages-project-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Passive DNS by IP API from Cloudflare — 1 operation(s) for passive dns by ip.
  name: Cloudflare Passive DNS by IP API
  slug: cloudflare-passive-dns-by-ip-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Per-hostname Authenticated Origin Pull API from Cloudflare — 4 operation(s) for per-hostname authenticated origin pull.
  name: Cloudflare Per-hostname Authenticated Origin Pull API
  slug: cloudflare-per-hostname-authenticated-origin-pull-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Per-Hostname TLS Settings API from Cloudflare — 2 operation(s) for per-hostname tls settings.
  name: Cloudflare Per-Hostname TLS Settings API
  slug: cloudflare-per-hostname-tls-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Permissions API from Cloudflare — 2 operation(s) for permissions.
  name: Cloudflare Permissions API
  slug: cloudflare-permissions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Physical Devices API from Cloudflare — 4 operation(s) for physical devices.
  name: Cloudflare Physical Devices API
  slug: cloudflare-physical-devices-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The policies API from Cloudflare — 3 operation(s) for policies.
  name: Cloudflare Policies API
  slug: cloudflare-policies-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppc_config API from Cloudflare — 4 operation(s) for ppc_config.
  name: Cloudflare Ppc Config API
  slug: cloudflare-ppc-config-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppc_crawlers API from Cloudflare — 1 operation(s) for ppc_crawlers.
  name: Cloudflare Ppc Crawlers API
  slug: cloudflare-ppc-crawlers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppc_stripe API from Cloudflare — 2 operation(s) for ppc_stripe.
  name: Cloudflare Ppc Stripe API
  slug: cloudflare-ppc-stripe-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppc_terms API from Cloudflare — 3 operation(s) for ppc_terms.
  name: Cloudflare Ppc Terms API
  slug: cloudflare-ppc-terms-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppu_configuration API from Cloudflare — 4 operation(s) for ppu_configuration.
  name: Cloudflare Ppu Configuration API
  slug: cloudflare-ppu-configuration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppu_enabled_domains API from Cloudflare — 1 operation(s) for ppu_enabled_domains.
  name: Cloudflare Ppu Enabled Domains API
  slug: cloudflare-ppu-enabled-domains-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppu_pricing API from Cloudflare — 3 operation(s) for ppu_pricing.
  name: Cloudflare Ppu Pricing API
  slug: cloudflare-ppu-pricing-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppu_usage_reports API from Cloudflare — 1 operation(s) for ppu_usage_reports.
  name: Cloudflare Ppu Usage Reports API
  slug: cloudflare-ppu-usage-reports-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The ppu_usage_stats API from Cloudflare — 2 operation(s) for ppu_usage_stats.
  name: Cloudflare Ppu Usage Stats API
  slug: cloudflare-ppu-usage-stats-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Precursor API from Cloudflare — 1 operation(s) for precursor.
  name: Cloudflare Precursor API
  slug: cloudflare-precursor-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Prefix Bindings API from Cloudflare — 2 operation(s) for prefix bindings.
  name: Cloudflare Prefix Bindings API
  slug: cloudflare-prefix-bindings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Presets API from Cloudflare — 2 operation(s) for presets.
  name: Cloudflare Presets API
  slug: cloudflare-presets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Preview Deployments API from Cloudflare — 3 operation(s) for preview deployments.
  name: Cloudflare Preview Deployments API
  slug: cloudflare-preview-deployments-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Previews API from Cloudflare — 2 operation(s) for previews.
  name: Cloudflare Previews API
  slug: cloudflare-previews-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Priority Intelligence Requirements API from Cloudflare — 10 operation(s) for priority intelligence requirements.
  name: Cloudflare Priority Intelligence Requirements API
  slug: cloudflare-priority-intelligence-requirements-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Priority Intelligence Requirements (PIR) API from Cloudflare — 4 operation(s) for priority intelligence requirements (pir).
  name: Cloudflare Priority Intelligence Requirements (PIR) API
  slug: cloudflare-priority-intelligence-requirements-pir-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Public - Credential Monitor API from Cloudflare — 3 operation(s) for public - credential monitor.
  name: Cloudflare Public - Credential Monitor API
  slug: cloudflare-public-credential-monitor-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Query API from Cloudflare — 2 operation(s) for query.
  name: Cloudflare Query API
  slug: cloudflare-query-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Query run API from Cloudflare — 1 operation(s) for query run.
  name: Cloudflare Query run API
  slug: cloudflare-query-run-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Queue API from Cloudflare — 17 operation(s) for queue.
  name: Cloudflare Queue API
  slug: cloudflare-queue-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The R2 Account API from Cloudflare — 1 operation(s) for r2 account.
  name: Cloudflare R2 Account API
  slug: cloudflare-r2-account-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The R2 Bucket API from Cloudflare — 15 operation(s) for r2 bucket.
  name: Cloudflare R2 Bucket API
  slug: cloudflare-r2-bucket-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The R2 Catalog API from Cloudflare — 1 operation(s) for r2 catalog.
  name: Cloudflare R2 Catalog API
  slug: cloudflare-r2-catalog-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The R2 Catalog Management API from Cloudflare — 5 operation(s) for r2 catalog management.
  name: Cloudflare R2 Catalog Management API
  slug: cloudflare-r2-catalog-management-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The R2 Object API from Cloudflare — 2 operation(s) for r2 object.
  name: Cloudflare R2 Object API
  slug: cloudflare-r2-object-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The R2 Super Slurper API from Cloudflare — 10 operation(s) for r2 super slurper.
  name: Cloudflare R2 Super Slurper API
  slug: cloudflare-r2-super-slurper-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Agent Readiness API from Cloudflare — 1 operation(s) for radar agent readiness.
  name: Cloudflare Radar Agent Readiness API
  slug: cloudflare-radar-agent-readiness-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar AI Bots API from Cloudflare — 5 operation(s) for radar ai bots.
  name: Cloudflare Radar AI Bots API
  slug: cloudflare-radar-ai-bots-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar AI Inference API from Cloudflare — 6 operation(s) for radar ai inference.
  name: Cloudflare Radar AI Inference API
  slug: cloudflare-radar-ai-inference-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Annotations API from Cloudflare — 4 operation(s) for radar annotations.
  name: Cloudflare Radar Annotations API
  slug: cloudflare-radar-annotations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar AS112 API from Cloudflare — 19 operation(s) for radar as112.
  name: Cloudflare Radar AS112 API
  slug: cloudflare-radar-as112-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Autonomous Systems API from Cloudflare — 6 operation(s) for radar autonomous systems.
  name: Cloudflare Radar Autonomous Systems API
  slug: cloudflare-radar-autonomous-systems-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar BGP API from Cloudflare — 19 operation(s) for radar bgp.
  name: Cloudflare Radar BGP API
  slug: cloudflare-radar-bgp-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Bots API from Cloudflare — 5 operation(s) for radar bots.
  name: Cloudflare Radar Bots API
  slug: cloudflare-radar-bots-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Certificate Transparency API from Cloudflare — 7 operation(s) for radar certificate transparency.
  name: Cloudflare Radar Certificate Transparency API
  slug: cloudflare-radar-certificate-transparency-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Datasets API from Cloudflare — 3 operation(s) for radar datasets.
  name: Cloudflare Radar Datasets API
  slug: cloudflare-radar-datasets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar DNS API from Cloudflare — 25 operation(s) for radar dns.
  name: Cloudflare Radar DNS API
  slug: cloudflare-radar-dns-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Domains Ranking API from Cloudflare — 3 operation(s) for radar domains ranking.
  name: Cloudflare Radar Domains Ranking API
  slug: cloudflare-radar-domains-ranking-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Email Routing API from Cloudflare — 14 operation(s) for radar email routing.
  name: Cloudflare Radar Email Routing API
  slug: cloudflare-radar-email-routing-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Email Security API from Cloudflare — 24 operation(s) for radar email security.
  name: Cloudflare Radar Email Security API
  slug: cloudflare-radar-email-security-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Geolocations API from Cloudflare — 2 operation(s) for radar geolocations.
  name: Cloudflare Radar Geolocations API
  slug: cloudflare-radar-geolocations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar HTTP API from Cloudflare — 41 operation(s) for radar http.
  name: Cloudflare Radar HTTP API
  slug: cloudflare-radar-http-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Internet Services Ranking API from Cloudflare — 3 operation(s) for radar internet services ranking.
  name: Cloudflare Radar Internet Services Ranking API
  slug: cloudflare-radar-internet-services-ranking-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar IP API from Cloudflare — 1 operation(s) for radar ip.
  name: Cloudflare Radar IP API
  slug: cloudflare-radar-ip-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Layer 3 Attacks API from Cloudflare — 22 operation(s) for radar layer 3 attacks.
  name: Cloudflare Radar Layer 3 Attacks API
  slug: cloudflare-radar-layer-3-attacks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Layer 7 Attacks API from Cloudflare — 23 operation(s) for radar layer 7 attacks.
  name: Cloudflare Radar Layer 7 Attacks API
  slug: cloudflare-radar-layer-7-attacks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Leaked Credential Checks API from Cloudflare — 6 operation(s) for radar leaked credential checks.
  name: Cloudflare Radar Leaked Credential Checks API
  slug: cloudflare-radar-leaked-credential-checks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Locations API from Cloudflare — 2 operation(s) for radar locations.
  name: Cloudflare Radar Locations API
  slug: cloudflare-radar-locations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Markdown for Agents API from Cloudflare — 2 operation(s) for radar markdown for agents.
  name: Cloudflare Radar Markdown for Agents API
  slug: cloudflare-radar-markdown-for-agents-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar NetFlows API from Cloudflare — 6 operation(s) for radar netflows.
  name: Cloudflare Radar NetFlows API
  slug: cloudflare-radar-netflows-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Origins API from Cloudflare — 5 operation(s) for radar origins.
  name: Cloudflare Radar Origins API
  slug: cloudflare-radar-origins-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Post-Quantum API from Cloudflare — 3 operation(s) for radar post-quantum.
  name: Cloudflare Radar Post-Quantum API
  slug: cloudflare-radar-post-quantum-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Quality API from Cloudflare — 6 operation(s) for radar quality.
  name: Cloudflare Radar Quality API
  slug: cloudflare-radar-quality-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Robots.txt API from Cloudflare — 2 operation(s) for radar robots.txt.
  name: Cloudflare Radar Robots.txt API
  slug: cloudflare-radar-robots-txt-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Search API from Cloudflare — 1 operation(s) for radar search.
  name: Cloudflare Radar Search API
  slug: cloudflare-radar-search-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar TCP Resets and Timeouts API from Cloudflare — 2 operation(s) for radar tcp resets and timeouts.
  name: Cloudflare Radar TCP Resets and Timeouts API
  slug: cloudflare-radar-tcp-resets-and-timeouts-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Top-Level Domains API from Cloudflare — 4 operation(s) for radar top-level domains.
  name: Cloudflare Radar Top-Level Domains API
  slug: cloudflare-radar-top-level-domains-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Traffic Anomalies API from Cloudflare — 3 operation(s) for radar traffic anomalies.
  name: Cloudflare Radar Traffic Anomalies API
  slug: cloudflare-radar-traffic-anomalies-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Verified Bots API from Cloudflare — 2 operation(s) for radar verified bots.
  name: Cloudflare Radar Verified Bots API
  slug: cloudflare-radar-verified-bots-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Radar Web Crawlers API from Cloudflare — 2 operation(s) for radar web crawlers.
  name: Cloudflare Radar Web Crawlers API
  slug: cloudflare-radar-web-crawlers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Rate Limiting Analytics API from Cloudflare — 1 operation(s) for rate limiting analytics.
  name: Cloudflare Rate Limiting Analytics API
  slug: cloudflare-rate-limiting-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Rate limits for a zone API from Cloudflare — 2 operation(s) for rate limits for a zone.
  name: Cloudflare Rate limits for a zone API
  slug: cloudflare-rate-limits-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Rate Plans API from Cloudflare — 1 operation(s) for rate plans.
  name: Cloudflare Rate Plans API
  slug: cloudflare-rate-plans-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Realtime SFU Apps API from Cloudflare — 2 operation(s) for realtime sfu apps.
  name: Cloudflare Realtime SFU Apps API
  slug: cloudflare-realtime-sfu-apps-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Realtime TURN Keys API from Cloudflare — 2 operation(s) for realtime turn keys.
  name: Cloudflare Realtime TURN Keys API
  slug: cloudflare-realtime-turn-keys-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Recordings API from Cloudflare — 4 operation(s) for recordings.
  name: Cloudflare Recordings API
  slug: cloudflare-recordings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Regions API from Cloudflare — 2 operation(s) for regions.
  name: Cloudflare Regions API
  slug: cloudflare-regions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Registrar Domains API from Cloudflare — 2 operation(s) for registrar domains.
  name: Cloudflare Registrar Domains API
  slug: cloudflare-registrar-domains-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Registrar Registration API from Cloudflare — 8 operation(s) for registrar registration.
  name: Cloudflare Registrar Registration API
  slug: cloudflare-registrar-registration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Registrar Transfer API from Cloudflare — 2 operation(s) for registrar transfer.
  name: Cloudflare Registrar Transfer API
  slug: cloudflare-registrar-transfer-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Registrations API from Cloudflare — 4 operation(s) for registrations.
  name: Cloudflare Registrations API
  slug: cloudflare-registrations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The remediations API from Cloudflare — 1 operation(s) for remediations.
  name: Cloudflare Remediations API
  slug: cloudflare-remediations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The reports_other API from Cloudflare — 5 operation(s) for reports_other.
  name: Cloudflare Reports Other API
  slug: cloudflare-reports-other-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Repository Connections API from Cloudflare — 2 operation(s) for repository connections.
  name: Cloudflare Repository Connections API
  slug: cloudflare-repository-connections-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Request for Information (RFI) API from Cloudflare — 12 operation(s) for request for information (rfi).
  name: Cloudflare Request for Information (RFI) API
  slug: cloudflare-request-for-information-rfi-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Requests - Dashboard API from Cloudflare — 5 operation(s) for requests - dashboard.
  name: Cloudflare Requests - Dashboard API
  slug: cloudflare-requests-dashboard-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Resource Sharing API from Cloudflare — 9 operation(s) for resource sharing.
  name: Cloudflare Resource Sharing API
  slug: cloudflare-resource-sharing-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Resource Tagging API from Cloudflare — 6 operation(s) for resource tagging.
  name: Cloudflare Resource Tagging API
  slug: cloudflare-resource-tagging-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Resources API from Cloudflare — 4 operation(s) for resources.
  name: Cloudflare Resources API
  slug: cloudflare-resources-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The RFI API from Cloudflare — 2 operation(s) for rfi.
  name: Cloudflare RFI API
  slug: cloudflare-rfi-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The RFI Messages API from Cloudflare — 3 operation(s) for rfi messages.
  name: Cloudflare RFI Messages API
  slug: cloudflare-rfi-messages-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Rollouts API from Cloudflare — 1 operation(s) for rollouts.
  name: Cloudflare Rollouts API
  slug: cloudflare-rollouts-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Rules API from Cloudflare — 15 operation(s) for rules.
  name: Cloudflare Rules API
  slug: cloudflare-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Saved Queries API from Cloudflare — 2 operation(s) for saved queries.
  name: Cloudflare Saved Queries API
  slug: cloudflare-saved-queries-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Scans API from Cloudflare — 6 operation(s) for scans.
  name: Cloudflare Scans API
  slug: cloudflare-scans-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Schema Validation API from Cloudflare — 4 operation(s) for schema validation.
  name: Cloudflare Schema Validation API
  slug: cloudflare-schema-validation-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Schema Validation Settings API from Cloudflare — 3 operation(s) for schema validation settings.
  name: Cloudflare Schema Validation Settings API
  slug: cloudflare-schema-validation-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The SCIM Discovery API from Cloudflare — 5 operation(s) for scim discovery.
  name: Cloudflare SCIM Discovery API
  slug: cloudflare-scim-discovery-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The SCIM Groups API from Cloudflare — 2 operation(s) for scim groups.
  name: Cloudflare SCIM Groups API
  slug: cloudflare-scim-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The SCIM Users API from Cloudflare — 2 operation(s) for scim users.
  name: Cloudflare SCIM Users API
  slug: cloudflare-scim-users-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Secondary DNS (ACL) API from Cloudflare — 2 operation(s) for secondary dns (acl).
  name: Cloudflare Secondary DNS (ACL) API
  slug: cloudflare-secondary-dns-acl-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Secondary DNS (Peer) API from Cloudflare — 2 operation(s) for secondary dns (peer).
  name: Cloudflare Secondary DNS (Peer) API
  slug: cloudflare-secondary-dns-peer-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Secondary DNS (Primary Zone) API from Cloudflare — 5 operation(s) for secondary dns (primary zone).
  name: Cloudflare Secondary DNS (Primary Zone) API
  slug: cloudflare-secondary-dns-primary-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Secondary DNS (Secondary Zone) API from Cloudflare — 2 operation(s) for secondary dns (secondary zone).
  name: Cloudflare Secondary DNS (Secondary Zone) API
  slug: cloudflare-secondary-dns-secondary-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Secondary DNS (TSIG) API from Cloudflare — 2 operation(s) for secondary dns (tsig).
  name: Cloudflare Secondary DNS (TSIG) API
  slug: cloudflare-secondary-dns-tsig-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Secrets Store API from Cloudflare — 6 operation(s) for secrets store.
  name: Cloudflare Secrets Store API
  slug: cloudflare-secrets-store-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Security Center Audit Log API from Cloudflare — 4 operation(s) for security center audit log.
  name: Cloudflare Security Center Audit Log API
  slug: cloudflare-security-center-audit-log-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Security Center Insights API from Cloudflare — 22 operation(s) for security center insights.
  name: Cloudflare Security Center Insights API
  slug: cloudflare-security-center-insights-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Security Center Partners API from Cloudflare — 4 operation(s) for security center partners.
  name: Cloudflare Security Center Partners API
  slug: cloudflare-security-center-partners-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Security Center Scans API from Cloudflare — 2 operation(s) for security center scans.
  name: Cloudflare Security Center Scans API
  slug: cloudflare-security-center-scans-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The security.txt API from Cloudflare — 1 operation(s) for security.txt.
  name: Cloudflare Security.txt API
  slug: cloudflare-security-txt-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Sessions API from Cloudflare — 8 operation(s) for sessions.
  name: Cloudflare Sessions API
  slug: cloudflare-sessions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Settings API from Cloudflare — 1 operation(s) for settings.
  name: Cloudflare Settings API
  slug: cloudflare-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Shared API from Cloudflare — 2 operation(s) for shared.
  name: Cloudflare Shared API
  slug: cloudflare-shared-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Sinkhole Config API from Cloudflare — 5 operation(s) for sinkhole config.
  name: Cloudflare Sinkhole Config API
  slug: cloudflare-sinkhole-config-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Slots API from Cloudflare — 2 operation(s) for slots.
  name: Cloudflare Slots API
  slug: cloudflare-slots-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Smart Shield Settings API from Cloudflare — 1 operation(s) for smart shield settings.
  name: Cloudflare Smart Shield Settings API
  slug: cloudflare-smart-shield-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Smart Tiered Cache API from Cloudflare — 1 operation(s) for smart tiered cache.
  name: Cloudflare Smart Tiered Cache API
  slug: cloudflare-smart-tiered-cache-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Spectrum Analytics API from Cloudflare — 4 operation(s) for spectrum analytics.
  name: Cloudflare Spectrum Analytics API
  slug: cloudflare-spectrum-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Spectrum Applications API from Cloudflare — 3 operation(s) for spectrum applications.
  name: Cloudflare Spectrum Applications API
  slug: cloudflare-spectrum-applications-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The SSL/TLS Mode Recommendation API from Cloudflare — 1 operation(s) for ssl/tls mode recommendation.
  name: Cloudflare SSL/TLS Mode Recommendation API
  slug: cloudflare-ssl-tls-mode-recommendation-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The SSL Verification API from Cloudflare — 2 operation(s) for ssl verification.
  name: Cloudflare SSL Verification API
  slug: cloudflare-ssl-verification-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The SSO API from Cloudflare — 3 operation(s) for sso.
  name: Cloudflare SSO API
  slug: cloudflare-sso-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream Audio Tracks API from Cloudflare — 3 operation(s) for stream audio tracks.
  name: Cloudflare Stream Audio Tracks API
  slug: cloudflare-stream-audio-tracks-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream Live Inputs API from Cloudflare — 7 operation(s) for stream live inputs.
  name: Cloudflare Stream Live Inputs API
  slug: cloudflare-stream-live-inputs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream MP4 Downloads API from Cloudflare — 2 operation(s) for stream mp4 downloads.
  name: Cloudflare Stream MP4 Downloads API
  slug: cloudflare-stream-mp4-downloads-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream Signing Keys API from Cloudflare — 2 operation(s) for stream signing keys.
  name: Cloudflare Stream Signing Keys API
  slug: cloudflare-stream-signing-keys-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream Subtitles/Captions API from Cloudflare — 4 operation(s) for stream subtitles/captions.
  name: Cloudflare Stream Subtitles/Captions API
  slug: cloudflare-stream-subtitles-captions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream Video Clipping API from Cloudflare — 1 operation(s) for stream video clipping.
  name: Cloudflare Stream Video Clipping API
  slug: cloudflare-stream-video-clipping-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream Videos API from Cloudflare — 7 operation(s) for stream videos.
  name: Cloudflare Stream Videos API
  slug: cloudflare-stream-videos-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream Watermark Profile API from Cloudflare — 2 operation(s) for stream watermark profile.
  name: Cloudflare Stream Watermark Profile API
  slug: cloudflare-stream-watermark-profile-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Stream Webhook API from Cloudflare — 1 operation(s) for stream webhook.
  name: Cloudflare Stream Webhook API
  slug: cloudflare-stream-webhook-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Table Maintenance Configuration API from Cloudflare — 6 operation(s) for table maintenance configuration.
  name: Cloudflare Table Maintenance Configuration API
  slug: cloudflare-table-maintenance-configuration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Table Management API from Cloudflare — 4 operation(s) for table management.
  name: Cloudflare Table Management API
  slug: cloudflare-table-management-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Tag API from Cloudflare — 8 operation(s) for tag.
  name: Cloudflare Tag API
  slug: cloudflare-tag-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The TagCategory API from Cloudflare — 4 operation(s) for tagcategory.
  name: Cloudflare Tag Category API
  slug: cloudflare-tagcategory-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Target Environments API from Cloudflare — 2 operation(s) for target environments.
  name: Cloudflare Target Environments API
  slug: cloudflare-target-environments-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Target Industry API from Cloudflare — 3 operation(s) for target industry.
  name: Cloudflare Target Industry API
  slug: cloudflare-target-industry-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Tenant-Level Custom Nameservers API from Cloudflare — 2 operation(s) for tenant-level custom nameservers.
  name: Cloudflare Tenant-Level Custom Nameservers API
  slug: cloudflare-tenant-level-custom-nameservers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Tenants API from Cloudflare — 5 operation(s) for tenants.
  name: Cloudflare Tenants API
  slug: cloudflare-tenants-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Threat Signals API from Cloudflare — 22 operation(s) for threat signals.
  name: Cloudflare Threat Signals API
  slug: cloudflare-threat-signals-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Tiered Caching API from Cloudflare — 1 operation(s) for tiered caching.
  name: Cloudflare Tiered Caching API
  slug: cloudflare-tiered-caching-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Token Validation Token Configuration API from Cloudflare — 3 operation(s) for token validation token configuration.
  name: Cloudflare Token Validation Token Configuration API
  slug: cloudflare-token-validation-token-configuration-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Token Validation Token Rules API from Cloudflare — 4 operation(s) for token validation token rules.
  name: Cloudflare Token Validation Token Rules API
  slug: cloudflare-token-validation-token-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Total TLS API from Cloudflare — 1 operation(s) for total tls.
  name: Cloudflare Total TLS API
  slug: cloudflare-total-tls-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Triggers API from Cloudflare — 4 operation(s) for triggers.
  name: Cloudflare Triggers API
  slug: cloudflare-triggers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The tseng-abuse-complaint-processor_other API from Cloudflare — 9 operation(s) for tseng-abuse-complaint-processor_other.
  name: Cloudflare Tseng Abuse Complaint Processor Other API
  slug: cloudflare-tseng-abuse-complaint-processor-other-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Tunnel Routing API from Cloudflare — 4 operation(s) for tunnel routing.
  name: Cloudflare Tunnel Routing API
  slug: cloudflare-tunnel-routing-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Tunnel Virtual Network API from Cloudflare — 2 operation(s) for tunnel virtual network.
  name: Cloudflare Tunnel Virtual Network API
  slug: cloudflare-tunnel-virtual-network-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Turnstile API from Cloudflare — 3 operation(s) for turnstile.
  name: Cloudflare Turnstile API
  slug: cloudflare-turnstile-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Universal SSL Settings for a Zone API from Cloudflare — 1 operation(s) for universal ssl settings for a zone.
  name: Cloudflare Universal SSL Settings for a Zone API
  slug: cloudflare-universal-ssl-settings-for-a-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The URL Intelligence API from Cloudflare — 1 operation(s) for url intelligence.
  name: Cloudflare URL Intelligence API
  slug: cloudflare-url-intelligence-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The URL Normalization API from Cloudflare — 1 operation(s) for url normalization.
  name: Cloudflare URL Normalization API
  slug: cloudflare-url-normalization-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The URL Scanner API from Cloudflare — 8 operation(s) for url scanner.
  name: Cloudflare URL Scanner API
  slug: cloudflare-url-scanner-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The URL Scanner (Deprecated) API from Cloudflare — 5 operation(s) for url scanner (deprecated).
  name: Cloudflare URL Scanner (Deprecated) API
  slug: cloudflare-url-scanner-deprecated-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Usage Analytics API from Cloudflare — 5 operation(s) for usage analytics.
  name: Cloudflare Usage Analytics API
  slug: cloudflare-usage-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Usage API from Cloudflare — 1 operation(s) for usage.
  name: Cloudflare Usage API
  slug: cloudflare-usage-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User Agent Blocking rules API from Cloudflare — 2 operation(s) for user agent blocking rules.
  name: Cloudflare User Agent Blocking rules API
  slug: cloudflare-user-agent-blocking-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User Analytics (Deprecated) API from Cloudflare — 1 operation(s) for user analytics (deprecated).
  name: Cloudflare User Analytics (Deprecated) API
  slug: cloudflare-user-analytics-deprecated-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User API Tokens API from Cloudflare — 5 operation(s) for user api tokens.
  name: Cloudflare User API Tokens API
  slug: cloudflare-user-api-tokens-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User Billing History API from Cloudflare — 1 operation(s) for user billing history.
  name: Cloudflare User Billing History API
  slug: cloudflare-user-billing-history-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User Billing Profile API from Cloudflare — 1 operation(s) for user billing profile.
  name: Cloudflare User Billing Profile API
  slug: cloudflare-user-billing-profile-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User's Account Memberships API from Cloudflare — 3 operation(s) for user's account memberships.
  name: Cloudflare User's Account Memberships API
  slug: cloudflare-user-s-account-memberships-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User's Invites API from Cloudflare — 2 operation(s) for user's invites.
  name: Cloudflare User's Invites API
  slug: cloudflare-user-s-invites-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User's Organizations API from Cloudflare — 2 operation(s) for user's organizations.
  name: Cloudflare User's Organizations API
  slug: cloudflare-user-s-organizations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The User Subscription API from Cloudflare — 2 operation(s) for user subscription.
  name: Cloudflare User Subscription API
  slug: cloudflare-user-subscription-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Values API from Cloudflare — 1 operation(s) for values.
  name: Cloudflare Values API
  slug: cloudflare-values-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Vectorize API from Cloudflare — 12 operation(s) for vectorize.
  name: Cloudflare Vectorize API
  slug: cloudflare-vectorize-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Vectorize Beta (Deprecated) API from Cloudflare — 7 operation(s) for vectorize beta (deprecated).
  name: Cloudflare Vectorize Beta (Deprecated) API
  slug: cloudflare-vectorize-beta-deprecated-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Vulnerability Discovery API from Cloudflare — 6 operation(s) for vulnerability discovery.
  name: Cloudflare Vulnerability Discovery API
  slug: cloudflare-vulnerability-discovery-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The WAF overrides API from Cloudflare — 2 operation(s) for waf overrides.
  name: Cloudflare WAF overrides API
  slug: cloudflare-waf-overrides-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The WAF packages API from Cloudflare — 2 operation(s) for waf packages.
  name: Cloudflare WAF packages API
  slug: cloudflare-waf-packages-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The WAF rule groups API from Cloudflare — 2 operation(s) for waf rule groups.
  name: Cloudflare WAF rule groups API
  slug: cloudflare-waf-rule-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The WAF rules API from Cloudflare — 2 operation(s) for waf rules.
  name: Cloudflare WAF rules API
  slug: cloudflare-waf-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Waiting Room API from Cloudflare — 11 operation(s) for waiting room.
  name: Cloudflare Waiting Room API
  slug: cloudflare-waiting-room-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The WARP Change Events API from Cloudflare — 1 operation(s) for warp change events.
  name: Cloudflare WARP Change Events API
  slug: cloudflare-warp-change-events-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The warp-teams-device-api_other API from Cloudflare — 1 operation(s) for warp-teams-device-api_other.
  name: Cloudflare Warp Teams Device API Other API
  slug: cloudflare-warp-teams-device-api-other-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Web Analytics API from Cloudflare — 10 operation(s) for web analytics.
  name: Cloudflare Web Analytics API
  slug: cloudflare-web-analytics-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Web3 Hostname API from Cloudflare — 5 operation(s) for web3 hostname.
  name: Cloudflare Web3 Hostname API
  slug: cloudflare-web3-hostname-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The WHOIS Record API from Cloudflare — 1 operation(s) for whois record.
  name: Cloudflare WHOIS Record API
  slug: cloudflare-whois-record-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Worker Cron Trigger API from Cloudflare — 1 operation(s) for worker cron trigger.
  name: Cloudflare Worker Cron Trigger API
  slug: cloudflare-worker-cron-trigger-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Worker Deployments API from Cloudflare — 2 operation(s) for worker deployments.
  name: Cloudflare Worker Deployments API
  slug: cloudflare-worker-deployments-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Worker Environment API from Cloudflare — 2 operation(s) for worker environment.
  name: Cloudflare Worker Environment API
  slug: cloudflare-worker-environment-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Worker Routes API from Cloudflare — 2 operation(s) for worker routes.
  name: Cloudflare Worker Routes API
  slug: cloudflare-worker-routes-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Worker Script API from Cloudflare — 14 operation(s) for worker script.
  name: Cloudflare Worker Script API
  slug: cloudflare-worker-script-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Worker Subdomain API from Cloudflare — 1 operation(s) for worker subdomain.
  name: Cloudflare Worker Subdomain API
  slug: cloudflare-worker-subdomain-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Worker Tail Logs API from Cloudflare — 2 operation(s) for worker tail logs.
  name: Cloudflare Worker Tail Logs API
  slug: cloudflare-worker-tail-logs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Worker Versions API from Cloudflare — 2 operation(s) for worker versions.
  name: Cloudflare Worker Versions API
  slug: cloudflare-worker-versions-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Workers Account Settings API from Cloudflare — 1 operation(s) for workers account settings.
  name: Cloudflare Workers Account Settings API
  slug: cloudflare-workers-account-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Workers AI API from Cloudflare — 8 operation(s) for workers ai.
  name: Cloudflare Workers AI API
  slug: cloudflare-workers-ai-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Workers AI Finetune API from Cloudflare — 4 operation(s) for workers ai finetune.
  name: Cloudflare Workers AI Finetune API
  slug: cloudflare-workers-ai-finetune-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Workers for Platforms API from Cloudflare — 13 operation(s) for workers for platforms.
  name: Cloudflare Workers for Platforms API
  slug: cloudflare-workers-for-platforms-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The workers_k2_other API from Cloudflare — 3 operation(s) for workers_k2_other.
  name: Cloudflare Workers K2 Other API
  slug: cloudflare-workers-k2-other-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Workers KV Namespace API from Cloudflare — 8 operation(s) for workers kv namespace.
  name: Cloudflare Workers KV Namespace API
  slug: cloudflare-workers-kv-namespace-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The workers_pipelines_other API from Cloudflare — 9 operation(s) for workers_pipelines_other.
  name: Cloudflare Workers Pipelines Other API
  slug: cloudflare-workers-pipelines-other-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Workers Smart Placement API from Cloudflare — 1 operation(s) for workers smart placement.
  name: Cloudflare Workers Smart Placement API
  slug: cloudflare-workers-smart-placement-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Workflows API from Cloudflare — 19 operation(s) for workflows.
  name: Cloudflare Workflows API
  slug: cloudflare-workflows-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zaraz API from Cloudflare — 7 operation(s) for zaraz.
  name: Cloudflare Zaraz API
  slug: cloudflare-zaraz-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust accounts API from Cloudflare — 6 operation(s) for zero trust accounts.
  name: Cloudflare Zero Trust accounts API
  slug: cloudflare-zero-trust-accounts-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust applications review status API from Cloudflare — 1 operation(s) for zero trust applications review status.
  name: Cloudflare Zero Trust applications review status API
  slug: cloudflare-zero-trust-applications-review-status-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust certificates API from Cloudflare — 4 operation(s) for zero trust certificates.
  name: Cloudflare Zero Trust certificates API
  slug: cloudflare-zero-trust-certificates-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Connectivity Settings API from Cloudflare — 1 operation(s) for zero trust connectivity settings.
  name: Cloudflare Zero Trust Connectivity Settings API
  slug: cloudflare-zero-trust-connectivity-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Gateway application and application type mappings API from Cloudflare — 1 operation(s) for zero trust gateway application and application type mappings.
  name: Cloudflare Zero Trust Gateway application and application type mappings API
  slug: cloudflare-zero-trust-gateway-application-and-application-type-mappings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Gateway categories API from Cloudflare — 1 operation(s) for zero trust gateway categories.
  name: Cloudflare Zero Trust Gateway categories API
  slug: cloudflare-zero-trust-gateway-categories-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Gateway DNS destination IPv4 address pairs API from Cloudflare — 1 operation(s) for zero trust gateway dns destination ipv4 address pairs.
  name: Cloudflare Zero Trust Gateway DNS destination IPv4 address pairs API
  slug: cloudflare-zero-trust-gateway-dns-destination-ipv4-address-pairs-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Gateway locations API from Cloudflare — 2 operation(s) for zero trust gateway locations.
  name: Cloudflare Zero Trust Gateway locations API
  slug: cloudflare-zero-trust-gateway-locations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Gateway operations API from Cloudflare — 2 operation(s) for zero trust gateway operations.
  name: Cloudflare Zero Trust Gateway operations API
  slug: cloudflare-zero-trust-gateway-operations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Gateway PAC files API from Cloudflare — 2 operation(s) for zero trust gateway pac files.
  name: Cloudflare Zero Trust Gateway PAC files API
  slug: cloudflare-zero-trust-gateway-pac-files-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Gateway proxy endpoints API from Cloudflare — 2 operation(s) for zero trust gateway proxy endpoints.
  name: Cloudflare Zero Trust Gateway proxy endpoints API
  slug: cloudflare-zero-trust-gateway-proxy-endpoints-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Gateway rules API from Cloudflare — 4 operation(s) for zero trust gateway rules.
  name: Cloudflare Zero Trust Gateway rules API
  slug: cloudflare-zero-trust-gateway-rules-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Hostname Route API from Cloudflare — 2 operation(s) for zero trust hostname route.
  name: Cloudflare Zero Trust Hostname Route API
  slug: cloudflare-zero-trust-hostname-route-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust lists API from Cloudflare — 4 operation(s) for zero trust lists.
  name: Cloudflare Zero Trust lists API
  slug: cloudflare-zero-trust-lists-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust organization API from Cloudflare — 3 operation(s) for zero trust organization.
  name: Cloudflare Zero Trust organization API
  slug: cloudflare-zero-trust-organization-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Risk Scoring API from Cloudflare — 4 operation(s) for zero trust risk scoring.
  name: Cloudflare Zero Trust Risk Scoring API
  slug: cloudflare-zero-trust-risk-scoring-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Risk Scoring Integrations API from Cloudflare — 3 operation(s) for zero trust risk scoring integrations.
  name: Cloudflare Zero Trust Risk Scoring Integrations API
  slug: cloudflare-zero-trust-risk-scoring-integrations-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust seats API from Cloudflare — 1 operation(s) for zero trust seats.
  name: Cloudflare Zero Trust seats API
  slug: cloudflare-zero-trust-seats-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust SSH Settings API from Cloudflare — 2 operation(s) for zero trust ssh settings.
  name: Cloudflare Zero Trust SSH Settings API
  slug: cloudflare-zero-trust-ssh-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust Subnets API from Cloudflare — 5 operation(s) for zero trust subnets.
  name: Cloudflare Zero Trust Subnets API
  slug: cloudflare-zero-trust-subnets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zero Trust users API from Cloudflare — 8 operation(s) for zero trust users.
  name: Cloudflare Zero Trust users API
  slug: cloudflare-zero-trust-users-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Analytics (Deprecated) API from Cloudflare — 2 operation(s) for zone analytics (deprecated).
  name: Cloudflare Zone Analytics (Deprecated) API
  slug: cloudflare-zone-analytics-deprecated-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone API from Cloudflare — 7 operation(s) for zone.
  name: Cloudflare Zone API
  slug: cloudflare-zone-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Cache Settings API from Cloudflare — 4 operation(s) for zone cache settings.
  name: Cloudflare Zone Cache Settings API
  slug: cloudflare-zone-cache-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Cloud Connector Rules GET API from Cloudflare — 1 operation(s) for zone cloud connector rules get.
  name: Cloudflare Zone Cloud Connector Rules GET API
  slug: cloudflare-zone-cloud-connector-rules-get-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Cloud Connector Rules PUT API from Cloudflare — 1 operation(s) for zone cloud connector rules put.
  name: Cloudflare Zone Cloud Connector Rules PUT API
  slug: cloudflare-zone-cloud-connector-rules-put-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Entitlements API from Cloudflare — 1 operation(s) for zone entitlements.
  name: Cloudflare Zone Entitlements API
  slug: cloudflare-zone-entitlements-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Environments API from Cloudflare — 3 operation(s) for zone environments.
  name: Cloudflare Zone Environments API
  slug: cloudflare-zone-environments-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Holds API from Cloudflare — 2 operation(s) for zone holds.
  name: Cloudflare Zone Holds API
  slug: cloudflare-zone-holds-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Access applications API from Cloudflare — 5 operation(s) for zone-level access applications.
  name: Cloudflare Zone-Level Access applications API
  slug: cloudflare-zone-level-access-applications-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Access groups API from Cloudflare — 2 operation(s) for zone-level access groups.
  name: Cloudflare Zone-Level Access groups API
  slug: cloudflare-zone-level-access-groups-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Access identity providers API from Cloudflare — 2 operation(s) for zone-level access identity providers.
  name: Cloudflare Zone-Level Access identity providers API
  slug: cloudflare-zone-level-access-identity-providers-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Access mTLS authentication API from Cloudflare — 3 operation(s) for zone-level access mtls authentication.
  name: Cloudflare Zone-Level Access mTLS authentication API
  slug: cloudflare-zone-level-access-mtls-authentication-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Access policies API from Cloudflare — 2 operation(s) for zone-level access policies.
  name: Cloudflare Zone-Level Access policies API
  slug: cloudflare-zone-level-access-policies-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Access service tokens API from Cloudflare — 2 operation(s) for zone-level access service tokens.
  name: Cloudflare Zone-Level Access service tokens API
  slug: cloudflare-zone-level-access-service-tokens-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Access short-lived certificate CAs API from Cloudflare — 2 operation(s) for zone-level access short-lived certificate cas.
  name: Cloudflare Zone-Level Access short-lived certificate CAs API
  slug: cloudflare-zone-level-access-short-lived-certificate-cas-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Authenticated Origin Pulls API from Cloudflare — 3 operation(s) for zone-level authenticated origin pulls.
  name: Cloudflare Zone-Level Authenticated Origin Pulls API
  slug: cloudflare-zone-level-authenticated-origin-pulls-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone-Level Zero Trust organization API from Cloudflare — 2 operation(s) for zone-level zero trust organization.
  name: Cloudflare Zone-Level Zero Trust organization API
  slug: cloudflare-zone-level-zero-trust-organization-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Lockdown API from Cloudflare — 2 operation(s) for zone lockdown.
  name: Cloudflare Zone Lockdown API
  slug: cloudflare-zone-lockdown-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Rate Plan API from Cloudflare — 3 operation(s) for zone rate plan.
  name: Cloudflare Zone Rate Plan API
  slug: cloudflare-zone-rate-plan-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Rulesets API from Cloudflare — 10 operation(s) for zone rulesets.
  name: Cloudflare Zone Rulesets API
  slug: cloudflare-zone-rulesets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Settings API from Cloudflare — 14 operation(s) for zone settings.
  name: Cloudflare Zone Settings API
  slug: cloudflare-zone-settings-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Snippets API from Cloudflare — 4 operation(s) for zone snippets.
  name: Cloudflare Zone Snippets API
  slug: cloudflare-zone-snippets-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Zone Subscription API from Cloudflare — 2 operation(s) for zone subscription.
  name: Cloudflare Zone Subscription API
  slug: cloudflare-zone-subscription-api
- baseURL: https://api.cloudflare.com
  baseurl_source: declared
  description: The Organization Members API from Cloudflare — 3 operation(s) for organization members.
  name: Cloudflare Organization Members API
  slug: cloudflare-organization-members-api
arazzos:
- description: Create a zone IP access rule, list the rules, then remove it.
  name: Cloudflare Block IP Access Rule
  slug: cloudflare-block-ip-access-rule-workflow
- description: Read the current SSL mode, change it, then read it back to confirm.
  name: Cloudflare Configure SSL Mode
  slug: cloudflare-configure-ssl-mode-workflow
- description: Create a zone, trigger an activation check, and poll its status.
  name: Cloudflare Create and Activate Zone
  slug: cloudflare-create-and-activate-zone-workflow
- description: Create a DNS record in a zone and read it back to confirm it was stored.
  name: Cloudflare Create DNS Record and Verify
  slug: cloudflare-create-dns-record-and-verify-workflow
- description: Create a filter expression, attach a firewall rule to it, then list the rules.
  name: Cloudflare Create Firewall Rule
  slug: cloudflare-create-firewall-rule-workflow
- description: Create a zone load balancer over existing pools and read it back.
  name: Cloudflare Create Load Balancer
  slug: cloudflare-create-load-balancer-workflow
- description: Create a page rule for a URL pattern and read it back to confirm it.
  name: Cloudflare Create Page Rule
  slug: cloudflare-create-page-rule-workflow
- description: Create a custom zone ruleset, append a rule, then read it back.
  name: Cloudflare Create Ruleset with Rule
  slug: cloudflare-create-ruleset-with-rule-workflow
- description: Create a URI-based WAF override, read it back, then list the overrides.
  name: Cloudflare Create WAF Override
  slug: cloudflare-create-waf-override-workflow
- description: Create a Worker, bind a zone route to it, then list the zone routes.
  name: Cloudflare Deploy Worker Route
  slug: cloudflare-deploy-worker-route-workflow
- description: Toggle Universal SSL for a zone, read the setting, then check verification.
  name: Cloudflare Enable Universal SSL
  slug: cloudflare-enable-universal-ssl-workflow
- description: Create a zone, add a root DNS record, then read the zone details back.
  name: Cloudflare Provision Zone with DNS
  slug: cloudflare-provision-zone-with-dns-workflow
- description: Confirm a zone is active, then purge its cache by files or entirely.
  name: Cloudflare Purge Cache
  slug: cloudflare-purge-cache-workflow
- description: Create a page rule, fully replace its configuration, then read it back.
  name: Cloudflare Replace Page Rule
  slug: cloudflare-replace-page-rule-workflow
- description: Create a DNS record, update its content, then delete it.
  name: Cloudflare Rotate DNS Record
  slug: cloudflare-rotate-dns-record-workflow
- description: Create a load balancer, update its pools, then delete it.
  name: Cloudflare Rotate Load Balancer
  slug: cloudflare-rotate-load-balancer-workflow
- description: Create a page rule, edit its action, then delete it.
  name: Cloudflare Rotate Page Rule
  slug: cloudflare-rotate-page-rule-workflow
- description: Create a Worker route, update its pattern, then delete it.
  name: Cloudflare Rotate Worker Route
  slug: cloudflare-rotate-worker-route-workflow
- description: Create a Worker, read it back, then delete it.
  name: Cloudflare Rotate Worker
  slug: cloudflare-rotate-worker-workflow
- description: Read the zone WAF setting, change it, then read it back to confirm.
  name: Cloudflare Toggle WAF Setting
  slug: cloudflare-toggle-waf-setting-workflow
- description: Read a phase entrypoint ruleset, then replace its rules in one update.
  name: Cloudflare Update Entrypoint Ruleset
  slug: cloudflare-update-entrypoint-ruleset-workflow
- description: Upload a custom SSL certificate, read it back, then remove it.
  name: Cloudflare Upload Custom SSL Certificate
  slug: cloudflare-upload-custom-ssl-certificate-workflow
- description: Find a DNS record by name and update it if present, otherwise create it.
  name: Cloudflare Upsert DNS Record
  slug: cloudflare-upsert-dns-record-workflow
artifact_total: 1165
asyncapis:
- description: Cloudflare Notifications sends webhook events to configured endpoints when various alerts fire across your account. Webhooks deliver JSON payloads for events including DDoS attacks, SSL certificate ex
  name: Cloudflare Notifications Webhooks
  slug: cloudflare-notifications-webhooks-asyncapi
- description: Cloudflare Stream sends webhook notifications when videos finish processing and are ready to stream, or when a video enters an error state. Webhooks can also be configured for live streaming events. C
  name: Cloudflare Stream Webhooks
  slug: cloudflare-stream-webhooks-asyncapi
collections:
- collection_type: postman
  name: Cloudflare accounts/
  slug: postman-cloudflare-accounts--openapi-original
- collection_type: postman
  name: Cloudflare AI Gateway API
  slug: postman-cloudflare-ai-gateway
- collection_type: postman
  name: Cloudflare certificates/
  slug: postman-cloudflare-certificates--openapi-original
- collection_type: postman
  name: Cloudflare D1 API
  slug: postman-cloudflare-d1
- collection_type: postman
  name: Cloudflare DNS API
  slug: postman-cloudflare-dns
- collection_type: postman
  name: Cloudflare Durable Objects API
  slug: postman-cloudflare-durable-objects
- collection_type: postman
  name: Cloudflare Hyperdrive API
  slug: postman-cloudflare-hyperdrive
- collection_type: postman
  name: Cloudflare Images API
  slug: postman-cloudflare-images
- collection_type: postman
  name: Cloudflare ips/
  slug: postman-cloudflare-ips--openapi-original
- collection_type: postman
  name: Cloudflare KV API
  slug: postman-cloudflare-kv
- collection_type: postman
  name: Cloudflare Logpush API
  slug: postman-cloudflare-logpush
- collection_type: postman
  name: Cloudflare memberships/
  slug: postman-cloudflare-memberships--openapi-original
- collection_type: postman
  name: Cloudflare API
  slug: postman-cloudflare-openapi-original
- collection_type: postman
  name: Cloudflare Pages API
  slug: postman-cloudflare-pages
- collection_type: postman
  name: Cloudflare Queues API
  slug: postman-cloudflare-queues
- collection_type: postman
  name: Cloudflare R2 API
  slug: postman-cloudflare-r2
- collection_type: postman
  name: Cloudflare radar/
  slug: postman-cloudflare-radar--openapi-original
- collection_type: postman
  name: Cloudflare Stream API
  slug: postman-cloudflare-stream
- collection_type: postman
  name: Cloudflare Turnstile API
  slug: postman-cloudflare-turnstile
- collection_type: postman
  name: Cloudflare user/
  slug: postman-cloudflare-user--openapi-original
- collection_type: postman
  name: Cloudflare Vectorize API
  slug: postman-cloudflare-vectorize
- collection_type: postman
  name: Cloudflare Workers AI API
  slug: postman-cloudflare-workers-ai
- collection_type: postman
  name: Cloudflare Workers API
  slug: postman-cloudflare-workers
- collection_type: postman
  name: Cloudflare zones/
  slug: postman-cloudflare-zones--openapi-original
- collection_type: open
  name: Cloudflare / Accounts API
  slug: open-cloudflare-accounts-api
- collection_type: open
  name: Cloudflare AI Gateway API
  slug: open-cloudflare-ai-gateway
- collection_type: open
  name: Cloudflare / Accounts AI Inference API
  slug: open-cloudflare-ai-inference-api
- collection_type: open
  name: Cloudflare / Accounts Buckets API
  slug: open-cloudflare-buckets-api
- collection_type: open
  name: Cloudflare / Accounts Bulk Operations API
  slug: open-cloudflare-bulk-operations-api
- collection_type: open
  name: Cloudflare / Accounts Certificates API
  slug: open-cloudflare-certificates-api
- collection_type: open
  name: Cloudflare / Accounts Configuration API
  slug: open-cloudflare-configuration-api
- collection_type: open
  name: Cloudflare / Accounts Configurations API
  slug: open-cloudflare-configurations-api
- collection_type: open
  name: Cloudflare / Accounts Consumers API
  slug: open-cloudflare-consumers-api
- collection_type: open
  name: Cloudflare D1 API
  slug: open-cloudflare-d1
- collection_type: open
  name: Cloudflare / Accounts Databases API
  slug: open-cloudflare-databases-api
- collection_type: open
  name: Cloudflare / Accounts Datasets API
  slug: open-cloudflare-datasets-api
- collection_type: open
  name: Cloudflare / Accounts Deployments API
  slug: open-cloudflare-deployments-api
- collection_type: open
  name: Cloudflare / Accounts Direct Uploads API
  slug: open-cloudflare-direct-uploads-api
- collection_type: open
  name: Cloudflare / Accounts DNS Analytics API
  slug: open-cloudflare-dns-analytics-api
- collection_type: open
  name: Cloudflare / Accounts DNS Batch Operations API
  slug: open-cloudflare-dns-batch-operations-api
- collection_type: open
  name: Cloudflare / Accounts DNS Record Import/Export API
  slug: open-cloudflare-dns-record-import-export-api
- collection_type: open
  name: Cloudflare / Accounts DNS Record Scanning API
  slug: open-cloudflare-dns-record-scanning-api
- collection_type: open
  name: Cloudflare / Accounts DNS Records API
  slug: open-cloudflare-dns-records-api
- collection_type: open
  name: Cloudflare DNS API
  slug: open-cloudflare-dns
- collection_type: open
  name: Cloudflare / Accounts DNSSEC API
  slug: open-cloudflare-dnssec-api
- collection_type: open
  name: Cloudflare / Accounts Domains API
  slug: open-cloudflare-domains-api
- collection_type: open
  name: Cloudflare Durable Objects API
  slug: open-cloudflare-durable-objects
- collection_type: open
  name: Cloudflare / Accounts Gateways API
  slug: open-cloudflare-gateways-api
- collection_type: open
  name: Cloudflare Hyperdrive API
  slug: open-cloudflare-hyperdrive
- collection_type: open
  name: Cloudflare / Accounts Images API
  slug: open-cloudflare-images-api
- collection_type: open
  name: Cloudflare Images API
  slug: open-cloudflare-images
- collection_type: open
  name: Cloudflare / Accounts Import/Export API
  slug: open-cloudflare-import-export-api
- collection_type: open
  name: Cloudflare / Accounts Indexes API
  slug: open-cloudflare-indexes-api
- collection_type: open
  name: Cloudflare / Accounts Ips API
  slug: open-cloudflare-ips-api
- collection_type: open
  name: Cloudflare / Accounts Key-Value Pairs API
  slug: open-cloudflare-key-value-pairs-api
- collection_type: open
  name: Cloudflare / Accounts Keys API
  slug: open-cloudflare-keys-api
- collection_type: open
  name: Cloudflare KV API
  slug: open-cloudflare-kv
- collection_type: open
  name: Cloudflare / Accounts Live Inputs API
  slug: open-cloudflare-live-inputs-api
- collection_type: open
  name: Cloudflare / Accounts Logpush Jobs API
  slug: open-cloudflare-logpush-jobs-api
- collection_type: open
  name: Cloudflare Logpush API
  slug: open-cloudflare-logpush
- collection_type: open
  name: Cloudflare / Accounts Logs API
  slug: open-cloudflare-logs-api
- collection_type: open
  name: Cloudflare / Accounts Memberships API
  slug: open-cloudflare-memberships-api
- collection_type: open
  name: Cloudflare / Accounts Messages API
  slug: open-cloudflare-messages-api
- collection_type: open
  name: Cloudflare / Accounts Metadata API
  slug: open-cloudflare-metadata-api
- collection_type: open
  name: Cloudflare / Accounts Namespaces API
  slug: open-cloudflare-namespaces-api
- collection_type: open
  name: Cloudflare / Accounts Objects API
  slug: open-cloudflare-objects-api
- collection_type: open
  name: Cloudflare / Accounts OpenAI Compatible API
  slug: open-cloudflare-openai-compatible-api
- collection_type: open
  name: Cloudflare / Accounts Organizations API
  slug: open-cloudflare-organizations-api
- collection_type: open
  name: Cloudflare / Accounts Ownership API
  slug: open-cloudflare-ownership-api
- collection_type: open
  name: Cloudflare Pages API
  slug: open-cloudflare-pages
- collection_type: open
  name: Cloudflare / Accounts Projects API
  slug: open-cloudflare-projects-api
- collection_type: open
  name: Cloudflare / Accounts Purge API
  slug: open-cloudflare-purge-api
- collection_type: open
  name: Cloudflare / Accounts Queries API
  slug: open-cloudflare-queries-api
- collection_type: open
  name: Cloudflare / Accounts Queues API
  slug: open-cloudflare-queues-api
- collection_type: open
  name: Cloudflare Queues API
  slug: open-cloudflare-queues
- collection_type: open
  name: Cloudflare R2 API
  slug: open-cloudflare-r2
- collection_type: open
  name: Cloudflare / Accounts Radar API
  slug: open-cloudflare-radar-api
- collection_type: open
  name: Cloudflare / Accounts Routes API
  slug: open-cloudflare-routes-api
- collection_type: open
  name: Cloudflare / Accounts Scripts API
  slug: open-cloudflare-scripts-api
- collection_type: open
  name: Cloudflare / Accounts Secrets API
  slug: open-cloudflare-secrets-api
- collection_type: open
  name: Cloudflare / Accounts Signing Keys API
  slug: open-cloudflare-signing-keys-api
- collection_type: open
  name: Cloudflare Stream API
  slug: open-cloudflare-stream
- collection_type: open
  name: Cloudflare / Accounts Time Travel API
  slug: open-cloudflare-time-travel-api
- collection_type: open
  name: Cloudflare Turnstile API
  slug: open-cloudflare-turnstile
- collection_type: open
  name: Cloudflare / Accounts User API
  slug: open-cloudflare-user-api
- collection_type: open
  name: Cloudflare / Accounts Variants API
  slug: open-cloudflare-variants-api
- collection_type: open
  name: Cloudflare Vectorize API
  slug: open-cloudflare-vectorize
- collection_type: open
  name: Cloudflare / Accounts Vectors API
  slug: open-cloudflare-vectors-api
- collection_type: open
  name: Cloudflare / Accounts Verification API
  slug: open-cloudflare-verification-api
- collection_type: open
  name: Cloudflare / Accounts Versions API
  slug: open-cloudflare-versions-api
- collection_type: open
  name: Cloudflare / Accounts Videos API
  slug: open-cloudflare-videos-api
- collection_type: open
  name: Cloudflare / Accounts Webhooks API
  slug: open-cloudflare-webhooks-api
- collection_type: open
  name: Cloudflare / Accounts Widgets API
  slug: open-cloudflare-widgets-api
- collection_type: open
  name: Cloudflare Workers AI API
  slug: open-cloudflare-workers-ai
- collection_type: open
  name: Cloudflare / Accounts Workers API
  slug: open-cloudflare-workers-api
- collection_type: open
  name: Cloudflare Workers API
  slug: open-cloudflare-workers
- collection_type: open
  name: Cloudflare / Accounts Zones API
  slug: open-cloudflare-zones-api
common:
- group: commercial
  href: https://artifacts.apis.io/cloudflare/finops/cloudflare-finops.yml
  title: ''
  type: FinOps
  url: finops/cloudflare-finops.yml
- group: operate
  href: https://artifacts.apis.io/cloudflare/rate-limits/cloudflare-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cloudflare-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/rules/cloudflare-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudflare-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/rules/cloudflare-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudflare-rules.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/rules/cloudflare-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudflare-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/rules/cloudflare-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/cloudflare-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-workers-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-workers-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-workers-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-workers-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-vectorize-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-vectorize-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-turnstile-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-turnstile-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-stream-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-stream-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-r2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-r2-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-queues-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-queues-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-pages-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-pages-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-logpush-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-logpush-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-kv-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-kv-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-images-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-images-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-hyperdrive-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-hyperdrive-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-durable-objects-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-durable-objects-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-dns-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-dns-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-d1-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-d1-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-ai-gateway-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-ai-gateway-context.jsonld
- group: design
  href: https://artifacts.apis.io/cloudflare/vocabulary/cloudflare-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cloudflare-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cloudflare/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/asyncapi/cloudflare-stream-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/cloudflare-stream-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/asyncapi/cloudflare-notifications-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/cloudflare-notifications-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/data-model/cloudflare-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cloudflare-data-model.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/conventions/cloudflare-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/cloudflare-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/conventions/cloudflare-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cloudflare-conventions.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/errors/cloudflare-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cloudflare-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/conformance/cloudflare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cloudflare-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cloudflare/llms/cloudflare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cloudflare-llms.txt
- group: agent
  href: https://artifacts.apis.io/cloudflare/well-known/cloudflare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cloudflare-well-known.yml
- group: other
  href: https://artifacts.apis.io/cloudflare/hosts/cloudflare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cloudflare-hosts.yml
- group: other
  href: https://artifacts.apis.io/cloudflare/vendors/cloudflare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cloudflare-vendors.yml
- group: build
  href: https://artifacts.apis.io/cloudflare/packages/cloudflare-packages.yml
  title: ''
  type: Packages
  url: packages/cloudflare-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://dash.cloudflare.com/sign-up
- group: auth
  title: ''
  type: Security
  url: https://blog.cloudflare.com/tag/security/
- group: company
  title: ''
  type: Newsroom
  url: https://www.cloudflare.com/press/
- group: other
  href: https://artifacts.apis.io/cloudflare/vendor-facets/cloudflare-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/cloudflare-vendor-facets.yml
- group: commercial
  href: https://artifacts.apis.io/cloudflare/plans/cloudflare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cloudflare-plans-pricing.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cloudflare.com/api/
- group: other
  title: ''
  type: Canonical
  url: https://github.com/api-evangelist/cloudflare
- group: company
  title: ''
  type: Website
  url: https://www.cloudflare.com/
- group: other
  href: https://artifacts.apis.io/cloudflare/capabilities/cloudflare-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cloudflare-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/cloudflare/a2a/cloudflare-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cloudflare-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cloudflare/agentic-access/cloudflare-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudflare-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cloudflare/security/cloudflare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cloudflare-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cloudflare/security/cloudflare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudflare-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cloudflare/authentication/cloudflare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cloudflare-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/cloudflare/skills
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cloudflare/overview
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-block-ip-access-rule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-block-ip-access-rule-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-configure-ssl-mode-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-configure-ssl-mode-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-create-and-activate-zone-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-create-and-activate-zone-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-create-dns-record-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-create-dns-record-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-create-firewall-rule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-create-firewall-rule-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-create-load-balancer-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-create-load-balancer-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-create-page-rule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-create-page-rule-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-create-ruleset-with-rule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-create-ruleset-with-rule-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-create-waf-override-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-create-waf-override-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-deploy-worker-route-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-deploy-worker-route-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-enable-universal-ssl-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-enable-universal-ssl-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-provision-zone-with-dns-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-provision-zone-with-dns-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-purge-cache-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-purge-cache-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-replace-page-rule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-replace-page-rule-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-rotate-dns-record-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-rotate-dns-record-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-rotate-load-balancer-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-rotate-load-balancer-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-rotate-page-rule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-rotate-page-rule-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-rotate-worker-route-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-rotate-worker-route-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-rotate-worker-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-rotate-worker-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-toggle-waf-setting-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-toggle-waf-setting-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-update-entrypoint-ruleset-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-update-entrypoint-ruleset-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-upload-custom-ssl-certificate-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-upload-custom-ssl-certificate-workflow.yml
- group: design
  href: https://artifacts.apis.io/cloudflare/arazzo/cloudflare-upsert-dns-record-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/cloudflare-upsert-dns-record-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudflare
- group: design
  href: https://artifacts.apis.io/cloudflare/json-ld/cloudflare-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cloudflare-context.jsonld
- group: docs
  href: https://artifacts.apis.io/cloudflare/json-schema/cloudflare-dns-record-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cloudflare-dns-record-schema.json
- group: docs
  href: https://artifacts.apis.io/cloudflare/json-schema/cloudflare-zone-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cloudflare-zone-schema.json
- group: docs
  href: https://artifacts.apis.io/cloudflare/json-schema/cloudflare-worker-script-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cloudflare-worker-script-schema.json
- group: docs
  href: https://artifacts.apis.io/cloudflare/json-schema/cloudflare-account-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cloudflare-account-schema.json
- group: docs
  href: https://artifacts.apis.io/cloudflare/json-schema/cloudflare-notification-webhook-payload-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cloudflare-notification-webhook-payload-schema.json
- group: docs
  href: https://artifacts.apis.io/cloudflare/json-schema/cloudflare-r2-bucket-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cloudflare-r2-bucket-schema.json
- group: docs
  href: https://artifacts.apis.io/cloudflare/json-schema/cloudflare-d1-database-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/cloudflare-d1-database-schema.json
- group: start
  title: ''
  type: Portal
  url: https://developers.cloudflare.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cloudflare.com/fundamentals/get-started/
- group: company
  title: ''
  type: Blog
  url: https://blog.cloudflare.com/
- group: start
  title: ''
  type: Signup
  url: https://dash.cloudflare.com/sign-up
- group: start
  title: ''
  type: Signup
  url: https://dash.cloudflare.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cloudflare.com/plans/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
- group: build
  title: ''
  type: SDKs
  url: https://developers.cloudflare.com/fundamentals/api/reference/sdks/
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.cloudflare.com/fundamentals/api/reference/limits/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cloudflare.com/changelog/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cloudflarestatus.com/
- group: start
  title: ''
  type: Portal
  url: https://www.cloudflare.com/
- group: start
  title: ''
  type: Console
  url: https://dash.cloudflare.com/
- group: operate
  title: ''
  type: Support
  url: https://support.cloudflare.com/
- group: operate
  title: ''
  type: Support
  url: https://community.cloudflare.com/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/cloudflaredev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloudflare
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloudflare/api-schemas
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cloudflare.com/privacypolicy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloudflare.com/terms/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/directory/
- group: other
  title: ''
  type: X
  url: https://x.com/CloudflareDev
- group: build
  title: ''
  type: SDKs
  url: https://developers.cloudflare.com/terraform/
- group: build
  title: ''
  type: SDKs
  url: https://developers.cloudflare.com/pulumi/
- group: build
  title: ''
  type: CLI
  url: https://developers.cloudflare.com/workers/wrangler/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudflare/cloudflare-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudflare/cloudflare-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudflare/cloudflare-typescript
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/cloudflare
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/cloudflare/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/cloudflare/agents
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/agents
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloudflare/workers-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloudflare/workerd
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloudflare/workers-rs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloudflare/quiche
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloudflare/cloudflared
- group: other
  title: ''
  type: RSS
  url: https://blog.cloudflare.com/rss/
- group: other
  title: ''
  type: RSS
  url: https://developers.cloudflare.com/changelog/rss/index.xml
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://developers.cloudflare.com/learning-paths/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/products/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/cloudflare/mcp-server-cloudflare
- group: agent
  title: ''
  type: MCPServer
  url: https://observability.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://bindings.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://builds.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://radar.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://dns-analytics.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://ai-gateway.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://browser.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://logpush.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://graphql.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://casb.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://containers.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://auditlogs.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://dex.mcp.cloudflare.com/mcp
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.cloudflare.com/llms.txt
created: 2024/04/14
description: Cloudflare is a global network designed to make everything you connect to the Internet secure, private, fast, and reliable.
examples:
- key_count: 11
  name: Cloudflare Ai Gateway Gateway Example
  slug: cloudflare-ai-gateway-gateway-example
- key_count: 7
  name: Cloudflare Ai Gateway Gateway Input Example
  slug: cloudflare-ai-gateway-gateway-input-example
- key_count: 2
  name: Cloudflare Ai Gateway Gateway List Response Example
  slug: cloudflare-ai-gateway-gateway-list-response-example
- key_count: 3
  name: Cloudflare Ai Gateway Gateway Response Example
  slug: cloudflare-ai-gateway-gateway-response-example
- key_count: 6
  name: Cloudflare D1 D1 Database Example
  slug: cloudflare-d1-d1-database-example
- key_count: 3
  name: Cloudflare D1 D1 Database List Response Example
  slug: cloudflare-d1-d1-database-list-response-example
- key_count: 3
  name: Cloudflare D1 D1 Database Response Example
  slug: cloudflare-d1-d1-database-response-example
- key_count: 2
  name: Cloudflare D1 D1 Query Response Example
  slug: cloudflare-d1-d1-query-response-example
- key_count: 13
  name: Cloudflare Dns Dns Record Example
  slug: cloudflare-dns-dns-record-example
- key_count: 7
  name: Cloudflare Dns Dns Record Input Example
  slug: cloudflare-dns-dns-record-input-example
- key_count: 5
  name: Cloudflare Dns Dns Record List Response Example
  slug: cloudflare-dns-dns-record-list-response-example
- key_count: 3
  name: Cloudflare Dns Dns Record Response Example
  slug: cloudflare-dns-dns-record-response-example
- key_count: 0
  name: Cloudflare Dns Record Type Example
  slug: cloudflare-dns-record-type-example
- key_count: 4
  name: Cloudflare Durable Objects Durable Object Namespace Example
  slug: cloudflare-durable-objects-durable-object-namespace-example
- key_count: 4
  name: Cloudflare Durable Objects Namespace List Response Example
  slug: cloudflare-durable-objects-namespace-list-response-example
- key_count: 3
  name: Cloudflare Hyperdrive Config Input Example
  slug: cloudflare-hyperdrive-config-input-example
- key_count: 2
  name: Cloudflare Hyperdrive Config List Response Example
  slug: cloudflare-hyperdrive-config-list-response-example
- key_count: 3
  name: Cloudflare Hyperdrive Config Response Example
  slug: cloudflare-hyperdrive-config-response-example
- key_count: 4
  name: Cloudflare Hyperdrive Hyperdrive Config Example
  slug: cloudflare-hyperdrive-hyperdrive-config-example
- key_count: 6
  name: Cloudflare Images Image Example
  slug: cloudflare-images-image-example
- key_count: 2
  name: Cloudflare Images Image List Response Example
  slug: cloudflare-images-image-list-response-example
- key_count: 3
  name: Cloudflare Images Image Response Example
  slug: cloudflare-images-image-response-example
- key_count: 3
  name: Cloudflare Images Variant Input Example
  slug: cloudflare-images-variant-input-example
- key_count: 2
  name: Cloudflare Kv Bulk Operation Response Example
  slug: cloudflare-kv-bulk-operation-response-example
- key_count: 3
  name: Cloudflare Kv Key List Response Example
  slug: cloudflare-kv-key-list-response-example
- key_count: 3
  name: Cloudflare Kv Namespace Example
  slug: cloudflare-kv-namespace-example
- key_count: 3
  name: Cloudflare Kv Namespace List Response Example
  slug: cloudflare-kv-namespace-list-response-example
- key_count: 3
  name: Cloudflare Kv Namespace Response Example
  slug: cloudflare-kv-namespace-response-example
- key_count: 10
  name: Cloudflare Logpush Logpush Job Example
  slug: cloudflare-logpush-logpush-job-example
- key_count: 8
  name: Cloudflare Logpush Logpush Job Input Example
  slug: cloudflare-logpush-logpush-job-input-example
- key_count: 2
  name: Cloudflare Logpush Logpush Job List Response Example
  slug: cloudflare-logpush-logpush-job-list-response-example
- key_count: 3
  name: Cloudflare Logpush Logpush Job Response Example
  slug: cloudflare-logpush-logpush-job-response-example
- key_count: 5
  name: Cloudflare Pages Deployment Example
  slug: cloudflare-pages-deployment-example
- key_count: 2
  name: Cloudflare Pages Deployment List Response Example
  slug: cloudflare-pages-deployment-list-response-example
- key_count: 7
  name: Cloudflare Pages Project Example
  slug: cloudflare-pages-project-example
- key_count: 3
  name: Cloudflare Pages Project Input Example
  slug: cloudflare-pages-project-input-example
- key_count: 2
  name: Cloudflare Pages Project List Response Example
  slug: cloudflare-pages-project-list-response-example
- key_count: 3
  name: Cloudflare Pages Project Response Example
  slug: cloudflare-pages-project-response-example
- key_count: 2
  name: Cloudflare Queues Consumer Input Example
  slug: cloudflare-queues-consumer-input-example
- key_count: 2
  name: Cloudflare Queues Message Input Example
  slug: cloudflare-queues-message-input-example
- key_count: 6
  name: Cloudflare Queues Queue Example
  slug: cloudflare-queues-queue-example
- key_count: 2
  name: Cloudflare Queues Queue List Response Example
  slug: cloudflare-queues-queue-list-response-example
- key_count: 3
  name: Cloudflare Queues Queue Response Example
  slug: cloudflare-queues-queue-response-example
- key_count: 4
  name: Cloudflare R2 Bucket Example
  slug: cloudflare-r2-bucket-example
- key_count: 2
  name: Cloudflare R2 Bucket List Response Example
  slug: cloudflare-r2-bucket-list-response-example
- key_count: 3
  name: Cloudflare R2 Bucket Response Example
  slug: cloudflare-r2-bucket-response-example
- key_count: 11
  name: Cloudflare Stream Video Example
  slug: cloudflare-stream-video-example
- key_count: 2
  name: Cloudflare Stream Video List Response Example
  slug: cloudflare-stream-video-list-response-example
- key_count: 3
  name: Cloudflare Stream Video Response Example
  slug: cloudflare-stream-video-response-example
- key_count: 6
  name: Cloudflare Turnstile Verify Response Example
  slug: cloudflare-turnstile-verify-response-example
- key_count: 8
  name: Cloudflare Turnstile Widget Example
  slug: cloudflare-turnstile-widget-example
- key_count: 4
  name: Cloudflare Turnstile Widget Input Example
  slug: cloudflare-turnstile-widget-input-example
- key_count: 2
  name: Cloudflare Turnstile Widget List Response Example
  slug: cloudflare-turnstile-widget-list-response-example
- key_count: 3
  name: Cloudflare Turnstile Widget Response Example
  slug: cloudflare-turnstile-widget-response-example
- key_count: 3
  name: Cloudflare Vectorize Index Input Example
  slug: cloudflare-vectorize-index-input-example
- key_count: 2
  name: Cloudflare Vectorize Index List Response Example
  slug: cloudflare-vectorize-index-list-response-example
- key_count: 3
  name: Cloudflare Vectorize Index Response Example
  slug: cloudflare-vectorize-index-response-example
- key_count: 2
  name: Cloudflare Vectorize Query Response Example
  slug: cloudflare-vectorize-query-response-example
- key_count: 5
  name: Cloudflare Vectorize Vectorize Index Example
  slug: cloudflare-vectorize-vectorize-index-example
- key_count: 9
  name: Cloudflare Workers Ai Ai Run Request Example
  slug: cloudflare-workers-ai-ai-run-request-example
- key_count: 4
  name: Cloudflare Workers Ai Ai Run Response Example
  slug: cloudflare-workers-ai-ai-run-response-example
- key_count: 6
  name: Cloudflare Workers Ai Chat Completion Request Example
  slug: cloudflare-workers-ai-chat-completion-request-example
- key_count: 6
  name: Cloudflare Workers Ai Chat Completion Response Example
  slug: cloudflare-workers-ai-chat-completion-response-example
- key_count: 4
  name: Cloudflare Workers Ai Embedding Response Example
  slug: cloudflare-workers-ai-embedding-response-example
- key_count: 2
  name: Cloudflare Workers Route Input Example
  slug: cloudflare-workers-route-input-example
- key_count: 2
  name: Cloudflare Workers Route List Response Example
  slug: cloudflare-workers-route-list-response-example
- key_count: 2
  name: Cloudflare Workers Script List Response Example
  slug: cloudflare-workers-script-list-response-example
- key_count: 2
  name: Cloudflare Workers Worker Input Example
  slug: cloudflare-workers-worker-input-example
- key_count: 2
  name: Cloudflare Workers Worker List Response Example
  slug: cloudflare-workers-worker-list-response-example
- key_count: 4
  name: Cloudflare Workers Worker Response Example
  slug: cloudflare-workers-worker-response-example
features:
- REST API at api.cloudflare.com/client/v4 (1,200 req/5min global cap)
- GraphQL Analytics API for traffic, security, Workers analytics
- Workers serverless edge compute (100k req/day Free, 10M+ Paid at $5/mo, +$0.30/M requests, +$0.02/M CPU ms)
- Workers KV low-latency key-value storage
- R2 object storage with zero egress fees (S3-compatible)
- R2 SQL serverless analytic query engine with JOINs over Iceberg tables (May 2026)
- D1 serverless SQLite with global read replication and 30-day Time Travel
- Durable Objects for stateful coordination and per-instance SQL
- Cloudflare Images for storage and on-the-fly resizing
- Cloudflare Stream for VOD and live video
- Realtime SFU, TURN, and RealtimeKit for WebRTC media
- Pages for static site / JAMstack hosting
- 'Free plan: unlimited bandwidth, DDoS, Universal SSL'
- Pro at $25/zone/mo with WAF and image optimization
- Business at $200/zone/mo with custom SSL, 100% SLA
- Enterprise from ~$5k/zone/mo with Bot Management, Argo, API Shield
- Workers AI catalog of 78+ open-source models with OpenAI-compatible endpoints
- AI Gateway with 23+ providers and a unified REST endpoint (launched May 21 2026)
- Vectorize vector database; Hyperdrive for connection pooling
- Workflows for durable multi-step execution (Dynamic Workflows added May 2026)
- Agents SDK on Durable Objects with WebSockets, scheduling, MCP support
- Containers serverless container runtime co-located with Workers (SSH via Wrangler)
- Browser Run (formerly Browser Rendering) with /screenshot, /pdf, /markdown, /scrape, /crawl Quick Actions
- Workers VPC for private connectivity into AWS / Azure / GCP / on-prem and Cloudflare WAN
- Artifacts versioned Git-compatible file storage (closed beta)
- Cloudflare One SASE platform (Access, Tunnel, Gateway, Browser Isolation, CASB, DLP)
- Magic WAN, Magic Transit, Magic Firewall for network-as-a-service
- 14+ remote MCP servers at *.mcp.cloudflare.com for AI agent access to Cloudflare APIs
- Pingora reverse proxy and quiche QUIC/HTTP3 open-source reference implementations
finops:
- has_sources: true
  method: derived
  name: Cloudflare Finops
  primary_unit: m input tokens
  service_category: ''
  slug: cloudflare-finops
  template: false
graphqls:
- description: The Cloudflare GraphQL Analytics API provides flexible access to analytics data across Cloudflare products including HTTP requests, firewall events, and load balancing metrics. Developers can query sp
  name: Cloudflare GraphQL API
  slug: cloudflare-graphql
image: /assets/icons/cloudflare.png
json_schemas:
- name: aaa_audit_logs_response_collection
  property_count: 0
  slug: cloudflare-aaa-audit-logs-response-collection
- name: aaa_filters
  property_count: 40
  slug: cloudflare-aaa-filters
- name: Cloudflare Account
  property_count: 5
  slug: cloudflare-account
- name: addressing_api-response-single
  property_count: 4
  slug: cloudflare-addressing-api-response-single
- name: addressing_ips_jdcloud
  property_count: 4
  slug: cloudflare-addressing-ips-jdcloud
- name: addressing_ips
  property_count: 3
  slug: cloudflare-addressing-ips
- name: GatewayInput
  property_count: 7
  slug: cloudflare-ai-gateway-gateway-input
- name: GatewayListResponse
  property_count: 2
  slug: cloudflare-ai-gateway-gateway-list-response
- name: GatewayResponse
  property_count: 3
  slug: cloudflare-ai-gateway-gateway-response
- name: Gateway
  property_count: 11
  slug: cloudflare-ai-gateway-gateway
- name: AiRunRequest
  property_count: 9
  slug: cloudflare-ai-run-request
- name: AiRunResponse
  property_count: 4
  slug: cloudflare-ai-run-response
- name: bill-subs-api_subscription-v2
  property_count: 11
  slug: cloudflare-bill-subs-api-subscription-v2
- name: BucketListResponse
  property_count: 2
  slug: cloudflare-bucket-list-response
- name: BucketResponse
  property_count: 4
  slug: cloudflare-bucket-response
- name: BulkOperationResponse
  property_count: 2
  slug: cloudflare-bulk-operation-response
- name: ChatCompletionRequest
  property_count: 6
  slug: cloudflare-chat-completion-request
- name: ChatCompletionResponse
  property_count: 6
  slug: cloudflare-chat-completion-response
- name: ConfigInput
  property_count: 3
  slug: cloudflare-config-input
- name: ConfigListResponse
  property_count: 2
  slug: cloudflare-config-list-response
- name: ConfigResponse
  property_count: 4
  slug: cloudflare-config-response
- name: ConsumerInput
  property_count: 2
  slug: cloudflare-consumer-input
- name: D1DatabaseListResponse
  property_count: 3
  slug: cloudflare-d1-d1-database-list-response
- name: D1DatabaseResponse
  property_count: 3
  slug: cloudflare-d1-d1-database-response
- name: D1Database
  property_count: 6
  slug: cloudflare-d1-d1-database
- name: D1QueryResponse
  property_count: 2
  slug: cloudflare-d1-d1-query-response
- name: D1DatabaseListResponse
  property_count: 3
  slug: cloudflare-d1-database-list-response
- name: D1DatabaseResponse
  property_count: 4
  slug: cloudflare-d1-database-response
- name: Cloudflare D1 Database
  property_count: 7
  slug: cloudflare-d1-database
- name: D1QueryResponse
  property_count: 2
  slug: cloudflare-d1-query-response
- name: digital-experience-monitoring_http_details_response
  property_count: 7
  slug: cloudflare-digital-experience-monitoring-http-details-response
- name: DnsRecordInput
  property_count: 7
  slug: cloudflare-dns-dns-record-input
- name: DnsRecordListResponse
  property_count: 5
  slug: cloudflare-dns-dns-record-list-response
- name: DnsRecordResponse
  property_count: 3
  slug: cloudflare-dns-dns-record-response
- name: DnsRecord
  property_count: 13
  slug: cloudflare-dns-dns-record
- name: DnsRecordInput
  property_count: 8
  slug: cloudflare-dns-record-input
- name: DnsRecordListResponse
  property_count: 5
  slug: cloudflare-dns-record-list-response
- name: DnsRecordResponse
  property_count: 4
  slug: cloudflare-dns-record-response
- name: Cloudflare DNS Record
  property_count: 17
  slug: cloudflare-dns-record
- name: RecordType
  property_count: 0
  slug: cloudflare-dns-record-type
- name: DurableObjectNamespace
  property_count: 4
  slug: cloudflare-durable-objects-durable-object-namespace
- name: NamespaceListResponse
  property_count: 4
  slug: cloudflare-durable-objects-namespace-list-response
- name: EmbeddingResponse
  property_count: 4
  slug: cloudflare-embedding-response
- name: GatewayInput
  property_count: 7
  slug: cloudflare-gateway-input
- name: GatewayListResponse
  property_count: 2
  slug: cloudflare-gateway-list-response
- name: GatewayResponse
  property_count: 4
  slug: cloudflare-gateway-response
- name: ConfigInput
  property_count: 3
  slug: cloudflare-hyperdrive-config-input
- name: ConfigListResponse
  property_count: 2
  slug: cloudflare-hyperdrive-config-list-response
- name: ConfigResponse
  property_count: 3
  slug: cloudflare-hyperdrive-config-response
- name: HyperdriveConfig
  property_count: 4
  slug: cloudflare-hyperdrive-hyperdrive-config
- name: iam_api-response-single
  property_count: 4
  slug: cloudflare-iam-api-response-single
- name: iam_collection_membership_response
  property_count: 5
  slug: cloudflare-iam-collection-membership-response
- name: iam_membership_components-schemas-identifier
  property_count: 0
  slug: cloudflare-iam-membership-components-schemas-identifier
- name: iam_schemas-response_collection
  property_count: 5
  slug: cloudflare-iam-schemas-response-collection
- name: iam_single_membership_response
  property_count: 4
  slug: cloudflare-iam-single-membership-response
- name: ImageListResponse
  property_count: 2
  slug: cloudflare-image-list-response
- name: ImageResponse
  property_count: 4
  slug: cloudflare-image-response
- name: ImageListResponse
  property_count: 2
  slug: cloudflare-images-image-list-response
- name: ImageResponse
  property_count: 3
  slug: cloudflare-images-image-response
- name: Image
  property_count: 6
  slug: cloudflare-images-image
- name: VariantInput
  property_count: 3
  slug: cloudflare-images-variant-input
- name: IndexInput
  property_count: 3
  slug: cloudflare-index-input
- name: IndexListResponse
  property_count: 2
  slug: cloudflare-index-list-response
- name: IndexResponse
  property_count: 4
  slug: cloudflare-index-response
- name: KeyListResponse
  property_count: 3
  slug: cloudflare-key-list-response
- name: BulkOperationResponse
  property_count: 2
  slug: cloudflare-kv-bulk-operation-response
- name: KeyListResponse
  property_count: 3
  slug: cloudflare-kv-key-list-response
- name: NamespaceListResponse
  property_count: 3
  slug: cloudflare-kv-namespace-list-response
- name: NamespaceResponse
  property_count: 3
  slug: cloudflare-kv-namespace-response
- name: Namespace
  property_count: 3
  slug: cloudflare-kv-namespace
- name: load-balancing_load_shedding
  property_count: 4
  slug: cloudflare-load-balancing-load-shedding
- name: load-balancing_monitor-editable
  property_count: 16
  slug: cloudflare-load-balancing-monitor-editable
- name: load-balancing_origin_steering
  property_count: 1
  slug: cloudflare-load-balancing-origin-steering
- name: load-balancing_rules
  property_count: 0
  slug: cloudflare-load-balancing-rules
- name: load-balancing_schemas-references_response
  property_count: 5
  slug: cloudflare-load-balancing-schemas-references-response
- name: load-balancing_session_affinity_attributes
  property_count: 6
  slug: cloudflare-load-balancing-session-affinity-attributes
- name: LogpushJobInput
  property_count: 8
  slug: cloudflare-logpush-logpush-job-input
- name: LogpushJobListResponse
  property_count: 2
  slug: cloudflare-logpush-logpush-job-list-response
- name: LogpushJobResponse
  property_count: 3
  slug: cloudflare-logpush-logpush-job-response
- name: LogpushJob
  property_count: 10
  slug: cloudflare-logpush-logpush-job
- name: logpush_output_options
  property_count: 12
  slug: cloudflare-logpush-output-options
- name: MessageInput
  property_count: 2
  slug: cloudflare-message-input
- name: NamespaceListResponse_2
  property_count: 3
  slug: cloudflare-namespace-list-response-2
- name: NamespaceListResponse
  property_count: 4
  slug: cloudflare-namespace-list-response
- name: NamespaceResponse
  property_count: 4
  slug: cloudflare-namespace-response
- name: Cloudflare Notification Webhook Payload
  property_count: 10
  slug: cloudflare-notification-webhook-payload
- name: DeploymentListResponse
  property_count: 2
  slug: cloudflare-pages-deployment-list-response
- name: pages_deployment-response-logs
  property_count: 4
  slug: cloudflare-pages-deployment-response-logs
- name: Deployment
  property_count: 5
  slug: cloudflare-pages-deployment
- name: ProjectInput
  property_count: 3
  slug: cloudflare-pages-project-input
- name: ProjectListResponse
  property_count: 2
  slug: cloudflare-pages-project-list-response
- name: ProjectResponse
  property_count: 3
  slug: cloudflare-pages-project-response
- name: Project
  property_count: 7
  slug: cloudflare-pages-project
- name: QueryResponse
  property_count: 2
  slug: cloudflare-query-response
- name: QueueListResponse
  property_count: 2
  slug: cloudflare-queue-list-response
- name: QueueResponse
  property_count: 4
  slug: cloudflare-queue-response
- name: ConsumerInput
  property_count: 2
  slug: cloudflare-queues-consumer-input
- name: MessageInput
  property_count: 2
  slug: cloudflare-queues-message-input
- name: QueueListResponse
  property_count: 2
  slug: cloudflare-queues-queue-list-response
- name: QueueResponse
  property_count: 3
  slug: cloudflare-queues-queue-response
- name: Queue
  property_count: 6
  slug: cloudflare-queues-queue
- name: BucketListResponse
  property_count: 2
  slug: cloudflare-r2-bucket-list-response
- name: BucketResponse
  property_count: 3
  slug: cloudflare-r2-bucket-response
- name: Bucket
  property_count: 4
  slug: cloudflare-r2-bucket
- name: RouteInput
  property_count: 2
  slug: cloudflare-route-input
- name: RouteListResponse
  property_count: 2
  slug: cloudflare-route-list-response
- name: ScriptListResponse
  property_count: 2
  slug: cloudflare-script-list-response
- name: stream_signed_token_request
  property_count: 6
  slug: cloudflare-stream-signed-token-request
- name: VideoListResponse
  property_count: 2
  slug: cloudflare-stream-video-list-response
- name: VideoResponse
  property_count: 3
  slug: cloudflare-stream-video-response
- name: Video
  property_count: 11
  slug: cloudflare-stream-video
- name: tls-certificates-and-hostnames_certificate_response_single_id
  property_count: 4
  slug: cloudflare-tls-certificates-and-hostnames-certificate-response-single-id
- name: tls-certificates-and-hostnames_csr
  property_count: 0
  slug: cloudflare-tls-certificates-and-hostnames-csr
- name: tls-certificates-and-hostnames_hostnames
  property_count: 0
  slug: cloudflare-tls-certificates-and-hostnames-hostnames
- name: tls-certificates-and-hostnames_request_type
  property_count: 0
  slug: cloudflare-tls-certificates-and-hostnames-request-type
- name: tls-certificates-and-hostnames_requested_validity
  property_count: 0
  slug: cloudflare-tls-certificates-and-hostnames-requested-validity
- name: tls-certificates-and-hostnames_schemas-certificate_response_collection
  property_count: 5
  slug: cloudflare-tls-certificates-and-hostnames-schemas-certificate-response-collection
- name: tls-certificates-and-hostnames_sslpost
  property_count: 0
  slug: cloudflare-tls-certificates-and-hostnames-sslpost
- name: VerifyResponse
  property_count: 6
  slug: cloudflare-turnstile-verify-response
- name: WidgetInput
  property_count: 4
  slug: cloudflare-turnstile-widget-input
- name: WidgetListResponse
  property_count: 2
  slug: cloudflare-turnstile-widget-list-response
- name: WidgetResponse
  property_count: 3
  slug: cloudflare-turnstile-widget-response
- name: Widget
  property_count: 8
  slug: cloudflare-turnstile-widget
- name: VariantInput
  property_count: 3
  slug: cloudflare-variant-input
- name: IndexInput
  property_count: 3
  slug: cloudflare-vectorize-index-input
- name: IndexListResponse
  property_count: 2
  slug: cloudflare-vectorize-index-list-response
- name: IndexResponse
  property_count: 3
  slug: cloudflare-vectorize-index-response
- name: QueryResponse
  property_count: 2
  slug: cloudflare-vectorize-query-response
- name: VectorizeIndex
  property_count: 5
  slug: cloudflare-vectorize-vectorize-index
- name: VerifyResponse
  property_count: 6
  slug: cloudflare-verify-response
- name: VideoListResponse
  property_count: 2
  slug: cloudflare-video-list-response
- name: VideoResponse
  property_count: 4
  slug: cloudflare-video-response
- name: WidgetInput
  property_count: 4
  slug: cloudflare-widget-input
- name: WidgetListResponse
  property_count: 2
  slug: cloudflare-widget-list-response
- name: WidgetResponse
  property_count: 4
  slug: cloudflare-widget-response
- name: WorkerInput
  property_count: 2
  slug: cloudflare-worker-input
- name: WorkerListResponse
  property_count: 2
  slug: cloudflare-worker-list-response
- name: WorkerResponse
  property_count: 4
  slug: cloudflare-worker-response
- name: Cloudflare Worker Script
  property_count: 15
  slug: cloudflare-worker-script
- name: AiRunRequest
  property_count: 9
  slug: cloudflare-workers-ai-ai-run-request
- name: AiRunResponse
  property_count: 4
  slug: cloudflare-workers-ai-ai-run-response
- name: ChatCompletionRequest
  property_count: 6
  slug: cloudflare-workers-ai-chat-completion-request
- name: ChatCompletionResponse
  property_count: 6
  slug: cloudflare-workers-ai-chat-completion-response
- name: Cloudflare Workers Ai Clef Flash Schema Input
  property_count: 4
  slug: cloudflare-workers-ai-clef-flash-schema-input
- name: Cloudflare Workers Ai Clef Flash Schema Output
  property_count: 3
  slug: cloudflare-workers-ai-clef-flash-schema-output
- name: Cloudflare Workers Ai Clef Schema Input
  property_count: 4
  slug: cloudflare-workers-ai-clef-schema-input
- name: Cloudflare Workers Ai Clef Schema Output
  property_count: 3
  slug: cloudflare-workers-ai-clef-schema-output
- name: EmbeddingResponse
  property_count: 4
  slug: cloudflare-workers-ai-embedding-response
- name: RouteInput
  property_count: 2
  slug: cloudflare-workers-route-input
- name: RouteListResponse
  property_count: 2
  slug: cloudflare-workers-route-list-response
- name: ScriptListResponse
  property_count: 2
  slug: cloudflare-workers-script-list-response
- name: WorkerInput
  property_count: 2
  slug: cloudflare-workers-worker-input
- name: WorkerListResponse
  property_count: 2
  slug: cloudflare-workers-worker-list-response
- name: WorkerResponse
  property_count: 4
  slug: cloudflare-workers-worker-response
- name: zero-trust-gateway_rule-settings
  property_count: 20
  slug: cloudflare-zero-trust-gateway-rule-settings
- name: Cloudflare Zone
  property_count: 17
  slug: cloudflare-zone
- name: zones_setting
  property_count: 0
  slug: cloudflare-zones-setting
- name: zones_zone
  property_count: 13
  slug: cloudflare-zones-zone
- name: zones_zone_settings_response_collection
  property_count: 4
  slug: cloudflare-zones-zone-settings-response-collection
json_structures:
- name: Cloudflare Ai Gateway Gateway Input Structure
  property_count: 7
  slug: cloudflare-ai-gateway-gateway-input-structure
- name: Cloudflare Ai Gateway Gateway List Response Structure
  property_count: 2
  slug: cloudflare-ai-gateway-gateway-list-response-structure
- name: Cloudflare Ai Gateway Gateway Response Structure
  property_count: 3
  slug: cloudflare-ai-gateway-gateway-response-structure
- name: Cloudflare Ai Gateway Gateway Structure
  property_count: 11
  slug: cloudflare-ai-gateway-gateway-structure
- name: Cloudflare D1 D1 Database List Response Structure
  property_count: 3
  slug: cloudflare-d1-d1-database-list-response-structure
- name: Cloudflare D1 D1 Database Response Structure
  property_count: 3
  slug: cloudflare-d1-d1-database-response-structure
- name: Cloudflare D1 D1 Database Structure
  property_count: 6
  slug: cloudflare-d1-d1-database-structure
- name: Cloudflare D1 D1 Query Response Structure
  property_count: 2
  slug: cloudflare-d1-d1-query-response-structure
- name: Cloudflare Dns Dns Record Input Structure
  property_count: 7
  slug: cloudflare-dns-dns-record-input-structure
- name: Cloudflare Dns Dns Record List Response Structure
  property_count: 5
  slug: cloudflare-dns-dns-record-list-response-structure
- name: Cloudflare Dns Dns Record Response Structure
  property_count: 3
  slug: cloudflare-dns-dns-record-response-structure
- name: Cloudflare Dns Dns Record Structure
  property_count: 13
  slug: cloudflare-dns-dns-record-structure
- name: Cloudflare Dns Record Type Structure
  property_count: 0
  slug: cloudflare-dns-record-type-structure
- name: Cloudflare Durable Objects Durable Object Namespace Structure
  property_count: 4
  slug: cloudflare-durable-objects-durable-object-namespace-structure
- name: Cloudflare Durable Objects Namespace List Response Structure
  property_count: 4
  slug: cloudflare-durable-objects-namespace-list-response-structure
- name: Cloudflare Hyperdrive Config Input Structure
  property_count: 3
  slug: cloudflare-hyperdrive-config-input-structure
- name: Cloudflare Hyperdrive Config List Response Structure
  property_count: 2
  slug: cloudflare-hyperdrive-config-list-response-structure
- name: Cloudflare Hyperdrive Config Response Structure
  property_count: 3
  slug: cloudflare-hyperdrive-config-response-structure
- name: Cloudflare Hyperdrive Hyperdrive Config Structure
  property_count: 4
  slug: cloudflare-hyperdrive-hyperdrive-config-structure
- name: Cloudflare Images Image List Response Structure
  property_count: 2
  slug: cloudflare-images-image-list-response-structure
- name: Cloudflare Images Image Response Structure
  property_count: 3
  slug: cloudflare-images-image-response-structure
- name: Cloudflare Images Image Structure
  property_count: 6
  slug: cloudflare-images-image-structure
- name: Cloudflare Images Variant Input Structure
  property_count: 3
  slug: cloudflare-images-variant-input-structure
- name: Cloudflare Kv Bulk Operation Response Structure
  property_count: 2
  slug: cloudflare-kv-bulk-operation-response-structure
- name: Cloudflare Kv Key List Response Structure
  property_count: 3
  slug: cloudflare-kv-key-list-response-structure
- name: Cloudflare Kv Namespace List Response Structure
  property_count: 3
  slug: cloudflare-kv-namespace-list-response-structure
- name: Cloudflare Kv Namespace Response Structure
  property_count: 3
  slug: cloudflare-kv-namespace-response-structure
- name: Cloudflare Kv Namespace Structure
  property_count: 3
  slug: cloudflare-kv-namespace-structure
- name: Cloudflare Logpush Logpush Job Input Structure
  property_count: 8
  slug: cloudflare-logpush-logpush-job-input-structure
- name: Cloudflare Logpush Logpush Job List Response Structure
  property_count: 2
  slug: cloudflare-logpush-logpush-job-list-response-structure
- name: Cloudflare Logpush Logpush Job Response Structure
  property_count: 3
  slug: cloudflare-logpush-logpush-job-response-structure
- name: Cloudflare Logpush Logpush Job Structure
  property_count: 10
  slug: cloudflare-logpush-logpush-job-structure
- name: Cloudflare Pages Deployment List Response Structure
  property_count: 2
  slug: cloudflare-pages-deployment-list-response-structure
- name: Cloudflare Pages Deployment Structure
  property_count: 5
  slug: cloudflare-pages-deployment-structure
- name: Cloudflare Pages Project Input Structure
  property_count: 3
  slug: cloudflare-pages-project-input-structure
- name: Cloudflare Pages Project List Response Structure
  property_count: 2
  slug: cloudflare-pages-project-list-response-structure
- name: Cloudflare Pages Project Response Structure
  property_count: 3
  slug: cloudflare-pages-project-response-structure
- name: Cloudflare Pages Project Structure
  property_count: 7
  slug: cloudflare-pages-project-structure
- name: Cloudflare Queues Consumer Input Structure
  property_count: 2
  slug: cloudflare-queues-consumer-input-structure
- name: Cloudflare Queues Message Input Structure
  property_count: 2
  slug: cloudflare-queues-message-input-structure
- name: Cloudflare Queues Queue List Response Structure
  property_count: 2
  slug: cloudflare-queues-queue-list-response-structure
- name: Cloudflare Queues Queue Response Structure
  property_count: 3
  slug: cloudflare-queues-queue-response-structure
- name: Cloudflare Queues Queue Structure
  property_count: 6
  slug: cloudflare-queues-queue-structure
- name: Cloudflare R2 Bucket List Response Structure
  property_count: 2
  slug: cloudflare-r2-bucket-list-response-structure
- name: Cloudflare R2 Bucket Response Structure
  property_count: 3
  slug: cloudflare-r2-bucket-response-structure
- name: Cloudflare R2 Bucket Structure
  property_count: 4
  slug: cloudflare-r2-bucket-structure
- name: Cloudflare Stream Video List Response Structure
  property_count: 2
  slug: cloudflare-stream-video-list-response-structure
- name: Cloudflare Stream Video Response Structure
  property_count: 3
  slug: cloudflare-stream-video-response-structure
- name: Cloudflare Stream Video Structure
  property_count: 11
  slug: cloudflare-stream-video-structure
- name: Cloudflare Turnstile Verify Response Structure
  property_count: 6
  slug: cloudflare-turnstile-verify-response-structure
- name: Cloudflare Turnstile Widget Input Structure
  property_count: 4
  slug: cloudflare-turnstile-widget-input-structure
- name: Cloudflare Turnstile Widget List Response Structure
  property_count: 2
  slug: cloudflare-turnstile-widget-list-response-structure
- name: Cloudflare Turnstile Widget Response Structure
  property_count: 3
  slug: cloudflare-turnstile-widget-response-structure
- name: Cloudflare Turnstile Widget Structure
  property_count: 8
  slug: cloudflare-turnstile-widget-structure
- name: Cloudflare Vectorize Index Input Structure
  property_count: 3
  slug: cloudflare-vectorize-index-input-structure
- name: Cloudflare Vectorize Index List Response Structure
  property_count: 2
  slug: cloudflare-vectorize-index-list-response-structure
- name: Cloudflare Vectorize Index Response Structure
  property_count: 3
  slug: cloudflare-vectorize-index-response-structure
- name: Cloudflare Vectorize Query Response Structure
  property_count: 2
  slug: cloudflare-vectorize-query-response-structure
- name: Cloudflare Vectorize Vectorize Index Structure
  property_count: 5
  slug: cloudflare-vectorize-vectorize-index-structure
- name: Cloudflare Workers Ai Ai Run Request Structure
  property_count: 9
  slug: cloudflare-workers-ai-ai-run-request-structure
- name: Cloudflare Workers Ai Ai Run Response Structure
  property_count: 4
  slug: cloudflare-workers-ai-ai-run-response-structure
- name: Cloudflare Workers Ai Chat Completion Request Structure
  property_count: 6
  slug: cloudflare-workers-ai-chat-completion-request-structure
- name: Cloudflare Workers Ai Chat Completion Response Structure
  property_count: 6
  slug: cloudflare-workers-ai-chat-completion-response-structure
- name: Cloudflare Workers Ai Embedding Response Structure
  property_count: 4
  slug: cloudflare-workers-ai-embedding-response-structure
- name: Cloudflare Workers Route Input Structure
  property_count: 2
  slug: cloudflare-workers-route-input-structure
- name: Cloudflare Workers Route List Response Structure
  property_count: 2
  slug: cloudflare-workers-route-list-response-structure
- name: Cloudflare Workers Script List Response Structure
  property_count: 2
  slug: cloudflare-workers-script-list-response-structure
- name: Cloudflare Workers Worker Input Structure
  property_count: 2
  slug: cloudflare-workers-worker-input-structure
- name: Cloudflare Workers Worker List Response Structure
  property_count: 2
  slug: cloudflare-workers-worker-list-response-structure
- name: Cloudflare Workers Worker Response Structure
  property_count: 4
  slug: cloudflare-workers-worker-response-structure
jsonld:
- class_count: 0
  name: Cloudflare Ai Gateway Context
  property_count: 0
  slug: cloudflare-ai-gateway-context
- class_count: 0
  name: Cloudflare Context
  property_count: 13
  slug: cloudflare-context
- class_count: 0
  name: Cloudflare D1 Context
  property_count: 0
  slug: cloudflare-d1-context
- class_count: 0
  name: Cloudflare Dns Context
  property_count: 0
  slug: cloudflare-dns-context
- class_count: 0
  name: Cloudflare Durable Objects Context
  property_count: 0
  slug: cloudflare-durable-objects-context
- class_count: 0
  name: Cloudflare Hyperdrive Context
  property_count: 0
  slug: cloudflare-hyperdrive-context
- class_count: 0
  name: Cloudflare Images Context
  property_count: 0
  slug: cloudflare-images-context
- class_count: 0
  name: Cloudflare Kv Context
  property_count: 0
  slug: cloudflare-kv-context
- class_count: 0
  name: Cloudflare Logpush Context
  property_count: 0
  slug: cloudflare-logpush-context
- class_count: 0
  name: Cloudflare Pages Context
  property_count: 0
  slug: cloudflare-pages-context
- class_count: 0
  name: Cloudflare Queues Context
  property_count: 0
  slug: cloudflare-queues-context
- class_count: 0
  name: Cloudflare R2 Context
  property_count: 0
  slug: cloudflare-r2-context
- class_count: 0
  name: Cloudflare Stream Context
  property_count: 0
  slug: cloudflare-stream-context
- class_count: 0
  name: Cloudflare Turnstile Context
  property_count: 0
  slug: cloudflare-turnstile-context
- class_count: 0
  name: Cloudflare Vectorize Context
  property_count: 0
  slug: cloudflare-vectorize-context
- class_count: 0
  name: Cloudflare Workers Ai Context
  property_count: 0
  slug: cloudflare-workers-ai-context
- class_count: 0
  name: Cloudflare Workers Context
  property_count: 0
  slug: cloudflare-workers-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server (monorepo)
  slug: mcp-server-monorepo
- description: ''
  name: Observability MCP
  slug: observability-mcp
- description: ''
  name: Workers Bindings MCP
  slug: workers-bindings-mcp
- description: ''
  name: Workers Builds MCP
  slug: workers-builds-mcp
- description: ''
  name: Radar MCP
  slug: radar-mcp
- description: ''
  name: DNS Analytics MCP
  slug: dns-analytics-mcp
- description: ''
  name: AI Gateway MCP
  slug: ai-gateway-mcp
- description: ''
  name: Browser Rendering MCP
  slug: browser-rendering-mcp
- description: ''
  name: Logpush MCP
  slug: logpush-mcp
- description: ''
  name: GraphQL MCP
  slug: graphql-mcp
- description: ''
  name: CASB MCP
  slug: casb-mcp
- description: ''
  name: Container Sandbox MCP
  slug: container-sandbox-mcp
- description: ''
  name: Audit Logs MCP
  slug: audit-logs-mcp
- description: ''
  name: DEM MCP
  slug: dem-mcp
modified: '2026-05-22'
name: Cloudflare
nav: Providers
network: true
overview: 'Cloudflare publishes 651 API contracts indexed on the [APIs.io](https://apis.io/) network, including Workers AI Clef Decision Models API, Waiting Room API, Workflows API, and 648 more. Tagged areas include AI Gateway, API Gateway, Artificial Intelligence, CDN, and Cloud.


  The Cloudflare catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 17 JSON-LD contexts, and 4 Spectral governance rulesets.


  Cloudflare''s developer surface includes signup flow, API reference, authentication, developer portal, getting-started guide, engineering blog, pricing, and 133 more developer resources.'
plans:
- name: Cloudflare Plans Pricing
  plan_count: 6
  slug: cloudflare-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Cloudflare Rate Limits
  slug: cloudflare-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Cloudflare — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: cloudflare-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Cloudflare — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cloudflare-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Cloudflare API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: cloudflare-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Cloudflare API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: cloudflare-spectral-rules
score:
  band: exemplar
  composite: 82.8
  coverage:
    artifact_dirs: 44
    catalog_earned: 79.0
    catalog_earned_first_party: 12.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 84.2
    contract_governance: 45.5
    contract_quality: 80.5
    developer_ergonomics: 91.1
    discoverability: 72.5
    operational_transparency: 57.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 82.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 97.6
      total: 620
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/cloudflare/cloudflare-2026-06-20T174548.png
security:
- kind: authentication
  name: Cloudflare Authentication
  slug: cloudflare-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Cloudflare Domain Security
  slug: cloudflare-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudflare Vulnerability Disclosure
  slug: cloudflare-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 11
skills:
- name: agents-sdk
  slug: agents-sdk
- name: cloudflare-email-service
  slug: cloudflare-email-service
- name: cloudflare-one-migrations
  slug: cloudflare-one-migrations
- name: cloudflare-one
  slug: cloudflare-one
- name: cloudflare
  slug: cloudflare
- name: durable-objects
  slug: durable-objects
- name: sandbox-sdk
  slug: sandbox-sdk
- name: turnstile-spin
  slug: turnstile-spin
- name: web-perf
  slug: web-perf
- name: workers-best-practices
  slug: workers-best-practices
- name: wrangler
  slug: wrangler
slug: cloudflare
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
- Cloudflare
- A2A
use_cases:
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
website: https://www.cloudflare.com/
---
