---
aid: unkey
name: Unkey
description: Unkey is the developer platform for modern APIs, providing globally distributed API key management, rate limiting, identity management, analytics, and deployment capabilities. The platform enables API providers to issue, verify, and revoke keys with metadata, expiration, usage credits, permissions, and roles — without managing any infrastructure.
url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-04'
specificationVersion: '0.19'
type: Index
tags:
  - API Keys
  - Rate Limiting
  - Authentication
  - Developer Platform
  - Access Control
  - Identity
  - Analytics
apis:
  - aid: unkey:unkey-api
    name: Unkey API
    description: 'Unkey''s REST API providing programmatic access to all platform resources: API namespace management, API key lifecycle (create, verify, update, reroll, delete), identity management, permissions and roles, standalone rate limiting with namespace overrides, key verification analytics via SQL, and deployment operations. All management operations use Bearer authentication with root keys.'
    humanURL: https://www.unkey.com
    baseURL: https://api.unkey.com
    tags:
      - API Keys
      - Rate Limiting
      - Identity
      - Permissions
      - Analytics
      - Deployments
    properties:
      - type: Documentation
        url: https://www.unkey.com/docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/openapi/unkey-openapi.yml
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/rules/unkey-rules.yml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/capabilities/api-key-management.yaml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/capabilities/rate-limiting.yaml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/capabilities/identity-management.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/json-schema/unkey-key-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/json-schema/unkey-ratelimit-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/json-schema/unkey-identity-schema.json
common:
  - type: Website
    url: https://www.unkey.com
  - type: Documentation
    url: https://www.unkey.com/docs
  - type: GitHub
    url: https://github.com/unkeyed/unkey
  - type: Pricing
    url: https://www.unkey.com/pricing
  - type: Blog
    url: https://www.unkey.com/blog
  - type: Changelog
    url: https://www.unkey.com/changelog
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/vocabulary/unkey-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/unkey/refs/heads/main/json-ld/unkey-context.jsonld
  - type: Features
    data:
      - 'Free: 0.25 vCPU / 0.25 GB per instance, 1 concurrent build'
      - 'Starter $5/mo: 2 vCPU/2 GB, $5 credits, custom domains'
      - 'Pro $25/mo: 8 vCPU/8 GB, $25 credits'
      - 'Business $50/mo: 32 vCPU/32 GB, $50 credits'
      - Predictable usage-based billing on top of subscription
      - 'API Keys: create, verify, list, update, delete'
      - 'Rate Limiting: standalone evaluations without keys'
      - REST API at api.unkey.com
      - 'REST rate limit: 60 req/sec Free, 600 req/sec Pro+'
      - Identities for tying multiple keys to a user/account
      - Permissions and roles per key
      - Multi-namespace ratelimit overrides
      - OAuth 2.0 + root keys
      - Audit log for key/identity events
      - Webhooks for key/identity changes
      - Open-source self-hostable
    sources:
      - https://www.unkey.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
