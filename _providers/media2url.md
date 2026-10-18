---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Media2Url Agentic Access
  operation_count: 1
  slug: media2url-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Media2URL Direct Media Delivery API
  name: Media2URL API
  slug: media2url-api
artifact_total: 9
asyncapis:
- description: ''
  name: Media2Url Webhooks
  slug: media2url-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/agentic-access/media2url-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/media2url-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/rate-limits/media2url-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/media2url-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/plans/media2url-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/media2url-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/rules/media2url-rules.yml
  title: ''
  type: Spectral
  url: rules/media2url-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/asyncapi/media2url-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/media2url-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/cli/media2url-cli.yml
  title: ''
  type: CLI
  url: cli/media2url-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/authentication/media2url-authentication.yml
  title: ''
  type: Authentication
  url: authentication/media2url-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/errors/media2url-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/media2url-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/conformance/media2url-conformance.yml
  title: ''
  type: Conformance
  url: conformance/media2url-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/well-known/media2url-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/media2url-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/well-known/media2url-gitlab-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/media2url-gitlab-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/well-known/media2url-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/media2url-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/well-known/media2url-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/media2url-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/hosts/media2url-hosts.yml
  title: ''
  type: Hosts
  url: hosts/media2url-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/vendors/media2url-vendors.yml
  title: ''
  type: Vendors
  url: vendors/media2url-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://media2url.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://media2url.com/dashboard/media
- group: start
  title: ''
  type: Login
  url: https://media2url.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheSourabhaSahu
- group: start
  title: ''
  type: DeveloperPortal
  url: https://media2url.com/dashboard/developer
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/security/media2url-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/media2url-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/media2url/refs/heads/main/security/media2url-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/media2url-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://media2url.com
- group: docs
  title: ''
  type: Documentation
  url: https://media2url.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://media2url.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://media2url.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://media2url.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://media2url.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://media2url.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://media2url.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://gitlab.com/sahukumarsonu/media2url-uploader-sdk
created: '2026-10-06'
description: Media2URL provides a direct media delivery platform that lets users upload images, videos, PDFs, audio, and other files and instantly obtain shareable direct URLs. The service includes tools for bulk uploads, custom domains, media library management, team workspaces, and integrations with platforms like Google Workspace, Zapier, Make, n8n, and Notion. It offers an API (base URL https://api.media2url.com/v1) secured with Bearer token authentication, supporting operations for usage stats, presigned upload URLs, finalizing uploads, and asset management.
image: https://media2url.com/og-image.png
layout: provider
modified: '2026-10-06'
name: Media2URL Direct Media Delivery API
nav: Providers
network: true
overview: 'Media2URL Direct Media Delivery API is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media, FileHosting, DirectLinks, and Upload.


  The Media2URL Direct Media Delivery API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Media2URL Direct Media Delivery API''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Media2Url Plans Pricing
  plan_count: 4
  slug: media2url-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 32
  name: Media2Url Rate Limits
  slug: media2url-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Media2URL Direct Media Delivery API API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: media2url-rules
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.5
    catalog_earned_first_party: 24.0
    catalog_gap: 54.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 59.5
    discoverability: 58.9
    operational_transparency: 55.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Media2Url Authentication
  slug: media2url-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Media2Url Domain Security
  slug: media2url-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Media2Url Vulnerability Disclosure
  slug: media2url-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: media2url
tags:
- Media
- FileHosting
- DirectLinks
- Upload
website: https://media2url.com
---
