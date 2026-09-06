---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apache Httpd Agentic Access
  operation_count: 4
  slug: apache-httpd-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: Configuration directive reference for Apache HTTP Server covering VirtualHost, mod_ssl, mod_rewrite, mod_proxy, and all core directives for web server, proxy, and SSL configuration.
  name: Apache HTTP Server Configuration Reference
  slug: apache-httpd-config-api
- baseURL: http://localhost:80
  baseurl_source: declared
  description: Load balancer management
  name: Apache HTTP Server Balancer API
  slug: apache-httpd-balancer-api
- baseURL: http://localhost:80
  baseurl_source: declared
  description: Server status and metrics
  name: Apache HTTP Server Status API
  slug: apache-httpd-status-api
artifact_total: 46
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache HTTP Server Status Balancer API
  slug: open-apache-httpd-balancer-api
- collection_type: open
  name: Apache HTTP Server Balancer Status API
  slug: open-apache-httpd-status-api
- collection_type: open
  name: Apache HTTP Server Status API
  slug: open-apache-httpd-status
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/httpd/blob/trunk/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/httpd/blob/trunk/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-httpd-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-httpd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-httpd-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://httpd.apache.org/docs/current/
- group: start
  title: ''
  type: GettingStarted
  url: https://httpd.apache.org/docs/current/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/httpd
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-httpd-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-httpd-vocabulary.yaml
created: '2026-03-16'
description: Apache HTTP Server (httpd) is the world's most widely used web server software. It serves static and dynamic content, acts as a reverse proxy and load balancer, and exposes a mod_status monitoring API and balancer-manager management interface for operational visibility.
examples:
- key_count: 6
  name: Httpd Balancermember Example
  slug: httpd-balancermember-example
- key_count: 4
  name: Httpd Proxybalancer Example
  slug: httpd-proxybalancer-example
- key_count: 11
  name: Httpd Serverstatus Example
  slug: httpd-serverstatus-example
- key_count: 7
  name: Httpd Virtualhost Example
  slug: httpd-virtualhost-example
features:
- description: Real-time server status endpoint providing request rates, worker states, and CPU usage.
  name: mod_status Monitoring
- description: Full-featured reverse proxy with HTTP, HTTPS, WebSocket, and AJP protocol support.
  name: mod_proxy Reverse Proxy
- description: Load balancing across backend servers with byrequests, bytraffic, and bybusyness algorithms.
  name: mod_proxy_balancer Load Balancing
- description: TLS/SSL termination with client certificate authentication and OCSP stapling support.
  name: mod_ssl TLS Termination
- description: Powerful rule-based URL rewriting engine for redirects, proxying, and access control.
  name: mod_rewrite URL Rewriting
- description: Name-based and IP-based virtual hosting for serving multiple domains from a single server.
  name: Virtual Hosting
- description: CGI and FastCGI support for dynamic content generation with external applications.
  name: CGI and FastCGI
- description: Per-directory configuration files for decentralized access control and configuration.
  name: .htaccess Per-Directory Config
finops:
- name: Apache Httpd Finops
  service_category: API
  slug: apache-httpd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-httpd.png
integrations:
- description: Embeds PHP interpreter directly in the Apache process for PHP application hosting.
  name: mod_php
- description: AJP protocol integration with Apache Tomcat for Java web application proxying.
  name: Tomcat AJP Connector
- description: Automated TLS certificate provisioning with Certbot and the mod_md module.
  name: Let's Encrypt / Certbot
- description: Often deployed alongside Nginx, with Nginx handling static files and Apache handling dynamic content.
  name: Nginx
- description: ModSecurity web application firewall module for OWASP rule-based request filtering.
  name: ModSecurity WAF
json_schemas:
- name: BalancerMember
  property_count: 6
  slug: httpd-balancermember
- name: ProxyBalancer
  property_count: 4
  slug: httpd-proxybalancer
- name: ServerStatus
  property_count: 11
  slug: httpd-serverstatus
- name: VirtualHost
  property_count: 7
  slug: httpd-virtualhost
json_structures:
- name: Httpd Balancermember Structure
  property_count: 6
  slug: httpd-balancermember-structure
- name: Httpd Proxybalancer Structure
  property_count: 4
  slug: httpd-proxybalancer-structure
- name: Httpd Serverstatus Structure
  property_count: 11
  slug: httpd-serverstatus-structure
- name: Httpd Virtualhost Structure
  property_count: 7
  slug: httpd-virtualhost-structure
jsonld:
- class_count: 26
  name: Apache Httpd Status Context
  property_count: 0
  slug: apache-httpd-status-context
layout: provider
modified: '2026-05-19'
name: Apache HTTP Server
nav: Providers
network: true
overview: 'Apache HTTP Server publishes 2 APIs on the [APIs.io](https://apis.io/) network: Balancer API and Status API. Tagged areas include Apache, Load Balancer, Open-Source, Proxy, and Reverse Proxy.


  The Apache HTTP Server catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache HTTP Server''s developer surface includes documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Apache Httpd Plans Pricing
  plan_count: 3
  slug: apache-httpd-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Apache Httpd Rate Limits
  slug: apache-httpd-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache HTTP Server API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-httpd-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Apache HTTP Server API Rules
  rule_count: 11
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 7
  slug: apache-httpd-spectral-rules
score:
  band: thin
  composite: 34.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 52.4
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 50.0
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-httpd/refs/heads/main/screenshots/apache-httpd-2026-06-20T172105.png
security:
- kind: domain-security
  name: Apache Httpd Domain Security
  slug: apache-httpd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Httpd Vulnerability Disclosure
  slug: apache-httpd-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-httpd
tags:
- Apache
- Load Balancer
- Open-Source
- Proxy
- Reverse Proxy
- Web Server
use_cases:
- description: Serve HTML, CSS, JavaScript, and media files with high performance and caching headers.
  name: Static Web Hosting
- description: Proxy requests to application servers (Node.js, Python, Java) with SSL termination.
  name: Reverse Proxy for Applications
- description: Distribute traffic across multiple backend application instances with health checking.
  name: Load Balancing
- description: Route and transform API requests using mod_rewrite and mod_proxy rules.
  name: API Gateway
- description: Run legacy CGI or PHP applications via mod_cgi, mod_fcgid, or mod_php.
  name: Legacy CGI Application Hosting
---
