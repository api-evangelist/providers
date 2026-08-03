---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Php Fpm Agentic Access
  operation_count: 2
  slug: php-fpm-agentic-access
  summary_line: 2 operations
api_count: 3
apis:
- description: PHP-FPM liveness check.
  name: PHP-FPM Ping API
  slug: php-fpm-ping-api
- description: PHP-FPM pool status.
  name: PHP-FPM Status API
  slug: php-fpm-status-api
- description: Operational status endpoint exposed by PHP-FPM via the pm.status_path directive. Returns pool statistics (active processes, idle processes, accepted connections, slow requests) in plain text, JSON, XM
  name: PHP-FPM Status Endpoint
  slug: status-endpoint
artifact_total: 7
collections:
- collection_type: open
  name: PHP-FPM Status and Ping Endpoints
  slug: open-php-fpm
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/php-fpm-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/php-fpm-vulnerability-disclosure.yml
- group: auth
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
modified: '2026-07-25'
name: PHP-FPM
nav: Providers
network: true
overview: 'PHP-FPM publishes 2 APIs on the [APIs.io](https://apis.io/) network: Ping API and Status API. Tagged areas include PHP, FastCGI, Process Manager, Web Server, and Application Server.


  PHP-FPM''s developer surface includes documentation and 7 more developer resources.'
random_paper: 31
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 54.3
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 21.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/php-fpm/refs/heads/main/screenshots/php-fpm-2026-06-20T191655.png
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
- Process Manager
- Web Server
- Application Server
- Open Source
website: https://www.php.net/
---
