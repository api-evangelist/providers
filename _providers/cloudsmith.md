---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 229
  human_in_the_loop: 4
  name: Cloudsmith Agentic Access
  operation_count: 349
  slug: cloudsmith-agentic-access
  summary_line: 349 operations · 229 acting · 4 human-in-the-loop
api_count: 22
apis:
- description: The audit-log API from Cloudsmith — 2 operation(s) for audit-log.
  name: Cloudsmith audit-log API
  slug: cloudsmith-audit-log-api
- description: The badges API from Cloudsmith — 1 operation(s) for badges.
  name: Cloudsmith badges API
  slug: cloudsmith-badges-api
- description: The broadcasts API from Cloudsmith — 1 operation(s) for broadcasts.
  name: Cloudsmith broadcasts API
  slug: cloudsmith-broadcasts-api
- description: The bulk-action API from Cloudsmith — 1 operation(s) for bulk-action.
  name: Cloudsmith bulk-action API
  slug: cloudsmith-bulk-action-api
- description: The distros API from Cloudsmith — 2 operation(s) for distros.
  name: Cloudsmith distros API
  slug: cloudsmith-distros-api
- description: The entitlements API from Cloudsmith — 8 operation(s) for entitlements.
  name: Cloudsmith entitlements API
  slug: cloudsmith-entitlements-api
- description: The files API from Cloudsmith — 5 operation(s) for files.
  name: Cloudsmith files API
  slug: cloudsmith-files-api
- description: The formats API from Cloudsmith — 2 operation(s) for formats.
  name: Cloudsmith formats API
  slug: cloudsmith-formats-api
- description: The metrics API from Cloudsmith — 3 operation(s) for metrics.
  name: Cloudsmith metrics API
  slug: cloudsmith-metrics-api
- description: The namespaces API from Cloudsmith — 2 operation(s) for namespaces.
  name: Cloudsmith namespaces API
  slug: cloudsmith-namespaces-api
- description: The orgs API from Cloudsmith — 40 operation(s) for orgs.
  name: Cloudsmith orgs API
  slug: cloudsmith-orgs-api
- description: The packages API from Cloudsmith — 70 operation(s) for packages.
  name: Cloudsmith packages API
  slug: cloudsmith-packages-api
- description: The quota API from Cloudsmith — 4 operation(s) for quota.
  name: Cloudsmith quota API
  slug: cloudsmith-quota-api
- description: The rates API from Cloudsmith — 1 operation(s) for rates.
  name: Cloudsmith rates API
  slug: cloudsmith-rates-api
- description: The recycle-bin API from Cloudsmith — 2 operation(s) for recycle-bin.
  name: Cloudsmith recycle-bin API
  slug: cloudsmith-recycle-bin-api
- description: The repos API from Cloudsmith — 59 operation(s) for repos.
  name: Cloudsmith repos API
  slug: cloudsmith-repos-api
- description: The status API from Cloudsmith — 1 operation(s) for status.
  name: Cloudsmith status API
  slug: cloudsmith-status-api
- description: The storage-regions API from Cloudsmith — 2 operation(s) for storage-regions.
  name: Cloudsmith storage-regions API
  slug: cloudsmith-storage-regions-api
- description: The user API from Cloudsmith — 4 operation(s) for user.
  name: Cloudsmith user API
  slug: cloudsmith-user-api
- description: The users API from Cloudsmith — 1 operation(s) for users.
  name: Cloudsmith users API
  slug: cloudsmith-users-api
- description: The vulnerabilities API from Cloudsmith — 4 operation(s) for vulnerabilities.
  name: Cloudsmith vulnerabilities API
  slug: cloudsmith-vulnerabilities-api
- description: The webhooks API from Cloudsmith — 2 operation(s) for webhooks.
  name: Cloudsmith webhooks API
  slug: cloudsmith-webhooks-api
artifact_total: 31
collections:
- collection_type: open
  name: Cloudsmith API (v1)
  slug: open-cloudsmith
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudsmith-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudsmith-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudsmith-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudsmith
- group: company
  title: ''
  type: Website
  url: https://cloudsmith.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudsmith.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cloudsmith.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.cloudsmith.io/reference/getting-started-with-the-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudsmith.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudsmith.com/legal/privacy-notice/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudsmith-io
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/cloudsmith-openapi.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cloudsmith-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cloudsmith-rules.yml
created: '2024-01-01'
description: Cloudsmith is a cloud-native, universal package management platform providing fully managed, geo-replicated artifact repositories for over 30 package formats (Docker, npm, Maven, NuGet, PyPI, RubyGems, RPM, Deb, Helm, Cargo, Go, Composer, Conan, Conda, Vagrant, Raw, and more). The Cloudsmith REST API (v1) at api.cloudsmith.io exposes operations for organizations, repositories, packages, files, entitlements, vulnerabilities, webhooks, audit logs, metrics, quotas, deny policies, namespaces, distros, formats, recycle bin, storage regions, and broadcasts. Authentication is via API key passed in the Authorization header as "token YOUR_API_KEY".
finops:
- name: Cloudsmith Finops
  service_category: API
  slug: cloudsmith-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudsmith.png
jsonld:
- class_count: 0
  name: Cloudsmith Context
  property_count: 9
  slug: cloudsmith-context
layout: provider
modified: '2026-05-19'
name: Cloudsmith
nav: Providers
network: true
overview: 'Cloudsmith publishes 22 APIs on the [APIs.io](https://apis.io/) network, including audit-log API, badges API, broadcasts API, and 19 more. Tagged areas include Artifact Management, DevOps, DevSecOps, Distribution, and Package Management.


  The Cloudsmith catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudsmith''s developer surface includes authentication, documentation, API reference, getting-started guide, GitHub presence, and 9 more developer resources.'
plans:
- name: Cloudsmith Plans Pricing
  plan_count: 1
  slug: cloudsmith-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 2
  name: Cloudsmith Rate Limits
  slug: cloudsmith-rate-limits
rules:
- name: Cloudsmith API Rules
  rule_count: 14
  severity_counts:
    error: 4
    hint: 0
    info: 5
    warn: 5
  slug: cloudsmith-rules
score:
  band: developing
  composite: 46.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.6
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 27.1
    operational_transparency: 42.1
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudsmith/refs/heads/main/screenshots/cloudsmith-2026-06-20T174624.png
security:
- kind: authentication
  name: Cloudsmith Authentication
  slug: cloudsmith-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cloudsmith Domain Security
  slug: cloudsmith-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudsmith
tags:
- Artifact Management
- DevOps
- DevSecOps
- Distribution
- Package Management
- Registry
- Repository
- Software Supply Chain
- Universal
- Vulnerability Scanning
website: https://cloudsmith.com/
---
