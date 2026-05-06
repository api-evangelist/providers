---
aid: scalable-systems
name: Scalable Systems
description: A topic collection focused on APIs, tools, and platforms for designing and operating scalable distributed systems. Covers load balancing, auto-scaling, service discovery, distributed caching, message queues, and the cloud infrastructure APIs that enable systems to handle growth in data, traffic, and complexity. Relevant to site reliability engineers, infrastructure architects, and platform engineers responsible for operating high-scale production environments.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Auto Scaling
  - Caching
  - Cloud Infrastructure
  - Distributed Systems
  - High Availability
  - Infrastructure
  - Load Balancing
  - Message Queues
  - Platform Engineering
  - Scalable Architecture
  - Service Discovery
type: Index
created: '2025-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scalable-systems:aws-autoscaling
    name: AWS Auto Scaling API
    description: AWS Auto Scaling monitors applications and automatically adjusts capacity across multiple AWS resources including EC2, ECS, Lambda, DynamoDB, and Aurora. The API enables defining scaling policies, target tracking, and scheduled scaling for systems that must respond to variable load.
    tags:
      - Auto Scaling
      - AWS
      - Cloud Infrastructure
      - Scalable Architecture
    humanURL: https://docs.aws.amazon.com/autoscaling/application/APIReference/Welcome.html
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/autoscaling/application/APIReference/Welcome.html
  - aid: scalable-systems:haproxy
    name: HAProxy Data Plane API
    description: HAProxy's Data Plane API is a modern REST API for dynamically configuring the HAProxy load balancer without restarting. Enables runtime management of backends, servers, frontends, and ACLs in high-availability deployments.
    tags:
      - High Availability
      - Load Balancing
      - Proxy
      - Traffic Management
    humanURL: https://www.haproxy.com/documentation/dataplaneapi/
    properties:
      - type: Documentation
        url: https://www.haproxy.com/documentation/dataplaneapi/
      - type: OpenAPI
        url: https://github.com/haproxytech/dataplaneapi/blob/master/specification/build/haproxy_spec.yaml
      - type: GitHub
        url: https://github.com/haproxytech/dataplaneapi
  - aid: scalable-systems:redis
    name: Redis REST API (Upstash)
    description: Redis is the dominant distributed in-memory cache and data structure store used to reduce latency and database load in scalable systems. Upstash provides a serverless Redis-compatible REST API for low-latency caching at scale.
    tags:
      - Caching
      - Distributed Systems
      - In-Memory
      - Low Latency
    humanURL: https://upstash.com/docs/redis/features/restapi
    properties:
      - type: Documentation
        url: https://upstash.com/docs/redis/features/restapi
      - type: GitHub
        url: https://github.com/redis/redis
  - aid: scalable-systems:rabbitmq
    name: RabbitMQ Management API
    description: RabbitMQ's HTTP-based Management API enables programmatic administration of queues, exchanges, bindings, vhosts, and consumers. RabbitMQ is widely used for asynchronous task queues, decoupling services, and absorbing traffic spikes in scalable systems.
    tags:
      - Asynchronous
      - Decoupling
      - Message Queues
      - Messaging
    humanURL: https://www.rabbitmq.com/management.html
    properties:
      - type: Documentation
        url: https://www.rabbitmq.com/management.html
      - type: OpenAPI
        url: https://www.rabbitmq.com/resources/specs/management-api.json
      - type: GitHub
        url: https://github.com/rabbitmq/rabbitmq-server
  - aid: scalable-systems:consul
    name: Consul API
    description: HashiCorp Consul provides service discovery, health checking, key-value storage, and service mesh capabilities via a comprehensive REST API. Core component for service registry and dynamic configuration in scalable distributed systems.
    tags:
      - Configuration Management
      - High Availability
      - Service Discovery
      - Service Mesh
    humanURL: https://developer.hashicorp.com/consul/api-docs
    properties:
      - type: Documentation
        url: https://developer.hashicorp.com/consul/api-docs
      - type: GitHub
        url: https://github.com/hashicorp/consul
  - aid: scalable-systems:etcd
    name: etcd API
    description: etcd is a strongly consistent, distributed key-value store used as the backing store for Kubernetes and many distributed systems. Its gRPC API provides atomic operations, watches, leases, and transactions for distributed coordination and consensus.
    tags:
      - Configuration Management
      - Distributed Systems
      - High Availability
      - Kubernetes
    humanURL: https://etcd.io/docs/latest/learning/api/
    properties:
      - type: Documentation
        url: https://etcd.io/docs/latest/learning/api/
      - type: GitHub
        url: https://github.com/etcd-io/etcd
  - aid: scalable-systems:celery
    name: Celery Flower API
    description: Celery is a distributed task queue for Python applications. Flower is Celery's real-time monitoring tool that exposes an HTTP API for inspecting workers, tasks, queues, and scheduled jobs in production systems.
    tags:
      - Asynchronous
      - Distributed Systems
      - Message Queues
      - Task Queue
    humanURL: https://flower.readthedocs.io/en/latest/api.html
    properties:
      - type: Documentation
        url: https://flower.readthedocs.io/en/latest/api.html
      - type: GitHub
        url: https://github.com/celery/celery
  - aid: scalable-systems:nginx-plus
    name: NGINX Plus API
    description: NGINX Plus provides an advanced REST API for runtime configuration and statistics of upstream server groups, virtual servers, and cache zones. Enables dynamic load balancer reconfiguration and real-time traffic monitoring without reloads.
    tags:
      - HTTP
      - High Performance
      - Load Balancing
      - Traffic Management
    humanURL: https://nginx.org/en/docs/http/ngx_http_api_module.html
    properties:
      - type: Documentation
        url: https://nginx.org/en/docs/http/ngx_http_api_module.html
common:
  - type: Guide
    url: https://www.nginx.com/resources/glossary/load-balancing/
    name: Load Balancing Explained
  - type: Guide
    url: https://aws.amazon.com/autoscaling/features/
    name: AWS Auto Scaling Features
  - type: Guide
    url: https://redis.io/docs/manual/scaling/
    name: Redis Scaling Guide
  - type: Guide
    url: https://www.consul.io/use-cases/service-discovery-and-health-checking
    name: Service Discovery with Consul
  - type: Guide
    url: https://geeksforgeeks.org/distributed-systems/what-is-scalable-system-in-distributed-system/
    name: Scalable Systems in Distributed Computing
  - type: JSONSchema
    url: https://github.com/api-evangelist/scalable-systems/blob/main/json-schema/scalable-systems-load-balancer-schema.json
    name: Load Balancer JSON Schema
  - type: JSONStructure
    url: https://github.com/api-evangelist/scalable-systems/blob/main/json-structure/scalable-systems-load-balancer-structure.json
    name: Load Balancer JSON Structure
  - type: JSONLDContext
    url: https://github.com/api-evangelist/scalable-systems/blob/main/json-ld/scalable-systems-context.jsonld
    name: Scalable Systems JSON-LD Context
  - type: Vocabulary
    url: https://github.com/api-evangelist/scalable-systems/blob/main/vocabulary/scalable-systems-vocabulary.yml
    name: Scalable Systems Vocabulary
  - type: Examples
    url: https://github.com/api-evangelist/scalable-systems/blob/main/examples/scalable-systems-rabbitmq-queue-example.json
    name: RabbitMQ Queue Configuration Example
  - type: Examples
    url: https://github.com/api-evangelist/scalable-systems/blob/main/examples/scalable-systems-consul-service-registration-example.json
    name: Consul Service Registration Example
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
