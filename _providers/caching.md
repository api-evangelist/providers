---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 33
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering API-accessible caching services, in-memory data stores, key-value caches, and edge/CDN cache APIs. Caching reduces latency, lowers backend load, and improves API consumer experience by serving frequently requested data from memory or geographically distributed edges. This collection covers managed in-memory data stores like Redis, Amazon ElastiCache, and Google Cloud Memorystore; high-throughput alternatives such as Dragonfly, Aerospike, and Hazelcast; and edge cache services from Cloudflare, Fastly, Akamai, AWS CloudFront, and Vercel. It focuses on caching as a service or product, not on HTTP cache header semantics handled at the gateway or proxy layer.
examples:
- key_count: 12
  name: Caching Cache Entry Example
  slug: caching-cache-entry-example
- key_count: 11
  name: Caching Purge Request Example
  slug: caching-purge-request-example
features:
- description: Caching services like Redis, Memcached, and Valkey store data in RAM keyed by strings, hashes, or structured types, returning values in sub-millisecond response times for hot data paths.
  name: In-Memory Key-Value Storage
- description: Cloud providers like Amazon ElastiCache, Google Cloud Memorystore, Azure Cache for Redis, and Upstash offer fully managed Redis and Memcached clusters with provisioning, patching, failover, and scaling handled by the provider.
  name: Managed Cache as a Service
- description: Services like Cloudflare, Fastly, Akamai, and AWS CloudFront cache API responses, static assets, and dynamic content at globally distributed edge locations to minimize latency for geographically dispersed consumers.
  name: Edge and CDN Caching
- description: Edge and in-memory cache services expose purge, invalidate, and refresh endpoints that let applications evict stale entries by key, tag, surrogate-key, or URL pattern when underlying data changes.
  name: Cache Invalidation and Purge APIs
- description: Cache entries are governed by time-to-live values and eviction strategies (LRU, LFU, allkeys-lru, volatile-ttl) configurable per key or per cache instance to balance hit rates against memory pressure.
  name: TTL and Eviction Policies
- description: Platforms like Hazelcast, Apache Ignite, GridGain, and Aerospike distribute cache data across multiple nodes with partitioning, replication, and near-cache support for large-scale, low-latency workloads.
  name: Distributed and Clustered Caches
- description: Newer products like Cloudflare Workers KV, Vercel Edge Config, Akamai EdgeKV, and Fastly KV Store expose programmatic key-value APIs at the edge, blending CDN distribution with application state.
  name: Edge Key-Value Stores
- description: Edge caches like Fastly and Cloudflare support surrogate keys and cache tags that group related objects so a single purge request can invalidate thousands of related entries atomically.
  name: Cache Tagging and Surrogate Keys
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: The most widely deployed open source in-memory data structure store, supporting strings, hashes, sets, sorted sets, streams, and pub/sub with sub-millisecond latency.
  name: Redis
- description: Fully managed in-memory cache service from AWS supporting Redis and Memcached engines with multi-AZ failover and seamless EC2 integration.
  name: Amazon ElastiCache
- description: Google Cloud's managed Redis and Memcached service with VPC integration, automatic patching, and high-availability replication.
  name: Google Cloud Memorystore
- description: Microsoft's managed Redis service offering Basic, Standard, Premium, and Enterprise tiers with geo-replication and persistence.
  name: Azure Cache for Redis
- description: Serverless Redis and Kafka platform with per-request pricing, global replication, and an HTTP-based REST API for edge and serverless workloads.
  name: Upstash
- description: Global edge network providing CDN caching, Workers KV, R2, Cache API, and surrogate-key purging across 300+ POPs worldwide.
  name: Cloudflare
- description: Real-time edge cloud platform with instant purge, surrogate keys, VCL-based cache configuration, and the Fastly KV Store for edge state.
  name: Fastly
- description: Enterprise CDN and edge platform with EdgeKV key-value storage, Ion delivery, and global edge caching across the world's largest distributed network.
  name: Akamai Technologies
- description: Frontend cloud with Edge Config, KV (powered by Upstash), and CDN caching for Next.js and other frameworks deployed to its global edge network.
  name: Vercel
- description: Open-source in-memory data grid for distributed caching, stream processing, and real-time analytics across clustered Java and polyglot applications.
  name: Hazelcast
json_schemas:
- name: CacheEntry
  property_count: 12
  slug: caching-cache-entry
- name: PurgeRequest
  property_count: 11
  slug: caching-purge-request
json_structures:
- name: Caching Cache Entry Structure
  property_count: 12
  slug: caching-cache-entry-structure
- name: Caching Purge Request Structure
  property_count: 11
  slug: caching-purge-request-structure
jsonld:
- class_count: 3
  name: Caching Context
  property_count: 21
  slug: caching-context
layout: provider
modified: '2026-05-19'
name: Caching
nav: Providers
network: true
overview: 'Caching is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cache, Caching, In-Memory Database, Edge Cache, and Key-Value Store.


  The Caching catalog on APIs.io includes 1 JSON-LD context.


  Caching''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: caching
tags:
- Cache
- Caching
- In-Memory Database
- Edge Cache
- Key-Value Store
- CDN
use_cases:
- description: Applications cache authenticated sessions, JWTs, and OAuth tokens in Redis or Memcached so API gateways can validate requests without round-tripping to an identity provider on every call.
  name: Session and Token Caching
- description: API gateways and edge networks cache GET responses keyed by URL and headers so repeated requests for the same resource are served from cache, reducing backend cost and latency.
  name: API Response Caching
- description: Backend services cache expensive database query results in Redis or Hazelcast with TTLs so subsequent identical queries return immediately without hitting the source database.
  name: Database Query Result Caching
- description: Redis and similar in-memory stores back distributed rate limiters, leaderboards, and counters using atomic increment operations that scale to millions of operations per second.
  name: Rate Limiting and Counters
- description: Cloudflare, Fastly, CloudFront, and Akamai cache images, JavaScript, CSS, and other static assets at edge POPs to minimize origin bandwidth and serve global users with low latency.
  name: CDN Static Asset Delivery
- description: Edge KV stores like Vercel Edge Config and Cloudflare Workers KV hold feature flags, A/B test configurations, and personalization data accessed by edge functions on every request.
  name: Edge Personalization and Feature Flags
- description: Redis sorted sets and pub/sub channels power real-time leaderboards, chat backends, and notification fanout patterns where in-memory speed is required.
  name: Real-Time Leaderboards and Pub/Sub
- description: Applications pre-populate caches before traffic spikes and use techniques like singleflight and probabilistic early expiration backed by Redis to prevent thundering herds against origin systems.
  name: Pre-Warming and Cache Stampede Prevention
website: https://apievangelist.com
---
