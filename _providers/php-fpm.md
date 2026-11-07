---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Php Fpm Agentic Access
  operation_count: 2
  slug: php-fpm-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: http://localhost
  baseurl_source: declared
  description: PHP-FPM liveness check.
  name: PHP-FPM Ping API
  slug: php-fpm-ping-api
- baseURL: http://localhost
  baseurl_source: declared
  description: PHP-FPM pool status.
  name: PHP-FPM Status API
  slug: php-fpm-status-api
- description: Operational status endpoint exposed by PHP-FPM via the pm.status_path directive. Returns pool statistics (active processes, idle processes, accepted connections, slow requests) in plain text, JSON, XM
  name: PHP-FPM Status Endpoint
  slug: status-endpoint
artifact_total: 10
collections:
- collection_type: open
  name: PHP-FPM Status and Endpoints Ping API
  slug: open-php-fpm-ping-api
- collection_type: open
  name: PHP-FPM and Endpoints Ping Status API
  slug: open-php-fpm-status-api
- collection_type: open
  name: PHP-FPM Status and Ping Endpoints
  slug: open-php-fpm
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.php.net/feed.atom
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/php/php-src/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/php/php-src/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/php/php-src/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/php/php-src/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/php/php-src/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/php-fpm/agentic-access/php-fpm-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/php-fpm-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/php-fpm/security/php-fpm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/php-fpm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/php-fpm/security/php-fpm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/php-fpm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.php.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.php.net/manual/en/install.fpm.php
- group: other
  title: ''
  type: Download
  url: https://www.php.net/downloads.php
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/php/php-src
- group: operate
  title: ''
  type: Issue Tracker
  url: https://github.com/php/php-src/issues
created: '2026-05-11'
description: PHP-FPM (FastCGI Process Manager) is the primary PHP FastCGI implementation bundled with PHP for handling heavy-loaded sites, providing advanced process management with multiple worker pools, graceful start/stop, adaptive process spawning (static, dynamic, ondemand), slowlog tracking, and accelerated upload support. It is configured via php.ini-style pool files and is typically deployed behind a web server such as Nginx, Apache, Caddy, or LiteSpeed via FastCGI. PHP-FPM exposes operational status pages (in plain, JSON, XML, OpenMetrics, and HTML formats) but does not provide a public HTTP API; it runs only on POSIX systems that support fork().
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/php-fpm.png
layout: provider
modified: '2026-10-06'
name: PHP-FPM
nav: Providers
network: true
overview: 'PHP-FPM publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ping API, Status API, and 1 more. Tagged areas include PHP, FastCGI, Process-Manager, Web Server, and Application Server.


  The PHP-FPM catalog on APIs.io includes 1 Spectral governance ruleset.


  PHP-FPM''s developer surface includes documentation and 13 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: PHP-FPM API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: php-fpm-rules
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 42.9
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 31.6
  open_source:
    applies: true
    score: 85.0
  previous_composite: 29.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/php-fpm/php-fpm-2026-06-20T191655.png
security:
- kind: domain-security
  name: Php Fpm Domain Security
  slug: php-fpm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Php Fpm Vulnerability Disclosure
  slug: php-fpm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: php-fpm
tags:
- PHP
- FastCGI
- Process-Manager
- Web Server
- Application Server
- Open Source
website: https://www.php.net/
---
