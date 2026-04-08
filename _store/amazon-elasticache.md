---
aid: amazon-elasticache
url: https://raw.githubusercontent.com/api-evangelist/amazon-elasticache/refs/heads/main/apis.yml
apis:
- name: Amazon ElastiCache API
  description: API for managing Amazon ElastiCache clusters, replication groups, and related resources.
  image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
  url: https://aws.amazon.com/elasticache/
  baseURL: https://elasticache.amazonaws.com
  properties:
  - type: documentation
    url: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/
  - type: openapi
    url: openapi/amazon-elasticache-openapi.yml
  - type: openapi
    url: https://api.apis.guru/v2/specs/amazonaws.com/elasticache/2015-02-02/openapi.yaml
  - type: json-schema
    url: json-schema/amazon-elasticache-cachecluster-schema.json
  - type: json-ld
    url: json-ld/amazon-elasticache-context.jsonld
  - type: pricing
    url: https://aws.amazon.com/elasticache/pricing/
  - type: getting-started
    url: https://aws.amazon.com/elasticache/getting-started/
  - type: faq
    url: https://aws.amazon.com/elasticache/faqs/
  - type: user-guide
    url: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/
  - type: api-reference
    url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/
  - type: cli-reference
    url: https://docs.aws.amazon.com/cli/latest/reference/elasticache/
  - type: security
    url: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/security.html
name: Amazon ElastiCache
tags:
- Amazon Web Services
- AWS
- Caching
- Database
- ElastiCache
- In-Memory
- Memcached
- Redis
type: Contract
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Amazon ElastiCache is a fully managed in-memory caching service supporting Redis and Memcached. ElastiCache makes it easy to deploy, operate, and scale popular open-source compatible in-memory data stores, improving the performance of web applications by allowing you to retrieve information from fast, managed, in-memory caches.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

