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
description: An index and topic collection covering API versioning patterns, schema evolution, and breaking-change detection across the API lifecycle. API versioning communicates change to consumers, while schema versioning and diff tooling makes those changes explicit, reviewable, and reversible. This collection brings together versioning approaches like SemVer and CalVer, registry-driven schema evolution platforms (Apollo, Buf, Apicurio, Confluent Schema Registry), spec-diff tools (oasdiff, Optic, Bump.sh, GraphQL Inspector), API documentation versioning (Stoplight, Scalar, Bump.sh), versioning headers and sunsetting practices (Stripe API Versioning, Sunset Header), and dependency-versioning automation (Dependabot, Renovate, Conventional Commits).
examples:
- key_count: 12
  name: Versioning Api Version Example
  slug: versioning-api-version-example
- key_count: 11
  name: Versioning Breaking Change Example
  slug: versioning-breaking-change-example
features:
- description: Established conventions like SemVer (MAJOR.MINOR.PATCH) and CalVer (YYYY.MM) give API and library producers a shared vocabulary for communicating compatibility and release cadence to consumers.
  name: Semantic and Calendar Versioning
- description: Spec-diff tools like oasdiff, openapi-diff, Optic, and GraphQL Inspector compare two versions of an API specification and classify changes as breaking, non-breaking, or unclassified before they ship to production.
  name: Breaking Change Detection
- description: Platforms like Apicurio, Confluent Schema Registry, Buf Schema Registry, and Apollo GraphOS track every version of a schema, enforce compatibility rules (backward, forward, full), and prevent incompatible deploys.
  name: Schema Registries and Evolution
- description: Providers like Stripe and GitHub pin requests to a version via a header or date string, allowing the platform to ship new API behavior without breaking existing integrations.
  name: API Version Headers and Date-Based Versioning
- description: The Deprecation and Sunset HTTP headers (RFC 8594 / RFC 9745) and platform-level deprecation policies give consumers structured advance notice that an endpoint or version is going away.
  name: Deprecation and Sunsetting
- description: Tools like Bump.sh, Stoplight, Scalar, LaunchNotes, and Keep a Changelog publish per-version API references and human-readable release notes alongside the underlying spec or code change.
  name: Documentation and Changelog Versioning
- description: The Conventional Commits specification encodes change type (feat, fix, BREAKING CHANGE) directly in commit messages so that SemVer bumps and changelogs can be generated automatically.
  name: Conventional Commits and Release Automation
- description: Bots like Dependabot and Renovate continuously open pull requests to upgrade dependencies, respecting SemVer ranges and surfacing breaking changes upstream.
  name: Dependency Version Management
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Open-source CLI and library that compares two OpenAPI specifications and classifies every change as breaking or non-breaking, with rule-level configuration.
  name: Oasdiff
- description: API change-management platform that captures real traffic, generates OpenAPI, and gates pull requests on breaking changes against the existing spec.
  name: Optic
- description: API documentation and changelog platform that publishes per-version OpenAPI and AsyncAPI references and surfaces diffs between releases.
  name: Bump.sh
- description: Buf Schema Registry and CLI for Protocol Buffers, with first-class breaking-change detection and lint rules across proto versions.
  name: Buf
- description: Apollo GraphOS schema registry and Apollo Studio check every proposed GraphQL schema change against operations from real clients before publication.
  name: Apollo GraphQL
- description: Open-source schema registry from Red Hat for Avro, JSON Schema, OpenAPI, AsyncAPI, and Protobuf, with pluggable compatibility rules.
  name: Apicurio
- description: Stripe's date-based API versioning model pins every integration to a release date and provides a Versioning Stripe API reference for upgrading between versions.
  name: Stripe
- description: GitHub-native dependency-update automation that opens PRs for upgrades, respecting SemVer ranges and security advisories.
  name: Dependabot
- description: Configurable dependency upgrade bot with SemVer-aware grouping, scheduling, and automerge across npm, Maven, Docker, and many other ecosystems.
  name: Renovate
- description: Standard HTTP response header (RFC 8594) for communicating the date at which a resource will become unavailable, used together with Deprecation (RFC 9745).
  name: Sunset Header
json_schemas:
- name: APIVersion
  property_count: 12
  slug: versioning-api-version
- name: BreakingChange
  property_count: 11
  slug: versioning-breaking-change
json_structures:
- name: Versioning Api Version Structure
  property_count: 12
  slug: versioning-api-version-structure
- name: Versioning Breaking Change Structure
  property_count: 11
  slug: versioning-breaking-change-structure
jsonld:
- class_count: 7
  name: Versioning Context
  property_count: 21
  slug: versioning-context
layout: provider
modified: '2026-05-19'
name: Versioning
nav: Providers
network: true
overview: 'Versioning is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API Versioning, SemVer, CalVer, Schema Evolution, and Breaking Change.


  The Versioning catalog on APIs.io includes 1 JSON-LD context.


  Versioning''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
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
slug: versioning
tags:
- API Versioning
- SemVer
- CalVer
- Schema Evolution
- Breaking Change
- Deprecation
- Schema Registry
- Spec Diff
- Conventional Commits
- Sunset Header
use_cases:
- description: Run oasdiff or Optic in CI on every pull request that touches the OpenAPI spec and block the merge if breaking changes are introduced without an explicit major version bump.
  name: Pre-Merge Breaking Change Gate
- description: Issue per-account or per-request API versions (e.g. Stripe's 2024-04-10 versioning) so customer integrations remain stable while the platform iterates rapidly behind the scenes.
  name: Date-Pinned API Versions
- description: Producers and consumers of Kafka, gRPC, or GraphQL schemas register every revision in Apicurio, Confluent, Buf, or Apollo and the registry refuses incompatible changes at publish time.
  name: Schema Registry Compatibility Enforcement
- description: Publish v1, v2, and v3 documentation simultaneously through Bump.sh, Stoplight, or Scalar so consumers on older versions still have authoritative reference material.
  name: Multi-Version API Documentation
- description: Emit Deprecation and Sunset HTTP headers from deprecated endpoints, then track consumer migration through analytics before fully removing the version.
  name: Deprecation and Sunset Notification
- description: Use Conventional Commits plus tools like semantic-release to compute the next SemVer version, generate a changelog, tag the repo, and publish a release entirely from commit history.
  name: Automated SemVer Release
- description: Configure Dependabot or Renovate to open weekly PRs for dependency upgrades, with SemVer-aware grouping and automatic merge for non-breaking patches.
  name: Continuous Dependency Upgrades
- description: Publish a structured changelog through LaunchNotes, Beamer, or Keep a Changelog conventions so consumers can review what changed in every API release.
  name: API Changelog and Release Notes
website: https://apievangelist.com
---
