---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://apinity.io/'', ''status'': 301, ''note'': ''declared website redirects to https://bipro-service.gmbh/ — a different registrable domain (apinity.io -> bipro-service.gmbh), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: The Apinity API enables organizations to manage their compliant API marketplace programmatically, including API registration, discovery, subscription management, and governance policy enforcement acro
  name: Apinity.io API
  slug: apinity-io
artifact_total: 22
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/security/apinity-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apinity-io-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.apinity.io/
- group: operate
  title: ''
  type: Support
  url: https://docs.apinity.io/resources/get-help
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.apinity.io/release-notes/about-the-release-notes
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/changelog/apinity-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apinity-io-changelog.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/llms/apinity-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apinity-io-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/well-known/apinity-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apinity-io-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/well-known/apinity-io-openid-configuration.json
  title: ''
  type: OpenIDConnect
  url: well-known/apinity-io-openid-configuration.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/lifecycle/apinity-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apinity-io-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/conformance/apinity-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apinity-io-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/packages/apinity-io-packages.yml
  title: ''
  type: Packages
  url: packages/apinity-io-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/plans/apinity-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apinity-io-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/rate-limits/apinity-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apinity-io-rate-limits.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apinity-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apinity
- group: company
  title: ''
  type: Website
  url: https://apinity.io/
created: '2025-01-08'
description: Apinity empowers organisations to run their compliant API marketplace that simplifies integration, drives adoption, and secures governance. The platform provides tools for managing API lifecycle, enabling API discovery, enforcing compliance policies, and facilitating secure API-driven integrations across partner ecosystems.
examples:
- key_count: 9
  name: Apinity Marketplace Example
  slug: apinity-marketplace-example
features:
- description: Run a branded API marketplace that meets regulatory and compliance requirements for API sharing.
  name: Compliant API Marketplace
- description: Enable partners and teams to discover available APIs through a governed marketplace catalog.
  name: API Discovery
- description: Enforce governance policies across the API lifecycle from design through deprecation.
  name: API Governance
- description: Simplify partner integrations through standardized API access, documentation, and subscription management.
  name: Integration Simplification
- description: Track API adoption metrics and usage across marketplace subscribers.
  name: Adoption Tracking
finops:
- name: Apinity Io Finops
  service_category: API
  slug: apinity-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apinity-io.png
json_schemas:
- name: Apinity Marketplace API
  property_count: 9
  slug: apinity-marketplace
json_structures:
- name: Apinity Marketplace Structure
  property_count: 9
  slug: apinity-marketplace-structure
jsonld:
- class_count: 9
  name: Apinity Context
  property_count: 1
  slug: apinity-context
layout: provider
modified: '2026-09-18'
name: Apinity.io
nav: Providers
network: true
overview: 'Apinity.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Governance, API Marketplace, Compliance, Discovery, and Integration Platform.


  The Apinity.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Apinity.io''s developer surface includes documentation, support, changelog, and 13 more developer resources.'
plans:
- name: Apinity Io Plans Pricing
  plan_count: 0
  slug: apinity-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Apinity Io Rate Limits
  slug: apinity-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apinity.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apinity-io-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 28.0
    contract_quality: 18.7
    developer_ergonomics: 38.1
    discoverability: 75.9
    operational_transparency: 18.4
  previous_composite: 27.2
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/apinity-io/refs/heads/main/screenshots/apinity-io-2026-06-20T172250.png
security:
- kind: authentication
  name: Apinity Io Authentication
  slug: apinity-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Apinity Io Domain Security
  slug: apinity-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: apinity-io
solutions:
- description: Full-featured compliant API marketplace for partner and customer-facing API distribution.
  name: API Marketplace
- description: Enterprise-grade API governance and compliance tooling for regulated industries.
  name: Enterprise Governance
tags:
- API Governance
- API Marketplace
- Compliance
- Discovery
- Integration Platform
use_cases:
- description: Build and manage a governed API marketplace for sharing APIs with external partners and customers.
  name: Partner API Ecosystem
- description: Ensure API access and usage complies with regulatory requirements through policy enforcement.
  name: Regulatory Compliance
- description: Provide an internal marketplace for discovering and subscribing to internal APIs across teams.
  name: Internal API Catalog
- description: Monetize APIs through marketplace subscriptions and usage-based billing.
  name: API Monetization
website: https://apinity.io/
---
