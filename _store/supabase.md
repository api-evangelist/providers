---
aid: supabase
name: Supabase
description: Supabase is an open-source Firebase alternative that provides a suite of backend services built on top of PostgreSQL. It offers a managed PostgreSQL database with auto-generated REST and GraphQL APIs via PostgREST, real-time data subscriptions via WebSockets, user authentication with JWT (GoTrue), file storage with S3-compatible object storage, edge compute via globally distributed TypeScript functions on the Deno runtime, and a management API for programmatic control of projects and organizations. Supabase is available as a fully managed cloud service (app.supabase.com) and as a self-hosted open-source deployment.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Backend As A Service
  - PostgreSQL
  - Open Source
  - Authentication
  - Real Time
  - Storage
  - Edge Functions
  - Database
url: https://raw.githubusercontent.com/api-evangelist/supabase/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: supabase:management-api
    name: Supabase Management API
    description: 'The Supabase Management API provides programmatic access to manage Supabase projects and organizations. Supports creating, configuring, pausing, and deleting projects; managing database migrations and extensions; deploying Edge Functions; managing secrets; configuring custom domains and vanity subdomains; controlling network restrictions; and managing organization membership. Authentication uses personal access tokens or OAuth2 tokens. Base URL: https://api.supabase.com/v1.'
    humanURL: https://supabase.com/docs/reference/api/introduction
    tags:
      - Management
      - Projects
      - Organizations
      - Edge Functions
      - Database
    properties:
      - type: Documentation
        url: https://supabase.com/docs/reference/api/introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supabase/refs/heads/main/openapi/supabase-management-api-openapi.yml
  - aid: supabase:auth-api
    name: Supabase Auth API
    description: 'The Supabase Auth API (based on GoTrue) is a JWT-based authentication service supporting user signup, email/password sign-in, magic links, one-time passwords (OTP), OAuth2 social login (Google, GitHub, etc.), token refresh, multi-factor authentication (TOTP/WebAuthn), SAML-based SSO, and administrative user management. Authentication uses an apikey header (anon or service_role key) plus JWT bearer tokens for user context. Per-project base URL: https://{project_ref}.supabase.co/auth/v1.'
    humanURL: https://supabase.com/docs/guides/auth
    tags:
      - Authentication
      - Users
      - OAuth
      - JWT
      - MFA
      - SAML
    properties:
      - type: Documentation
        url: https://supabase.com/docs/guides/auth
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supabase/refs/heads/main/openapi/supabase-auth-api-openapi.yml
  - aid: supabase:storage-api
    name: Supabase Storage API
    description: 'The Supabase Storage API enables developers to store, organize, and serve large files in S3-compatible object storage. Provides bucket management (public/private), file upload (standard and TUS resumable), download, deletion, and on-the-fly image transformations (resize, format, quality). Access control is enforced via Row Level Security policies. Supports signed URLs for temporary access. Per-project base URL: https://{project_ref}.supabase.co/storage/v1.'
    humanURL: https://supabase.com/docs/guides/storage
    tags:
      - Storage
      - File Upload
      - Buckets
      - Images
      - S3
    properties:
      - type: Documentation
        url: https://supabase.com/docs/guides/storage
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supabase/refs/heads/main/openapi/supabase-storage-api-openapi.yml
  - aid: supabase:database-rest-api
    name: Supabase Database REST API
    description: 'The Supabase Database REST API provides auto-generated RESTful endpoints for every table, view, and stored function in the PostgreSQL database, powered by PostgREST. Supports full CRUD operations with advanced filtering operators (eq, neq, gt, lt, like, ilike, in, fts, cs, cd, ov, adj, not, or, and), horizontal and vertical filtering, pagination, ordering, and embedding related resources via foreign key relationships. Row Level Security policies are enforced on all requests. Per-project base URL: https://{project_ref}.supabase.co/rest/v1.'
    humanURL: https://supabase.com/docs/guides/api
    tags:
      - Database
      - REST
      - PostgreSQL
      - PostgREST
      - CRUD
    properties:
      - type: Documentation
        url: https://supabase.com/docs/guides/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supabase/refs/heads/main/openapi/supabase-database-rest-api-openapi.yml
  - aid: supabase:edge-functions-api
    name: Supabase Edge Functions API
    description: 'Supabase Edge Functions are globally distributed, server-side TypeScript functions powered by the Deno runtime. They are deployed and invoked via HTTP requests to a project-specific URL. Functions can access Supabase client libraries to interact with the database, auth, and storage services. JWT verification is required by default but can be disabled per function. Per-project base URL: https://{project_ref}.supabase.co/functions/v1.'
    humanURL: https://supabase.com/docs/guides/functions
    tags:
      - Edge Functions
      - Serverless
      - Deno
      - TypeScript
    properties:
      - type: Documentation
        url: https://supabase.com/docs/guides/functions
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/supabase/refs/heads/main/openapi/supabase-edge-functions-api-openapi.yml
  - aid: supabase:realtime-api
    name: Supabase Realtime API
    description: 'The Supabase Realtime API provides WebSocket-based subscriptions for real-time data changes from PostgreSQL databases. It supports three channel types: database change events (INSERT/UPDATE/DELETE on tables via logical replication), presence (track and synchronize connected users'' state), and broadcast (low-latency message passing between clients). Authentication uses JWT tokens. Implemented using the Phoenix channels protocol.'
    humanURL: https://supabase.com/docs/guides/realtime
    tags:
      - Realtime
      - WebSocket
      - Database
      - Presence
      - Broadcast
    properties:
      - type: Documentation
        url: https://supabase.com/docs/guides/realtime
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/supabase/refs/heads/main/asyncapi/supabase-realtime-api-asyncapi.yml
common:
  - type: Website
    url: https://supabase.com
  - type: Documentation
    url: https://supabase.com/docs
  - type: GitHub Organization
    url: https://github.com/supabase
  - type: Status Page
    url: https://status.supabase.com
  - type: Pricing
    url: https://supabase.com/pricing
  - type: Blog
    url: https://supabase.com/blog
  - type: Community
    url: https://github.com/supabase/supabase/discussions
  - type: X
    url: https://twitter.com/supabase
  - type: Features
    data:
      - Hosted Postgres (1 GB Free, 8 GB Pro included)
      - PostgREST auto-generated REST API over your schema
      - Realtime API for Postgres replication and presence
      - Auth (email/password, OAuth, magic links, SAML SSO)
      - Storage (S3-compatible object store with policies)
      - Edge Functions (Deno-based, 500k free invocations)
      - Vector embeddings via pgvector
      - 'Free tier: 2 projects, auto-pause after 7 days'
      - Pro at $25/mo + usage (8GB DB, 100GB storage, 100k MAU)
      - Team at $599/mo with SOC 2, SSO, 14-day backups
      - Enterprise with HIPAA, BAA, dedicated infra
      - Storage overage $0.021/GB; egress $0.09/GB; MAU $0.00325 each
      - Extra micro compute add-on at $10/month
      - 'Auth signup rate limits: 30/hr Free, 150/hr Pro'
      - 'Realtime: 200 concurrent (Free), 500 (Pro)'
      - Read replicas, branching, and Vault add-ons
    sources:
      - https://supabase.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
