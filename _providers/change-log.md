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
artifact_total: 31
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
description: An index and topic collection covering developer changelog publishing, release-notes platforms, and API change-tracking services. Change Log services help product, engineering, and developer-relations teams communicate releases, deprecations, and breaking changes to customers and integrators through structured changelog feeds, in-app widgets, and machine-readable diffs. This collection includes dedicated changelog publishing platforms like LaunchNotes, AnnounceKit, Beamer, and Canny, API specification diffing tools like oasdiff and Optic, and the broader ecosystem of API management and product-update platforms that expose changelog feeds, release notes, and version-tracking capabilities.
examples:
- key_count: 14
  name: Change Log Api Change Example
  slug: change-log-api-change-example
- key_count: 17
  name: Change Log Changelog Entry Example
  slug: change-log-changelog-entry-example
features:
- description: Dedicated platforms like LaunchNotes, AnnounceKit, and Beamer give product and developer-relations teams structured workflows to publish customer-facing changelog entries, release notes, and deprecation notices.
  name: Customer-Facing Changelog Publishing
- description: Tools like Beamer, Chameleon, and Userpilot embed changelog widgets and what-is-new notifications directly inside applications so users discover updates in context.
  name: In-App Release Widgets
- description: Spec-diff tools like oasdiff and Optic compare OpenAPI definitions across versions to detect breaking and non-breaking changes, generate structured changelogs, and gate releases in CI.
  name: API Specification Diffing
- description: Most changelog platforms expose RSS, Atom, JSON, or webhook feeds of release entries so other systems can react to releases programmatically.
  name: Release Notes Feeds and Webhooks
- description: Platforms like Canny, Productboard, and Aha tie changelog entries back to feedback, requests, and roadmap items so customers see the full lifecycle from idea to ship.
  name: Roadmap and Feedback Integration
- description: API management platforms like Kong, Tyk, Apigee, and Bump.sh track API versions and surface deprecations through documentation portals and machine-readable feeds.
  name: API Versioning and Deprecation Tracking
- description: Conventions like Keep a Changelog provide a stable Markdown structure (Added, Changed, Deprecated, Removed, Fixed, Security) widely adopted across open source and enterprise projects.
  name: Changelog Templates and Conventions
- description: Modern changelog platforms distribute the same release entry to email, in-app widgets, RSS, Slack, and developer portals, ensuring every audience sees the update through their preferred channel.
  name: Multi-Channel Release Communication
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Release communication platform for sharing changelogs, roadmaps, and deprecation notices with structured publishing workflows and a public API.
  name: LaunchNotes
- description: Changelog and release-notes platform with in-app widgets, email distribution, and segmented announcements for SaaS products.
  name: AnnounceKit
- description: In-app changelog and announcement platform that delivers what-is-new notifications, feedback collection, and NPS surveys via embedded widgets.
  name: Beamer
- description: Feedback management platform with a built-in changelog that closes the loop between user requests and shipped releases.
  name: Canny
- description: Open-source CLI that diffs OpenAPI specifications, detects breaking changes, and emits structured changelogs for CI pipelines.
  name: Oasdiff
- description: API change-management platform that captures API behavior, diffs OpenAPI specs, and produces governance-friendly changelogs.
  name: Optic
- description: API documentation and change-tracking platform that publishes versioned API docs and diff-based changelogs from OpenAPI and AsyncAPI specs.
  name: Bump.sh
- description: Issue tracker with a built-in changelog feature that publishes completed work to public release pages.
  name: Linear
json_schemas:
- name: APIChange
  property_count: 15
  slug: change-log-api-change
- name: ChangelogEntry
  property_count: 18
  slug: change-log-changelog-entry
json_structures:
- name: Change Log Api Change Structure
  property_count: 13
  slug: change-log-api-change-structure
- name: Change Log Changelog Entry Structure
  property_count: 17
  slug: change-log-changelog-entry-structure
jsonld:
- class_count: 9
  name: Change Log Context
  property_count: 25
  slug: change-log-context
layout: provider
modified: '2026-05-19'
name: Change Log
nav: Providers
network: true
overview: 'Change Log is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Changelog, Release Notes, API Versioning, Product Updates, and Spec Diff.


  The Change Log catalog on APIs.io includes 1 JSON-LD context.


  Change Log''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 13
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
slug: change-log
tags:
- Changelog
- Release Notes
- API Versioning
- Product Updates
- Spec Diff
- Deprecation
use_cases:
- description: API providers publish customer-facing changelogs of new endpoints, breaking changes, and deprecations on platforms like LaunchNotes or Bump.sh to keep integrators informed.
  name: Public API Changelog Publishing
- description: Engineering teams run oasdiff or Optic in CI to detect breaking changes between OpenAPI versions and block merges that would silently break consumers.
  name: Automated Breaking-Change Detection
- description: Product teams use Beamer, AnnounceKit, or Chameleon to show in-app changelog widgets that notify end users of new features without leaving the application.
  name: In-App Product Update Announcements
- description: Teams use Canny or Productboard to collect feedback, prioritize features, and then announce shipped work back to the same customers via a connected changelog.
  name: Customer Feedback to Release Loop
- description: API management platforms like Apigee, Kong, and SwaggerHub publish release notes alongside API documentation so developer portals stay current with each version.
  name: Developer Portal Release Notes
- description: Open source projects follow the Keep a Changelog convention and pair it with GitHub or GitLab releases to publish human-readable changelogs alongside semantic version tags.
  name: Open Source Release Documentation
- description: API teams use changelog platforms to announce upcoming deprecations, surface them through Deprecation HTTP headers, and track adoption of newer versions.
  name: Deprecation Lifecycle Communication
- description: Incident and status platforms like Statuspage combine system status with release notes so customers see both reliability and feature updates in one place.
  name: Customer-Facing Status and Release Notes
website: https://apievangelist.com
---
