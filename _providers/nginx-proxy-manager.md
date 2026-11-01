---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 42
  human_in_the_loop: 4
  name: Nginx Proxy Manager Agentic Access
  operation_count: 70
  slug: nginx-proxy-manager-agentic-access
  summary_line: 70 operations · 42 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: API for managing proxy hosts, certificates, and settings via HTTP endpoints.
  name: Nginx Proxy Manager API
  slug: nginx-proxy-manager-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Audit Log API from Nginx Proxy Manager — 2 operation(s) for audit log.
  name: Nginx Proxy Manager Audit Log API
  slug: nginx-proxy-manager-audit-log-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Logs API from Nginx Proxy Manager — 2 operation(s) for logs.
  name: Nginx Proxy Manager Logs API
  slug: nginx-proxy-manager-logs-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Nginx API from Nginx Proxy Manager — 26 operation(s) for nginx.
  name: Nginx Proxy Manager Nginx API
  slug: nginx-proxy-manager-nginx-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Nginx Proxy Manager API API from Nginx Proxy Manager — 1 operation(s) for nginx proxy manager api.
  name: Nginx Proxy Manager Nginx Proxy Manager API
  slug: nginx-proxy-manager-nginx-proxy-manager-api-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Reports API from Nginx Proxy Manager — 1 operation(s) for reports.
  name: Nginx Proxy Manager Reports API
  slug: nginx-proxy-manager-reports-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Schema API from Nginx Proxy Manager — 1 operation(s) for schema.
  name: Nginx Proxy Manager Schema API
  slug: nginx-proxy-manager-schema-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Settings API from Nginx Proxy Manager — 2 operation(s) for settings.
  name: Nginx Proxy Manager Settings API
  slug: nginx-proxy-manager-settings-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Tokens API from Nginx Proxy Manager — 2 operation(s) for tokens.
  name: Nginx Proxy Manager Tokens API
  slug: nginx-proxy-manager-tokens-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Users API from Nginx Proxy Manager — 8 operation(s) for users.
  name: Nginx Proxy Manager Users API
  slug: nginx-proxy-manager-users-api
- baseURL: http://127.0.0.1:81/api
  baseurl_source: spec
  description: The Version API from Nginx Proxy Manager — 1 operation(s) for version.
  name: Nginx Proxy Manager Version API
  slug: nginx-proxy-manager-version-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/nginx-proxy-manager/capabilities/nginx-proxy-manager-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nginx-proxy-manager-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/nginx-proxy-manager/agentic-access/nginx-proxy-manager-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nginx-proxy-manager-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/nginx-proxy-manager/rules/nginx-proxy-manager-rules.yml
  title: ''
  type: Spectral
  url: rules/nginx-proxy-manager-rules.yml
- group: design
  href: https://artifacts.apis.io/nginx-proxy-manager/vocabulary/nginx-proxy-manager-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nginx-proxy-manager-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nginx-proxy-manager/conformance/nginx-proxy-manager-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nginx-proxy-manager-conformance.yml
- group: other
  href: https://artifacts.apis.io/nginx-proxy-manager/hosts/nginx-proxy-manager-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nginx-proxy-manager-hosts.yml
- group: other
  href: https://artifacts.apis.io/nginx-proxy-manager/vendors/nginx-proxy-manager-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nginx-proxy-manager-vendors.yml
- group: build
  href: https://artifacts.apis.io/nginx-proxy-manager/packages/nginx-proxy-manager-packages.yml
  title: ''
  type: SDKs
  url: packages/nginx-proxy-manager-packages.yml
- group: build
  href: https://artifacts.apis.io/nginx-proxy-manager/packages/nginx-proxy-manager-packages.yml
  title: ''
  type: Packages
  url: packages/nginx-proxy-manager-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://nginxproxymanager.com/setup/
- group: auth
  href: https://artifacts.apis.io/nginx-proxy-manager/security/nginx-proxy-manager-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nginx-proxy-manager-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nginxproxymanager.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nginxproxymanager.com/guide/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/NginxProxyManager/nginx-proxy-manager
coverage:
  checked: '2026-10-28'
  detail: Provider documentation does not host a machine‑readable OpenAPI spec for the API.
  evidence:
  - status: 200
    url: https://nginxproxymanager.com/guide/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Nginx Proxy Manager is an open-source Docker-based web application that provides a simple, powerful interface for managing Nginx proxy hosts. It enables users to expose services securely with free SSL certificates from Let's Encrypt, supports custom Nginx configurations, and is designed with security in mind for home and small-business networks. The platform offers a user-friendly UI, Docker deployment, and community-driven development under the MIT license.
image: https://nginxproxymanager.com/icon.png
layout: provider
modified: '2026-10-28'
name: Nginx Proxy Manager
nav: Providers
network: true
overview: 'Nginx Proxy Manager publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit Log API, Logs API, Nginx API, and 8 more. Tagged areas include Company, OpenSource, Docker, Nginx, and Proxy.


  The Nginx Proxy Manager catalog on APIs.io includes 1 Spectral governance ruleset.


  Nginx Proxy Manager''s developer surface includes getting-started guide, documentation, and 12 more developer resources.'
plans:
- name: Nginx Proxy Manager Plans Pricing
  plan_count: 0
  slug: nginx-proxy-manager-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Nginx Proxy Manager Rate Limits
  slug: nginx-proxy-manager-rate-limits
rules:
- authorship: generated
  effective_rule_count: 44
  extends:
  - spectral:oas
  name: Nginx Proxy Manager API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: nginx-proxy-manager-rules
scopes:
- name: Nginx Proxy Manager Scopes
  scope_count: 0
  slug: nginx-proxy-manager-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 34.9
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nginx Proxy Manager Authentication
  slug: nginx-proxy-manager-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Nginx Proxy Manager Domain Security
  slug: nginx-proxy-manager-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nginx-proxy-manager
tags:
- Company
- OpenSource
- Docker
- Nginx
- Proxy
- SSL
website: https://nginxproxymanager.com/
---
